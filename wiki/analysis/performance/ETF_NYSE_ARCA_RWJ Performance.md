---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:RWJ
ticker: RWJ
exchange: NYSE Arca
fund: Invesco S&P SmallCap 600 Revenue ETF
tracked_index: S&P SmallCap 600 Revenue-Weighted Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-08-14
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-14
price_nav_as_of: not disclosed
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return where official; secondary dividend-reinvested proxy for annual/current fields
tags:
  - analysis/etf-performance
  - ticker/RWJ
  - geography/United-States
---

# RWJ Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

RWJ เป็น passive/index-tracking U.S. small-cap equity ETF ที่ติดตาม S&P SmallCap 600 Revenue-Weighted Index โดย Invesco ระบุว่ากองทุนลงทุนอย่างน้อย 90% ในองค์ประกอบของดัชนีและใช้ revenue weighting. Official SEC prospectus รายงาน average annual total return ของกองทุน `10.33%` สำหรับ 10 ปีสิ้นสุด 2024-12-31. ตาราง annual 2016-2025 และ current YTD ในหน้านี้ใช้ secondary dividend-reinvested total-return proxy เพราะไม่พบ official NAV calendar series/current NAV YTD ที่สอดคล้องกันใน capture เดียวกัน.

## Performance check

- entity_key: NYSE Arca:RWJ
- Inception: 2008-02-19
- Metric: Total Return with distributions reinvested; official SEC average annual return is net of fund expenses, while rows marked `*` are secondary dividend-reinvested proxy observations
- Tracked index (issuer benchmark): S&P SmallCap 600 Revenue-Weighted Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- Expense ratio: `0.39%` (official Invesco summary prospectus)
- 2016-2025 calendar total-return proxy: cumulative `215.92%`; rounded-input CAGR `12.19%`
- 2021-2025 calendar total-return proxy: cumulative `90.51%`; rounded-input CAGR `13.76%`
- Official issuer average annual total return: `10.33%` for the period ended 2024-12-31; this is a separate issuer window and is not relabelled as the 2016-2025 proxy CAGR
- Current total-return proxy YTD: `28.61%` as of 2026-08-14; a separate ETFRC standardized snapshot reports `25.7%` as of 2026-07-31 and is not mixed because the as-of dates and capture differ

| Year | RWJ TR* | S&P 500 TR |
|---|---:|---:|
| 2016 | 30.72% | 11.96% |
| 2017 | 5.09% | 21.83% |
| 2018 | -16.95% | -4.38% |
| 2019 | 20.29% | 31.49% |
| 2020 | 20.83% | 18.40% |
| 2021 | 52.83% | 28.71% |
| 2022 | -10.97% | -18.11% |
| 2023 | 16.22% | 26.29% |
| 2024 | 11.81% | 25.02% |
| 2025 | 7.75% | 17.88% |

`*` RWJ rows are a secondary dividend-reinvested proxy from TotalRealReturns, not official NAV rows. S&P 500 rows reuse the project’s cached USD total-return convention for complete calendar years 2016-2025.

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016-2025
- Best: 2021, `52.83%*`
- Least positive: 2017, `5.09%*`
- Worst: 2018, `-16.95%*`
- Least bad down year: 2022, `-10.97%*`
- 2016-2025 rounded-input CAGR: `12.19%*`; 2021-2025 rounded-input CAGR: `13.76%*`
- Current YTD total-return proxy: `28.61%*` as of 2026-08-14; common S&P 500 current cross-check `10.14%` as of 2026-07-31 is not same-date and is not used as a synchronized spread

## Risk read-through

RWJ เป็น small-cap revenue-weighted exposure จึงมี small-cap, cyclicality, liquidity และ concentration risk. Official prospectus ระบุความเสี่ยงจากบริษัทขนาดเล็กและการกระจุกตัวของกลุ่มอุตสาหกรรม/consumer discretionary. Secondary total-return history reports maximum drawdown `-45.04%` เมื่อ 2020-03-18 จาก peak 2019-12-26; recovery date ไม่ได้เปิดเผยใน source. ณ 2026-08-14 drawdown ปัจจุบันอยู่ที่ `-0.83%` จาก peak 2026-08-04. Annual-row sample standard deviation จากค่าที่ปัดเศษคือ `19.95%`; ไม่ใช่ daily NAV volatility.

## Driver notes

- Confirmed structure: passive full-replication exposure to the S&P SmallCap 600 Revenue-Weighted Index; revenue weighting can create factor and sector tilts relative to market-cap-weighted small-cap benchmarks.
- Observed regime points: 2021 was the strongest complete year at `+52.83%*`, while 2018 was the weakest at `-16.95%*`. These are return observations, not causal event attribution.
- Benchmark context: official issuer benchmark is the S&P SmallCap 600 Revenue-Weighted Index; S&P 500 TR is retained only as a common large-cap reference and should not be read as RWJ’s tracking benchmark.

## Sources

- [SEC RWJ summary prospectus](https://www.sec.gov/Archives/edgar/data/1378872/000119312525325669/d54028d497k.htm) — fund identity, NYSE Arca listing, objective, index, expense ratio, passive treatment, risks, inception, and official average annual total returns through 2024-12-31
- [Invesco RWJ factsheet](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/rwj-invesco-s-p-smallcap-600-revenue-etf-fact-sheet.pdf) — official product/factsheet entry point and fund identity
- [TotalRealReturns RWJ comparison](https://totalrealreturns.com/n/AVUV%2CRWJ%2CXSVM) — secondary dividend-reinvested annual rows, current YTD, rolling returns, and drawdown proxy through 2026-08-14
- [ETF Research Center RWJ profile](https://www.etfrc.com/RWJ) — secondary standardized performance and expense snapshot through 2026-07-31
- [Slickcharts S&P 500 YTD total return](https://www.slickcharts.com/sp500/returns/ytd) — secondary current benchmark cross-check through 2026-07-31
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as-of 2025-12-31
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
