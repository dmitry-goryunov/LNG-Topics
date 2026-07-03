# LNG Structuring and Trading: Key LNG-Related Topics

**LNG Structuring and Trading**
Core topics: curve construction, benchmarks, regas, netbacks, optionality, shipping, transaction risk, stress testing and ETRM / risk reporting interface.

*Prepared 1 July 2026; revised 3 July 2026 after validation audit. Market figures are date-specific; worked values are illustrative and should be checked against live curves, freight and assessment data before use. Not trading advice.*

---

## Q1. DES NWE forward curve construction and marking

### Construction

- Backbone: ICE TTF futures settlements; DES NWE marked as a basis to TTF (regas slot value, entry capacity, port costs), normally a discount that widens when regas is loose
- Front 12–24 months: observable DES markers where available (Spark NWE DES, Platts DES NWE, Argus), broker quotes and executed cargo trades
- Beyond the liquid window: seasonal shape from TTF plus a modelled basis (regas utilisation, storage cost, supply wave timing)
- Sanity bounds every tenor: curve must sit inside the diversion arbitrage corridor (see below)
- DES NWE is therefore TTF-led, location-adjusted and arbitrage-constrained, not mechanically equal to TTF plus a fixed spread

### Marking and governance

- Observability hierarchy: exchange settles, then broker quotes and trades, then assessed markers, then model marks with reserves
- Independent price verification monthly; bid–offer and liquidity reserves grow with tenor
- Back-test marks against the portfolio's own executed DES cargoes
- Document basis methodology; recalibrate after regime shifts (2022, 2026)

> **Caution:** Subject to the current Platts methodology, DES NWE marks should be treated as normalised physical cargo assessments rather than literal single-cargo trade prints. Underlying bids, offers and trades may differ by volume, delivery window, port optionality, quality and other commercial terms within the methodology. For curve marking, Platts DES NWE should be used as one front-end observable, and reconciled against TTF, local hub basis, executed cargoes and the portfolio's own physical evidence.

### Ceiling and floor

| Bound | Rule | Level (late June 2026) |
|---|---|---|
| Ceiling | JKM minus incremental freight east — above this, cargoes divert to Asia and DES NWE cannot clear higher | Date-specific: calculate as JKM minus incremental freight / timing / operational penalty |
| Floor | US-linked short-run lifting economics — broadly 115% Henry Hub plus variable liquefaction / fuel and destination shipping costs; below this, flexible US cargoes may be cancelled or turned down where the contract permits | TTF near $14, HH near $3.3 |

---

## Q2. Henry Hub, TTF and JKM: benchmark relationships and European LNG pricing

**Henry Hub** — US domestic gas benchmark and cost anchor for US FOB LNG. Full-cycle US LNG economics are often framed as 115% HH plus tolling and variable costs. For short-run lifting or cancellation decisions, the fixed toll may be sunk, so the relevant floor is closer to variable feedgas, liquefaction / fuel and shipping economics.

**TTF** — Europe's dominant continental hub and the main hedge / monetisation benchmark for DES NWE LNG. European DES cargoes are usually valued as a physical basis to TTF, but not on a TTF-only basis: NBP, PVB/MIBGAS, PEG/TRF, THE, PSV and ZTP matter where delivery or monetisation is local. Oil indexation is marginal for European spot / DES LNG pricing, but still relevant in legacy and portfolio SPAs.

**JKM** — Asian spot marker. Competes with TTF for every flexible Atlantic cargo; JKM minus TTF net of freight steers diversions.

- European netback minus US short-run lifting cost = variable margin of flexible US LNG; when negative, cancellation or turndown rights may create a soft floor where contracts permit
- JKM minus TTF (net of freight) allocates flexible supply between basins; March 2026 flip to a ~$2.8 Asian premium pulled cargoes east
- In a glut, Europe absorbs surplus into storage and TTF can converge toward the HH-linked US LNG short-run cost floor; in a squeeze, TTF must outbid JKM for reloads and flexible cargoes

