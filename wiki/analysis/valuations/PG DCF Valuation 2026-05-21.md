---
type: analysis
analysis_type: dcf-valuation
ticker: PG
company: The Procter & Gamble Company
date: 2026-05-21
currency: USD
source_files:
  - wiki/entities/PG.md
  - raw/financials/PG_fundamentals.md
  - raw/imports/PG_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/PG
---

# PG DCF Valuation - 2026-05-21
Entity: [[PG]]

## Bottom Line

This DCF uses source-backed TTM simple free cash flow of USD 15.028B, latest available market close of USD 142.44 on 2026-05-20, cash of USD 12.306B, total debt of USD 37.026B, and Q3 FY2026 diluted shares of 2,416.5M.

Base-case fair value is approximately **USD 133.34 per diluted share**, or about **6.4% downside** versus USD 142.44. P&G is a high-quality defensive compounder, but the current price already discounts a lot of that quality.

Action implication: **WAIT / HOLD-existing-quality**. Existing holders can justify holding for defensive compounding and cash returns, but new capital should wait for a better FCF yield, clearer margin recovery, or stronger evidence that FY2026/FY2027 growth can exceed the low-single-digit base case.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/PG.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized facts | `raw/financials/PG_fundamentals.md` | Q3 FY2026 financials, FY2025 annual baseline, FCF, cash, debt, shares, guidance. |
| Latest results source note | `raw/imports/PG_latest_results_source.md` | Source map and raw extraction. |
| P&G Q3 FY2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/80424/000008042426000060/pg-20260331.htm | Q3 / nine-month statements, balance sheet, share count, cash flow. |
| P&G Q3 FY2026 earnings release | https://www.pginvestor.com/news/news-details/2026/PG-Announces-Fiscal-Year-2026-Third-Quarter-Results/default.aspx | Segment results, non-GAAP reconciliations, guidance, cash-return plan. |
| P&G FY2025 Annual Report / Form 10-K PDF | https://www.sec.gov/Archives/edgar/data/0000080424/000119312525191752/d879413dars.pdf | FY2025 cash flow and annual baseline. |
| Stooq PG quote CSV | https://stooq.com/q/l/?s=pg.us&f=sd2t2ohlcv&h&e=csv | Fresh market price checked 2026-05-21 Asia/Bangkok. |

## Input Table

All financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 142.44 | Stooq close on 2026-05-20; fetched 2026-05-21 Asia/Bangkok. |
| Market capitalization | USD 331.69B | USD 142.44 * 2,328.599M common shares outstanding. |
| Shares outstanding | 2,328.599M | P&G Q3 FY2026 Form 10-Q shareholders' equity table. |
| Diluted shares used for DCF | 2,416.5M | P&G Q3 FY2026 diluted weighted-average shares. |
| Cash and cash equivalents | 12.306 | P&G Q3 FY2026 Form 10-Q. |
| Debt due within one year | 13.174 | P&G Q3 FY2026 Form 10-Q. |
| Long-term debt | 23.852 | P&G Q3 FY2026 Form 10-Q. |
| Total debt | 37.026 | 13.174 + 23.852. |
| Net debt used in DCF | 24.720 | 37.026 - 12.306. |
| FY2025 simple FCF | 14.044 | FY2025 operating cash flow 17.817 - capex 3.773. |
| 9M FY2025 simple FCF | 10.055 | 9M FY2025 operating cash flow 12.832 - capex 2.777. |
| 9M FY2026 simple FCF | 11.039 | 9M FY2026 operating cash flow 14.425 - capex 3.386. |
| TTM simple FCF | 15.028 | 14.044 - 10.055 + 11.039. |
| FY2026 organic sales guidance | in-line to +4% | P&G Q3 FY2026 earnings release. |
| FY2026 core EPS guidance | USD 6.83 to USD 7.09 | P&G Q3 FY2026 earnings release. |
| FY2026 adjusted FCF productivity | 85% to 90% | P&G Q3 FY2026 earnings release; non-GAAP. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | TTM FCF USD 15.028B | TTM FCF USD 15.028B | TTM FCF USD 15.028B |
| Year 1 FCF growth | 0% | 2.5% | 4.0% |
| Year 2 FCF growth | 1.0% | 3.0% | 4.5% |
| Year 3 FCF growth | 1.5% | 3.0% | 4.0% |
| Year 4 FCF growth | 1.5% | 3.0% | 3.5% |
| Year 5 FCF growth | 1.5% | 2.5% | 3.0% |
| WACC | 8.0% | 7.0% | 6.5% |
| Terminal growth | 1.5% | 2.5% | 3.0% |

