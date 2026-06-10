---
type: entity
ticker: AAPL
company: Apple Inc.
market: Nasdaq
currency: USD
period_type: quarterly + annual
reporting_scope: FY2025 annual baseline plus Q2 FY2026 quarter and six months ended 2026-03-28
latest_period: Q2 FY2026
latest_period_end: 2026-03-28
latest_total_revenue_usd_m: 111184
latest_net_income_usd_m: 29578
source_gap_count: 8
source_gaps:
  - Official Apple investor-relations Q2 FY2026 press release page was not verified in this pass.
  - Official earnings-call transcript was not verified in this pass.
  - Forward revenue, EPS, gross margin, capex, or FCF guidance was not disclosed in the verified official source set.
  - Product unit volumes and product-level margins below Products / Services are not disclosed.
  - Segment-level FCF by product or geography is not disclosed.
  - AI-specific revenue or Apple Intelligence monetization is not disclosed.
  - Q2 standalone operating cash flow and capex are not disclosed in the extracted official table.
  - Investor-specific position size, tax basis, and required return were not provided.
source_notes:
  - raw/imports/AAPL_latest_results_source.md
  - raw/imports/AAPL_market_quote_2026-06-11.md
normalized_markdown: raw/financials/AAPL_fundamentals.md
normalized_json: raw/financials/AAPL_fundamentals.json
tags:
  - entity/company
  - ticker/AAPL
---

# AAPL - Apple Inc.

## Snapshot

| Item | Value |
|---|---|
| Ticker | AAPL |
| Company | Apple Inc. |
| Market | Nasdaq |
| Currency | USD |
| Latest verified period | Q2 FY2026, quarter ended 2026-03-28 |
| Annual baseline | FY2025, year ended 2025-09-27 |
| Latest quarterly revenue | USD 111,184 million |
| Latest quarterly net income | USD 29,578 million |
| Latest quarterly operating income | USD 35,885 million |
| TTM free cash flow | USD 129,174 million |
| Fresh price check | USD 292.15 on 2026-06-10 1:01 PM EDT |
| Normalized file | [[AAPL_fundamentals]] |
| Latest source note | [[AAPL_latest_results_source]] |
| Market quote note | [[AAPL_market_quote_2026-06-11]] |
| Latest valuation memo | [[AAPL DCF Valuation 2026-06-11]] |
| Bullish valuation scenario | [[AAPL Bullish Valuation Scenario 2026-06-11]] |
| Latest decision memo | [[AAPL Decision Memo 2026-06-11]] |

Apple เป็น consumer technology ecosystem ที่รายได้ยังพึ่ง iPhone สูง แต่คุณภาพของ model ดีขึ้นจาก Services gross margin ที่สูงมาก, installed base, App Store/cloud/advertising economics, และ capital return ขนาดใหญ่. ประเด็นหลักตอนนี้ไม่ใช่ business quality แต่คือ valuation ที่แพงเมื่อเทียบกับ FCF ที่ verify ได้.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | Q2 FY2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/320193/000032019326000013/aapl-20260328.htm. FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm. |
| 2 | Earnings release / call materials | Partial / gap | Official Apple newsroom Q2 FY2026 press release and official transcript were not verified in this pass. |
| 3 | Financial statements / metrics | Found | SEC filings plus StockAnalysis market-data pages used for quote and standardized cross-checks. |
| 4 | News / web context | Not used | No secondary news was needed for durable company facts. |

## Business Model

| Business line | Revenue mechanism | Durable driver | Primary official source |
|---|---|---|---|
| iPhone | Hardware sales through direct and indirect channels | Upgrade cycle, Pro mix, carrier/channel demand, ecosystem lock-in | SEC Q2 FY2026 Form 10-Q. |
| Mac / iPad | Hardware sales | Product refresh cycles, Apple silicon, education/enterprise demand | SEC Q2 FY2026 Form 10-Q. |
| Wearables, Home and Accessories | Hardware and accessories | Watch, AirPods, Vision, accessories attach rate | SEC Q2 FY2026 Form 10-Q. |
| Services | App Store, advertising, cloud services, AppleCare, subscriptions, payment and content services | Installed base, payment rails, App Store economics, recurring service attach | SEC Q2 FY2026 Form 10-Q and FY2025 Form 10-K. |