**Spot levels, late June / early July 2026 ($/MMBtu, dated snapshot):** Henry Hub c.3.3, TTF c.14.1, JKM c.15.7. Use exact source dates when quoting. **June 2026 monthly averages:** JKM 17.33 vs TTF 13.19 (LSEG via Reuters) — a ~$4.1 Asian premium. The monthly average is the flow-relevant measure: it pushed Europe's share of US LNG exports below half in June for the first time since July 2024.

---

## Q3. European regasification capacity and terminal-slot valuation

### Value = strip of spread options

- Per slot: expected value of max(hub forward value of regasified gas minus DES LNG cost minus variable regas cost, 0)
- Intrinsic: today's forward local hub versus DES basis net of tariff, entry costs and losses. TTF is the main NWE hedge, but NBP, PVB/MIBGAS, PEG/TRF, THE, PSV and ZTP matter where delivery or monetisation is local
- Extrinsic: volatility of that basis; 2022 and 2026 crises are the proof that scarcity states dominate the value
- Ancillary: tank storage play, reload and re-export rights, truck loading, berthing flexibility
- Strategic: security-of-supply and the option to land portfolio length; valued by portfolio simulation, not standalone

Formal form, summed over delivery periods *t* with discount factor *DF*, contracted volume *Q*, and fixed capacity fees separated out:

V = E[ Σₜ DFₜ · max(Hubₜ − DESₜ − VariableRegasₜ − Entryₜ − Lossesₜ, 0) · Qₜ ] − Σₜ DFₜ · FixedFeesₜ

### Method and calibration

- Model as a spread option or Monte Carlo on the relevant local hub versus DES, with send-out limits, berth windows, boil-off, entry costs and tariff structure. TTF remains the main NWE hedge, but local hub basis matters where delivery differs
- Respect use-it-or-lose-it and third-party access rules; haircut for slot inflexibility and nomination deadlines
- Calibrate to observables: secondary capacity trades and auction results (Gate, Zeebrugge, Grain, German FSRUs)
- Cross-check: implied basis vol from TTF options plus historic DES basis; stress with the 2022 scarcity regime

*Current regime: with Europe structurally long regas since 2023, merchant intrinsic value is thin in aggregate; most of the price is optionality and insurance. The qualification is terminal- and regime-specific: aggregate European slack does not eliminate value at constrained or well-located terminals (Q1 2026: nine EU terminals ran above 80% utilisation while nine ran below 30%).*

---

## Q4. Complex LNG transaction structures: selected examples

| Transaction type | Commercial issue | Key risk | Structuring solution | Structuring / valuation contribution |
|---|---|---|---|---|
| Mid-term DES SPA with force majeure linked to specific seller facilities | Buyer wanted delivered LNG supply, but seller's FM wording was linked to multiple seller facilities rather than a clean generic FM standard. | The FM wording could allow the seller to allocate a supply shortfall disproportionately to this buyer, even where the seller had other unaffected facilities or portfolio supply available. | Recast the clause so that FM-related shortfall was allocated pro-rata across affected supply / customers, with clearer causation, mitigation and allocation language. The aim was to avoid discretionary allocation of the whole shortfall against one buyer. | Identified that the FM clause created hidden volume optionality in favour of the seller. Quantified downside supply loss and helped move the contract towards a fairer pro-rata allocation mechanism. |
| Long-term Brent-linked SPA with cap / floor around TTF-equivalent level | SPA economics were primarily Brent-linked, while European monetisation and risk management were closer to TTF. | Long-dated Brent / TTF basis risk and limited hedge liquidity beyond the liquid tenor. Pure financial hedging would be expensive, incomplete or unavailable. | Introduced contractual cap / floor mechanics around a TTF-equivalent level to bound the exposure and reduce reliance on long-dated external hedges. | Helped convert an open-ended index mismatch into a defined risk corridor. Supported the commercial case by showing reduced tail risk, lower hedge dependency and clearer approval limits. |
| SPA with future ramp-up period | Contracted supply started in the future with uncertain COD, ramp-up profile and available volumes. | Fixed long-term pricing during ramp-up could misprice start-up uncertainty; buyer/seller could be locked into volumes and prices before production reliability was proven. | Use spot or market-linked pricing during the ramp-up period, with the long-term formula applying only after defined commercial operation / reliability milestones. | Separated commissioning risk from steady-state contract economics. Reduced valuation uncertainty by treating ramp-up volumes as short-term market exposure rather than full long-term baseload supply. |
| Portfolio SPA package with cooling-off / approval period | Portfolio transaction required a cooling-off or internal approval period between bid and binding commitment. | Market could move materially during the cooling-off period, leaving the buyer or seller exposed to stale pricing. | Lower the bid to compensate for the option granted during the cooling-off period, or introduce a tracker / price-adjustment mechanism linked to agreed market markers. | Framed the cooling-off period as an embedded option. Quantified market-move exposure and proposed either an option discount or a transparent tracker to keep economics aligned until execution. |

