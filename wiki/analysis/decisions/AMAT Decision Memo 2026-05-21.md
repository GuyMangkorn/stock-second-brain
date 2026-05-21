---
type: analysis
analysis_type: decision-memo
ticker: AMAT
company: Applied Materials, Inc.
date: 2026-05-21
action_read: AVOID-new-capital / WAIT-for-better-entry
currency: USD
source_files:
  - wiki/entities/AMAT.md
  - raw/financials/AMAT_fundamentals.md
  - wiki/analysis/valuations/AMAT DCF Valuation 2026-05-21.md
tags:
  - analysis/decision
  - ticker/AMAT
---

# AMAT Decision Memo - 2026-05-21

## Action Read

**AVOID-new-capital / WAIT-for-better-entry.**

AMAT is a high-quality semiconductor equipment leader with strong Q2 FY2026 execution and direct exposure to AI infrastructure, DRAM/HBM, leading-edge logic, and advanced packaging. The problem is not business quality; the problem is valuation. At USD 426.85, source-backed TTM FCF yield is only about 1.6%, and the base-case DCF fair value is far below the market quote.

ถ้ามี existing position, this memo supports **hold only with explicit valuation-risk tolerance** and a plan to refresh after Q3 FY2026 FCF conversion. For new capital, wait for either a much better price or verified FCF normalization.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Latest regular-session quote used | USD 426.85 on 2026-05-20 at 4:00 PM EDT | FinancialContent delayed quote; checked 2026-05-21. |
| Basic shares used for market cap | 794.0M | Q2 FY2026 weighted-average basic shares. |
| Approximate market capitalization | USD 338.92B | 426.85 * 794.0M. |
| Diluted shares used for DCF | 799.0M | Q2 FY2026 weighted-average diluted shares. |
| TTM FCF | USD 5.343B | FY2025 FCF + 6M FY2026 FCF - 6M FY2025 FCF. |
| TTM FCF yield | 1.58% | 5.343 / 338.92. |
| Market EV / TTM FCF | 63.5x | (338.92 + 6.455 - 8.241) / 5.343. |

Market data is provider-sourced and showed variance across current quote sources. The decision uses the latest dated regular-session quote found and records that variance as a source gap.

## Evidence From Vault

| Evidence | Read |
|---|---|
| Q2 FY2026 revenue was USD 7.910B, up 11.4% YoY | Strong operational momentum. |
| Q2 FY2026 non-GAAP EPS was USD 2.86, up 19.7% YoY | Earnings power improving. |
| Q3 FY2026 revenue guidance is USD 8.950B +/- USD 0.500B | Management sees near-term acceleration. |
| Management expects semiconductor equipment business to grow more than 30% in calendar 2026 | Bullish demand signal tied to AI / leading-edge logic / DRAM / advanced packaging. |
| 6M FY2026 FCF was USD 1.250B vs USD 1.605B in 6M FY2025 | Cash conversion has not yet confirmed the revenue/EPS story. |
| TTM FCF is USD 5.343B vs market cap about USD 338.92B | Valuation requires a large FCF recovery. |
| Net cash is USD 1.786B | Balance sheet is fine; this is not a leverage concern. |

## Valuation Read

| Scenario | Fair Value / Share | Upside / Downside vs USD 426.85 |
|---|---:|---:|
| Bear | USD 76.97 | -82.0% |
| Base | USD 120.50 | -71.8% |
| Bull | USD 181.22 | -57.5% |

DCF conclusion: current market price is far above source-backed DCF range. To justify the current quote, AMAT would need much higher normalized FCF than latest official TTM FCF. That may happen if the AI equipment cycle translates into major cash conversion, but the official source set does not yet verify it.

## Bull Case

AMAT has one of the cleanest equipment exposures to the AI semiconductor build-out. Semiconductor Systems is large and profitable, AGS growth was strong, and Q3 guidance points to acceleration. Management is explicitly bullish on calendar 2026 semiconductor equipment growth and has increased build plans and inventory positions to meet demand.

ถ้า Q3/Q4 show that inventory and capex build convert into high-margin revenue and FCF, today's DCF would be too conservative. Net cash balance sheet also gives management room to keep investing while returning capital.

## Bear Case

The stock price already prices a very large amount of future success. TTM FCF yield near 1.6% leaves little room for disappointment. Semiconductor equipment cycles can overshoot, customer capex can pause, and export controls / China exposure can create abrupt demand or shipment changes. Q2 GAAP net income was helped by investment gains, while FCF was weak.

ถ้า FCF conversion remains low, current valuation is difficult to defend.

## Key Assumptions

| Assumption | Why it matters |
|---|---|
| TTM FCF is the valuation anchor until official FCF guidance or stronger actual FCF is verified | Prevents replacing source-backed cash flow with a narrative estimate. |
| Q3 revenue/EPS guide supports growth, not automatically FCF conversion | Earnings and cash flow can diverge during inventory/capacity build. |
| Base WACC 9.5% | Reflects high-quality tech market leader plus semiconductor equipment cyclicality and geopolitical/customer concentration risk. |
| Terminal growth 2.5% | Mature developed-market compounder assumption; avoids perpetual AI supercycle extrapolation. |

## What Would Change The Decision

- Q3 FY2026 reports strong FCF recovery alongside revenue/EPS growth.
- Management provides source-backed FY2026 FCF guidance or a clearer working-capital bridge.
- Stock price falls enough to create a margin of safety versus a conservative FCF DCF.
- New official filings show higher period-end shares, debt, or capex needs that worsen valuation.
- China/export-control or customer capex risk materially changes.

## Missing / Unverified Data

| Item | Status | Decision impact |
|---|---|---|
| Q2 FY2026 Form 10-Q | not found | Update source base when filed. |
| FY2026 full-year FCF guidance | not disclosed | Cannot justify a high normalized FCF input. |
| Exact Q2 period-end shares outstanding | not verified | Uses weighted-average shares; refresh from next 10-Q. |
| Official full Q2 FY2026 transcript / Q&A | ไม่พบข้อมูลที่ยืนยันได้ | Limits management-commentary depth. |
| Segment-level FCF | not disclosed | Cannot verify cash engine by segment. |
| Customer-specific AI/HBM/advanced-packaging economics | not disclosed | AI upside cannot be directly modeled. |
| Market-data provider variance | provider-sourced | Refresh quote before any action change. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| [[AMAT_latest_results_source]] | `raw/imports/AMAT_latest_results_source.md` | P1 source note and extracted source map. |
| [[AMAT_fundamentals]] | `raw/financials/AMAT_fundamentals.md` | P4 normalized facts, FCF, cash, debt, shares, market-data check. |
| [[AMAT]] | `wiki/entities/AMAT.md` | P6 thesis, risks, catalysts, valuation watch items. |
| [[AMAT DCF Valuation 2026-05-21]] | `wiki/analysis/valuations/AMAT DCF Valuation 2026-05-21.md` | P11 source-backed DCF. |
| Applied Materials Q2 FY2026 Exhibit 99.1 | https://www.sec.gov/Archives/edgar/data/6951/000162828026035071/exhibit991q22026earningsre.htm | Official latest results and guidance. |
| Applied Materials FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/6951/000162828025056742/amat-20251026.htm | FY2025 annual baseline and business/risk context. |
| FinancialContent AMAT quote | https://markets.financialcontent.com/stocks.wetm/quote/detailedquote?Symbol=NQ%3AAMAT | Fresh market price check. |
