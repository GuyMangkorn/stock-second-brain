---
type: analysis
analysis_type: decision-memo
ticker: UL
company: Unilever PLC
date: 2026-06-28
currency: EUR
decision: WATCHLIST / WAIT; do not add new capital without better margin of safety
source_files:
  - wiki/entities/UL.md
  - raw/financials/UL_fundamentals.md
  - raw/imports/UL_latest_results_source.md
  - wiki/analysis/valuations/UL DCF Valuation 2026-06-28.md
tags:
  - analysis/decision-memo
  - ticker/UL
---

# UL Decision Memo - 2026-06-28

## Action Read

**Action: WATCHLIST / WAIT. Do not add new capital at USD 60.55 unless price improves, FY2026 FCF confirms the volume-led recovery, or margin expansion becomes clearer.**

UL มี quality signals ที่น่าสนใจ: Q1 2026 USG 3.8%, UVG 2.9%, Power Brands USG 5.0%, emerging markets USG 5.7%, FY2026 guidance ยังยืนยัน bottom end ของ 4%-6% range และ margin น่าจะ improve modestly. แต่ current valuation ยังไม่ให้ margin of safety เพียงพอ. Base-case DCF ได้ fair value ประมาณ USD 53.28 ต่อ ADR-equivalent share เทียบกับ USD 60.55 ล่าสุด หรือ downside ราว 12.0%.

สำหรับ existing position: **HOLD / WATCH** ได้ถ้าต้องการ defensive consumer staples exposure และเชื่อใน post-demerger execution. สำหรับ new money: **WAIT** จนกว่าจะมีราคาที่ดีกว่า หรือ source-backed FCF/cash/debt หลัง Q1/H1 2026 ชัดขึ้น.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| UL ADR close used | USD 60.55 on 2026-06-26 | StockAnalysis UL quote, checked 2026-06-28 Asia/Bangkok. |
| After-hours price | USD 61.21 on 2026-06-26 7:57 PM EDT | StockAnalysis UL quote. |
| Market cap | USD 131.45B | StockAnalysis UL quote. |
| Shares out | 2.18B | StockAnalysis UL quote. |
| Diluted shares used in DCF | 2,195.3M | Unilever Annual Report 2025. |
| Cash and cash equivalents | EUR 3.941B | Unilever Annual Report 2025. |
| Total financial liabilities used as debt | EUR 28.278B | Unilever Annual Report 2025. |
| Net debt | EUR 23.076B | Unilever Annual Report 2025. |
| FY2025 FCF | EUR 5.921B | Unilever Annual Report 2025. |
| EUR/USD | 1.13904 | XE, checked 2026-06-28 07:58 UTC. |
| Market FCF yield | 5.13% | FY2025 FCF converted to USD / StockAnalysis market cap. |
| Market EV / FY2025 FCF | 23.60x | Market cap converted to EUR + debt - cash, divided by FY2025 FCF. |

## Evidence From Vault

| Evidence | Read | Source |
|---|---|---|
| Q1 2026 USG was 3.8% and UVG was 2.9% | Growth quality improved because volume drove most of the quarter. | `raw/financials/UL_fundamentals.md` |
| Power Brands grew 5.0% with 4.0% volume growth | Brand focus is showing stronger momentum than group average. | `raw/financials/UL_fundamentals.md` |
| Emerging markets USG was 5.7% with 4.2% volume growth | EM remains a key growth engine. | `raw/financials/UL_fundamentals.md` |
| FY2025 UOM was 20.0% | Profitability is solid for staples, but needs post-transition consistency. | Annual Report 2025 / normalized facts |
| FY2025 FCF was EUR 5.921B, down from EUR 6.304B in FY2024 | Cash generation is material but not yet accelerating. | Annual Report 2025 / normalized facts |
| Net debt was EUR 23.076B | Balance sheet is manageable but not light relative to FCF. | Annual Report 2025 / normalized facts |
| FY2026 guidance calls for USG near bottom end of 4%-6%, at least 2% volume growth and modest margin improvement | Management is constructive but not signaling a breakout. | Q1 2026 Overview FAQ |
| Q1 2026 captured source lacks full statements | Decision should stay humble until H1/full filing confirms cash flow and balance sheet. | Source note missing data |

## Valuation Read

| Scenario | Fair Value / ADR-Equivalent USD | Upside / Downside vs USD 60.55 | Read |
|---|---:|---:|---|
| Bear | USD 30.13 | -50.2% | If FCF stays flat and WACC rises, leverage and terminal-value sensitivity hurt equity value. |
| Base | USD 53.28 | -12.0% | Quality is not enough for ADD at current price. |
| Bull | USD 73.28 | +21.0% | Requires sustained volume-led USG, margin expansion, and lower WACC / stronger terminal assumptions. |

