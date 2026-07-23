---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLTW
ticker: FLTW
exchange: NYSE Arca
fund: Franklin FTSE Taiwan ETF
tracked_index: FTSE Taiwan Capped Index-NR
benchmark: S&P 500 Total Return
updated: 2026-07-23
performance_as_of: 2026-07-10
annual_rows_as_of: 2026-03-31
current_ytd_as_of: 2026-07-10
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
primary_region: Taiwan
tags:
  - analysis/etf-performance
  - ticker/FLTW
  - geography/Taiwan
---

# FLTW Performance

> Navigation: [[ETF Region Index]] → [[Taiwan ETF]] → [[ETF Performance Index]]

## Bottom line

FLTW เป็น indexed/passive Taiwan equity ETF ที่ติดตาม FTSE Taiwan Capped
Index-NR และจดทะเบียนที่ NYSE Arca. Official product page รายงาน current YTD
NAV Total Return `63.10%` ณ `2026-07-10`; official factsheet ให้ annual NAV TR
rows ครบ `2018-2025`. กองทุนเริ่มเมื่อ `2017-11-02` ทำให้ช่วงถึง `2026-06-30`
มีเพียง `8.66` ปี จึงยังไม่มี 10-year NAV TR.

## Performance check

- entity_key: `NYSE Arca:FLTW`
- Inception: `2017-11-02`
- Classification: passive, indexed, single-country Taiwan equity ETF
- Metric: NAV Total Return รวม reinvested distributions และหัก fund expenses
- Tracked index: `FTSE Taiwan Capped Index-NR`
- Expense ratio: `0.19%` as of `2025-08-01`
- Distribution frequency: semi-annual
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR: `unavailable (<10.00 elapsed years)`
- Available period test: `2017-11-02` to `2026-06-30`, actual elapsed `8.66` years; no 10-year proxy created
- Current YTD NAV TR: `63.10%` as of `2026-07-10`

| Year | FLTW NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -8.93% | -4.38% |
| 2019 | 30.89% | 31.49% |
| 2020 | 30.41% | 18.40% |
| 2021 | 29.72% | 28.71% |
| 2022 | -27.74% | -18.11% |
| 2023 | 29.78% | 26.29% |
| 2024 | 17.29% | 25.02% |
| 2025 | 31.91% | 17.88% |

Annual ETF rows are official NAV Returns from the Franklin factsheet as of
`2026-03-31`; returns assume reinvestment of distributions and deduction of
fund expenses. 2017 is excluded as an inception-year partial. S&P 500 rows use
the cached USD Total Return convention as of `2025-12-31`.

## Up years / Down years

Among the complete official FLTW rows for `2018-2025`:

- Up years / Down years: `6 / 2`
- Best: `2025 +31.91%`
- Least positive: `2024 +17.29%`
- Worst: `2022 -27.74%`
- Least bad down year: `2018 -8.93%`
- 2018-2025 cumulative return: `+192.58%`
- 2018-2025 annualized return: `14.36%` over `8` complete calendar years
- 2021-2025 cumulative return: `+88.21%`
- 2021-2025 annualized return: `13.48%` over `5` complete calendar years
- Current YTD: `63.10%` as of `2026-07-10`

Calendar-row CAGRs are calculated from rounded official annual inputs. They are
available-period calculations, not 10-year NAV TR CAGRs.

## Risk read-through

FLTW มี annual NAV TR ที่แข็งแรงในปี 2019-2021 และ 2023-2025 แต่มี downside
ชัดเจนใน 2018 และ 2022. Portfolio risk กระจุกตัวใน Taiwan และ Information
Technology; Franklin reports IT exposure `76.55%` as of `2026-07-10`. จึงไวต่อ
semiconductor cycle, Taiwan/China geopolitical risk, export cycle, valuation และ
currency. Official product page ระบุว่าผลตอบแทน NAV รวม reinvested distributions
และ fund expenses แล้ว. Daily NAV history ที่พอจะคำนวณ max drawdown และ recovery
อย่าง reproducible ยังเป็น `ไม่พบข้อมูลที่ยืนยันได้` ใน source ที่ใช้รอบนี้.

## Sources

- [Franklin FTSE Taiwan ETF product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26351/SINGLCLASS/franklin-ftse-taiwan-etf/FLTW) — fund identity, exchange, benchmark, inception, current NAV/YTD, expenses, classification and portfolio snapshot; YTD as of `2026-07-10`
- [Franklin FLTW factsheet](https://www.franklintempleton.com/forms-literature/download/FLTW-FF) — official NAV Returns and calendar-year rows `2018-2025`; factsheet as of `2026-03-31`
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention — common USD total-return reference
- ETF source batch: [[ETF_performance_sources_2026-07-23]] | [[ETF Performance Index]]
