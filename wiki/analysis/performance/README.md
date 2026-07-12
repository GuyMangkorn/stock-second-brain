# ETF Performance Convention

## Purpose

เก็บ performance ของ passive, index-tracking equity ETF ให้สั้นพอสำหรับอ่านและ
นำไปวิเคราะห์ต่อได้ทันที. หน้า ETF หนึ่งไฟล์เป็น owner ของตัวเลขและคำแปลผล.

## File Convention

| Layer | Owner |
|---|---|
| `wiki/analysis/performance/ETF_EXCHANGE_TICKER Performance.md` | ตัวเลข annual return, best/worst, risk read-through, classification, driver notes และ source links |
| [[ETF Performance Index]] | coverage dashboard และ cross-ETF comparison |
| `raw/imports/ETF_performance_sources_YYYY-MM-DD.md` | source map รวม, as-of dates, gaps และ audit trail ต่อรอบ refresh |
| `raw/funds/ETF_EXCHANGE_TICKER_fund_facts.md` | holdings, methodology, cost และ fund structure; ไม่ซ้ำ performance table |

ไม่สร้าง `raw/funds/ETF_*_performance.md` แยกอีก. ไม่คัดลอก performance table
เข้า entity หรือ decision memo; ให้ลิงก์ไปหน้า ETF performance เพียงหน้าเดียว.

## Metric Convention

- Canonical return คือ `NAV Total Return` รวม reinvested distributions และ fund
  expenses; benchmark ต้องใช้ basis เดียวกัน
- ตารางหลักใช้คอลัมน์ `ETF TR` และ `Benchmark` เท่านั้น. Market-price return
  เก็บเฉพาะเมื่อมีประเด็น premium/discount ที่ต้องวิเคราะห์
- Calendar-year ranking ใช้เฉพาะ complete years; inception-year และ current YTD
  เป็น partial และไม่จัดอันดับรวมกับปีเต็ม
- `*` = secondary dividend-reinvested proxy; `†` = official inception-year
  partial. ทั้งคู่ต้องมีคำอธิบายใต้ตาราง
- Best/worst ของ ETF รายตัวใช้ complete years ที่มีในหน้านั้นได้ โดยต้องคง marker
  ของแหล่งข้อมูลไว้; cross-ETF comparison ใช้เฉพาะ official common window
  เดียวกัน
- `Best up year` คือ positive return สูงสุด; `least positive` คือ positive return
  ต่ำสุด; `worst down year` คือ negative return ติดลบมากสุด; `least bad` คือ
  negative return ที่ใกล้ศูนย์ที่สุด
- Monthly behavior และ maximum drawdown จาก secondary provider ต้องติดป้าย
  `secondary`; ห้ามใช้แทน official NAV facts

## Minimal Page Template

ลำดับมาตรฐานของ `ETF_EXCHANGE_TICKER Performance.md`:

1. `Bottom line` — 2-3 ประโยค: period, best/worst และ current YTD
2. `Performance check` — identity, metric, benchmark และ annual table
3. `Up years / Down years` — best, least positive, worst, least bad
4. `Risk read-through` — monthly behavior, drawdown, recovery และ as-of dates
5. `Driver notes` — ไม่เกิน 3 regime/event notes; แยก confirmed กับ probable
6. `Sources` — official issuer และ secondary links

## Classification Model

ใช้สองแกนในหน้า ETF และสรุปอีกครั้งใน index:

1. `Structural`: benchmark, geography, factor tilt, methodology และ cost
2. `Behavioral`: observed return, positive-month rate, drawdown และ response in
   a named regime

ชื่อกลุ่มเป็น hypothesis ที่ refresh ได้ ไม่ใช่คำสัญญาว่ากองจะป้องกันวิกฤติใน
อนาคต และไม่ใช่คำแนะนำ portfolio fit โดยไม่มี holdings ของผู้ใช้

## Refresh Workflow

1. Verify issuer identity and exchange as `EXCHANGE:TICKER`.
2. Capture sources in one dated batch note under `raw/imports/`.
3. Update one per-ETF performance page; keep only metrics needed for decisions.
4. Update [[ETF Performance Index]] when coverage, common window or grouping
   changes.
5. Add one dated workflow bullet to `log.md`.

## Pilot Status

Pilot coverage is [[ETF_AMEX_DGRO Performance]], [[ETF_AMEX_VIG Performance]],
[[ETF_NASDAQ_VIGI Performance]], and [[ETF_AMEX_DIVI Performance]]. The common
window is 2021-2025. 2026 data remain partial and are shown as freshness context,
not as a full-year ranking.
