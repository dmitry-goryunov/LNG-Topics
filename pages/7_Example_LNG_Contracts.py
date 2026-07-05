import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from auth import check_password

st.set_page_config(page_title="Example LNG Contracts | LNG Topics", page_icon="📄", layout="wide")

if not check_password():
    st.stop()

LNG_CONTRACTS_URL = "https://lng-contracts-pa6739uczcskttekanjk9p.streamlit.app/"

st.title("📄 Example LNG Contracts")
st.caption(
    "A companion app — economic-terms comparison of real LNG Sale and Purchase Agreements, "
    "built from the source contracts and their comparison decks."
)

with st.container(border=True):
    st.subheader("LNG SPA Economic Terms Comparison")
    st.write(
        "Side-by-side economic comparison of two sets of real LNG SPAs, RAG-scored (red/amber/"
        "green) by commercial driver:\n"
        "- **Driftwood LNG** — Vitol, Gunvor, Shell SPA1 (JKM) and SPA2 (TTF)\n"
        "- **Cheniere Sabine Pass** — BG, Gas Natural Fenosa, GAIL, Total\n\n"
        "Each comparison is browsable slide-by-slide as the original PowerPoint deck (pricing "
        "formulas, volume/shape, credit terms, force majeure, appendix formula text as filed), "
        "alongside the full-text source SPAs. This is an economic comparison, not a legal "
        "blackline — redacted contract terms (`[***]`) are never inferred."
    )
    st.link_button("Open Example LNG Contracts ↗", LNG_CONTRACTS_URL, width="stretch", type="primary")

st.caption(f"Repo: [dmitry-goryunov/lng-contracts](https://github.com/dmitry-goryunov/lng-contracts)")