---

## Q5. US FOB cargo netback: Europe versus Asia

**Europe:** NB(EU) = TTF (or DES NWE) − freight USG→NWE − regas and entry costs − losses

**Asia:** NB(Asia) = JKM − freight USG→Asia (Panama or Cape route: hire, fuel, boil-off, canal) − losses

**Illustrative netback, late June 2026 ($/MMBtu):** Europe ≈ 12.8–13.1, Asia ≈ 13.0–13.5 on the dated spot snapshot. On June monthly-average prices (TTF 13.19, JKM 17.33) the eastward pull was unambiguous, consistent with observed June flows.

- Illustrative inputs: TTF 14.1, JKM 15.7 (late-June snapshot); freight ranges ~$0.7–1.0/MMBtu to NWE (~12 days one way) and ~$1.9–2.4/MMBtu to North Asia via Cape (~28 days), depending on route, vessel, boil-off and charter-rate assumptions. Late-June 2026 Spark rates sat at the top of these ranges; verify against live freight quotes
- Decision rule: lift to the higher netback; the JKM premium must cover the extra voyage cost, exactly what the post-crisis ~$2.8 spread did
- Europe versus Asia is the core comparison, but the commercial decision is the highest netback across all feasible destinations: Egypt / North Africa, the Middle East and Latin America can clear above the European netback (June 2026: record Egyptian purchases of US LNG at premiums up to $1/MMBtu over TTF-linked prices)
- Cancellation / turndown rule: if the best destination netback is below the avoidable short-run US lifting cost, test whether turndown or cancellation rights can be exercised. For short-run cargo decisions, the fixed toll may be sunk; the relevant floor is variable feedgas, variable liquefaction / fuel and variable shipping costs
- Use DES NWE if valuing a delivered LNG sale. Use TTF or the relevant local hub if monetising regasified gas. Adjust for local basis, regas, entry costs and losses
- Mind second-order terms: Panama waiting time, charter market when extending voyages, working capital and hedge roll

---

## Q6. Destination flexibility and diversion optionality

### What the option is

- An FOB cargo with shipping is an option on the best of several basin netbacks: max(JKM − freight_A, TTF − freight_E, local sale)
- Value drivers: JKM–TTF spread volatility, imperfect correlation between hubs, freight volatility, and contractual freedom (destination clauses, notice windows)
- High hub correlation kills the value; regime breaks (2022, 2026) restore it violently
- Where the US offtake / tolling structure permits cargo cancellation or turndown, that right behaves like a put struck at avoidable variable cost. It should be valued alongside destination flexibility, because diversion helps when one basin is better than another, while turndown helps when all destinations are below lifting economics

Margin form: Cargo value = max(NB(E) − K, NB(A) − K, 0), where K is the avoidable variable lifting cost.

### How to value it

- Spread-option pricing (Margrabe/Kirk) for two-basin snapshots
- Correlated Monte Carlo of TTF, JKM and freight curves with exercise windows and notice constraints for the portfolio
- Least-squares Monte Carlo where decisions are sequential (divert now vs keep the option alive)
- Arbitrage windows can close quickly: the March 2026 window shut within roughly two weeks as the spread renormalised. This is why exercise windows, notice constraints and freight–spread correlation belong in the valuation — freight tends to firm when the arb opens, dampening realised diversion margin
- Backtest: realised diversion P&L is the ultimate calibration of modelled option value
- Portfolio effect: flexibility is worth more inside a book holding shipping, regas and storage than standalone

*Asian premium +$2.8/MMBtu over TTF (Mar 2026): the diversion option paying out — flexible cargoes swung east within weeks (IEA).*

