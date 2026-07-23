---
type: etf-performance
instrument_type: ETF
entity_key: LSE:VDPX
ticker: VGUDF
input_alias: VGUDF
exchange: London Stock Exchange
fund: Vanguard FTSE Developed Asia Pacific ex Japan UCITS ETF (USD) Distributing
tracked_index: FTSE Developed Asia Pacific ex Japan Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-03-31
current_ytd_as_of: not disclosed
latest_nav_as_of: 2026-07-20
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VGUDF
  - ticker/VDPX
  - geography/Asia-Pacific
---

# VGUDF Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

VGUDF เป็น OTC alias ที่ resolve ได้เป็น Vanguard FTSE Developed Asia Pacific ex
Japan UCITS ETF (USD) Distributing, canonical `LSE:VDPX`, ISIN `IE00B9F5YL18`.
กองทุนเป็น passive, physical, index-tracking equity ETF ที่ติดตาม FTSE
Developed Asia Pacific ex Japan Index. Official Vanguard factsheet ให้ 10-year
NAV Total Return CAGR `8.80%` สำหรับ 2016-03-31 ถึง 2026-03-31 หรือ `10.00`
elapsed years; normalized TR 100.00 เป็น 232.43 จาก CAGR ที่ issuer ปัดเศษ.
Current NAV TR YTD ยังเป็น `ไม่พบข้อมูลที่ยืนยันได้` จาก official capture ที่
ตรวจทาน; latest official NAV ที่พบคือ US$42.5244 ณ 2026-07-20.

## Performance check

- input ticker: VGUDF (OTC alias)
- entity_key: LSE:VDPX
- Inception: 2013-05-21; listing date 2013-05-22
- Metric: NAV Total Return including reinvested distributions and fund expenses; Vanguard states performance is NAV-to-NAV with gross income invested and distributions/capital gains reinvested
- Tracked index (issuer benchmark): FTSE Developed Asia Pacific ex Japan Index
- Benchmark comparison: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-03-31 to 2026-03-31; actual years `10.00`
- 10-year NAV TR CAGR: `8.80%` (official Vanguard annualized NAV return)
- Normalized NAV TR: start `100.00`; end `232.43` (calculated as `100 × (1 + 8.80%)^10`; raw NAV endpoints are not disclosed)
- Calendar-row calculation: official 2016-2025 rows compound to `122.03%` / CAGR `8.30%`; official 2021-2025 rows compound to `30.23%` / CAGR `5.42%`
- Coverage/source note: official factsheet calendar rows are as of 2025-12-31; rolling 10-year summary is as of 2026-03-31; latest NAV is as of 2026-07-20. Current YTD NAV TR is not disclosed in the reviewed official capture.

| Year | VGUDF / VDPX NAV TR | FTSE Developed Asia Pacific ex Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 8.49% | 8.62% | 11.96% |
| 2017 | 32.21% | 32.41% | 21.83% |
| 2018 | -14.37% | -14.23% | -4.38% |
| 2019 | 16.97% | 17.09% | 31.49% |
| 2020 | 18.67% | 18.59% | 18.40% |
| 2021 | 1.05% | 1.25% | 28.71% |
| 2022 | -12.65% | -12.62% | -18.11% |
| 2023 | 11.00% | 11.03% | 26.29% |
| 2024 | -5.67% | -5.59% | 25.02% |
| 2025 | 40.91% | 40.99% | 17.88% |

S&P 500 rows use the cached USD Total Return convention for complete calendar
years 2016-2025, with dividends reinvested and reference as-of `2025-12-31`.
This is a common comparison benchmark, not VDPX's tracked index.

## Common-window comparison

- VDPX 2021-2025 NAV TR CAGR: `5.42%`
- S&P 500 2021-2025 TR CAGR: `14.43%`
- VDPX trails by approximately `9.00 pp` CAGR in the common calendar window.
- Up years / Down years in 2021-2025: `4 / 1`
- Best year: 2025, `40.91%`; worst year: 2022, `-12.65%`
- Current standardized NAV TR YTD: `ไม่พบข้อมูลที่ยืนยันได้`; latest official NAV: `US$42.5244` as of 2026-07-20

## Risk read-through

VDPX มี developed Asia-Pacific ex-Japan exposure โดย official portfolio data ณ
2026-06-30 มี 376 holdings; South Korea `54.80%`, Australia `29.47%`, Hong Kong
`8.31%`, Singapore `6.49%`, และ New Zealand `0.92%`. Ongoing Charges Figure คือ
`0.15%` และจ่าย distribution รายไตรมาส. ความเสี่ยงหลักคือ country, sector,
currency และ semiconductor/technology concentration จาก Korea รวมถึง tracking
difference จาก fees, taxes, sampling และ trading costs. Daily NAV history ที่
ยืนยันได้เพียงพอสำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official Vanguard product and performance page: https://www.vanguard.co.uk/professional/product/etf/equity/9522/ftse-developed-asia-pacific-ex-japan-ucits-etf-usd-distributing
- Official Vanguard factsheet: https://fund-docs.vanguard.com/FTSE_Developed_Asia_Pacific_ex_Japan_UCITS_ETF_USD_Distributing_9522_EU_INT_UK_EN.pdf?management-style=Index
- OTC alias cross-check: https://www.schwab.wallst.com/schwab/Prospect/charts/interactive/popup.asp?symbol=VGUDF
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
