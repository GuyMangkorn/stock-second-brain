---
type: dashboard
updated: 2026-05-19
---

# Stock Second Brain Dashboard

## Latest Work

- 2026-05-19: Ran full new-ticker decision-grade flow for `[[JNJ]]`: created
  `[[JNJ_latest_results_source]]`, normalized `[[JNJ_fundamentals]]`, added
  `[[JNJ]]`, and created `[[JNJ DCF Valuation 2026-05-19]]` plus
  `[[JNJ Decision Memo 2026-05-19]]` with a WAIT / AVOID-new-capital action
  read.
- 2026-05-18: Ran full new-ticker decision-grade flow for `[[GOOGL]]`: created
  `[[GOOGL_latest_results_source]]`, normalized `[[GOOGL_fundamentals]]`, added
  `[[GOOGL]]`, and created `[[GOOGL DCF Valuation 2026-05-18]]` plus
  `[[GOOGL Decision Memo 2026-05-18]]` with a WAIT / AVOID-new-capital action
  read.
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
| [[JNJ]] | JNJ | Johnson & Johnson | NYSE | Q1 2026 | 5 |
| [[GOOGL]] | GOOGL | Alphabet Inc. | Nasdaq | Q1 2026 | 6 |
| [[MSFT]] | MSFT | Microsoft Corporation | Nasdaq | FY26 Q3 | 5 |

## Source Gaps

| Entity | Missing / Unverified |
|---|---|
| [[JNJ]] | Product-level revenue for ICOTYDE and IMAAVY is not disclosed; product-level profitability by brand is not disclosed; GAAP forward guidance is not provided; FY2026 full-year actual results are unavailable; sequential quarterly trend across recent quarters has not been normalized. |
| [[GOOGL]] | Product-level AI revenue/margins and TPU economics are not disclosed; FY2026 full-year results are unavailable; 2027 capex amount is not quantified; Q1 2026 net income includes large equity-security gains; investor-specific tax basis and position size are not provided. |
| [[MSFT]] | Current market price and valuation multiples require fresh market-data check; product-level FY26 Q3 revenue not normalized where only growth rates were disclosed; exact AI product revenue/margins are not disclosed; OpenAI-specific Azure economics and concentration are not disclosed with enough granularity; full annual FY2026 data is not yet available. |

## Raw Source Queue

| Source Note | Ticker | Source Kind | Scope | Normalized Output |
|---|---|---|---|---|
| [[JNJ_latest_results_source]] | JNJ | latest-results | Q1 2026 fiscal first quarter ended 2026-03-29 plus FY2025 annual baseline | [[JNJ_fundamentals]] |
| [[GOOGL_latest_results_source]] | GOOGL | latest-results | Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline | [[GOOGL_fundamentals]] |
| [[MSFT_latest_results_source]] | MSFT | latest-results | FY26 Q3 and nine months ended 2026-03-31 | [[MSFT_fundamentals]] |
| [[MSFT_company_deep_dive_2026-05-17]] | MSFT | company-deep-dive | FY2025 annual baseline plus FY26 Q3 update | [[MSFT]], [[MSFT_fundamentals]] |

Agent maintenance note: keep these Markdown tables synced whenever entity,
source-note, or fundamentals files change.

## Follow-Up

- For `[[JNJ]]`, refresh after Q2 2026 results with attention to FCF, net debt,
  STELARA erosion, MedTech tariff/separation pressure, product launch
  disclosure, and FY2026 guidance changes.
- For `[[GOOGL]]`, refresh after Q2 2026 results with special attention to
  FCF, capex, 2027 capex guidance, Google Cloud backlog recognition, Google
  Cloud margins, and AI/TPU economics.
- For `[[MSFT]]`, freshly check market price and valuation multiples before
  making valuation claims.
- After FY26 Q4 / FY2026 10-K, update full-year financials and segment trends.
- Track AI product revenue disclosure, OpenAI-related exposure, Microsoft Cloud
  gross margin, capex, depreciation, and finance lease impact in future updates.
