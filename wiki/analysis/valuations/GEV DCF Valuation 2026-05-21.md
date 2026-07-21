---
type: analysis
analysis_type: dcf-valuation
ticker: GEV
company: GE Vernova Inc.
date: 2026-05-21
currency: USD
source_files:
  - wiki/entities/GEV.md
  - raw/financials/GEV_fundamentals.md
  - raw/imports/GEV_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/GEV
---

# GEV DCF Valuation - 2026-05-21
Entity: [[GEV]]

## Bottom Line

This DCF uses a fresh market price of USD 1,024.52, market cap of USD 275.31B, source-backed cash / restricted cash of USD 10.172B, total borrowings and finance leases of USD 2.857B, Q1 2026 diluted shares of 272M, TTM non-GAAP FCF of USD 7.526B, and FY2026 FCF guidance midpoint of USD 7.0B.

Base-case fair value is approximately **USD 587.37 per diluted share**, or about **42.7% downside** versus USD 1,024.52. Bull case reaches about **USD 930.06**, still slightly below market price. That does not say the business is weak; it says market price already assumes a very strong power / electrification supercycle and successful Wind recovery.

Action implication: **WAIT / AVOID-new-capital** until the price offers more margin of safety or official results show FCF durability above the current guidance range.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/GEV.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized facts | `raw/financials/GEV_fundamentals.md` | Q1 2026 financials, FY2025 baseline, FCF, cash, debt, shares, guidance. |
| Latest results source note | `raw/imports/GEV_latest_results_source.md` | Source map and raw extraction. |
| GE Vernova Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1996810/000199681026000064/gev-20260331.htm | Primary filing source for statements, shares, cash, borrowings. |
| GE Vernova Q1 2026 earnings release | https://www.gevernova.com/sites/default/files/gev_webcast_pressrelease_04222026.pdf | Official results, FCF reconciliation, and FY2026 guidance. |
| GE Vernova FY2025 annual report | https://www.gevernova.com/sites/default/files/gevernova_2025_annual_report.pdf | FY2025 annual baseline. |
| Investing.com GEV quote page | https://www.investing.com/equities/ge-vernova-llc | Fresh market price and market cap checked 2026-05-21. |

## Input Table

All financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 1,024.52 | Investing.com GEV quote page, checked 2026-05-21. |
| Market capitalization | USD 275.31B | Investing.com quote page; cross-check from price * shares outstanding. |
| Shares outstanding | 0.268720B | GE Vernova Q1 2026 Form 10-Q cover page. |
| Diluted shares used for DCF | 0.272B | GE Vernova Q1 2026 weighted-average diluted shares. |
| Cash, cash equivalents, and restricted cash | 10.172 | GE Vernova Q1 2026 Form 10-Q. |
| Total borrowings and finance leases | 2.857 | GE Vernova Q1 2026 Form 10-Q. |
| Net cash | 7.315 | 10.172 - 2.857. |
| FY2025 free cash flow | 3.710 | GE Vernova FY2025 annual report; non-GAAP. |
| Q1 2025 free cash flow | 0.975 | GE Vernova Q1 2026 earnings release; non-GAAP. |
| Q1 2026 free cash flow | 4.791 | GE Vernova Q1 2026 earnings release; non-GAAP. |
| TTM free cash flow | 7.526 | 3.710 - 0.975 + 4.791. |
| FY2026 FCF guidance midpoint | 7.000 | Midpoint of GE Vernova guidance range USD 6.5B to USD 7.5B. |

Base DCF uses FY2026 FCF guidance midpoint as the starting anchor because Q1 2026 FCF benefited from working capital, customer down payments, and slot reservation agreements. Annualizing Q1 would make the model look more certain than the source facts support.

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | FY2026 guidance midpoint USD 7.0B | FY2026 guidance midpoint USD 7.0B | FY2026 guidance midpoint USD 7.0B |
| Year 1 FCF growth | 3.0% | 12.0% | 18.0% |
| Year 2 FCF growth | 3.0% | 10.0% | 16.0% |
| Year 3 FCF growth | 2.5% | 8.0% | 13.0% |
| Year 4 FCF growth | 2.5% | 6.0% | 10.0% |
| Year 5 FCF growth | 2.0% | 4.0% | 7.0% |
| WACC | 9.5% | 8.5% | 7.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |
| Debt treatment | Total borrowings and finance leases | Total borrowings and finance leases | Total borrowings and finance leases |

