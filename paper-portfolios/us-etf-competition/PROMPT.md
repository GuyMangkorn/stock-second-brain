# US ETF Paper Portfolio Manager — Portfolio Run

Execute exactly one educational Portfolio Run at `paper-portfolios/us-etf-competition/`.
Use `config.yaml` for numeric mandate, liquidity, freshness, score and risk limits.
The authorized phase is `simulation`: record local simulated trades without a
broker. Live-money routes, broker order submission, margin, shorts, options,
leveraged/inverse and non-equity funds remain prohibited. The competition is
open-ended until explicit user termination. There is no ten-session waiting phase.
Use `execution_profile: scheduled-inline`; perform verification locally in the
current context and do not dispatch subagents or reviewers for this run.

## Ordered procedure

### 1. Reconcile and resolve pending execution

Read config, ledger, state, latest run note, and run `scripts/rebuild_portfolio.py
--check`. The check validates accounting; separately compare rebuilt state with
stored projections, ignoring generated_at. Rebuild stale projections from the
ledger; block the whole run only for invalid accounting or unverifiable portfolio
risk that prevents safe sizing. Do not rewrite historical events.

Read pending_decisions. Reserve their cash and exposure; settle or explicitly
cancel a ticker's pending decision before making another. Verify the official
exchange calendar, including next session date and opening time. Manual reviews
use invocation time; scheduled reviews use their configured cadence. Outside
market hours and holidays, analysis can proceed, while fills wait for the
predetermined next session open. Waiting is `PENDING_EXECUTION`, not BLOCKED.

For due pending orders, collect the exact session's unadjusted opening price
along with this run's other market evidence. Simulate their effects for current
risk analysis, and record/settle them before persisting any new decisions. Review
holdings and exposure after settlement, including any cancelled opening-gap orders.

### 2. Read research before searching prices

Read `index.md`, relevant entity/fund facts/performance pages, previous decisions
and unresolved blockers. Review existing holdings first: thesis changes, losses,
drawdown triggers, sector/region/style/FX concentration and cash. Use cached
performance to understand total return, drawdown, recovery, methodology, costs
and benchmark-relative evidence over compatible windows. Past return or a low
nominal share price alone is never a buy rationale.

Read `evidence/market-data/latest-prices.md` and only the tail of `price-log.md`.
Use the cache for screening, not execution. Form a compact shortlist from the
existing research universe based on portfolio role, distinct exposure, thesis,
risk and evidence maturity. State why each shortlisted fund belongs and why a
plausible alternative was excluded. There is no whole-universe price refresh.
Refresh existing research only for a decision-changing gap or material event;
research at most the configured number of new candidates per review. A new
candidate may qualify in this run after the same local admission review.

### 3. Finish decision-critical research

For shortlisted candidates, read official issuer/filing evidence first, then
reputable market/news sources as needed. Identify which missing fact can change
BUY/SELL or sizing before browsing. Close actionable blockers in this run:
calculate scores, resolve role comparisons, and construct weights instead of
repeating `construction incomplete`. Carry an exact unresolved dependency and
the attempted resolution when a source is unavailable.

Forum/X sentiment is optional hypothesis discovery only. Consult it for a
specific narrative or event question; verify consequential claims against primary
sources. Absence of forum analysis never blocks a trade. This portfolio workflow
does not invoke the durable ETF performance workflow or alter its verification gate.

### 4. Local admission and sizing

Classify each candidate as `ELIGIBLE`, `ELIGIBLE_WITH_WARNING`, or `INELIGIBLE`.
A research page's PASS is useful evidence, but is not a required handoff token.
Resolve any existing review finding locally from sources; never ignore a
material integrity finding or change the original research review status.

Hard candidate gates: verified exchange-qualified identity; official unleveraged
long-only equity eligibility; verified AUM, median dollar volume, spread, expense
and history satisfying config; decision-price freshness; no unresolved material
source conflict; and enough exposure evidence to apply portfolio risk limits.
Use the liquidity freshness limit. Missing eligibility/price/liquidity evidence
blocks that candidate, not unrelated candidates. Verified thesis breaks trigger
exit review. Stale research alone must not obstruct a justified risk reduction.

Holdings/valuation and performance freshness thresholds trigger targeted review.
A missing valuation multiple, older noncritical research metric or incomplete
score component may be a warning when it cannot reverse the thesis or hide a
risk-limit breach. Explain that judgment and cap the position at the configured
warning weight. Never fabricate a missing value. For uncertain overlap, assume
full overlap with the plausible peer group and enforce its combined cap; if
conservative exposure bounds cannot establish compliance, exclude the candidate.

Use the configured six score components. Label sourced facts, calculations and
PM judgments. For a missing component show a score interval using zero to the
component maximum; size conservatively and do not use an incomplete score to
trigger mechanical SELL/REDUCE. Complete the evidence first. Use the configured
sell/drop thresholds only with comparable complete scores. Scores rank candidates;
state thesis, why now, falsifier and the evidence that changes sizing.

Construct a feasible target from eligible candidates now. The 6–10 fund count is
a long-term goal, not a prerequisite: fewer funds and more cash are acceptable
during staged entry. Retain position, cash, seasoning, sector/theme, overlap,
no-trade-band, turnover, position-loss and portfolio-drawdown limits from config.
Normal turnover is gross BUY plus SELL notional / pre-rebalance equity for this
rebalance, including pending orders; the dashboard's lifetime turnover is not a
remaining allowance. Initial deployment uses the same turnover cap. Do not force
BUY to meet a count, cash-investment target or activity quota.

### 5. Refresh only decision-relevant prices and lock the decision

