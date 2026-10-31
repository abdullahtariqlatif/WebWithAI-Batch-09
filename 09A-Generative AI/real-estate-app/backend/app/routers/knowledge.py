"""Manage the RAG knowledge base: add web pages, list / remove sources, test retrieval."""

from fastapi import APIRouter, HTTPException
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel, Field, HttpUrl

from ..ai import rag

router = APIRouter(prefix="/knowledge", tags=["knowledge"])


class AddUrlsRequest(BaseModel):
    urls: list[HttpUrl] = Field(min_length=1, max_length=10)


class AddUrlResult(BaseModel):
    source: str
    ok: bool
    title: str = ""
    chunks: int = 0
    error: str = ""


@router.post("/urls", response_model=list[AddUrlResult])
async def add_urls(req: AddUrlsRequest):
    """Download each page, extract the article, chunk + embed it into Chroma.
    One bad URL doesn't fail the others."""
    results = []
    for url in map(str, req.urls):
        try:
            results.append(AddUrlResult(ok=True, **await run_in_threadpool(rag.add_url, url)))
        except Exception as exc:
            results.append(AddUrlResult(source=url, ok=False, error=str(exc)))
    return results


@router.get("/sources")
def list_sources():
    return rag.list_sources()


@router.delete("/sources")
def remove_source(source: str):
    removed = rag.remove_source(source)
    if not removed:
        raise HTTPException(404, "Source not found")
    return {"source": source, "chunks_removed": removed}


@router.get("/search")
def search(q: str, k: int = 4):
    """See exactly which chunks retrieval returns for a query."""
    return [{"metadata": d.metadata, "content": d.page_content} for d in rag.retrieve(q, k)]
