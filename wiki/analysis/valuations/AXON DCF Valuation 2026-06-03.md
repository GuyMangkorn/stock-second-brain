---
type: analysis
analysis_type: dcf-valuation
ticker: AXON
company: Axon Enterprise, Inc.
date: 2026-06-03
currency: USD
source_files:
  - wiki/entities/AXON.md
  - raw/financials/AXON_fundamentals.md
  - raw/imports/AXON_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/AXON
---

# AXON DCF Valuation - 2026-06-03

## Bottom Line

This is a source-backed scenario DCF, not a precise target price. AXON has strong business quality, but Q1 FCF was negative and FY2026 FCF guidance is only approximately USD 450M. The model therefore uses management's FY2026 FCF guidance as the starting cash-flow anchor, not Q1 annualized FCF or provider TTM FCF.

Base-case fair value is approximately **USD 136 per share**, versus a freshly checked intraday price of **USD 482.23** on 2026-06-03 at 10:51 AM EDT. Even the aggressive scenario reaches only about **USD 197 per share** under this five-year FCF fade. The market price appears to require a much longer and stronger FCF compounding path than can be verified from current sources.

Action implication: **WAIT / WATCHLIST-new-capital**. Business quality is high, but current valuation lacks margin of safety under source-backed FCF assumptions.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/AXON.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized facts | `raw/financials/AXON_fundamentals.md` | Q1/FY2025 facts, FCF, cash, debt, shares, guidance, market-data check. |
| Latest results source note | `raw/imports/AXON_latest_results_source.md` | Source map and raw extraction. |
| Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1069183/000162828026031542/axon-20260331.htm | Quarterly statements, balance sheet, debt, shares, cash flow. |
| FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1069183/000162828026011360/axon-20251231.htm | Annual history and segment baseline. |
| Q1 2026 results release / shareholder letter | https://www.sec.gov/Archives/edgar/data/1069183/000162828026031285/axon-20260506xex991.htm | FY2026 FCF guidance, revenue growth guidance, Adjusted EBITDA margin guidance, ARR, NRR, bookings. |
| StockAnalysis overview / statistics | https://stockanalysis.com/stocks/axon/ and https://stockanalysis.com/stocks/axon/statistics/ | Fresh market-data provider check on 2026-06-03. |

## Input Table

All financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Current intraday price | USD 482.23 | StockAnalysis overview, 2026-06-03 10:51 AM EDT. |
| Market capitalization | 38.87 | StockAnalysis overview. |
| Provider shares outstanding | 80.60M | StockAnalysis overview. |
| Diluted shares used for DCF | 80.60M | Provider current shares; filing Q1 common shares outstanding were 80.572M. |
| Cash + short-term investments + marketable securities | 0.737 | Q1 2026 Form 10-Q balance sheet. |
| Senior Notes principal | 1.750 | Q1 2026 Form 10-Q debt note. |
| Net debt used in DCF | 1.013 | 1.750 - 0.737. |
| Q1 2026 free cash flow | -0.055 | Q1 2026 release; OCF - capex. |
| FY2025 simple FCF | 0.075 | FY2025 Form 10-K OCF - capex. |
| FY2026 FCF guidance | approximately 0.450 | Q1 2026 release / shareholder letter. |
| FY2026 revenue guidance midpoint | 3.641 | FY2025 revenue x 31% midpoint growth. |
| FY2026 Adjusted EBITDA margin guidance | 25.5% | Q1 2026 release / shareholder letter. |
| FY2026 implied Adjusted EBITDA midpoint | 0.929 | FY2026 revenue guidance midpoint x 25.5%. |

## Base Case Assumptions

| Assumption | Conservative | Base | Aggressive |
|---|---:|---:|---:|
| Starting FCF anchor | FY2026 FCF guidance USD 450M | FY2026 FCF guidance USD 450M | FY2026 FCF guidance USD 450M |
| Year 1 FCF growth | 20.0% | 28.0% | 40.0% |
| Year 2 FCF growth | 18.0% | 24.0% | 35.0% |
| Year 3 FCF growth | 16.0% | 20.0% | 30.0% |
| Year 4 FCF growth | 14.0% | 17.0% | 25.0% |
| Year 5 FCF growth | 12.0% | 14.0% | 20.0% |
| WACC | 10.5% | 10.5% | 10.5% |
| Terminal growth | 2.5% | 2.5% | 2.5% |
| Shares | 80.60M | 80.60M | 80.60M |