Retrieve directly opened quotes for holdings, SPY and shortlisted funds whose
price changes the decision. Reuse a verified batch observation within freshness
limits when no new price is needed; cite batch path and evidence ID, never cache
alone. Open known source URLs directly where possible; search is discovery only.
Use the latest completed unadjusted close outside market hours for decision
reference. A prior close is not today's simulated fill.

Record analysis_at/information_cutoff_at at the final decision boundary, after
collecting decision evidence, with actual source and retrieval timestamps.
Only evidence available by that boundary may justify the decision. Earlier
invocation time remains separate. Later execution evidence may settle the fixed
order but may not rewrite its rationale or quantity.

Persist one DECISION per intended BUY or SELL (REDUCE maps to side SELL):

```json
{
  "event_id": "decision-RUN-TICKER",
  "event_type": "DECISION",
  "competition_id": "us-etf-competition-2026",
  "run_id": "RUN",
  "recorded_at": "actual decision timestamp with timezone",
  "effective_at": "same decision timestamp",
  "information_cutoff_at": "same or earlier decision cutoff",
  "execution_model": "next-session-open",
  "status": "PENDING",
  "ticker": "TICKER",
  "exchange_qualified_identity": "EXCHANGE:TICKER",
  "side": "BUY",
  "quantity": "fixed positive shares, rounded down to six decimals",
  "maximum_notional_usd": "positive precommitted notional cap",
  "decision_reference_price": "verified unadjusted price",
  "execution_at": "09:30 America/New_York next trading session as ISO timestamp",
  "calendar_evidence": "official calendar URL or captured evidence",
  "source_evidence": ["batch path and evidence ID", "research source paths"],
  "rationale": "thesis, score or interval, risks and target weight",
  "risk_override": false
}
```

The schema example describes fields, not real observations. Calculate quantity
and cap before execution, retaining cash and risk headroom for opening gaps.
Set all orders for a rebalance using joint cash/exposure constraints. Record the
limits calculation in the run note. Validate the proposed ledger in a temporary
copy with rebuild before appending; recheck that the original ledger did not
change during analysis. Do not alter or cancel orders using later information
and then claim the historical opening fill. A cancellation before its scheduled
open is a DECISION_CANCELLED event; once the open has occurred, settle the fixed
order or record the mechanical rejection before making a new decision.

### 6. Batch evidence and settle

Store one immutable evidence batch (schema_version 2 market-data) per run containing clock,
calendar, quotes and any due execution observations. Use actual timestamps and
SHA-256 of captured visible text. Each execution observation must have
price_basis `unadjusted-session-open`, source_as_of equal to the predetermined
execution_at, matching ticker/exchange identity and USD currency. Use the
historical table's actual Open column; never adjusted close/NAV or an invented
open. Missing open evidence leaves the affected order pending; explicitly refresh
that exact opening row next run instead of silently choosing a later session.
Do not create a new JSON file per ticker; use the batch recorder for new evidence.

The current batch cutoff permits currently available execution evidence; this
is separate from each prior decision's cutoff. Never feed it back into that
prior decision. Market data pages are read-only inputs; simulation events are
local accounting records, not broker-confirmed fills.

```bash
python3 paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py --root paper-portfolios/us-etf-competition --batch /path/to/staged-batch.json
python3 paper-portfolios/us-etf-competition/scripts/settle_simulation.py --batch paper-portfolios/us-etf-competition/evidence/market-data/batches/RUN.json
python3 paper-portfolios/us-etf-competition/scripts/settle_simulation.py --batch paper-portfolios/us-etf-competition/evidence/market-data/batches/RUN.json --write
```

Settle prior orders before appending new decisions. The CLI validates the batch,
locks the ledger, settles SELL before BUY, rejects duplicate fills, and applies
open + 5 bps for BUY / open - 5 bps for SELL. A breached fixed notional budget or
accounting constraint cancels that order for re-review, without blocking other
orders. The agent remains responsible for joint admission, exposure and per-run
turnover checks; the settlement CLI is an accounting guard, not a research engine.
Preserve raw price marks separately from slippage-inclusive cost basis.

Retain legacy evidence unchanged. Read the full price log only for cache recovery.
Use CORRECTION for accounting errors; never rewrite events. Record distributions
as cash on pay date, no automatic reinvestment; handle splits from verified
sources, including cancelling pre-split pending quantities before execution when
known. Mark holdings using unadjusted closes with explicit cash distributions;
SPY uses its adjusted total-return proxy. Do not double-count distributions by
marking held shares with dividend-adjusted prices.

### 7. Complete and report

Rebuild state/dashboard after valid events. Write one dated run note with:
shortlist and exclusions; gaps resolved/attempted; admission per candidate;
scores or intervals; exposure/overlap and joint sizing; IN/OUT/HOLD; pending
orders; settlement results; source timestamps, batch/evidence links; and next
specific trigger. Show actual versus target weights, quantity, decision reference,
simulated execution price, rationale and status. Use `SIMULATED`, `PENDING`,
`CANCELLED`, or `NO_ORDER`, keeping broker-confirmed fills separate.

Report actual portfolio value/cash/return/drawdown, same-window SPY comparison,
verified official S&P 500 TR if available, and per-run turnover. Pending targets
do not change current holdings or returns. A missing official reference benchmark
is a disclosed reporting gap, not a trading blocker.

Run status: `COMPLETED` for a valid review (including justified NO_TRADE),
`COMPLETED_WITH_GAPS` for candidate-specific failures/warnings,
`PENDING_EXECUTION` when only waiting for the fixed opening evidence, and
`BLOCKED` only for portfolio-wide accounting/risk dependencies. Every repeated
blocker must show a concrete resolution attempt or a known external dependency.
