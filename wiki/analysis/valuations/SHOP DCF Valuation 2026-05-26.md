---
type: analysis
analysis_type: dcf-valuation
ticker: SHOP
company: Shopify Inc.
date: 2026-05-26
currency: USD
source_files:
  - wiki/entities/SHOP.md
  - raw/financials/SHOP_fundamentals.md
  - raw/imports/SHOP_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/SHOP
---

# SHOP DCF Valuation - 2026-05-26
Entity: [[SHOP]]

## Bottom Line

This DCF uses a fresh market price of USD 103.00 from the latest verified regular close on 2026-05-22, market cap of USD 133.66B, cash / marketable securities of USD 5.743B, operating lease liabilities of USD 0.179B, Q1 2026 diluted shares of 1.303357874B, and TTM FCF of USD 2.120B.

Base-case fair value is approximately **USD 51.45 per diluted share**, or about **50.0% downside** versus USD 103.00. Bull case reaches about **USD 85.33**, still below market price. This is not a weak-business conclusion; it is a valuation conclusion. SHOP is compounding fast, but current price already discounts a long stretch of high FCF growth.

Action implication: **WAIT / WATCHLIST** for new capital until price gives more margin of safety or official results make a higher long-term FCF path more source-backed.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/SHOP.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized facts | `raw/financials/SHOP_fundamentals.md` | Q1 2026 financials, FY2025 baseline, FCF, cash, debt-like obligations, shares, and guidance. |
| Latest results source note | `raw/imports/SHOP_latest_results_source.md` | Source map and raw extraction. |
| Shopify Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1594805/000159480526000019/shop-20260331.htm | Primary filing source for quarterly statements, shares, cash, leases, and MD&A. |
| Shopify Q1 2026 results press release | https://www.shopify.com/investors/press-releases/shopify-delivers-again-as-merchants-clear-100-billion-in-q1-gmv | Official Q1 results, FCF reconciliation, and Q2 outlook. |
| Shopify FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm | FY2025 annual baseline and annual cash flow. |
| Stooq SHOP.US quote CSV | https://stooq.com/q/l/?s=shop.us&f=sd2t2ohlcv&h&e=csv | Fresh market price checked 2026-05-26. |

## Input Table

All financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 103.00 | Stooq SHOP.US quote CSV, latest regular close on 2026-05-22, checked 2026-05-26. |
| Market capitalization | USD 133.66B | USD 103.00 * 1.297654610B shares outstanding. |
| Shares outstanding | 1.297654610B | Shopify Q1 2026 Form 10-Q cover page as of 2026-05-01. |
| Diluted shares used for DCF | 1.303357874B | Shopify Q1 2026 weighted-average diluted shares. |
| Cash, cash equivalents, and marketable securities | 5.743 | Shopify Q1 2026 Form 10-Q MD&A. |
| Operating lease liabilities | 0.179 | Shopify Q1 2026 Form 10-Q; treated as debt-like obligation. |
| Net cash | 5.564 | 5.743 - 0.179. |
| FY2025 operating cash flow | 2.033 | Shopify FY2025 Form 10-K. |
| FY2025 capex spend | 0.026 | Shopify FY2025 Form 10-K purchases of property and equipment. |
| FY2025 FCF | 2.007 | 2.033 - 0.026. |
| Q1 2025 FCF | 0.363 | Shopify Q1 2026 press release. |
| Q1 2026 FCF | 0.476 | Shopify Q1 2026 press release. |
| TTM FCF | 2.120 | 2.007 - 0.363 + 0.476. |
| Q2 2026 FCF margin outlook | Mid-teens | Shopify Q1 2026 press release; guidance context only. |

The DCF uses TTM FCF as the starting anchor because full-year FY2026 FCF guidance was not verified. Q2 2026 guidance supports continued mid-teens FCF margin, but it does not provide a full-year FCF dollar anchor.

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | TTM FCF USD 2.120B | TTM FCF USD 2.120B | TTM FCF USD 2.120B |
| Year 1 FCF growth | 8.0% | 22.0% | 30.0% |
| Year 2 FCF growth | 7.0% | 18.0% | 25.0% |
| Year 3 FCF growth | 6.0% | 15.0% | 22.0% |
| Year 4 FCF growth | 5.0% | 12.0% | 18.0% |
| Year 5 FCF growth | 4.0% | 10.0% | 15.0% |
| WACC | 10.0% | 9.0% | 8.0% |
| Terminal growth | 2.5% | 3.0% | 3.5% |
| Debt treatment | Operating lease liabilities | Operating lease liabilities | Operating lease liabilities |

