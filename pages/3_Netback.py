import sys
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from auth import check_password

st.set_page_config(page_title="Netback | LNG Topics", page_icon="🚢", layout="wide")

if not check_password():
    st.stop()

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "netback.csv"


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Date (BST)"])
    return df.rename(columns={"Date (BST)": "Date"}).sort_values("Date").reset_index(drop=True)


df = load_data(DATA_PATH)
netback_cols = [c for c in df.columns if c != "Date"]

st.title("🚢 LNG Netback Prices by Destination Market")
st.caption("Source: netback.xls (Refinitiv).")

selected = st.multiselect("Markets to show", netback_cols, default=netback_cols)

fig = go.Figure()
for col in selected:
    fig.add_trace(go.Scatter(x=df["Date"], y=df[col], mode="lines", name=col.strip(), connectgaps=True))

fig.update_layout(
    title="LNG Netback Prices by Destination Market (USD/MMBtu)",
    xaxis_title="Date",
    yaxis_title="Netback Price (USD/MMBtu)",
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    template="plotly_white",
    height=650,
)
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(buttons=[
        dict(count=3, label="3m", step="month", stepmode="backward"),
        dict(count=6, label="6m", step="month", stepmode="backward"),
        dict(count=1, label="1y", step="year", stepmode="backward"),
        dict(step="all", label="All"),
    ]),
)
st.plotly_chart(fig, width='stretch')

with st.expander("Show raw data"):
    st.dataframe(df, width='stretch')
