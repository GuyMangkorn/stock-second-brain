---
type: source-note
instrument_type: ETF
entity_key: NASDAQ:VIGI
ticker: VIGI
source_profile: performance-history
accessed: 2026-07-12
normalized_output: raw/funds/ETF_NASDAQ_VIGI_performance.md
tags:
  - source/etf
  - source/performance
  - ticker/VIGI
---

# VIGI Performance Source Note - 2026-07-12

## Source Map

| Priority | Source | Data date / access | Use |
|---|---|---|---|
| 1 | [Vanguard VIGI product page](https://investor.vanguard.com/investment-products/etfs/profile/vigi) | official performance through 2026-05-31; accessed 2026-07-12 | NAV total return, market-price return, benchmark, annual history and fees |
| 4 | [PortfoliosLab VIGI](https://portfolioslab.com/symbol/VIGI) | dividend-adjusted daily data; last updated 2026-07-09 | monthly behavior, beta/capture and drawdown context only; secondary source |
| 4 | [Total Real Returns VIGI](https://totalrealreturns.com/n/VIGI) | dividend-reinvested series through 2026-07-02 | annual and drawdown cross-check; secondary source |

## Reporting Scope

Canonical ranking uses official issuer NAV total returns for complete years
2017-2025. The 2016 inception-year observation is partial because the fund
launched on 2016-02-25 and is retained as context, not ranked beside complete
years.

## Currency / Units

- Returns are percentages in USD terms.
- NAV total return includes reinvested income and fund expenses.
- Secondary monthly and drawdown data are dividend-adjusted market-data context.

## Extracted Facts

| Field | Value | Source |
|---|---:|---|
| Fund inception | 2016-02-25 | Vanguard product page |
| Benchmark | Spliced S&P Global Ex-U.S. Dividend Growers Index in USD NTR | Vanguard product page |
| Expense ratio | 0.07% as of 2026-02-27 | Vanguard product page |
| 2026 YTD NAV total return | 4.12% as of 2026-05-31 | Vanguard product page |
| 1-year NAV total return | 7.72% as of 2026-05-31 | Vanguard product page |
| 3-year average annual NAV return | 11.07% as of 2026-05-31 | Vanguard product page |
| 5-year average annual NAV return | 4.77% as of 2026-05-31 | Vanguard product page |

## Missing / Unverified Data

- Vanguard's captured page exposes annual and recent-period performance but not
  a durable full monthly NAV observation file.
- Monthly behavior and drawdown metrics are secondary and should not overwrite
  official NAV returns.

## Handoff For Ingest

- Normalize official 2016-2025 calendar-year NAV returns, marking 2016 partial,
  into `raw/funds/ETF_NASDAQ_VIGI_performance.md`.
- Use the common 2021-2025 window for the first cross-ETF matrix.
