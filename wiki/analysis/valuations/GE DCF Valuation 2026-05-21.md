---
type: analysis
analysis_type: dcf-valuation
ticker: GE
company: GE Aerospace
date: 2026-05-21
currency: USD
source_files:
  - wiki/entities/GE.md
  - raw/financials/GE_fundamentals.md
  - raw/imports/GE_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/GE
---

# GE DCF Valuation - 2026-05-21

## Bottom Line

This DCF uses source-backed GE-defined TTM free cash flow of USD 7.901B, FY2026 FCF guidance midpoint of USD 8.2B, latest available market close of USD 300.17 on 2026-05-20, cash / restricted cash of USD 10.981B, total borrowings of USD 20.277B, and Q1 2026 diluted shares of 1.054B.

Base-case fair value is approximately **USD 146.40 per diluted share**, or about **51.2% downside** versus USD 300.17. Even the bull case reaches only about USD 227.49, still below market price. That does not mean GE Aerospace is a weak business; it means current valuation requires unusually strong and durable FCF growth.

Action implication: **avoid new capital / wait** unless the stock price offers a much wider margin of safety or future official results show FCF materially exceeding the current guidance path.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/GE.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized facts | `raw/financials/GE_fundamentals.md` | Q1 2026 financials, FY2025 baseline, FCF, cash, debt, shares, guidance. |
| Latest results source note | `raw/imports/GE_latest_results_source.md` | Source map and raw extraction. |
| GE Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/40545/000004054526000027/ge-20260331.htm | Primary filing source for statements, shares, cash, borrowings. |
| GE Q1 2026 earnings release | https://www.sec.gov/Archives/edgar/data/40545/000004054526000026/ge1q2026earningsrelease.htm | Official results, FCF reconciliation, and guidance. |
| GE FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm | FY2025 FCF, liquidity, debt, annual baseline, and business context. |
| Stooq GE quote CSV | https://stooq.com/q/l/?s=ge.us&f=sd2t2ohlcv&h&e=csv | Fresh market price checked 2026-05-21 Asia/Bangkok. |

## Input Table

All financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 300.17 | Stooq close on 2026-05-20; fetched 2026-05-21 Asia/Bangkok. |
| Market capitalization | USD 313.18B | USD 300.17 * 1.043337B shares outstanding. |
| Shares outstanding | 1.043337B | GE Q1 2026 Form 10-Q. |
| Diluted shares used for DCF | 1.054B | GE Q1 2026 weighted-average diluted shares. |
| Cash, cash equivalents and restricted cash | 10.981 | GE Q1 2026 Form 10-Q. |
| Total borrowings | 20.277 | GE Q1 2026 Form 10-Q; short-term + long-term borrowings. |
| Net debt using cash only | 9.296 | 20.277 - 10.981. |
| FY2025 GE-defined FCF | 7.694 | GE FY2025 Form 10-K. |
| Q1 2025 GE-defined FCF | 1.451 | GE Q1 2026 earnings release. |
| Q1 2026 GE-defined FCF | 1.658 | GE Q1 2026 earnings release. |
| TTM GE-defined FCF | 7.901 | 7.694 - 1.451 + 1.658. |
| FY2026 FCF guidance midpoint | 8.200 | Midpoint of GE guidance range USD 8.0B to USD 8.4B. |
| FY2026 adjusted EPS guidance midpoint | 7.25 | Midpoint of GE guidance range USD 7.10 to USD 7.40. |

Base DCF uses cash/restricted cash and total borrowings. It does not treat the full USD 38.193B investment securities balance as excess cash because GE also carries large run-off insurance liabilities; that adjustment needs a dedicated insurance-balance-sheet normalization.

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | TTM FCF USD 7.901B | FY2026 FCF guidance midpoint USD 8.2B | FY2026 FCF guidance midpoint USD 8.2B |
| Year 1 FCF growth | 2.0% | 8.0% | 12.0% |
| Year 2 FCF growth | 3.0% | 7.0% | 11.0% |
| Year 3 FCF growth | 3.0% | 6.0% | 10.0% |
| Year 4 FCF growth | 2.0% | 5.0% | 8.0% |
| Year 5 FCF growth | 2.0% | 4.0% | 6.0% |
| WACC | 9.5% | 8.5% | 7.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |
| Debt treatment | Total borrowings | Total borrowings | Total borrowings |

