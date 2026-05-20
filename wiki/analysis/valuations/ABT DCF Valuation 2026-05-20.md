---
type: analysis
analysis_type: dcf-valuation
ticker: ABT
company: Abbott Laboratories
date: 2026-05-20
currency: USD
source_files:
  - wiki/entities/ABT.md
  - raw/financials/ABT_fundamentals.md
  - raw/imports/ABT_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/ABT
---

# ABT DCF Valuation - 2026-05-20

## Bottom Line

DCF can be run because the required inputs were freshly checked or source-backed: current price, market cap, shares, cash, debt, FCF, and guidance. The main limitation is that Abbott has not disclosed FY2026 full-year FCF guidance in the extracted official Q1 sources, so this model uses a source-backed TTM FCF calculation rather than inventing an FY2026 FCF guide.

Using TTM FCF of USD 7.378B, cash plus short-term investments of USD 7.295B, total debt of USD 34.047B, diluted weighted-average shares of 1.747073B, base WACC of 8.5%, terminal growth of 2.5%, and a five-year FCF growth path fading from 5.0% to 3.5%, base-case fair value is approximately USD 63.17 per diluted share.

Against the fresh close-price check of USD 88.82 on 2026-05-19, the base case implies about 29% downside. ABT remains a quality diversified health care franchise, but current price needs either stronger FCF growth, faster debt paydown, or lower discount-rate assumptions to create margin of safety.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/ABT.md` | Business model, source map, thesis, risks. |
| Normalized facts | `raw/financials/ABT_fundamentals.md` | Q1 2026 financials, balance sheet, FCF, shares, segment data, and guidance. |
| Latest source note | `raw/imports/ABT_latest_results_source.md` | Local source extraction and ingest provenance. |
| SEC Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1800/000162828026028357/abt-20260331.htm | Official quarterly facts, shares, cash, debt, OCF, and capex. |
| Abbott Q1 2026 earnings release | https://abbott.mediaroom.com/2026-04-16-Abbott-Reports-First-Quarter-2026-Results-Updates-Guidance-to-Reflect-Acquisition-of-Exact-Sciences?asPDF=1 | Guidance, segment/category revenue, and management commentary. |
| Abbott FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1800/000162828026010185/abt-20251231.htm | FY2025/FY2024/FY2023 FCF baseline. |
| StockAnalysis ABT statistics page | https://stockanalysis.com/stocks/abt/statistics/ | Fresh price, market cap, enterprise value, and market metrics; checked 2026-05-20. |
| MarketBeat ABT quote page | https://www.marketbeat.com/stocks/NYSE/ABT/ | Cross-check for quote, market cap, and shares; checked 2026-05-20. |

## Input Table

All company financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 88.82 | StockAnalysis, close for 2026-05-19; checked 2026-05-20. |
| MarketBeat quote cross-check | USD 88.81 close / USD 88.66 extended | MarketBeat, checked 2026-05-20. |
| Market cap | USD 154.71B | StockAnalysis. |
| Enterprise value | USD 181.55B | StockAnalysis. |
| Diluted shares used for DCF | 1.747073B | SEC Form 10-Q, Q1 2026 diluted weighted-average shares. |
| SEC common shares outstanding | 1.741812B | SEC Form 10-Q, 2026-03-31. |
| Cash and cash equivalents | 6.803 | SEC Form 10-Q. |
| Short-term investments | 0.492 | SEC Form 10-Q. |
| Cash plus short-term investments | 7.295 | 6.803 + 0.492. |
| Current portion of long-term debt | 4.409 | SEC Form 10-Q. |
| Long-term debt | 29.638 | SEC Form 10-Q. |
| Total debt | 34.047 | 4.409 + 29.638. |
| Net debt using cash plus short-term investments | 26.752 | 34.047 - 7.295. |
| Q1 2026 operating cash flow | 1.315 | SEC Form 10-Q. |
| Q1 2026 capex spend | 0.399 | SEC Form 10-Q; PP&E acquisitions converted to positive spend. |
| Q1 2026 free cash flow | 0.916 | 1.315 - 0.399. |
| FY2025 free cash flow | 7.395 | FY2025 Form 10-K calculation: 9.566 - 2.171. |
| Q1 2025 free cash flow | 0.933 | SEC Form 10-Q calculation: 1.417 - 0.484. |
| TTM free cash flow | 7.378 | 7.395 - 0.933 + 0.916. |
| FY2026 comparable sales growth guidance | 6.5% to 7.5% | Abbott Q1 2026 release. |
| FY2026 adjusted diluted EPS guidance | USD 5.38 to USD 5.58 | Abbott Q1 2026 release. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Year 1 FCF anchor | 7.378 | 7.378 | 7.378 |
| Year 1 FCF growth | 2.5% | 5.0% | 7.0% |
| Year 2 FCF growth | 2.5% | 5.0% | 6.5% |
| Year 3 FCF growth | 2.5% | 4.5% | 6.0% |
| Year 4 FCF growth | 2.5% | 4.0% | 5.5% |
| Year 5 FCF growth | 2.5% | 3.5% | 5.0% |
| WACC | 9.5% | 8.5% | 7.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |

WACC basis: Health Care range in `wiki/reference/valuation-assumptions.md` is 8%-10%. Base WACC is 8.5% because ABT is a diversified large-cap health care company with an investment-grade profile, but Exact Sciences integration, higher leverage, regulatory/product risk, and GAAP/non-GAAP conversion keep it above the lower end.

Terminal growth basis: 2.5% is inside the mature developed-market compounder range. The bull case uses 3.0% only if Medical Devices/Cancer Diagnostics growth and FCF conversion remain strong while debt falls.

## FCF Projection

Base case amounts are USD billions.

| Year | FCF | Growth |
|---:|---:|---:|
| Year 1 | 7.747 | 5.0% |
| Year 2 | 8.134 | 5.0% |
| Year 3 | 8.500 | 4.5% |
| Year 4 | 8.840 | 4.0% |
| Year 5 | 9.150 | 3.5% |

Base rationale: the model starts from source-backed TTM FCF and fades below FY2026 comparable sales guidance because acquisition integration, higher interest burden, and GAAP/non-GAAP conversion can limit near-term FCF compounding.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | Enterprise Value | Cash + STI | Total Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 88.82 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 9.5% | 2.0% | 102.5 | 7.3 | (34.0) | 75.8 | 43.36 | -51.2% |
| Base | 8.5% | 2.5% | 137.1 | 7.3 | (34.0) | 110.4 | 63.17 | -28.9% |
| Bull | 7.5% | 3.0% | 193.1 | 7.3 | (34.0) | 166.4 | 95.22 | 7.2% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 7.5% | 71.85 | 78.98 | 87.69 |
| 8.5% | 58.33 | 63.17 | 68.90 |
| 9.5% | 48.42 | 51.89 | 55.89 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 4.77% | Not enough yield to ignore leverage/integration risk. |
| Market EV / TTM FCF | 24.61x | Premium multiple for an equity story with near-term GAAP pressure. |
| Net debt / TTM FCF | 3.63x | Manageable for Abbott, but material after Exact Sciences. |
| Base terminal value share of EV | 75.8% | High but below the 85%-90% warning zone. |
| FY2026 adjusted EPS guide vs price | about 16.2x | Looks more reasonable on non-GAAP EPS than on FCF DCF, so FCF conversion is the debate. |

## What Would Change The Valuation

- FY2026 actual FCF materially exceeds the current TTM FCF anchor.
- Abbott discloses a credible deleveraging path after the Exact Sciences acquisition.
- Cancer Diagnostics growth and synergy evidence offset acquisition dilution.
- Nutrition volume improves without requiring margin-destructive pricing.
- Medical Devices sustains high-single-digit comparable growth.
- Current price falls toward or below base-case fair value while guidance remains intact.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| FY2026 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | DCF uses source-backed TTM FCF instead of invented FY2026 FCF. |
| FY2026 full-year actual results | not disclosed | Q1 2026 was the latest official period found. |
| Forward GAAP EPS / net income guidance | not provided | Limits GAAP earnings normalization and P/E cross-check. |
| Exact Sciences full run-rate contribution and integration cost detail | partially disclosed | Limits acquisition accretion/dilution and synergy modeling. |
| Product-level profitability | not disclosed | Limits segment-specific valuation. |
| Official full Q&A transcript | not normalized | Could refine management-confidence and analyst-pushback reads. |
| Investor-specific required return | not provided | Could change whether ABT is acceptable as a hold despite limited DCF upside. |

## Entity Update

Updated `wiki/entities/ABT.md` with this valuation memo link and valuation watch items. The valuation pushes the action read toward wait/watchlist for new capital at current price.
