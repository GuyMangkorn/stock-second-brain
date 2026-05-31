---
name: stock-decision-pipeline
description: Orchestrate the common stock-second-brain decision-grade ticker workflow, chaining source discovery, financial ingest, company research, DCF valuation, and decision memo refreshes with fresh current price checks.
---

# Stock Decision Pipeline

Use this skill when the user asks to chain prompts, run a full decision-grade
workflow, go from a new ticker to a decision memo, or refresh an existing
decision memo using the current stock price.

This skill coordinates other stock-second-brain skills. It should not replace
their source integrity rules.

## Language Standard

Follow `wiki/reference/output-contract.md`: decision memo narratives should be
Thai-first, while headings, ticker labels, source labels, market data fields,
and finance/valuation terms remain English for precision and searchability.

## Non-Negotiables

- Use source-backed facts before writing durable notes.
- Keep facts, assumptions, calculations, and judgment separate.
- Freshly check current price, market cap, shares, and other market data before
  any valuation or action call.
- Do not force a DCF, fair value target, or action recommendation when required
  inputs are missing or the business model makes a point-estimate DCF fragile.
- Append `log.md` for every durable source note, financial ingest, valuation
  memo, decision memo, entity update, or audit memo.

## Full New-Ticker Pipeline

Use when the ticker does not yet have a reliable entity page or normalized
financial facts.

```text
P1 -> P4 -> P6 -> P11 -> P13 -> optional P10
```

Execution order:

1. Use `latest-results-web` to create
   `raw/imports/TICKER_latest_results_source.md`.
   - This step is source discovery only.
   - Do not normalize statements or update the entity page here unless the user
     explicitly asks for a one-step ingest.
2. Use `financial-facts-ingest` on that source note to create or update
   `raw/financials/TICKER_fundamentals.md`,
   optional `raw/financials/TICKER_fundamentals.json`, `wiki/entities/TICKER.md`,
   and `log.md`.
3. Use `official-source-stock-research` for the company deep dive and thesis
   work, updating `wiki/entities/TICKER.md` and creating an analysis memo only
   when useful.
4. Use `dcf-valuation` only after core inputs are verified: current price,
   FCF or OCF minus capex, cash, debt, diluted shares, and assumptions. If DCF
   inputs are unstable, treat P11 as a valuation-gap or multi-method valuation
   read instead of forcing a point estimate.
5. Create `wiki/analysis/decisions/TICKER Decision Memo YYYY-MM-DD.md` with an
   action read: add, hold, wait, trim, or avoid/watchlist.
6. Use `source-integrity-audit` before or after P13 when the decision depends
   on fragile source coverage, old notes, or many linked files.

## Existing-Data Decision Refresh

Use when the vault already has some data and the user wants an updated decision
memo with the current price.

Read first:

- `index.md`
- `wiki/entities/TICKER.md`
- `raw/financials/TICKER_fundamentals.md`
- latest relevant valuation, thesis, decision, catalyst, and audit memos in
  the relevant `wiki/analysis/<category>/` folder

Then choose the lightest sufficient flow:

| Situation | Flow |
|---|---|
| Entity/fundamentals and latest DCF are still valid; only price changed | P13 only, with a fresh current price check |
| Valuation inputs or upside/downside are stale | P11 -> P13 |
| Thesis may be stale but financials are not newly reported | P7 -> P11 -> P13 |
| New quarter/year was reported | P1 -> P4 -> P7 -> P11 -> P13 |
| Source quality is uncertain before a real decision | P10 -> fix gaps -> P13 |

If no reliable valuation exists, do not infer upside/downside from price alone.
Either run P11 first or write the decision memo as a watchlist/hold-style memo
with valuation gaps clearly labeled.

## Multi-Method Valuation Policy

DCF is one valuation lens, not a required anchor for every decision memo. Use a
DCF-led `Valuation Read` only when normalized FCF, reinvestment needs, capital
structure, share count, and terminal assumptions are reliable enough to support
the output.

For high-growth, pre-profit, optionality-heavy, cyclical, financial-sector, or
otherwise hard-to-normalize companies, do not force a precise DCF. Use a
multi-method valuation read and label each lens clearly:

- `DCF Read` when input quality supports it.
- `Reverse DCF Read` to identify what growth, margin, and FCF conversion the
  current price implies.
- `Multiple Read` using sourced peer or historical valuation ranges when
  available.
- `Growth-Adjusted Read` such as EV/Sales, EV/Gross Profit, or P/FCF relative
  to growth, margin, scale, and quality.
- `Unit Economics / Cohort Read` for SaaS, marketplaces, fintech, and other
  cohort-driven businesses.
- `Scenario / Optionality Read` for outcomes with wide dispersion or meaningful
  product, platform, regulatory, or cycle optionality.
- `Margin of Safety / Position Sizing Read` to connect valuation uncertainty to
  portfolio action.

Keep the decision humble when valuation dispersion is wide. Prefer `wait`,
`watchlist`, smaller sizing, or explicit follow-up triggers over a false-precise
fair value.

## Decision Memo Requirements

Save as:

```text
wiki/analysis/decisions/TICKER Decision Memo YYYY-MM-DD.md
```

Recommended sections:

- `# TICKER Decision Memo - YYYY-MM-DD`
- `## Action Read`
- `## Current Price / Market Data Check`
- `## Evidence From Vault`
- `## Valuation Read`
- `## Bull Case`
- `## Bear Case`
- `## Key Assumptions`
- `## What Would Change The Decision`
- `## Missing / Unverified Data`
- `## Source Map`

`Valuation Read` should state which lenses were used and why. If DCF is skipped,
explain why and use other source-backed valuation lenses rather than implying a
fair value from price movement alone.

Decision language should be explicit but humble. Prefer `wait` or `watchlist`
when source gaps or valuation uncertainty are material.

## Example Prompts

```text
ใช้ skill stock-decision-pipeline สำหรับ MSFT
รัน full new-ticker decision-grade flow: P1 -> P4 -> P6 -> P11 -> P13
ถ้าขั้นไหน source ไม่พอ ให้หยุดและเขียน missing data แทนการเดา
```

```text
ใช้ skill stock-decision-pipeline สำหรับ MSFT
vault มี data และ DCF แล้ว ช่วยอัปเดต decision memo ด้วยราคาปัจจุบัน
ถ้า valuation assumptions ยัง valid ให้รัน P13 เท่านั้น
ถ้า valuation stale ให้รัน P11 -> P13
```

## Stop Conditions

Stop and report gaps when:

- ticker identity is ambiguous
- current price or market data cannot be freshly checked for a decision memo
- FCF, cash/debt, or share count is missing for a DCF-dependent decision
- the business requires a non-DCF valuation lens but the needed peer,
  unit-economics, scenario, or market-data inputs are unavailable
- source notes conflict and the conflict changes the decision
- the user asks for an action call but the vault has no durable source base
