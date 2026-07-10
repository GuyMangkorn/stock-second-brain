---
type: analysis
analysis_type: dcf-valuation
ticker: VST
company: Vistra Corp.
date: 2026-06-03
currency: USD
source_files:
  - wiki/entities/VST.md
  - raw/financials/VST_fundamentals.md
  - raw/imports/VST_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/VST
---

# VST DCF Valuation - 2026-06-03
Entity: [[VST]]

## Bottom Line

This valuation uses the fresh intraday market-data check from 2026-06-03: USD 155.37 at 12:00 PM EDT, market open. Core source-backed inputs are market cap USD 52.39B, 337.18M shares outstanding, cash USD 0.634B, net debt before cash margin deposits USD 18.628B, preferred stock liquidation preference USD 2.476B, TTM GAAP-style FCF USD 1.803B, and FY2026 consolidated Adjusted FCFbG guidance midpoint USD 4.160B.

Base-case fair value is approximately **USD 120.01 per share**, or about **22.8% downside** versus USD 155.37. Bull case reaches **USD 209.62**, but it requires stronger Adjusted FCFbG growth and a lower WACC. Because VST's current price is below the bull case but above the source-backed base case, the valuation read is **WAIT for new capital / HOLD existing thesis-aware positions**, with a sharper add zone only if price falls or Q2/Q3 cash conversion validates the non-GAAP FCFbG bridge.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/VST.md` | Business model, thesis, risks, catalysts, and source gaps. |
| Normalized facts | `raw/financials/VST_fundamentals.md` | Q1 2026 financials, FY2025 baseline, FCF, cash, debt, preferred stock, shares, guidance, and market data. |
| Latest results source note | `raw/imports/VST_latest_results_source.md` | Source map and raw extraction. |
| VST Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1692819/000169281926000014/vistra-20260331.htm | Primary filing source for statements, shares, cash, debt, preferred stock, and cash flow. |
| VST Q1 2026 earnings release | https://investor.vistracorp.com/2026-05-07-Vistra-Reports-First-Quarter-2026-Results?asPDF=1 | Official results, non-GAAP reconciliation, guidance, hedging, liquidity, and buyback update. |
| VST Q1 2026 investor presentation | https://filecache.investorroom.com/mr5ir_vistracorp_ir/343/Q1_2026_Results_Presentation_vFINAL.pdf | Debt bridge, net debt, cash margin deposits, and strategic context. |
| VST FY2025 results release | https://investor.vistracorp.com/2026-02-26-Vistra-Reports-Fourth-Quarter-and-Full-Year-2025-Results?asPDF=1 | FY2025 annual baseline. |
| StockAnalysis VST quote / statistics | https://stockanalysis.com/stocks/vst/statistics/ | Fresh market price, market cap, shares outstanding, and EV checked 2026-06-03. |
| Vistra IR stock information | https://investor.vistracorp.com/stock-information | Delayed quote and market cap cross-check. |

## Input Table

All financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 155.37 | StockAnalysis, 2026-06-03 12:00 PM EDT, market open. |
| Market capitalization | 52.39 | StockAnalysis; local cross-check 155.37 * 337.18M = 52.388. |
| Market-data shares outstanding | 0.33718 | StockAnalysis; cross-check with VST Q1 release approximately 337M as of 2026-05-01. |
| Q1 2026 weighted-average diluted shares | 0.341857 | VST Q1 2026 Form 10-Q. |
| Cash and cash equivalents | 0.634 | VST Q1 2026 Form 10-Q. |
| Total Debt, company debt bridge | 19.262 | VST Q1 2026 presentation. |
| Net debt before cash margin deposits | 18.628 | VST Q1 2026 presentation: total debt 19.262 less cash 0.634. |
| Net debt after cash margin deposits | 17.569 | VST Q1 2026 presentation; shown as alternate bridge, not base case. |
| Preferred stock liquidation preference | 2.476 | VST Q1 2026 Form 10-Q. |
| FY2025 GAAP-style FCF | 1.318 | FY2025 OCF 4.070 - capex 2.752. |
| Q1 2025 GAAP-style FCF | (0.169) | Q1 2025 OCF 0.599 - capex 0.768. |
| Q1 2026 GAAP-style FCF | 0.316 | Q1 2026 OCF 1.199 - capex 0.883. |
| TTM GAAP-style FCF | 1.803 | 1.318 - (0.169) + 0.316. |
| FY2026 consolidated Adjusted FCFbG guidance | 3.760-4.560 | VST Q1 2026 release; non-GAAP. |
| Starting Adjusted FCFbG anchor | 4.160 | FY2026 consolidated Adjusted FCFbG midpoint; non-GAAP scenario anchor. |
| Local EV bridge for common equity DCF | 73.492 | Market cap 52.388 + net debt 18.628 + preferred stock 2.476. |

DCF choice: A point DCF on TTM GAAP-style FCF alone may understate VST's guided FY2026 cash generation, but a point DCF on Adjusted FCFbG may overstate owner earnings because it is non-GAAP and before growth. This memo uses consolidated Adjusted FCFbG as the scenario anchor, while using TTM GAAP-style FCF and EV multiples as sanity checks.

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | FY2026 consolidated Adjusted FCFbG low case USD 3.760B | FY2026 consolidated Adjusted FCFbG midpoint USD 4.160B | FY2026 consolidated Adjusted FCFbG high case USD 4.560B |
| Year 1 FCF growth | 0.0% | 5.0% | 8.0% |
| Year 2 FCF growth | 0.0% | 5.0% | 8.0% |
| Year 3 FCF growth | 1.0% | 4.0% | 6.0% |
| Year 4 FCF growth | 1.0% | 3.0% | 5.0% |
| Year 5 FCF growth | 1.0% | 2.5% | 4.0% |
| WACC | 10.5% | 9.5% | 8.5% |
| Terminal growth | 1.5% | 2.0% | 2.5% |
| Common-equity bridge | subtract net debt before cash margin deposits and preferred stock | subtract net debt before cash margin deposits and preferred stock | subtract net debt before cash margin deposits and preferred stock |

