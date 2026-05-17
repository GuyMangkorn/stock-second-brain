# Entity Template

Use this as the target shape for `wiki/entities/TICKER.md`.

```markdown
---
type: entity
ticker: TICKER
company: Company Name
market:
currency:
period_type:
reporting_scope:
latest_period:
latest_period_end:
latest_total_revenue_usd_m:
latest_net_income_usd_m:
source_gap_count: 0
source_gaps: []
source_notes: []
normalized_markdown: raw/financials/TICKER_fundamentals.md
normalized_json:
tags:
  - entity/company
  - ticker/TICKER
---

# TICKER - Company Name

## Snapshot

| Item | Value |
|---|---|
| Ticker | TICKER |
| Company | Company Name |
| Market |  |
| Currency |  |
| Latest period |  |
| Reporting scope |  |
| Normalized file | [[TICKER_fundamentals]] |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings |  |  |
| 2 | Earnings transcript |  |  |
| 3 | Financial statements / metrics |  |  |
| 4 | News / web context |  |  |

## Business Model

## Segments / Revenue Mix

## Financial Facts

## Charts

Charts should use only verified values from the financial facts table or linked
normalized file. Keep quarterly, YTD, annual, segment, cash-flow, and balance
sheet charts separated.

## Transcript / Management Commentary

## Thesis

### Bull Case

### Bear Case

### Key Debate

## Risks

## Catalysts

## Valuation Watch Items

## Reports / Source Notes

## Follow-Up

## Missing / Unverified Data
```
