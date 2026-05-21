---
type: entity
ticker: GEV
company: GE Vernova Inc.
market: NYSE
currency: USD
period_type: quarterly + annual
reporting_scope: Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 9339
latest_net_income_usd_m: 4745
source_gap_count: 8
source_gaps:
  - Full FY2026 actual results are not disclosed.
  - GAAP reconciliation for forward non-GAAP FCF / adjusted EBITDA margin guidance is not disclosed.
  - Segment-level FCF is not disclosed.
  - Wind project-level loss reserve and contract profitability is not disclosed.
  - Customer down-payment / slot-reservation conversion and cancellation terms are not disclosed.
  - Prolec GE full post-integration run-rate profitability is only partially disclosed.
  - Product-level data-center / gas turbine / grid equipment profitability is not disclosed.
  - Investor-specific cost basis, position size, tax status, and required return were not provided.
source_notes:
  - raw/imports/GEV_latest_results_source.md
normalized_markdown: raw/financials/GEV_fundamentals.md
normalized_json: raw/financials/GEV_fundamentals.json
tags:
  - entity/company
  - ticker/GEV
---

# GEV - GE Vernova Inc.

## Snapshot

| Item | Value |
|---|---|
| Ticker | GEV |
| Company | GE Vernova Inc. |
| Market | NYSE |
| Currency | USD |
| Latest period | Q1 2026, quarter ended 2026-03-31 |
| Reporting scope | Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline |
| Normalized file | `raw/financials/GEV_fundamentals.md` |
| Latest price check | USD 1,024.52 on 2026-05-21; market cap USD 275.31B |
| Current action read | WAIT / AVOID-new-capital; HOLD only if already owned and thesis-aware |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Available | Q1 2026 Form 10-Q and FY2025 annual report reviewed. |
| 1 | Official company results | Available | Q1 2026 earnings release / presentation used for segment data, FCF reconciliation, and guidance. |
| 2 | Earnings transcript / call material | Available | Company-hosted LSEG Q1 2026 transcript reviewed for commentary; no unsupported numbers normalized from it. |
| 3 | Financial statements / metrics | Available | Investing.com used only for fresh market-data check; official SEC share count takes priority. |
| 4 | News / web context | Limited | Not needed for core financial facts in this pass. |

## Business Model

GE Vernova เป็น energy transition / electrification infrastructure company ที่แยกออกจาก General Electric โดยมีสาม segment หลัก: `Power`, `Wind`, และ `Electrification`. Business mix ครอบคลุม gas turbines, services, steam, nuclear, onshore/offshore wind, grid equipment, power conversion, electrification software, and related services.

Quality ของ business มาจาก installed base, grid / power demand, electrification capex, data-center load growth, and long-cycle backlog. แต่ risk profile ยังไม่เหมือน pure software compounder เพราะ margin cycle, project execution, Wind losses, supply chain, customer down payments, and working-capital timing สำคัญมากต่อ cash flow.

## Segments / Revenue Mix

| Segment | Q1 2026 Revenue | Q1 2026 Mix of revenue | Q1 2026 YoY | Q1 2026 EBITDA | Q1 2026 EBITDA Margin | Source |
|---|---:|---:|---:|---:|---:|---|
| Power | USD 4.971B | 53.2% | 11.7% | USD 0.811B | 16.3% | GE Vernova Q1 2026 release. |
| Electrification | USD 2.959B | 31.7% | 60.8% | USD 0.528B | 17.8% | GE Vernova Q1 2026 release. |
| Wind | USD 1.432B | 15.3% | -22.6% | USD (0.382B) | (26.7)% | GE Vernova Q1 2026 release. |

Power คือ cash / earnings anchor ตอนนี้ ขณะที่ Electrification เป็น growth engine ที่ margin ดีขึ้น และ Wind เป็น turnaround risk ที่ยัง drag consolidated profitability. Q1 2026 orders โตเด่นใน Power และ Electrification แต่ Wind EBITDA ยังติดลบหนัก.

## Financial Facts

| Metric | Latest value | Source |
|---|---:|---|
| Q1 2026 revenue | USD 9.339B | GE Vernova Q1 2026 Form 10-Q. |
| Q1 2026 net income attributable to GEV | USD 4.745B | GE Vernova Q1 2026 Form 10-Q; includes M&A gains primarily from Prolec GE. |
| Q1 2026 adjusted EBITDA / margin | USD 896M / 9.6% | GE Vernova Q1 2026 release; non-GAAP. |
| Q1 2026 diluted EPS | USD 17.44 | GE Vernova Q1 2026 Form 10-Q. |
| Q1 2026 FCF | USD 4.791B | GE Vernova Q1 2026 release; non-GAAP. |
| FY2025 FCF | USD 3.710B | GE Vernova FY2025 annual report; non-GAAP. |
| TTM FCF | USD 7.526B | FY2025 FCF - Q1 2025 FCF + Q1 2026 FCF. |
| Cash, cash equivalents, and restricted cash | USD 10.172B | GE Vernova Q1 2026 Form 10-Q. |
| Total borrowings and finance leases | USD 2.857B | GE Vernova Q1 2026 Form 10-Q. |
| Net cash | USD 7.315B | Cash minus total borrowings and finance leases. |
| FY2026 revenue guidance | USD 44.5B to USD 45.5B | GE Vernova Q1 2026 release. |
| FY2026 FCF guidance | USD 6.5B to USD 7.5B | GE Vernova Q1 2026 release; non-GAAP. |

## Charts

See `raw/financials/GEV_fundamentals.md` for source-backed quarterly YoY, annual, segment revenue, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

