---
type: entity-index
scope: etf
updated: 2026-08-07
tags:
  - entity/etf-index
---

# ETF Index

นี่คือ index ของ ETF ที่ถูกยกระดับเป็น durable entity เพราะเป็น core candidate ใน current triage. ETF อีก 100 rows ใน [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]] ยังคงเป็น comparison universe และไม่จำเป็นต้องมี entity page จนกว่าจะมี allocation, watchlist, หรือ research workflow ต่อเนื่อง.

| Entity | Instrument Key | Fund | Role | Primary Tracker |
|---|---|---|---|---|
| [[ETF_AMEX_DGRO]] | `AMEX:DGRO` | iShares Core Dividend Growth ETF | Core candidate | [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]] |
| [[ETF_AMEX_VIG]] | `NYSE Arca:VIG` | Vanguard Dividend Appreciation ETF | Core candidate | [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]] |
| [[ETF_NASDAQ_VIGI]] | `NASDAQ:VIGI` | Vanguard International Dividend Appreciation ETF | Core candidate | [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]] |
| [[ETF_AMEX_DIVI]] | `AMEX:DIVI` | Franklin International Core Dividend Tilt Index ETF | International dividend tilt | [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]] |

## Maintenance Rule

ใช้ `entity_key: EXCHANGE:TICKER` เป็น identity หลัก เพื่อไม่ให้ ticker ที่ซ้ำข้ามตลาด เช่น `TDIV` หรือ `WDIV` ชนกัน. Holdings, yield, distribution, expense ratio, และ price ต้องอ้างอิง official source ที่มี as-of date ก่อนอัปเดต entity.

## Performance Tracker

- [[ETF Performance Index]]
- [[ETF Performance Ranking 2026-08-07]] — reproducible 2016-2025 USA Top 10 and non-U.S. Regional Top 5 screen

Performance history belongs to the single page
`wiki/analysis/performance/ETF_EXCHANGE_TICKER Performance.md`, not to this
entity index. Fund structure and holdings remain in `raw/funds/`.

## Reusable prompt: ETF performance ranking

ใช้ prompt นี้เมื่อทำ performance screen รอบใหม่; ให้ยึด owner pages และ dated source batch เป็นหลัก:

```text
สร้าง reproducible ETF performance ranking จาก current wiki/analysis/performance/ETF_* Performance.md pages และ source batch ที่ linked อยู่ในแต่ละหน้า โดยใช้เฉพาะ passive, index-tracking equity ETFs ที่มี canonical entity_key: EXCHANGE:TICKER และ verified underlying exposure/primary region.

Data contract:
- Common complete-calendar window = 2016-2025.
- Metric = NAV Total Return รวม reinvested distributions และ fund expenses เท่านั้น; ห้ามผสม market-price return, price return, YTD, partial year, benchmark row, incompatible currency หรือ unresolved return basis.
- ต้องมี annual observations ครบ 10 ปี; อย่างน้อย 8 แถวต้องเป็น official หรือ official-derived; AI-derived ได้ไม่เกิน 2 แถว และต้อง label ทุกปีเป็น official, official-derived, secondary หรือ AI-derived.
- Exclude active, bond, commodity, multi-asset, leveraged, inverse, derivative-heavy, incomplete, unresolved-basis และ material strategy/index-break records.

Scoring:
- สำหรับแต่ละปีคำนวณ mid-rank percentile ใน eligible universe เดียวกัน: P(x) = 100 × (rank_mid - 1) / (N - 1), rank_mid = 1 + count(values < x) + 0.5 × count(values = x).
- Confidence weights: official = 1.00, official-derived = 0.80, secondary = 0.50, AI-derived = 0.25. Normalize weighted annual percentiles ก่อนคูณ 60.
- Weighted TR Score = 60 points; Consistency = 15 × positive_years/10 + 10 × longest_positive_streak/10; Downside stability = 10 × percentile(worst annual TR)/100 + 5 × percentile(-population annual volatility)/100. Total Score = TR + Consistency + Downside, 0-100.
- Tie-breakers: official/official-derived coverage, Consistency, Downside stability, ticker alphabetically.

Selection:
- USA Top 10 = 10 highest-scoring ETFs whose primary region is USA.
- Non-U.S. Regional Top 5 = rank one common non-USA pool, keep the highest scorer per distinct primary region, then select the five highest regional winners. ห้ามใช้ exchange location แทน underlying exposure.

Output (Thai-first narrative; English metric names, tickers, formulas and source labels): methodology/eligibility, USA Top 10 table, Non-U.S. Regional Top 5 table, exact exclusions, source-confidence mix with AI-derived rows and 0.25 weight, formulas plus intermediate values sufficient to reproduce every score, and source links near supported figures. Validate 10 annual rows per selected ETF, score reconciliation, exactly 10 USA rows, five distinct non-U.S. regions, and resolving owner/region wikilinks. ระบุชัดว่าเป็น performance screen ไม่ใช่คำแนะนำหรือ portfolio-fit claim.
```