### What Makes The Model Work

- iPhone remains the core revenue driver: Q2 FY2026 iPhone revenue was USD 56.994B, up 22% YoY.
- Services adds high-margin durability: Q2 FY2026 Services revenue was USD 30.976B and Services gross margin was 76.7%.
- Apple generated USD 129.174B of TTM FCF through Q2 FY2026 using official-source calculations.
- Balance sheet has USD 146.595B of cash and marketable securities versus USD 84.711B total debt.
- Capital return remains meaningful: Apple disclosed remaining authorization under the prior repurchase program and an additional USD 100B authorization after quarter-end.

## Segments / Revenue Mix

### Q2 FY2026 Product Mix

| Product / service | Q2 FY2026 Revenue | Share of Q2 FY2026 Revenue | YoY Change | Source |
|---|---:|---:|---:|---|
| iPhone | 56,994 | 51.26% | 22% | SEC Q2 FY2026 Form 10-Q. |
| Mac | 8,399 | 7.55% | 6% | SEC Q2 FY2026 Form 10-Q. |
| iPad | 6,914 | 6.22% | 8% | SEC Q2 FY2026 Form 10-Q. |
| Wearables, Home and Accessories | 7,901 | 7.11% | 5% | SEC Q2 FY2026 Form 10-Q. |
| Services | 30,976 | 27.86% | 16% | SEC Q2 FY2026 Form 10-Q. |
| Total | 111,184 | 100.00% | 17% | SEC Q2 FY2026 Form 10-Q. |

### Revenue Mix Read

Q2 FY2026 เป็น quarter ที่แข็งแรงมาก: iPhone Pro mix ช่วยดัน product revenue และ Services ยังโต double digit. แต่ Apple ยังเป็น hardware-led ecosystem มากกว่า pure recurring software company ดังนั้น valuation ต้องเผื่อ product-cycle risk, component-cost risk, tariff risk, และ AI monetization ที่ยังไม่ disclosed.

## Financial Facts

### Latest Quarterly Facts

| Metric | Q2 FY2026 | Q2 FY2025 | Source |
|---|---:|---:|---|
| Total net sales | 111,184 | 95,359 | SEC Q2 FY2026 Form 10-Q. |
| Gross margin | 54,781 | 44,867 | SEC Q2 FY2026 Form 10-Q. |
| Operating income | 35,885 | 29,589 | SEC Q2 FY2026 Form 10-Q. |
| Net income | 29,578 | 24,780 | SEC Q2 FY2026 Form 10-Q. |
| Diluted EPS | 2.01 | 1.65 | SEC Q2 FY2026 Form 10-Q. |
| Weighted-average diluted shares | 14,725.873M | 15,056.133M | SEC Q2 FY2026 Form 10-Q. |

### Balance Sheet Facts

| Metric | 2026-03-28 | Source |
|---|---:|---|
| Cash and cash equivalents | 45,572 | SEC Q2 FY2026 Form 10-Q. |
| Current marketable securities | 22,935 | SEC Q2 FY2026 Form 10-Q. |
| Non-current marketable securities | 78,088 | SEC Q2 FY2026 Form 10-Q. |
| Cash, cash equivalents, and marketable securities | 146,595 | SEC Q2 FY2026 Form 10-Q. |
| Total debt | 84,711 | Calculated from commercial paper + term debt. |
| Net cash | 61,884 | Calculated from cash/marketable securities - total debt. |
| Shares issued and outstanding | 14.687B | SEC Form 10-Q cover page as of 2026-04-17. |

### Key Ratios

