---
type: analysis
analysis_type: dcf-valuation
ticker: CEG
company: Constellation Energy Corporation
date: 2026-05-31
currency: USD
source_files:
  - wiki/entities/CEG.md
  - raw/financials/CEG_fundamentals.md
  - raw/imports/CEG_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/CEG
---

# CEG DCF Valuation - 2026-05-31
Entity: [[CEG]]

## Bottom Line

This valuation uses the latest regular-market close found during the fresh check: USD 287.75 on 2026-05-29. Core source-backed inputs are market cap cross-check USD 104.27B, cash / restricted cash USD 1.171B, total debt used locally USD 22.466B, net debt USD 21.295B, expected FY2026 diluted shares of 361M, TTM GAAP-style FCF of USD 1.137B, and management's non-GAAP `free cash flow before growth` of USD 8.4B across 2026-2027.

Base-case fair value is approximately **USD 194.39 per diluted share**, or about **32.4% downside** versus USD 287.75. Bull case reaches **USD 349.31**, but it requires strong FCF-before-growth expansion, a lower WACC, and favorable terminal assumptions. Because the valuation depends heavily on a non-GAAP FCF-before-growth guide while GAAP-style TTM FCF is much lower, the action implication is **WAIT / WATCHLIST-new-capital**, not a confident add.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/CEG.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized facts | `raw/financials/CEG_fundamentals.md` | Q1 2026 financials, FY2025 baseline, FCF, cash, debt, shares, guidance, market data. |
| Latest results source note | `raw/imports/CEG_latest_results_source.md` | Source map and raw extraction. |
| CEG Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1868275/000186827526000067/ceg-20260331.htm | Primary filing source for statements, shares, cash, debt, and cash flow. |
| CEG Q1 2026 release / presentation | https://investors.constellationenergy.com/static-files/9dc0168f-5328-42ce-9d66-2c3abe07bff0 | Official results, non-GAAP reconciliation, and guidance. |
| CEG Q1 2026 earnings presentation | https://investors.constellationenergy.com/static-files/e5a93793-71b7-453f-a5d3-6a8acb420282 | FCF before growth, Base EPS growth, capital allocation, and fleet context. |
| CEG FY2025 Form 10-K / annual report | https://investors.constellationenergy.com/static-files/8d46f4dc-04f9-4916-aa5d-e12bd5c45aa7 | FY2025 annual baseline. |
| Twelve Data CEG historical quote page | https://twelvedata.com/markets/736051/stock/nasdaq/ceg/historical-data | Fresh market price checked 2026-05-31; latest close found 2026-05-29. |

## Input Table

All financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 287.75 | Twelve Data, 2026-05-29 close; checked 2026-05-31. |
| Market capitalization | 104.27 | 287.75 * 362.359M shares outstanding. |
| Shares outstanding | 0.362359 | CEG Q1 2026 Form 10-Q statement of equity. |
| Diluted shares used for DCF | 0.361 | CEG Q1 2026 presentation expected average diluted shares for FY2026 guidance. |
| Cash, restricted cash, and cash equivalents | 1.171 | CEG Q1 2026 Form 10-Q. |
| Total debt used locally | 22.466 | Short-term borrowings + current LTD + long-term debt. |
| Net debt | 21.295 | 22.466 - 1.171. |
| FY2025 GAAP-style FCF | 1.288 | FY2025 OCF 4.237 - capex 2.949. |
| Q1 2025 GAAP-style FCF | (0.699) | Q1 2025 OCF 0.107 - capex 0.806. |
| Q1 2026 GAAP-style FCF | (0.850) | Q1 2026 OCF 0.425 - capex 1.275. |
| TTM GAAP-style FCF | 1.137 | 1.288 - (0.699) + (0.850). |
| FCF before growth, 2026-2027 | 8.4 aggregate | CEG Q1 2026 presentation; non-GAAP. |
| Starting FCF-before-growth anchor | 4.2 | 8.4 / 2 years; non-GAAP scenario anchor. |

DCF choice: A point DCF on TTM GAAP-style FCF would produce an extremely low fair value and may understate the post-Calpine guide path. A point DCF on FCF before growth may overstate cash available after required growth capex. This memo uses FCF before growth as the scenario anchor, while using TTM GAAP-style FCF as a sanity check and source gap.

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | 2026-2027 average FCF before growth USD 4.2B | 2026-2027 average FCF before growth USD 4.2B | 2026-2027 average FCF before growth USD 4.2B |
| Year 1 FCF growth | 3.0% | 12.0% | 18.0% |
| Year 2 FCF growth | 3.0% | 10.0% | 16.0% |
| Year 3 FCF growth | 2.5% | 8.0% | 13.0% |
| Year 4 FCF growth | 2.0% | 6.0% | 10.0% |
| Year 5 FCF growth | 2.0% | 4.0% | 7.0% |
| WACC | 9.5% | 8.5% | 7.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |
| Debt treatment | Total debt minus cash / restricted cash | Total debt minus cash / restricted cash | Total debt minus cash / restricted cash |

