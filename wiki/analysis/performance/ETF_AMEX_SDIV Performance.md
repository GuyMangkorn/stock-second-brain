---
type: etf-performance
entity_key: NYSE Arca:SDIV
updated: 2026-07-14
return_basis: NAV total return
tags:
  - analysis/etf-performance
---

# SDIV Performance

## Bottom line

official calendar-year NAV Total Return ยังไม่ครบ จึงไม่จัดอันดับ common-window; ใช้ rolling return ที่ issuer เปิดเผยแยกต่างหาก.

## Performance check

- `entity_key: NYSE Arca:SDIV`
- Fund: Global X SuperDividend ETF
- Inception: `2011-06-08`; expense ratio: `0.58%`
- Metric: `NAV Total Return` รวม distributions reinvested และ fund expenses
- Issuer benchmark: Solactive Global SuperDividend Index
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested)
- 10-year NAV TR CAGR: `0.13%` as of `2025-12-31` (official rolling issuer figure)
- Coverage/source note: prospectus chart captured but year-label mapping was not machine-verifiable

- Annual NAV TR coverage: 2016-2025 official calendar NAV TR rows not exposed; rolling 10Y CAGR retained

| ปี | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | ไม่พบข้อมูลที่ยืนยันได้ | 11.96% |
| 2017 | ไม่พบข้อมูลที่ยืนยันได้ | 21.83% |
| 2018 | ไม่พบข้อมูลที่ยืนยันได้ | -4.38% |
| 2019 | ไม่พบข้อมูลที่ยืนยันได้ | 31.49% |
| 2020 | ไม่พบข้อมูลที่ยืนยันได้ | 18.40% |
| 2021 | ไม่พบข้อมูลที่ยืนยันได้ | 28.71% |
| 2022 | ไม่พบข้อมูลที่ยืนยันได้ | -18.11% |
| 2023 | ไม่พบข้อมูลที่ยืนยันได้ | 26.29% |
| 2024 | ไม่พบข้อมูลที่ยืนยันได้ | 25.02% |
| 2025 | ไม่พบข้อมูลที่ยืนยันได้ | 17.88% |

**Up years / Down years**

- Best: ไม่พบข้อมูลที่ยืนยันได้; least positive: ไม่พบข้อมูลที่ยืนยันได้
- Worst: ไม่พบข้อมูลที่ยืนยันได้; least bad down year: ไม่พบข้อมูลที่ยืนยันได้
- Current YTD: `5.50%` as of `2026-07-10`

## Risk read-through

ข้อจำกัดหลักคือ calendar-year NAV Total Return ไม่ครบ จึงยังประเมิน upside/downside รายปีอย่างเทียบเท่าไม่ได้. กองเป็น passive index-tracking equity ETF; ผลลัพธ์จึงอ่านเป็นคุณภาพของ index methodology, implementation และ cost drag. Classification: `global high-dividend equity`. อย่าใช้ CAGR อย่างเดียวตัดสินความเสี่ยง โดยเฉพาะ sector/country-concentrated funds.

## Sources

- [Official issuer product/performance source](https://www.globalxetfs.com/funds/SDIV)
- Benchmark convention and cached 2016-2025 rows: [[ETF_performance_sources_2026-07-14]]
