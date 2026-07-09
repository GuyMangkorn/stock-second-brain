---
type: entity
ticker: SMIC
company: Semiconductor Manufacturing International Corporation
market: SEHK 00981 / SSE STAR 688981
currency: USD / CNY / HKD
period_type: quarterly + annual
reporting_scope: Q1 2026 and FY2025 annual baseline
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 2505.5
latest_net_income_usd_m: 230.9
source_gap_count: 7
source_gaps:
  - Official Q1 2026 earnings call transcript text was not found.
  - FY2026 FCF guidance was not found.
  - FY2026 capex guidance was not found.
  - Market-source shares, market cap, and official diluted shares do not reconcile cleanly.
  - Segment-dollar table was not normalized from disclosed mix.
  - Node-level profitability is not disclosed.
  - Investor-specific position size, cost basis, tax status, and required return were not provided.
source_notes:
  - raw/imports/SMIC_latest_results_source.md
  - raw/imports/SMIC_market_quote_2026-07-09.md
normalized_markdown: raw/financials/SMIC_fundamentals.md
normalized_json:
tags:
  - entity/company
  - ticker/SMIC
---

# SMIC - Semiconductor Manufacturing International Corporation

## Snapshot

| Item | Value |
|---|---|
| Ticker | SMIC |
| Company | Semiconductor Manufacturing International Corporation |
| Market | SEHK `00981`; SSE STAR `688981` |
| Currency | Q1 statements in USD; annual PRC baseline in RMB; quote in HKD |
| Latest period | Q1 2026, three months ended 2026-03-31 |
| Reporting scope | Q1 2026 and FY2025 annual baseline |
| Fresh H-share price | HKD 84.10 at 2026-07-09 15:14:56 GMT+8 |
| Displayed market cap | HKD 996.95B from Google Finance |
| Normalized file | `raw/financials/SMIC_fundamentals.md` |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | Official filings / IR | Complete for Q1 2026 and FY2025 baseline | SMIC IR page, Q1 2026 earnings release, quarterly statement spreadsheets, annual report, and PRC annual spreadsheets used. |
| 2 | Earnings transcript | Missing | Official webcast access found; no official transcript text found. |
| 3 | Financial statements / metrics | Partial but sufficient for P4 | Core statements, cash, borrowings, shares, FCF calculation, and Q2 guidance normalized. |
| 4 | News / web context | Not used | Decision does not rely on secondary news. |

## Business Model

SMIC เป็น pure-play semiconductor foundry ของจีน ให้บริการผลิต wafer / integrated circuit manufacturing แก่ลูกค้า fabless และระบบ semiconductor ecosystem ในจีนและต่างประเทศ. Thesis หลักโยงกับ China semiconductor localization, domestic capacity expansion, และความสามารถในการรักษา utilization / gross margin ในช่วงที่ capex สูงมาก.

ธุรกิจมี strategic value สูง แต่ economics สำหรับ equity investor ยังหนักด้าน reinvestment: Q1 2026 revenue โต YoY และ guidance Q2 ดีขึ้น แต่ simple FCF ยังติดลบเพราะ capex สูงกว่ากระแสเงินสดจากการดำเนินงาน.

## Segments / Revenue Mix

Q1 2026 release เปิดเผย mix by geography, service type, application, and wafer size แต่ P4 นี้ยังไม่ normalize เป็น segment-dollar table.

| Mix item | Q1 2026 | Q4 2025 | Q1 2025 | Source |
|---|---:|---:|---:|---|
| China revenue mix | 88.9% | 87.6% | 84.3% | SMIC Q1 2026 earnings release. |
| America revenue mix | 9.3% | 10.3% | 12.6% | SMIC Q1 2026 earnings release. |
| Eurasia revenue mix | 1.8% | 2.1% | 3.1% | SMIC Q1 2026 earnings release. |
| Wafers service type mix | 93.9% | 92.4% | 95.2% | SMIC Q1 2026 earnings release. |
| 12-inch wafer mix | 76.4% | 77.2% | 78.1% | SMIC Q1 2026 earnings release. |

## Financial Facts

| Metric | Latest Value | Source / Calculation |
|---|---:|---|
| Q1 2026 revenue | USD 2.5055B | Q1 2026 earnings release / income statement spreadsheet. |
| Q1 2026 gross profit | USD 0.5036B | Q1 2026 earnings release / income statement spreadsheet. |
| Q1 2026 gross margin | 20.1% | Q1 2026 earnings release. |
| Q1 2026 profit from operations | USD 0.2478B | Q1 2026 income statement spreadsheet. |
| Q1 2026 profit for the period | USD 0.2309B | Q1 2026 income statement spreadsheet. |
| Q1 2026 operating cash flow | USD 0.6850B | Q1 2026 cash-flow spreadsheet. |
| Q1 2026 capex spend | USD 1.3121B | Q1 2026 cash-flow spreadsheet; cash outflow converted to positive spend. |
| Q1 2026 simple FCF | USD -0.6271B | 0.6850B - 1.3121B. |
| Cash and cash equivalents | USD 7.2790B | Q1 2026 balance sheet spreadsheet. |
| Debt-like obligations used for watchlist | USD 14.5123B | Borrowings + lease liabilities. |
| Official diluted shares used in EPS | 8.012731B | Q1 2026 income statement spreadsheet. |
| Q2 2026 revenue guidance | +14% to +16% QoQ | Q1 2026 earnings release. |
| Q2 2026 gross-margin guidance | 20% to 22% | Q1 2026 earnings release. |

