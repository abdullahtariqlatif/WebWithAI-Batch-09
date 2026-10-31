"""App settings, loaded from the .env file in the project root."""

from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

# Put .env values into os.environ too — LangSmith, Langfuse and the provider
# SDKs (GROQ_API_KEY, ...) read their settings straight from the environment.
load_dotenv(PROJECT_ROOT / ".env")


class Settings(BaseSettings):
    llm_model: str = "groq:openai/gpt-oss-120b"
    embedding_model: str = "fastembed:BAAI/bge-small-en-v1.5"
    database_url: str = f"sqlite:///{PROJECT_ROOT / 'real_estate.db'}"

    # Chroma: Chroma Cloud when an API key is set, otherwise a local folder.
    chroma_api_key: str | None = None
    chroma_tenant: str | None = None
    chroma_database: str | None = None
    chroma_collection: str = "real_estate_knowledge"
    chroma_persist_dir: str = str(PROJECT_ROOT / "chroma_db")

    langfuse_public_key: str | None = None
    langfuse_secret_key: str | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()
