---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EPI
ticker: EPI
exchange: NYSE Arca
fund: WisdomTree India Earnings Fund
tracked_index: WisdomTree India Earnings Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EPI
  - geography/India
---

# EPI Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

EPI เป็น passive/index-tracking India equity ETF ที่ติดตาม WisdomTree India Earnings Index. Official rolling 10-year NAV Total Return CAGR คือ `9.18%` สำหรับ `2016-06-30` ถึง `2026-06-30` (`10.00` elapsed years); raw start/end TR values และ raw cumulative return ไม่ได้เปิดเผย. Official calendar NAV TR rows `2016-2025` compound เป็น `163.67%` / CAGR `10.18%`. Current NAV TR YTD คือ `-7.91%` ณ `2026-06-30`.

## Performance check

- entity_key: `NYSE Arca:EPI`
- Inception: `2008-02-22`
- Metric: NAV Total Return including reinvested distributions and fund expenses; WisdomTree states total returns use the daily 4:00pm NAV
- Tracked index: WisdomTree India Earnings Index; earnings-weighted exposure to profitable Indian companies
- Official 10-year window: start date `2016-06-30`; end date `2026-06-30`; actual years `10.00`; start TR value `not disclosed`; end TR value `not disclosed`; official CAGR `9.18%`
- Implied cumulative return from the official CAGR is approximately `140.67%`; this is a shown calculation, not a substitute for undisclosed raw endpoints
- Official issuer-index rolling 10-year NAV-equivalent reference: `11.35%` as of `2026-06-30`; annual WisdomTree India Earnings Index rows were not disclosed in the reviewed official capture
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not the issuer benchmark)

| Year | EPI NAV TR | WisdomTree India Earnings Index TR | MSCI India TR | S&P 500 TR |
|---|---:|---:|---:|---:|
| 2016 | 2.24% | not disclosed | -1.43% | 11.96% |
| 2017 | 39.03% | not disclosed | 38.75% | 21.83% |
| 2018 | -10.44% | not disclosed | -7.30% | -4.38% |
| 2019 | 1.70% | not disclosed | 7.58% | 31.49% |
| 2020 | 18.07% | not disclosed | 15.55% | 18.40% |
| 2021 | 28.02% | not disclosed | 26.23% | 28.71% |
| 2022 | -5.72% | not disclosed | -7.95% | -18.11% |
| 2023 | 26.31% | not disclosed | 20.81% | 26.29% |
| 2024 | 11.11% | not disclosed | 11.21% | 25.02% |
| 2025 | 1.83% | not disclosed | 2.62% | 17.88% |

EPI annual NAV TR rows and MSCI India reference rows are from WisdomTree's official Q1 2026 presentation; annual WisdomTree India Earnings Index rows were not disclosed in the reviewed official capture. S&P 500 rows reuse the cached USD Total Return convention for complete calendar years `2016-2025`.

## Window calculations

- Official rolling 10-year EPI NAV TR: CAGR `9.18%`; implied cumulative from CAGR `140.67%` (raw cumulative and raw endpoints not disclosed)
- 2016-2025 EPI NAV TR: cumulative `163.67%` / CAGR `10.18%`; S&P 500 TR: cumulative `298.33%` / CAGR `14.82%`; EPI trails by approximately `4.64 pp` CAGR
- 2021-2025 EPI NAV TR: cumulative `72.49%` / CAGR `11.52%`; S&P 500 TR: cumulative `96.17%` / CAGR `14.43%`; EPI trails by approximately `2.91 pp` CAGR
- Up years / down years: `8 / 2`
- Best year: `2017`, `39.03%`; worst year: `2018`, `-10.44%`
- Current NAV TR YTD: `-7.91%` as of `2026-06-30`

## Risk read-through

EPI มี exposure India `100%` และเน้นบริษัทที่มีกำไร โดย WisdomTree รายงาน 568 holdings ณ `2026-03-31`; หน้าผลิตภัณฑ์ล่าสุดรายงาน total assets ประมาณ `$2.02bn` และ expense ratio `0.84%` ณ `2026-07-22`. ความเสี่ยงหลักคือ single-country concentration, emerging-market liquidity, INR/USD, sector concentration และ valuation volatility. Daily NAV history ที่ยืนยันได้สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official WisdomTree EPI product and performance page: https://www.wisdomtree.com/us/products/equity/epi
- Official WisdomTree EPI quarterly factsheet (performance as of 2026-03-31): https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-epi-1066.pdf?la=en
- Official WisdomTree Q1 2026 India-equity presentation: https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/presentations/equity/epi_indh_presentation.pdf
- SEC summary prospectus (December 10, 2024): https://www.sec.gov/Archives/edgar/data/1350487/000121465924020138/epi120924497k.htm
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