---

## Q7. Key assumptions in LNG portfolio valuation

1. **Flat price and spread deck** — The biggest driver is the long-run relationship between TTF, JKM, Henry Hub, Brent-linked formulas and freight. Key spreads are JKM-TTF, TTF minus US LNG variable cost, and JKM minus US LNG variable cost. These determine whether the portfolio is structurally long, short, in-the-money, or dependent on optionality.
2. **Demand elasticity and market absorption** — The same LNG supply wave has very different price impact depending on whether Asian demand responds quickly to lower prices. If China, India and South / South-East Asia absorb cheap LNG, the downside is limited. If demand is infrastructure-, credit- or policy-constrained, the supply wave depresses prices more severely.
3. **Supply-wave timing and availability** — Start-up dates, ramp-up curves, feedgas constraints, maintenance and outages can reshape the curve. A six-month delay in new liquefaction capacity can keep the market tight through the affected season; an early ramp can push Europe into surplus and weaken DES / TTF basis.
4. **Volatility and TTF-JKM correlation** — These drive the value of destination flexibility, diversion rights, regas slots, storage and US turndown rights. High correlation reduces normal-market option value, but regime breaks such as 2022 and 2026 can make the optionality pay out sharply.
5. **Freight and vessel availability** — Freight converts a theoretical spread into an executable arbitrage. The relevant signal is not simply JKM minus TTF, but JKM minus TTF minus incremental freight, canal costs, voyage time, boil-off and operational penalties.
6. **Regas, storage and terminal access** — European LNG length only has value if it can be landed, stored, reloaded or sent out. Firm regas rights, berth windows, tank capacity, send-out rates, reload rights and local hub basis can make two otherwise similar portfolios worth very different amounts.
7. **Contractual, credit and performance assumptions** — Destination clauses, cargo cancellation or turndown rights, delivery-window flexibility, quantity tolerance under multi-cargo SPAs where applicable, force majeure, start-up delay, counterparty performance, collateral and PFE can dominate the valuation. An option has little value if the contract does not allow exercise or the counterparty cannot perform.
8. **Financial assumptions** — Discount rate, FX, inflation indexation, liquidity reserves, margining and funding costs matter especially for long-dated SPAs, tolling arrangements and infrastructure-linked deals.

- **3.8% → 2.2%** — one LSEG outlook comparison cut global LNG import CAGR by c.40% between the Jun-24 and Apr-25 vintages. The risk is not the valuation formula; it is the demand-growth assumption
- **Supply shock sensitivity** — Shell's 2026 global LNG export-growth outlook swings materially between a pre-crisis baseline and a prolonged Strait of Hormuz disruption case. The point is that supply availability and disruption duration can dominate the curve deck

---

## Q8. LNG shipping economics, chartering and vessel optimisation

### Freight is a netback input, not a constant

Freight should be built from the ground up and expressed in $/MMBtu delivered, not only in $/day:

Freight ($/MMBtu) = (day rate × voyage days + fuel + boil-off + canal + port + insurance + war risk + other) / delivered MMBtu

### Cost build

- Charter hire: spot versus term charter; day rate depends on vessel type, market balance and positioning
- Vessel efficiency: modern two-stroke vessels such as ME-GI / X-DF usually have better fuel and boil-off economics than older steam / TFDE tonnage, but the premium must be tested against the route and cargo value
- Voyage economics: round-trip days, ballast leg, speed, fuel consumption, boil-off, heel, cool-down, port costs, canal fees, insurance and war-risk premia
- Delivered volume: a standard cargo is often modelled around 3.4–3.5 TBtu, but modern 174k m³ vessels may deliver closer to 3.6–3.8 TBtu; actual delivered MMBtu depends on vessel size, cargo specification and boil-off, so state the vessel basis when quoting $/MMBtu

### Market state (verify live)

Spot LNG freight rates can move sharply with vessel availability, route disruption, newbuild deliveries, war-risk premia and basin arbitrage. Specific rate levels should be checked against live Spark / broker quotes before use. The modelling point is that freight is a stochastic risk factor, not a fixed adder.

### Destination decision

For Europe versus Asia, the relevant signal is not simply JKM minus TTF. It is:

