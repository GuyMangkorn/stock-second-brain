---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:GXC
ticker: GXC
exchange: NYSE Arca
fund: State Street SPDR S&P China ETF
tracked_index: S&P China BMI Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/GXC
  - geography/China
---

# GXC Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

GXC เป็น passive/index-tracking China equity ETF ที่ติดตาม S&P China BMI Index. Official rolling 10-year NAV Total Return CAGR คือ `4.37%` สำหรับ `2016-06-30` ถึง `2026-06-30` (`10.00` elapsed years); raw start/end TR values และ raw cumulative return ไม่ได้เปิดเผย. Current NAV TR YTD คือ `-10.99%` ณ `2026-06-30`.

## Performance check

- entity_key: `NYSE Arca:GXC`
- Inception: `2007-03-20`
- Metric: NAV Total Return including reinvested dividends/capital gains and fund expenses
- Tracked index: S&P China BMI Index; float-adjusted market-capitalization-weighted exposure to investable China equities, including eligible China A Shares through Stock Connect
- Official 10-year window: start date `2016-06-30`; end date `2026-06-30`; actual years `10.00`; start TR value `not disclosed`; end TR value `not disclosed`; official CAGR `4.37%`
- Implied cumulative return from the official CAGR is approximately `53.38%`; this is a shown calculation, not a substitute for undisclosed raw endpoints
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not the issuer benchmark)

| Year | GXC NAV TR | S&P China BMI TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | not disclosed | not disclosed | 28.71% |
| 2022 | not disclosed | not disclosed | -18.11% |
| 2023 | not disclosed | not disclosed | 26.29% |
| 2024 | not disclosed | not disclosed | 25.02% |
| 2025 | not disclosed | not disclosed | 17.88% |

The reviewed current State Street factsheet and product performance table disclose rolling periods but do not disclose readable annual NAV/index rows for `2016-2025`; no third-party annual proxy is substituted. S&P 500 rows reuse the cached USD Total Return convention for complete calendar years `2016-2025`.

## Window calculations

- Official rolling 10-year GXC NAV TR: CAGR `4.37%`; implied cumulative from CAGR `53.38%` (raw cumulative not disclosed)
- 2016-2025 and 2021-2025 GXC annual-window CAGR: `not disclosed` because issuer annual NAV rows are not disclosed in the reviewed official capture
- S&P 500 reference: 2016-2025 cumulative `298.33%` / CAGR `14.82%`; 2021-2025 cumulative `96.17%` / CAGR `14.43%`
- Up years / down years, best/worst calendar year and exact common-window spread: `not disclosed`
- Current NAV TR YTD: `-10.99%` as of `2026-06-30`

## Risk read-through

GXC มี 1,309 holdings ใน factsheet ณ `2026-06-30` และ exposure กระจุกใน China/Hong Kong โดย sector หลักคือ consumer discretionary, financials, information technology และ communication services. ความเสี่ยงหลักคือ China policy/geopolitical risk, emerging-market liquidity, ADR/H-share/A-share structure, country concentration และ valuation volatility. Daily NAV history ที่ยืนยันได้สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official State Street GXC product/performance page: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-china-etf-gxc
- Official State Street GXC factsheet (as of 2026-06-30): https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-gxc.pdf
- SEC summary prospectus (January 31, 2026): https://www.sec.gov/Archives/edgar/data/1168164/000119312526031213/d92286d497k.htm
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
