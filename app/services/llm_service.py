import httpx

from app.config import settings


def ask_llm(prompt: str) -> str:
    response = httpx.post(
        settings.AI_API_ASK,
        headers={
            "Content-Type": "application/json",
        },
        json={
            "model": settings.ASK_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "stream": False,
        },
        timeout=httpx.Timeout(
            connect=10.0,
            read=300.0,
            write=10.0,
            pool=10.0,
        ),
    )

    response.raise_for_status()
    data = response.json()

    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        raise ValueError(f"Unknown LLM response format: {data}")