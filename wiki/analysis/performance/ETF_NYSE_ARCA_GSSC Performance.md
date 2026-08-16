---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:GSSC
ticker: GSSC
exchange: NYSE Arca
fund: Goldman Sachs ActiveBeta U.S. Small Cap Equity ETF
tracked_index: Goldman Sachs ActiveBeta U.S. Small Cap Equity Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-07-27
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/GSSC
  - geography/United-States
---

# GSSC Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

GSSC เป็น Goldman Sachs ActiveBeta U.S. Small Cap Equity ETF แบบ
passive/index-tracking ที่ใช้ multi-factor index บน NYSE Arca. Official
2018-2025 NAV Total Return ให้ cumulative `93.95%` และ rounded-input CAGR
`8.63%` โดยมี 6 up years / 2 down years; current official NAV TR YTD คือ
`21.33%` ณ 2026-06-30. ใน common 2021-2025 window กองทุนให้ CAGR `8.25%`
ต่ำกว่า S&P 500 Total Return `14.43%`.

## Performance check

- entity_key: `NYSE Arca:GSSC`
- Inception: 2017-06-28
- Expense ratio: 0.20%
- Metric: `NAV Total Return` รวม reinvested dividends/distributions และ fund expenses; USD
- Tracked index (issuer benchmark): Goldman Sachs ActiveBeta U.S. Small Cap Equity Index
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR: `not applicable (<10 years)` ณ 2026-06-30; official since-inception annualized NAV TR `10.86%` เป็นคนละ metric กับ 10-year CAGR
- Common calendar window: official complete 2018-2025; cumulative `93.95%` / rounded-input CAGR `8.63%`
- 2021-2025 cumulative `48.66%` / CAGR `8.25%`; S&P 500 cached 2021-2025 cumulative `96.17%` / CAGR `14.43%`
- Coverage/source note: 2017 เป็น inception-year partial และไม่รวมใน ranking; annual rows 2018-2025 เป็น official issuer NAV TR. S&P 500 rows ใช้ cached USD Total Return convention as of 2025-12-31.

| Year | GSSC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -8.72% | -4.38% |
| 2019 | 23.43% | 31.49% |
| 2020 | 15.80% | 18.40% |
| 2021 | 24.05% | 28.71% |
| 2022 | -16.87% | -18.11% |
| 2023 | 17.37% | 26.29% |
| 2024 | 10.94% | 25.02% |
| 2025 | 10.71% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ GSSC;
annual rows ใช้ cached USD Total Return convention และไม่ได้ผสมกับ NAV/market-price
return ของ GSSC.

## Up years / Down years

- Up years / Down years: 6 / 2 in the complete 2018-2025 window
- Best: 2021, +24.05%
- Least positive: 2025, +10.71%
- Worst: 2022, -16.87%
- Least bad down year: 2018, -8.72%
- Current GSSC NAV TR YTD: +21.33% as of 2026-06-30

## Risk read-through

GSSC มี small-cap และ multi-factor exposure จึงยังมี cyclicality, liquidity และ
factor-regime risk แม้ index จะใช้ value, momentum, quality และ low volatility.
SEC summary prospectus ระบุ best quarter `+29.24%` ใน 4Q2020 และ worst quarter
`-30.94%` ใน 1Q2020; official daily NAV history สำหรับคำนวณ max drawdown และ
recovery ยังไม่พบข้อมูลที่ยืนยันได้. Expense ratio `0.20%` สะท้อนต้นทุนกองทุนใน
NAV Total Return แล้ว.

## Sources

- [Official Goldman Sachs GSSC product/fact card](https://am.gs.com/public-assets/documents/574deb07-24d6-11ef-870d-c7a1cb19e681)
- [SEC GSSC summary prospectus](https://www.sec.gov/Archives/edgar/data/1479026/000119312525334837/d72082d497k.htm)
- [SEC GSSC semi-annual shareholder report](https://www.sec.gov/Archives/edgar/data/1479026/000119312526206736/d120512dncsrs.htm)
- [ETF Central GSSC secondary snapshot](https://www.etfcentral.com/fund/GSSC) (price/NAV context only; not used in NAV TR ranking)
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- [S&P 500 historical reference](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true)
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
