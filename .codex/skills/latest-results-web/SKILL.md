---
name: latest-results-web
description: Use when the user asks for latest company results, the latest quarter or year, recent earnings, current official result sources, or source discovery before ingest.
---

# Latest Results Web

## Instrument Boundary

Use this workflow for operating-company reporting. Do not treat ETF sponsor
pages, holdings, distributions, or NAV updates as company earnings. Route a
passive, index-tracking equity ETF to `official-source-etf-research`; do not
create `TICKER_latest_results_source.md` for an ETF.
For bond, commodity, multi-asset, active, leveraged, inverse, or derivative-
heavy ETFs, stop with `unsupported ETF type` and create no artifacts.

## Source Priority

1. SEC and official company filings
2. Official earnings releases, presentations, prepared remarks, and transcripts
3. Official financial tables and data books
4. Reputable news for context not yet in official documents

Prefer Investor Relations for discovery and the underlying document as evidence.

## Profiles

- `chat`: answer-only request; freshly research, stay under 400 words, write no files.
- `minimal`: default durable/pipeline profile; extract only facts required for
  normalization, thesis, valuation, or the requested question.
- `full`: explicit archive/deep-dive request; capture broader tables and
  commentary without duplicating them in downstream files.

## Workflow

1. Identify ticker, company, exchange, reporting currency, fiscal calendar, and
   latest reported period.
2. Build the official source map in priority order.
3. Verify publication dates, period labels, units, and reporting basis.
4. In durable modes, save before normalization:
   - quarterly: `raw/imports/TICKER_latest_results_source.md`
   - annual: `raw/imports/TICKER_latest_annual_source.md`
5. Extract source facts once. Keep market quotes in a separate dated market
   source when a valuation or decision needs them.
6. Add an ingest handoff that names the exact blocks and gaps to normalize.
7. Append one workflow bullet to `log.md`.

## Minimal Source Note

```markdown
---
type: source-note
ticker: TICKER
company: Company Name
source_kind: latest-results
search_date: YYYY-MM-DD
reporting_scope:
currency:
normalized_output: raw/financials/TICKER_fundamentals.md
entity: "[[TICKER]]"
tags: [source/latest-results, ticker/TICKER]
---

# TICKER - Latest Results Source

## Source Map
## Reporting Scope
## Currency / Units
## Extracted Facts
## Missing / Unverified Data
## Handoff For Ingest
```

Add transcript or financial-table sections only when they contain downstream
facts. Preserve source wording and do not normalize inside this skill.

## Stop Conditions

Stop when identity, period, currency, units, or reporting basis is ambiguous;
official evidence cannot be found; or only untraceable secondary summaries are
available. Report `ไม่พบข้อมูลที่ยืนยันได้` rather than infer.