JKM − TTF − Δ Freight − Δ Time − operational penalty

A wide JKM premium only creates value if a vessel is available, the delivery window can be met, and the diversion does not damage the next fixture.

### Vessel optimisation

Optimisation levers include triangulation to reduce ballast, speed versus boil-off trade-off, Panama versus Cape routing, heel and cool-down management, spot versus term charter mix, and positioning vessels ahead of expected arbitrage windows.

---

## Q9. Quantitative techniques for embedded LNG optionality

**Spread options** — Margrabe and Kirk approximations for two-asset diversion rights and DES-vs-hub basis options; fast, good for screening and limits

**Correlated curve Monte Carlo** — Multi-factor forward-curve simulation of HH, TTF, JKM and freight with seasonality and Samuelson effect; prices cargo cancellation / turndown rights, destination flexibility, cargo baskets and quantity tolerance under long-term SPAs where applicable

**Least-squares MC (Longstaff–Schwartz)** — Sequential and American-style decisions: divert-or-hold, storage and slot scheduling, exercise-timing of turndowns

**Stochastic DP / rolling intrinsic** — Regas plus storage assets; rolling intrinsic as the conservative lower bound, SDP for full extrinsic

*Calibration and model risk: vols from listed TTF/JKM options; correlations from history with regime weighting; add jump or regime-switching overlays, because 2021–22 and 2026 sit far outside Gaussian tails. Correlation instability is the dominant model risk; always benchmark against intrinsic value and realised P&L.*

---

## Q10. Market, legal and execution risks in LNG transactions

### Risk taxonomy

- **Flat price and basis** — Index mismatch between cost leg and revenue leg: HH, Brent, TTF, JKM, DES basis, local hub basis and freight.
- **Volume and optionality** — Cargo cancellation or turndown rights, destination flexibility, diversion rights, delivery-window flexibility, quantity tolerance under multi-cargo SPAs where applicable, force majeure, start-up delay and whether optionality is with us or against us.
- **Freight and shipping** — Charter-rate risk, vessel availability, voyage timing, canal constraints, boil-off, port access and whether diversion assumptions are physically executable.
- **Chokepoint and route concentration** — Exposure to Hormuz, Panama and Suez / Cape routing; war-risk premia and insurance availability; the cost and time of re-routing when a corridor closes or slows.
- **Liquidity and hedgeability** — Hedge depth by tenor, bid-offer cost, JKM/TTF/DES basis liquidity, freight hedgeability and margin-call funding under stress.
- **Credit and performance** — Counterparty default, PFE, collateral, parent support, performance risk, settlement terms and replacement cost.
- **Regulatory and legal** — Sanctions, destination restrictions, EU storage rules, methane rules, terminal-access rules and change-in-law exposure.
- **SPA dispute risk** — Price review, take-or-pay / quantity tolerance, non-delivery, commercial-operations date, force majeure, sanctions / change in law, destination and resale rights, demurrage, cargo quality, credit support and close-out damages.
- **Model and correlation risk** — Valuation of embedded options, regime breaks, unstable TTF-JKM correlation, freight volatility and model reliance beyond observable tenors.

### Quantify and govern

- VaR for the hedgeable window; PFE and expected exposure for credit tenors.
- Stress P&L on named scenarios, including combined market, freight, operational and funding stress.
- Hedge-slippage analysis: what fraction of the structure is hedgeable, at what cost, and out to what tenor.
- Deal memo: risk-adjusted return on capital, concentration versus book, exit strategy and unwind cost.
- Approval conditional on limits: basis, tenor, credit, liquidity, model reliance and review triggers if entry assumptions break.

---

## Q11. LNG portfolio stress testing

### Stress-testing method

Five lenses, applied together:

1. **Historical replay** — Revalue today's book under past market regimes: 2020 glut, 2021–22 European scarcity, and 2026 Hormuz / Middle East disruption.
2. **Forward deterministic scenarios** — Build named scenarios around future market risks: supply wave landing, Asian demand disappointment, Russian gas return, prolonged Hormuz disruption, or freight squeeze.
3. **Cross-factor shocks** — Do not shock prices in isolation. Stress TTF, JKM, Henry Hub, Brent-linked formulas, DES basis, freight, volatility, correlation, regas access and credit exposure together.
4. **Liquidity and funding overlay** — Include hedge liquidity, bid-offer widening, margin calls, collateral, PFE, and whether the book remains financeable under stress.
5. **Operational overlay** — Test vessel non-availability, canal disruption, terminal outage, berth delays, regas constraints, force majeure and cargo timing slippage.

