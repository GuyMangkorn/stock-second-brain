---
type: entity
ticker: UNH
company: UnitedHealth Group Incorporated
market: NYSE
currency: USD
period_type: mixed
reporting_scope: Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 111721
latest_net_income_usd_m: 6280
source_gap_count: 8
source_gaps:
  - FY2026 full-year actual results are not disclosed.
  - FY2026 full-year FCF guidance is not disclosed.
  - Official full Q&A transcript was not normalized.
  - Segment-level FCF is not disclosed.
  - Product / contract-level profitability is not disclosed.
  - Full regulatory / legal exposure quantification is only partially disclosed.
  - End-of-day 2026-05-20 price was not available during workflow.
  - Investor-specific position size, cost basis, tax status, and required return were not provided.
source_notes:
  - raw/imports/UNH_latest_results_source.md
normalized_markdown: raw/financials/UNH_fundamentals.md
normalized_json: raw/financials/UNH_fundamentals.json
tags:
  - entity/company
  - ticker/UNH
---

# UNH - UnitedHealth Group Incorporated

## Snapshot

| Item | Value |
|---|---|
| Ticker | UNH |
| Company | UnitedHealth Group Incorporated |
| Market | NYSE |
| Currency | USD |
| Latest period | Q1 2026 ended 2026-03-31 |
| Reporting scope | Q1 2026 plus FY2025 annual baseline |
| Normalized file | `raw/financials/UNH_fundamentals.md` |
| Latest source note | `raw/imports/UNH_latest_results_source.md` |
| Latest valuation | [[UNH DCF Valuation 2026-05-20]] |
| Latest decision memo | [[UNH Decision Memo 2026-05-20]] |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | Q1 2026 Form 10-Q and FY2025 Form 10-K used for durable facts. |
| 2 | Earnings transcript / call materials | Partial | Official prepared remarks found; official full Q&A transcript not normalized. |
| 3 | Financial statements / metrics | Found | Official release tables plus StockAnalysis / MarketBeat market-data checks. |
| 4 | News / web context | Not used as fact base | No secondary news was needed for durable financial facts. |

## Business Model

UNH เป็น health care and well-being platform ขนาดใหญ่ที่ประกอบด้วยสองแกนหลักคือ UnitedHealthcare และ Optum. UnitedHealthcare รับบทเป็น benefits business สำหรับ employer, individual, Medicare, Medicaid และ public programs ส่วน Optum เป็น services / technology / pharmacy / care delivery platform ที่ทำงานทั้งกับ payer, provider, employer, government, life sciences และ consumer.

โครงสร้าง business model ทำให้ UNH มี revenue base ใหญ่มากและมีหลาย lever: insurance pricing, medical cost management, pharmacy services, care delivery, data / analytics / technology services, and capital allocation. แต่จุดที่ต้องระวังคือ medical cost trend, Medicare Advantage repricing, regulatory scrutiny, PBM pressure, litigation / investigation risk, and execution risk ในการปรับ Optum Health value-based care.

## Segments / Revenue Mix

| Segment | Q1 2026 Revenue | Q1 2026 Earnings from Operations | Notes |
|---|---:|---:|---|
| UnitedHealthcare | USD 86.265B | USD 5.694B | Benefits business; Q1 operating margin 6.6%. |
| Optum Health | USD 24.109B | USD 1.141B | Care delivery / value-based care / health financial services; fewer value-based care members pressured revenue. |
| Optum Insight | USD 5.125B | USD 0.963B | Analytics, technology, consulting, and health financial services. |
| Optum Rx | USD 35.736B | USD 1.192B | Pharmacy care services; scripts down YoY from UHC membership attrition. |
| Total Optum | USD 63.749B | USD 3.296B | Segment revenue includes intersegment activity and eliminations apply at consolidation. |

## Financial Facts

