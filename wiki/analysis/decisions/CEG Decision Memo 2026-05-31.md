---
type: analysis
analysis_type: decision-memo
ticker: CEG
company: Constellation Energy Corporation
date: 2026-05-31
currency: USD
decision: WAIT / WATCHLIST-new-capital; HOLD only for thesis-aware existing positions
source_files:
  - index.md
  - wiki/entities/CEG.md
  - raw/financials/CEG_fundamentals.md
  - raw/imports/CEG_latest_results_source.md
  - wiki/analysis/valuations/CEG DCF Valuation 2026-05-31.md
tags:
  - analysis/decision-memo
  - ticker/CEG
---

# CEG Decision Memo - 2026-05-31
Entity: [[CEG]]

## Action Read

**Action: WAIT / WATCHLIST-new-capital. HOLD only for thesis-aware existing positions.**

CEG เป็น high-quality power-demand / nuclear-scarcity / reliable-capacity story ที่น่าสนใจมากหลัง Calpine. Q1 2026 revenue โต 63.9% YoY เป็น USD 11.122B, Adjusted Operating EPS โตเป็น USD 2.74, management reaffirmed FY2026 Adjusted Operating EPS guidance ที่ USD 11.00-12.00, และ presentation ชี้ไปที่ FCF before growth รวม USD 8.4B ใน 2026-2027.

แต่ new capital ยังไม่ควรไล่ซื้อที่ USD 287.75. Market cap cross-check อยู่ที่ประมาณ USD 104.27B และ net debt ประมาณ USD 21.295B. Base-case DCF จาก FCF-before-growth anchor ให้ fair value ราว USD 194.39 ต่อ diluted share หรือ downside ประมาณ 32.4%. Bull case ไปถึง USD 349.31 แต่ต้องพึ่ง assumptions ที่ค่อนข้างดีมากและ non-GAAP FCF-before-growth ต้องกลายเป็น durable cash จริง.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Fresh market price checked | USD 287.75 at 2026-05-29 close | Twelve Data historical quote page, checked 2026-05-31; market closed Sunday. |
| Market cap | USD 104.27B | 287.75 * 362.359M SEC shares outstanding. |
| Shares outstanding | 362.359M | CEG Q1 2026 Form 10-Q statement of equity. |
| Diluted shares used in DCF | 361M | CEG Q1 2026 presentation expected average diluted shares for FY2026 guidance. |
| Cash, restricted cash, and cash equivalents | USD 1.171B | CEG Q1 2026 Form 10-Q. |
| Total debt used locally | USD 22.466B | Short-term borrowings + current LTD + long-term debt. |
| Net debt | USD 21.295B | 22.466 - 1.171. |
| TTM GAAP-style FCF | USD 1.137B | FY2025 FCF 1.288B - Q1 2025 FCF (0.699B) + Q1 2026 FCF (0.850B). |
| FCF before growth, 2026-2027 average | USD 4.2B per year | 8.4B / 2; non-GAAP. |
| TTM GAAP-style FCF yield | 1.09% | 1.137 / 104.27. |
| FCF-before-growth yield | 4.03% | 4.2 / 104.27. |
| Market EV / FCF before growth | 29.90x | (104.27 + 21.295) / 4.2. |

## Evidence From Vault

| Evidence | Read | Source |
|---|---|---|
| Q1 2026 operating revenues were USD 11.122B | Revenue step-up is large, but Calpine makes YoY comparison not clean organic growth. | `raw/financials/CEG_fundamentals.md` |
| Q1 2026 GAAP EPS was USD 4.49 and Adjusted Operating EPS was USD 2.74 | Earnings power improved versus Q1 2025. | CEG Q1 2026 release. |
| FY2026 Adjusted Operating EPS guidance was affirmed at USD 11.00-12.00 | Management confidence remains intact. | CEG Q1 2026 release / presentation. |
| FCF before growth is guided at USD 8.4B across 2026-2027 | Supports bull case, but is non-GAAP and before growth. | CEG Q1 2026 presentation. |
| Q1 2026 GAAP-style FCF was USD (850)M | Cash conversion is not yet clean under `OCF - capex`. | CEG Q1 2026 Form 10-Q. |
| Net debt was about USD 21.295B | Calpine increases financial leverage and reduces margin for error. | CEG Q1 2026 Form 10-Q. |
| Nuclear generation was 44,666 GWh with 92.3% capacity factor | Core nuclear fleet remains a major reliability asset. | CEG Q1 2026 release. |
| Management cites 55 GW fleet and data-center / large-load optionality | Strategic value is real but depends on policy and contracting economics. | CEG Q1 2026 presentation. |

## Valuation Read

| Scenario | Fair Value / Share | Upside / Downside vs USD 287.75 | Read |
|---|---:|---:|---|
| Bear | USD 102.93 | -64.2% | If FCF before growth does not convert cleanly, downside is severe. |
| Base | USD 194.39 | -32.4% | Good business, but valuation is not cheap enough for new capital. |
| Bull | USD 349.31 | 21.4% | Upside exists if power-demand optionality and FCF conversion both work. |

