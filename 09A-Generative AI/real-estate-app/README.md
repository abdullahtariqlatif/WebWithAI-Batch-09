# 🏠 Real Estate AI Assistant

FastAPI backend + Streamlit frontend. An AI agent (LangChain + LangGraph) searches property
listings, calculates mortgages, and answers questions from a knowledge base (RAG).

```
Streamlit (frontend/)  ──HTTP──▶  FastAPI (backend/app/)
                                   ├── /properties         plain REST over SQLite (SQLModel)
                                   ├── /knowledge/urls     add web articles to the RAG index (POST)
                                   ├── /knowledge/sources  list (GET) / remove (DELETE) indexed sources
                                   ├── /knowledge/search   see what retrieval returns for a query
                                   └── /chat               LangGraph agent (Groq) ──▶ tools:
                                                             search_listings, get_property_details,
                                                             mortgage_calculator, search_knowledge_base (RAG)
                    RAG store: Chroma ← local Hugging Face embeddings
                    Tracing:   LangSmith (env vars only) · Langfuse (callback)
```

## Run it

```bash
cd "09A-Generative AI/real-estate-app"
uv sync                       # installs everything into .venv
cp .env.example .env          # then put your GROQ_API_KEY in .env

# terminal 1 — backend  (API docs: http://localhost:8000/docs)
uv run fastapi dev backend/app/main.py

# terminal 2 — frontend (http://localhost:8501)
uv run streamlit run frontend/streamlit_app.py
```

## What each key is for
| Service | Used for | Needed? |
|---|---|---|
| **Groq** (`GROQ_API_KEY`) | The LLM that powers the chat agent | Yes, for the chat tab |
| **Hugging Face** embedding model `BAAI/bge-small-en-v1.5` | Turning text into vectors for RAG — runs locally via FastEmbed | No key |
| **Chroma** (`CHROMA_API_KEY`, `CHROMA_TENANT`, `CHROMA_DATABASE`) | Vector store. Empty = local `./chroma_db`, filled = Chroma Cloud | Optional |
| LangSmith / Langfuse | Tracing | Optional |

The listings tab works with no keys at all. Swap the LLM by changing `LLM_MODEL`
(e.g. `groq:llama-3.3-70b-versatile`); other providers: `uv sync --extra anthropic` (or `google`, `ollama`).

## Try asking
- "Find me a 3-bed house in Lahore under 5 crore"
- "What's the monthly instalment on listing #1 with 30% down?"
- "What should I check before renting an upper portion?"  ← RAG
- "Compare DHA and Johar Town for a first-time buyer"     ← RAG + listings

**Web articles:** paste links in the sidebar's *Knowledge base* box, e.g. the CNBC articles from the
class demo, then ask *"What was the 30-year fixed mortgage rate, and on what date?"*. Each answer
lists the sources the agent searched.

## Where things live
| File | What it teaches |
|---|---|
| `backend/app/db.py` | SQLModel table, seeding, the shared `search_properties` query |
| `backend/app/ai/llm.py` | `init_chat_model` (Groq) + a custom `Embeddings` class for a local Hugging Face model |
| `backend/app/ai/rag.py` | load (files / web pages via trafilatura) → split → embed → Chroma → retrieve |
| `scripts/ingest.py` | rebuild the vector index from the guides (also clears added web pages) |
| `backend/app/ai/tools.py` | `@tool` functions the LLM can call; RAG tool returns sources as an *artifact* |
| `backend/app/ai/agent.py` | `create_agent` (a LangGraph graph) + memory via checkpointer |
| `backend/app/ai/observability.py` | Langfuse callback; LangSmith via env vars |
| `backend/app/routers/chat.py` | invoking the agent per `thread_id`, collecting tool calls + sources |
| `backend/app/routers/knowledge.py` | managing what's in the RAG index |
| `data/` | sample listings + markdown guides for RAG (illustrative, not real advice) |
