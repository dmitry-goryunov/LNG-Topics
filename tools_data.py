"""Shared registry of external tools, used by both the Topics and Tools pages
to build bidirectional links (topic -> tool, tool -> topic) from one source."""

TOOLS = [
    {
        "slug": "xva-cva",
        "title": "XVA / CVA Adjustments",
        "url": "https://agxrz252lkxboz3ovanwn4.streamlit.app/",
        "related": [
            ("Q9", "PFE / credit simulations, XVA metrics"),
            ("Q10", "credit and performance risk"),
        ],
        "description": (
            "Interactive calculator for credit valuation adjustment (CVA) and the wider XVA "
            "stack on a derivative/portfolio exposure profile. Walks through expected exposure, "
            "probability of default, and how counterparty credit risk gets priced into a deal's "
            "valuation — the same PFE/credit-simulation logic referenced in the quant methods "
            "and risk-taxonomy sections."
        ),
    },
    {
        "slug": "spread-hedge",
        "title": "Hedging Spread Options with Static Calls/Puts",
        "url": "https://spread-hedge-aqdbbqkvon6gxewpuf9z5d.streamlit.app/",
        "related": [
            ("Q6", "destination flexibility"),
            ("Q9", "spread options — Margrabe/Kirk"),
        ],
        "description": (
            "Demonstrates static replication of a spread option (e.g. a JKM-TTF diversion spread) "
            "using a strip of vanilla calls and puts, as an alternative to dynamic delta-hedging. "
            "Useful for seeing why static hedges are attractive when the spread's volatility or "
            "correlation is hard to trade directly."
        ),
    },
    {
        "slug": "rainbow",
        "title": "Rainbow / Diversion Optionality",
        "url": "https://rainbow-options-4hwgd2sbshbb6t5cakamff.streamlit.app/",
        "related": [
            ("Q6", "destination flexibility and diversion optionality"),
            ("Q9", "correlated curve Monte Carlo"),
        ],
        "description": (
            "Explores multi-asset \"rainbow\" option payoffs — picking the best of several basin "
            "netbacks (e.g. max(JKM − freight, TTF − freight, local sale)) — which is the payoff "
            "structure behind cargo diversion rights. Shows how correlation between basins drives "
            "the option's value."
        ),
    },
    {
        "slug": "fleet-lp",
        "title": "Linear Optimisation of LNG Fleet",
        "url": "https://dmitry-goryunov.github.io/lng-fleet-sim/",
        "related": [
            ("Q8", "shipping economics, vessel optimisation"),
            ("Q9", "least-squares MC / linear programming"),
        ],
        "description": (
            "An LP-based vessel/fleet scheduling simulator: allocates a fleet of LNG carriers "
            "across cargoes and routes to maximise netback, subject to voyage time, boil-off and "
            "charter constraints — the linear-programming counterpart to the deck's vessel "
            "optimisation levers (triangulation, Panama vs. Cape routing, charter mix)."
        ),
    },
    {
        "slug": "storage",
        "title": "Storage Valuation for Storage & Regas",
        "url": "https://storage-db3cfmtmlkdv4fwgzqjidp.streamlit.app/",
        "related": [
            ("Q3", "regasification slot valuation"),
            ("Q7", "quantity tolerance under multi-cargo SPAs"),
            ("Q9", "stochastic DP / rolling intrinsic, 1-factor storage"),
        ],
        "description": (
            "Values a storage or regas-slot asset via rolling intrinsic and 1-factor "
            "(Clewlow-Strickland) stochastic optimisation, showing how the conservative rolling-"
            "intrinsic lower bound compares to the full extrinsic value captured by stochastic "
            "dynamic programming. The same 1-factor Clewlow-Strickland engine doubles as a swing "
            "model: where an SPA has flexibility in annual and monthly contract quantities (ACQ/MCQ "
            "tolerance), that optionality can be valued the same way as storage — as a swing right "
            "to flex offtake up or down within the contractual band each period."
        ),
    },
]


def tools_for_topic(q_number):
    """Returns TOOLS entries whose 'related' list references the given topic, e.g. 'Q9'."""
    return [tool for tool in TOOLS if any(q == q_number for q, _ in tool["related"])]
