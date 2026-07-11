---
name: official-source-etf-research
description: Use when the user asks for an index-tracking equity ETF deep dive, fund profile, methodology or holdings analysis, ETF comparison, thesis refresh, or research-to-decision work using official sources.
---

# Official Source ETF Research

## Core Principle

Analyze the fund as a portfolio vehicle, not as an operating company. Resolve
the listing identity, understand the index rules, inspect dated holdings, and
separate fund suitability from portfolio fit.

## Required References

Read `references/equity-index-etf.md` and `wiki/reference/output-contract.md`.
For durable work also read `wiki/reference/etf-entity-template.md` and
`wiki/reference/source-hierarchy.md`.

## Scope Gate

This v1 supports passive, index-tracking equity ETFs. Stop with
`unsupported ETF type` for bond, commodity, multi-asset, active, leveraged,
inverse, or derivative-heavy funds. Do not silently adapt this workflow.

Resolve `entity_key: EXCHANGE:TICKER` before research. Use filenames prefixed
with `ETF_EXCHANGE_TICKER`; ticker-only identity is insufficient. Preserve an
existing vault `entity_key` and record the official listing venue separately;
do not silently migrate an exchange alias into a second entity.

## Profiles

| Profile | Trigger | Output |
|---|---|---|
| `chat` | General ETF question without save/update intent | At most 400 words; no files |
| `thesis-delta` | Existing ETF refresh | Changed fund facts/entity sections; comparison only when asked |
| `deep-dive` | New ETF, explicit deep dive, or research-to-decision | Source note, fund facts, thin ETF entity; decision handoff only when requested |

## Workflow

1. Resolve exchange, ticker, fund name, sponsor, domicile, listing currency,
   benchmark, and passive index-tracking status.
2. Build the official source map in the priority defined by
   `references/equity-index-etf.md`; record publication and as-of dates.
3. In durable modes, save
   `raw/imports/ETF_EXCHANGE_TICKER_fund_source_YYYY-MM-DD.md` before
   normalization.
4. Normalize verified facts into
   `raw/funds/ETF_EXCHANGE_TICKER_fund_facts.md`. Keep incompatible periods and
   currencies separate; never infer missing weights or metrics.
5. Analyze index methodology, exposure, concentration, cost, tradability,
   tracking, income, FX, and fund-specific risks. Use look-through or
   peer-relative valuation only when inputs are sourced and period-compatible.
6. Prepare the `wiki/entities/ETF_EXCHANGE_TICKER.md` delta. For research-only
   work, apply it once. For research-to-decision, let the pipeline apply it once
   after the decision so the latest-decision link is included.
   Create a memo in `wiki/analysis/comparisons/` only for an explicit peer or
   overlap question.
7. For research-to-decision, hand the verified evidence to the ETF branch of
   `stock-decision-pipeline`. Do not invoke P1, P4, P6, P7, or P11.
8. Append one workflow bullet to `log.md` after standalone durable work. Inside
   a decision pipeline, the pipeline owns one bullet for the whole workflow.

## Decision Boundary

ETF valuation is not a corporate DCF. Use price/NAV, premium or discount,
look-through portfolio multiples, distribution yield, expense drag, tracking
difference, and peer comparison when verified. Do not create a DCF memo or an
intrinsic-value target for an ETF.

Without user-provided portfolio holdings, state fund-level suitability only.
Do not claim portfolio fit, diversification benefit, or whole-portfolio
overlap. With portfolio holdings, label overlap analysis as a separate input-
dependent calculation.

## Stop Conditions

Stop when identity or benchmark is ambiguous; passive equity status cannot be
verified; official methodology or holdings are unavailable; holdings or market
data are stale for the requested conclusion; as-of dates, periods, currencies,
or units are incompatible; or a source conflict changes the conclusion.
Report the exact gap and write `ไม่พบข้อมูลที่ยืนยันได้` rather than improvise.
For an unsupported ETF type, do not create source, fund-facts, entity,
comparison, valuation, or decision artifacts.

## Chat Handoff

After durable work, answer in under 200 words with updated files, current fund
thesis or decision implication, and the most important freshness or source gap.
