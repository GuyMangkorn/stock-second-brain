---
type: etf-performance
instrument_type: ETF
entity_key: AMEX:DGRO
ticker: DGRO
exchange: AMEX
benchmark: Morningstar US Dividend Growth Index
return_basis: NAV total return
official_performance_as_of: 2026-06-30
secondary_behavior_as_of: 2026-07-11
source_note: raw/imports/ETF_AMEX_DGRO_performance_source_2026-07-12.md
coverage_status: pilot_partial
tags:
  - fund-performance/etf
  - ticker/DGRO
  - exchange/AMEX
---

# AMEX:DGRO Performance

## Snapshot

| Metric | Value | As-of / basis |
|---|---:|---|
| 2026 YTD NAV total return | 10.22% | 2026-06-30; official issuer |
| 1-year NAV total return | 21.00% | 2026-06-30; official issuer |
| 3-year average annual NAV return | 16.38% | 2026-06-30; official issuer |
| 5-year average annual NAV return | 11.02% | 2026-06-30; official issuer |
| Average monthly return | 1.05% | 2026-07-11; secondary dividend-adjusted daily data |
| Positive months | 67% | 2026-07-11; secondary dividend-adjusted daily data |
| Maximum drawdown | -35.10% | COVID crash, 2020-03-23; secondary |
| Recovery from maximum drawdown | 161 trading sessions | secondary |

## Calendar Year NAV Total Return - Canonical

Official issuer calendar-year history currently exposed for 2021-2025. The
benchmark is pre-fee and is shown for tracking context.

| Year | NAV total return | Market price total return | Benchmark | Period status | Source |
|---:|---:|---:|---:|---|---|
| 2021 | 26.56% | 26.64% | 26.69% | complete | iShares factsheet |
| 2022 | -7.85% | -7.90% | -7.75% | complete | iShares factsheet |
| 2023 | 10.43% | 10.49% | 10.44% | complete | iShares factsheet |
| 2024 | 16.61% | 16.63% | 16.67% | complete | iShares factsheet |
| 2025 | 15.74% | 15.70% | 15.87% | complete | iShares factsheet |

## Extended Historical Context - Secondary Proxy

These rows use a dividend-reinvested market-price-adjusted proxy and are kept
separate from the issuer NAV table. 2014 is partial because DGRO launched in
June.

| Year | Adjusted total-return proxy | Period status | Source |
|---:|---:|---|---|
| 2014 | 8.56% | partial | Total Real Returns |
| 2015 | -0.69% | complete | Total Real Returns |
| 2016 | 15.20% | complete | Total Real Returns |
| 2017 | 23.00% | complete | Total Real Returns |
| 2018 | -2.38% | complete | Total Real Returns |
| 2019 | 29.87% | complete | Total Real Returns |
| 2020 | 9.50% | complete | Total Real Returns |

## Monthly Behavior Metrics - Secondary Context

| Metric | Value | Definition |
|---|---:|---|
| Best month | +12.1% in 2020-11 | dividend-adjusted daily data aggregated monthly |
| Worst month | -12.8% in 2020-03 | dividend-adjusted daily data aggregated monthly |
| Longest winning streak | 10 months | secondary source |
| Longest losing streak | 3 months | secondary source |
| Beta vs. S&P 500 | 0.87 | secondary daily-data calculation |
| R-squared vs. S&P 500 | 0.89 | secondary daily-data calculation |

The normalized monthly observation series is not yet stored. These metrics are
useful for pilot classification but are not a substitute for an official NAV
series.

## Common Window Calculation

Common complete window: 2021-2025 official NAV total return.

| Calculation | Result |
|---|---:|
| Cumulative growth | 73.82% |
| CAGR | 11.69% |
| Positive years | 4 / 5 |
| Negative years | 1 / 5 |
| Sample standard deviation of annual returns | 12.68% |

Formula: `CAGR = (1.2656 x 0.9215 x 1.1043 x 1.1661 x 1.1574)^(1/5) - 1`.
The annual-return standard deviation is a small-sample descriptive statistic,
not the issuer's monthly volatility statistic.

## Provenance

Primary source note: [[ETF_AMEX_DGRO_performance_source_2026-07-12]]. Secondary
sources and dates are listed there. Do not mix the secondary proxy with the
canonical issuer NAV ranking.
