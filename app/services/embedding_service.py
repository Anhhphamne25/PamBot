import time
import httpx

from app.config import settings


def create_embedding(text: str) -> list[float]:
    payload = {
        "model": settings.EMBEDDINGS_MODEL,
        "input": text,
        "keep_alive": "30m",
    }

    last_error = None

    for attempt in range(5):
        try:
            response = httpx.post(
                settings.AI_API_EMBEDDINGS,
                json=payload,
                timeout=httpx.Timeout(
                    connect=10.0,
                    read=300.0,
                    write=10.0,
                    pool=10.0,
                ),
            )

            response.raise_for_status()
            data = response.json()

            print("ok")

            return data["embeddings"][0]

        except httpx.HTTPStatusError as e:
            last_error = e

            status_code = e.response.status_code
            print(f"Embedding API error {status_code}, retry {attempt + 1}/5...")

            if status_code == 504:
                time.sleep(10)
            else:
                raise

        except httpx.ReadTimeout as e:
            last_error = e
            print(f"Embedding read timeout, retry {attempt + 1}/5...")
            time.sleep(10)

    raise RuntimeError(f"Embedding failed after retries: {last_error}")