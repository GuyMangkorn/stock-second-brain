---
type: etf-performance
instrument_type: ETF
entity_key: LSE:VDJP
ticker: VDJP
input_alias: VNFGF
exchange: London Stock Exchange
fund: Vanguard FTSE Japan UCITS ETF (USD) Distributing
tracked_index: FTSE Japan Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-05-31
current_ytd_as_of: 2026-05-31
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VDJP
  - ticker/VNFGF
  - geography/Japan
---

# VDJP Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

VNFGF เป็น OTC alias ที่ resolve ได้เป็น Vanguard FTSE Japan UCITS ETF (USD) Distributing, canonical `LSE:VDJP`, ISIN `IE00B95PGT31`. กองทุนเป็น passive physical equity ETF ที่ติดตาม FTSE Japan Index. Official Vanguard factsheet ระบุ rolling 10-year NAV Total Return CAGR `9.45%` สำหรับ 2016-06-01 ถึง 2026-05-31 หรือ 10.00 elapsed years. Raw NAV TR endpoints ไม่ได้เปิดเผย; normalized start `100.00` และ end ประมาณ `246.69` เป็นค่าที่คำนวณจาก CAGR ที่ issuer ปัดเศษ. Current page แสดง NAV `US$50.23` ณ 2026-07-22 แต่ standardized YTD ล่าสุดที่ยืนยันได้จาก official factsheet คือ `16.30%` ณ 2026-05-31.

## Performance check

- input ticker: VNFGF (OTC alias)
- entity_key: LSE:VDJP
- Inception: 2013-05-21; listing date 2013-05-22
- Metric: NAV Total Return including reinvested distributions and fund expenses; Vanguard states dividends and capital-gains distributions are reinvested and performance is NAV-to-NAV with gross income invested
- Tracked index (issuer benchmark): FTSE Japan Index
- Benchmark comparison: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-06-01 to 2026-05-31; actual years `10.00`
- 10-year NAV TR CAGR: `9.45%` (official Vanguard annualized NAV return)
- Normalized NAV TR: start `100.00`; end `246.69` (calculated as `100 × (1 + 9.45%)^10`; raw endpoints not disclosed)
- Coverage/source note: Vanguard publishes rolling 12-month NAV TR periods rather than complete calendar-year rows in the reviewed factsheet. The table below preserves the official periods and does not relabel them as calendar years. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31 and are shown separately because their calendar window is not date-aligned with Vanguard's June-May periods.

| Official rolling 12-month period | VDJP NAV TR | FTSE Japan Index TR |
|---|---:|---:|
| 2016-06-01 to 2017-05-31 | 15.56% | 15.76% |
| 2017-06-01 to 2018-05-31 | 14.79% | 14.94% |
| 2018-06-01 to 2019-05-31 | -10.92% | -10.74% |
| 2019-06-01 to 2020-05-31 | 6.92% | 7.06% |
| 2020-06-01 to 2021-05-31 | 24.81% | 24.97% |
| 2021-06-01 to 2022-05-31 | -13.73% | -13.64% |
| 2022-06-01 to 2023-05-31 | 4.48% | 4.57% |
| 2023-06-01 to 2024-05-31 | 17.73% | 17.85% |
| 2024-06-01 to 2025-05-31 | 11.48% | 11.59% |
| 2025-06-01 to 2026-05-31 | 32.20% | 32.31% |

## S&P 500 Total Return reference

The S&P 500 rows below are the cached USD Total Return convention for complete calendar years 2016-2025. They are a directional reference, not a date-aligned substitute for the official June-May VDJP periods.

| Calendar year | S&P 500 TR |
|---|---:|
| 2016 | 11.96% |
| 2017 | 21.83% |
| 2018 | -4.38% |
| 2019 | 31.49% |
| 2020 | 18.40% |
| 2021 | 28.71% |
| 2022 | -18.11% |
| 2023 | 26.29% |
| 2024 | 25.02% |
| 2025 | 17.88% |

- VDJP rolling 10-year NAV TR CAGR: `9.45%` for 2016-06-01 to 2026-05-31.
- S&P 500 calendar 2016-2025 cumulative/CAGR: `298.33% / 14.82%`; the CAGR comparison is directional because the windows differ.

## Up years / Down years

- Up rolling periods / Down rolling periods: `8 / 2`
- Best official rolling period: 2025-06-01 to 2026-05-31, `32.20%`
- Least positive official rolling period: 2022-06-01 to 2023-05-31, `4.48%`
- Worst official rolling period: 2021-06-01 to 2022-05-31, `-13.73%`
- Least bad down period: 2018-06-01 to 2019-05-31, `-10.92%`
- Calendar 2021-2025 CAGR: not disclosed; official rows are rolling June-May periods, not calendar years
- Latest standardized official YTD: `16.30%` as of 2026-05-31; current-page NAV `US$50.23` as of 2026-07-22

## Risk read-through

VDJP มี Japan exposure `100.0%` และ 476 holdings ณ 2026-06-30. Sector exposures ณ factsheet 2026-05-31 ได้แก่ Industrials `27.7%`, Consumer Discretionary `17.2%`, Financials `15.8%`, และ Technology `14.8%`. Ongoing charges figure คือ `0.10%`; fund เป็น USD distributing share class จ่าย quarterly. ความเสี่ยงหลักคือ Japan/country/sector/FX และ tracking difference จาก fees, sampling, taxes และ trading costs. Daily NAV history สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official Vanguard product page: https://www.vanguard.co.uk/professional/product/etf/equity/9504/ftse-japan-ucits-etf-usd-distributing
- Official Vanguard factsheet: https://fund-docs.vanguard.com/FTSE_Japan_UCITS_ETF_USD_Distributing_9504_EU_INT_UK_EN.pdf
- Official Vanguard prospectus: https://fund-docs.vanguard.com/etf-prospectus-en.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