Valuation lens: DCF-led with market FCF yield and EV/FCF sanity checks. DCF is appropriate enough because Unilever has positive, source-backed FCF, but the output should be treated as scenario valuation, not a precise target. Base case uses FY2025 actual FCF because Q1 2026 source does not provide full cash-flow data.

## Bull Case

- Post-Ice-Cream Unilever is simpler and more category-focused.
- Q1 2026 growth was volume-led, with Power Brands and emerging markets outperforming group average.
- FY2025 UOM of 20.0% and modest margin-improvement guidance support quality thesis.
- Long-term algorithm targets mid-single-digit USG, at least 2% UVG, modest UOM improvement and about 100% cash conversion.
- EUR 1.5B buyback and capital allocation discipline can support per-share compounding if FCF holds.
- Defensive consumer staples exposure can deserve a premium when execution improves.

## Bear Case

- Base-case DCF is below current price, so valuation risk is immediate.
- FY2025 FCF declined from FY2024, and Q1 2026 source does not include cash flow.
- Total financial liabilities / FY2025 FCF is about 4.78x; net debt / FY2025 FCF is about 3.90x.
- Portfolio transition after Ice Cream demerger and Foods-related transaction context can make historical comparison messy.
- Consumer staples premium multiples can compress if rates rise or if volume-led growth fades.
- ADR mechanics were not independently verified from depositary/company source.

## Key Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| FCF basis | FY2025 company-reported FCF of EUR 5.921B | Source-backed and avoids inferring capex from incomplete extracted tables. |
| WACC | 7.5% base | Consumer Staples reference range is 7%-8%; emerging-market exposure, leverage and portfolio transition keep it above best-quality low end. |
| Terminal growth | 2.5% base | Mature developed-market compounder assumption. |
| FX | EUR/USD 1.13904 | Converts EUR fair value to USD ADR-equivalent read. |
| Action threshold | Require margin of safety before ADD | Current base fair value is below market price. |
| Investor profile | Long-term investor, no cost basis or sizing provided | Memo avoids personalized tax/sizing advice. |

## What Would Change The Decision

- Upgrade toward ADD if price falls below base fair value while Q1/H1 2026 execution and FCF remain intact.
- Upgrade toward ADD if H1/FY2026 results show FCF growth, lower leverage, sustained UVG above 2%, and UOM expansion.
- Keep HOLD/WATCH if valuation remains premium but volume-led growth continues.
- Downgrade toward AVOID if FCF weakens, debt rises, guidance is cut, or Power Brands momentum fades.
- Re-run valuation after next full filing with updated cash, debt, shares, FCF and guidance.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Q1 2026 full income statement, balance sheet and cash flow | not disclosed in captured source | Current P11/P13 must rely on FY2025 FCF, cash, debt and shares. |
| Latest balance sheet after 2025-12-31 | not disclosed | Debt/cash may have changed after buyback and portfolio actions. |
| Official Q1 2026 transcript / Q&A | ไม่พบข้อมูลที่ยืนยันได้ | Limits confidence in management commentary behind guidance. |
| Legal ADR-to-ordinary share ratio source | ไม่พบข้อมูลที่ยืนยันได้ | DCF is labeled ADR-equivalent and uses market shares as cross-check. |
| Capex-only annual line | ไม่พบข้อมูลที่ยืนยันได้ in extracted table | Uses company-reported FCF instead of deriving FCF. |
| Product-level profitability below business groups | not disclosed | Cannot underwrite brand/product economics below business group level. |
| Investor-specific cost basis, position size, tax status and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/UL.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized financial facts | `raw/financials/UL_fundamentals.md` | Q1 2026 facts, FY2025 annual baseline, market data, cash, debt, FCF, guidance. |
| Latest results source note | `raw/imports/UL_latest_results_source.md` | Source map and raw extraction. |
| DCF valuation memo | `wiki/analysis/valuations/UL DCF Valuation 2026-06-28.md` | Source-backed valuation scenarios and sensitivity. |
| Unilever Annual Report and Accounts 2025 / Form 20-F | https://www.unilever.com/files/unilever-annual-report-and-accounts-2025.pdf | FY2025 financials and capital allocation. |
| Unilever Q1 2026 Overview | https://www.unilever.com/investors/results-events/results-events-webcasts/overview-q1-2026/ | Latest official trading update and guidance. |
| StockAnalysis UL quote | https://stockanalysis.com/stocks/ul/ | Fresh ADR price and market data. |
| XE EUR/USD converter | https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD | Fresh FX conversion. |
