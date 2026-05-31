# Output Contract

This page defines the expected shape for durable outputs.

## Language Standard

Future durable outputs should use hybrid Thai/English:

- Narrative analysis, thesis, risks, catalysts, decision reads, caveats, and
  chat summaries: Thai-first.
- Headings, frontmatter keys, JSON keys, filenames, ticker symbols, source
  labels, table column names, formulas, and metric names: English.
- Finance and valuation terms should stay English when they are clearer or more
  searchable, such as `valuation`, `DCF`, `reverse DCF`, `FCF`, `WACC`,
  `terminal growth`, `margin of safety`, `upside/downside`, `multiple`, `net
  debt`, `capex`, `unit economics`, and `guidance`.
- Raw source notes should preserve the source's meaning and language as much as
  possible. Thai summaries are allowed, but they must not replace traceable
  source facts.
- Financial facts Markdown and JSON should remain structured and automation
  friendly; use Thai mainly in explanatory notes, missing-data explanations, and
  judgment sections.

## Source Note

File:

```text
raw/imports/TICKER_source_kind_YYYY-MM-DD.md
raw/imports/TICKER_latest_results_source.md
```

Required sections:

- `# TICKER - Source Title`
- `## Source Map`
- `## Reporting Scope`
- `## Currency / Units`
- `## Extracted Facts`
- `## Transcript / Commentary` when relevant
- `## Financial Tables` when relevant
- `## Missing / Unverified Data`
- `## Handoff For Ingest`

Required frontmatter:

```yaml
---
type: source-note
ticker:
company:
source_kind:
search_date:
reporting_scope:
currency:
normalized_output:
entity:
tags:
---
```

## Financial Facts Markdown

File:

```text
raw/financials/TICKER_fundamentals.md
```

Required sections:

- `# TICKER - Company Name`
- `## Snapshot`
- `## Provenance`
- `## Reporting Scope`
- `## Financial Table`
- `## Key Ratios`
- `## Quarterly YoY Comparison` when same-quarter data exists
- `## Quarterly Trend` when sequential quarterly data exists
- `## YTD Comparison` when year-to-date comparable periods exist
- `## Annual Trend` when complete fiscal-year data exists
- `## Segment Revenue Chart`
- `## Cash Flow And Capex Chart` when cash flow data exists
- `## Balance Sheet Snapshot Chart` when balance sheet snapshots exist
- `## Missing / Unverified Data`

## Optional Financial Facts JSON

File:

```text
raw/financials/TICKER_fundamentals.json
```

Recommended top-level keys:

```json
{
  "company": "",
  "ticker": "",
  "market": "",
  "currency": "",
  "period_type": "annual",
  "reporting_scope": "",
  "periods": [],
  "provenance": [],
  "financial_series": {},
  "segment_series": [],
  "ratios": [],
  "missing_data": []
}
```

## Entity Page

File:

```text
wiki/entities/TICKER.md
```

Required sections:

- Snapshot
- Source Map
- Business Model
- Segments / Revenue Mix
- Financial Facts
- Charts
- Transcript / Management Commentary
- Thesis
- Risks
- Catalysts
- Valuation Watch Items
- Reports / Source Notes
- Follow-Up
- Missing / Unverified Data

## Analysis Memos

Use category folders under `wiki/analysis/` so agents can find the right class
of memo without scanning every analysis note:

| Folder | Memo type |
|---|---|
| `wiki/analysis/decisions/` | decision memos |
| `wiki/analysis/valuations/` | DCF and valuation work |
| `wiki/analysis/earnings/` | earnings and transcript digests |
| `wiki/analysis/catalysts/` | catalyst and news context |
| `wiki/analysis/comparisons/` | peer/theme comparisons and screener triage |
| `wiki/analysis/sentiment/` | X/Twitter and market chatter context |
| `wiki/analysis/audits/` | source integrity audits and source gap registries |

Decision memo:

```text
wiki/analysis/decisions/TICKER Decision Memo YYYY-MM-DD.md
```

Required sections:

- Action Read
- Current Price / Market Data Check when market data affects the action
- Evidence From Vault
- Valuation Read when relevant; use DCF only when inputs are reliable, otherwise
  label alternative lenses such as reverse DCF, peer multiples,
  growth-adjusted multiples, unit economics, scenario analysis, and optionality
- Bull Case
- Bear Case
- Key Assumptions
- What Would Change The Decision
- Missing / Unverified Data
- Source Map

DCF valuation:

```text
wiki/analysis/valuations/TICKER DCF Valuation YYYY-MM-DD.md
```

Required sections:

- Bottom Line
- Source Map
- Input Table
- Base Case Assumptions
- FCF Projection
- Valuation Summary
- Sensitivity Matrix
- Sanity Checks
- Missing / Unverified Data

X / market sentiment:

```text
wiki/analysis/sentiment/TICKER X Sentiment YYYY-MM-DD.md
```

Required sections:

- Query Summary
- Bullish Themes
- Bearish Themes
- Neutral / Mixed Themes
- Source-Backed Posts
- Overall Sentiment
- Caveats
- Follow-Up

Source integrity audit:

```text
wiki/analysis/audits/Source Integrity Audit YYYY-MM-DD.md
```

Required sections:

- Scope
- High Severity Findings
- Medium Severity Findings
- Low Severity Findings
- Chart / Table Checks
- Source Gap Summary
- Fixes Applied
- Follow-Up
