import json
import sys
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from auth import check_password

st.set_page_config(page_title="Fleet Portfolio | LNG Topics", page_icon="🚢", layout="wide")

if not check_password():
    st.stop()

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "fleet_results.json"


@st.cache_data
def load(path: Path, mtime: float) -> dict:
    return json.loads(path.read_text())


res = load(DATA_PATH, DATA_PATH.stat().st_mtime)
env, cfg = res["environment"], res["config"]

st.title("🚢 Fleet Portfolio Optimiser (lng-fleet-sim v8)")
st.caption(
    f"Generated artefact — lngfleet {env['package_version']}, numpy {env['numpy']}, "
    f"seed {cfg['seed']}, {cfg['n_paths']:,} paths, {env['generated_utc']}. "
    "Every number regenerates from code; nothing on this page is hand-typed."
)

# ── Strategy comparison ───────────────────────────────────────────────────────
st.subheader("Strategy comparison ($M, 90-day horizon, one cargo per ship)")
rows = []
for key, label in [
    ("fleet6_fixed", "6-ship fixed"), ("fleet6_two_stage", "6-ship two-stage"),
    ("fleet8_fixed", "8-ship fixed"), ("fleet8_two_stage", "8-ship two-stage"),
]:
    s = res["portfolio"][key]
    rows.append({
        "Strategy": label, "E[P&L]": round(s["mean"], 2), "Std": round(s["std"], 2),
        "P5": round(s["p5"], 2), "CVaR5": round(s["cvar"], 2),
        "CVaR 95% CI": f"[{s['cvar_ci']['lo']:.2f}, {s['cvar_ci']['hi']:.2f}]",
        "P95": round(s["p95"], 2),
    })
st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch")

u_m, u_c = res["uplift_fleet6"]["mean_paired"], res["uplift_fleet6"]["cvar_paired"]
st.markdown(
    f"Two-stage uplift (6-ship, common paths): E[P&L] **+${u_m['delta']:.2f}M** "
    f"[{u_m['lo']:.2f}, {u_m['hi']:.2f}]; CVaR **+${u_c['delta']:.2f}M** "
    f"[{u_c['lo']:.2f}, {u_c['hi']:.2f}]."
)

# ── Hedge sweep ───────────────────────────────────────────────────────────────
st.subheader("Tiered hedge sweep (6-ship, fixed routes)")
sw = pd.DataFrame(res["hedge_sweep_fleet6"])
fig = go.Figure()
fig.add_trace(go.Scatter(x=sw["committed_hr"], y=sw["mean"], name="E[P&L]", mode="lines"))
fig.add_trace(go.Scatter(x=sw["committed_hr"], y=sw["p5"], name="P5", mode="lines", line=dict(dash="dash")))
fig.add_trace(go.Scatter(x=sw["committed_hr"], y=sw["cvar"], name="CVaR5", mode="lines", line=dict(dash="dot")))
fig.update_layout(xaxis_title="Committed hedge ratio (swing tier scales 30–60%)",
                  yaxis_title="$M", template="plotly_white", height=450, hovermode="x unified")
st.plotly_chart(fig, width="stretch")
st.caption("Prices are martingales, so E[P&L] is ~flat in the hedge ratio; hedging buys tail, not mean.")

# ── Switch premia ─────────────────────────────────────────────────────────────
st.subheader("Destination-flexibility premia (swing ships)")
prem = pd.DataFrame(res["switch_premia"]).rename(columns={
    "name": "Ship", "default_dest": "Default", "per_mmbtu": "$/MMBtu (sim)",
    "bachelier_per_mmbtu": "$/MMBtu (Bachelier)", "open_leg_M": "Open-leg $M",
    "full_cargo_M": "Full-cargo $M", "switch_rate_two_stage": "Switch rate",
})
st.dataframe(prem, hide_index=True, width="stretch")
st.info(res["switch_premia_note"])

# ── Acquisition ───────────────────────────────────────────────────────────────
st.subheader("Acquisition case: Ship 7 + Ship 8 (charter basis: " + res["acquisition"]["charter_basis"] + ")")
a = res["acquisition"]
c1, c2, c3, c4 = st.columns(4)
c1.metric("Gross marginal E[P&L]", f"${a['gross_marginal']['mean']:.2f}M")
c2.metric("Charter + positioning", f"−${a['cost_M']:.2f}M",
          f"${a['tc_rate_usd_day']:,.0f}/day", delta_color="off")
c3.metric("Net marginal E[P&L]", f"${a['net_marginal']['mean']:.2f}M")
c4.metric("Break-even TC rate", f"${a['breakeven_tc_rate_usd_day']:,.0f}/day")
st.caption(a["note"] + f" Net marginal CVaR5: ${a['net_marginal']['cvar']:.2f}M.")

for w in res.get("warnings", []):
    st.warning(w)
