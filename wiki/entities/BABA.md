---
type: entity
ticker: BABA
company: Alibaba Group Holding Limited
market: NYSE ADS / HKEX
currency: RMB
period_type: quarterly + annual
reporting_scope: March quarter 2026 and fiscal year 2026, period ended 2026-03-31
latest_period: FY2026
latest_period_end: 2026-03-31
latest_total_revenue_rmb_m: 1023670
latest_net_income_rmb_m: 102127
source_gap_count: 6
source_gaps:
  - Full FY2026 Form 20-F was not found in this source pass.
  - Earnings call transcript was not found in this source pass.
  - Segment-level free cash flow is not disclosed.
  - AI product profitability and cloud capex payback period are not disclosed.
  - Quick commerce gross margin and subsidy cadence are not disclosed.
  - Current intraday quote for 2026-06-11 was not verified.
source_notes:
  - raw/imports/BABA_latest_results_source.md
  - raw/imports/BABA_market_quote_2026-06-11.md
normalized_markdown: raw/financials/BABA_fundamentals.md
normalized_json: raw/financials/BABA_fundamentals.json
tags:
  - entity/company
  - ticker/BABA
---

# BABA - Alibaba Group Holding Limited

## Snapshot

| Item | Value |
|---|---|
| Ticker | BABA / 9988 |
| Company | Alibaba Group Holding Limited |
| Market | NYSE ADS / HKEX |
| Reporting currency | RMB |
| Latest verified period | FY2026, year ended 2026-03-31 |
| Latest annual revenue | RMB 1,023,670 million |
| Latest annual net income | RMB 102,127 million |
| Latest annual non-GAAP net income | RMB 60,658 million |
| Latest annual free cash flow | RMB (46,609) million |
| Latest available ADR close | USD 115.38 on 2026-06-10 |
| Normalized file | [[BABA_fundamentals]] |
| Latest source note | [[BABA_latest_results_source]] |
| Market quote note | [[BABA_market_quote_2026-06-11]] |
| Latest decision memo | [[BABA Decision Memo 2026-06-11]] |

Alibaba เป็น China commerce + cloud + international commerce platform ที่กำลังเปลี่ยนจาก story แบบ mature e-commerce cash cow ไปเป็น AI/cloud and quick-commerce reinvestment story. ราคาหุ้นลงแรงเพราะตลาดไม่ได้กังวลแค่ headline revenue แต่กังวลว่า profit และ FCF ถูกกดหนักแค่ไหนก่อน investment cycle จะคืนเงินสดกลับมา.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | Official company filings / IR | Found | Alibaba IR page and official March Quarter 2026 / FY2026 results release. |
| 2 | Earnings transcript / call material | Gap | ไม่พบข้อมูลที่ยืนยันได้ in this source pass. |
| 3 | Financial statements / metrics | Found | Official results release includes income statement, cash flow, balance sheet, segment revenue, segment adjusted EBITA, dividend. |
| 4 | News / market data | Used as context | MarketWatch for latest close/drawdown; Barron's for lower-priority context on investor concerns. |

## Business Model

| Business line | Revenue mechanism | Durable driver | Primary source |
|---|---|---|---|
| Alibaba China E-commerce Group | Customer management, direct sales/logistics, quick commerce, wholesale | Merchant spend, take rate, 88VIP retention, Taobao/Tmall engagement, quick-commerce order density | Official FY2026 results release. |
| Alibaba International Digital Commerce Group | International retail and wholesale commerce | AliExpress, Lazada, Trendyol, cross-border supply chain, logistics efficiency | Official FY2026 results release. |
| Cloud Intelligence Group | Cloud infrastructure, public cloud, AI-related products, model services | AI demand, external cloud revenue growth, Qwen/MaaS adoption, compute supply | Official FY2026 results release. |
| All others | Freshippo, Cainiao, Alibaba Health, Amap, Qwen Consumer Business Group, DingTalk, media and other businesses | Portfolio rationalization, operating discipline, logistics and local services scale | Official FY2026 results release. |

## Segments / Revenue Mix

### FY2026 Segment Revenue And Adjusted EBITA

