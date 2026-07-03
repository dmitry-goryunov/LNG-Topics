"""
Generates synthetic sample data used by the Streamlit app.

The real workbooks (LNG prices.xls, netback.xls) are Refinitiv-licensed
data and cannot be redistributed. This script produces fictitious data
with the same shape/columns so the app can be demoed publicly. Values
are random walks and are NOT real market prices.

Re-run with: python scripts/generate_sample_data.py
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)


def random_walk(n, start, drift=0.0, vol=1.0, floor=0.0):
    steps = rng.normal(drift, vol, n)
    path = start + np.cumsum(steps)
    return np.clip(path, floor, None)


# ---------------------------------------------------------------------------
# 1. LNG prices sample (mirrors "LNG prices.xls" -> Data sheet)
# ---------------------------------------------------------------------------
dates = pd.date_range("2021-07-01", periods=98, freq="MS")
n = len(dates)
cutover = 68  # index around which "historical" turns into "forward" curve

ttf_base = random_walk(n, start=12.0, drift=0.02, vol=2.5, floor=2.0)
hh_base = random_walk(n, start=3.8, drift=0.01, vol=0.5, floor=1.5)
jkm_base = ttf_base + rng.normal(2.0, 1.5, n)

lng_prices = pd.DataFrame({"Date (CEST)": dates})
lng_prices["JCC Indexed"] = np.round(random_walk(n, 10.5, 0.02, 0.15, 5), 3)
lng_prices["Brent Indexed Historical"] = np.round(lng_prices["JCC Indexed"] - rng.normal(0.2, 0.1, n), 3)
lng_prices[" NE Asia LNG spot"] = np.round(jkm_base, 3)
lng_prices["TTF front month hist"] = np.round(ttf_base, 3)
lng_prices["Henry Hub front month hist"] = np.round(hh_base, 3)
lng_prices["TTF forward"] = np.round(ttf_base + rng.normal(0, 0.8, n), 3)
lng_prices["Henry Hub forward"] = np.round(hh_base + rng.normal(0, 0.3, n), 3)
lng_prices["Brent Indexed forward"] = np.round(lng_prices["JCC Indexed"] + rng.normal(0, 0.5, n), 3)
lng_prices["Nymex JKM swaps forward"] = np.round(jkm_base + rng.normal(0, 0.6, n), 3)

# Emulate the real file: historical cols populated early, forward cols later
hist_cols = ["JCC Indexed", "Brent Indexed Historical", " NE Asia LNG spot",
             "TTF front month hist", "Henry Hub front month hist"]
fwd_cols = ["TTF forward", "Henry Hub forward", "Brent Indexed forward", "Nymex JKM swaps forward"]
lng_prices.loc[lng_prices.index >= cutover, hist_cols] = np.nan
lng_prices.loc[lng_prices.index < cutover - 20, fwd_cols] = np.nan
lng_prices.loc[0, ["JCC Indexed", "Brent Indexed Historical"]] = np.nan

lng_prices.to_csv("data/lng_prices_sample.csv", index=False)

# ---------------------------------------------------------------------------
# 2. Netback sample (mirrors "netback.xls" -> Data sheet)
# ---------------------------------------------------------------------------
weeks = pd.date_range("2025-01-06", periods=78, freq="W-MON")
m = len(weeks)
base = random_walk(m, start=12.5, drift=0.01, vol=0.8, floor=5)

countries = {
    "Japan": 0.0, "China": -0.1, "South Korea": 0.0, "Chinese Taipei": -0.05,
    "India": -0.3, "United Kingdom": 0.6, "France": 0.65, "Belgium": 0.6,
    "Spain": 0.5, "Turkey": 0.1, "Mexico (Altamira)": 0.9,
    "Mexico (Manzanillo)": 0.4, "Argentina": 0.1, "Brazil (Salvador)": 0.5,
    "Egypt (Ain Sukhna)": 0.55,
}

netback = pd.DataFrame({"Date (BST)": weeks})
for country, offset in countries.items():
    noise = rng.normal(0, 0.25, m)
    netback[country] = np.round(base + offset + noise, 3)

netback.to_csv("data/netback_sample.csv", index=False)

# ---------------------------------------------------------------------------
# 3. Regas costs sample (mirrors the "Regas Costs" snapshot table)
# ---------------------------------------------------------------------------
hubs = [
    ("Netherlands (TTF)", "Front Month"),
    ("France (PEG)", "Front Month"),
    ("Italy (PSV)", "Front Month"),
    ("Belgium (ZTP)", "Front Month"),
    ("United Kingdom (NBP)", "Front Month"),
    ("Germany (THE)", "Front Month"),
    ("Spain (PVB)", "Front Month"),
    ("Poland (VTP)", "Front Month"),
    ("Finland (FIN)", "Front Month"),
    ("Lithuania (LTU)", "Front Month"),
    ("Greece (HEE)", "Day Ahead"),
]

k = len(hubs)
des_price = np.round(rng.normal(42.5, 0.4, k), 3)
hub_price = np.round(des_price + rng.normal(1.5, 1.3, k), 2)

regas = pd.DataFrame({
    "Hub": [h[0] for h in hubs],
    "Contract Delivery": [h[1] for h in hubs],
    "Hub Price": hub_price,
    "ACER LNG DES Price": des_price,
    "Economics Pre-Regas (Hub-DES)": np.round(hub_price - des_price, 2),
    "Estimated Regas Cost": "Sample regas cost, EUR/MWh (illustrative)",
    "Voyage Cost Delta from Montoir": np.round(rng.normal(0.25, 0.35, k), 2),
    "Contracted Capacity %": rng.integers(35, 101, k),
    "Regas Utilization %": rng.integers(5, 121, k),
})

regas.to_csv("data/regas_costs_sample.csv", index=False)

print("Sample data written to data/*.csv")
