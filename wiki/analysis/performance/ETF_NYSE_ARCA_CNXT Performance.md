---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:CNXT
ticker: CNXT
exchange: NYSE Arca
fund: VanEck ChiNext Innovators ETF
tracked_index: ChiNext Index (SZ988107)
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-08-28
performance_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/CNXT
  - geography/China
---

# CNXT Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

CNXT เป็น passive/index-tracking China A-share equity ETF ที่พยายามติดตาม
ChiNext Index (SZ988107). Latest official VanEck factsheet ณ 2026-07-31
รายงาน NAV Total Return YTD `8.45%`, rolling 1-year `55.19%`, 3-year
annualized `18.06%`, 5-year annualized `-0.09%` และ 10-year annualized
`4.80%`. ช่วง 10-year คือ 2016-07-31 ถึง 2026-07-31 ครบ `10.00` elapsed
years. Raw start/end TR values ไม่ได้เปิดเผย; ค่า normalized end `159.81` จาก
start `100.00` และ cumulative `59.81%` เป็นค่าที่คำนวณจาก CAGR ที่ issuer
ปัดเศษ ไม่ใช่ official endpoint. Calendar-year NAV rows ของกองทุนไม่ถูก
เปิดเผยใน capture นี้ จึงไม่จัดอันดับ best/worst หรือคำนวณ 2021-2025 CAGR.

## Performance check

- entity_key: NYSE Arca:CNXT
- Inception: 2014-07-23
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index (issuer benchmark): ChiNext Index (SZ988107)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-07-31 to 2026-07-31; actual years `10.00`
- 10-year NAV TR CAGR: `4.80%` (official issuer average annual total return)
- Normalized NAV TR: start `100.00`; end `159.81` (calculated as `100 × (1 + 4.80%)^10`; raw endpoints not disclosed)
- Coverage/source note: official issuer calendar-year NAV TR rows are not disclosed in the reviewed capture. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed.
- Latest official month-end fields as of `2026-07-31`: NAV TR 1-month `-23.56%`, 3-month `-8.60%`, YTD `8.45%`, 1-year `55.19%`, 3-year annualized `18.06%`, 5-year annualized `-0.09%`, 10-year annualized `4.80%`, and since ETF inception `6.52%`.

| Window ended 2026-07-31 | CNXT NAV TR | ChiNext Index | Difference |
|---|---:|---:|---:|
| 1-month | -23.56% | -22.49% | -1.07 pp |
| 3-month | -8.60% | -7.53% | -1.07 pp |
| YTD | 8.45% | 8.78% | -0.33 pp |
| 1-year | 55.19% | 54.54% | +0.65 pp |
| 3-year annualized | 18.06% | 17.93% | +0.13 pp |
| 5-year annualized | -0.09% | -0.01% | -0.08 pp |
| 10-year annualized | 4.80% | 6.17% | -1.37 pp |
| Since ETF inception | 6.52% | 8.19% | -1.67 pp |

The ChiNext Index returns are before fund fees and expenses; the differences are
tracking/fee comparisons, not alpha.

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
- Current NAV TR YTD: `8.45%` as of 2026-07-31; latest share-price/NAV snapshot captured in the prior official source was `US$51.14` on 2026-07-22, and a 2026-07-31 NAV quote was not disclosed in the reviewed factsheet

## Risk read-through

CNXT มี 99 holdings และ net assets `$102.75m` ณ 2026-07-31 และเป็น China
A-share/ChiNext exposure ที่มีความกระจุกตัวเชิง sector สูง โดย factsheet ล่าสุด
ระบุ Information Technology `48.2%` และ Industrials `29.6%`. Net expense ratio
คือ `0.65%` (gross `1.00%`); fee cap/waiver มีถึง 2027-05-01. Official issuer
ระบุว่าข้อมูล index ก่อน market close 2021-12-10 สะท้อน SME-ChiNext 100 Index
(CNI6109) และหลังจากนั้นสะท้อน ChiNext Index (SZ988107); ดังนั้น rolling
10-year figure คร่อม methodology/index change นี้. Daily NAV history สำหรับ
max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official issuer product and performance page: https://www.vaneck.com/us/en/investments/chinext-innovators-etf-cnxt/
- Official issuer factsheet: https://www.vaneck.com/us/en/investments/chinext-innovators-etf-cnxt-fact-sheet.pdf/
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-28]] | [[ETF Performance Index]]