| Segment | Revenue | Share of consolidated revenue | Adjusted EBITA | Source |
|---|---:|---:|---:|---|
| Alibaba China E-commerce Group | 554,217 | 54.14% | 107,509 | Official results PDF. |
| Alibaba International Digital Commerce Group | 144,170 | 14.08% | (2,051) | Official results PDF. |
| Cloud Intelligence Group | 158,132 | 15.45% | 14,265 | Official results PDF. |
| All others | 254,367 | 24.85% | (35,737) | Official results PDF. |
| Inter-segment elimination and unallocated | (87,216) net | N/A | (7,570) net | Official results PDF. |

### Segment Read

China E-commerce ยังเป็น profit engine หลัก แต่ FY2026 adjusted EBITA ลด 44% YoY เพราะ quick commerce, user experience, and technology investment. Cloud เป็น bright spot: FY2026 revenue โต 34% และ March quarter revenue โต 38%, แต่ขนาดกำไรยังไม่พอชดเชย pressure จาก China e-commerce investment และ All others losses.

## Financial Facts

| Metric | FY2025 | FY2026 | Read |
|---|---:|---:|---|
| Revenue | 996,347 | 1,023,670 | Headline growth เพียง 3%; like-for-like excluding divestitures โต 11%. |
| Income from operations | 140,905 | 50,150 | Profit compression ชัดเจน. |
| Adjusted EBITA | 173,065 | 76,416 | ลด 56% YoY จาก investment cycle. |
| Non-GAAP net income | 158,122 | 60,658 | ลด 62% YoY. |
| Operating cash flow | 163,509 | 76,213 | Cash conversion อ่อนลงมาก. |
| Free cash flow | 73,870 | (46,609) | FCF ติดลบจาก quick commerce และ cloud infrastructure. |
| Cash and other liquid investments | 597,132 | 520,824 | Balance sheet ยังใหญ่ แต่ cash pile ลดลง. |

## Charts

Charts live in [[BABA_fundamentals]] and use only verified official values.

## Transcript / Management Commentary

| Topic | Commentary / fact | Investment read |
|---|---|---|
| AI + Cloud | Cloud revenue grew 38% in March quarter 2026, and external customer revenue grew 40%. | จุดแข็งจริง แต่ต้องพิสูจน์ว่ากำไรและ FCF จะตามมา. |
| AI-related products | AI-related product revenue reached RMB8,971 million and had triple-digit YoY growth for the eleventh consecutive quarter. | มี growth signal ที่น่าสนใจ แต่ profitability / capex payback ยังไม่ disclosed. |
| Quick commerce | March quarter quick commerce revenue grew 57%; management said unit economics and average order value improved QoQ. | Revenue traction ดี แต่ตลาดยังกลัว subsidy / competition drag. |
| FCF pressure | FY2026 FCF outflow was RMB46,609 million. | นี่คือเหตุผลหลักที่ stock ถูก de-rate. |
| Dividend | Annual dividend US$1.05 per ADS approved. | Capital return มี แต่ yield ยังต่ำมากเมื่อเทียบกับ thesis risk. |

## Thesis

### Bull Case

- ราคา BABA ลงมาใกล้จุดที่ตลาดเริ่ม discount ความเสี่ยงหนักขึ้น: ล่าสุดปิด USD 115.38 หรือ 40.12% ต่ำกว่า 52-week high.
- Balance sheet ยังแข็งแรง: cash and other liquid investments USD 75.504B เทียบกับ interest-bearing debt ประมาณ USD 37.692B.
- Cloud Intelligence เป็น growth engine ที่ verify ได้: FY2026 revenue โต 34%, March quarter โต 38%, external cloud revenue โต 40%.
- AI-related product revenue โต triple-digit ต่อเนื่อง และ Qwen ถูก integrate เข้ากับ commerce ecosystem.
- ถ้า quick commerce losses peak แล้ว, China e-commerce profit engine สามารถฟื้น operating leverage ได้.
- AIDC loss ใกล้ break-even ใน March quarter, ซึ่งช่วยลด drag ถ้าดำเนินต่อได้.

