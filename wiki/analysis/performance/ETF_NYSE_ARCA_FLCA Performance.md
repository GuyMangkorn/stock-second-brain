---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLCA
ticker: FLCA
exchange: NYSE Arca
fund: Franklin FTSE Canada ETF
tracked_index: FTSE Canada Capped Index-NR
benchmark: S&P 500 Total Return
updated: 2026-07-13
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-06
price_nav_as_of: 2026-07-06
source_batch: raw/imports/ETF_performance_sources_2026-07-13.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FLCA
  - geography/Canada
---

# FLCA Performance

## Bottom line

FLCA ให้ `NAV Total Return` เป็นบวก 6 จาก 8 complete calendar years ในช่วง
2018-2025; การทบต้นจาก annual rows ให้ cumulative ประมาณ `127.81%` หรือ CAGR
`10.84%`. ปีดีที่สุดคือ 2025 ที่ `+34.90%` และแย่ที่สุดคือ 2018 ที่ `-15.80%`.
Current YTD ล่าสุดจาก issuer คือ `+8.17%` ณ 6 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:FLCA`
- Inception: 2 พ.ย. 2017
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Tracked index (issuer benchmark): `FTSE Canada Capped Index-NR`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ FLCA)
- 10-year NAV TR CAGR: `ไม่พบข้อมูลที่ยืนยันได้` เพราะกองทุนยังมีประวัติไม่ครบ 10 ปี
- Annual coverage: official complete calendar years 2018-2025; 2017 partial ไม่ได้
  แสดงเป็นตัวเลขใน factsheet จึงไม่รวมในการจัดอันดับ
- Since-inception NAV annualized return: `11.37%` ณ 30 มิ.ย. 2026

- Annual NAV TR coverage: 2016-2017 unavailable; 2018-2025 official NAV TR

| ปี | FLCA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | ไม่พบข้อมูลที่ยืนยันได้ | 11.96% |
| 2017 | ไม่พบข้อมูลที่ยืนยันได้ | 21.83% |
| 2018 | -15.80% | -4.38% |
| 2019 | 28.67% | 31.49% |
| 2020 | 5.91% | 18.40% |
| 2021 | 29.10% | 28.71% |
| 2022 | -11.95% | -18.11% |
| 2023 | 15.23% | 26.29% |
| 2024 | 12.36% | 25.02% |
| 2025 | 34.90% | 17.88% |

S&P 500 rows ใช้ cached official common-reference convention ณ 31 ธ.ค. 2025;
2026 YTD ไม่ใส่ในตารางเพราะยังไม่พบ S&P 500 TR snapshot ที่ยืนยันได้ในวันเดียวกับ
FLCA YTD.

## Up years / Down years

- Up years / Down years: `6 / 2` ใน 2018-2025
- Best: 2025, `+34.90%`
- Least positive: 2023, `+15.23%`
- Worst: 2018, `-15.80%`
- Least bad down year: 2022, `-11.95%`
- 2021-2025 cumulative / CAGR: `98.54%` / `14.70%`
- Current YTD: `+8.17%` NAV ณ 6 ก.ค. 2026; NAV `US$51.83` ในวันเดียวกัน

## Risk read-through

FLCA เป็น passive, indexed, single-country Canada equity ETF. Official 3-year NAV
standard deviation อยู่ที่ `13.77%` ณ 30 มิ.ย. 2026. โครงสร้าง sector ล่าสุดยัง
กระจุกใน Financials, Energy และ Materials; จึงมี country, commodity และ FX
sensitivity. Expense ratio คือ `0.09%` gross/net และจ่าย distribution แบบ
semi-annual. Max drawdown และ recovery period ยัง `ไม่พบข้อมูลที่ยืนยันได้` จาก
issuer; ไม่คำนวณจาก annual table เพราะข้อมูลรายปีไม่เห็น intra-year drawdown.

## Driver notes

- `Observed`: 2025 เป็นปีเด่นสุดในชุดข้อมูลที่ยืนยันได้ (`+34.90%`).
- `Observed`: 2022 ติดลบ `-11.95%` แต่ขาดทุนน้อยกว่า S&P 500 TR ที่ `-18.11%`.
- `Structural`: ผลตอบแทนสะท้อน Canada equity exposure และ sector mix ของดัชนี
  FTSE Canada Capped; ไม่ใช่ crisis hedge.

## Sources

- [Franklin Templeton FLCA product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26364/SINGLCLASS/franklin-ftse-canada-etf/FLCA) — identity, exchange, inception, benchmark, expense ratio, current NAV/YTD, distribution frequency, and classification
- [Franklin Templeton FLCA factsheet](https://www.franklintempleton.com/forms-literature/download/FLCA-FF) — official NAV calendar-year returns, since-inception return, and 3-year standard deviation; as of 2026-06-30
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference index identity
- [S&P U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — cached S&P 500 TR reference through 2025
