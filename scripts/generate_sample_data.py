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

# Public GitHub copy only shows the LNG price forward curve up to May 2029.
MAX_DATE = pd.Timestamp("2029-05-31")


def random_walk(n, start, drift=0.0, vol=1.0, floor=0.0):
    steps = rng.normal(drift, vol, n)
    path = start + np.cumsum(steps)
    return np.clip(path, floor, None)


def trend(dates, anchors, floor=0.0):
    """Piecewise-linear interpolation through (date_str, value) anchor points."""
    xs = np.array([pd.Timestamp(d).value for d, _ in anchors], dtype=float)
    ys = np.array([v for _, v in anchors], dtype=float)
    x = dates.values.astype("datetime64[ns]").astype(np.int64).astype(float)
    return np.clip(np.interp(x, xs, ys), floor, None)


# ---------------------------------------------------------------------------
# 1. LNG prices sample (mirrors "LNG prices.xls" -> Data sheet)
#
# Shaped (not a pure random walk) to resemble real LNG/gas price history:
# the 2021-22 European gas crisis spike, 2023-24 normalization, current
# (mid-2026) levels anchored to the Topics deck's cited spot levels, then a
# 2027-29 decline consistent with the deck's "supply wave" scenario (Q7/Q11).
# ---------------------------------------------------------------------------
dates = pd.date_range("2021-07-01", periods=95, freq="MS")
n = len(dates)
cutover = 61  # index of 2026-07 -- where "historical" turns into "forward" curve

ttf_trend = trend(dates, [
    ("2021-07-01", 12), ("2021-10-01", 25), ("2021-12-01", 33),
    ("2022-03-01", 34), ("2022-06-01", 30), ("2022-08-01", 68),
    ("2022-10-01", 45), ("2023-01-01", 22), ("2023-06-01", 11),
    ("2023-12-01", 12), ("2024-06-01", 10), ("2024-12-01", 11.5),
    ("2025-06-01", 13), ("2026-01-01", 13.5), ("2026-07-01", 14.1),
    ("2027-01-01", 12), ("2027-07-01", 10), ("2028-01-01", 8.5),
    ("2028-07-01", 7.8), ("2029-05-01", 7.3),
], floor=2.0)

jkm_trend = trend(dates, [
    ("2021-07-01", 14), ("2021-10-01", 34), ("2021-12-01", 39),
    ("2022-03-01", 36), ("2022-06-01", 34), ("2022-08-01", 72),
    ("2022-10-01", 48), ("2023-01-01", 24), ("2023-06-01", 12.5),
    ("2023-12-01", 13.5), ("2024-06-01", 11), ("2024-12-01", 13),
    ("2025-06-01", 15), ("2026-01-01", 15.2), ("2026-07-01", 15.7),
    ("2027-01-01", 13.5), ("2027-07-01", 11.5), ("2028-01-01", 10),
    ("2028-07-01", 9.3), ("2029-05-01", 8.8),
], floor=2.5)

hh_trend = trend(dates, [
    ("2021-07-01", 3.7), ("2021-10-01", 5.5), ("2021-12-01", 3.8),
    ("2022-03-01", 4.9), ("2022-06-01", 7.5), ("2022-08-01", 9.0),
    ("2022-10-01", 6.5), ("2023-01-01", 3.5), ("2023-06-01", 2.2),
    ("2023-12-01", 2.6), ("2024-06-01", 2.0), ("2024-12-01", 2.8),
    ("2025-06-01", 3.4), ("2026-01-01", 3.6), ("2026-07-01", 3.3),
    ("2027-01-01", 3.6), ("2027-07-01", 3.8), ("2028-01-01", 4.0),
    ("2028-07-01", 4.2), ("2029-05-01", 4.3),
], floor=1.5)

jcc_trend = trend(dates, [
    ("2021-07-01", 10.4), ("2021-12-01", 11.7), ("2022-06-01", 13.5),
    ("2022-12-01", 15.5), ("2023-06-01", 14.0), ("2023-12-01", 12.5),
    ("2024-06-01", 11.0), ("2024-12-01", 10.3), ("2025-06-01", 10.0),
    ("2026-01-01", 10.2), ("2026-07-01", 10.4), ("2027-07-01", 10.6),
    ("2028-07-01", 10.8), ("2029-05-01", 11.0),
], floor=5.0)

lng_prices = pd.DataFrame({"Date (CEST)": dates})
lng_prices["JCC Indexed"] = np.round(jcc_trend + rng.normal(0, 0.1, n), 3)
lng_prices["Brent Indexed Historical"] = np.round(jcc_trend - 0.2 + rng.normal(0, 0.1, n), 3)
lng_prices[" NE Asia LNG spot"] = np.round(jkm_trend + rng.normal(0, 0.8, n), 3)
lng_prices["TTF front month hist"] = np.round(ttf_trend + rng.normal(0, 0.8, n), 3)
lng_prices["Henry Hub front month hist"] = np.round(hh_trend + rng.normal(0, 0.15, n), 3)
lng_prices["TTF forward"] = np.round(ttf_trend + rng.normal(0, 0.4, n), 3)
lng_prices["Henry Hub forward"] = np.round(hh_trend + rng.normal(0, 0.1, n), 3)
lng_prices["Brent Indexed forward"] = np.round(jcc_trend + 0.3 + rng.normal(0, 0.2, n), 3)
lng_prices["Nymex JKM swaps forward"] = np.round(jkm_trend + rng.normal(0, 0.4, n), 3)

# Emulate the real file: historical cols populated up to "today", forward
# cols appear starting ~1 year before "today" and continue to the last tenor.
hist_cols = ["JCC Indexed", "Brent Indexed Historical", " NE Asia LNG spot",
             "TTF front month hist", "Henry Hub front month hist"]
fwd_cols = ["TTF forward", "Henry Hub forward", "Brent Indexed forward", "Nymex JKM swaps forward"]
lng_prices.loc[lng_prices.index > cutover, hist_cols] = np.nan
lng_prices.loc[lng_prices.index < cutover - 12, fwd_cols] = np.nan
lng_prices.loc[0, ["JCC Indexed", "Brent Indexed Historical"]] = np.nan

lng_prices = lng_prices[lng_prices["Date (CEST)"] <= MAX_DATE]
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

netback = netback[netback["Date (BST)"] <= MAX_DATE]
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
