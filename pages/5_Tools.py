import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from auth import check_password
from tools_data import TOOLS

st.set_page_config(page_title="Tools | LNG Topics", page_icon="🧰", layout="wide")

if not check_password():
    st.stop()

st.title("🧰 Related Tools & Simulators")
st.caption(
    "These are interactive **numerical libraries** — small apps that go deeper on specific "
    "quant methods referenced in the Topics."
)

TOPICS_PAGE = "pages/1_Topics.py"

highlight_slug = st.query_params.get("tool")
if highlight_slug:
    st.query_params.clear()

for tool in TOOLS:
    is_highlighted = tool["slug"] == highlight_slug
    with st.container(border=True):
        if is_highlighted:
            st.success("You jumped here from a Topic reference.")
        st.subheader(tool["title"])

        st.caption("Related topics:")
        cols = st.columns([1] * len(tool["related"]) + [3])
        for col, (q, label) in zip(cols, tool["related"]):
            with col:
                st.page_link(
                    TOPICS_PAGE,
                    label=f"{q} — {label}",
                    query_params={"q": q},
                )

        st.write(tool["description"])
        st.link_button(f"Open {tool['title']} ↗", tool["url"], width="stretch", type="primary")