| Ratio | Period / date | Value | Formula |
|---|---|---:|---|
| Revenue growth | Q2 FY2026 YoY | 16.60% | 111,184 / 95,359 - 1 |
| Operating margin | Q2 FY2026 | 32.27% | 35,885 / 111,184 |
| Net profit margin | Q2 FY2026 | 26.60% | 29,578 / 111,184 |
| Gross margin | Q2 FY2026 | 49.27% | 54,781 / 111,184 |
| Services gross margin | Q2 FY2026 | 76.68% | 23,752 / 30,976 |
| TTM FCF margin | TTM Q2 FY2026 | 28.61% | 129,174 / 451,442 |
| Cash and marketable securities / debt | 2026-03-28 | 1.73x | 146,595 / 84,711 |

## Charts

Charts use only verified values from `raw/financials/AAPL_fundamentals.md`.

### Quarterly YoY Comparison

```chart
type: bar
labels: ["Q2 FY2025", "Q2 FY2026"]
series:
  - title: Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [95359, 111184]
  - title: Operating Income
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [29589, 35885]
  - title: Net Income
    backgroundColor: rgba(251, 191, 36, 0.72)
    borderColor: rgba(252, 211, 77, 1)
    data: [24780, 29578]
```

### Product Revenue

```chart
type: bar
labels: ["iPhone", "Mac", "iPad", "Wearables", "Services"]
series:
  - title: Q2 FY2026 Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [56994, 8399, 6914, 7901, 30976]
  - title: Q2 FY2025 Revenue
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [46841, 7949, 6402, 7522, 26645]
```

### Cash Flow And Capex

```chart
type: bar
labels: ["1H FY2025", "1H FY2026", "TTM Q2 FY2026"]
series:
  - title: Operating Cash Flow
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [53887, 82627, 140222]
  - title: Capex Spend
    backgroundColor: rgba(244, 63, 94, 0.64)
    borderColor: rgba(251, 113, 133, 1)
    data: [6011, 4344, 11048]
  - title: Free Cash Flow
    backgroundColor: rgba(251, 191, 36, 0.72)
    borderColor: rgba(252, 211, 77, 1)
    data: [47876, 78283, 129174]
```

## Transcript / Management Commentary

| Topic | Commentary | Investment read |
|---|---|---|
| iPhone | Q2 FY2026 iPhone revenue increased 22% YoY due to higher net sales of Pro models. | Product cycle is strong, but durability depends on refresh cadence and mix. |
| Services | Services revenue increased 16% YoY, driven by advertising, App Store, and cloud services. | Services mix supports margin and recurring quality. |
| Component costs / supply | Apple says supply constraints and increasing costs for advanced semiconductors, NAND, and DRAM could intensify. | Gross margin risk is real despite strong Q2 margin. |
| Tariffs | Apple says tariffs and other measures may affect supply chain, component availability, pricing, gross margin, and results. | Bear-case risk to margins and demand. |
| Capital return | Additional USD 100B repurchase authorization announced after quarter-end; dividend raised to USD 0.27 per share from Q3 FY2026. | Buybacks support per-share growth but can destroy value if done at too-high valuation. |
| Guidance | Forward revenue / EPS / FCF guidance not disclosed in verified official source set. | Valuation must rely on historical FCF and explicit scenario assumptions. |

## Thesis

### Bull Case

- Apple has a rare ecosystem moat: hardware, software, services, developer/payment rails, brand, and installed base reinforce one another.
- Q2 FY2026 growth was broad: total revenue +17% YoY, iPhone +22%, Services +16%, Greater China +28%.
- Services gross margin of 76.7% gives the model a higher-quality profit layer than pure hardware.
- TTM FCF of USD 129.174B gives Apple enormous capital-return capacity.
- Balance sheet remains net cash even after large buybacks.
- If AI features, device refresh, Services, and buybacks keep compounding per-share FCF, Apple can remain a quality compounder.

### Bear Case

- Fresh valuation is demanding: market cap about USD 4.29T and P/FCF about 33x.
- DCF base case using verified TTM FCF and mature-tech assumptions is far below the current price.
- iPhone remains more than half of Q2 FY2026 revenue, so product-cycle risk still matters.
- Apple explicitly flags component-cost/supply pressure and gross-margin volatility/downward pressure.
- Tariffs and international disputes could pressure pricing, demand, and margins.
- AI-specific monetization is not disclosed, so the market may be pricing optionality that cannot yet be verified.

