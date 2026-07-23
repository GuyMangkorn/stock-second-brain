---
type: etf-performance
instrument_type: ETF
entity_key: LSE:CSKR
ticker: CSKR
input_alias: CSKRF
exchange: London Stock Exchange
fund: iShares MSCI Korea UCITS ETF USD (Acc)
tracked_index: MSCI Korea 20/35 Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/CSKR
  - ticker/CSKRF
  - geography/South-Korea
---

# CSKR Performance

> Navigation: [[ETF Region Index]] → [[South Korea ETF]] → [[ETF Performance Index]]

## Bottom line

CSKRF เป็น OTC alias ของ iShares MSCI Korea UCITS ETF USD (Acc), canonical `LSE:CSKR`, ซึ่งเป็น physical/replicated passive equity ETF. Official iShares ระบุ rolling 10-year NAV Total Return cumulative `369.63%` และ CAGR `16.73%` ณ 2026-06-30 ครอบคลุม 10.00 elapsed years. Raw NAV TR endpoints ไม่ได้เปิดเผย; normalized start `100.00` และ end `469.63` ใช้ official cumulative return. Official calendar NAV TR rows 2016-2025 compound เป็น `141.88%` และ CAGR `9.23%`; common 2021-2025 compound เป็น `21.32%` และ CAGR `3.94%`. Current NAV YTD ล่าสุดคือ `70.53%` ณ 2026-07-21.

## Performance check

- input ticker: CSKRF (OTC alias)
- entity_key: LSE:CSKR
- Inception: 2010-08-24
- Metric: NAV Total Return with gross income reinvested where applicable
- Tracked index (issuer benchmark): MSCI Korea 20/35 Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR cumulative: `369.63%`; normalized TR start `100.00`, end `469.63`
- 10-year NAV TR CAGR: `16.73%` (official issuer annualized NAV return)
- Coverage/source note: official iShares calendar NAV TR rows 2016-2025 and benchmark rows are captured below. iShares states the benchmark changed from MSCI Korea Index to MSCI Korea 20/35 Index on 2020-02-11. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed.

| Year | CSKR NAV TR | MSCI Korea benchmark TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 8.0% | 8.7% | 11.96% |
| 2017 | 46.4% | 47.3% | 21.83% |
| 2018 | -21.4% | -20.9% | -4.38% |
| 2019 | 11.8% | 12.5% | 31.49% |
| 2020 | 43.5% | 44.7% | 18.40% |
| 2021 | -8.4% | -8.0% | 28.71% |
| 2022 | -29.2% | -29.0% | -18.11% |
| 2023 | 21.8% | 22.9% | 26.29% |
| 2024 | -22.9% | -22.5% | 25.02% |
| 2025 | 99.2% | 99.8% | 17.88% |

## Up years / Down years

- Up years / Down years: `6 / 4` over calendar years 2016-2025
- Best: 2025, `99.2%`
- Least positive: 2019, `11.8%`
- Worst: 2022, `-29.2%`
- Least bad down year: 2021, `-8.4%`
- Calendar 2016-2025 cumulative/CAGR: `141.88% / 9.23%`
- Common 2021-2025 cumulative/CAGR: `21.32% / 3.94%`; positive / negative `2 / 3`
- Current YTD: `70.53%` as of 2026-07-21; latest NAV `US$462.74` on the same date

## Risk read-through

CSKR มี 77 holdings ณ 2026-07-20 และ South Korea single-country exposure. Product structure เป็น physical, methodology replicated, use of income accumulating, และ total expense ratio `0.65%`. Standard deviation 3-year คือ `44.57%` ณ 2026-06-30; risk is concentrated in Korea, technology/semiconductor and currency. Official page also notes that one or more trading lines were delisted or cancelled on 2025-10-28; the London Stock Exchange USD line `CSKR` remains listed in the current listing table. Daily NAV history สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official iShares product and performance page: https://www.ishares.com/uk/professional/en/products/253733/cskr
- Official iShares factsheet: https://www.ishares.com/uk/professional/en/literature/fact-sheet/cskr-ishares-msci-korea-ucits-etf-usd-acc-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
