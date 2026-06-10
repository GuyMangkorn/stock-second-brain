---
type: analysis
analysis_type: dcf-valuation
ticker: IBM
company: International Business Machines Corporation
date: 2026-06-10
currency: USD
source_files:
  - wiki/entities/IBM.md
  - raw/financials/IBM_fundamentals.md
  - raw/imports/IBM_latest_results_source.md
  - raw/imports/IBM_market_quote_2026-06-10.md
tags:
  - analysis/dcf
  - ticker/IBM
---

# IBM DCF Valuation - 2026-06-10

## Bottom Line

This refresh keeps the same source-backed operating inputs from the Q1 2026 official-source ingest and updates the market price to **USD 277.49** from the latest trading day returned by Alpha Vantage, 2026-06-09.

Base-case fair value remains about **USD 240.27 per diluted share**, but the stock price has moved from USD 224.88 in the 2026-05-21 memo to USD 277.49. That changes the valuation read from modest upside to about **13.4% downside** versus base case.

Action read: IBM is now closer to **WAIT / HOLD-existing-only** than ADD. The business quality setup is still improving, but the market is paying more for the Software/AI/hybrid-cloud narrative before debt reduction, Consulting acceleration, and post-Confluent FCF proof are fully visible.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Market quote source note | `raw/imports/IBM_market_quote_2026-06-10.md` | Fresh market price and market-data calculations. |
| Normalized facts | `raw/financials/IBM_fundamentals.md` | Q1 2026 financial facts, FY2025 baseline, FCF, cash, debt, shares, guidance. |
| Entity page | `wiki/entities/IBM.md` | Business model, thesis, risks, catalysts, prior valuation watch items. |
| IBM Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/51143/000005114326000038/ibm-20260331.htm | Q1 2026 statements, share count, cash flow reconciliation, FCF definition. |
| IBM Q1 2026 earnings release | https://newsroom.ibm.com/2026-04-22-IBM-RELEASES-FIRST-QUARTER-RESULTS | Q1 2026 segment results, cash/debt summary, guidance, dividend. |
| IBM 1Q26 prepared remarks | https://www.ibm.com/downloads/documents/us-en/15db805fff4249f1 | Management commentary and guidance details. |
| IBM FY2025 10-K / annual report extract | https://www.sec.gov/Archives/edgar/data/51143/000005114326000010/ibm-20251231_d2.htm | FY2025 FCF, cash, debt, and annual baseline. |

## Input Table

All financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 277.49 | Alpha Vantage `GLOBAL_QUOTE`, latest trading day 2026-06-09; fetched 2026-06-10 Asia/Bangkok. |
| Prior DCF price | USD 224.88 | Stooq close on 2026-05-20; prior memo checked 2026-05-21 Asia/Bangkok. |
| Price move since prior DCF | +23.4% | 277.49 / 224.88 - 1. |
| Market capitalization | USD 260.81B | 277.49 * 939.885M shares outstanding from IBM Q1 2026 Form 10-Q. |
| Shares outstanding | 939.885M | IBM Q1 2026 Form 10-Q cover page. |
| Diluted shares used for DCF | 952.1M | IBM Q1 2026 weighted-average diluted shares. |
| Cash + restricted cash + marketable securities | 11.828 | IBM Q1 2026 Form 10-Q line items. |
| Total debt | 66.400 | IBM Q1 2026 earnings release. |
| IBM Financing debt included in total debt | 12.800 | IBM Q1 2026 earnings release and prepared remarks. |
| Net debt used in base DCF | 54.572 | 66.400 - 11.828. |
| TTM IBM-defined FCF | 14.992 | FY2025 FCF 14.734 - Q1 2025 FCF 1.962 + Q1 2026 FCF 2.220. |
| FY2026 FCF guidance | About 15.7 | FY2025 FCF 14.734 + management guidance for about USD 1B YoY increase. |
| FY2026 revenue guidance | More than 5% constant-currency growth | IBM Q1 2026 earnings release and prepared remarks. |
| FY2026 Software revenue guidance | 10%+ growth | IBM 1Q26 prepared remarks. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | TTM FCF USD 14.992B | TTM FCF USD 14.992B | TTM FCF USD 14.992B |
| Year 1 FCF growth | 0% | 5.0% | 8.0% |
| Year 2 FCF growth | 2.0% | 5.5% | 7.5% |
| Year 3 FCF growth | 2.0% | 5.0% | 7.0% |
| Year 4 FCF growth | 2.0% | 4.5% | 6.0% |
| Year 5 FCF growth | 2.0% | 4.0% | 5.0% |
| WACC | 9.5% | 8.5% | 7.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |
| Debt treatment | Total debt | Total debt | Total debt |

