# 09A — Generative AI

Learning the LangChain ecosystem by building one project — **[real-estate-app](real-estate-app/)** —
and adding a tool at each step.

| # | Tool | What it is | Step in the real-estate app | Status |
|---|---|---|---|---|
| 1 | **LangChain** | Building blocks: models, prompts, tools, documents | `init_chat_model`, `@tool` functions | ✅ starter |
| 2 | **RAG** | Answer from your own documents via embeddings + vector search | `ai/rag.py`: Hugging Face embeddings + Chroma | ✅ starter |
| 3 | **LangGraph** | Stateful agent graphs with loops, memory, human-in-the-loop | `create_agent` + `InMemorySaver` | ✅ starter |
| 3b | **Groq** | Very fast hosted open-source LLMs (Llama, GPT-OSS) | default `LLM_MODEL` | ✅ starter |
| 3c | **Hugging Face LLMs** | Open models via HF Inference Providers or run locally | compare against Groq on the same questions | ⏳ next |
| 4 | **LangSmith** | Tracing, datasets and evals (LangChain's hosted platform) | set `LANGSMITH_TRACING=true` | ⚙️ configure |
| 5 | **Langfuse** | Open-source alternative to LangSmith (cloud or self-host) | set `LANGFUSE_*` keys | ⚙️ configure |
| 6 | **Deep Agents** | Agents that plan, use sub-agents and a virtual file system | a "property research report" agent | ⏳ next |
| 7 | **Langflow** | Visual drag-and-drop builder for LangChain flows | rebuild the RAG flow visually (`uvx langflow run`) | ⏳ next |

## Ideas for later steps
- Custom LangGraph `StateGraph` (router node → listings / RAG / mortgage branches) instead of `create_agent`
- Streaming tokens to Streamlit (`agent.stream(..., stream_mode="messages")` + Server-Sent Events)
- PDF ingestion into Chroma; compare embedding models from Hugging Face
- Structured output: extract search filters from free text with a Pydantic schema
- Persistent memory with `SqliteSaver` / `PostgresSaver`
- Evals in LangSmith/Langfuse: a dataset of questions with expected answers
- Human-in-the-loop: agent drafts a "book a viewing" request, user approves
