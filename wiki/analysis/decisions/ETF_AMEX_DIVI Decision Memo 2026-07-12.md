---
type: decision
instrument_type: ETF
entity_key: AMEX:DIVI
ticker: DIVI
decision_date: 2026-07-12
action: WATCH
portfolio_role: satellite international dividend tilt
source_note: raw/imports/ETF_AMEX_DIVI_fund_source_2026-07-12.md
fund_facts: raw/funds/ETF_AMEX_DIVI_fund_facts.md
entity: wiki/entities/ETF_AMEX_DIVI.md
tags:
  - decision/etf
  - action/watch
  - ticker/DIVI
---

# ETF_AMEX_DIVI Decision Memo - 2026-07-12

## Portfolio Role

DIVI เหมาะกับบทบาท `satellite international dividend tilt` หรือเป็นแกน
ex-U.S. เฉพาะกรณีที่ต้องการ developed-markets exposure ที่เอนเข้าหา dividend
yield/value อย่างตั้งใจ. กองทุนไม่ได้เป็น pure high-yield income vehicle:
30-Day SEC Yield ล่าสุดอยู่ที่ `2.88%` และจ่ายรายไตรมาส. การประเมินนี้เป็น
fund-level suitability เท่านั้น เพราะยังไม่มี user-provided portfolio holdings
จึงไม่อ้างว่าเหมาะกับ portfolio ทั้งหมดหรือช่วยลด diversification overlap.

## Action Read

**WATCH**. โครงสร้างกองทุนดีพอสำหรับ watchlist: passive equity, expense ratio
`0.09%`, holdings `417` ราย, top-10 รวมเพียง `14.29%`, และ benchmark ถูกออกแบบ
ให้เพิ่ม dividend yield โดยจำกัด tracking error จาก developed ex-North America
parent index. เหตุผลที่ยังไม่ยกระดับเป็น `BUY` คือ market-data pair ล่าสุดจาก
issuer ที่ยืนยันได้มีถึง 2026-06-24 เท่านั้น และไม่มี same-day NAV ที่จับคู่กับ
secondary price ล่าสุด 2026-07-08. นอกจากนี้ financials มีน้ำหนัก `29.13%`
และ Japan `23.93%` ทำให้ต้องยอมรับ factor/country concentration.

เงื่อนไขยกระดับเป็น `BUY`: ได้ issuer NAV/market price และ premium/discount
ในวันเดียวกันที่ยังสด, complete holdings snapshot สำหรับตรวจ overlap, และผู้ลงทุน
ต้องการ international dividend tilt นี้จริง ไม่ใช่เพียงต้องการ yield สูงสุด.

## Current Price / NAV Check

Issuer page ณ 2026-06-24 รายงาน NAV `$42.72` และ market price `$42.81` หรือ
`+0.21%` premium at close; 30-day median bid/ask spread `0.14%`. Secondary
market context ณ 2026-07-08 อยู่ที่ close `$42.41`, แต่ไม่มี issuer NAV วันเดียวกัน
จึงไม่คำนวณ July premium/discount และไม่ใช้ price stale นี้เป็น target.

## Peer-Relative Read

เมื่อเทียบเชิง mandate กับ `VIGI` ใน vault, DIVI เน้น dividend tilt/value และ
tracking-error control ส่วน VIGI เป็น international dividend-appreciation/
quality exposure. สองกองทุนจึงอาจทับกันในชื่อบริษัทและประเทศ แต่ไม่ใช่
substitute ที่เทียบกันได้โดยอัตโนมัติ. รอบนี้ไม่ได้สร้าง comparison memo เพราะ
ผู้ใช้ไม่ได้ขอ peer/overlap analysis และยังไม่มี complete current holdings ของ DIVI
กับ peer ใน snapshot เดียวกัน.

## Valuation / Cost / Tracking Read

ไม่มี corporate DCF สำหรับ ETF. Cost/implementation เป็นจุดแข็ง: factsheet ณ
2026-06-30 รายงาน total net assets `$2.56B`, P/B `2.09x`, trailing P/E `17.40x`,
และ 1-year NAV return `24.65%` เทียบ underlying index `24.58%` หรือดีกว่า
`0.07 percentage points`. ตั้งแต่ inception NAV return เฉลี่ยปีละ `11.02%`
เทียบ index `11.26%`, ต่าง `-0.24 percentage points`; เป็น return difference
ไม่ใช่ full tracking-error statistic. Sector/country tilt และ FX risk จึงสำคัญ
กว่าการไล่หา intrinsic-value target.

## Key Falsifier

มุมมองจะผิดถ้า optimizer ทำให้ financials/Japan concentration สูงขึ้นจน
ผลตอบแทนและ dividend quality แย่กว่า parent อย่างต่อเนื่อง, tracking difference
กว้างขึ้นอย่างมีนัยสำคัญ, หรือ full holdings แสดง overlap กับ international sleeve
ที่มีอยู่จนบทบาทกองทุนซ้ำกัน.

## Action-Relevant Gaps

- `ไม่พบข้อมูลที่ยืนยันได้` สำหรับ same-day issuer NAV/market price หลัง 2026-06-24.
- `ไม่พบข้อมูลที่ยืนยันได้` สำหรับ complete holdings XLS ใน source capture รอบนี้.
- ยังไม่มี portfolio holdings ของผู้ใช้ จึงสรุปได้เฉพาะ fund suitability ไม่ใช่ fit.
- Tax/withholding outcome ยังขึ้นกับ account และ jurisdiction.

## Reports / Sources

- [[ETF_AMEX_DIVI]]
- [[ETF_AMEX_DIVI_fund_facts]]
- [[ETF_AMEX_DIVI_fund_source_2026-07-12]]
- [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]]
- [Franklin official product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/21412/SINGLCLASS/franklin-international-core-dividend-tilt-index-etf/DIVI)
- [Franklin official factsheet](https://www.franklintempleton.com/forms-literature/download/DIVI-FF)
- [Franklin official prospectus](https://www.franklintempleton.com/forms-literature/download/ETF3-P)
- [StockAnalysis secondary price context](https://stockanalysis.com/etf/divi/)
