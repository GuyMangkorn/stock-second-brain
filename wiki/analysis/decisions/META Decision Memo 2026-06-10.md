---
type: analysis
analysis_type: decision-memo
ticker: META
company: Meta Platforms, Inc.
date: 2026-06-10
currency: USD
decision: WAIT new capital / HOLD existing quality position
source_files:
  - index.md
  - wiki/entities/META.md
  - raw/financials/META_fundamentals.md
  - raw/imports/META_latest_results_source.md
  - raw/imports/META_market_quote_2026-06-10.md
  - wiki/analysis/valuations/META DCF Valuation 2026-06-10.md
tags:
  - analysis/decision-memo
  - ticker/META
---

# META Decision Memo - 2026-06-10
Entity: [[META]]

## Action Read

**Action: WAIT new capital / HOLD existing quality position.**

Meta เป็น business คุณภาพสูงมากในฝั่ง Family of Apps: Q1 2026 revenue โต 33% YoY, operating margin ยังประมาณ 41%, และ FoA operating income ถึง USD 26.900B ในไตรมาสเดียว. แต่ราคาปัจจุบันไม่ได้มี margin of safety ชัดเจนเมื่อเทียบกับ FCF หลัง capex step-up.

ที่ fresh Nasdaq price USD 577.61, base DCF fair value ประมาณ USD 529 ต่อ diluted share หรือ downside ราว 8%. เพราะ sensitivity กว้างและ bull case ยังมี upside ถ้า AI capex ให้ผลตอบแทนสูง, ผมไม่จัดเป็น avoid. แต่สำหรับ new capital ควรรอราคาต่ำกว่า base value หรือรอหลักฐาน FCF recovery ที่ verify ได้มากขึ้น.

## Current Price / Market Data Check

| Item | Value | Source |
|---|---:|---|
| Fresh price | USD 577.61 | Nasdaq quote API, Jun 10, 2026 12:52 PM ET. |
| Market cap | USD 1.466T | Nasdaq summary API, checked 2026-06-10. |
| Class A + Class B shares outstanding | 2.538B | SEC Q1 2026 Form 10-Q cover facts, as of 2026-04-24. |
| Weighted-average diluted shares | 2.564B | SEC Q1 2026 Form 10-Q / Exhibit 99.1. |
| Yahoo quote cross-check | USD 576.91 | Yahoo Finance chart API, 2026-06-10 12:51:30 PM ET. |

## Evidence From Vault

| Fact | Value | Source |
|---|---:|---|
| Latest verified period | Q1 2026 | `raw/financials/META_fundamentals.md` |
| Q1 2026 revenue | USD 56.311B | SEC 8-K Exhibit 99.1 and Form 10-Q. |
| Q1 2026 revenue growth | 33.08% YoY | Calculated from Q1 2026 and Q1 2025 revenue. |
| Q1 2026 operating income | USD 22.872B | SEC 8-K Exhibit 99.1 and companyfacts. |
| Q1 2026 operating margin | 40.62% | Calculated from official tables. |
| Q1 2026 net income | USD 26.773B | SEC 8-K Exhibit 99.1; includes USD 8.03B tax benefit. |
| Q1 2026 FCF | USD 12.386B | SEC 8-K Exhibit 99.1 company FCF reconciliation. |
| TTM Q1 2026 FCF | USD 45.637B | Calculated using company FCF method from official facts. |
| Q1 2026 FoA revenue | USD 55.909B | SEC 8-K Exhibit 99.1. |
| Q1 2026 FoA operating income | USD 26.900B | SEC 8-K Exhibit 99.1. |
| Q1 2026 Reality Labs revenue | USD 402M | SEC 8-K Exhibit 99.1. |
| Q1 2026 Reality Labs operating loss | USD (4.028B) | SEC 8-K Exhibit 99.1. |
| Q2 2026 revenue guidance | USD 58B-61B | SEC 8-K Exhibit 99.1. |
| FY2026 capex guidance | USD 125B-145B | SEC 8-K Exhibit 99.1, including finance lease principal. |

## Valuation Read

| Valuation item | Result | Read |
|---|---:|---|
| DCF base fair value | USD 529.40 per diluted share | ต่ำกว่า fresh market price ประมาณ 8% |
| DCF bear fair value | USD 296.65 per diluted share | downside ใหญ่ถ้า capex กิน FCF นานกว่าคาด |
| DCF bull fair value | USD 1,032.81 per diluted share | upside ใหญ่ แต่ terminal-value-sensitive |
| Market cap / TTM FCF | 32.1x | ต้องการ FCF recovery ที่ดี |
| TTM FCF yield | 3.11% | ยังไม่ถูกพอสำหรับ add แบบมี margin of safety |
| Reverse DCF | About 19.8% 5-year FCF CAGR required | strong แต่ไม่ถึงขั้นเป็นไปไม่ได้สำหรับ Meta ถ้า AI capex ได้ผล |

valuation อ่านว่า price ปัจจุบันอยู่แถว fair-to-slightly-rich สำหรับ base case. จุดที่ทำให้ยังไม่ควร avoid คือ FoA quality และ bull-case optionality; จุดที่ทำให้ยังไม่ควร add คือ capex guidance ที่สูงมากและ AI ROI ที่ยังไม่ disclosed.

