# LNG Topics

A Streamlit app collecting LNG structuring/trading topic notes alongside
interactive charts on LNG prices, netbacks, and European regasification economics.

## Pages

- **Topics** — curve construction, benchmarks (Henry Hub / TTF / JKM), European
  regas capacity valuation, complex transaction structures, US FOB netback,
  destination flexibility / diversion optionality, portfolio valuation
  assumptions, shipping economics, quantitative techniques for embedded
  optionality, market/legal/execution risk, portfolio stress testing, and the
  ETRM / risk-reporting interface.
- **LNG Prices** — historical and forward price curves (JCC, Brent, TTF, Henry
  Hub, JKM).
- **Netback** — weekly LNG netback prices by destination market/port.
- **Regas Costs** — European hub delivery economics and regas terminal
  utilization.
- **Tools** — links to related interactive numerical libraries (XVA/CVA,
  spread-option hedging, diversion optionality, fleet optimisation, storage
  valuation), cross-linked with the Topics they support.
- **Fleet Portfolio** — generated results from the `lng-fleet-sim` v8 Monte
  Carlo engine (`data/fleet_results.json`): strategy comparison, hedge
  sweep, destination-flexibility premia, and an acquisition case.

## Data

The charts use the real underlying data:

- `data/lng_prices.csv` — from `LNG prices.xls` (Refinitiv).
- `data/netback.csv` — from `netback.xls` (Refinitiv).
- `data/regas_costs.csv` — a European hub delivery-economics snapshot as of 2026-07-01.

Note: `LNG prices.xls` and `netback.xls` carry a Refinitiv redistribution
restriction under their subscription terms; these CSV exports are published
here on the basis that redistribution is authorized. If that's ever not the
case, swap `data/lng_prices.csv` and `data/netback.csv` for synthetic or your
own licensed data (same column names) and update the captions in
`pages/2_LNG_Prices.py` / `pages/3_Netback.py` accordingly.

The Topics page is parsed directly from the source deck,
[`data/LNG_Structuring_Trading_Topics_Rev_2026-07-03.pptx`](data/LNG_Structuring_Trading_Topics_Rev_2026-07-03.pptx),
via `pptx_reader.py` — there's no separate hand-maintained copy, so editing
the deck and redeploying is enough to update the app. The notes cite dated
market levels from public sources (IEA, Reuters/LSEG, Shell, EIA, ICE) — not
resold data. They are not trading advice.

## Access

The app is gated behind a shared password (see `auth.py`). This is a soft
gate meant to keep casual visitors out, not real access control — since the
repo is public, the fallback password (`"pass"`) is visible in source. Set an
`app_password` secret in Streamlit Cloud's Secrets manager (or a local
`.streamlit/secrets.toml`, gitignored) to override it.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy

The app is ready for [Streamlit Community Cloud](https://streamlit.io/cloud):
point it at this repo with `app.py` as the entry point.