WACC basis: VST has power infrastructure assets, investment-grade progress, and hedged near-term generation, but it is not a pure regulated utility. Merchant power exposure, high leverage, preferred stock, hedge roll-off, regulatory risk, commodity risk, and non-GAAP FCF definition risk justify using a base WACC above the regulated Utilities range and closer to the Energy / merchant-power risk range.

Terminal growth basis: 1.5%-2.5% fits a mature, cyclical power platform. The model does not use a terminal growth rate above 2.5% because power supercycle benefits should not be assumed to compound forever.

## FCF Projection

Amounts are USD billions and use non-GAAP consolidated Adjusted FCFbG as the starting anchor.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| Starting anchor | 3.760 | 4.160 | 4.560 |
| Year 1 | 3.760 | 4.368 | 4.925 |
| Year 2 | 3.760 | 4.586 | 5.319 |
| Year 3 | 3.798 | 4.770 | 5.638 |
| Year 4 | 3.836 | 4.913 | 5.920 |
| Year 5 | 3.874 | 5.036 | 6.157 |

Base case rationale: VST's FY2026 guidance already implies a large cash-flow step-up versus TTM GAAP-style FCF. The base case allows growth from power demand, capacity prices, hedging, Meta/Cogentrix optionality not yet included in guidance, and continued buybacks, but fades growth because future hedges, capex, collateral, and regulatory terms remain uncertain.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Debt | Preferred Stock | Common Equity Value | Fair Value / Share | Upside / Downside vs USD 155.37 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 10.5% | 1.5% | 14.221 | 26.519 | 40.740 | (18.628) | (2.476) | 19.636 | 58.24 | -62.5% |
| Base | 9.5% | 2.0% | 18.063 | 43.505 | 61.568 | (18.628) | (2.476) | 40.464 | 120.01 | -22.8% |
| Bull | 8.5% | 2.5% | 21.837 | 69.946 | 91.783 | (18.628) | (2.476) | 70.679 | 209.62 | 34.9% |

## Sensitivity Matrix

Base projection fair value per share, USD. The matrix subtracts net debt before cash margin deposits and preferred stock.

| WACC / Terminal Growth | 1.5% | 2.0% | 2.5% |
|---:|---:|---:|---:|
| 8.5% | 136.45 | 148.29 | 162.11 |
| 9.5% | 111.35 | 120.01 | 129.90 |
| 10.5% | 91.84 | 98.38 | 105.75 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM GAAP-style FCF yield on market cap | 3.44% | Not cheap if GAAP `OCF - capex` is the right owner-earnings base. |
| FY2026 Adjusted FCFbG midpoint yield on market cap | 7.94% | More attractive, but this is non-GAAP and before growth. |
| Local EV / TTM GAAP-style FCF | 40.76x | Current valuation depends on cash flow stepping up materially. |
| Local EV / FY2026 Adjusted FCFbG midpoint | 17.67x | Reasonable for a scarce power platform only if guidance converts well. |
| Base DCF terminal value share of EV | 70.7% | Assumption-sensitive but not extreme for a mature DCF. |
| Bull DCF terminal value share of EV | 76.2% | Still below the 85%-90% warning threshold, but relies on favorable WACC and growth. |
| Reverse DCF growth requirement | ~8.2% annual Adjusted FCFbG growth for five years | Required to justify USD 155.37 at 9.5% WACC and 2.0% terminal growth from the FY2026 midpoint anchor. |

## What Would Change The Valuation

- Q2/Q3 2026 show GAAP `OCF - capex` converging toward Adjusted FCFbG without a large recurring growth-capex or collateral drag.
- Cogentrix closes and actual contribution is disclosed with attractive returns.
- Meta PPA economics become clearer and show durable, long-duration contracted cash flow.
- Net debt and preferred-stock drag decline faster than expected.
- Hedge coverage and power-price environment support 2027 cash generation without requiring aggressive assumptions.
- Price falls enough to create margin of safety against the base-case fair value.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Full FY2026 actual results | not disclosed | Uses Q1 2026, FY2025 baseline, and forward guide instead. |
| Official written Q1 2026 call transcript / Q&A | not verified | Limits call-level nuance and analyst pushback signals. |
| GAAP reconciliation for 2027 Adjusted EBITDA midpoint opportunity | not provided | Limits confidence in 2027+ growth modeling. |
| Post-close Cogentrix actual contribution | not disclosed | Could lift FCF or add integration / capital needs. |
| Meta PPA contribution economics | partially disclosed | Core bull narrative is not yet fully modelable. |
| Segment-level FCF | not disclosed | Cannot prove which segments produce durable distributable cash. |
| Growth capex versus maintenance capex split | partially disclosed | Key reason this is a scenario valuation, not a high-confidence fair value. |
| End-of-day 2026-06-03 market price | not available during workflow | Intraday price was used; recheck before trade execution. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Update `wiki/entities/VST.md` with this valuation memo, base-case fair value of approximately USD 120.01 per share, bull-case fair value of approximately USD 209.62, and a `WAIT / HOLD-existing` valuation read. The main follow-up is Q2 2026 cash conversion versus Adjusted FCFbG.