### Bear Case

- FY2026 FCF ติดลบ RMB46.609B จากบวก RMB73.870B ใน FY2025; นี่ไม่ใช่แค่ accounting issue.
- Adjusted EBITA ลด 56% YoY และ non-GAAP net income ลด 62% YoY ขณะที่ revenue โตเพียง 3%.
- Quick commerce และ China internet competition อาจเป็น price war ที่กินเวลานานกว่าที่ตลาดอยากเห็น.
- Cloud/AI ต้องใช้ capex สูงมาก: FY2026 capex RMB126.063B และ March quarter capex RMB26.887B.
- All others adjusted EBITA loss กว้างขึ้นมากเป็น RMB35.737B ใน FY2026.
- China / ADR / geopolitics risk ยังทำให้ multiple discount ต่อ U.S. megacap tech สมเหตุสมผลบางส่วน.

### Base View

ผมมอง BABA เป็น **WATCHLIST / not yet automatic buy** หลังราคาลงแรง. ราคาลงทำให้ risk/reward น่าสนใจกว่าเดิม แต่ยังไม่พอให้สรุปว่า “ถูกมาก” เพราะ FY2026 earnings base และ FCF base ถูกกดหนักมาก. สำหรับ new capital ต้องรออย่างน้อยหนึ่งในสองอย่าง: ราคาถูกลงจนชดเชย FCF uncertainty ชัดเจน หรือ official results ถัดไปแสดงว่า FCF trough ผ่านไปแล้ว.

## Risks

- FCF outflow persists because AI/cloud capex and quick commerce subsidy stay elevated.
- China e-commerce take rate recovery fails to offset competition from JD, PDD/Temu, Meituan, and local services platforms.
- Cloud revenue grows but margin does not scale due to compute cost, chip constraints, or pricing pressure.
- Regulatory / geopolitics / ADR risk keeps valuation multiple discounted.
- Portfolio businesses under All others continue to consume capital or require impairments.

## Catalysts

- Next official quarterly results showing narrowing quick-commerce losses and positive consolidated FCF.
- Cloud revenue growth remains above 30% while Cloud adjusted EBITA expands.
- More disclosure on AI-related product revenue, margins, and capex payback.
- AIDC reaches sustained break-even.
- Buyback or capital return acceleration after FCF normalizes.
- Geopolitical de-risking or ADR risk reduction.

## Valuation Watch Items

| Watch item | Current read |
|---|---|
| Latest close | USD 115.38 on 2026-06-10. |
| Drawdown | 40.12% below USD 192.67 52-week high. |
| Implied market cap | USD 277.417B using diluted ADS equivalent. |
| Implied enterprise value | USD 239.605B after company-defined liquid investments and interest-bearing debt. |
| Price / FY2026 non-GAAP net income | 31.5x. |
| EV / FY2026 adjusted EBITA | 21.6x. |
| EV / FY2026 revenue | 1.6x. |
| FCF multiple | Not meaningful on FY2026 FCF because FCF was negative. |

## Reports / Source Notes

- [[BABA_latest_results_source]]
- [[BABA_market_quote_2026-06-11]]
- [[BABA_fundamentals]]
- [[BABA Decision Memo 2026-06-11]]

## Follow-Up

- Find FY2026 Form 20-F when filed and reconcile annual release fields.
- Find official earnings transcript or call replay transcript if available.
- Refresh after next quarterly result to check whether FCF outflow narrows.
- Build a DCF only after we can underwrite normalized FCF or management provides clearer capex / FCF trajectory.

## Missing / Unverified Data

| Item | Status |
|---|---|
| Full FY2026 Form 20-F | ไม่พบข้อมูลที่ยืนยันได้ |
| Earnings call transcript | ไม่พบข้อมูลที่ยืนยันได้ |
| Segment-level free cash flow | Not disclosed |
| AI product profitability and cloud capex payback | Not disclosed |
| Quick commerce gross margin and subsidy cadence | Not disclosed |
| Current intraday quote for 2026-06-11 | ไม่พบข้อมูลที่ยืนยันได้ |
