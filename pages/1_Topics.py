import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from auth import check_password
from pptx_reader import load_topics
from tools_data import tools_for_topic

TOOLS_PAGE = "pages/5_Tools.py"

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

query_topic = st.query_params.get("q")
if query_topic:
    match = next((t for t in titles if t.startswith(f"{query_topic}.")), None)
    if match and st.session_state.get("topic_choice") != match:
        st.session_state["topic_choice"] = match
    st.query_params.clear()

choice = st.sidebar.radio("Jump to topic", ["Overview"] + titles, key="topic_choice")

if choice == "Overview":
    st.markdown(intro)
else:
    q_number = choice.split(".", 1)[0]
    related_tools = tools_for_topic(q_number)
    if related_tools:
        with st.container(border=True):
            st.html(
                """
                <div style="background: linear-gradient(90deg,#6C63FF33,#00C2A833);
                            border-left: 6px solid #6C63FF; border-radius: 8px;
                            padding: 12px 16px; margin-bottom: 12px;">
                  <b>🧮 Numerical libraries for this topic</b><br/>
                  <span style="opacity:0.85;">Interactive numerical libraries that model this
                  topic's math in more depth — try them alongside the notes below.</span>
                </div>
                """
            )
            cols = st.columns(len(related_tools))
            for col, tool in zip(cols, related_tools):
                with col:
                    st.page_link(
                        TOOLS_PAGE,
                        label=f"🧮 {tool['title']}",
                        query_params={"tool": tool["slug"]},
                        width="stretch",
                    )
        st.divider()

    body = dict(sections)[choice]
    st.markdown(body)
