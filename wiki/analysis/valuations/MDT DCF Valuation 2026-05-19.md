---
type: analysis
analysis_type: dcf-valuation
ticker: MDT
company: Medtronic plc
date: 2026-05-19
currency: USD
source_files:
  - wiki/entities/MDT.md
  - raw/financials/MDT_fundamentals.md
  - raw/imports/MDT_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/MDT
---

# MDT DCF Valuation - 2026-05-19

## Bottom Line

DCF can be run because the required inputs were freshly checked or source-backed: current price, market cap, shares, cash plus investments, debt, FCF, and guidance. The key limitation is that Medtronic has not disclosed FY26 full-year FCF guidance in the extracted official Q3 sources, so this model uses a source-backed TTM FCF calculation rather than an invented FY26 FCF guide.

Using TTM FCF of USD 5.410B, cash plus investments of USD 8.383B, total debt of USD 28.071B, diluted weighted-average shares of 1.2895B, base WACC of 8.5%, terminal growth of 2.5%, and a five-year FCF growth path fading from 4.0% to 2.5%, base-case fair value is approximately USD 59.41 per diluted share.

Against the fresh close-price check of USD 77.32 on 2026-05-18, the base case implies about 23% downside. MDT is a quality medtech franchise, but current price still requires either stronger FCF growth, lower WACC, or clearer post-separation economics to provide margin of safety.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/MDT.md` | Business model, source map, thesis, risks. |
| Normalized facts | `raw/financials/MDT_fundamentals.md` | Q3 FY26 financials, balance sheet, FCF, shares, segment data, and guidance. |
| Latest source note | `raw/imports/MDT_latest_results_source.md` | Local source extraction and ingest provenance. |
| SEC Q3 FY26 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1613103/000162828026011107/mdt-20260123.htm | Official quarterly facts, shares, cash, investments, debt, OCF, capex. |
| Medtronic Q3 FY26 earnings release | https://news.medtronic.com/2026-02-17-Medtronic-reports-strong-third-quarter-fiscal-2026-results-with-highest-enterprise-revenue-growth-in-10-quarters | Guidance, segment revenue, and FCF reconciliation. |
| Medtronic FY2025 Q4/full-year release | https://news.medtronic.com/2025-05-21-Medtronic-reports-strong-finish-to-its-fiscal-year-with-its-fourth-quarter-financial-results-announces-dividend-increase | FY2025/FY2024/FY2023 FCF baseline. |
| StockAnalysis MDT statistics page | https://stockanalysis.com/stocks/mdt/statistics/ | Fresh price, market cap, enterprise value, and shares; checked 2026-05-19. |

## Input Table

All company financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 77.32 | StockAnalysis, close for 2026-05-18; checked 2026-05-19. |
| Premarket quote | USD 77.36 | StockAnalysis, 2026-05-19 08:01 AM EDT. |
| Market cap | USD 99.27B | StockAnalysis. |
| Enterprise value | USD 118.81B | StockAnalysis. |
| Diluted shares used for DCF | 1.2895B | SEC Form 10-Q, Q3 FY26 diluted weighted-average shares. |
| SEC ordinary shares outstanding | 1.2839B | SEC Form 10-Q, 2026-02-18. |
| Cash and cash equivalents | 1.147 | SEC Form 10-Q. |
| Investments | 7.236 | SEC Form 10-Q. |
| Cash plus investments | 8.383 | 1.147 + 7.236. |
| Current debt obligations | 0.191 | SEC Form 10-Q. |
| Long-term debt | 27.880 | SEC Form 10-Q. |
| Total debt | 28.071 | 0.191 + 27.880. |
| Net debt using cash plus investments | 19.688 | 28.071 - 8.383. |
| 9M FY26 operating cash flow | 4.757 | Medtronic Q3 FY26 release / SEC Form 10-Q. |
| 9M FY26 capex spend | 1.416 | Medtronic Q3 FY26 release; PP&E additions converted to positive spend. |
| 9M FY26 free cash flow | 3.341 | 4.757 - 1.416. |
| FY2025 free cash flow | 5.185 | Medtronic FY2025 Q4/full-year release. |
| 9M FY25 free cash flow | 3.116 | Medtronic Q3 FY26 release. |
| TTM free cash flow | 5.410 | 5.185 - 3.116 + 3.341. |
| FY26 organic revenue growth guidance | approximately 5.5% | Medtronic Q3 FY26 release. |
| FY26 non-GAAP diluted EPS guidance | USD 5.62 to USD 5.66 | Medtronic Q3 FY26 release. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Year 1 FCF anchor | 5.410 | 5.410 | 5.410 |
| Year 1 FCF growth | 2.0% | 4.0% | 6.0% |
| Year 2 FCF growth | 2.0% | 4.0% | 5.5% |
| Year 3 FCF growth | 2.0% | 3.5% | 5.0% |
| Year 4 FCF growth | 2.0% | 3.0% | 4.5% |
| Year 5 FCF growth | 2.0% | 2.5% | 4.0% |
| WACC | 9.5% | 8.5% | 7.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |

WACC basis: Health Care range in `wiki/reference/valuation-assumptions.md` is 8%-10%. Base WACC is 8.5% because MDT is a diversified large-cap medtech leader, but tariff, regulatory, product-cycle, litigation, and Diabetes separation risks keep it above the lower end.

Terminal growth basis: 2.5% is inside the mature developed-market compounder range. The bull case uses 3.0% only if product cycles and FCF conversion improve after FY2026.

## FCF Projection

Base case amounts are USD billions.

| Year | FCF | Growth |
|---:|---:|---:|
| Year 1 | 5.626 | 4.0% |
| Year 2 | 5.851 | 4.0% |
| Year 3 | 6.056 | 3.5% |
| Year 4 | 6.238 | 3.0% |
| Year 5 | 6.394 | 2.5% |

Base rationale: the model starts from source-backed TTM FCF and fades below current FY26 organic revenue guidance because FCF conversion, tariff impact, separation cost, and GAAP/non-GAAP conversion are still watch items.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | Enterprise Value | Cash + Investments | Total Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 77.32 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 9.5% | 2.0% | 73.6 | 8.4 | (28.1) | 53.9 | 41.79 | -46.0% |
| Base | 8.5% | 2.5% | 96.3 | 8.4 | (28.1) | 76.6 | 59.41 | -23.2% |
| Bull | 7.5% | 3.0% | 135.5 | 8.4 | (28.1) | 115.8 | 89.84 | 16.2% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 7.5% | 67.63 | 74.38 | 82.63 |
| 8.5% | 54.82 | 59.41 | 64.83 |
| 9.5% | 45.43 | 48.71 | 52.50 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 5.45% | Decent but not obviously cheap for a medtech name with execution risk. |
| Market EV / TTM FCF | 21.96x | Matches StockAnalysis EV/FCF context; not a deep-value multiple. |
| Net debt / TTM FCF | 3.64x | Manageable but material for equity value. |
| Base terminal value share of EV | 75.4% | High but below the 85%-90% warning zone. |
| FY26 non-GAAP EPS guide vs price | about 13.7x | Price / midpoint USD 5.64; cheaper on non-GAAP EPS than DCF, but GAAP/FCF conversion matters. |

## What Would Change The Valuation

- FY2026 actual FCF materially exceeds the current TTM FCF anchor.
- Diabetes separation creates clearer value without meaningful stranded costs.
- Cardiovascular growth sustains without higher reinvestment or margin drag.
- Tariff impact falls below the USD 185M assumption embedded in guidance.
- GAAP operating profit starts to follow organic revenue growth more cleanly.
- Current price falls toward or below base-case fair value while guidance remains intact.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| FY26 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | DCF uses source-backed TTM FCF instead of invented FY26 FCF. |
| FY26 full-year actual results | not disclosed | Q4 FY26 results scheduled for 2026-06-03. |
| Diabetes standalone post-separation financials | ไม่พบข้อมูลที่ยืนยันได้ | Limits sum-of-the-parts and stranded-cost analysis. |
| Product/division-level profitability | not disclosed | Limits granular segment valuation. |
| Full Q&A transcript review | not normalized | Management commentary is based on official release and filings, not full Q&A signal extraction. |
| Investor-specific required return | not provided | Could change whether MDT is acceptable as a hold despite limited DCF upside. |

## Entity Update

Updated `wiki/entities/MDT.md` with this valuation memo link and valuation watch items. The valuation pushes the action read toward wait/watchlist for new capital at current price.
