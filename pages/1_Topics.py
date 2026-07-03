import re
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Topics | LNG Topics", page_icon="📚", layout="wide")

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "topics.md"


@st.cache_data
def load_sections(path: Path):
    text = path.read_text(encoding="utf-8")
    # Split on level-2 headers ("## ..."), keeping the header text as the title.
    parts = re.split(r"\n(?=## )", text)
    intro = parts[0]
    sections = []
    for part in parts[1:]:
        title = part.splitlines()[0].removeprefix("## ").strip()
        sections.append((title, part))
    return intro, sections


intro, sections = load_sections(DATA_PATH)

st.title("📚 LNG Interview Prep Topics")

titles = [t for t, _ in sections]
choice = st.sidebar.radio("Jump to topic", ["Overview"] + titles)

if choice == "Overview":
    st.markdown(intro)
else:
    body = dict(sections)[choice]
    st.markdown(body)
