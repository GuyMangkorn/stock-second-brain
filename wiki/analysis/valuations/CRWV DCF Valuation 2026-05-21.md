---
type: valuation
ticker: CRWV
company: CoreWeave, Inc.
date: 2026-05-21
valuation_type: DCF stop-before-fair-value
action_dependency: P13
price_checked: "2026-05-21"
tags:
  - analysis/valuation
  - ticker/CRWV
---

# CRWV DCF Valuation - 2026-05-21
Entity: [[CRWV]]

## Bottom Line

P11 **stopped before calculating a precise DCF fair value**. The reason is not lack of growth data; it is lack of a source-backed positive normalized FCF base. CRWV has verified strong revenue growth, backlog, and FY2026 guidance, but FY2025 FCF, Q1 2026 FCF, and TTM FCF are all negative by `OCF - cash capex`.

Fresh market data checked 2026-05-21 shows USD 101.28 close price, USD 55.26B market cap, USD 88.14B enterprise value, and 545.57M shares out. At that price, the stock is being valued on AI infrastructure growth and backlog conversion, not on current FCF support.

## Source Map

| Source | URL / Path | Used For |
|---|---|---|
| Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000222/crwv-20260331.htm | Cash, debt, leases, shares, Q1 financials, and cash flow |
| FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm | Annual revenue, OCF, capex, and FCF baseline |
| Q1 2026 earnings release | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-First-Quarter-2026-Results/default.aspx | Adjusted EBITDA, backlog, RPO, capex, and summary results |
| Q1 2026 outlook presentation | https://s205.q4cdn.com/133937190/files/doc_financials/2026/q1/CoreWeave-1Q26-Outlook-Presentation.pdf | Q2 2026 and FY2026 guidance |
| Q1 2026 earnings call transcript | https://s205.q4cdn.com/133937190/files/doc_financials/2026/q1/CoreWeave-Inc-CRWV-US-Q1-2026-Earnings-Call-7-May-2026-5_00-PM-ET.pdf | Management commentary on growth, capex, funding, and guidance context |
| StockAnalysis CRWV quote / statistics | https://stockanalysis.com/stocks/crwv/ | Current price, market cap, enterprise value, shares out, and provider multiples checked 2026-05-21 |
| Local fundamentals | `raw/financials/CRWV_fundamentals.md` | Normalized source-backed facts |

## Input Table

| Input | Value | Source / Basis |
|---|---:|---|
| Current close price | 101.28 | StockAnalysis, at close 2026-05-20 4:00 PM EDT; checked 2026-05-21 |
| Pre-market price | 105.95 | StockAnalysis, 2026-05-21 8:15 AM EDT |
| Market cap | 55.26B | StockAnalysis provider value |
| Enterprise value | 88.14B | StockAnalysis provider value |
| Shares out | 545.57M | StockAnalysis provider value; aligns with Q1 2026 Form 10-Q total shares at 2026-04-30 |
| Cash and marketable securities | 2.266B | Q1 2026 Form 10-Q |
| Cash, restricted cash, and marketable securities | 3.342B | Q1 2026 Form 10-Q / earnings release |
| Total debt excluding leases | 24.859B | Q1 2026 Form 10-Q |
| Debt-like obligations including leases | 35.147B | Q1 2026 Form 10-Q |
| Q1 2026 FCF | (4.711B) | OCF 2.984B - cash capex 7.695B |
| TTM FCF | (10.616B) | FY2025 FCF + Q1 2026 FCF - Q1 2025 FCF |
| FY2026 revenue guidance midpoint | 12.5B | Q1 2026 outlook presentation |
| FY2026 adjusted operating income guidance midpoint | 1.0B | Q1 2026 outlook presentation |
| FY2026 capex guidance midpoint | 33.0B | Q1 2026 outlook presentation |
| FY2026 FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Not disclosed in official materials reviewed |

## Base Case Assumptions

No base-case DCF assumptions were selected because the minimum viable DCF input set is not source-sufficient. A precise DCF would require assumptions about when capex normalizes, how much backlog converts into OCF, what maintenance capex looks like after the buildout, and what financing cost remains after the current expansion cycle.

