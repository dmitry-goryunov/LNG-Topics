import sys
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from auth import check_password

st.set_page_config(page_title="LNG Prices | LNG Topics", page_icon="📈", layout="wide")

if not check_password():
    st.stop()

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "lng_prices.csv"


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Date (CEST)"])
    return df.rename(columns={"Date (CEST)": "Date"}).sort_values("Date").reset_index(drop=True)


df = load_data(DATA_PATH)

EXPECTED_COLS = {
    "Date", "JCC Indexed", "Brent Indexed Historical", " NE Asia LNG spot",
    "TTF front month hist", "Henry Hub front month hist", "TTF forward",
    "Henry Hub forward", "Brent Indexed forward", "Nymex JKM swaps forward",
}
missing = EXPECTED_COLS - set(df.columns)
if missing:
    st.error(f"lng_prices.csv is missing expected column(s): {sorted(missing)}")
    st.stop()

price_cols = [c for c in df.columns if c != "Date"]

st.title("📈 LNG & Gas Price Benchmarks")
st.caption("Source: LNG prices.xls (Refinitiv).")

hist_cols = [c for c in price_cols if "hist" in c.lower() or "indexed" in c.lower() or "spot" in c.lower()]
fwd_cols = [c for c in price_cols if c not in hist_cols]

fig = go.Figure()
for col in hist_cols:
    fig.add_trace(go.Scatter(x=df["Date"], y=df[col], mode="lines", name=col.strip()))
for col in fwd_cols:
    fig.add_trace(go.Scatter(x=df["Date"], y=df[col], mode="lines", name=col.strip(), line=dict(dash="dash")))

fig.update_layout(
    title="Historical (solid) vs. Forward Curves (dashed)",
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

st.subheader("JKM − TTF spread (historical)")
spread = (df[" NE Asia LNG spot"] - df["TTF front month hist"]).rename("JKM−TTF")
sfig = go.Figure(go.Scatter(x=df["Date"], y=spread, mode="lines", name="JKM−TTF"))
sfig.add_hline(y=0, line_dash="dot")
sfig.add_vline(x="2026-03-01", line_dash="dash")
sfig.add_annotation(x="2026-03-01", y=1, yref="paper", yanchor="bottom",
                     text="Mar 2026 flip to Asian premium", showarrow=False)
sfig.update_layout(template="plotly_white", height=350, yaxis_title="USD/MMBtu")
st.plotly_chart(sfig, width="stretch")
st.caption("Q2/Q6 context: monthly averages drive flows; a snapshot can understate the pull.")

with st.expander("📐 Historical vols & correlations vs model assumptions"):
    hist = df.set_index("Date")[["Brent Indexed Historical", "Henry Hub front month hist",
                                 "TTF front month hist", " NE Asia LNG spot"]].dropna()
    r = np.log(hist).diff().dropna()
    vols = (r.std() * (12 ** 0.5)).round(2)
    st.write("Annualised vols (monthly data — indicative only):", vols.to_frame("σ").T)
    st.write("Log-return correlations:", r.corr().round(2))
    st.caption(
        "Model assumptions (lng-fleet-sim v8): σ Brent 0.28, HH 0.45, TTF 0.35, JKM 0.30; "
        "TTF–JKM ρ 0.75 normal / 0.40 stress. Monthly frequency gives noisy estimates and "
        "cannot resolve the stress regime — daily history is needed for real calibration."
    )

with st.expander("Show raw data"):
    st.dataframe(df, width='stretch')
