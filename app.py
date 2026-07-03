import streamlit as st

from auth import check_password

st.set_page_config(
    page_title="LNG Topics",
    page_icon="🛢️",
    layout="wide",
)

if not check_password():
    st.stop()

st.title("🛢️ LNG Topics")

st.markdown(
    """
Welcome — this app collects LNG structuring/trading interview-prep notes alongside
interactive charts on LNG prices, netbacks and European regasification economics.

**Use the sidebar to navigate:**

- **📚 Topics** — curve construction, benchmarks, regas, transaction structures,
  netbacks, optionality, shipping, quant methods, risk and stress testing.
- **📈 LNG Prices** — historical and forward price curves (JCC, Brent, TTF, Henry
  Hub, JKM).
- **🚢 Netback** — weekly LNG netback prices by destination market/port.
- **🏭 Regas Costs** — European hub delivery economics and regas terminal
  utilization.

> **Data note:** the charts in this app use **synthetic sample data** generated to
> match the shape of the original (Refinitiv-licensed) source files. The values are
> illustrative only and do not reflect real market prices — see `scripts/generate_sample_data.py`.
> The Topics notes cite dated market levels from public sources (IEA, Reuters/LSEG,
> Shell, EIA, ICE); they are prepared notes, not resold data, and are not trading advice.
"""
)