| Assumption Needed | Status | Why It Matters |
|---|---|---|
| Positive normalized FCF base | Missing | Current, FY2025, and TTM FCF are negative. |
| FY2026 FCF guidance | Missing | Revenue and adjusted operating income guidance do not translate directly into FCF because capex is very large. |
| Maintenance versus growth capex split | Missing | DCF needs a sustainable FCF base after the buildout. |
| Long-term interest cost / funding terms | Partial | Q2 interest expense guidance exists, but full pro forma debt cost after post-quarter financing is not verified. |
| Customer concentration economics | Partial | Backlog is large, but detailed customer economics are not fully disclosed. |

## FCF Projection

Not calculated. The verified FCF base is negative:

| Period | OCF | Cash Capex | FCF |
|---|---:|---:|---:|
| FY2023 | 1.833B | 2.943B | (1.110B) |
| FY2024 | 2.749B | 8.702B | (5.953B) |
| FY2025 | 3.058B | 10.309B | (7.251B) |
| Q1 2026 | 2.984B | 7.695B | (4.711B) |
| TTM ended 2026-03-31 | 5.981B | 16.597B | (10.616B) |

## Valuation Summary

No DCF fair value per share was calculated.

Cross-checks that can be source-backed today:

| Cross-Check | Value | Read |
|---|---:|---|
| EV / TTM revenue | 14.15x | High multiple on a business with negative TTM FCF. |
| EV / FY2026 revenue guidance midpoint | 7.05x | Still growth-priced even against forward revenue guidance. |
| Market cap / FY2026 revenue guidance midpoint | 4.42x | Equity value assumes continued execution and funding access. |
| TTM FCF | (10.616B) | Positive FCF yield is not meaningful. |
| Debt-like obligations including leases / market cap | 63.6% | 35.147B / 55.26B; leverage and leases are central to equity risk. |

## Sensitivity Matrix

DCF sensitivity is not calculated because the FCF base is negative and no source-backed positive normalized FCF bridge was verified.

| Terminal Growth / WACC | 10.0% | 11.0% | 12.0% |
|---|---|---|---|
| 2.0% | not calculated | not calculated | not calculated |
| 2.5% | not calculated | not calculated | not calculated |
| 3.0% | not calculated | not calculated | not calculated |

## Sanity Checks

- Revenue growth is source-backed, but FCF support is not. This makes a conventional FCF DCF fragile.
- FY2026 capex guidance midpoint is USD 33B, much larger than FY2026 revenue guidance midpoint of USD 12.5B.
- Q2 2026 guidance includes USD 650M to USD 730M of interest expense, so financing cost is already material.
- Enterprise value is about USD 88.14B while TTM FCF is negative USD 10.616B.
- Treating leases as debt-like obligations is important because capacity commitments are central to the business model.

## What Would Change The Valuation

- Official FY2026 or medium-term FCF guidance that bridges from negative FCF to positive normalized FCF.
- A disclosed maintenance capex range after the current AI infrastructure buildout.
- Evidence that revenue backlog converts into OCF without incremental leverage accelerating.
- Lower funding cost, less restrictive debt terms, or more equity-friendly financing.
- Segment or customer economics that prove durable returns on invested capital above WACC.

## Missing / Unverified Data

- FY2026 full-year actual results are not available as of 2026-05-21.
- FY2026 free cash flow guidance is not disclosed.
- Positive normalized FCF is not verified.
- Maintenance capex versus growth capex is not disclosed.
- Revenue by product line, customer type, or individual major customer is not fully disclosed.
- Segment-level operating income and segment-level FCF are not disclosed.
- Post-quarter DDTL 5.0 draw amounts and exact pro forma debt outstanding are not verified in a filing-level balance sheet.
- GAAP net income or EPS guidance for FY2026 was not verified.
- Investor-specific cost basis, position size, tax status, and required return were not provided.

## Entity Update

Updated `wiki/entities/CRWV.md` with valuation watch items and an AVOID-new-capital / WATCHLIST read because P11 lacks source-backed inputs for a positive-FCF DCF.
