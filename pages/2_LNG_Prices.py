import sys
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from auth import check_password

st.set_page_config(page_title="LNG Prices | LNG Topics", page_icon="📈", layout="wide")

if not check_password():
    st.stop()

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "lng_prices_sample.csv"


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Date (CEST)"])
    return df.rename(columns={"Date (CEST)": "Date"}).sort_values("Date").reset_index(drop=True)


df = load_data(DATA_PATH)
price_cols = [c for c in df.columns if c != "Date"]

st.title("📈 LNG & Gas Price Benchmarks")
st.caption("Synthetic sample data — illustrative only, not real market prices.")

selected = st.multiselect("Series to show", price_cols, default=price_cols)

fig = go.Figure()
for col in selected:
    fig.add_trace(go.Scatter(x=df["Date"], y=df[col], mode="lines", name=col.strip(), connectgaps=True))

fig.update_layout(
    title="LNG & Gas Price Benchmarks (USD/MMBtu)",
    xaxis_title="Date",
    yaxis_title="Price (USD/MMBtu)",
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    template="plotly_white",
    height=600,
)
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(buttons=[
        dict(count=1, label="1y", step="year", stepmode="backward"),
        dict(count=3, label="3y", step="year", stepmode="backward"),
        dict(count=5, label="5y", step="year", stepmode="backward"),
        dict(step="all", label="All"),
    ]),
)
st.plotly_chart(fig, width='stretch')

st.subheader("Historical vs. forward curves")
hist_cols = [c for c in price_cols if "hist" in c.lower() or "indexed" in c.lower() or "spot" in c.lower()]
fwd_cols = [c for c in price_cols if c not in hist_cols]

fig2 = go.Figure()
for col in hist_cols:
    fig2.add_trace(go.Scatter(x=df["Date"], y=df[col], mode="lines", name=col.strip()))
for col in fwd_cols:
    fig2.add_trace(go.Scatter(x=df["Date"], y=df[col], mode="lines", name=col.strip(), line=dict(dash="dash")))

fig2.update_layout(
    title="Historical (solid) vs. Forward Curves (dashed)",
    xaxis_title="Date",
    yaxis_title="Price (USD/MMBtu)",
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    template="plotly_white",
    height=600,
)
fig2.update_xaxes(rangeslider_visible=True)
st.plotly_chart(fig2, width='stretch')

with st.expander("Show raw data"):
    st.dataframe(df, width='stretch')