Management tone was bullish on demand and more constructive on 2026 than the prior guide. The company raised 2026 adjusted EBITDA and FCF guidance, with Power and Electrification driving the upgrade. The key positive signal is not just Q1 revenue growth, but backlog and orders: Q1 orders were USD 18.3B and backlog / RPO reached about USD 163B.

The caveat is cash-flow quality. Q1 2026 FCF was very strong, but management commentary and source facts point to customer down payments / slot reservation agreements and working-capital timing. That makes the cash flow source-backed, but not something to annualize blindly.

## Thesis

### Bull Case

GEV sits directly in the power demand / grid bottleneck debate. If data centers, AI compute, electrification, industrial reshoring, and grid modernization keep driving orders, Power and Electrification can compound for longer than a normal industrial cycle. Q1 2026 orders of USD 18.3B, backlog / RPO around USD 163B, and guidance raise support the idea that demand is real and not only a one-quarter burst.

Power has service economics and installed base support, while Electrification has strong growth and margin expansion potential. If Wind losses narrow without new project surprises, consolidated EBITDA margin can move higher and FCF could stay well above the pre-spin baseline.

### Bear Case

Valuation is the main problem. At USD 1,024.52 and market cap about USD 275.31B, the stock trades at roughly 2.54% forward guided FCF yield using FY2026 FCF guidance midpoint. Base DCF gives fair value around USD 587.37 per diluted share, meaning current price already prices in a lot of success.

Wind is still materially loss-making, project execution can surprise, and Q1 FCF benefited from working capital / down payments. If those cash inflows reverse, if Wind takes longer to repair, or if the market compresses premium power-infrastructure multiples, downside can be meaningful even if the business remains strategically attractive.

### Key Debate

คำถามหลักคือ GEV เป็น power-infrastructure compounder ที่ควรได้ premium multiple ระยะยาวแค่ไหน. Business momentum ดีมาก แต่ current price ต้องการทั้ง Power demand, Electrification growth, Wind turnaround, and FCF conversion ที่เกือบ flawless. ถ้า thesis ถูกแต่ timing หรือ valuation ผิด นักลงทุนใหม่ยังอาจได้ return ไม่ดี.

## Risks

- Valuation risk: forward guided FCF yield around 2.54% and market EV / TTM FCF around 35.6x.
- Wind execution risk from offshore losses, onshore restructuring, warranty / contract risk, and margin recovery timing.
- Cash-flow timing risk because Q1 FCF benefited from customer down payments and slot reservation agreements.
- Power and grid cycle risk from project timing, customer financing, permitting, supply chain, and equipment bottlenecks.
- Margin risk from inflation, tariffs, mix, restructuring, and growth investment.
- Integration / acquisition risk from Prolec GE and any future capacity expansion.
- Source gap risk: segment-level FCF and product-level economics are not disclosed.

## Catalysts

- Q2 2026 results and whether FCF continues to track toward or above USD 7.0B midpoint.
- Additional upward revision to FY2026 adjusted EBITDA margin or FCF guidance.
- Evidence that Wind losses shrink toward the approximately USD 400M FY2026 loss guide without new project charges.
- Continued strong orders in Power and Electrification, especially grid and gas power demand.
- More disclosure on backlog conversion, customer down payments, slot reservations, and cancellation terms.
- Price pullback that lifts forward FCF yield toward a more attractive margin of safety.

## Valuation Watch Items

- Current DCF memo: [[GEV DCF Valuation 2026-05-21]].
- Base-case fair value from P11 is approximately USD 587.37 per diluted share versus USD 1,024.52 fresh price check.
- Bull case reaches about USD 930.06, still below the current price.
- Watch whether FY2026 FCF can exceed USD 7.5B sustainably without relying on one-time working-capital inflows.
- Re-run valuation after Q2 2026 results, updated Wind loss trajectory, and any guidance change.

## Reports / Source Notes

| Note | Type |
|---|---|
| [[GEV_latest_results_source]] | Latest results source note |
| [[GEV_fundamentals]] | Normalized financial facts |
| [[GEV DCF Valuation 2026-05-21]] | DCF valuation |
| [[GEV Decision Memo 2026-05-21]] | Decision memo |

## Follow-Up

- Refresh after Q2 2026 results with revenue, segment orders, backlog, adjusted EBITDA, Wind losses, OCF, capex, FCF, cash, debt, shares, and updated guidance.
- Track whether down payments and slot reservations convert into revenue / projects without future cash-flow reversal.
- Monitor Wind loss path versus the approximately USD 400M FY2026 segment EBITDA loss guide.
- Recheck current price before any action change.
- If disclosure improves, split FCF quality into recurring operating conversion versus customer advances / working-capital timing.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Full FY2026 actual results | not disclosed | Q1 2026 is the latest official period found. |
| GAAP reconciliation for forward non-GAAP FCF / adjusted EBITDA margin guidance | not disclosed | Forward guidance uses company non-GAAP definitions. |
| Segment-level FCF | not disclosed | FCF is disclosed at company level. |
| Wind project-level loss reserve and contract profitability | not disclosed | Important to assess turnaround durability. |
| Customer down-payment / slot-reservation conversion and cancellation terms | not disclosed | Important because Q1 FCF is not safe to annualize. |
| Prolec GE full post-integration run-rate profitability | partially disclosed | Full normalized contribution was not isolated. |
| Product-level data-center / gas turbine / grid equipment profitability | not disclosed | Segment-level data does not isolate product economics. |
| Investor-specific tax basis, position size, and required return | not provided | Needed for personalized sizing. |