Reverse DCF read: current price needs roughly 15.8% annual FCF-before-growth growth for five years at 8.5% WACC and 2.5% terminal growth. That is possible if the power supercycle is real, but not a humble base case.

## Bull Case

- CEG owns scarce reliable power assets at a time when data centers, electrification, reshoring, and grid reliability needs are increasing.
- Nuclear fleet and 55 GW post-Calpine platform are hard to replicate.
- Calpine adds dispatchable gas capacity and broader regional reach.
- Management guides to 20%+ Base EPS growth through 2029 and USD 11.5B-13.0B FCF before growth across 2028-2029.
- Large-load / powered-land deals could add earnings upside if regulatory frameworks settle favorably.
- USD 5.0B buyback authorization can help per-share value if cash flow materializes.

## Bear Case

- Valuation already discounts a lot: market EV / FCF before growth is about 29.9x and market EV / TTM GAAP-style FCF is above 100x.
- FCF before growth is not the same as GAAP FCF after capex; Q1 2026 `OCF - capex` was negative.
- Net debt rose materially after Calpine, making execution and cash conversion more important.
- Regulatory outcomes in PJM, ERCOT, nuclear PTC, co-location, and large-load procurement remain uncertain.
- Segment-level FCF and customer-level profitability are not disclosed.
- Commodity prices, weather, outages, collateral, and hedging can make quarterly cash flow volatile.

## Key Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| FCF basis | Scenario DCF uses non-GAAP FCF before growth; sanity check uses GAAP-style FCF | This is the central uncertainty in the valuation. |
| Starting FCF anchor | USD 4.2B, average of 2026-2027 FCF before growth guide | Avoids annualizing Q1 GAAP FCF, but still relies on non-GAAP guidance. |
| Debt treatment | Total debt minus cash / restricted cash | Conservative enough after Calpine leverage step-up. |
| Required margin of safety | High for new capital | Merchant power + regulatory + leverage + FCF definition risk deserve humility. |
| Investor profile | Long-term investor, normal-sized position | No position size, tax basis, or required return was provided. |

## What Would Change The Decision

- Upgrade toward selective ADD if price falls materially or FCF-before-growth yield becomes much more attractive.
- Upgrade if Q2/Q3 2026 show GAAP `OCF - capex` converging toward management's FCF-before-growth narrative.
- Upgrade if large-load / powered-land contracts are disclosed with durable economics and low regulatory leakage.
- Keep WAIT if price stays near current level and FCF disclosure remains mostly non-GAAP.
- Downgrade toward TRIM for oversized positions if price rises further without debt reduction or stronger FCF conversion.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Full FY2026 actual results | not disclosed | Need full-year post-Calpine cash conversion. |
| Official written Q1 2026 call transcript / full Q&A | not verified | Limits view of analyst pushback and management nuance. |
| GAAP reconciliation for forward `Base EPS` and `free cash flow before growth` | not fully disclosed | Core valuation uncertainty. |
| Segment-level operating income and FCF | not disclosed | Cannot isolate nuclear, gas, Calpine, or regional cash engines. |
| Durable post-Calpine run-rate FCF after growth capex | partially disclosed | Determines whether FCF-before-growth is a fair owner-earnings proxy. |
| Product/customer-level data-center and powered-land profitability | not disclosed | Core bull case cannot be modeled by customer economics. |
| Exact future regulatory outcomes | not knowable | Can change contract value, capacity revenue, and cost allocation. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/CEG.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized financial facts | `raw/financials/CEG_fundamentals.md` | Q1 2026 financial facts, FY2025 baseline, market data, cash, debt, FCF, guidance. |
| Latest results source note | `raw/imports/CEG_latest_results_source.md` | Source map and extracted facts. |
| DCF valuation memo | `wiki/analysis/valuations/CEG DCF Valuation 2026-05-31.md` | Source-backed scenario DCF and sensitivity. |
| CEG Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1868275/000186827526000067/ceg-20260331.htm | Primary filing source. |
| CEG Q1 2026 release / presentation | https://investors.constellationenergy.com/static-files/9dc0168f-5328-42ce-9d66-2c3abe07bff0 | Official results and guidance. |
| CEG Q1 2026 earnings presentation | https://investors.constellationenergy.com/static-files/e5a93793-71b7-453f-a5d3-6a8acb420282 | FCF before growth, Base EPS growth, and capital allocation. |
| CEG FY2025 Form 10-K / annual report | https://investors.constellationenergy.com/static-files/8d46f4dc-04f9-4916-aa5d-e12bd5c45aa7 | FY2025 annual baseline. |
| Twelve Data CEG quote page | https://twelvedata.com/markets/736051/stock/nasdaq/ceg/historical-data | Fresh market price. |
