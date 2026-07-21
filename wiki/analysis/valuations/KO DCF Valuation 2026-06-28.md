---
type: analysis
analysis_type: dcf-valuation
ticker: KO
company: The Coca-Cola Company
date: 2026-06-28
currency: USD
source_files:
  - wiki/entities/KO.md
  - raw/financials/KO_fundamentals.md
  - raw/imports/KO_latest_results_source.md
  - raw/imports/KO_market_quote_2026-06-28.md
tags:
  - analysis/dcf
  - ticker/KO
---

# KO DCF Valuation - 2026-06-28
Entity: [[KO]]

## Bottom Line

This DCF uses freshly checked price of USD 82.63 from the 2026-06-26 regular-session close, MarketWatch displayed market cap of USD 355.54B, official Q1 2026 cash and short-term investments of USD 11.083B, valuation debt of USD 43.890B, diluted shares of 4.314B, and company FY2026 free cash flow guidance of approximately USD 12.2B.

Base-case fair value is approximately **USD 51.53 per diluted share**, about **37.6% below** the fresh price. Even the bull scenario reaches only about **USD 80.57**, still slightly below the market price and highly sensitive to WACC / terminal growth.

Action implication: **WAIT / AVOID-new-capital at current price**. KO is a high-quality defensive brand compounder, but current valuation already prices in a large amount of quality and FCF normalization.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/KO.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized facts | `raw/financials/KO_fundamentals.md` | Q1 2026 financials, FY2025 annual baseline, FCF, cash, debt, shares, guidance. |
| Latest results source note | `raw/imports/KO_latest_results_source.md` | Source map and raw extraction. |
| Market quote source note | `raw/imports/KO_market_quote_2026-06-28.md` | Fresh current price and market cap check. |
| KO Q1 2026 Form 10-Q | https://investors.coca-colacompany.com/filings-reports/all-sec-filings/content/0001628280-26-028802/ko-20260403.htm | Q1 statements, balance sheet, share count, cash flow. |
| KO Q1 2026 earnings release | https://investors.coca-colacompany.com/news-events/press-releases/detail/1158/coca-cola-reports-first-quarter-2026-results-and-updates-full-year-guidance | FY2026 guidance and official result commentary. |
| KO FY2025 Form 10-K | https://investors.coca-colacompany.com/filings-reports/all-sec-filings/content/0001628280-26-010047/ko-20251231.htm | Annual baseline and historical FCF. |
| MarketWatch KO quote page | https://www.marketwatch.com/investing/stock/ko | Fresh price and market cap checked 2026-06-28 Asia/Bangkok. |

## Input Table

All financial-statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 82.63 | MarketWatch close on 2026-06-26; checked 2026-06-28 Asia/Bangkok. |
| Market capitalization displayed by source | USD 355.54B | MarketWatch KO quote page. |
| Market capitalization calculated from filing shares | USD 355.51B | USD 82.63 * 4,302.482M common shares outstanding. |
| Shares outstanding | 4,302.482M | KO Q1 2026 Form 10-Q shares outstanding at 2026-04-17. |
| Diluted shares used for DCF | 4,314M | KO Q1 2026 Form 10-Q diluted weighted-average shares. |
| Cash and cash equivalents | 9.316 | KO Q1 2026 Form 10-Q. |
| Short-term investments | 1.767 | KO Q1 2026 Form 10-Q. |
| Cash and short-term investments | 11.083 | 9.316 + 1.767. |
| Loans and notes payable | 0.332 | KO Q1 2026 Form 10-Q. |
| Current maturities of long-term debt | 4.493 | KO Q1 2026 Form 10-Q. |
| Long-term debt | 39.065 | KO Q1 2026 Form 10-Q. |
| Total debt used for valuation | 43.890 | 0.332 + 4.493 + 39.065. |
| Net debt used in DCF | 32.807 | 43.890 - 11.083. |
| FY2025 simple FCF | 5.296 | FY2025 operating cash flow 7.408 - capex 2.112. |
| Q1 2026 simple FCF | 1.755 | Q1 operating cash flow 2.021 - capex 0.266. |
| FY2026 FCF guidance | approximately 12.2 | KO Q1 2026 earnings release. |
| FY2026 organic revenue guidance | 5% to 6% | KO Q1 2026 earnings release. |
| FY2026 comparable currency-neutral EPS growth guidance | 8% to 10% | KO Q1 2026 earnings release. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | USD 11.0B | USD 12.2B FY2026 guidance | USD 12.5B |
| Year 1 FCF growth / level | Below guide | Company guidance | Slightly above guide |
| Year 2 FCF growth | 2.0% | 5.0% | 6.0% |
| Year 3 FCF growth | 2.0% | 4.0% | 5.0% |
| Year 4 FCF growth | 2.0% | 3.0% | 4.0% |
| Year 5 FCF growth | 2.0% | 3.0% | 4.0% |
| WACC | 8.5% | 7.5% | 6.5% |
| Terminal growth | 1.5% | 2.5% | 3.0% |