WACC basis: GE Aerospace is an Industrials / Aerospace leader with high-quality aftermarket cash flows, but aerospace cyclicality, supply-chain execution, long-cycle programs, and residual insurance-balance-sheet complexity argue against a very low discount rate. The vault reference range for Industrials is 8%-9%; base WACC uses 8.5%, bear uses 9.5% for execution/macro risk, and bull uses 7.5% only if the market treats GE as a premium compounder.

Terminal growth basis: 2.0%-3.0% matches a mature developed-market compounder. The model does not assume terminal growth above 3.0% because GE is already a large global aerospace franchise.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| Starting anchor | 7.901 | 8.200 | 8.200 |
| Year 1 | 8.059 | 8.856 | 9.184 |
| Year 2 | 8.301 | 9.476 | 10.194 |
| Year 3 | 8.550 | 10.044 | 11.214 |
| Year 4 | 8.721 | 10.547 | 12.111 |
| Year 5 | 8.895 | 10.969 | 12.837 |

Base case rationale: Q1 demand and FY2026 guidance support starting above TTM FCF, but sustained high growth needs supply-chain improvement, strong services mix, and no material airline/fuel/geopolitical drag.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 300.17 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 9.5% | 2.0% | 32.511 | 76.847 | 109.358 | 9.296 | 100.063 | 94.94 | -68.4% |
| Base | 8.5% | 2.5% | 38.980 | 124.616 | 163.596 | 9.296 | 154.301 | 146.40 | -51.2% |
| Bull | 7.5% | 3.0% | 44.402 | 204.673 | 249.074 | 9.296 | 239.779 | 227.49 | -24.2% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 7.5% | 163.62 | 177.79 | 195.11 |
| 8.5% | 136.77 | 146.40 | 157.77 |
| 9.5% | 117.09 | 123.98 | 131.93 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 2.52% | Very demanding for an industrial, even a high-quality aerospace franchise. |
| FY2026 guided FCF yield on market cap | 2.62% | Market already discounts a strong guide and further growth. |
| Market EV / TTM FCF | 40.81x | Requires durable high FCF growth or sustained premium multiple. |
| Forward adjusted P/E | 41.40x | High relative to the cyclical/industrial risk profile. |
| Net debt / TTM FCF | 1.18x | Balance sheet is manageable using cash-only net debt. |
| Base DCF terminal value share of EV | 76.2% | High but below the 85%-90% warning threshold. |
| Bull DCF terminal value share of EV | 82.2% | Still below 85%, but valuation becomes highly terminal-assumption sensitive. |

## What Would Change The Valuation

- FY2026 FCF tracking above USD 8.4B without margin deterioration.
- Evidence that CES services growth sustains without material supply-chain or airline credit pressure.
- Lower share count from buybacks at attractive prices.
- Clearer disclosure showing investment securities can safely be treated as excess capital after insurance liabilities.
- A lower stock price that lifts forward FCF yield toward a more attractive margin of safety.
- Program-level evidence that LEAP / GE9X / defense growth does not dilute long-term margins.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Full FY2026 actual results | not disclosed | Uses Q1 2026 and FY2025 baseline instead. |
| Forward GAAP reconciliation for non-GAAP guidance | not disclosed | DCF uses GE-defined FCF and labels it as non-GAAP. |
| Segment-level FCF | not disclosed | Cannot prove CES vs DPT cash conversion. |
| Program-level profitability | not disclosed | LEAP/GE9X and defense economics cannot be separately modeled. |
| Excess cash / insurance investment normalization | judgment required | Base case avoids treating investment securities as excess cash. |
| Market quote after 2026-05-20 close | ไม่พบข้อมูลที่ยืนยันได้ | Refresh before future action changes. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Updated `wiki/entities/GE.md` with valuation watch items and report link. Core action read is `AVOID-new-capital / WAIT`, because the source-backed DCF range is materially below the latest checked market price despite strong business quality.
