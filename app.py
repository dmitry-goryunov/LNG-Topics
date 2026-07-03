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
- **🧰 Tools** — interactive **numerical libraries** for XVA/CVA, spread-option
  hedging, diversion optionality, LNG fleet optimisation and storage
  valuation, each tied back to the relevant Topic.

> **Data note:** the price charts use the real underlying data (`LNG prices.xls`,
> `netback.xls`, and a regas-cost snapshot). The Topics notes cite dated market
> levels from public sources (IEA, Reuters/LSEG, Shell, EIA, ICE); they are
> prepared notes, not resold data. Nothing here is trading advice.
"""
)
