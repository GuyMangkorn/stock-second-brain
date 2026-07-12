---
type: etf-performance
instrument_type: ETF
entity_key: AMEX:VIG
ticker: VIG
exchange: AMEX
benchmark: Spliced S&P U.S. Dividend Growers Index TR
return_basis: NAV total return
official_performance_as_of: 2026-05-31
secondary_behavior_as_of: 2026-07-10
source_note: raw/imports/ETF_AMEX_VIG_performance_source_2026-07-12.md
coverage_status: pilot_complete_with_secondary_extension
tags:
  - fund-performance/etf
  - ticker/VIG
  - exchange/AMEX
---

# AMEX:VIG Performance

## Snapshot

| Metric | Value | As-of / basis |
|---|---:|---|
| 2026 YTD NAV total return | 7.19% | 2026-05-31; official issuer |
| 1-year NAV total return | 20.36% | 2026-05-31; official issuer |
| 3-year average annual NAV return | 17.37% | 2026-05-31; official issuer |
| 5-year average annual NAV return | 10.59% | 2026-05-31; official issuer |
| Average monthly return | 0.88% | 2026-07-10; secondary dividend-adjusted daily data |
| Positive months | 67% | 2026-07-10; secondary dividend-adjusted daily data |
| Maximum drawdown | -46.81% | Financial crisis, 2009-03-09; secondary |
| Recovery from maximum drawdown | 491 trading sessions | secondary |

## Calendar Year NAV Total Return - Canonical

The official Vanguard annual table provides complete calendar years from 2011.
The 2006 inception-year period is partial and excluded from ranking.

| Year | NAV total return | Market price total return | Benchmark | Period status | Source |
|---:|---:|---:|---:|---|---|
| 2011 | 6.21% | 6.19% | 6.32% | complete | Vanguard |
| 2012 | 11.61% | 11.58% | 11.73% | complete | Vanguard |
| 2013 | 28.99% | 29.01% | 29.03% | complete | Vanguard |
| 2014 | 10.06% | 10.06% | 10.12% | complete | Vanguard |
| 2015 | -1.95% | -1.97% | -1.88% | complete | Vanguard |
| 2016 | 11.84% | 11.90% | 11.93% | complete | Vanguard |
| 2017 | 22.22% | 22.21% | 22.29% | complete | Vanguard |
| 2018 | -2.02% | -2.10% | -1.98% | complete | Vanguard |
| 2019 | 29.71% | 29.76% | 29.75% | complete | Vanguard |
| 2020 | 15.46% | 15.49% | 15.62% | complete | Vanguard |
| 2021 | 23.64% | 23.58% | 23.71% | complete | Vanguard |
| 2022 | -9.79% | -9.79% | -9.70% | complete | Vanguard |
| 2023 | 14.46% | 14.53% | 14.52% | complete | Vanguard |
| 2024 | 17.02% | 16.96% | 17.07% | complete | Vanguard |
| 2025 | 14.18% | 14.16% | 14.24% | complete | Vanguard |

## Extended Historical Context - Secondary Proxy

| Year | Adjusted total-return proxy | Period status | Source |
|---:|---:|---|---|
| 2006 | 8.55% | partial | Total Real Returns |
| 2007 | 5.63% | complete | Total Real Returns |
| 2008 | -26.69% | complete | Total Real Returns |
| 2009 | 19.58% | complete | Total Real Returns |
| 2010 | 14.74% | complete | Total Real Returns |

## Monthly Behavior Metrics - Secondary Context

| Metric | Value | Definition |
|---|---:|---|
| Best month | +10.0% in 2020-11 | dividend-adjusted daily data aggregated monthly |
| Worst month | -14.1% in 2008-10 | dividend-adjusted daily data aggregated monthly |
| COVID drawdown | -31.72% in 2020-03 | peak-to-trough secondary series |
| 2022 bear-market drawdown | -20.39% in 2022-09 | peak-to-trough secondary series |
| Beta vs. S&P 500 | 0.84 | secondary daily-data calculation |
| Downside capture vs. S&P 500 | 81.66% | secondary daily-data calculation |

The normalized monthly observation series is not yet stored. These metrics are
useful for pilot classification but are not a substitute for an official NAV
series.

## Common Window Calculation

Common complete window: 2021-2025 official NAV total return.

| Calculation | Result |
|---|---:|
| Cumulative growth | 70.58% |
| CAGR | 11.27% |
| Positive years | 4 / 5 |
| Negative years | 1 / 5 |
| Sample standard deviation of annual returns | 12.71% |

Formula: `CAGR = (1.2364 x 0.9021 x 1.1446 x 1.1702 x 1.1418)^(1/5) - 1`.

## Provenance

Primary source note: [[ETF_AMEX_VIG_performance_source_2026-07-12]]. Secondary
sources and dates are listed there. Do not mix the secondary proxy with the
canonical issuer NAV ranking.
