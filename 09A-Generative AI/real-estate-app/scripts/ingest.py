"""Rebuild the Chroma collection from data/knowledge/.
Note: this also removes any web pages added through the app.

Run from the project root:  uv run python -m scripts.ingest
"""

from backend.app.ai.rag import get_vector_store, index_documents, load_guides

store = get_vector_store()
store.reset_collection()
print(f"Indexed {index_documents(store, load_guides())} chunks into '{store._collection.name}'")
