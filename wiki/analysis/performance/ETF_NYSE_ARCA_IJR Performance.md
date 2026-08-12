---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IJR
ticker: IJR
exchange: NYSE Arca
fund: iShares Core S&P Small-Cap ETF
tracked_index: S&P SmallCap 600 Index
benchmark: S&P 500 Total Return
updated: 2026-08-12
performance_as_of: 2026-08-10
rolling_10y_as_of: 2025-12-31
current_ytd_as_of: 2026-08-10
price_nav_as_of: 2026-08-11
distribution_as_of: not disclosed
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-12.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IJR
  - geography/United-States
---

# IJR Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

IJR ให้ cumulative `NAV Total Return` `153.87%` หรือ CAGR `9.76%` ใน complete
calendar years 2016-2025 เทียบ S&P 500 TR `298.33%` / `14.82%`; เป็นบวก 8 ปี
และลบ 2 ปี. ปีดีที่สุดคือ 2021 `+26.69%`, แย่ที่สุดคือ 2022 `-16.20%`, และ
current NAV YTD คือ `+23.66%` ณ 10 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:IJR`
- Inception: 22 พ.ค. 2000; expense ratio: `0.06%` ณ 31 ก.ค. 2026
- Metric: `NAV Total Return` รวม reinvested dividends/distributions หลัง fund expenses; currency: USD
- Issuer benchmark: `S&P SmallCap 600 Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference)
- 10-year calendar-window calculation: official complete-year NAV TR rows from 2016-2025;
  cumulative `153.87%`, CAGR `9.76%` using `(Π(1 + annual TR))^(1 / 10) - 1`.
- Current quote: market price `US$148.41`, NAV `US$148.34`, calculated premium
  `0.05%` ณ 11 ส.ค. 2026
- Annual coverage: official complete years 2016-2025; ไม่มี `*` หรือ `†`.

| ปี | IJR NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 26.49% | 11.96% |
| 2017 | 13.20% | 21.83% |
| 2018 | -8.43% | -4.38% |
| 2019 | 22.79% | 31.49% |
| 2020 | 11.24% | 18.40% |
| 2021 | 26.69% | 28.71% |
| 2022 | -16.20% | -18.11% |
| 2023 | 16.03% | 26.29% |
| 2024 | 8.61% | 25.02% |
| 2025 | 5.95% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2021, `+26.69%`; least positive: 2025, `+5.95%`
- Worst: 2022, `-16.20%`; least bad down year: 2018, `-8.43%`
- 2021-2025 cumulative: IJR `41.75%`, CAGR `7.23%`; S&P 500 TR `96.17%`,
  CAGR `14.43%`
- Current YTD: IJR NAV `+23.66%` ณ 10 ส.ค. 2026

## Risk read-through

IJR เป็น passive U.S. small-cap equity แบบ representative sampling จึงมี
small-cap และ cyclicality sensitivity ชัด. Official three-year standard deviation
อยู่ที่ `19.36%` ณ 31 ก.ค. 2026; best quarter คือ `+31.29%` (ไตรมาสสิ้นสุด
31 ธ.ค. 2020) และ worst quarter คือ `-32.65%` (ไตรมาสสิ้นสุด 31 มี.ค. 2020).
Secondary inflation-adjusted dividend-reinvested history รายงาน maximum drawdown
`-58.94%` ณ 9 มี.ค. 2009 จาก peak 19 ก.ค. 2007; AssetsAnalyzer รายงานอีกวิธีเป็น
`-58.15%` และ 484 trading sessions ถึง recovery. Methodologies ต่างกัน จึงไม่
ใช้เป็น authoritative nominal NAV max-drawdown/recovery. Expense ratio อยู่ที่
`0.06%`.

## Sources

- [iShares IJR product page](https://www.ishares.com/us/products/239774/ishares-core-sp-smallcap-etf?fundSearch=true&qt=IJR)
- [iShares summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-core-s-and-p-small-cap-etf-3-31.pdf) | [official factsheet](https://www.ishares.com/us/literature/fact-sheet/ijr-ishares-core-s-p-small-cap-etf-fund-fact-sheet-en-us.pdf)
- [Total Real Returns](https://totalrealreturns.com/s/IJR) | [AssetsAnalyzer](https://assetsanalyzer.com/etf/IJR/performance) — secondary drawdown context only
- [[ETF_performance_sources_2026-08-12]] | [[ETF Performance Index]]
