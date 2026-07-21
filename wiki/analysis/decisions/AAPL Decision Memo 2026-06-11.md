---
type: analysis
analysis_type: decision-memo
ticker: AAPL
company: Apple Inc.
date: 2026-06-11
currency: USD
decision: AVOID new capital / HOLD existing quality position only if sizing and tax context justify it
source_files:
  - index.md
  - wiki/entities/AAPL.md
  - raw/financials/AAPL_fundamentals.md
  - raw/imports/AAPL_latest_results_source.md
  - raw/imports/AAPL_market_quote_2026-06-11.md
  - wiki/analysis/valuations/AAPL DCF Valuation 2026-06-11.md
tags:
  - analysis/decision-memo
  - ticker/AAPL
---

# AAPL Decision Memo - 2026-06-11
Entity: [[AAPL]]

## Action Read

**Action: AVOID new capital / HOLD existing quality position only if sizing and tax context justify it.**

Apple เป็น business คุณภาพสูงและ Q2 FY2026 แข็งแรงมาก: revenue +17% YoY, iPhone +22%, Services +16%, Services gross margin 76.7%, และ TTM FCF อยู่ที่ USD 129.174B. แต่ valuation ตอนนี้ต้องการ growth ที่สูงมากจากฐาน FCF ที่ใหญ่มากอยู่แล้ว.

ที่ fresh price USD 292.15, base DCF fair value ประมาณ USD 153 ต่อ diluted share และ bull case ประมาณ USD 229 ต่อ share. Reverse DCF ต้องการ FCF CAGR ราว 20.5% ต่อปี 5 ปีที่ WACC 9.0% / terminal growth 2.5%. ผมจึงไม่ add new capital ที่ราคานี้ แม้จะยอมรับว่า existing holder อาจ hold ได้ถ้า sizing ไม่ใหญ่และ tax friction สูง.

## Current Price / Market Data Check

| Item | Value | Source |
|---|---:|---|
| Fresh price | USD 292.15 | StockAnalysis statistics page, Jun 10, 2026 1:01 PM EDT. |
| Market cap | USD 4.29T | StockAnalysis statistics page, checked 2026-06-10. |
| Enterprise value | USD 4.21T | StockAnalysis statistics page. |
| Shares outstanding | 14.69B | StockAnalysis statistics page. |
| Shares issued and outstanding | 14.687356B | SEC Q2 FY2026 Form 10-Q cover page, as of 2026-04-17. |
| Weighted-average diluted shares | 14.768115B | SEC Q2 FY2026 Form 10-Q, 1H FY2026. |
| Cash and marketable securities | USD 146.595B | SEC Q2 FY2026 Form 10-Q. |
| Total debt | USD 84.711B | SEC Q2 FY2026 Form 10-Q, calculated. |
| TTM FCF | USD 129.174B | Official-source calculation in `[[AAPL_fundamentals]]`. |
| P/FCF | 33.04x | StockAnalysis statistics page. |
| EV/FCF | 32.56x | StockAnalysis statistics page. |

## Evidence From Vault

| Fact | Value | Source |
|---|---:|---|
| Latest verified period | Q2 FY2026 | `raw/financials/AAPL_fundamentals.md` |
| Q2 FY2026 total net sales | USD 111.184B | SEC Q2 FY2026 Form 10-Q. |
| Q2 FY2026 revenue growth | 16.60% YoY | Calculated from SEC Q2 FY2026 Form 10-Q. |
| Q2 FY2026 operating income | USD 35.885B | SEC Q2 FY2026 Form 10-Q. |
| Q2 FY2026 operating margin | 32.27% | Calculated from official table. |
| Q2 FY2026 net income | USD 29.578B | SEC Q2 FY2026 Form 10-Q. |
| Q2 FY2026 diluted EPS | USD 2.01 | SEC Q2 FY2026 Form 10-Q. |
| Q2 FY2026 iPhone revenue | USD 56.994B | SEC Q2 FY2026 Form 10-Q. |
| Q2 FY2026 Services revenue | USD 30.976B | SEC Q2 FY2026 Form 10-Q. |
| Q2 FY2026 Services gross margin | 76.7% | SEC Q2 FY2026 Form 10-Q. |
| 1H FY2026 FCF | USD 78.283B | Calculated: 1H OCF - capex. |
| TTM Q2 FY2026 FCF | USD 129.174B | Calculated from FY2025, 1H FY2025, and 1H FY2026 official inputs. |
| Official forward guidance | not disclosed | Missing / Unverified Data. |

## Valuation Read

| Valuation item | Result | Read |
|---|---:|---|
| DCF base fair value | USD 153.37 per diluted share | ต่ำกว่า fresh market price ประมาณ 48% |
| DCF bear fair value | USD 103.18 per diluted share | downside ใหญ่ถ้า product cycle / margins normalize |
| DCF bull fair value | USD 228.65 per diluted share | ยังต่ำกว่า fresh price ประมาณ 22% |
| Market cap / TTM FCF | 33.0x | demanding สำหรับบริษัทที่ FCF base ใหญ่มาก |
| TTM FCF yield | 3.03% | margin of safety บาง |
| Reverse DCF | About 20.5% 5-year FCF CAGR required | high bar มากสำหรับ Apple scale |