WACC basis: Shopify is an Information Technology / commerce software platform with strong growth, high gross margin in subscriptions, net cash, and recurring platform characteristics. The vault reference range for Information Technology is 8%-12%; base WACC uses 9.0% because competitive, payments, credit, and high-valuation risk offset the net cash balance sheet.

Terminal growth basis: high-growth company fading to maturity. Bull case uses 3.5% terminal growth only as an optimistic scenario; base stays at 3.0%.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| Starting anchor | 2.120 | 2.120 | 2.120 |
| Year 1 | 2.290 | 2.586 | 2.756 |
| Year 2 | 2.450 | 3.052 | 3.445 |
| Year 3 | 2.597 | 3.510 | 4.203 |
| Year 4 | 2.727 | 3.931 | 4.959 |
| Year 5 | 2.836 | 4.324 | 5.703 |

Base case rationale: Q1 2026 revenue grew 34.3% and operating income grew 88.2%, so a strong FCF growth path is plausible. The model still fades growth because Merchant solutions mix, credit losses, investment needs, competition, and full-year guidance gaps make a perpetual high-growth FCF path unsafe.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Cash | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 103.00 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 10.0% | 2.5% | 9.680 | 24.064 | 33.745 | 5.564 | 39.309 | 30.16 | -70.7% |
| Base | 9.0% | 3.0% | 13.247 | 48.244 | 61.490 | 5.564 | 67.054 | 51.45 | -50.0% |
| Bull | 8.0% | 3.5% | 16.369 | 89.277 | 105.645 | 5.564 | 111.209 | 85.33 | -17.2% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.5% | 3.0% | 3.5% |
|---:|---:|---:|---:|
| 8.0% | 56.81 | 61.24 | 66.66 |
| 9.0% | 48.43 | 51.45 | 55.01 |
| 10.0% | 42.30 | 44.46 | 46.95 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 1.59% | Very demanding even for a high-quality grower. |
| Market EV / TTM FCF | 60.42x | Requires durable high FCF growth. |
| Net cash / TTM FCF | 2.62x | Balance sheet is a strength. |
| Base DCF terminal value share of EV | 78.5% | Assumption-heavy but below the 85%-90% warning threshold. |
| Bull DCF terminal value share of EV | 84.5% | Very close to assumption-sensitive territory. |
| Q2 2026 FCF margin outlook | Mid-teens | Supports current FCF margin but is not enough to validate a full-year DCF anchor. |

## What Would Change The Valuation

- Q2 and Q3 2026 results proving FCF growth materially above the current base projection.
- Full-year FY2026 FCF guidance or a source-backed annualized FCF run-rate above USD 3B.
- Merchant solutions gross margin remaining stable while Merchant solutions continues to grow faster than total revenue.
- Transaction and loan losses stabilizing as a percentage of revenue.
- Clearer product-level profitability for payments, Capital, Shop Pay, advertising, POS, B2B/enterprise, and AI tools.
- A lower stock price that lifts TTM FCF yield toward a more attractive margin of safety.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Full FY2026 actual results | not disclosed | Uses Q1 2026 and TTM FCF instead. |
| FY2026 full-year revenue / FCF guidance | not disclosed | DCF cannot anchor on a management full-year FCF guide. |
| Official company-hosted full call transcript / Q&A | not verified | Limits management-commentary evidence. |
| Segment-level operating income or FCF | not disclosed | Cannot prove cash conversion by solution category. |
| Product-level profitability | not disclosed | Payments / Capital / Shop Pay economics cannot be modeled separately. |
| Merchant cohort retention, take rate, and GMV by geography | partially disclosed / not disclosed | Limits confidence in long-duration growth assumptions. |
| Credit-loss behavior through a downturn | not disclosed | Important as lending and payments exposure grows. |
| Equity investment fair-value path | not predictable | GAAP earnings may remain volatile. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Updated `wiki/entities/SHOP.md` with valuation watch items and report link. Core action read is `WAIT / WATCHLIST`, because the source-backed base-case DCF is materially below the fresh market price despite excellent operating momentum.
