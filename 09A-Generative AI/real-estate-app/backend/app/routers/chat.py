"""Chat with the LangGraph agent."""

from fastapi import APIRouter, HTTPException
from langchain_core.messages import AIMessage, ToolMessage
from pydantic import BaseModel

from ..ai.agent import get_agent
from ..ai.observability import get_callbacks

router = APIRouter(tags=["ai"])


class ChatRequest(BaseModel):
    message: str
    thread_id: str = "default"


class ToolCall(BaseModel):
    name: str
    args: dict


class Source(BaseModel):
    source: str
    title: str = ""


class ChatResponse(BaseModel):
    answer: str
    tool_calls: list[ToolCall]
    sources: list[Source]


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    config = {"configurable": {"thread_id": req.thread_id}, "callbacks": get_callbacks()}
    try:
        result = get_agent().invoke(
            {"messages": [{"role": "user", "content": req.message}]}, config
        )
    except Exception as exc:  # surface provider / API-key errors to the UI
        raise HTTPException(500, f"{type(exc).__name__}: {exc}") from exc

    # Only look at what happened for *this* message, not earlier turns.
    messages = result["messages"]
    turn = messages[max(i for i, m in enumerate(messages) if m.type == "human") :]

    tool_calls = [
        ToolCall(name=tc["name"], args=tc["args"])
        for m in turn
        if isinstance(m, AIMessage)
        for tc in m.tool_calls
    ]
    # Sources come from the RAG tool's artifact (see tools.search_knowledge_base).
    sources = {
        s["source"]: Source(**s)
        for m in turn
        if isinstance(m, ToolMessage) and m.name == "search_knowledge_base" and m.artifact
        for s in m.artifact
    }
    return ChatResponse(answer=messages[-1].text, tool_calls=tool_calls, sources=list(sources.values()))
