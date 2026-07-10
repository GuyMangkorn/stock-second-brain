---
name: stock-decision-pipeline
description: Use when the user asks to chain stock-second-brain stages, run a new-ticker decision workflow, refresh a decision memo, or use legacy P1/P4/P6/P7/P10/P11/P13 aliases.
---

# Stock Decision Pipeline

## Mode Selection

- Explicit `mode:` wins.
- Save/update/refresh without `full` uses `lean`.
- Explicit full/deep-dive/archive or legacy `full new-ticker` uses `full`.

Both durable modes use one evidence set and links; `full` adds depth, not copied
tables or repeated narrative.

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

## Stop Conditions

Stop on ambiguous identity, unavailable current market data for an action call,
decision-changing source conflict, or no durable source base. Record the exact
gap; do not force a target or recommendation.
