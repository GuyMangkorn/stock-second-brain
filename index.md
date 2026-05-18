---
type: dashboard
updated: 2026-05-18
---

# Stock Second Brain Dashboard

## Latest Work

- 2026-05-18: Created `[[MSFT Decision Memo 2026-05-18]]` with a WAIT-for-new-capital / HOLD-existing-core action read, using vault facts plus freshly checked market valuation data.
- 2026-05-17: Created `[[MSFT_latest_results_source]]`, normalized
  `[[MSFT_fundamentals]]`, and added `[[MSFT]]` from Microsoft FY26 Q3 official
  sources.
- 2026-05-17: Added `[[MSFT_company_deep_dive_2026-05-17]]` and expanded
  `[[MSFT]]` into an official-source company deep dive with FY2025 annual
  baseline, revenue mix, moat, risks, catalysts, valuation watch items, and
  unanswered questions.

## Active Entities

| Entity | Ticker | Company | Market | Latest Period | Source Gaps |
|---|---|---|---|---|---:|
| [[MSFT]] | MSFT | Microsoft Corporation | Nasdaq | FY26 Q3 | 5 |

## Source Gaps

| Entity | Missing / Unverified |
|---|---|
| [[MSFT]] | Current market price and valuation multiples require fresh market-data check; product-level FY26 Q3 revenue not normalized where only growth rates were disclosed; exact AI product revenue/margins are not disclosed; OpenAI-specific Azure economics and concentration are not disclosed with enough granularity; full annual FY2026 data is not yet available. |

## Raw Source Queue

| Source Note | Ticker | Source Kind | Scope | Normalized Output |
|---|---|---|---|---|
| [[MSFT_latest_results_source]] | MSFT | latest-results | FY26 Q3 and nine months ended 2026-03-31 | [[MSFT_fundamentals]] |
| [[MSFT_company_deep_dive_2026-05-17]] | MSFT | company-deep-dive | FY2025 annual baseline plus FY26 Q3 update | [[MSFT]], [[MSFT_fundamentals]] |

Agent maintenance note: keep these Markdown tables synced whenever entity,
source-note, or fundamentals files change.

## Follow-Up

- For `[[MSFT]]`, freshly check market price and valuation multiples before
  making valuation claims.
- After FY26 Q4 / FY2026 10-K, update full-year financials and segment trends.
- Track AI product revenue disclosure, OpenAI-related exposure, Microsoft Cloud
  gross margin, capex, depreciation, and finance lease impact in future updates.
