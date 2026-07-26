---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:KTEC
ticker: KTEC
exchange: NYSE Arca
fund: KraneShares Hang Seng TECH Index ETF
tracked_index: Hang Seng TECH Index
benchmark: S&P 500 Total Return
inception: 2021-06-08
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/KTEC
  - geography/Hong-Kong
---

# KTEC Performance

> Navigation: [[ETF Region Index]] → [[Hong Kong ETF]] → [[ETF Performance Index]]

## Bottom line

KTEC มี available-period NAV Total Return ตั้งแต่ 2021-06-08 ถึง 2026-06-30 รวม 5.06 elapsed years: cumulative `-49.08%` และ issuer-reported since-inception annualized return `-12.48%`. `10-year NAV TR unavailable` อย่างตรงไปตรงมา; current NAV TR YTD คือ `-22.88%` ณ 2026-06-30.

## Performance check

- entity_key: NYSE Arca:KTEC
- Inception: 2021-06-08; official available period ends 2026-06-30 (`5.06` years using `days / 365.25`)
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index (issuer benchmark): Hang Seng TECH Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR: unavailable; official history is shorter than 10 years
- Available-period NAV TR: cumulative `-49.08%`; issuer-reported annualized `-12.48%`; start/end TR values are `not disclosed`, so normalized `100.00 → 50.92` is an implied endpoint from the disclosed cumulative return
- Coverage/source note: official complete calendar rows are available for 2022-2024; 2021 inception-year partial and 2025 annual NAV TR are `not disclosed`; S&P 500 rows reuse cached USD Total Return convention as of 2025-12-31; market-price return is not mixed

| Year | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2022 | -25.01% | -18.11% |
| 2023 | -11.21% | 26.29% |
| 2024 | 18.46% | 25.02% |
| 2025 | not disclosed | 17.88% |

## Up years / Down years

- Up years / Down years: 1 / 2 among official complete rows 2022-2024
- Best: 2024 `18.46%`
- Least positive: not applicable; only one positive complete year disclosed
- Worst: 2022 `-25.01%`
- Least bad down year: 2023 `-11.21%`
- Current YTD: -22.88% as of 2026-06-30

## Risk read-through

KTEC เป็น passive/index-tracking Hong Kong technology equity ETF; expense ratio `0.69%`. Available-period result is highly negative, with two down years among the three official complete calendar rows; max drawdown/recovery history is `ไม่พบข้อมูลที่ยืนยันได้` in the official capture. S&P common-reference comparison over the disclosed 2022-2024 rows is ETF cumulative `-21.13%` / annualized `-7.61%` versus S&P cumulative `29.29%` / annualized `8.94%`; this is not a 10-year comparison.

## Sources

- Official issuer product/performance page: https://kraneshares.com/etf/ktec/
- Official issuer factsheet: https://kraneshares.com/resources/factsheet/ktec_factsheet.pdf
- SEC summary prospectus: https://kraneshares.com/resources/compliance/2026_02_20_ktec_summary.prospectus.pdf
- Official annual shareholder report: https://kraneshares.com/resources/compliance/2026_05_29_ktec_annual.TSR.report.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
