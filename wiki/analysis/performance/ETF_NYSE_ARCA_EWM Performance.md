---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWM
ticker: EWM
exchange: NYSE Arca
fund: iShares MSCI Malaysia Index Fund
tracked_index: not disclosed in compact capture
benchmark: S&P 500 Total Return
updated: 2026-07-23
performance_as_of: 2026-07-17
current_ytd_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWM
  - geography/Malaysia
---

# EWM Performance

> Navigation: [[ETF Region Index]] → [[Malaysia ETF]] → [[ETF Performance Index]]

## Bottom line

EWM มี official annual NAV Total Return ในช่วง 2021-2025; เป็นบวก 2 ปีและลบ 3 ปี, best คือ 2024 20.13% และ worst คือ 2021 -6.30%. Current NAV YTD คือ 4.62% ณ 2026-07-17.

## Performance check

- entity_key: NYSE Arca:EWM
- Inception: not disclosed in compact capture
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index (issuer benchmark): not disclosed in compact capture
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR CAGR: not disclosed for reproducibility; raw endpoints not disclosed in source capture
- Coverage/source note: official complete calendar years 2021-2025; S&P 500 rows reuse cached USD Total Return convention as of 2025-12-31; market-price return is not mixed

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
- Available-period cumulative/CAGR: 16.86% / 3.17% จาก published annual rows
- Current YTD: 4.62% as of 2026-07-17

## Risk read-through

EWM เป็น passive/index-tracking equity ETF ใน primary region Malaysia. Expense ratio, issuer benchmark, daily NAV Total Return drawdown และ recovery: not disclosed in this compact capture. ข้อจำกัดสำคัญ: raw 10Y endpoints not disclosed; earlier annual rows not surfaced.

## Sources

- Official issuer source: https://www.ishares.com/us/products/239669/EWM
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-23]] | [[ETF Performance Index]]