WACC basis: CEG has utility-like reliability assets and investment-grade intent, but it is not a pure regulated utility. Merchant power exposure, Calpine integration, higher leverage, regulatory uncertainty, commodity / capacity price exposure, and FCF definition risk justify using a base WACC above the vault's regulated Utilities range. Base WACC is 8.5%, with 9.5% bear and 7.5% bull.

Terminal growth basis: 2.0%-3.0% matches a mature developed-market power infrastructure company. The model does not use a terminal growth rate above 3.0% because the company is already large and terminal value should not assume perpetual power-supercycle economics.

## FCF Projection

Amounts are USD billions and use non-GAAP FCF before growth as the starting anchor.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| Starting anchor | 4.200 | 4.200 | 4.200 |
| Year 1 | 4.326 | 4.704 | 4.956 |
| Year 2 | 4.456 | 5.174 | 5.749 |
| Year 3 | 4.567 | 5.588 | 6.496 |
| Year 4 | 4.659 | 5.924 | 7.146 |
| Year 5 | 4.752 | 6.161 | 7.646 |

Base case rationale: management's non-GAAP FCF before growth guide already embeds a material step-up versus FY2025 GAAP-style FCF. The model gives CEG above-GDP growth from power demand and Calpine scale, but fades growth because regulatory, commodity, capex, collateral, and integration risk remain material.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 287.75 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 9.5% | 2.0% | 17.404 | 41.050 | 58.455 | (21.295) | 37.160 | 102.93 | -64.2% |
| Base | 8.5% | 2.5% | 21.478 | 69.992 | 91.469 | (21.295) | 70.174 | 194.39 | -32.4% |
| Bull | 7.5% | 3.0% | 25.491 | 121.906 | 147.398 | (21.295) | 126.103 | 349.31 | 21.4% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 7.5% | 222.62 | 245.85 | 274.25 |
| 8.5% | 178.60 | 194.39 | 213.05 |
| 9.5% | 146.34 | 157.64 | 170.69 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM GAAP-style FCF yield on market cap | 1.09% | Very thin; GAAP cash conversion does not yet support the market value. |
| FCF-before-growth yield on market cap | 4.03% | More reasonable, but non-GAAP and before growth capex. |
| Market EV / TTM GAAP-style FCF | 110.43x | Highlights how dependent valuation is on future FCF step-up. |
| Market EV / FCF before growth | 29.90x | Premium multiple even on management's more favorable cash-flow lens. |
| Base DCF terminal value share of EV | 76.5% | High but below the 85%-90% warning threshold. |
| Bull DCF terminal value share of EV | 82.7% | Close to assumption-sensitive territory. |
| Reverse DCF growth requirement | ~15.8% annual FCF-before-growth growth for five years | Required to justify USD 287.75 at 8.5% WACC and 2.5% terminal growth. |

## What Would Change The Valuation

- Official results show GAAP `OCF - capex` converging toward FCF-before-growth without a large required growth-capex / collateral drag.
- Clear post-Calpine deleveraging and lower net debt.
- More disclosure on free cash flow after growth capital, not just before growth.
- Large-load / powered-land deals with clear long-duration contracted cash economics.
- PJM / ERCOT regulatory clarity that improves capacity contracting without adding major cost-sharing or price-cap risk.
- A lower stock price that lifts FCF-before-growth yield closer to an attractive margin of safety.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Full FY2026 actual results | not disclosed | Uses Q1 2026, FY2025 baseline, and forward guide instead. |
| Official written Q1 2026 call transcript / Q&A | not verified | Limits call-level nuance and Q&A risk signals. |
| GAAP reconciliation for forward `Base EPS` and `free cash flow before growth` | not fully disclosed | Core reason the valuation is scenario-weighted rather than high-confidence. |
| Segment-level FCF | not disclosed | Cannot prove which regions / Calpine assets produce durable cash. |
| Durable post-Calpine run-rate FCF after growth capex | partially disclosed | Key variable for fair value. |
| Product/customer-level data-center / powered-land profitability | not disclosed | Core bull narrative is not modelable by customer economics. |
| Future regulatory outcomes | not knowable | Can change capacity, co-location, and large-load economics. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Updated `wiki/entities/CEG.md` with valuation watch items and report link. Core action read is `WAIT / WATCHLIST-new-capital`, because the source-backed base-case DCF is below the fresh market price and the bullish case depends on non-GAAP FCF-before-growth converting into durable cash after growth investment.
