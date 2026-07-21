---
type: analysis
analysis_type: decision-memo
ticker: VST
company: Vistra Corp.
date: 2026-06-03
currency: USD
decision: WAIT / HOLD-existing; watchlist for better entry or validated cash conversion
source_files:
  - index.md
  - wiki/entities/VST.md
  - raw/financials/VST_fundamentals.md
  - raw/imports/VST_latest_results_source.md
  - wiki/analysis/valuations/VST DCF Valuation 2026-06-03.md
tags:
  - analysis/decision-memo
  - ticker/VST
---

# VST Decision Memo - 2026-06-03
Entity: [[VST]]

## Action Read

**Action: WAIT / HOLD-existing. Watchlist for better entry or validated cash conversion.**

VST เป็นหนึ่งใน listed power-demand beneficiaries ที่น่าสนใจกว่าเพราะมี integrated retail + generation model, near-term hedging, dispatchable fleet, nuclear / gas optionality, and capital return. Q1 2026 operating revenue โต 43.4% YoY เป็น USD 5.640B, net income attributable to Vistra เป็น USD 1.029B, Ongoing Operations Adjusted EBITDA เป็น USD 1.494B, และ management reaffirmed FY2026 Ongoing Operations Adjusted FCFbG guidance ที่ USD 3.925B-4.725B.

แต่ที่ USD 155.37 ต่อ share ยังไม่เห็น margin of safety ชัดพอสำหรับ new capital. Base-case valuation จาก consolidated Adjusted FCFbG midpoint ให้ fair value ราว USD 120.01/share หรือ downside ประมาณ 22.8%. Bull case ไปถึง USD 209.62/share แต่ต้องอาศัย FCFbG conversion, 2027 opportunity, Cogentrix / Meta execution, และ lower risk premium. Existing position ที่เข้าใจ thesis อาจ HOLD ได้ แต่ new capital ควรรอ price pullback หรือหลักฐาน cash conversion เพิ่ม.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Fresh intraday price checked | USD 155.37 at 2026-06-03 12:00 PM EDT, market open | StockAnalysis VST statistics page, checked 2026-06-03. |
| Market cap | USD 52.39B | StockAnalysis; local cross-check 155.37 * 337.18M = 52.388B. |
| Shares outstanding | 337.18M | StockAnalysis; cross-check with VST release approximately 337M as of 2026-05-01. |
| Enterprise value | USD 72.53B | StockAnalysis VST statistics page. |
| Cash and cash equivalents | USD 0.634B | VST Q1 2026 Form 10-Q. |
| Net debt before cash margin deposits | USD 18.628B | VST Q1 2026 presentation. |
| Preferred stock liquidation preference | USD 2.476B | VST Q1 2026 Form 10-Q. |
| Local EV bridge for common equity DCF | USD 73.492B | Market cap + net debt + preferred stock. |
| TTM GAAP-style FCF | USD 1.803B | FY2025 FCF 1.318B - Q1 2025 FCF (0.169B) + Q1 2026 FCF 0.316B. |
| FY2026 consolidated Adjusted FCFbG midpoint | USD 4.160B | (3.760 + 4.560) / 2; non-GAAP guidance. |
| Local EV / FY2026 Adjusted FCFbG midpoint | 17.67x | 73.492 / 4.160. |

## Evidence From Vault

| Evidence | Read | Source |
|---|---|---|
| Q1 2026 operating revenues were USD 5.640B, up 43.4% YoY | Strong reported growth, helped by higher wholesale capacity / energy revenue and Lotus contribution. | `raw/financials/VST_fundamentals.md` |
| Q1 2026 net income attributable to Vistra was USD 1.029B | GAAP earnings rebounded, but included mark-to-market hedge effects. | VST Q1 2026 Form 10-Q / release. |
| Q1 2026 Ongoing Operations Adjusted EBITDA was USD 1.494B, up 20.5% YoY | Operating cash-generation lens improved despite Retail weakness. | VST Q1 2026 release; non-GAAP. |
| Q1 2026 GAAP-style FCF was USD 316M | Positive quarter, but still far below FY2026 Adjusted FCFbG run-rate midpoint. | VST Q1 2026 Form 10-Q. |
| FY2026 Ongoing Operations Adjusted FCFbG guidance was USD 3.925B-4.725B | Supports bull case, but is non-GAAP and before growth. | VST Q1 2026 release. |
| VST was approximately 98% hedged for expected 2026 generation volumes | Near-term earnings visibility is better than pure merchant exposure. | VST Q1 2026 release. |
| Net debt before cash margin deposits was USD 18.628B and preferred stock was USD 2.476B | Common-equity value is sensitive to capital structure. | VST Q1 2026 presentation / Form 10-Q. |
| Retail Adjusted EBITDA fell to USD 68M from USD 184M | Mild Texas weather can hit retail margin even when generation performs well. | VST Q1 2026 release. |

## Valuation Read

| Scenario | Fair Value / Share | Upside / Downside vs USD 155.37 | Read |
|---|---:|---:|---|
| Bear | USD 58.24 | -62.5% | If FCFbG does not convert into durable common cash flow, downside is severe. |
| Base | USD 120.01 | -22.8% | Good business, but price is ahead of the humble source-backed base case. |
| Bull | USD 209.62 | 34.9% | Upside exists if power-demand optionality and FCFbG conversion both work. |