WACC basis: the vault reference range for Consumer Staples is 7%-8%. Base WACC uses 7.0% because P&G has scale, defensive demand, brand durability, and investment-grade-like access to debt markets; bear case uses 8.0% to reflect valuation sensitivity, tariffs, and margin pressure; bull case uses 6.5% for a best-quality defensive compounder scenario.

Terminal growth basis: mature developed-market compounder range is 2.0%-3.0%. Bear uses 1.5% because organic growth could stay soft; base uses 2.5%; bull uses 3.0% and should be treated as premium-quality sensitivity rather than a conservative anchor.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| TTM anchor | 15.028 | 15.028 | 15.028 |
| Year 1 | 15.028 | 15.404 | 15.629 |
| Year 2 | 15.178 | 15.866 | 16.332 |
| Year 3 | 15.406 | 16.342 | 16.986 |
| Year 4 | 15.637 | 16.832 | 17.580 |
| Year 5 | 15.872 | 17.253 | 18.108 |

Base case rationale: management guidance supports low-single-digit organic growth and ongoing productivity, but Q3 margin pressure and lower-end EPS commentary argue against assuming aggressive FCF compounding.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 142.44 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 8.0% | 1.5% | 61.453 | 168.677 | 230.130 | 24.720 | 205.410 | 85.00 | -40.3% |
| Base | 7.0% | 2.5% | 66.736 | 280.190 | 346.926 | 24.720 | 322.206 | 133.34 | -6.4% |
| Bull | 6.5% | 3.0% | 70.018 | 388.940 | 458.959 | 24.720 | 434.239 | 179.70 | 26.2% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 6.0% | 154.20 | 174.40 | 201.33 |
| 7.0% | 121.23 | 133.34 | 148.47 |
| 8.0% | 99.25 | 107.20 | 116.75 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 4.53% | Quality premium is already embedded; not a cheap FCF yield. |
| Market EV / TTM FCF | 23.72x | Premium multiple requires durable margin recovery and cash conversion. |
| Net debt / TTM FCF | 1.64x | Balance sheet is manageable; not the main problem. |
| FY2026 YTD FCF growth | 9.79% | Cash flow is moving in the right direction. |
| Base DCF terminal value share of EV | 80.8% | High but below the 85%-90% warning threshold. |
| Bull DCF terminal value share of EV | 84.7% | Near the warning threshold; bull value is very sensitive to terminal assumptions. |

## What Would Change The Valuation

- A lower stock price that lifts FCF yield and creates margin of safety.
- FY2026 full-year FCF above the TTM anchor with stronger margin recovery.
- FY2027 guidance showing organic growth sustainably above low-single-digit.
- Evidence tariff and commodity headwinds are fading faster than expected.
- A reconciled forward adjusted FCF dollar amount from company sources.
- Higher/lower WACC depending on interest rates and defensive-staples risk premium.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Full FY2026 actual results | not disclosed | Uses Q3 FY2026 / FY2025 baseline instead. |
| Official company-hosted full earnings transcript | ไม่พบข้อมูลที่ยืนยันได้ | Limits management Q&A confidence. |
| Forward adjusted free cash flow dollar amount | not disclosed | DCF uses TTM simple FCF and growth assumptions rather than a company FCF dollar guide. |
| Product/category-level profitability below segments | not disclosed | Cannot model margin drivers below reportable segment level. |
| Exact realized tariff / commodity impact after Q3 | not disclosed | FY2026 margin outcome remains guidance-based. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Updated `wiki/entities/PG.md` with the valuation watch item and report link. Core action read is `WAIT / HOLD-existing-quality`, because P&G quality is high but base-case DCF does not show enough upside for new capital at the current price.
