---
type: analysis
analysis_type: dcf-valuation
ticker: MCD
company: McDonald's Corporation
date: 2026-05-26
currency: USD
source_files:
  - wiki/entities/MCD.md
  - raw/financials/MCD_fundamentals.md
  - raw/imports/MCD_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/MCD
---

# MCD DCF Valuation - 2026-05-26

## Bottom Line

This DCF uses source-backed TTM simple free cash flow of USD 7.039B, latest available market close of USD 282.27 on 2026-05-22, market cap of USD 200.55B, cash of USD 1.170B, long-term debt of USD 40.105B, and Q1 2026 diluted shares of 713.5M.

Base-case fair value is approximately **USD 125.32 per diluted share**, or about **55.6% downside** versus USD 282.27. McDonald's is a high-quality franchised restaurant compounder, but current market valuation is very demanding at about 36.1x market EV / TTM FCF.

Action implication: **AVOID-new-capital / WATCHLIST**. Existing holders may HOLD for quality, dividend, and tax/portfolio reasons, but new capital should wait for a materially better entry price or much stronger source-backed FCF growth.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/MCD.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized facts | `raw/financials/MCD_fundamentals.md` | Q1 2026 financials, FY2025 annual baseline, FCF, cash, debt, shares, guidance. |
| Latest results source note | `raw/imports/MCD_latest_results_source.md` | Source map and raw extraction. |
| McDonald's Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/63908/000006390826000051/mcd-20260331.htm | Q1 statements, balance sheet, cash flow, outlook. |
| McDonald's Q1 2026 earnings release PDF | https://corporate.mcdonalds.com/content/dam/sites/corp/nfl/pdf/Q1%202026%20Exhibit%2099.1%20-%203.31.26.pdf | Official results and commentary. |
| McDonald's FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm | FY2025 annual baseline and historical FCF. |
| StockAnalysis MCD quote / market cap | https://stockanalysis.com/stocks/mcd/ | Fresh market-data check on 2026-05-26 Asia/Bangkok. |

## Input Table

All financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 282.27 | StockAnalysis close on 2026-05-22; checked 2026-05-26 Asia/Bangkok. |
| Market capitalization | USD 200.55B | StockAnalysis market cap page, checked 2026-05-26. |
| Shares outstanding | 710.51M | StockAnalysis statistics page. |
| Diluted shares used for DCF | 713.5M | Q1 2026 diluted weighted-average shares. |
| Cash and equivalents | 1.170 | Q1 2026 Form 10-Q. |
| Long-term debt | 40.105 | Q1 2026 Form 10-Q. |
| Long-term lease liability | 14.069 | Q1 2026 Form 10-Q; shown as debt-like context. |
| Core net debt used in base DCF | 38.935 | 40.105 - 1.170. |
| FY2025 simple FCF | 7.186 | FY2025 operating cash flow 10.551 - capex 3.365. |
| Q1 2025 simple FCF | 1.877 | Q1 2025 operating cash flow 2.428 - capex 0.551. |
| Q1 2026 simple FCF | 1.730 | Q1 2026 operating cash flow 2.412 - capex 0.682. |
| TTM simple FCF | 7.039 | 7.186 - 1.877 + 1.730. |
| 2026 capex guidance | USD 3.7B to USD 3.9B | Q1 2026 Form 10-Q outlook. |
| 2026 FCF conversion guidance | low-to-mid 80% range | Q1 2026 Form 10-Q outlook. |
| 2026 operating margin guidance | mid-to-high 40% range | Q1 2026 Form 10-Q outlook. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | TTM FCF USD 7.039B | TTM FCF USD 7.039B | TTM FCF USD 7.039B |
| Annual FCF growth, Years 1-5 | 1.0% | 4.0% | 6.0% |
| WACC | 9.5% | 8.5% | 7.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |

WACC basis: vault reference range for Consumer Discretionary is 8%-10%. Base WACC uses 8.5% because McDonald's has exceptional brand durability and a franchised model, but debt and lease obligations argue against using a low consumer-staples-style discount rate. Bear uses 9.5%; bull uses 7.5% for a premium-quality scenario.

Terminal growth basis: mature developed-market compounder range is 2.0%-3.0%. Base uses 2.5%; bull uses 3.0% and should be treated as a high-quality sensitivity.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| TTM anchor | 7.039 | 7.039 | 7.039 |
| Year 1 | 7.109 | 7.321 | 7.461 |
| Year 2 | 7.180 | 7.613 | 7.909 |
| Year 3 | 7.252 | 7.918 | 8.383 |
| Year 4 | 7.325 | 8.235 | 8.886 |
| Year 5 | 7.398 | 8.564 | 9.419 |

Base case rationale: Q1 2026 comparable sales were positive and 2026 operating margin guidance remains high, but capex is rising and forward FCF dollars are not disclosed. A 4% annual FCF growth base is already assuming that development and digital initiatives translate into durable cash growth.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Core Net Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 282.27 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 9.5% | 2.0% | 28.337 | 63.364 | 91.701 | 38.935 | 52.766 | 73.97 | -73.8% |
| Base | 8.5% | 2.5% | 31.051 | 97.297 | 128.348 | 38.935 | 89.413 | 125.32 | -55.6% |
| Bull | 7.5% | 3.0% | 34.131 | 149.796 | 183.927 | 38.935 | 144.992 | 203.22 | -28.0% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 7.5% | 145.20 | 161.54 | 181.51 |
| 8.5% | 114.21 | 125.32 | 138.44 |
| 9.5% | 91.50 | 99.45 | 108.62 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 3.51% | Very low cash yield; current price embeds a quality premium. |
| Market EV / TTM FCF | 36.13x | Demanding multiple for a mature restaurant compounder. |
| Core net debt / TTM FCF | 5.53x | Leverage is a material valuation constraint. |
| Lease-adjusted net obligations / TTM FCF | 7.53x | Lease liabilities matter for risk context even if base DCF uses long-term debt only. |
| Q1 2026 FCF growth | -7.83% YoY | Higher capex weighed on FCF despite better operating results. |
| Base DCF terminal value share of EV | 75.8% | Material but below the 85%-90% high-warning range. |

## What Would Change The Valuation

- A lower stock price that lifts FCF yield meaningfully.
- Source-backed 2026 FCF dollars above the TTM anchor despite higher capex.
- Evidence that unit expansion and loyalty growth are driving guest counts, not only average check.
- Lower debt / lease-adjusted obligation burden relative to FCF.
- A justified lower WACC if rates fall and the market continues to price MCD closer to a defensive staple.
- Weaker comparable sales, franchisee pressure, or FCF conversion below guidance would reduce fair value.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Full FY2026 actual results | not disclosed | DCF uses Q1 2026 plus FY2025 TTM bridge. |
| Official text transcript / full Q&A | ไม่พบข้อมูลที่ยืนยันได้ | Limits detailed management commentary. |
| Forward FCF dollar guidance | not disclosed | DCF uses TTM FCF and growth assumptions rather than a company FCF dollar guide. |
| Product-level profitability by menu category | not disclosed | Cannot model menu category margin drivers directly. |
| Franchisee-level profitability and leverage | not disclosed | Franchisee health is central but not fully visible. |
| Intraday market price on 2026-05-26 | ไม่พบข้อมูลที่ยืนยันได้ | Latest available source price is 2026-05-22 close. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Updated `wiki/entities/MCD.md` with the valuation watch item and report link. Core action read is `AVOID-new-capital / WATCHLIST`, because business quality is high but source-backed DCF and market FCF yield do not support adding at the latest available price.
