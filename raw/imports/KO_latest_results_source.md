---
type: source-note
ticker: KO
company: The Coca-Cola Company
source_kind: latest-results
search_date: 2026-06-28
reporting_scope: Q1 2026 and FY2025 annual baseline
currency: USD
normalized_output: raw/financials/KO_fundamentals.md
entity: "[[KO]]"
tags:
  - source/latest-results
  - ticker/KO
---

# KO - Latest Results Source

## Source Map

| Priority | Source | URL / Path | Publication Date | Notes |
|---:|---|---|---|---|
| 1 | The Coca-Cola Company Q1 2026 Form 10-Q | https://investors.coca-colacompany.com/filings-reports/all-sec-filings/content/0001628280-26-028802/ko-20260403.htm | 2026-04-28 | Primary filing for Q1 2026 income statement, balance sheet, cash flow, segment data, debt, and share count. |
| 1 | The Coca-Cola Company Q1 2026 earnings release / Form 8-K exhibit | https://investors.coca-colacompany.com/news-events/press-releases/detail/1158/coca-cola-reports-first-quarter-2026-results-and-updates-full-year-guidance | 2026-04-28 | Official results summary, organic revenue / comparable EPS, cash flow, and FY2026 guidance. |
| 1 | The Coca-Cola Company FY2025 Form 10-K | https://investors.coca-colacompany.com/filings-reports/all-sec-filings/content/0001628280-26-010047/ko-20251231.htm | 2026-02-23 | Annual baseline, business model, annual revenue / cash flow / balance sheet, segment revenue, and risk context. |
| 2 | Company IR transcript PDF link | https://d1io3yog0oux5.cloudfront.net/_68ea4ba5f00600d452a80d1f5d4ff29b/cocacolacompany/db/761/4031/pdf/Q1+2026+KO+Transcript.pdf | 2026-04-28 | Official transcript link was discovered on the IR result page, but direct fetch returned access blocked in this session; not used as extracted evidence. |
| 3 | MarketWatch KO quote page | https://www.marketwatch.com/investing/stock/ko | Checked 2026-06-28 | Fresh market-data source for P11/P13 price and market cap; saved separately as `raw/imports/KO_market_quote_2026-06-28.md`. |

## Reporting Scope

- Company: The Coca-Cola Company.
- Ticker: KO.
- Market: NYSE.
- Latest verified reporting period: Q1 2026, quarter ended 2026-04-03.
- Annual baseline: FY2025, year ended 2025-12-31.
- Fiscal calendar: fiscal year ended December 31; Q1 2026 Form 10-Q covers the quarter ended April 3, 2026.
- Reporting basis: unaudited US GAAP for Q1 2026; FY2025 audited US GAAP annual baseline.

## Currency / Units

- Currency: USD.
- Units: USD millions unless stated otherwise.
- Per-share metrics are USD per share.
- Share counts are millions of shares unless stated otherwise.
- Free cash flow uses the vault formula `operating cash flow - capex spend`; capex is converted to positive spend when the filing reports it as a cash outflow.

## Extracted Facts

### Q1 2026 Official Results

| Metric | Q1 2026 | Q1 2025 | Source |
|---|---:|---:|---|
| Net operating revenues | 12,472 | 11,129 | Q1 2026 Form 10-Q. |
| Gross profit | 7,852 | 6,805 | Q1 2026 Form 10-Q. |
| Operating income | 4,359 | 2,542 | Q1 2026 Form 10-Q. |
| Income before income taxes | 4,790 | 2,885 | Q1 2026 Form 10-Q. |
| Consolidated net income | 3,966 | 2,403 | Q1 2026 Form 10-Q. |
| Net income attributable to shareowners of The Coca-Cola Company | 3,924 | 2,361 | Q1 2026 Form 10-Q. |
| Basic net income per share | 0.91 | 0.55 | Q1 2026 Form 10-Q. |
| Diluted net income per share | 0.91 | 0.55 | Q1 2026 Form 10-Q. |
| Diluted weighted-average shares | 4,314 | 4,309 | Q1 2026 Form 10-Q. |

### Q1 2026 Cash Flow

| Metric | Q1 2026 | Q1 2025 | Source |
|---|---:|---:|---|
| Net cash provided by / used in operating activities | 2,021 | (5,202) | Q1 2026 Form 10-Q. |
| Purchases of property, plant and equipment | 266 | 309 | Q1 2026 Form 10-Q; cash outflow converted to positive spend. |
| Simple free cash flow | 1,755 | (5,511) | Calculation: operating cash flow - capex spend. |

### Q1 2026 Balance Sheet

| Metric | 2026-04-03 | 2025-12-31 | Source |
|---|---:|---:|---|
| Cash and cash equivalents | 9,316 | 8,081 | Q1 2026 Form 10-Q. |
| Short-term investments | 1,767 | 1,866 | Q1 2026 Form 10-Q. |
| Cash and short-term investments | 11,083 | 9,947 | Calculation from Q1 2026 Form 10-Q. |
| Total current assets | 30,384 | 28,005 | Q1 2026 Form 10-Q. |
| Total assets | 106,327 | 105,183 | Q1 2026 Form 10-Q. |
| Loans and notes payable | 332 | 4,926 | Q1 2026 Form 10-Q. |
| Current maturities of long-term debt | 4,493 | 4,477 | Q1 2026 Form 10-Q. |
| Long-term debt | 39,065 | 36,356 | Q1 2026 Form 10-Q. |
| Total debt used for valuation | 43,890 | 45,759 | Calculation: loans and notes payable + current maturities + long-term debt. |
| Total liabilities | 79,059 | 80,495 | Q1 2026 Form 10-Q. |
| Total equity | 27,268 | 24,688 | Q1 2026 Form 10-Q. |
| Common shares outstanding | 4,302.482 | 4,302.192 | Q1 2026 Form 10-Q, shares outstanding at 2026-04-17 and 2026-02-13. |