valuation อ่านว่า market กำลังให้ credit กับ Apple quality, buybacks, Services, and AI/device-cycle optionality สูงมาก. สิ่งเหล่านี้อาจเกิดขึ้นได้บางส่วน แต่ official source set ยังไม่พอให้ underwrite new capital ที่ราคานี้.

## Bull Case

- Ecosystem moat ยังแข็งแรง: hardware, OS, services, developer network, brand, and installed base หนุนกัน.
- Q2 FY2026 iPhone revenue +22% YoY และ Greater China +28% YoY ทำให้เห็น product-cycle momentum.
- Services revenue +16% YoY และ gross margin 76.7% ช่วยยกระดับ quality ของ earnings.
- TTM FCF USD 129.174B ทำให้ buyback/dividend capacity ใหญ่มาก.
- Balance sheet เป็น net cash เมื่อรวม marketable securities.
- ถ้า Apple Intelligence / AI features กระตุ้น upgrade cycle และ Services monetization โดยไม่ทำให้ cost structure เสีย อาจหนุน bull case ได้.

## Bear Case

- Fresh valuation สูง: P/FCF 33.04x และ market cap USD 4.29T.
- Bull DCF จาก source-backed FCF ยังต่ำกว่าราคาปัจจุบัน.
- iPhone ยังคิดเป็น 51% ของ Q2 FY2026 revenue; product-cycle normalization จะกระทบมาก.
- Apple ระบุ component constraints and increasing costs อาจ intensify.
- Tariffs and trade disputes could pressure supply chain, pricing, demand, and gross margin.
- AI monetization, Apple Intelligence economics, and official forward guidance are not disclosed.

## Key Assumptions

| Assumption | Working choice |
|---|---|
| Investor profile | Long-term investor ที่ต้องการ margin of safety จาก source-backed FCF ไม่ไล่ quality เมื่อ valuation สูงมาก |
| Position status | ไม่ทราบ; action จึงแยก new capital ออกจาก existing position |
| Valuation discipline | ใช้ TTM FCF จาก official-source calculation เป็น anchor ไม่ใช้ analyst target เป็น fair value |
| AI economics | Treat as upside optionality only until official monetization data appears |
| Required margin of safety | ต้องเห็น discount ชัดจาก base DCF หรือเห็น verified FCF growth ที่ทำให้ reverse DCF สมเหตุสมผล |

## What Would Change The Decision

- upgrade toward WATCHLIST/ADD ถ้าราคาลงใกล้หรือต่ำกว่า valuation range พร้อม margin of safety.
- upgrade ถ้า official results แสดง FCF per share compounding สูงมากต่อเนื่องโดย margin ไม่ถูกกด.
- upgrade ถ้า Apple disclose AI / Services monetization ที่ชัดและ source-backed.
- downgrade existing-position read toward TRIM ถ้า iPhone growth normalize, Services decelerate, หรือ gross margin pressure ชัดขึ้น.
- downgrade ถ้า buybacks ยังสูงมากที่ valuation แพงโดยไม่มี FCF growth รองรับ.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Official Apple investor-relations Q2 FY2026 press release page | ไม่พบข้อมูลที่ยืนยันได้ | ขาด official release wording และ management framing |
| Official earnings-call transcript | ไม่พบข้อมูลที่ยืนยันได้ | ขาด Q&A / management tone |
| Forward revenue, EPS, gross margin, capex, or FCF guidance | Not disclosed in verified source set | DCF ต้องใช้ assumptions ไม่ใช่ guidance |
| Product unit volumes and product-level margins below Products / Services | Not disclosed | วิเคราะห์ unit economics ลึกไม่ได้ |
| Segment-level FCF by product or geography | Not disclosed | แยก cash contribution by product/geography ไม่ได้ |
| AI-specific revenue or Apple Intelligence monetization | Not disclosed | ยัง underwrite AI optionality โดยตรงไม่ได้ |
| Investor-specific tax basis and position size | Not provided | existing-position hold/trim ขึ้นกับ sizing และ tax context |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| `raw/imports/AAPL_latest_results_source.md` | Local source note | P1 official-source discovery and extraction. |
| `raw/imports/AAPL_market_quote_2026-06-11.md` | Local market source note | Fresh price, market cap, shares, cash/debt and quote provenance. |
| `raw/financials/AAPL_fundamentals.md` | Local normalized facts | P4 verified financial facts, charts, ratios. |
| `wiki/entities/AAPL.md` | Local entity page | P6 business model, thesis, risks, catalysts. |
| `wiki/analysis/valuations/AAPL DCF Valuation 2026-06-11.md` | Local valuation memo | P11 DCF and sensitivity. |
| SEC Q2 FY2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/320193/000032019326000013/aapl-20260328.htm | Official quarterly facts and shares. |
| SEC FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm | Annual baseline. |
| StockAnalysis statistics | https://stockanalysis.com/stocks/aapl/statistics/ | Fresh price, market cap, shares, and valuation metrics checked 2026-06-10. |