WACC basis: IBM sits between mature Information Technology, enterprise software, consulting, infrastructure, and financing complexity. The vault reference range for Information Technology is 8%-12%. Base WACC remains 8.5% because IBM has recurring software/support cash flows and investment-grade liquidity, but leverage, acquisition integration, Consulting cyclicality, and IBM Financing complexity prevent a lower discount rate.

Terminal growth basis: 2.0%-3.0% matches the mature developed-market compounder range. The model does not use a terminal growth rate above 3.0% because IBM is already a large mature company.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| TTM anchor | 14.992 | 14.992 | 14.992 |
| Year 1 | 14.992 | 15.742 | 16.191 |
| Year 2 | 15.292 | 16.607 | 17.406 |
| Year 3 | 15.598 | 17.438 | 18.624 |
| Year 4 | 15.910 | 18.222 | 19.742 |
| Year 5 | 16.228 | 18.951 | 20.729 |

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 277.49 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 9.5% | 2.0% | 59.700 | 140.194 | 199.893 | 54.572 | 145.321 | 152.63 | -45.0% |
| Base | 8.5% | 2.5% | 68.020 | 215.310 | 283.330 | 54.572 | 228.758 | 240.27 | -13.4% |
| Bull | 7.5% | 3.0% | 74.336 | 330.486 | 404.822 | 54.572 | 350.250 | 367.87 | 32.6% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 7.5% | 273.23 | 300.33 | 333.45 |
| 8.5% | 221.85 | 240.27 | 262.03 |
| 9.5% | 184.20 | 197.38 | 212.60 |

Current price at USD 277.49 is above the base case and slightly above the 7.5% WACC / 2.0% terminal-growth sensitivity cell. To justify the price without waiting for a pullback, IBM needs either a lower risk premium, stronger terminal confidence, faster FCF growth, or meaningful debt reduction.

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 5.75% | Less attractive than the 7.09% yield in the prior memo; valuation cushion has compressed. |
| Market EV / TTM FCF | 21.04x | Richer than prior 17.74x; still possible for a durable software-led compounder, but no longer obviously cheap. |
| FY2026 guided FCF yield | about 6.03% | Uses approximate USD 15.7B FY2026 FCF guidance and current market cap. |
| Annualized dividend yield | about 2.44% | Based on USD 1.69 quarterly dividend and USD 277.49 price. |
| Total debt / TTM FCF | 4.43x | Leverage remains material; debt reduction matters to equity upside. |
| Net debt / TTM FCF | 3.64x | Still meaningful even after cash/marketable securities. |
| Base DCF terminal value share of EV | 76.0% | High but below the 85%-90% warning threshold. |
| Price versus base fair value | -13.4% downside | Current market price is above base-case fair value. |

## What Would Change The Valuation

- Upgrade valuation if Q2/FY2026 data confirms FCF tracking above USD 15.7B, Software stays 10%+, Consulting reaccelerates, and total debt starts declining.
- Upgrade valuation if management gives clearer product-level AI revenue, AI margins, or backlog conversion that supports higher FCF growth assumptions.
- Downgrade valuation if Q2 shows Software growth deceleration, Consulting remains near-flat, z17-driven Infrastructure strength normalizes quickly, or debt rises further.
- Re-run after Q2 2026 results because current price already discounts more execution than the 2026-05-21 memo did.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Full FY2026 actual results | not disclosed | Uses Q1 2026 and FY2025 baseline instead. |
| Product-level AI revenue and AI margins | not disclosed | AI upside cannot be directly modeled. |
| Exact Q1 2026 generative AI book of business value | ไม่พบข้อมูลที่ยืนยันได้ | Cannot quantify Q1 AI pipeline expansion from official source set. |
| Segment-level FCF | not disclosed | Cannot test whether Software, Consulting, or Infrastructure is driving cash conversion. |
| Intraday 2026-06-10 real-time quote | not disclosed | Latest quote source returned 2026-06-09 trading day. |
| Financing debt adjustment | judgment required | Base DCF uses total debt conservatively; excluding IBM Financing debt would raise fair value. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Updated `wiki/entities/IBM.md` with the 2026-06-10 valuation watch item. Core action read moves from `HOLD / WATCHLIST` to `WAIT / HOLD-existing-only` because current price is above base fair value after a 23.4% move since the prior DCF price.