Reverse DCF read: current price needs roughly 8.2% annual Adjusted FCFbG growth for five years at 9.5% WACC and 2.0% terminal growth from the FY2026 consolidated midpoint anchor. That hurdle is plausible, but it is not low-risk enough to chase without more proof.

## Bull Case

- VST has an integrated retail + generation platform that can monetize load growth through both customer relationships and generation economics.
- Dispatchable gas and nuclear exposure are scarce in a market increasingly focused on data-center power, reliability, and speed-to-power.
- FY2026 Ongoing Operations Adjusted FCFbG guidance of USD 3.925B-4.725B gives a materially stronger cash-flow lens than GAAP-style TTM FCF.
- Hedge coverage is high for 2026 and still meaningful for 2027, reducing near-term commodity exposure.
- Cogentrix and Meta PPAs are excluded from 2026 guidance, so successful execution can create upside to current modeled cash flows.
- Buybacks remain material, with approximately USD 1.5B authorization expected to be completed by year-end 2027.

## Bear Case

- The central cash-flow metric is non-GAAP and before growth; treating Adjusted FCFbG as pure owner earnings may be too generous.
- Local EV / TTM GAAP-style FCF is about 40.8x, so GAAP cash generation alone does not support the current valuation.
- Capital structure matters: net debt before cash margin deposits plus preferred stock creates a large bridge ahead of common equity.
- Retail margins are weather-sensitive, and Q1 2026 Retail Adjusted EBITDA declined sharply YoY.
- Hedge protection rolls down after 2026, increasing dependence on forward power prices, market design, and execution.
- Cogentrix, Meta PPAs, nuclear PTC, PJM / ERCOT rules, environmental obligations, outages, and collateral needs can all change value.

## Key Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| FCF basis | Scenario DCF uses FY2026 consolidated Adjusted FCFbG midpoint; sanity check uses GAAP-style TTM FCF | This is the core uncertainty in the decision. |
| Common-equity bridge | Subtract net debt before cash margin deposits and preferred stock | Preferred stock is material for common shareholders. |
| Required margin of safety | Moderate-to-high | Merchant power, leverage, hedging, and non-GAAP cash-flow definition require humility. |
| Action threshold | New capital waits for pullback or better conversion evidence | Current price is above base-case fair value. |
| Investor profile | Long-term investor with normal position sizing | No cost basis, tax status, required return, or portfolio constraints were provided. |

## What Would Change The Decision

- Upgrade toward selective ADD if price falls closer to or below the source-backed base-case range.
- Upgrade if Q2/Q3 2026 show GAAP `OCF - capex` converging toward Adjusted FCFbG.
- Upgrade if Cogentrix and Meta PPA disclosures show attractive contracted returns without excessive capex or leverage.
- Keep WAIT if price stays near USD 155 and FCFbG remains the main valuation support.
- Downgrade toward TRIM for oversized positions if price rises toward the bull case before cash-flow proof arrives.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Full FY2026 actual results | not disclosed | Need full-year cash conversion and hedge performance. |
| Official written Q1 2026 call transcript / full Q&A | not verified | Limits view of analyst pushback and management nuance. |
| GAAP reconciliation for 2027 Adjusted EBITDA midpoint opportunity | not provided | Limits confidence in 2027+ modeling. |
| Post-close Cogentrix actual contribution | not disclosed | Could change both FCF and debt/capex profile. |
| Meta PPA contribution economics | partially disclosed | Core bull case cannot be fully modeled yet. |
| Segment-level FCF | not disclosed | Cannot isolate Retail, Texas, East, and West cash engines. |
| Growth capex versus maintenance capex split | partially disclosed | Determines whether FCFbG is a fair owner-earnings proxy. |
| End-of-day 2026-06-03 price | not available during workflow | Intraday price was used; recheck before trade execution. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/VST.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized financial facts | `raw/financials/VST_fundamentals.md` | Q1 2026 facts, FY2025 baseline, market data, cash, debt, preferred stock, shares, FCF, guidance. |
| Latest results source note | `raw/imports/VST_latest_results_source.md` | Source map and extracted facts. |
| DCF valuation memo | `wiki/analysis/valuations/VST DCF Valuation 2026-06-03.md` | Source-backed scenario valuation and sensitivity. |
| VST Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1692819/000169281926000014/vistra-20260331.htm | Primary filing source. |
| VST Q1 2026 earnings release | https://investor.vistracorp.com/2026-05-07-Vistra-Reports-First-Quarter-2026-Results?asPDF=1 | Official results and guidance. |
| VST Q1 2026 investor presentation | https://filecache.investorroom.com/mr5ir_vistracorp_ir/343/Q1_2026_Results_Presentation_vFINAL.pdf | Debt bridge, hedging, strategic context. |
| VST FY2025 results release | https://investor.vistracorp.com/2026-02-26-Vistra-Reports-Fourth-Quarter-and-Full-Year-2025-Results?asPDF=1 | FY2025 baseline. |
| StockAnalysis VST statistics | https://stockanalysis.com/stocks/vst/statistics/ | Fresh market data. |
