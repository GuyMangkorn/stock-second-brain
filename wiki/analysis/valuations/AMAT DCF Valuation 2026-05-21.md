---
type: analysis
analysis_type: dcf-valuation
ticker: AMAT
company: Applied Materials, Inc.
date: 2026-05-21
currency: USD
source_files:
  - wiki/entities/AMAT.md
  - raw/financials/AMAT_fundamentals.md
  - raw/imports/AMAT_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/AMAT
---

# AMAT DCF Valuation - 2026-05-21

## Bottom Line

This DCF uses source-backed TTM free cash flow of USD 5.343B, latest regular-session quote of USD 426.85 on 2026-05-20, cash + short-term investments of USD 8.241B, total debt of USD 6.455B, and Q2 FY2026 weighted-average diluted shares of 799M.

Base-case fair value is approximately **USD 120.50 per diluted share**, or about **71.8% downside** versus USD 426.85. Even the bull case is about USD 181.22, still below the market quote, because latest verified FCF is small relative to market capitalization.

นี่ไม่ได้แปลว่า AMAT เป็น business ที่แย่. ตรงกันข้าม Q2 results and Q3 guidance are strong. แต่ current price seems to require a large FCF normalization step that was not verified in the official source set. Without full-year FCF guidance or a cleaner normalized FCF bridge, P11 should stay conservative.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/AMAT.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized facts | `raw/financials/AMAT_fundamentals.md` | Q2 FY2026 financials, FY2025 annual baseline, FCF, cash, debt, shares, guidance. |
| Latest results source note | `raw/imports/AMAT_latest_results_source.md` | Source map and raw extraction. |
| Applied Materials Q2 FY2026 Exhibit 99.1 | https://www.sec.gov/Archives/edgar/data/6951/000162828026035071/exhibit991q22026earningsre.htm | Latest official result, balance sheet, cash flow, segment data, Q3 outlook. |
| Applied Materials FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/6951/000162828025056742/amat-20251026.htm | FY2025 annual cash flow, business model, segment data, risk context. |
| FinancialContent AMAT delayed quote | https://markets.financialcontent.com/stocks.wetm/quote/detailedquote?Symbol=NQ%3AAMAT | Fresh market price checked 2026-05-21. |

## Input Table

All financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 426.85 | FinancialContent delayed quote, updated 2026-05-20 4:00 PM EDT; fetched 2026-05-21. |
| Approximate market capitalization | 338.92 | USD 426.85 * 794M weighted-average basic shares. |
| Weighted-average basic shares | 794M | Q2 FY2026 Exhibit 99.1. |
| Diluted shares used for DCF | 799M | Q2 FY2026 Exhibit 99.1. |
| Cash and cash equivalents | 6.301 | Q2 FY2026 Exhibit 99.1. |
| Short-term investments | 1.940 | Q2 FY2026 Exhibit 99.1. |
| Cash + short-term investments | 8.241 | 6.301 + 1.940. |
| Short-term debt | 1.199 | Q2 FY2026 Exhibit 99.1. |
| Long-term debt | 5.256 | Q2 FY2026 Exhibit 99.1. |
| Total debt | 6.455 | 1.199 + 5.256. |
| Net cash used in DCF | 1.786 | 8.241 - 6.455. |
| FY2025 FCF | 5.698 | FY2025 OCF 7.958 - capex 2.260. |
| 6M FY2026 FCF | 1.250 | OCF 2.531 - capex 1.281. |
| 6M FY2025 FCF | 1.605 | OCF 2.496 - capex 0.891. |
| TTM FCF | 5.343 | 5.698 + 1.250 - 1.605. |
| Q3 FY2026 revenue guidance | 8.950 +/- 0.500 | Q2 FY2026 Exhibit 99.1. |
| Q3 FY2026 non-GAAP EPS guidance | USD 3.36 +/- USD 0.20 | Q2 FY2026 Exhibit 99.1. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | TTM FCF USD 5.343B | TTM FCF USD 5.343B | TTM FCF USD 5.343B |
| Year 1 FCF growth | -5.0% | 10.0% | 18.0% |
| Year 2 FCF growth | 2.0% | 8.0% | 14.0% |
| Year 3 FCF growth | 2.0% | 7.0% | 10.0% |
| Year 4 FCF growth | 2.0% | 5.0% | 8.0% |
| Year 5 FCF growth | 2.0% | 4.0% | 6.0% |
| WACC | 10.5% | 9.5% | 8.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |
| Debt treatment | Total debt | Total debt | Total debt |

