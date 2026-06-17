import sys
from pathlib import Path
from uuid import uuid4

sys.path.append(str(Path(__file__).resolve().parents[1]))

from qdrant_client.models import PointStruct

from app.vectorstore.qdrant import create_collection_if_not_exists, upsert_chunks
from app.services.embedding_service import create_embedding
from app.utils.textloader import load_text_file
from app.utils.split_text import split_text


DATA_PATH = "data/personal_data.md"


def main():
    print("Starting PamBot ingest...")

    create_collection_if_not_exists()

    text = load_text_file(DATA_PATH)
    chunks = split_text(text)

    points = []

    for index, chunk in enumerate(chunks):
        vector = create_embedding(chunk)

        point = PointStruct(
            id=str(uuid4()),
            vector=vector,
            payload={
                "source": "personal_data.md",
                "chunk_index": index,
                "text": chunk,
            },
        )

        points.append(point)

    upsert_chunks(points)

    print(f"Ingested {len(points)} chunks into Qdrant.")


if __name__ == "__main__":
    main()