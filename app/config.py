from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    QDRANT_URL: str
    QDRANT_API_KEY: str
    QDRANT_COLLECTION_NAME: str = "pambot_personal_info"

    VECTOR_SIZE: int 

    AI_API_EMBEDDINGS: str
    EMBEDDINGS_MODEL: str
    AI_API_ASK: str
    ASK_MODEL: str

    class Config:
        env_file = ".env"


settings = Settings()