"""Chat model + embeddings, chosen by the LLM_MODEL / EMBEDDING_MODEL settings.

`init_chat_model("groq:openai/gpt-oss-120b")` lets you swap providers without
touching any other code — e.g. "groq:llama-3.3-70b-versatile" or "openai:gpt-5-mini".
"""

from functools import lru_cache

from langchain.chat_models import init_chat_model
from langchain.embeddings import init_embeddings
from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel

from ..config import get_settings


class FastEmbedEmbeddings(Embeddings):
    """Runs a Hugging Face embedding model locally with FastEmbed (ONNX, CPU-only).

    The model (~130 MB) is downloaded from the Hugging Face Hub on first use.
    An `Embeddings` class only needs these two methods to work with any vector store.
    """

    def __init__(self, model_name: str):
        from fastembed import TextEmbedding

        self.model = TextEmbedding(model_name)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [vector.tolist() for vector in self.model.embed(texts)]

    def embed_query(self, text: str) -> list[float]:
        return next(iter(self.model.query_embed(text))).tolist()


@lru_cache
def get_llm() -> BaseChatModel:
    return init_chat_model(get_settings().llm_model)


@lru_cache
def get_embeddings() -> Embeddings:
    provider, _, model = get_settings().embedding_model.partition(":")
    if provider == "fastembed":
        return FastEmbedEmbeddings(model)
    return init_embeddings(get_settings().embedding_model)
