from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from app.config import settings

client = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY,
)

def create_collection_if_not_exists():
    collections = client.get_collections().collections
    collection_names = [collection.name for collection in collections]

    if settings.QDRANT_COLLECTION_NAME not in collection_names:
        client.create_collection(
            collection_name=settings.QDRANT_COLLECTION_NAME,
            vectors_config=VectorParams(
                size=settings.VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )

        print(f"Created collection: {settings.QDRANT_COLLECTION_NAME}")
    else:
        print(f"Collection already exists: {settings.QDRANT_COLLECTION_NAME}")

def upsert_chunks(points: list[PointStruct]):
    client.upsert(
        collection_name=settings.QDRANT_COLLECTION_NAME,
        points=points,
    )


def search_similar(vector: list[float], limit: int = 5):
    return client.search(
        collection_name=settings.QDRANT_COLLECTION_NAME,
        query_vector=vector,
        limit=limit,
    )