### Key Debate

Can Apple grow FCF per share fast enough from an already huge USD 129B TTM FCF base to justify a 33x P/FCF multiple, or is the stock pricing a level of AI/device-cycle upside that official filings do not yet verify?

## Risks

- iPhone demand or Pro mix normalizes after a strong quarter.
- Services growth slows or faces regulatory pressure around App Store economics, payments, advertising, or platform rules.
- Component costs, memory/NAND/DRAM pricing, or advanced semiconductor supply constraints pressure margins.
- Tariffs and trade disputes hurt supply chain, pricing, demand, or gross margin.
- Buybacks at elevated valuation reduce long-term value creation.
- AI monetization remains unproven while competitors move faster in consumer AI.

## Catalysts

- FY2026 second-half results confirm Q2 strength without margin erosion.
- Services revenue and gross margin continue compounding above product revenue growth.
- Apple discloses clearer AI, device refresh, or Services monetization signals.
- Component/tariff pressure eases or is offset by pricing and mix.
- Share price falls enough to create a margin of safety versus source-backed DCF scenarios.

## Valuation Watch Items

- Fresh price check: USD 292.15 on 2026-06-10 1:01 PM EDT.
- Base DCF fair value from `[[AAPL DCF Valuation 2026-06-11]]`: about USD 153 per diluted share.
- Base-case upside/downside vs fresh price: about (48)%.
- Bull DCF fair value: about USD 229 per diluted share, still below fresh price.
- Bullish scenario addendum from `[[AAPL Bullish Valuation Scenario 2026-06-11]]`: Quality Bull fair value about USD 290 per share, Aggressive Bull about USD 430, and Dream Case about USD 726; the latter two are highly terminal-value-sensitive.
- P/FCF: about 33.0x; EV/FCF: about 32.6x.
- Reverse DCF at 9.0% WACC / 2.5% terminal growth requires about 20.5% 5-year FCF CAGR from TTM Q2 FY2026 FCF, which is a high bar for Apple at this scale.

## Reports / Source Notes

- [[AAPL_latest_results_source]]
- [[AAPL_market_quote_2026-06-11]]
- [[AAPL_fundamentals]]
- [[AAPL DCF Valuation 2026-06-11]]
- [[AAPL Bullish Valuation Scenario 2026-06-11]]
- [[AAPL Decision Memo 2026-06-11]]

## Follow-Up

- Verify official Apple IR / newsroom earnings release and any official call transcript when accessible.
- Recheck current price and market cap before any action.
- Watch FY2026 Q3 for Services growth, iPhone durability, margin pressure, capex, and buyback pace.
- Track any official disclosure on AI monetization, Apple Intelligence adoption, or Services regulatory risk.

## Missing / Unverified Data

| Data item | Status | Handling |
|---|---|---|
| Official Apple investor-relations Q2 FY2026 press release page | ไม่พบข้อมูลที่ยืนยันได้ | Use SEC Form 10-Q as primary official source. |
| Official earnings-call transcript | ไม่พบข้อมูลที่ยืนยันได้ in this pass | Use 10-Q MD&A commentary only. |
| Forward revenue, EPS, gross margin, capex, or FCF guidance | Not disclosed in verified official source set | Use explicit valuation assumptions, not company guidance. |
| Product unit volumes and product-level margins below Products / Services | Not disclosed | Do not infer. |
| Segment-level FCF by product or geography | Not disclosed | Use consolidated FCF only. |
| AI-specific revenue or Apple Intelligence monetization | Not disclosed | Treat as thesis variable. |
| Q2 standalone operating cash flow and capex | Not disclosed in extracted official table | Use 1H and TTM calculations only. |
| Investor-specific position size, tax basis, and required return | Not provided | Decision memo separates new capital from existing position. |