### Scenarios that matter

- **2020 glut** — Covid demand shock: JKM below $2, US cargo cancellations and low utilisation. Tests SRMC floor, turndown economics and long-supply downside.
- **2021–22 Russia / Europe scarcity** — TTF spike, European security-of-supply stress, regas scarcity and extreme margin calls. Tests funding liquidity, hedge slippage and short-Europe exposure.
- **2026 Hormuz / Middle East disruption** — Around 20% of global LNG supply affected; around 9–10 bcm/month at risk; JKM-TTF flipped towards Asia; JKM volatility spiked. Tests force majeure cascades, freight, diversion value and basin basis risk.

### Forward-looking scenarios

- Extended Hormuz disruption versus fast normalisation
- Russian pipeline and LNG return, weakening TTF and Atlantic basis
- Supply wave landing in 2027–28 with weak Asian demand: sub-$8 TTF, US turndowns, regas intrinsic near zero
- Asian demand disappointment plus FID overbuild: second glut risk into the 2030s
- Freight squeeze plus Panama / routing constraint against a wide JKM–TTF spread

### Reverse stress

Ask what breaks the book: what combination of low prices, high freight, failed hedges, unavailable regas, counterparty default and margin calls would breach risk appetite or liquidity headroom?

### Governance

Run quarterly base stress cycles plus event-driven reruns. Tie them to observable signposts: Hormuz transits, Qatar force majeure status, EU storage levels, FID count, project ramp-up, Asian demand, freight rates and hedge liquidity.

Outputs should include not only stress P&L, but also management actions: hedge, divert, cancel / turndown where permitted, secure freight, nominate regas, reduce exposure, or trigger review / approval limits.

---

## Q12. Openlink Endur and ETRM / risk reporting interface

I do not enter deals directly into Openlink Endur, so I would not describe myself as an Endur operator. My role has been on the front-office structuring and valuation side. I build the economics of complex transactions in Python and spreadsheets, take them through the Deal Approval Form process, and then work with Middle Office / Risk to ensure the approved economics are implemented correctly for M2M and risk reporting.

That means I am familiar with the interface between commercial valuation and the official ETRM / risk reporting setup: pricing legs, embedded optionality, index exposures, volume flexibility, settlement mechanics, reserves and hedge representation. In practice this covers deal representation and templates, curve and index mapping, settlement mapping, end-of-day valuation and exposure grids, reserves, and reconciliation between the Python / spreadsheet economics and the official M2M. My strength is translating complex deal economics into a valuation and control framework that Risk and Middle Office can operationalise.

---

## Sources and caveats

**Folder documents:** Shell LNG Outlook 2024/2025/2026; Shell LNG Portfolio Strategic Spotlight (Mar 2026); LSEG LNG Market Outlook (Apr 2025, Jun 2026); bp Energy Outlook 2024/2025.

**External:** IEA Gas Market Reports Q1/Q2-2026 and Gas 2025; OIES, The LNG Wave in 2026/2027 (Feb 2026); IEEFA Global LNG Outlook 2024–28; EIA (Henry Hub ~$3.3, late June 2026); Global LNG Hub price updates (TTF ~$14.1, JKM ~$15.7, late June 2026); Reuters/LSEG June 2026 monthly averages (JKM 17.33, TTF 13.19); freight reporting via Spark/press.

All worked numbers (netbacks, freight, basis levels) are illustrative and dated; verify against live curves before quoting or using in any decision.

Q4 uses anonymised transaction structures and should be adapted to the relevant transaction context before use.

*Connected update: the following sections map the deep-research report and current web-search anchors back to the LNG topics.*

---

## Research connection map

Use this section to keep the LNG topic notes, deep research and current web search in one consistent story.

