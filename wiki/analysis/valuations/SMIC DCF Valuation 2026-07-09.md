---
type: analysis
analysis_type: dcf-valuation
ticker: SMIC
company: Semiconductor Manufacturing International Corporation
date: 2026-07-09
currency: USD / HKD
source_files:
  - wiki/entities/SMIC.md
  - raw/financials/SMIC_fundamentals.md
  - raw/imports/SMIC_latest_results_source.md
  - raw/imports/SMIC_market_quote_2026-07-09.md
tags:
  - analysis/dcf
  - ticker/SMIC
---

# SMIC DCF Valuation - 2026-07-09
Entity: [[SMIC]]

## Bottom Line

P11 stops before a precise fair-value DCF. Core inputs were freshly checked, but the source base is not sufficient for a point estimate:

- Fresh price: HKD 84.10 for `0981:HKG`, timestamp 2026-07-09 15:14:56 GMT+8.
- Displayed market cap: HKD 996.95B.
- Official diluted shares used in EPS: 8.012731B.
- Q1 2026 cash and cash equivalents: USD 7.279B.
- Q1 2026 debt-like obligations used for watchlist: USD 14.512B.
- Q1 2026 simple FCF: USD -0.627B.
- FY2025 annual simple FCF: RMB -39.870B.
- FY2026 FCF guidance: ไม่พบข้อมูลที่ยืนยันได้.

Action implication: **WATCHLIST / WAIT**. SMIC may be strategically important and Q2 guidance improved, but valuation cannot be underwritten with a clean DCF while FCF is negative, capex is heavy, FY2026 FCF guidance is missing, and market-cap/share-count data do not reconcile cleanly.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/SMIC.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized facts | `raw/financials/SMIC_fundamentals.md` | Q1 2026 financials, FCF, cash, debt-like obligations, shares, guidance. |
| Latest results source note | `raw/imports/SMIC_latest_results_source.md` | Official source map and raw extraction. |
| Market quote source note | `raw/imports/SMIC_market_quote_2026-07-09.md` | Fresh market price, displayed market cap, market-source share data, conflict log. |
| Google Finance `0981:HKG` | https://www.google.com/finance/quote/0981:HKG | Fresh market quote checked 2026-07-09. |

## Input Table

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh H-share price | HKD 84.10 | Google Finance `0981:HKG`, 2026-07-09 15:14:56 GMT+8. |
| Displayed market cap | HKD 996.95B | Google Finance. |
| Google displayed shares outstanding | 5.04B | Google Finance. |
| Official diluted shares used in EPS | 8.012731B | SMIC Q1 2026 income statement spreadsheet. |
| Implied shares from displayed market cap / price | 11.85B | 996.95B / 84.10. |
| Cash and cash equivalents | USD 7.279B | SMIC Q1 2026 balance sheet spreadsheet. |
| Borrowings subtotal | USD 14.508B | Non-current borrowings + current borrowings. |
| Lease liabilities | USD 0.005B | Non-current lease liabilities + current lease liabilities. |
| Debt-like obligations used for watchlist | USD 14.512B | Borrowings subtotal + lease liabilities. |
| Q1 2026 operating cash flow | USD 0.685B | SMIC Q1 2026 cash-flow spreadsheet. |
| Q1 2026 capex spend | USD 1.312B | SMIC Q1 2026 cash-flow spreadsheet. |
| Q1 2026 simple FCF | USD -0.627B | 0.685 - 1.312. |
| FY2025 annual simple FCF | RMB -39.870B | 2025 PRC cash-flow spreadsheet calculation. |
| Q2 2026 revenue guidance | +14% to +16% QoQ | SMIC Q1 2026 earnings release. |
| Q2 2026 gross-margin guidance | 20% to 22% | SMIC Q1 2026 earnings release. |

## Base Case Assumptions

No base-case DCF assumptions are set in this memo. Doing so would require unsupported normalization of:

- future FCF inflection after heavy capex,
- FY2026 full-year capex,
- total diluted share count across listing structure,
- USD/HKD valuation bridge and total market capitalization reconciliation.

## FCF Projection

ไม่พบข้อมูลที่ยืนยันได้สำหรับ source-backed positive starting FCF or FY2026 FCF guidance. A 5-year FCF projection is therefore not created.

## Valuation Summary

| Lens | Result | Read |
|---|---|---|
| DCF Read | Stopped | FCF is negative and no FY2026 FCF guidance was found. |
| Market Multiple Read | Google Finance displays P/E 118.83x | Multiple looks demanding, but EPS basis and dual-listing market cap need reconciliation before a stronger conclusion. |
| Balance Sheet Read | Cash USD 7.279B vs debt-like obligations USD 14.512B | Expansion is not net-cash-funded; balance-sheet leverage matters while FCF is negative. |
| Growth / Guidance Read | Q2 revenue +14% to +16% QoQ and gross margin 20% to 22% | Operating momentum is improving, but cash conversion remains unproven. |

## Sensitivity Matrix

Not produced. A sensitivity table would imply a base FCF anchor that is not source-backed.

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| Q1 2026 simple FCF | USD -0.627B | Negative after capex; unsuitable as positive DCF base. |
| FY2025 simple FCF | RMB -39.870B | Annual baseline confirms heavy reinvestment. |
| Debt-like obligations / cash | 1.99x | Balance sheet is not net-cash on this watchlist definition. |
| Market-source P/E | 118.83x | High headline multiple; needs EPS basis reconciliation. |
| Market cap / share-count consistency | Conflict | Google market cap, Google shares, and official diluted EPS shares do not reconcile. |

## What Would Change The Valuation

- Official FY2026 capex and cash-flow guidance.
- Positive trailing or normalized FCF after capacity expansion.
- Reconciled total share count across H shares, A shares, and diluted EPS basis.
- Clearer evidence that 20%-22% gross margin can hold while utilization remains high.
- A price reset that reduces dependence on long-run strategic optionality.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| FY2026 FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Blocks source-backed DCF. |
| FY2026 capex guidance | ไม่พบข้อมูลที่ยืนยันได้ | Blocks FCF normalization. |
| Reconciled total share count / market cap | ไม่พบข้อมูลที่ยืนยันได้ | Blocks reliable per-share fair value. |
| Official Q1 2026 transcript text | ไม่พบข้อมูลที่ยืนยันได้ | Limits management-color around guidance. |
| Positive normalized FCF base | ไม่พบข้อมูลที่ยืนยันได้ | Q1 2026 and FY2025 simple FCF are negative. |

## Entity Update

Updated `wiki/entities/SMIC.md` with valuation watch items and report link. Core action read is `WATCHLIST / WAIT`, not a DCF-derived buy/sell call.
