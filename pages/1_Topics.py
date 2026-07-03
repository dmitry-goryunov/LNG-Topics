import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from auth import check_password
from pptx_reader import load_topics

st.set_page_config(page_title="Topics | LNG Topics", page_icon="📚", layout="wide")

if not check_password():
    st.stop()

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "LNG_Interview_Prep_Connected_Rev_2026-07-03.pptx"


@st.cache_data
def load(path: Path):
    return load_topics(path)


intro, sections = load(DATA_PATH)

st.title("📚 LNG Interview Prep Topics")
st.caption("Extracted directly from the source .pptx.")

titles = [t for t, _ in sections]
choice = st.sidebar.radio("Jump to topic", ["Overview"] + titles)

if choice == "Overview":
    st.markdown(intro)
else:
    body = dict(sections)[choice]
    st.markdown(body)
