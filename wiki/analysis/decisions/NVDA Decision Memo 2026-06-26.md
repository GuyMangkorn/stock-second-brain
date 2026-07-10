---
type: decision-memo
ticker: NVDA
company: NVIDIA Corporation
decision_date: 2026-06-26
action_read: WAIT / HOLD-existing-quality-position
price_check: 2026-06-25 12:43 PM EDT
tags:
  - analysis/decision
  - ticker/NVDA
---

# NVDA Decision Memo - 2026-06-26
Entity: [[NVDA]]

## Action Read

`WAIT / HOLD-existing-quality-position`.

NVDA เป็นหนึ่งในธุรกิจคุณภาพสูงสุดใน AI infrastructure cycle: revenue, margin, FCF และ balance sheet แข็งมาก. แต่ราคา USD 195.03 และ market cap USD 4.72T ทำให้ margin of safety บางใน conservative DCF. สำหรับ new capital ควรรอ either better entry หรือ evidence รอบถัดไปที่ทำให้ starting FCF / growth assumptions สูงขึ้นอย่าง source-backed.

ถ้ามี position อยู่แล้ว, thesis ยังพอถือได้ในฐานะ quality compounder แต่ควรระวัง sizing เพราะ downside to conservative DCF ยังสูง.

## Current Price / Market Data Check

| Metric | Value | Checked At | Source |
|---|---:|---|---|
| Stock price | USD 195.03 | 2026-06-25 12:43 PM EDT | StockAnalysis |
| Market cap | USD 4.72T | 2026-06-25 12:43 PM EDT | StockAnalysis |
| Shares outstanding | 24.22B | 2026-06-25 12:43 PM EDT | StockAnalysis |
| TTM revenue | USD 253.49B | 2026-06-25 12:43 PM EDT | StockAnalysis |
| TTM net income | USD 159.61B | 2026-06-25 12:43 PM EDT | StockAnalysis |

## Evidence From Vault

| Evidence | Read |
|---|---|
| Q1 FY2027 revenue USD 81.615B, up 85% YoY | Demand remains extremely strong. |
| Data Center revenue USD 75.2B, up 92% YoY | Thesis is still AI infrastructure-led. |
| Q1 FY2027 FCF USD 48.554B | Cash conversion is exceptional. |
| TTM calculated FCF USD 118.994B | Supports real earning power, not only accounting profit. |
| Cash + marketable debt securities USD 50.335B vs debt USD 8.470B | Balance sheet is a strength. |
| Q2 FY2027 revenue guidance USD 91.0B +/- 2% | Near-term growth remains high, but market already prices in a large runway. |
| Base DCF fair value USD 117.96/share | Current price is materially above conservative intrinsic value estimate. |

## Valuation Read

ใช้ `DCF Read` เป็น main lens เพราะมี source-backed FCF, cash, debt, shares และ guidance ครบพอ. Base case ใช้ TTM FCF USD 118.994B, FCF growth fade 28% -> 6%, WACC 10.0%, terminal growth 2.5%, conservative net cash ที่ไม่นับ marketable equity securities.

ผลลัพธ์: base DCF fair value ประมาณ USD 117.96/share หรือ downside ประมาณ 39.5% จากราคา USD 195.03. Sensitivity range ที่ WACC 9%-11% และ terminal growth 2.0%-3.0% อยู่ประมาณ USD 99.46-145.63/share, ยังต่ำกว่าราคาเช็คสดทั้งหมด.

Interpretation: ตลาดอาจถูกได้ถ้า NVDA สามารถ sustain growth และ FCF conversion สูงกว่าสมมติฐาน conservative base case เป็นเวลานาน. แต่สำหรับ decision memo ที่ต้องมี margin of safety, ราคา ณ ตอนนี้ยังไม่ให้ cushion พอ.

## Bull Case

- NVIDIA ยืนกลาง AI factory buildout และมี platform breadth ตั้งแต่ compute, networking, systems, software ecosystem ไปถึง edge/robotics.
- Q1 FY2027 growth ยังเร่งแรง และ Q2 guide USD 91.0B +/- 2% บ่งชี้ demand visibility ระยะสั้นยังดี.
- FCF conversion สูงมาก ทำให้ buybacks/dividends/investment capacity แข็งแรง.
- Net cash position แบบ conservative ช่วยลด balance-sheet risk.

## Bear Case

- Valuation ต้องการ perfect execution ต่อเนื่องจากฐานรายได้และ FCF ที่ใหญ่มากแล้ว.
- Customer concentration และ hyperscaler capex digestion อาจทำให้ growth rate fade เร็วกว่าที่ตลาดคาด.
- Export controls โดยเฉพาะ China compute revenue ทำให้ upside บางส่วนถูกจำกัด.
- Competition/custom silicon อาจกด pricing power หรือ attach rate ในอนาคต.
- Segment taxonomy ใหม่ลด comparability และทำให้ tracking historical mix ต้องระวัง.

## Key Assumptions

- TTM FCF USD 118.994B เป็น starting FCF ที่เหมาะกับ DCF ณ วันนี้.
- WACC 10.0% สะท้อน Information Technology risk, AI cycle volatility, market leadership, and net cash.
- Terminal growth 2.5% สอดคล้องกับ mature compounder terminal range.
- Marketable equity securities ไม่ถูกนับเป็น cash ใน base DCF เพราะ fair value volatility.

## What Would Change The Decision

- เปลี่ยนเป็น ADD ได้ถ้าราคาลงใกล้ conservative DCF range หรือ Q2/Q3 FY2027 ทำให้ source-backed TTM FCF base สูงขึ้นมากพอพร้อม guidance ที่ยืนยัน runway.
- ลดเป็น AVOID ถ้า gross margin ต่ำกว่า guidance, FCF conversion แย่ลงชัดเจน, หรือ capex/customer concentration risk ทำให้ demand quality อ่อนลง.
- Re-run P11 หลัง Q2 FY2027 results และ refresh price/market cap/shares ก่อน action call ใหม่.

## Missing / Unverified Data

- Full earnings call transcript / Q&A: ไม่พบข้อมูลที่ยืนยันได้ใน ingest นี้.
- Peer multiple set: not built.
- Named hyperscaler demand/backlog: not disclosed.
- Intraday market data should be refreshed before actual trading.

## Source Map

| Source | URL / Path |
|---|---|
| Latest results source note | `raw/imports/NVDA_latest_results_source.md` |
| Market quote source note | `raw/imports/NVDA_market_quote_2026-06-25.md` |
| Normalized financial facts | `raw/financials/NVDA_fundamentals.md` |
| Entity page | `wiki/entities/NVDA.md` |
| DCF valuation memo | `wiki/analysis/valuations/NVDA DCF Valuation 2026-06-26.md` |
