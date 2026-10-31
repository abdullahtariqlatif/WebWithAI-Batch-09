"""RAG: load documents, chunk them, embed them, and search them.

Pipeline:  load (markdown files or web pages) -> split into chunks -> embed -> store in Chroma
           query -> embed -> find the most similar chunks -> give them to the LLM

The guides in data/knowledge/ are indexed once (when the collection is empty).
Web pages are added at runtime through POST /knowledge/urls.
After editing the guides or changing EMBEDDING_MODEL, rebuild with:  uv run python -m scripts.ingest
"""

from functools import lru_cache

import trafilatura
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from ..config import DATA_DIR, get_settings
from .llm import get_embeddings

KNOWLEDGE_DIR = DATA_DIR / "knowledge"


# ---------- Loading ----------
def load_guides() -> list[Document]:
    return [
        Document(page_content=path.read_text(), metadata={"source": path.name, "title": path.stem})
        for path in sorted(KNOWLEDGE_DIR.glob("*.md"))
    ]


def load_url(url: str) -> Document:
    """Download a web page and keep only the main article text (no menus, ads, footers)."""
    html = trafilatura.fetch_url(url)
    if html is None:
        raise ValueError("could not download the page")
    page = trafilatura.bare_extraction(html, url=url, with_metadata=True)
    if page is None or not page.text:
        raise ValueError("no article text found on the page")
    metadata = {"source": url, "title": page.title or url, "date": page.date or ""}
    return Document(page_content=page.text, metadata=metadata)


# ---------- Splitting + storing ----------
def split_documents(docs: list[Document]) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    return splitter.split_documents(docs)


@lru_cache
def get_vector_store() -> Chroma:
    s = get_settings()
    location = (
        # Chroma Cloud (https://trychroma.com)
        dict(chroma_cloud_api_key=s.chroma_api_key, tenant=s.chroma_tenant, database=s.chroma_database)
        if s.chroma_api_key
        # Local on-disk database
        else dict(persist_directory=s.chroma_persist_dir)
    )
    store = Chroma(collection_name=s.chroma_collection, embedding_function=get_embeddings(), **location)
    if not store.get(limit=1)["ids"]:
        index_documents(store, load_guides())
    return store


def index_documents(store: Chroma, docs: list[Document]) -> int:
    """(Re)index documents. Old chunks of the same source are removed first,
    so re-adding a page replaces it instead of creating duplicates."""
    for source in {d.metadata["source"] for d in docs}:
        remove_source(source, store)
    chunks = split_documents(docs)
    ids = [f"{c.metadata['source']}#{i}" for i, c in enumerate(chunks)]
    store.add_documents(chunks, ids=ids)
    return len(chunks)


def add_url(url: str) -> dict:
    doc = load_url(url)
    chunks = index_documents(get_vector_store(), [doc])
    return {"source": url, "title": doc.metadata["title"], "chunks": chunks}


def remove_source(source: str, store: Chroma | None = None) -> int:
    store = store or get_vector_store()
    ids = store.get(where={"source": source}, include=[])["ids"]
    if ids:
        store.delete(ids=ids)
    return len(ids)


def list_sources() -> list[dict]:
    """Everything currently in the knowledge base, one row per guide / web page."""
    sources: dict[str, dict] = {}
    for meta in get_vector_store().get(include=["metadatas"])["metadatas"]:
        row = sources.setdefault(meta["source"], {"source": meta["source"], "title": meta.get("title", ""), "chunks": 0})
        row["chunks"] += 1
    return sorted(sources.values(), key=lambda r: r["source"])


# ---------- Retrieval ----------
def retrieve(query: str, k: int = 4) -> list[Document]:
    return get_vector_store().similarity_search(query, k=k)
