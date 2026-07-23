---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VPL
ticker: VPL
exchange: NYSE Arca
fund: Vanguard FTSE Pacific ETF
tracked_index: FTSE Developed Asia Pacific All Cap Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-05-31
current_ytd_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VPL
  - geography/Asia-Pacific
---

# VPL Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

VPL เป็น passive/index-tracking equity ETF ของ Vanguard ที่ติดตาม FTSE
Developed Asia Pacific All Cap Index. Official rolling NAV Total Return 10 ปี
ณ 2026-05-31 อยู่ที่ cumulative `177.37%` และ CAGR `10.74%` จาก normalized TR
100.00 เป็น 277.37 ใน 10.00 ปี. Annual NAV TR แบบ calendar year 2016-2025
compound ได้ `114.60%` หรือ CAGR `7.94%`; common window 2021-2025 ได้ CAGR
`6.05%` เทียบกับ S&P 500 TR `14.43%`. Current NAV TR YTD ล่าสุดที่ยืนยันได้
จาก Vanguard คือ `19.62%` ณ 2026-07-17.

## Performance check

- entity_key: NYSE Arca:VPL
- Inception: 2005-03-04
- Metric: NAV Total Return รวม reinvested dividends/capital-gains distributions และ net of fund expenses
- Tracked index (issuer benchmark): FTSE Developed Asia Pacific All Cap Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year window: 2016-05-31 to 2026-05-31
- 10-year NAV TR CAGR: 10.74%; start TR value 100.00 and end TR value 277.37 เป็น normalized levels จาก official cumulative return; actual years 10.00
- Formula: (277.37 / 100.00)^(1 / 10.00) - 1 = 10.74%
- Calendar-row calculation: official rows 2016-2025 compound to 114.60% and CAGR 7.94%; rows 2021-2025 compound to 34.15% and CAGR 6.05%
- Coverage/source note: rolling return is as of 2026-05-31; annual rows are as of 2025-12-31; current YTD is as of 2026-07-17. Raw NAV endpoint levels are not disclosed.

| Year | VPL NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 5.31% | 11.96% |
| 2017 | 28.60% | 21.83% |
| 2018 | -13.85% | -4.38% |
| 2019 | 17.61% | 31.49% |
| 2020 | 16.58% | 18.40% |
| 2021 | 1.51% | 28.71% |
| 2022 | -15.21% | -18.11% |
| 2023 | 15.58% | 26.29% |
| 2024 | 1.27% | 25.02% |
| 2025 | 33.16% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ VPL;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31.

## Up years / Down years

- Up years / Down years: 8 / 2
- Best: 2025, +33.16%
- Least positive: 2024, +1.27%
- Worst: 2018, -13.85%
- Least bad down year: 2022, -15.21%
- Current YTD: +19.62% as of 2026-07-17

## Risk read-through

VPL กระจายหุ้น Pacific developed markets แต่ยังมี country, currency และ
sector concentration; factsheet ณ 2026-06-30 ระบุ Japan 52.9%, Korea 25.7%
และ Australia 14.1% ของ common-stock exposure. Expense ratio อยู่ที่ 0.07%
และ 3-year standard deviation 16.27% ณ 2026-06-30. Daily NAV history สำหรับ
การคำนวณ max drawdown และ recovery: ไม่พบข้อมูลที่ยืนยันได้ใน lean capture.

## Sources

- Official issuer product and performance page:
  https://investor.vanguard.com/investment-products/etfs/profile/vpl
- Official issuer factsheet (as of 2026-06-30):
  https://fund-docs.vanguard.com/F0962.pdf
- Official Vanguard Advisors performance page (current YTD as of 2026-07-17):
  https://advisors.vanguard.com/investments/products/vpl/vanguard-ftse-pacific-etf
- Official S&P 500 index page:
  https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
