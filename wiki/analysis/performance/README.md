# ETF Performance Section

## Purpose

นี่คือชั้น analysis สำหรับเก็บและเปรียบเทียบ performance ของ passive,
index-tracking equity ETF โดยมีเป้าหมายระยะยาวคือดูว่า ETF ใดเหมาะกับ
สภาวะตลาดแบบใด, จุดแข็ง/จุดอ่อนอยู่ตรงไหน, drawdown หนักเพราะอะไร และควร
จัดกลุ่ม exposure อย่างไรเพื่อรับมือหลาย economic regime หรือวิกฤติ

## Ownership

| Layer | Owner |
|---|---|
| `raw/imports/ETF_*_performance_source_YYYY-MM-DD.md` | source map, as-of dates, extraction gaps |
| `raw/funds/ETF_*_performance.md` | normalized annual returns, rolling/monthly metrics, drawdown calculations and provenance |
| `wiki/analysis/performance/ETF_* Performance.md` | per-ETF interpretation, ranking, behavioral classification and driver notes |
| [[ETF Performance Index]] | coverage dashboard and entry point |
| [[ETF Performance Regime Matrix]] | cross-ETF comparison and two-axis classification |

อย่าคัดลอกตาราง performance เต็มจาก `raw/funds/` มาซ้ำใน entity หรือ decision
memo ให้ลิงก์กลับมาที่ normalized owner แทน

## Metric Convention

- Canonical return คือ `NAV Total Return` ซึ่งรวม reinvested distributions และ
  fund expenses เมื่อ issuer เปิดเผยข้อมูลในรูปนี้
- `Market Price Total Return` เก็บแยกเพื่อดูผลจากราคาซื้อขาย, premium/discount
  และ timing
- Benchmark ต้องใช้ return basis เดียวกันกับ ETF และต้องรักษา as-of date
- Calendar-year ranking ใช้เฉพาะ complete years; inception-year และ current YTD
  เป็น partial และไม่จัดอันดับรวมกับปีเต็ม
- `Best up year` คือ positive return สูงสุด; `least positive` คือ positive return
  ต่ำสุด; `worst down year` คือ negative return ติดลบมากสุด; `least bad` คือ
  negative return ที่ใกล้ศูนย์ที่สุด
- Monthly behavior และ maximum drawdown จาก secondary provider ต้องติดป้าย
  `secondary`; ห้ามใช้แทน official NAV facts โดยไม่เปิดเผย

## Classification Model

ใช้สองแกนแยกกัน:

1. `Structural classification`: benchmark, geography, sector/factor tilt,
   methodology, concentration and cost
2. `Behavioral classification`: observed return, beta/capture, positive-month
   rate, drawdown and response in a named regime

ชื่อกลุ่มเป็น hypothesis ที่ refresh ได้ ไม่ใช่คำสัญญาว่ากองจะป้องกันวิกฤติใน
อนาคต และไม่ใช่คำแนะนำ portfolio fit โดยไม่มี holdings ของผู้ใช้

## Refresh Workflow

1. Verify issuer identity and exchange as `EXCHANGE:TICKER`.
2. Capture official performance/factsheet and source note first.
3. Normalize annual and rolling/monthly metrics in `raw/funds/`.
4. Refresh the per-ETF analysis note.
5. Update [[ETF Performance Index]] and [[ETF Performance Regime Matrix]] only
   when the common window or classification changes.
6. Add one dated workflow bullet to `log.md` for a durable refresh.

## Pilot Status

Pilot coverage is [[ETF_AMEX_DGRO Performance]], [[ETF_AMEX_VIG Performance]],
[[ETF_NASDAQ_VIGI Performance]], and [[ETF_AMEX_DIVI Performance]]. The first
cross-ETF common window is 2021-2025. 2026 data remain partial and are shown as
freshness context, not as a full-year ranking.
