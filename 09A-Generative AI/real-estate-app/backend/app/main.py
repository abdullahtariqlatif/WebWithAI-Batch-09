"""FastAPI entry point.  Run:  uv run fastapi dev backend/app/main.py"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .config import get_settings
from .db import init_db
from .routers import chat, knowledge, properties


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Real Estate AI API", version="0.1.0", lifespan=lifespan)
app.include_router(properties.router)
app.include_router(knowledge.router)
app.include_router(chat.router)


@app.get("/health")
def health():
    return {"status": "ok", "llm_model": get_settings().llm_model}