### Q1 2026 Segment Revenue

| Segment | Q1 2026 Net Operating Revenues | Q1 2025 Net Operating Revenues | Source |
|---|---:|---:|---|
| Europe, Middle East & Africa | 2,807 | 2,211 | Q1 2026 Form 10-Q. |
| Latin America | 1,678 | 1,538 | Q1 2026 Form 10-Q. |
| North America | 4,891 | 4,407 | Q1 2026 Form 10-Q. |
| Asia Pacific | 1,426 | 1,374 | Q1 2026 Form 10-Q. |
| Bottling Investments | 1,638 | 1,569 | Q1 2026 Form 10-Q. |
| Corporate | 32 | 30 | Q1 2026 Form 10-Q. |
| Total company | 12,472 | 11,129 | Q1 2026 Form 10-Q. |

### FY2025 Annual Baseline

| Metric | FY2025 | FY2024 | FY2023 | Source |
|---|---:|---:|---:|---|
| Net operating revenues | 47,061 | 47,061 | 45,754 | FY2025 Form 10-K. |
| Gross profit | 28,580 | 28,956 | 27,234 | FY2025 Form 10-K. |
| Operating income | 11,543 | 9,992 | 11,311 | FY2025 Form 10-K. |
| Net income attributable to shareowners | 10,631 | 10,714 | 10,714 | FY2025 Form 10-K. |
| Diluted EPS | 2.46 | 2.47 | 2.47 | FY2025 Form 10-K. |
| Operating cash flow | 7,408 | 6,805 | 11,599 | FY2025 Form 10-K. |
| Purchases of property, plant and equipment | 2,112 | 2,064 | 1,852 | FY2025 Form 10-K; cash outflow converted to positive spend. |
| Simple free cash flow | 5,296 | 4,741 | 9,747 | Calculation: operating cash flow - capex spend. |

## Transcript / Commentary

- CEO commentary in the official Q1 2026 release states that volume, revenues, and comparable EPS grew ahead of expectations, and that the company is increasing full-year 2026 organic revenue and comparable currency-neutral EPS guidance.
- Official Q1 2026 transcript PDF URL was discovered on the company IR result page, but direct access was blocked in this session. No transcript Q&A claims were extracted.
- Management commentary from non-official transcript providers was not used because the user requested official-source priority and the official release / filing were sufficient for P4/P11 source facts.

## Financial Tables

### Guidance

| Guidance item | Management outlook | Source |
|---|---|---|
| FY2026 organic revenue growth | 5% to 6% | Q1 2026 earnings release. |
| FY2026 comparable currency-neutral EPS growth | 8% to 10% | Q1 2026 earnings release. |
| FY2026 comparable EPS growth | approximately -1% to +1%, including currency headwind and structural headwind | Q1 2026 earnings release. |
| FY2026 operating cash flow | approximately USD 14.4B | Q1 2026 earnings release. |
| FY2026 capital expenditures | approximately USD 2.2B | Q1 2026 earnings release. |
| FY2026 free cash flow | approximately USD 12.2B | Q1 2026 earnings release; company-defined free cash flow from operating cash flow less capex. |
| Q2 2026 comparable net revenues impact from acquisitions, divestitures and structural changes | approximately 3% headwind | Q1 2026 earnings release. |
| Q2 2026 comparable EPS currency impact | approximately 5% tailwind | Q1 2026 earnings release. |

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Official Q1 2026 earnings call transcript text | ไม่พบข้อมูลที่ยืนยันได้ | Official PDF link was discovered but access was blocked in this session. |
| Product/category-level profitability | not disclosed | Reportable segment revenue is available; profitability below company level is not normalized here. |
| Unit case volume by segment in filing table format | not normalized | Press release provides growth commentary, but the normalized ingest uses verified financial-statement values. |
| Detailed bridge from FY2025 simple FCF to FY2026 FCF guidance | not disclosed | FY2025 OCF was pressured by working capital timing; FY2026 guidance is used as forward company outlook, not as historical fact. |
| Current price and market cap inside company filing | not disclosed | Fresh market check saved separately in `raw/imports/KO_market_quote_2026-06-28.md`. |

## Handoff For Ingest

- Normalize Q1 2026 and Q1 2025 income statement, cash flow, balance sheet, segment revenue, FY2025/FY2024/FY2023 annual baseline, and FY2026 guidance.
- Use Q1 2026 Form 10-Q as the primary source for statement values.
- Use FY2025 Form 10-K for annual trend and business model baseline.
- Use the Q1 2026 earnings release for guidance and non-GAAP / organic commentary, keeping those labels explicit.
- Use `raw/imports/KO_market_quote_2026-06-28.md` for current price, market cap, FCF yield, EV/FCF, and valuation memo inputs.
- Do not use the blocked official transcript PDF as extracted evidence; record it under `Missing / Unverified Data`.