WACC basis: GE Vernova is an Industrials / energy infrastructure company with strong secular demand, but it also has project execution, Wind turnaround, supply-chain, and working-capital cyclicality. The vault reference range for Industrials is 8%-9%; base WACC uses 8.5%, bear uses 9.5%, and bull uses 7.5% only for a premium market-leader scenario.

Terminal growth basis: 2.0%-3.0% matches a mature developed-market compounder. The model does not use a terminal growth rate above 3.0% because GEV is already a very large infrastructure company and terminal value should not assume perpetual supercycle economics.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| Starting anchor | 7.000 | 7.000 | 7.000 |
| Year 1 | 7.210 | 7.840 | 8.260 |
| Year 2 | 7.426 | 8.624 | 9.582 |
| Year 3 | 7.612 | 9.314 | 10.828 |
| Year 4 | 7.802 | 9.873 | 11.911 |
| Year 5 | 7.958 | 10.268 | 12.745 |

Base case rationale: official guidance supports a large FCF step-up from FY2025, while Power and Electrification growth can support above-GDP FCF growth. The model still fades growth because Wind recovery, project mix, customer advances, and working-capital timing are not risk-free.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Cash | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 1,024.52 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 9.5% | 2.0% | 29.058 | 68.753 | 97.811 | 7.315 | 105.126 | 386.49 | -62.3% |
| Base | 8.5% | 2.5% | 35.796 | 116.653 | 152.449 | 7.315 | 159.764 | 587.37 | -42.7% |
| Bull | 7.5% | 3.0% | 42.485 | 203.177 | 245.663 | 7.315 | 252.978 | 930.06 | -9.2% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 7.5% | 649.82 | 701.21 | 764.02 |
| 8.5% | 552.45 | 587.37 | 628.64 |
| 9.5% | 481.08 | 506.09 | 534.94 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 2.73% | Very demanding, especially with Q1 working-capital tailwinds. |
| FY2026 guided FCF yield on market cap | 2.54% | Market already discounts a strong guide and continued growth. |
| Market EV / TTM FCF | 35.61x | Premium multiple requires durable FCF growth and Wind recovery. |
| Net cash / TTM FCF | 0.97x | Balance sheet is supportive; valuation problem is not leverage. |
| Base DCF terminal value share of EV | 76.5% | High but below the 85%-90% warning threshold. |
| Bull DCF terminal value share of EV | 82.7% | Close enough to be assumption-sensitive, though still below 85%. |

## What Would Change The Valuation

- FY2026 FCF tracking above USD 7.5B without obvious working-capital reversal.
- Evidence that customer advances and slot reservations convert into durable revenue and cash flow.
- Wind moving toward the approximately USD 400M FY2026 loss guide without new project charges.
- Electrification margin sustaining low double digits while revenue grows high teens.
- Clearer disclosure of segment-level FCF and project-level profitability.
- A lower stock price that lifts guided FCF yield toward a more attractive margin of safety.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Full FY2026 actual results | not disclosed | Uses Q1 2026 and FY2026 guidance instead. |
| GAAP reconciliation for forward non-GAAP FCF / adjusted EBITDA guidance | not disclosed | DCF uses company-defined FCF and labels it as non-GAAP. |
| Segment-level FCF | not disclosed | Cannot prove Power versus Electrification versus Wind cash conversion. |
| Wind project-level loss reserve and contract profitability | not disclosed | Turnaround timing may be more fragile than segment guide suggests. |
| Customer down-payment / slot-reservation conversion terms | not disclosed | Q1 FCF could overstate recurring cash generation. |
| Product-level profitability | not disclosed | Data-center, gas turbine, grid, and wind economics cannot be modeled separately. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Updated `wiki/entities/GEV.md` with valuation watch items and report link. Core action read is `WAIT / AVOID-new-capital`, because the source-backed base-case DCF is materially below the fresh market price even with strong business momentum.
