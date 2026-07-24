---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:CHIQ
ticker: CHIQ
exchange: NYSE Arca
fund: Global X MSCI China Consumer Discretionary ETF
tracked_index: MSCI China Consumer Discretionary 10/50 Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: not disclosed
current_ytd_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/CHIQ
  - geography/China
---

# CHIQ Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

CHIQ เป็น passive/index-tracking China consumer discretionary equity ETF ของ Global X ติดตาม MSCI China Consumer Discretionary 10/50 Index. Official prospectus มี NAV total-return annual rows ครบ 10 calendar years 2016-2025: normalized TR `100.00` เป็น `199.05`, cumulative `99.05%`, CAGR `7.13%` สำหรับ 2015-12-31 ถึง 2025-12-31. Current official rolling 10Y NAV TR CAGR คือ `5.31%` สำหรับ 2016-06-30 ถึง 2026-06-30; current YTD คือ `-25.23%` ณ 2026-07-21.

## Performance check

- entity_key: NYSE Arca:CHIQ
- Inception: 2009-11-30; fund name/objective/strategy and underlying index changed effective 2018-12-06
- Metric: official NAV Total Return; dividends and capital gains are reinvested and NAV performance reflects fund expenses
- Tracked index (issuer benchmark): MSCI China Consumer Discretionary 10/50 Index; predecessor Solactive China Consumer Total Return Index through 2018-12-04
- Expense ratio: 0.65%
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year calendar NAV TR CAGR: 7.13% for 2015-12-31 to 2025-12-31; rolling official 10Y NAV TR CAGR: 5.31% for 2016-06-30 to 2026-06-30
- Coverage/source note: the calendar window uses official annual NAV TR rows; raw NAV endpoints for the rolling June window are not disclosed; S&P 500 rows reuse cached USD Total Return convention as of 2025-12-31; market-price return is not mixed

### 10-year NAV TR window

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative return | CAGR | Disclosure |
|---|---|---:|---:|---:|---:|---:|---|
| 2015-12-31 | 2025-12-31 | 10.00 | 100.00 (normalized) | 199.05 (calculated from official annual rows) | 99.05% | 7.13% | Complete calendar years 2016-2025 |

Formula: `199.05 = 100.00 × Π(1 + annual NAV TR)` and `CAGR = (199.05 / 100.00)^(1/10) - 1 = 7.13%`. The normalized endpoint is calculated from official annual returns, not a proxy.

| Year | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -5.88% | 11.96% |
| 2017 | 65.28% | 21.83% |
| 2018 | -27.72% | -4.38% |
| 2019 | 43.06% | 31.49% |
| 2020 | 93.43% | 18.40% |
| 2021 | -27.23% | 28.71% |
| 2022 | -22.07% | -18.11% |
| 2023 | -10.92% | 26.29% |
| 2024 | 12.16% | 25.02% |
| 2025 | 12.91% | 17.88% |
| 2026 YTD | -25.23% as of 2026-07-21 | not comparable; current year not cached |

## Window read-through

- 10 complete calendar-year NAV TR CAGR: `7.13%` for 2016-2025; cumulative return `99.05%`.
- 2021-2025 NAV TR CAGR: `-8.55%`; the five-year window is a comparison slice, not the primary 10-year coverage.
- Current official rolling 10Y NAV TR CAGR: `5.31%` for 2016-06-30 to 2026-06-30. It is shown separately because its end date differs from the complete-calendar window.
- Best calendar year: `2020 +93.43%`; worst: `2022 -22.07%`.
- Current YTD NAV TR: `-25.23%` as of 2026-07-21; S&P 500 current-year comparison is not used because the cached benchmark window ends 2025-12-31.

## Risk read-through

CHIQ เป็น non-diversified China consumer discretionary ETF มี 57 holdings ณ 2026-07-21 และ exposure กระจุกใน retail/distribution, autos, consumer durables และ consumer services. ความเสี่ยงหลักคือ China/A-share and foreign-listing access, policy/geopolitical, sector concentration, currency, liquidity และ benchmark/index change effective 2018-12-06. Daily NAV TR drawdown/recovery series: `ไม่พบข้อมูลที่ยืนยันได้` ใน reviewed official capture.

## Sources

- Official issuer source: https://www.globalxetfs.com/funds/CHIQ
- Official factsheet: https://assets.globalxetfs.com/funds/documents/chiq/Fact-Sheet_CHIQ.pdf
- Official summary prospectus: https://assets.globalxetfs.com/funds/documents/chiq/prospectus-regulatory/Summary-Prospectus_CHIQ.pdf
- Official annual shareholder report: https://assets.globalxetfs.com/funds/documents/chiq/prospectus-regulatory/Annual-Shareholder-Report.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
