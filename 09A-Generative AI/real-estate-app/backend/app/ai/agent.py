"""The real-estate agent: an LLM in a LangGraph loop that can call tools.

`create_agent` builds a LangGraph graph:  model -> (tool calls?) -> tools -> model -> ... -> answer
The checkpointer stores each conversation by `thread_id`, giving the agent memory.
"""

from functools import lru_cache

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from .llm import get_llm
from .tools import TOOLS

SYSTEM_PROMPT = """You are a friendly, honest real-estate assistant for properties in Pakistan.

- Use `search_listings` to find properties and `get_property_details` for more detail.
  Never invent listings — only mention properties a tool returned, with their id.
- Use `mortgage_calculator` for any instalment / affordability question.
- Use `search_knowledge_base` for questions about buying, renting, financing, areas,
  or market news (it also holds web articles the user added). Answer only from what it
  returns, and name the guide or article you used. If it has nothing relevant, say so.
- Prices are in PKR. Format them readably (e.g. PKR 3.2 crore, PKR 120,000/month).
- If the user's request is vague, ask a short clarifying question (city, budget, buy or rent)."""


@lru_cache
def get_agent():
    return create_agent(
        model=get_llm(),
        tools=TOOLS,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=InMemorySaver(),
    )
