---
type: analysis
analysis_type: dcf-valuation
ticker: ATLX
company: Atlas Lithium Corporation
date: 2026-05-20
currency: USD
status: stopped_missing_inputs
source_files:
  - wiki/entities/ATLX.md
  - raw/financials/ATLX_fundamentals.md
  - raw/imports/ATLX_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/ATLX
---

# ATLX DCF Valuation - 2026-05-20

## Bottom Line

**DCF stopped. No fair value per share was calculated.**

เหตุผลคือ ATLX ยังเป็น pre-production / project-development equity สำหรับ Neves ใน source-backed operating results. Core inputs ที่ผู้ใช้ขอให้ fresh check มีบางตัว verify ได้แล้ว: current price, market cap, shares, cash, debt, และ historical FCF burn. แต่ `FCF` เป็น negative cash burn ไม่ใช่ normalized recurring FCF, และไม่พบ official revenue guidance หรือ FCF guidance ที่พอใช้สร้าง DCF ได้โดยไม่เดา.

Project economics ใน official April 2026 releases เช่น 146,000 tonnes/year, USD 489/tonne operating cost, USD 539M NPV, 145% IRR, และ 11-month payback เป็น forward-looking DFS/project disclosures. ยังไม่ใช่ audited commercial production, realized price, realized cost, หรือ FCF base.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/ATLX.md` | Business model, thesis, risks, source gaps. |
| Normalized facts | `raw/financials/ATLX_fundamentals.md` | Q1 2026 financials, shares, cash, debt, FCF burn, and market-data check. |
| Latest source note | `raw/imports/ATLX_latest_results_source.md` | P1 official-source extraction and handoff. |
| SEC Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1540684/000149315226021719/form10-q.htm | Latest official filing. |
| SEC FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1540684/000149315226008854/form10-k.htm | Annual cash-flow baseline and exploration-stage risk. |
| Atlas Lithium Apr. 27, 2026 news release | https://www.atlas-lithium.com/news/atlas-lithium-contracts-key-project-execution-partners-to-drive-its-neves-project-toward-production/ | Forward-looking Neves production/cost/DFS disclosures. |
| Atlas Lithium Apr. 2, 2026 news release | https://www.atlas-lithium.com/news/u-s-and-japan-identify-atlas-lithiums-neves-project-for-potential-government-financial-support-in-landmark-critical-minerals-partnership/ | Potential strategic support, forward-looking. |
| StockAnalysis ATLX market-cap page | https://stockanalysis.com/stocks/atlx/market-cap/ | Fresh price, market cap, and EV; checked 2026-05-20. |

## Input Table

| Input | Verified value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 4.275 intraday, 2026-05-19 2:55 PM EDT | StockAnalysis, checked 2026-05-20. |
| Market cap | USD 126.07M | StockAnalysis. |
| Enterprise value | USD 102.91M | StockAnalysis. |
| SEC cover-page shares outstanding | 29,490,887 | SEC Form 10-Q, as of 2026-05-04. |
| Implied market cap using SEC shares | USD 126.074M | 4.275 * 29,490,887. |
| Cash and cash equivalents | USD 34.359M | SEC Form 10-Q, 2026-03-31. |
| Convertible Debt | USD 10.180M | SEC Form 10-Q, 2026-03-31. |
| Deferred consideration from royalties sold | USD 20.000M | SEC Form 10-Q, 2026-03-31. |
| Net cash excluding royalty liability | USD 24.179M | Cash - convertible debt. |
| Net cash after convertible debt and royalty liability | USD 4.179M | Cash - convertible debt - royalty liability. |
| Q1 2026 operating cash flow | USD (10.630M) | SEC Form 10-Q. |
| Q1 2026 capex spend | USD 1.212M | SEC Form 10-Q; acquisition of capital assets converted to positive spend. |
| Q1 2026 FCF before capitalized exploration | USD (11.843M) | OCF - capex. |
| FY2025 FCF before capitalized exploration | USD (28.258M) | FY2025 OCF - capex. |
| Revenue guidance | ไม่พบข้อมูลที่ยืนยันได้ | No official revenue guide found. |
| FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | No official FCF guide found. |

## Base Case Assumptions

ไม่มี base-case DCF assumptions เพราะการตั้ง production ramp, lithium price, sustaining capex, taxes, working capital, dilution, financing cost, และ terminal value โดยไม่มี realized operating base จะเป็นการเดาเกิน source integrity rules.

## FCF Projection

ไม่จัดทำ FCF projection. Verified FCF เป็น cash burn:

| Period | Operating Cash Flow | Capex Spend | FCF Before Capitalized Exploration | Source |
|---|---:|---:|---:|---|
| Q1 2026 | (10.630M) | 1.212M | (11.843M) | SEC Form 10-Q calculation. |
| FY2025 | (22.167M) | 6.092M | (28.258M) | SEC Form 10-K calculation. |

## Valuation Summary

| Item | Result |
|---|---|
| DCF fair value per share | ไม่พบข้อมูลที่ยืนยันได้ |
| Upside/downside vs current price | ไม่พบข้อมูลที่ยืนยันได้ |
| Reason | Missing verified normalized positive FCF, revenue/FCF guidance, fully diluted share count, final funding structure, and realized lithium economics. |

## Sensitivity Matrix

Not prepared. A WACC / terminal-growth matrix would imply false precision because ATLX lacks a verified recurring FCF base and is still pre-production for the project driving the thesis.

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| Q1 2026 FCF burn before exploration / cash | 34.47% | High burn relative to cash; timing and financing matter. |
| Cash runway at Q1 operating burn | 3.23 quarters | Simple run-rate only; management says at least twelve months, but capex/financing/ramp can change quickly. |
| Market cap / Q1 annualized revenue | NM / not useful | Revenue base is tiny and not lithium commercial revenue. |
| DFS NPV vs market cap | DFS NPV USD 539M vs market cap USD 126M | Interesting optionality, but DFS is forward-looking and not realized FCF. |

## What Would Change The Valuation

- Binding financing package for Neves with cost of capital and dilution known.
- Commercial lithium concentrate shipment and realized price/cost disclosure.
- Capex-to-completion and working-capital needs verified against DFS budget.
- Fully diluted share count normalized.
- Management revenue / FCF guidance with enough detail to model ramp.
- Evidence that DFS operating cost and production target are being met in practice.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Normalized positive FCF base | ไม่พบข้อมูลที่ยืนยันได้ | Blocks DCF. |
| Revenue guidance | ไม่พบข้อมูลที่ยืนยันได้ | Blocks production ramp model. |
| FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Blocks FCF forecast. |
| Commercial lithium revenue | not disclosed / not yet generated | Blocks realized economics validation. |
| Final Neves financing package | ไม่พบข้อมูลที่ยืนยันได้ | Blocks equity value and dilution analysis. |
| Fully diluted share count | not fully normalized | Blocks reliable per-share valuation. |
| Realized production cost and recovery | ไม่พบข้อมูลที่ยืนยันได้ | DFS assumptions cannot be treated as actuals. |

## Entity Update

Updated `wiki/entities/ATLX.md` with this valuation stop memo and valuation watch items. The lack of DCF-ready inputs pushes the decision read toward `AVOID new capital / WATCHLIST only`.
