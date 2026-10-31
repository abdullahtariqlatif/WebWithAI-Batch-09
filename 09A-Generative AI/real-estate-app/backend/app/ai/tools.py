"""Tools the agent can call. The docstring + type hints of each function are
what the LLM sees, so they double as the tool's "prompt"."""

import json
from typing import Literal

from langchain_core.tools import tool
from sqlmodel import Session

from ..db import Property, engine, search_properties
from .rag import retrieve


@tool
def search_listings(
    city: str | None = None,
    property_type: Literal["house", "apartment", "condo", "townhouse", "plot"] | None = None,
    listing_type: Literal["sale", "rent"] | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    min_bedrooms: int | None = None,
) -> str:
    """Search property listings in the database. Prices are in PKR; for rentals
    the price is the monthly rent. Leave a filter empty to not filter on it."""
    with Session(engine) as session:
        results = search_properties(
            session, city, property_type, listing_type, min_price, max_price, min_bedrooms, limit=10
        )
        if not results:
            return "No listings matched those filters."
        return json.dumps([p.model_dump(exclude={"description"}) for p in results])


@tool
def get_property_details(property_id: int) -> str:
    """Get the full details (including description) of one listing by its id."""
    with Session(engine) as session:
        prop = session.get(Property, property_id)
        return prop.model_dump_json() if prop else f"No property with id {property_id}."


@tool
def mortgage_calculator(
    price: float, down_payment_percent: float = 20, annual_rate_percent: float = 12, years: int = 20
) -> str:
    """Estimate the monthly instalment for a home loan."""
    loan = price * (1 - down_payment_percent / 100)
    r = annual_rate_percent / 100 / 12
    n = years * 12
    monthly = loan / n if r == 0 else loan * r * (1 + r) ** n / ((1 + r) ** n - 1)
    return json.dumps(
        {
            "loan_amount": round(loan),
            "monthly_payment": round(monthly),
            "total_paid": round(monthly * n),
            "total_interest": round(monthly * n - loan),
        }
    )


@tool(response_format="content_and_artifact")
def search_knowledge_base(query: str) -> tuple[str, list[dict]]:
    """Search the knowledge base: guides about buying, renting, home financing and
    neighborhoods, plus any news articles / web pages the user has added.
    Use this for general real-estate and market questions, not for finding listings."""
    docs = retrieve(query)
    content = "\n\n---\n\n".join(
        f"[source: {d.metadata['source']} | {d.metadata.get('title', '')}]\n{d.page_content}" for d in docs
    )
    # The LLM only sees `content`; the artifact goes to our code (shown as sources in the UI).
    sources = [{"source": d.metadata["source"], "title": d.metadata.get("title", "")} for d in docs]
    return content, sources

TOOLS = [search_listings, get_property_details, mortgage_calculator, search_knowledge_base]
