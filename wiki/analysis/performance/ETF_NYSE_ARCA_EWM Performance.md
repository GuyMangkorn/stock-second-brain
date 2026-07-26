---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWM
ticker: EWM
exchange: NYSE Arca
fund: iShares MSCI Malaysia ETF
tracked_index: MSCI Malaysia Index
benchmark: S&P 500 Total Return
inception: 1996-03-12
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWM
  - geography/Malaysia
---

# EWM Performance

> Navigation: [[ETF Region Index]] → [[Malaysia ETF]] → [[ETF Performance Index]]

## Bottom line

EWM มี official rolling 10-year NAV Total Return จาก 2026-06-30 ย้อนถึง 2016-06-30: cumulative `24.54%` และ CAGR `2.22%` (actual `10.00` years; raw endpoints not disclosed). ใน annual rows ที่ official page แสดงสำหรับ 2021-2025 เป็นบวก 2 ปีและลบ 3 ปี; best คือ 2024 `20.13%` และ worst คือ 2021 `-6.30%`. Current NAV TR YTD คือ `4.62%` ณ 2026-07-17.

## Performance check

- entity_key: NYSE Arca:EWM
- Inception: 1996-03-12; 10-year window 2016-06-30 to 2026-06-30 (`10.00` years)
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index (issuer benchmark): MSCI Malaysia Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year window: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR CAGR: `2.22%`; cumulative `24.54%`; raw start/end TR values are `not disclosed`, so normalized `100.00 → 124.54` is an implied endpoint from the official cumulative return
- Coverage/source note: official complete calendar years 2021-2025 are shown; earlier annual rows are not surfaced in the reviewed official capture; S&P 500 rows reuse cached USD Total Return convention as of 2025-12-31; market-price return is not mixed

| Year | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | -6.30% | 28.71% |
| 2022 | -6.25% | -18.11% |
| 2023 | -4.01% | 26.29% |
| 2024 | 20.13% | 25.02% |
| 2025 | 15.37% | 17.88% |

## Up years / Down years

- Up years / Down years: 2 / 3
- Best: 2024, 20.13%
- Least positive: 2025, 15.37%
- Worst: 2021, -6.30%
- Least bad down year: 2023, -4.01%
- 2021-2025 cumulative/CAGR: 16.86% / 3.17% from published annual rows; S&P 500 common-window cumulative/CAGR: 96.17% / 14.43%
- Current YTD: 4.62% as of 2026-07-17

## Risk read-through

EWM เป็น passive/index-tracking Malaysia equity ETF; expense ratio `0.50%`. Official rolling 10Y NAV TR CAGR คือ `2.22%`; raw endpoints and daily drawdown/recovery history are `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed official capture. Common complete calendar rows 2021-2025 show EWM CAGR `3.17%` versus S&P 500 TR `14.43%`, a gap of `-11.26 pp`; this is a calendar comparison, while the official EWM rolling window is 2016-06-30 to 2026-06-30.

## Sources

- Official issuer product/performance page: https://www.ishares.com/us/products/239669/ishares-msci-malaysia-etf
- Official issuer factsheet: https://www.ishares.com/us/literature/fact-sheet/ewm-ishares-msci-malaysia-etf-fund-fact-sheet-en-us.pdf
- SEC summary prospectus: https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-malaysia-etf-8-31.pdf
- Official annual shareholder report: https://www.ishares.com/us/literature/annual-report/ar-ewm-en.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