| Fact | Value | Source |
|---|---:|---|
| Q1 2026 total revenues | USD 111.721B | SEC Form 10-Q. |
| Q1 2026 revenue growth | 2.0% YoY | Calculation from SEC Form 10-Q. |
| Q1 2026 earnings from operations | USD 8.990B | SEC Form 10-Q. |
| Q1 2026 net earnings attributable to common shareholders | USD 6.280B | SEC Form 10-Q. |
| Q1 2026 diluted EPS | USD 6.90 | SEC Form 10-Q. |
| Q1 2026 adjusted diluted EPS | USD 7.23 | UnitedHealth Q1 release; non-GAAP. |
| Q1 2026 medical care ratio | 83.9% | SEC Form 10-Q / Q1 release. |
| Q1 2026 operating cash flow | USD 8.912B | SEC Form 10-Q. |
| Q1 2026 FCF | USD 8.149B | Calculation: OCF 8.912B - capex 0.763B. |
| FY2025 FCF | USD 16.075B | Calculation from FY2025 Form 10-K. |
| TTM FCF | USD 19.666B | Calculation from FY2025 and Q1 cash flows. |
| Cash plus short-term investments | USD 31.229B | SEC Form 10-Q calculation. |
| Total debt | USD 77.917B | SEC Form 10-Q calculation. |
| Common shares outstanding | 908,144,404 | SEC Form 10-Q cover page as of 2026-04-30. |
| FY2026 GAAP EPS guidance | Greater than USD 17.35 | UnitedHealth Q1 release. |
| FY2026 adjusted EPS guidance | Greater than USD 18.25 | UnitedHealth Q1 release; non-GAAP. |

## Charts

Charts should use `raw/financials/UNH_fundamentals.md` as source of truth.

### Quarterly YoY Snapshot

| Metric | Q1 2026 | Q1 2025 |
|---|---:|---:|
| Total revenues | 111,721 | 109,575 |
| Earnings from operations | 8,990 | 9,119 |
| Net earnings attributable to common shareholders | 6,280 | 6,292 |
| Free cash flow | 8,149 | 4,558 |

### Annual FCF Baseline

| Period | Operating Cash Flow | Capex Spend | Free Cash Flow |
|---|---:|---:|---:|
| FY2023 | 29,068 | 3,386 | 25,682 |
| FY2024 | 24,204 | 3,499 | 20,705 |
| FY2025 | 19,697 | 3,622 | 16,075 |

## Transcript / Management Commentary

Management commentary จาก official prepared remarks มี signal หลักคือ Q1 2026 ดีกว่า internal plan และ management เชื่อว่า pricing / medical cost alignment เริ่มดีขึ้น. อย่างไรก็ตาม management เตือนว่า Q1 มี seasonal benefit และ earnings cadence ทั้งปี front-half weighted: ประมาณสองในสามของ earnings อยู่ใน H1, โดย UnitedHealthcare และ Optum Health หนักไปทาง H1 มากกว่า segment อื่น.

สิ่งที่น่าจับตา:

- Medical care ratio ดีขึ้นเป็น 83.9% แต่ utilization และ unit cost trend ยัง elevated.
- Operating cost ratio 13.8% สะท้อน investment ใน operations, technology, care delivery, AI, customer experience, cybersecurity และ community engagement.
- Management เร่ง buyback อย่างน้อย USD 2.0B ภายใน Q2 2026 เพราะมองว่าหุ้นมี intrinsic value discount.
- AI modernization เป็นธีมสำคัญ แต่ management ระบุว่า Optum Insight AI-centric opportunity ต้องใช้เวลา later 2026 into 2027.

## Thesis

### Bull Case

UNH ยังเป็น scale leader ใน managed care + health services ecosystem. Q1 2026 แสดงว่า pricing discipline และ medical cost management เริ่มกลับเข้าทาง: revenue โต 2%, MCR ลดลง 90 bps YoY, FCF ดีมากในไตรมาส, และ guidance ถูกยกเป็น adjusted EPS มากกว่า USD 18.25. Balance sheet ยังมี access to capital, investment portfolio ใหญ่, และ management เริ่ม allocate capital ผ่าน buyback เมื่อราคาหุ้นอยู่ต่ำกว่ามุมมอง intrinsic value ของบริษัท.

Optum ยังเป็น long-term optionality ที่สำคัญ. ถ้า Optum Health แก้ value-based care execution ได้, Optum Insight monetizes AI / technology products ดีขึ้น, และ Optum Rx รักษา scale economics ได้, earnings quality อาจ recover ได้มากกว่าที่ market ให้ credit.

### Bear Case

ธุรกิจนี้ยังมีความเสี่ยงไม่ธรรมดา: medical cost trend, Medicare Advantage attrition, PBM / prior authorization scrutiny, regulatory and legal overhang, cyber / data risk, และ public trust risk. Q1 ดูดี แต่ management เองบอกว่า earnings cadence front-half weighted และบาง benefit อาจ moderate. Optum Health revenue ลด YoY และ earnings ลด YoY; Optum Insight / Optum Rx earnings ก็ลด YoY เช่นกัน.

