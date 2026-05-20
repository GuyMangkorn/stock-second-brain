---
type: analysis
analysis_type: dcf-valuation
ticker: COST
company: Costco Wholesale Corporation
date: 2026-05-20
currency: USD
source_files:
  - wiki/entities/COST.md
  - raw/financials/COST_fundamentals.md
  - raw/imports/COST_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/COST
---

# COST DCF Valuation - 2026-05-20

## Bottom Line

DCF can be run because the required inputs were freshly checked or source-backed: current price, market cap, shares, cash, debt, FCF, and guidance/opening outlook. The main limitation is that Costco has not disclosed full-year FY2026 sales, EPS, or FCF guidance in the reviewed official sources, so this model uses source-backed TTM FCF rather than inventing an FY2026 FCF guide.

Using TTM FCF of USD 9.099B, cash plus short-term investments of USD 18.240B, total debt used for valuation of USD 5.873B, diluted weighted-average shares of 444.468M, base WACC of 7.25%, terminal growth of 2.5%, and a five-year FCF growth path fading from 6.0% to 4.5%, base-case fair value is approximately USD 530.67 per diluted share.

Against the fresh close-price check of USD 1,094.32 on 2026-05-19, the base case implies about 51.5% downside. Costco is a superb business, but current valuation requires exceptional compounding and/or a very low required return. Even the bull case in this memo remains below the latest close.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/COST.md` | Business model, source map, thesis, risks. |
| Normalized facts | `raw/financials/COST_fundamentals.md` | Q2/H1 FY2026 financials, balance sheet, FCF, shares, market data, ratios, and guidance/opening outlook. |
| Latest source note | `raw/imports/COST_latest_results_source.md` | Local source extraction and ingest provenance. |
| SEC Q2 FY2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/909832/000090983226000029/cost-20260215.htm | Official quarterly facts, shares, cash, debt, OCF, capex, and membership data. |
| Costco Q2 FY2026 earnings release | https://investor.costco.com/news/news-details/2026/Costco-Wholesale-Corporation-Reports-Second-Quarter-and-Year-to-Date-Operating-Results-for-Fiscal-2026-and-February-Sales-Results/default.aspx | Official Q2/H1 results and comparable sales. |
| Costco April 2026 sales release | https://investor.costco.com/news/news-details/2026/Costco-Wholesale-Corporation-Reports-April-Sales-Results/default.aspx | Latest official monthly sales context. |
| Costco FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm | FY2025/FY2024/FY2023 FCF baseline and business context. |
| Q2 FY2026 earnings call transcript | https://stockanalysis.com/stocks/cost/transcripts/529905-q2-2026/ | Management commentary for capex, openings, tariffs, and digital growth. |
| StockAnalysis COST transcripts / quote page | https://stockanalysis.com/stocks/cost/transcripts/ | Fresh price check, checked 2026-05-20. |
| StockScan COST price history | https://stockscan.io/stocks/COST/price-history | Quote cross-check, checked 2026-05-20. |

## Input Table

All company financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 1,094.32 | StockAnalysis quote page, close for 2026-05-19; checked 2026-05-20. |
| Pre-market quote check | USD 1,089.90 | StockAnalysis quote page, 2026-05-20 08:02 EDT. |
| StockScan cross-check | USD 1,085.14 | StockScan price-history page, checked 2026-05-20. |
| Implied market cap | USD 485.54B | 1,094.32 * 443.692M SEC common shares. |
| Implied enterprise value | USD 473.17B | Market cap 485.54 - cash/STI 18.240 + total debt 5.873. |
| Diluted shares used for DCF | 0.444468B | SEC Form 10-Q, H1 FY2026 diluted weighted-average shares. |
| SEC common shares outstanding | 0.443692B | SEC Form 10-Q equity statement, 2026-02-15. |
| Cash and cash equivalents | 17.383 | SEC Form 10-Q. |
| Short-term investments | 0.857 | SEC Form 10-Q. |
| Cash plus short-term investments | 18.240 | 17.383 + 0.857. |
| Long-term debt carrying value including current portion before discounts/costs | 5.775 | SEC Form 10-Q Note 4. |
| Short-term borrowings | 0.098 | SEC Form 10-Q liquidity section. |
| Total debt used for valuation | 5.873 | 5.775 + 0.098. |
| Net cash using cash plus STI | 12.367 | 18.240 - 5.873. |
| H1 FY2026 operating cash flow | 7.684 | SEC Form 10-Q. |
| H1 FY2026 capex spend | 2.815 | SEC Form 10-Q; additions to PP&E converted to positive spend. |
| H1 FY2026 free cash flow | 4.869 | 7.684 - 2.815. |
| FY2025 free cash flow | 7.837 | FY2025 Form 10-K calculation: 13.335 - 5.498. |
| H1 FY2025 free cash flow | 3.607 | SEC Form 10-Q calculation: 6.008 - 2.401. |
| TTM free cash flow | 9.099 | 7.837 - 3.607 + 4.869. |
| FY2026 capex outlook | about 6.5 | SEC Form 10-Q / Q2 transcript. |
| FY2026 full-year sales / EPS / FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Not found in reviewed official sources. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Year 1 FCF anchor | 9.099 | 9.099 | 9.099 |
| Year 1 FCF growth | 3.0% | 6.0% | 8.0% |
| Year 2 FCF growth | 3.0% | 6.0% | 8.0% |
| Year 3 FCF growth | 3.0% | 5.5% | 7.0% |
| Year 4 FCF growth | 2.5% | 5.0% | 6.0% |
| Year 5 FCF growth | 2.5% | 4.5% | 5.5% |
| WACC | 8.0% | 7.25% | 6.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |

WACC basis: Consumer Staples range in `wiki/reference/valuation-assumptions.md` is 7%-8%. Base WACC is 7.25% because Costco has defensive demand, scale, renewal-based membership economics, and net cash, offset by retail margin thinness, capex-heavy expansion, tariff uncertainty, and current valuation risk.

Terminal growth basis: 2.5% sits inside the mature developed-market compounder range. The bull case uses 3.0% only if membership growth, unit openings, and digital growth remain durable without major margin pressure.

## FCF Projection

Base case amounts are USD billions.

| Year | FCF | Growth |
|---:|---:|---:|
| Year 1 | 9.645 | 6.0% |
| Year 2 | 10.223 | 6.0% |
| Year 3 | 10.785 | 5.5% |
| Year 4 | 11.325 | 5.0% |
| Year 5 | 11.835 | 4.5% |

Base rationale: the model gives Costco credit for strong H1 FY2026 FCF, high renewal rates, unit expansion, and digitally-enabled sales growth, but fades growth because capex remains high and valuation cannot rely indefinitely on double-digit FCF growth.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | Enterprise Value | Cash + STI | Total Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 1,094.32 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 8.0% | 2.0% | 160.3 | 18.2 | (5.9) | 172.7 | 388.50 | -64.5% |
| Base | 7.25% | 2.5% | 223.5 | 18.2 | (5.9) | 235.9 | 530.67 | -51.5% |
| Bull | 6.5% | 3.0% | 319.4 | 18.2 | (5.9) | 331.8 | 746.41 | -31.8% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 6.25% | 600.46 | 666.00 | 751.72 |
| 7.25% | 490.32 | 530.67 | 580.51 |
| 8.25% | 415.45 | 442.43 | 474.55 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 1.87% | Very low current cash yield; price assumes exceptional compounding. |
| Market EV / TTM FCF | 52.00x | Premium multiple far above what the base DCF supports. |
| Implied TTM P/E | 56.91x | Earnings multiple is also demanding despite strong quality. |
| Net cash / TTM FCF | 1.36x | Balance sheet is a real strength. |
| Base terminal value share of EV | 80.5% | High but below the 85%-90% warning zone. |
| Bull terminal value share of EV | 85.4% | Bull case is heavily terminal-value-sensitive. |

## What Would Change The Valuation

- Current price falls materially while membership, comps, and FCF remain intact.
- FY2026 actual FCF materially exceeds the current TTM FCF anchor without unsustainable working-capital benefit.
- Costco sustains high-single-digit adjusted comp growth and 20%+ digitally-enabled growth.
- Unit openings generate attractive returns without requiring capex materially above guidance.
- Tariff impact proves immaterial or gets offset without hurting traffic.
- Market required return for defensive compounders stays structurally lower than this model assumes.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| FY2026 full-year actual results | not disclosed | Q2/H1 FY2026 was the latest official quarterly filing found. |
| FY2026 full-year sales / EPS guidance | ไม่พบข้อมูลที่ยืนยันได้ | Limits forward revenue and earnings cross-checks. |
| FY2026 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | DCF uses source-backed TTM FCF instead of invented FY2026 FCF. |
| Company-hosted written transcript | ไม่พบข้อมูลที่ยืนยันได้ | Lower confidence in exact management wording from call. |
| Segment profitability by category/geography | not disclosed | Limits segment-specific valuation and margin analysis. |
| Tariff refund / net tariff impact | partially disclosed | Could affect gross margin and pricing assumptions. |
| Market data after regular-market open on 2026-05-20 | not verified | Future action calls should refresh price and market cap. |
| Investor-specific required return | not provided | Could change whether COST is acceptable as a long-term hold despite limited DCF upside. |

## Entity Update

Updated `wiki/entities/COST.md` with this valuation memo link and valuation watch items. The valuation pushes the action read toward AVOID / WAIT for new capital at current price, despite high business quality.