## Charts

See `raw/financials/SMIC_fundamentals.md` for source-backed chart blocks:

- Quarterly YoY Comparison
- Quarterly Trend
- Annual Trend
- Cash Flow And Capex Chart
- Balance Sheet Snapshot Chart

## Transcript / Management Commentary

- Management said Q1 2026 revenue was USD 2,505 million, up 0.7% sequentially, while gross margin was 20.1%.
- Q2 2026 guidance calls for revenue +14% to +16% QoQ and gross margin of 20% to 22%.
- Management commentary states it was more optimistic about the year than in the prior quarter based on customer demand and orders on hand.
- Official transcript text is missing, so Q&A color is not used in the thesis.

## Thesis

### Bull Case

SMIC เป็น strategic foundry platform ของจีน และ Q1 2026 evidence ชี้ว่า demand / order book ดีขึ้นพอที่ management guide Q2 revenue +14% to +16% QoQ. China revenue mix 88.9% และ localization theme อาจช่วย utilization / pricing resilience หาก domestic semiconductor demand แข็งแรงต่อเนื่อง. Cash balance USD 7.279B ช่วยรองรับ expansion cycle บางส่วน.

### Bear Case

FCF quality ยังเป็นจุดอ่อนชัดเจน. Q1 2026 simple FCF ติดลบ USD 627M แม้ OCF เป็นบวก เพราะ capex spend USD 1.312B. FY2025 annual simple FCF ก็ติดลบ RMB 39.87B. Debt-like obligations เพิ่มเป็น USD 14.512B และ market quote แสดง P/E 118.83x ที่ราคาสด HKD 84.10. เมื่อไม่มี FY2026 FCF guidance และ share/market-cap reconciliation ยังขัดกัน การทำ DCF ต่อ share แบบแม่นยำจะให้ความแน่นอนปลอม.

### Key Debate

Debate หลักคือ SMIC จะ convert strategic demand และ capacity expansion เป็น durable FCF ได้เมื่อไหร่. ถ้า gross margin อยู่ 20%-22% แต่ capex ยังสูงมาก equity value อาจขึ้นกับ sentiment / policy / localization มากกว่ากระแสเงินสดปัจจุบัน.

## Risks

- Negative simple FCF from heavy capex.
- Debt-like obligations rising faster than cash in the latest balance sheet snapshot.
- US / geopolitical export restrictions and technology access risk.
- Utilization / pricing risk if capacity expansion outruns demand.
- Share-count and market-cap reconciliation gap across dual listing / market-data source.
- Official transcript unavailable, limiting Q&A-level visibility.

## Catalysts

- Q2 2026 result confirming revenue +14% to +16% QoQ and 20%-22% gross margin.
- Evidence that utilization remains high while capex intensity starts to ease.
- Clear official FY2026 capex / cash-flow guidance.
- Reconciled total share count across H shares and A shares for valuation work.
- Any official disclosure improving visibility into advanced-node demand or capacity economics.

## Valuation Watch Items

- P11 created a valuation-gap memo, not a point-estimate DCF.
- Fresh quote: HKD 84.10; displayed market cap: HKD 996.95B; source timestamp 2026-07-09 15:14:56 GMT+8.
- Market data conflict: Google displayed shares outstanding 5.04B, official diluted EPS shares 8.012731B, and implied shares from market cap / price 11.85B.
- Re-run valuation only after share-count reconciliation and either positive normalized FCF or official FY2026 FCF/capex guidance.

## Reports / Source Notes

- [[SMIC_latest_results_source]]
- [[SMIC_market_quote_2026-07-09]]
- [[SMIC_fundamentals]]
- [[SMIC DCF Valuation 2026-07-09]]
- [[SMIC Decision Memo 2026-07-09]]

## Follow-Up

- Find official transcript text or webcast transcript if published later.
- Reconcile H-share, A-share, total ordinary share count, and market cap.
- Refresh price before any future action call.
- Track Q2 2026 revenue/gross margin delivery versus guidance.
- Look for official FY2026 capex and cash-flow guidance.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Official Q1 2026 earnings call transcript text | ไม่พบข้อมูลที่ยืนยันได้ | Official webcast access found but no transcript text found. |
| FY2026 FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Required before a cleaner DCF anchor. |
| FY2026 capex guidance | ไม่พบข้อมูลที่ยืนยันได้ | Q1 capex was disclosed only. |
| Reconciled total share count / market cap | ไม่พบข้อมูลที่ยืนยันได้ | Google market cap, Google shares, and official diluted shares conflict. |
| Node-level profitability | not disclosed | Important for advanced-node economics but not source-backed. |
| Investor-specific constraints | not provided | No personalized sizing or tax/cost-basis action call. |