DCF base case ที่ใช้ FY2025 FCF เป็น anchor ยังให้ fair value ต่ำกว่าราคา intraday 2026-05-20 อย่างมีนัยสำคัญ. ดังนั้นหุ้นอาจไม่ถูกพอสำหรับ new capital หาก investor ต้องการ margin of safety ชัดเจน.

### Key Debate

คำถามหลักคือ Q1 2026 เป็น evidence ของ durable margin recovery หรือเป็นแค่ early rebound ที่ front-loaded. ถ้า pricing catches up with medical cost trend และ Optum Health reset สำเร็จ, UNH น่าจะ regain compounder multiple ได้. ถ้า medical costs / regulatory pressure / Optum execution ยังลากต่อ, current price อาจ already discount recovery มากเกินไป.

## Risks

- Medical cost trend และ utilization สูงกว่าราคาที่ตั้งไว้.
- Medicare Advantage membership attrition และ repricing risk.
- Regulatory / legal scrutiny ต่อ Medicare, PBM, prior authorization, claim practices และ data/privacy.
- Optum Health value-based care execution และ contract risk.
- Optum Rx volume pressure จาก UnitedHealthcare membership attrition.
- Cybersecurity and technology execution risk.
- Debt load และ regulated capital constraints อาจจำกัด buyback / acquisition flexibility.
- DCF ใช้ FCF ของ consolidated health insurer / services hybrid จึงควรอ่านเป็น scenario ไม่ใช่ precision valuation.

## Catalysts

- Q2 2026 results เพื่อพิสูจน์ว่ารายได้และ medical cost trend ไม่ได้ดีแค่ Q1.
- Settlement of at least USD 2.0B buyback by end of Q2 2026.
- Progress toward debt-to-capital target around 40% in back half 2026.
- Evidence that Optum Health margins recover without relying on one-time reserve / restructuring effects.
- New AI-first Optum Insight products gaining commercial traction.
- Updated guidance or FCF disclosure.

## Valuation Watch Items

- Latest price check: StockAnalysis USD 385.99 at 2026-05-20 11:50 AM EDT; MarketBeat cross-check USD 383.69 at 12:12 PM Eastern.
- Base DCF fair value: about USD 258 per diluted share, using FY2025 FCF anchor, 9.0% WACC, and 2.5% terminal growth.
- Bull DCF fair value: about USD 459 per diluted share, using TTM FCF and stronger recovery assumptions.
- TTM FCF yield: about 5.6% on StockAnalysis market cap.
- Market EV / TTM FCF: about 20.4x.
- Watch whether FY2026 FCF converges toward Q1 TTM strength or remains closer to FY2025 depressed FCF.

## Reports / Source Notes

- `raw/imports/UNH_latest_results_source.md`
- `raw/financials/UNH_fundamentals.md`
- `raw/financials/UNH_fundamentals.json`
- [[UNH DCF Valuation 2026-05-20]]
- [[UNH Decision Memo 2026-05-20]]

## Follow-Up

- Refresh after Q2 2026 results for MCR, operating cost ratio, Optum Health margin, Optum Rx scripts, UHC membership, OCF, capex, cash, debt, shares, buyback completion, and guidance.
- Search for company-hosted full Q&A transcript if it becomes available.
- Update DCF if FY2026 FCF guidance or clearer normalized FCF commentary is disclosed.
- Monitor regulatory / legal disclosures and public responsibility / governance updates.
- Refresh market data before any action read changes.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| FY2026 full-year actual results | not disclosed | Q1 2026 is the latest official period found. |
| FY2026 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Official guidance gives EPS and capital priorities, not FCF. |
| Official full Q&A transcript | ไม่พบข้อมูลที่ยืนยันได้ | Prepared remarks were found; company-hosted full Q&A was not normalized. |
| Segment-level FCF | not disclosed | Limits segment-specific valuation. |
| Product / contract-level profitability | not disclosed | Important for Optum Health value-based care and Medicare Advantage margin recovery. |
| Full regulatory / legal exposure quantification | partially disclosed | The 10-Q and 10-K disclose risk factors and contingencies, but decision impact remains judgmental. |
| End-of-day 2026-05-20 price | not available during workflow | Market data was intraday as of 2026-05-20 before U.S. market close. |
| Investor-specific position size, cost basis, tax status, and required return | not provided | Needed for individualized sizing. |
