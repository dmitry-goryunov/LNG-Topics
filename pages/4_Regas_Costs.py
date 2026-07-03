import sys
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from auth import check_password

st.set_page_config(page_title="Regas Costs | LNG Topics", page_icon="🏭", layout="wide")

if not check_password():
    st.stop()

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "regas_costs.csv"


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


df = load_data(DATA_PATH)

st.title("🏭 European Hub LNG Delivery Economics")
st.caption("Snapshot as of 2026-07-01.")

st.subheader("Hub price vs. DES LNG price, and pre-regasification economics")
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Bar(x=df["Hub"], y=df["Hub Price"], name="Hub Price (EUR/MWh)"), secondary_y=False)
fig.add_trace(go.Bar(x=df["Hub"], y=df["ACER LNG DES Price"], name="ACER LNG DES Price (EUR/MWh)"), secondary_y=False)
fig.add_trace(
    go.Scatter(
        x=df["Hub"], y=df["Economics Pre-Regas (Hub-DES)"], name="Economics Pre-Regas (Hub-DES)",
        mode="lines+markers", line=dict(color="black", width=2),
    ),
    secondary_y=True,
)
fig.update_layout(
    title="European Hub LNG Delivery Economics",
    barmode="group",
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    template="plotly_white",
    height=600,
)
fig.update_yaxes(title_text="Price (EUR/MWh)", secondary_y=False)
fig.update_yaxes(title_text="Economics Pre-Regas (EUR/MWh)", secondary_y=True)
st.plotly_chart(fig, width='stretch')

st.subheader("Regas terminal utilization vs. contracted capacity")
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=df["Hub"], y=df["Contracted Capacity %"], name="Contracted Capacity (GIE) %"))
fig2.add_trace(go.Bar(x=df["Hub"], y=df["Regas Utilization %"], name="Regas Utilization %"))
fig2.update_layout(
    title="Regas Terminal Utilization vs. Contracted Capacity",
    yaxis_title="%",
    barmode="group",
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    template="plotly_white",
    height=600,
)
st.plotly_chart(fig2, width='stretch')

with st.expander("Show raw data"):
    st.dataframe(df, width='stretch')