WACC basis: AXON sits in Industrials / Aerospace & Defense by provider classification, but its mix includes high-growth SaaS, hardware, public-sector procurement, strategic investments, and FCF volatility. The vault reference range for Industrials is 8%-9%; the model adds a premium for growth-stage valuation sensitivity, public-sector/regulatory risk, hardware margin exposure, and volatile FCF. A base 10.5% WACC is used.

Terminal growth basis: 2.5% assumes AXON eventually fades toward mature developed-market growth after a high-growth explicit period.

## FCF Projection

Amounts are USD millions.

| Year | Conservative FCF | Base FCF | Aggressive FCF |
|---:|---:|---:|---:|
| Starting anchor | 450.0 | 450.0 | 450.0 |
| Year 1 | 540.0 | 576.0 | 630.0 |
| Year 2 | 637.2 | 714.2 | 850.5 |
| Year 3 | 739.2 | 857.1 | 1,105.7 |
| Year 4 | 842.6 | 1,002.8 | 1,382.1 |
| Year 5 | 943.7 | 1,143.2 | 1,658.5 |

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | Enterprise Value | Net Debt | Equity Value | Fair Value / Share | Upside / Downside vs USD 482.23 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Conservative | 10.5% | 2.5% | 10.036 | 1.013 | 9.023 | 111.95 | -76.8% |
| Base | 10.5% | 2.5% | 11.999 | 1.013 | 10.986 | 136.30 | -71.7% |
| Aggressive | 10.5% | 2.5% | 16.918 | 1.013 | 15.905 | 197.33 | -59.1% |

## Sensitivity Matrix

Base projection fair value per share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 9.5% | 150 | 159 | 170 |
| 10.5% | 129 | 136 | 144 |
| 11.5% | 113 | 119 | 125 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| EV / FY2026 FCF guidance | 88.6x | Very demanding for a business with negative Q1 FCF and approximately USD 450M full-year FCF guidance. |
| EV / FY2026 revenue guidance midpoint | 11.0x | Premium multiple for mixed hardware/software company, justified only if SaaS/AI/counter-drone scale strongly. |
| Provider TTM FCF | USD 19.51M | Too noisy to use as DCF anchor; highlights working-capital/acquisition volatility. |
| Base DCF terminal value share of EV | 74.1% | Assumption-heavy but below the 85%-90% danger zone. |
| Reverse DCF read | Current price requires roughly USD 1.59B starting FCF under the same base growth shape | About 3.5x management's FY2026 FCF guidance. |

## What Would Change The Valuation

- Official FCF guidance is raised materially above USD 450M.
- Q2/Q3 FCF conversion shows Q1 was purely seasonal and full-year FCF margin is sustainably rising.
- Software and Services mix grows faster with stable or expanding gross margin.
- AXON discloses stronger profitability for AI and counter-drone products.
- Price falls materially, improving FCF yield and margin of safety.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| FY2026 full-year actual results | not disclosed | Valuation relies on guidance and model assumptions. |
| FY2026 GAAP net income guidance / EBITDA reconciliation | not disclosed | Limits cross-check between Adjusted EBITDA and GAAP economics. |
| Product-level profitability | not disclosed | Cannot model AI, counter-drone, TASER, cameras, Fusus, Carbyne, and Prepared separately. |
| Segment-level FCF | not disclosed | Cannot isolate Software and Services cash generation. |
| Normalized recurring FCF | partially verified only | Q1 FCF is negative; FY2026 FCF guidance is positive but approximate. |
| Future contracted bookings margin / cancellation detail | not fully disclosed | Limits confidence in long-term conversion. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Updated `wiki/entities/AXON.md` with valuation watch items and report link. Core action read is `WAIT / WATCHLIST-new-capital`, because business quality is strong but current valuation needs a much larger FCF base than current official guidance verifies.
