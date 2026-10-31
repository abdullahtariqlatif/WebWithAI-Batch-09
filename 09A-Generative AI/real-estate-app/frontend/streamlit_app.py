"""Streamlit UI.  Run:  uv run streamlit run frontend/streamlit_app.py
(the FastAPI backend must be running first)."""

import os
import uuid

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Real Estate AI", page_icon="🏠", layout="wide")
st.title("🏠 Real Estate AI Assistant")


def format_price(price: float, listing_type: str) -> str:
    if listing_type == "rent":
        return f"PKR {price:,.0f}/month"
    if price >= 10_000_000:
        return f"PKR {price / 10_000_000:.2f} crore"
    return f"PKR {price / 100_000:.1f} lakh"


with st.sidebar:
    st.caption(f"Backend: `{API_URL}`")
    try:
        health = requests.get(f"{API_URL}/health", timeout=3).json()
        st.success(f"API online · model `{health['llm_model']}`")
    except requests.RequestException:
        st.error("API offline — start the FastAPI backend first.")
        st.stop()

    st.header("📚 Knowledge base")
    st.caption("Add news articles or web pages — the assistant can then answer questions about them.")
    with st.form("add_urls", clear_on_submit=True):
        urls_text = st.text_area("Article URLs (one per line)", height=110)
        if st.form_submit_button("Add to knowledge base"):
            urls = [u.strip() for u in urls_text.splitlines() if u.strip()]
            if urls:
                with st.spinner(f"Reading {len(urls)} page(s)..."):
                    resp = requests.post(f"{API_URL}/knowledge/urls", json={"urls": urls}, timeout=300)
                if resp.ok:
                    for r in resp.json():
                        if r["ok"]:
                            st.success(f"Added **{r['title']}** ({r['chunks']} chunks)")
                        else:
                            st.error(f"{r['source']}: {r['error']}")
                else:
                    st.error(resp.json().get("detail", resp.text))

    sources = requests.get(f"{API_URL}/knowledge/sources", timeout=30).json()
    with st.expander(f"Indexed sources ({len(sources)})"):
        for src in sources:
            is_url = src["source"].startswith("http")
            label = f"[{src['title'] or src['source']}]({src['source']})" if is_url else src["source"]
            c1, c2 = st.columns([5, 1])
            c1.markdown(f"{label}  \n<small>{src['chunks']} chunks</small>", unsafe_allow_html=True)
            if is_url and c2.button("✕", key=src["source"], help="Remove from knowledge base"):
                requests.delete(f"{API_URL}/knowledge/sources", params={"source": src["source"]}, timeout=30)
                st.rerun()

def show_details(msg: dict) -> None:
    for tc in msg.get("tool_calls", []):
        st.caption(f"🔧 `{tc['name']}` {tc['args']}")
    if msg.get("sources"):
        links = [
            f"[{s['title'] or s['source']}]({s['source']})" if s["source"].startswith("http") else f"`{s['source']}`"
            for s in msg["sources"]
        ]
        st.caption("📄 Sources searched: " + " · ".join(links))


listings_tab, chat_tab = st.tabs(["Browse listings", "Ask the assistant"])

# ---------------- Listings (plain REST, no AI) ----------------
with listings_tab:
    c1, c2, c3, c4 = st.columns(4)
    city = c1.selectbox("City", ["", "Lahore", "Karachi", "Islamabad", "Rawalpindi"])
    listing_type = c2.selectbox("Buy / Rent", ["", "sale", "rent"])
    property_type = c3.selectbox("Type", ["", "house", "apartment", "condo", "townhouse", "plot"])
    min_bedrooms = c4.number_input("Min bedrooms", 0, 10, 0)

    params = {
        "city": city or None,
        "listing_type": listing_type or None,
        "property_type": property_type or None,
        "min_bedrooms": min_bedrooms or None,
    }
    listings = requests.get(f"{API_URL}/properties", params=params, timeout=10).json()
    st.caption(f"{len(listings)} listing(s)")

    for row_start in range(0, len(listings), 3):
        for col, p in zip(st.columns(3), listings[row_start : row_start + 3]):
            with col.container(border=True):
                st.subheader(p["title"])
                st.markdown(f"**{format_price(p['price'], p['listing_type'])}**")
                st.caption(f"#{p['id']} · {p['neighborhood']}, {p['city']} · {p['property_type']}")
                st.write(f"🛏 {p['bedrooms']} · 🛁 {p['bathrooms']:g} · 📐 {p['area_sqft']:,} sqft")
                with st.expander("Details"):
                    st.write(p["description"])
                    st.caption("Amenities: " + p["amenities"].replace(",", ", "))

# ---------------- Chat (LangGraph agent) ----------------
with chat_tab:
    if "thread_id" not in st.session_state:
        st.session_state.thread_id = str(uuid.uuid4())
        st.session_state.messages = []

    if st.button("New conversation"):
        st.session_state.thread_id = str(uuid.uuid4())
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            show_details(msg)

    prompt = st.chat_input("e.g. Find a 3-bed house in Lahore under 5 crore · or ask about an article you added")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"), st.spinner("Thinking..."):
            resp = requests.post(
                f"{API_URL}/chat",
                json={"message": prompt, "thread_id": st.session_state.thread_id},
                timeout=120,
            )
            if resp.ok:
                data = resp.json()
                msg = {"role": "assistant", "content": data["answer"], **data}
                st.markdown(msg["content"])
                show_details(msg)
                st.session_state.messages.append(msg)
            else:
                st.error(resp.json().get("detail", resp.text))
