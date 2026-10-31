"""Tracing hooks.

- LangSmith needs no code: set LANGSMITH_TRACING=true + LANGSMITH_API_KEY in .env.
- Langfuse plugs in as a LangChain callback when its keys are set.
"""

from langchain_core.callbacks import BaseCallbackHandler

from ..config import get_settings


def get_callbacks() -> list[BaseCallbackHandler]:
    settings = get_settings()
    if settings.langfuse_public_key and settings.langfuse_secret_key:
        from langfuse.langchain import CallbackHandler

        return [CallbackHandler()]
    return []
