---
type: analysis
analysis_type: dcf-valuation
ticker: VZ
company: Verizon Communications Inc.
date: 2026-05-19
currency: USD
source_files:
  - wiki/entities/VZ.md
  - raw/financials/VZ_fundamentals.md
  - raw/imports/VZ_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/VZ
---

# VZ DCF Valuation - 2026-05-19
Entity: [[VZ]]

## Bottom Line

This DCF can be run because the required inputs were freshly checked: current price, market cap, shares, cash, debt, FCF, and guidance. The important caveat is that Verizon is highly levered, and the DCF follows the vault rule of calculating enterprise value from FCF and then subtracting cash/debt. That makes the output very sensitive to WACC and leverage.

Using FY2026 FCF guidance of USD 21.5B or more as Year 1 FCF, Q1 2026 cash of USD 8.366B, total debt of USD 172.460B, diluted weighted-average shares of 4.210B, a base WACC of 9.0%, terminal growth of 2.0%, and a five-year FCF growth path fading from 3.0% to 2.0%, base-case fair value is approximately USD 34.96 per diluted share.

Against the fresh close-price check of USD 46.88 on 2026-05-18, the base case implies about 25% downside. The bull sensitivity at 8.0% WACC and 2.0% terminal growth reaches approximately USD 47.29 per share, roughly current price, but it leaves little margin of safety.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/VZ.md` | Business model, source map, thesis, risks. |
| Normalized facts | `raw/financials/VZ_fundamentals.md` | Q1 2026 financials, balance sheet, FCF, shares, segment data, and guidance. |
| Latest source note | `raw/imports/VZ_latest_results_source.md` | Local source extraction and ingest provenance. |
| SEC Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/732712/000073271226000023/vz-20260331.htm | Official quarterly facts, shares, cash, debt, OCF, capex. |
| FY2025 Form 10-K | https://www.verizon.com/about/sites/default/files/2025-Annual-Report-on-Form-10k.pdf | FY2025 annual FCF baseline. |
| Verizon Q1 2026 earnings release | https://www.verizon.com/about/news/feed/verizons-transformation-actions-deliver-growth-profitability-1q26-company-raises-adjusted-eps | FY2026 guidance and operating highlights. |
| Q1 2026 earnings transcript | https://www.verizon.com/about/file/77847/download?token=DCOVBtyf | Management commentary and guidance context. |
| MarketBeat VZ stock page | https://www.marketbeat.com/stocks/NYSE/VZ/ | Fresh price and market cap check, checked 2026-05-19 Bangkok time. |

## Input Table

All company financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 46.88 | MarketBeat, close for 2026-05-18; checked 2026-05-19 Bangkok time. |
| Extended-hours quote | USD 46.79 | MarketBeat, 2026-05-19 04:35 AM Eastern. |
| Market cap | USD 195.74B | MarketBeat key stats. |
| Diluted shares used for DCF | 4.210B | SEC 10-Q, Q1 2026 diluted weighted-average shares. |
| Common shares outstanding | 4.176B | SEC 10-Q, 2026-03-31. |
| Cash and cash equivalents | 8.366 | SEC 10-Q. |
| Debt maturing within one year | 28.229 | SEC 10-Q. |
| Long-term debt | 144.231 | SEC 10-Q. |
| Total debt | 172.460 | 28.229 + 144.231. |
| Net debt | 164.094 | 172.460 - 8.366. |
| Q1 2026 operating cash flow | 7.984 | SEC 10-Q. |
| Q1 2026 capex spend | 4.201 | SEC 10-Q, cash outflow converted to positive spend. |
| Q1 2026 free cash flow | 3.783 | 7.984 - 4.201. |
| FY2025 operating cash flow | 37.137 | FY2025 Form 10-K. |
| FY2025 capex spend | 17.011 | FY2025 Form 10-K. |
| FY2025 free cash flow | 20.126 | 37.137 - 17.011. |
| FY2026 FCF guidance | 21.5 or more | Verizon Q1 2026 earnings release. |
| FY2026 adjusted EPS guidance | USD 4.95 to USD 4.99 | Verizon Q1 2026 earnings release. |
| FY2026 capex guidance | 16.0 to 16.5 | Verizon Q1 2026 earnings release. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Year 1 FCF anchor | 21.5 | 21.5 | 21.5 |
| Year 2 FCF growth | 2.0% | 3.0% | 4.0% |
| Year 3 FCF growth | 1.5% | 2.5% | 3.5% |
| Year 4 FCF growth | 1.0% | 2.0% | 3.0% |
| Year 5 FCF growth | 1.0% | 2.0% | 2.5% |
| WACC | 10.0% | 9.0% | 8.0% |
| Terminal growth | 2.0% | 2.0% | 2.0% |

WACC basis: Verizon sits in Communication Services, where the vault reference range is 8%-10%. Base WACC is 9.0% because recurring telecom demand and scale help, while high leverage, capex intensity, competition, integration risk, and regulatory/network reliability risk keep the discount rate above the lower end.

Terminal growth basis: 2.0% is inside the mature developed-market / GDP-like company range in `wiki/reference/valuation-assumptions.md`.

## FCF Projection

Base case amounts are USD billions.

| Year | FCF | Growth |
|---:|---:|---:|
| Year 1 | 21.500 | guidance floor |
| Year 2 | 22.145 | 3.0% |
| Year 3 | 22.699 | 2.5% |
| Year 4 | 23.153 | 2.0% |
| Year 5 | 23.616 | 2.0% |

Base rationale: the model uses company-disclosed FY2026 FCF guidance as the starting point and then fades toward mature telecom growth. This avoids inventing a high-growth telecom forecast unsupported by source data.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | Enterprise Value | Cash | Total Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 46.88 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 10.0% | 2.0% | 272.3 | 8.4 | (172.5) | 108.2 | 25.70 | -45.2% |
| Base | 9.0% | 2.0% | 311.3 | 8.4 | (172.5) | 147.2 | 34.96 | -25.4% |
| Bull | 8.0% | 2.0% | 363.2 | 8.4 | (172.5) | 199.1 | 47.29 | 0.9% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 1.5% | 2.0% | 2.5% |
|---:|---:|---:|---:|
| 8.0% | 42.01 | 47.29 | 53.54 |
| 9.0% | 31.17 | 34.96 | 39.32 |
| 10.0% | 22.89 | 25.70 | 28.90 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| FY2026 guided FCF yield on market cap | 10.98% | High equity FCF yield, but leverage absorbs much of the EV. |
| Market EV / FY2026 guided FCF | 16.7x | Calculation: (195.74 + 164.09) / 21.5. |
| Net debt / FY2026 guided FCF | 7.63x | Total-debt net debt basis; high balance sheet sensitivity. |
| Net unsecured debt / adjusted EBITDA | 2.6x | Company non-GAAP metric from Q1 2026 release. |
| Base terminal value share of EV | 71.8% | High but below the 85%-90% warning zone. |
| FY2026 dividend payout vs guided FCF | approximately 53.4% | FY2025 dividends paid 11.481 / FY2026 FCF guidance floor 21.5. |

## What Would Change The Valuation

- Total debt and net debt decline faster than the current source-backed path.
- Frontier integration produces clear cost synergies without higher capex or churn pressure.
- FY2026 actual FCF exceeds the USD 21.5B floor materially.
- Mobility and broadband service revenue growth sustains at or above the guided range with lower promotional intensity.
- WACC can be justified closer to 8.0% because leverage and integration risk fall.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Product-level profitability by wireless, FWA, fiber, IoT, security, and enterprise services | not disclosed | Limits segment-specific valuation. |
| Frontier standalone post-close financial contribution in Q1 2026 | not fully isolated | Makes pro forma post-acquisition run-rate less clear. |
| Exact normalized recurring FCF after Frontier integration and debt paydown | ไม่พบข้อมูลที่ยืนยันได้ | DCF uses FY2026 guidance floor rather than invented integration-adjusted FCF. |
| Intrayear market price after regular market open on 2026-05-19 | ไม่พบข้อมูลที่ยืนยันได้ | Valuation uses 2026-05-18 close and 2026-05-19 extended-hours check. |
| Investor-specific required return and dividend-income need | not provided | Affects whether the stock is suitable as income hold versus new capital add. |

## Entity Update

Updated `wiki/entities/VZ.md` with this valuation memo link and valuation watch items. The valuation changes the decision read toward wait/watchlist for new capital at current price, while an existing income-focused position may still be held if sizing and dividend-risk tolerance are appropriate.