WACC basis: AMAT is an Information Technology / semiconductor equipment company. The vault reference range for Information Technology is 8%-12%. Base WACC is 9.5% because AMAT is a high-quality market leader with net cash, but semiconductor equipment cyclicality, customer concentration, China/export-control risk, and volatile FCF conversion prevent using a low software-like discount rate.

Terminal growth basis: 2.0%-3.0% matches mature developed-market compounder assumptions. The model does not use a terminal growth rate above 3.0% because semiconductor equipment is cyclical and long-term growth should not assume an indefinite AI capex supercycle.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| TTM anchor | 5.343 | 5.343 | 5.343 |
| Year 1 | 5.076 | 5.877 | 6.305 |
| Year 2 | 5.177 | 6.347 | 7.188 |
| Year 3 | 5.281 | 6.791 | 7.907 |
| Year 4 | 5.386 | 7.130 | 8.539 |
| Year 5 | 5.494 | 7.416 | 9.052 |

Base case rationale: Q3 revenue/EPS guidance and management's >30% calendar 2026 semi equipment growth statement justify modeling FCF recovery, but the official source set does not include FY2026 FCF guidance. Therefore the model uses a recovery path, not an aggressive step-change to peak-cycle FCF.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Cash | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 426.85 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 10.5% | 2.0% | 19.696 | 40.020 | 59.716 | 1.786 | 61.502 | 76.97 | -82.0% |
| Base | 9.5% | 2.5% | 25.506 | 68.986 | 94.492 | 1.786 | 96.278 | 120.50 | -71.8% |
| Bull | 8.5% | 3.0% | 30.287 | 112.725 | 143.012 | 1.786 | 144.798 | 181.22 | -57.5% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 8.5% | 131.90 | 140.49 | 150.64 |
| 9.5% | 114.35 | 120.50 | 127.59 |
| 10.5% | 100.93 | 105.51 | 110.70 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 1.58% | Very demanding; market is pricing a major FCF recovery. |
| Market EV / TTM FCF | 63.5x | High for a cyclical equipment company unless normalized FCF is much higher. |
| Net cash | USD 1.786B | Balance sheet is not the issue; valuation is. |
| Total debt / TTM FCF | 1.21x | Debt is manageable. |
| Base DCF terminal value share of EV | 73.0% | High but below the 85%-90% warning threshold. |
| Bull DCF terminal value share of EV | 78.8% | Assumption-sensitive, but not mechanically dominated by terminal value. |

## What Would Change The Valuation

- Verified FY2026 FCF guidance or actual 2H FY2026 FCF recovery.
- Evidence that inventory/capex build in Q2 is temporary and converts to revenue/cash.
- Strong Q3 results with FCF conversion, not only revenue and EPS.
- Clearer customer visibility/backlog or order data for HBM, leading-edge logic, and advanced packaging.
- A lower share price that creates a real margin of safety.
- Higher capex or working-capital needs that keep FCF conversion low would reduce fair value.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Q2 FY2026 Form 10-Q | not found | Uses 8-K / Exhibit 99.1; update when 10-Q is filed. |
| FY2026 full-year FCF guidance | not disclosed | Prevents underwriting a precise normalized FCF step-up. |
| Exact Q2 period-end shares outstanding | not verified | DCF uses weighted-average diluted shares from Q2 release. |
| Official full Q2 call transcript / Q&A | ไม่พบข้อมูลที่ยืนยันได้ | Limits management-commentary depth. |
| Segment-level FCF | not disclosed | Cannot test which segment drives cash conversion. |
| Customer-specific AI/HBM/advanced-packaging economics | not disclosed | AI upside is modeled qualitatively, not directly. |
| Market-data provider variance | provider-sourced | Refresh before future decision updates. |

## Entity Update

Updated `wiki/entities/AMAT.md` with valuation watch item and report link. Current action read is `AVOID-new-capital / WAIT-for-better-entry` because source-backed DCF and FCF yield do not support the current market price.