## Bull Case

- FoA ads ยังเป็น machine ที่แข็งแรงมาก: revenue โต 33% YoY และ FoA operating income USD 26.900B ใน Q1 2026.
- Ad impressions +19% YoY และ average price per ad +12% YoY แปลว่า growth มาจากทั้ง volume และ monetization.
- Q2 2026 revenue guidance USD 58-61B ชี้ว่า top-line momentum ยังต่อเนื่อง.
- AI tools อาจเพิ่ม ad ROI, creative automation, business messaging, agents, and recommendation quality.
- Balance sheet ยังมี cash and marketable securities USD 81.180B เทียบกับ long-term debt USD 58.748B.
- ถ้า capex peak แล้ว FCF ramp เข้าใกล้ bull path, stock ยังมี upside meaningful.

## Bear Case

- FY2026 capex guidance USD 125-145B สูงมากและเพิ่งถูก raise จาก USD 115-135B.
- TTM FCF อยู่ที่ USD 45.637B เทียบกับ market cap USD 1.466T ทำให้ FCF yield เพียง 3.11%.
- Q1 2026 net income ได้แรงหนุนจาก USD 8.03B tax benefit.
- Reality Labs ยังขาดทุนหนัก: USD 4.028B operating loss บน revenue USD 402M.
- AI infrastructure ROI, product-level AI revenue, และ Meta AI monetization ยังไม่ disclosed.
- Legal/regulatory matters โดยเฉพาะ youth-related scrutiny อาจมี material loss หรือ operating constraint.

## Key Assumptions

| Assumption | Working choice |
|---|---|
| Investor profile | Long-term investor ที่ต้องการ risk-adjusted compounding และไม่ไล่ราคาเมื่อ margin of safety บาง |
| Position status | ไม่ทราบ; action จึงแยก new capital ออกจาก existing position |
| Valuation discipline | ใช้ FCF หลัง capex และ finance lease principal เป็น anchor ไม่ใช้ headline net income ที่มี tax benefit |
| AI economics | demand/benefit มีสัญญาณดี แต่ ROI ยังต้อง verify จาก FCF และ disclosure เพิ่ม |
| Required margin of safety | ต้องเห็น discount ชัดจาก base fair value หรือ FCF recovery ก่อน add |

## What Would Change The Decision

- upgrade toward ADD ถ้าราคาลงต่ำกว่า base DCF value พร้อม margin of safety หรือ FCF recovery แข็งแรงกว่าที่ base case ใช้.
- upgrade ถ้า Meta แสดงว่า capex กำลัง peak และ TTM FCF ขยับขึ้นแม้ยังลงทุนสูง.
- upgrade ถ้า official disclosure แยก AI ad-tool/business-messaging economics ได้ชัดขึ้น.
- downgrade toward TRIM ถ้า capex guidance ขึ้นอีกโดยไม่มี FCF recovery, Reality Labs losses เร่งขึ้น, หรือ FoA ad growth ชะลอลงชัด.
- downgrade ถ้า regulatory/legal outcomes เริ่มกระทบ product design, targeting, engagement, or cash costs อย่างมีนัยสำคัญ.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Product-level AI revenue, AI ad-tool revenue, Meta AI revenue, and AI infrastructure ROI | Not disclosed | ยัง underwrite AI payback โดยตรงไม่ได้ |
| Reality Labs unit economics and product-level margins | Not disclosed | optionality ยังประเมินเป็น value แยกไม่ได้อย่างมั่นใจ |
| Segment-level free cash flow | Not disclosed | แยก FoA cash engine กับ Reality Labs cash burn ไม่ได้ |
| Full FY2026 results | ไม่พบข้อมูลที่ยืนยันได้ | Q1 และ TTM data คือ cash-flow facts ที่สดและ verify ได้ที่สุด |
| Exact remaining-quarter 2026 capex cadence | Not disclosed | สำคัญต่อ timing ของ FCF trough |
| Investor-specific tax basis and position size | Not provided | existing-position hold/trim ขึ้นกับ sizing และ tax context |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| `raw/imports/META_latest_results_source.md` | Local source note | P1 official-source discovery and extraction. |
| `raw/imports/META_market_quote_2026-06-10.md` | Local market source note | Fresh price, market cap, shares, and quote provenance. |
| `raw/financials/META_fundamentals.md` | Local normalized facts | P4 verified financial facts, charts, ratios. |
| `wiki/entities/META.md` | Local entity page | P6 business model, thesis, risks, catalysts. |
| `wiki/analysis/valuations/META DCF Valuation 2026-06-10.md` | Local valuation memo | P11 DCF and sensitivity. |
| SEC Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm | Official quarterly facts and shares. |
| SEC Q1 2026 8-K Exhibit 99.1 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026028364/meta-03312026xexhibit991.htm | Financial tables, FCF, segment results, guidance. |
| Nasdaq quote / summary APIs | https://api.nasdaq.com/api/quote/META/info?assetclass=stocks; https://api.nasdaq.com/api/quote/META/summary?assetclass=stocks | Fresh price and market cap checked 2026-06-10. |
