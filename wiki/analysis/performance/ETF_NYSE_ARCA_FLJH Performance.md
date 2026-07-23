---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLJH
ticker: FLJH
exchange: NYSE Arca
fund: Franklin FTSE Japan Hedged ETF
tracked_index: FTSE Japan RIC Capped Hedged to USD Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-03-31
current_ytd_as_of: 2026-07-07
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FLJH
  - geography/Japan
---

# FLJH Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

FLJH เป็น passive/index-tracking Japan equity ETF ที่ hedge ค่าเงินเยนเป็นดอลลาร์สหรัฐ และติดตาม FTSE Japan RIC Capped Hedged to USD Index. Inception `2017-11-02` ทำให้ `10-year NAV TR unavailable` ณ รอบข้อมูลนี้. Official available-period NAV TR ตั้งแต่ inception ถึง `2026-03-31` มี annualized return `13.63%`; official current NAV TR YTD คือ `22.91%` ณ `2026-07-07`.

## Performance check

- entity_key: `NYSE Arca:FLJH`
- Inception: `2017-11-02`
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index: FTSE Japan RIC Capped Hedged to USD Index (FTSE Japan Capped Hedged Index); reconstituted semi-annually
- 10-year coverage: `10-year NAV TR unavailable`; inception `2017-11-02` to factsheet as-of `2026-03-31` is approximately `8.41` years, not 10 years
- Available-period official result: NAV TR annualized `13.63%` from inception through `2026-03-31`; raw start/end TR values and raw cumulative return are `not disclosed`
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not the issuer benchmark)

| Year | FLJH NAV TR | FTSE Japan Capped Hedged TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not applicable (pre-inception) | not applicable (pre-index history) | 11.96% |
| 2017 | not applicable (partial inception year) | not applicable | 21.83% |
| 2018 | -13.96% | -14.00% | -4.38% |
| 2019 | 20.52% | 20.79% | 31.49% |
| 2020 | 9.44% | 9.46% | 18.40% |
| 2021 | 12.78% | 12.82% | 28.71% |
| 2022 | -1.47% | -1.35% | -18.11% |
| 2023 | 35.04% | 34.92% | 26.29% |
| 2024 | 26.07% | 25.98% | 25.02% |
| 2025 | 29.25% | 29.20% | 17.88% |

Annual FLJH NAV TR and issuer-index rows are from the Franklin factsheet as of `2026-03-31`; 2017 is not shown as a complete calendar-year return because the fund launched on November 2. S&P 500 rows use the cached USD Total Return convention.

## Window calculations

- 2018-2025 FLJH NAV TR: cumulative `177.49%` / CAGR `13.61%`; S&P 500 TR: cumulative `192.03%` / CAGR `14.33%`
- 2021-2025 FLJH NAV TR: cumulative `144.52%` / CAGR `19.58%`; S&P 500 TR: cumulative `96.17%` / CAGR `14.43%`; FLJH leads by approximately `5.15 pp` CAGR
- Up years / down years in complete rows: `7 / 1`
- Best year: `2023`, `35.04%`; worst year: `2018`, `-13.96%`
- Current NAV TR YTD: `22.91%` as of `2026-07-07`

## Risk read-through

FLJH มี 478 holdings ณ factsheet date และใช้ currency hedge เพื่อลดผลกระทบจาก JPY/USD แต่ hedge cost และ basis risk อาจทำให้ผลตอบแทนต่างจาก unhedged Japan equity. ความเสี่ยงหลักคือ Japan/country concentration, equity volatility, currency-hedge effectiveness และ sector allocation. Daily NAV history ที่ยืนยันได้สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official Franklin FLJH product page: https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26355/SINGLCLASS/franklin-ftse-japan-hedged-etf/FLJH
- Official Franklin FLJH factsheet (as of 2026-03-31): https://www.franklintempleton.com/forms-literature/download/FLJH-FF
- Official Franklin FLJH annual report / total-return report: https://www.franklintempleton.com/tools-and-resources/literature/info/FLJH-ATSR
- Official Franklin FLJH summary prospectus: https://www.franklintempleton.com/forms-literature/download-preview/FLJH-PSUM
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
