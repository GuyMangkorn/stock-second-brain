---
name: stock-decision-pipeline
description: Use when the user asks to chain stock-second-brain stages, run or refresh a company or passive equity ETF decision workflow, or use legacy P1/P4/P6/P7/P10/P11/P13 aliases.
---

# Stock Decision Pipeline

## Mode Selection

- Explicit `mode:` wins.
- Save/update/refresh without `full` uses `lean`.
- Explicit full/deep-dive/archive or legacy `full new-ticker` uses `full`.

Both durable modes use one evidence set and links; `full` adds depth, not copied
tables or repeated narrative.

## Instrument Gate

Resolve identity and `instrument_type` before selecting stages.

- `company`: use the legacy P-code routes below.
- `ETF`: require `entity_key: EXCHANGE:TICKER` and verify passive,
  index-tracking equity status. Use the ETF route below.
- Unsupported or unresolved instrument: stop and report the exact identity or
  scope gap.

Never send an ETF through P1, P4, P6, P7, or P11. These stages own company
results, company financials, company research, and corporate valuation.

## Stage Aliases

P1 source discovery; P4 ingest; P6 new-ticker deep dive; P7 existing-ticker
thesis refresh; P10 audit; P11 valuation; P13 decision.

## New-Ticker Flow

```text
P1 -> P4 -> P6 -> P11 stage gate -> P13 -> optional P10
```

1. P1 creates the official source note once.
2. P4 creates normalized fundamentals and a skeletal thin entity.
3. P6 completes the entity using the same evidence. Do not create a separate
   research memo unless it owns durable analysis not covered elsewhere.
4. P11 creates a valuation memo only when calculation-ready. If blocked, pass a
   short valuation blocker directly to P13.
5. P13 creates one decision memo and updates the entity once with the final
   action-relevant delta.
6. Append one pipeline bullet to `log.md`, not one per stage.

## Existing-Ticker Routing

Read `index.md`, entity, fundamentals, and latest relevant analysis first.

| Situation | Flow |
|---|---|
| Only price changed | P13 with fresh market data |
| Valuation stale | P11 -> P13 |
| Thesis stale, no new results | P7 -> optional P11 -> P13 |
| New results | P1 -> P4 -> P7 -> optional P11 -> P13 |
| Source quality uncertain | P10 -> fix decision-critical gaps -> P13 |

## ETF Routing

Read `ETF Index`, the exchange-qualified ETF entity, normalized fund facts,
latest comparisons, and latest decision before choosing work.

| Situation | Flow |
|---|---|
| New supported ETF | `official-source-etf-research/deep-dive -> ETF decision` |
| Holdings, methodology, costs, or tracking stale | `official-source-etf-research/thesis-delta -> ETF decision` |
| Only current price/NAV changed | fresh market/NAV check -> `ETF decision` |
| Explicit peer or overlap question | ETF research -> comparison -> optional ETF decision |
| Source quality uncertain | P10 ETF checks -> fix decision-critical gaps -> ETF decision |

Save ETF outputs as:

```text
raw/imports/ETF_EXCHANGE_TICKER_fund_source_YYYY-MM-DD.md
raw/funds/ETF_EXCHANGE_TICKER_fund_facts.md
wiki/entities/ETF_EXCHANGE_TICKER.md
wiki/analysis/decisions/ETF_EXCHANGE_TICKER Decision Memo YYYY-MM-DD.md
```

Create a comparison memo only when the question needs peers or overlap. Whole-
portfolio overlap and fit require user-provided portfolio holdings.
Apply the ETF entity delta once after the decision so it links the current fund
facts, comparison when present, and latest decision. Append one pipeline log
bullet for the entire ETF workflow.

## Valuation Stage Gate

Use DCF only with reliable FCF, reinvestment, capital structure, shares, and
terminal assumptions. Otherwise use a sourced reverse DCF, multiple, growth-
adjusted, unit-economics, or scenario read. If those inputs are also missing,
state the blocker in P13 and prefer `wait` or `watchlist`.

## Decision Memo Recipe

```text
# TICKER Decision Memo - YYYY-MM-DD
## Action Read
## Current Price / Market Data Check
## Decision-Changing Evidence
## Valuation Read
## Key Assumption / Falsifier
## Action-Relevant Gaps
## Reports / Sources
```

Reference the entity thesis and valuation calculation. Restate bull/bear only
when the decision changes them.

Budgets: lean decision 400-500 words; full decision at most 800. Lean entity +
valuation + decision narrative must stay at or below 1,400 words; full at or
below 2,400. Tables are exempt.

## ETF Decision Memo Recipe

```text
# ETF_EXCHANGE_TICKER Decision Memo - YYYY-MM-DD
## Portfolio Role
## Action Read
## Current Price / NAV Check
## Peer-Relative Read
## Valuation / Cost / Tracking Read
## Key Falsifier
## Action-Relevant Gaps
## Reports / Sources
```

Use `BUY`, `WATCH`, or `AVOID`. Without portfolio holdings, describe fund
suitability only and do not claim portfolio fit or diversification benefit.
ETF valuation is not a DCF: use sourced price/NAV, premium/discount,
look-through multiples, yield, expense drag, tracking, and compatible peers.

## Stop Conditions

Stop on ambiguous identity, unavailable current market data for an action call,
decision-changing source conflict, or no durable source base. Record the exact
gap; do not force a target or recommendation.

For ETFs also stop when exchange-qualified identity, benchmark, passive equity
status, official methodology, or holdings cannot be verified; snapshots are
incompatible or too stale for the conclusion; or the fund is bond, commodity,
multi-asset, active, leveraged, inverse, or derivative-heavy.
For an unsupported ETF, do not create source, fund-facts, entity, comparison,
valuation, or decision artifacts.
