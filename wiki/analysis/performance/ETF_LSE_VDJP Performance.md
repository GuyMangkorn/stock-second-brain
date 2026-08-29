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
updated: 2026-08-29
performance_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
market_price_as_of: 2026-08-28
price_nav_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
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

VNFGF เป็น OTC alias ที่ resolve ได้เป็น Vanguard FTSE Japan UCITS ETF (USD) Distributing, canonical `LSE:VDJP`, ISIN `IE00B95PGT31`. กองทุนเป็น passive physical equity ETF ที่ติดตาม FTSE Japan Index. Official Vanguard factsheet ณ 2026-07-31 ระบุ rolling 10-year NAV Total Return CAGR `9.03%` สำหรับ 2016-08-01 ถึง 2026-07-31 หรือ 10.00 elapsed years. Raw NAV TR endpoints ไม่ได้เปิดเผย; normalized start `100.00` และ end ประมาณ `237.35` หรือ cumulative `137.35%` เป็นค่าที่คำนวณจาก CAGR ที่ issuer ปัดเศษ. Current official page แสดง NAV `US$52.30` และ market price `£38.65` ณ 2026-08-28 ขณะที่ standardized YTD ล่าสุดที่ยืนยันได้คือ `16.27%` ณ 2026-07-31.

## Performance check

- input ticker: VNFGF (OTC alias)
- entity_key: LSE:VDJP
- Inception: 2013-05-21; listing date 2013-05-22; ISIN `IE00B95PGT31`; USD LSE ticker `VDJP` (Bloomberg `VDJP LN`, Reuters `VDJP.L`)
- Metric: NAV Total Return including reinvested distributions and fund expenses; Vanguard states dividends and capital-gains distributions are reinvested and performance is NAV-to-NAV with gross income invested
- Tracked index (issuer benchmark): FTSE Japan Index
- Benchmark comparison: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-08-01 to 2026-07-31; actual years `10.00`
- 10-year NAV TR CAGR: `9.03%` (official Vanguard annualized NAV return)
- Normalized NAV TR: start `100.00`; end `237.35`, cumulative `137.35%` (calculated as `100 × (1 + 9.03%)^10`; raw endpoints not disclosed)
- Benchmark normalized reference: FTSE Japan Index annualized `9.17%`, normalized end `240.43`, cumulative `140.43%`; fund-minus-index is approximately `-3.09 pp` cumulative and `-0.14 pp` annualized.
- Current price snapshot: NAV `US$52.30` and market price `£38.65` at the 2026-08-28 close. These point-in-time prices are not substituted for standardized NAV total return.
- Coverage/source note: Vanguard publishes rolling 12-month NAV TR periods rather than complete calendar-year rows in the reviewed factsheet. The table below preserves the official August-July periods and does not relabel them as calendar years. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31 and are shown separately because their calendar window is not date-aligned with Vanguard's rolling periods.

| Official rolling 12-month period | VDJP NAV TR | FTSE Japan Index TR |
|---|---:|---:|
| 2016-08-01 to 2017-07-31 | 14.62% | 14.90% |
| 2017-08-01 to 2018-07-31 | 8.90% | 9.08% |
| 2018-08-01 to 2019-07-31 | -5.51% | -5.35% |
| 2019-08-01 to 2020-07-31 | 0.99% | 1.11% |
| 2020-08-01 to 2021-07-31 | 25.47% | 25.63% |
| 2021-08-01 to 2022-07-31 | -14.43% | -14.34% |
| 2022-08-01 to 2023-07-31 | 14.71% | 14.81% |
| 2023-08-01 to 2024-07-31 | 15.44% | 15.56% |
| 2024-08-01 to 2025-07-31 | 6.81% | 6.92% |
| 2025-08-01 to 2026-07-31 | 31.22% | 31.31% |

## S&P 500 Total Return reference

The S&P 500 rows below are the cached USD Total Return convention for complete calendar years 2016-2025. They are a directional reference, not a date-aligned substitute for the official August-July VDJP periods.

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

- VDJP rolling 10-year NAV TR CAGR: `9.03%` for 2016-08-01 to 2026-07-31; normalized cumulative `137.35%` is derived from the rounded issuer CAGR.
- S&P 500 calendar 2016-2025 cumulative/CAGR: `298.33% / 14.82%`; the comparison is directional because the windows and currency/market exposures differ.

## Up years / Down years

- Up rolling periods / Down rolling periods: `8 / 2`
- Best official rolling period: 2025-08-01 to 2026-07-31, `31.22%`
- Least positive official rolling period: 2019-08-01 to 2020-07-31, `0.99%`
- Worst official rolling period: 2021-08-01 to 2022-07-31, `-14.43%`
- Least bad down period: 2018-08-01 to 2019-07-31, `-5.51%`
- Calendar 2021-2025 CAGR: not disclosed; official rows are rolling August-July periods, not calendar years
- Latest standardized official YTD: `16.27%` as of 2026-07-31; current-page NAV `US$52.30` and market price `£38.65` as of 2026-08-28

## Risk read-through

VDJP มี Japan exposure `100.0%` และ 475 holdings ณ 2026-07-31. Sector exposures ได้แก่ Industrials `26.8%`, Financials `17.8%`, Consumer Discretionary `17.7%`, Technology `15.0%`, Health Care `5.1%`, Basic Materials `4.5%`, Consumer Staples `4.4%`, Telecommunications `4.0%`, Real Estate `2.7%`, Utilities `1.3%` และ Energy `0.9%`. Portfolio P/E คือ `16.6`, P/B `1.8`, ROE `10.2%`, earnings growth `16.8%`, median market cap `US$43.4B`; turnover `-20.4%` อ้างอิง 2026-06-30. Ongoing charges figure คือ `0.10%`; fund เป็น USD distributing share class จ่าย quarterly. Beta `0.99`, R-squared `1.00` และ annualized tracking error คือ `0.03%` 1Y, `0.47%` 3Y และ `0.36%` 5Y ณ 2026-07-31. ความเสี่ยงหลักคือ Japan/country/sector/FX และ tracking difference จาก fees, sampling, taxes และ trading costs. Daily NAV history สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official Vanguard product page: https://www.vanguard.co.uk/professional/product/etf/equity/9504/ftse-japan-ucits-etf-usd-distributing
- Official Vanguard factsheet: https://fund-docs.vanguard.com/FTSE_Japan_UCITS_ETF_USD_Distributing_9504_EU_INT_UK_EN.pdf
- Official Vanguard prospectus: https://fund-docs.vanguard.com/etf-prospectus-en.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