| Core topic summary | Deep research — method and evidence | 2 July web search — current market anchors |
|---|---|---|
| Keep the topic structure concise enough for practical review. | Adds first-principles explanation, sensitivity tables and source caveats. | Updates the live example: Asian price premium redirected US LNG cargoes from Europe. |
| Use formulas already in these notes: DES = TTF + basis; netback = hub/JKM minus freight and access costs. | Separates facts, assumptions and model choices; useful for technical detail. | Supports the curve argument: ICE reported record TTF / JKM activity and launched TTF Daily Options. |
| Q4 uses anonymised transaction examples, fact-checked against the actual deal context. | Adds the source tension: Shell/IEA resilience vs IEEFA/LSEG oversupply and weak-demand caution. | Confirms Hormuz as the lead 2026 stress-test example, not just an appendix case. |

*Practical rule: use the core topic summary for the main framework; use deep research for methodology and caveats; use web search only as a dated market anchor.*

---

## Targeted updates to the LNG topics

These are the small changes that make the LNG topic notes consistent with the deep research and current web search.

1. **Curve** — Add unit conversion and mark hierarchy explicitly; distinguish observable front-end from modelled back-end.
2. **Benchmarks** — Soften "oil indexation is marginal" to "marginal for European spot / DES pricing". Keep HH as the US cost floor.
3. **Regas** — Stress low merchant intrinsic value in a loose Europe; keep scarcity / insurance value as the source of premium.
4. **Transaction** — Q4 now uses anonymised, real-shaped transaction examples rather than a placeholder; keep them fact-checked against the actual deal context.
5. **Netback** — Use the June 2026 US export rerouting as a live example; treat all freight numbers as illustrative.
6. **Flexibility** — Add the 2025 high TTF-JKM correlation and 2026 spread break; option value sits in regime shifts.
7. **Assumptions** — Put demand elasticity and hysteresis near the top; source revisions are the risk, not just the model.
8. **Shipping** — Use voyage-cost build; avoid overclaiming live charter rates unless checked against Spark / broker quotes.
9. **Quant** — State the method ladder: intrinsic, spread option, MC, LSMC, SDP, then P&L back-test.
10–11. **Risk/stress** — Make 2026 Hormuz the lead combined market + physical + funding stress, alongside 2020 and 2022.

The result should be a concise technical note. Keep the main sections short; carry detailed research in backup notes or appendix.

---

## Current web-search anchors to use carefully

These are time-sensitive. State the date whenever using market levels or current-flow examples.

**Cargo flow / netback** — Reuters, 1 Jul 2026: US LNG exports to Europe fell to c.42% in June as Asian prices averaged $17.33/MMBtu vs Europe at $13.19/MMBtu; record Egyptian purchases at up to +$1 over TTF-linked prices. Use for Q2, Q5 and Q6.

**Market liquidity** — ICE, 15 Dec 2025: record TTF and JKM trading (TTF above 100 million contracts in 2025 for the first time) and the launch of TTF Daily Options (8 Dec 2025). Use for Q1, Q2 and hedging.

**Stress test** — Reuters, 30 Jun 2026: Shell said Hormuz disruption affected around 20% of monthly global LNG supply and may keep 2026 LNG trade flat. Use for Q10 and Q11.

*Fact / inference discipline: use current numbers only as dated examples; the enduring answer is the methodology, not the level.*

---

## Source crosswalk

Where each topic gets its support: core note, deep research and web search.

| Topic | Core note | Deep research | Web |
|---|---|---|---|
| Q1 Curve | Method | Hierarchy/caveats | ICE liquidity |
| Q2 Benchmarks | HH/TTF/JKM logic | Source context | June JKM premium |
| Q3 Regas | Spread option | IEEFA/OIES tension | Current storage/supply concerns |
| Q4 Transaction | Anonymised examples | Fact-check against deal context | Not applicable except market-risk framing |
| Q5–6 Netback/flex | Formula and option | Model details | US export rerouting |
| Q7–9 Assumptions/ship/quant | List | Sensitivities | ICE and shipping/chokepoint research |
| Q10–11 Risk/stress | Taxonomy | Combined shocks | Hormuz/Shell current example |

*Open issue: Q4 depends on transaction-specific facts. External research can support the risk framing, but the transaction examples should remain anonymised and fact-checked against the actual deal context.*
