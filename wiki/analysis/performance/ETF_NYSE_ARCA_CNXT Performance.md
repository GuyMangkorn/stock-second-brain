---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:CNXT
ticker: CNXT
exchange: NYSE Arca
fund: VanEck ChiNext Innovators ETF
tracked_index: ChiNext Index (SZ988107)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-22
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/CNXT
  - geography/China
---

# CNXT Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

CNXT เป็น passive/index-tracking China A-share equity ETF ที่พยายามติดตาม ChiNext Index (SZ988107). Official VanEck ระบุ rolling 10-year NAV Total Return CAGR `7.37%` ณ 2026-06-30 ครอบคลุม 10.00 elapsed years. Raw start/end TR values ไม่ได้เปิดเผย; ค่า normalized end `203.62` จาก start `100.00` เป็นค่าที่คำนวณจาก CAGR ที่ issuer ปัดเศษ ไม่ใช่ official endpoint. Calendar-year NAV rows ของกองทุนไม่ถูกเปิดเผยใน capture นี้ จึงไม่จัดอันดับ best/worst หรือคำนวณ 2021-2025 CAGR. Current NAV YTD คือ `16.05%` ณ 2026-07-22.

## Performance check

- entity_key: NYSE Arca:CNXT
- Inception: 2014-07-23
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index (issuer benchmark): ChiNext Index (SZ988107)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR CAGR: `7.37%` (official issuer average annual total return)
- Normalized NAV TR: start `100.00`; end `203.62` (calculated as `100 × (1 + 7.37%)^10`; raw endpoints not disclosed)
- Coverage/source note: official issuer calendar-year NAV TR rows are not disclosed in the reviewed capture. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed.

| Year | CNXT NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | 11.96% |
| 2017 | not disclosed | 21.83% |
| 2018 | not disclosed | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | not disclosed | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |

## Up years / Down years

- Up years / Down years: not disclosed because calendar-year NAV rows are not disclosed
- Best: not disclosed
- Least positive: not disclosed
- Worst: not disclosed
- Least bad down year: not disclosed
- 2021-2025 CAGR: not disclosed
- Current YTD: `16.05%` as of 2026-07-22; latest NAV `US$51.14` on the same date

## Risk read-through

CNXT มี 99 holdings ณ 2026-07-22 และเป็น China A-share/ChiNext exposure ที่มีความกระจุกตัวเชิง sector สูง โดย factsheet ณ 2026-06-30 ระบุ Information Technology `57.4%` และ Industrials `25.7%`. Net expense ratio คือ `0.65%` (gross `1.00%`); fee cap/waiver มีถึงอย่างน้อย 2027-05-01. Official issuer ระบุว่าข้อมูล index ก่อน market close 2021-12-10 สะท้อน SME-ChiNext 100 Index (CNI6109) และหลังจากนั้นสะท้อน ChiNext Index (SZ988107); ดังนั้น rolling 10-year figure คร่อม methodology/index change นี้. Daily NAV history สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official issuer product and performance page: https://www.vaneck.com/us/en/investments/chinext-innovators-etf-cnxt/
- Official issuer factsheet: https://www.vaneck.com/us/en/investments/chinext-innovators-etf-cnxt-fact-sheet.pdf/
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
