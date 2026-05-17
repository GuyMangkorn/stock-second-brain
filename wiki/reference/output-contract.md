# Output Contract

This page defines the expected shape for durable outputs.

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