WACC basis: vault reference range for Consumer Staples is 7%-8%. Base WACC uses 7.5% because KO has defensive brand quality but also meaningful net debt and valuation sensitivity. Bear uses 8.5% for rate / premium-multiple compression risk. Bull uses 6.5% for a best-quality defensive compounder scenario.

Terminal growth basis: mature developed-market compounder range is 2.0%-3.0%. Base uses 2.5%; bull uses 3.0% and should be treated as premium-quality sensitivity, not conservative underwriting.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| Year 1 | 11.000 | 12.200 | 12.500 |
| Year 2 | 11.220 | 12.810 | 13.250 |
| Year 3 | 11.440 | 13.322 | 13.913 |
| Year 4 | 11.670 | 13.722 | 14.469 |
| Year 5 | 11.900 | 14.134 | 15.048 |

Base case rationale: FY2026 FCF guidance is source-backed and much higher than FY2025 simple FCF. The model gives KO credit for FCF normalization but does not assume high-single-digit FCF growth indefinitely.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 82.63 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 8.5% | 1.5% | 44.960 | 114.754 | 159.714 | 32.807 | 126.907 | 29.42 | -64.4% |
| Base | 7.5% | 2.5% | 53.278 | 201.822 | 255.100 | 32.807 | 222.293 | 51.53 | -37.6% |
| Bull | 6.5% | 3.0% | 57.167 | 323.216 | 380.383 | 32.807 | 347.576 | 80.57 | -2.5% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 6.5% | 59.29 | 66.37 | 75.46 |
| 7.5% | 47.07 | 51.53 | 56.98 |
| 8.5% | 38.61 | 41.64 | 45.22 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| Forward FCF yield on market cap | 3.43% | Low yield for new capital; price is demanding. |
| Forward EV / guided FCF | 31.83x | Requires durable growth, FCF normalization, and premium terminal assumptions. |
| Net debt / FY2026 guided FCF | 2.69x | Manageable for KO, but material enough to matter in equity value. |
| FY2025 simple FCF | USD 5.296B | Shows why FY2026 guidance must convert before treating normalized FCF as proven. |
| Q1 2026 simple FCF | USD 1.755B | Positive start, but not enough alone to validate full-year USD 12.2B. |
| Base DCF terminal value share of EV | 79.1% | High but below the 85%-90% warning threshold. |
| Bull DCF terminal value share of EV | 85.0% | Near warning threshold; bull value is highly terminal-assumption sensitive. |

## What Would Change The Valuation

- Price pullback that lifts FY2026 guided FCF yield materially above current 3.43%.
- Q2 / FY2026 results confirming that operating cash flow is tracking toward USD 14.4B and FCF toward USD 12.2B.
- Evidence that organic revenue growth can stay above the 5%-6% FY2026 guidance range without margin pressure.
- Faster net debt reduction or lower WACC / interest-rate backdrop.
- Peer multiple compression or expansion among global beverage / consumer staples companies.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Official Q1 2026 earnings call transcript text | ไม่พบข้อมูลที่ยืนยันได้ | Limits management Q&A detail behind guidance and margin bridge. |
| Full FY2026 actual FCF | not disclosed | DCF relies on guidance, not completed annual cash flow. |
| Detailed bridge from FY2025 FCF to FY2026 guided FCF | not disclosed | FY2026 guidance is much higher than FY2025 actual simple FCF. |
| Product/category-level profitability | not disclosed | Cannot underwrite margin by category. |
| Real-time quote after 2026-06-26 close | ไม่พบข้อมูลที่ยืนยันได้ | 2026-06-28 is a Sunday; refresh before future action changes. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Updated `wiki/entities/KO.md` with valuation watch items and report link. Core action read is `WAIT / AVOID-new-capital`, because source-backed base and bull DCF scenarios do not provide enough margin of safety at the current price.
