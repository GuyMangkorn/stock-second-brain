---
type: entity-index
scope: etf
updated: 2026-07-12
tags:
  - entity/etf-index
---

# ETF Index

นี่คือ index ของ ETF ที่ถูกยกระดับเป็น durable entity เพราะเป็น core candidate ใน current triage. ETF อีก 100 rows ใน [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]] ยังคงเป็น comparison universe และไม่จำเป็นต้องมี entity page จนกว่าจะมี allocation, watchlist, หรือ research workflow ต่อเนื่อง.

| Entity | Instrument Key | Fund | Role | Primary Tracker |
|---|---|---|---|---|
| [[ETF_AMEX_DGRO]] | `AMEX:DGRO` | iShares Core Dividend Growth ETF | Core candidate | [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]] |
| [[ETF_AMEX_VIG]] | `AMEX:VIG` | Vanguard Dividend Appreciation ETF | Core candidate | [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]] |
| [[ETF_NASDAQ_VIGI]] | `NASDAQ:VIGI` | Vanguard International Dividend Appreciation ETF | Core candidate | [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]] |
| [[ETF_AMEX_DIVI]] | `AMEX:DIVI` | Franklin International Core Dividend Tilt Index ETF | International dividend tilt | [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]] |

## Maintenance Rule

ใช้ `entity_key: EXCHANGE:TICKER` เป็น identity หลัก เพื่อไม่ให้ ticker ที่ซ้ำข้ามตลาด เช่น `TDIV` หรือ `WDIV` ชนกัน. Holdings, yield, distribution, expense ratio, และ price ต้องอ้างอิง official source ที่มี as-of date ก่อนอัปเดต entity.

## Performance Tracker

- [[ETF Performance Index]]
- [[ETF Performance Regime Matrix]]

Performance history belongs to `raw/funds/ETF_EXCHANGE_TICKER_performance.md`
and its linked analysis note, not to this entity index.
