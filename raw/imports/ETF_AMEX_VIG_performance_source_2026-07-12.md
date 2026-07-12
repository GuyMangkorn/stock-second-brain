---
type: source-note
instrument_type: ETF
entity_key: AMEX:VIG
ticker: VIG
source_profile: performance-history
accessed: 2026-07-12
normalized_output: raw/funds/ETF_AMEX_VIG_performance.md
tags:
  - source/etf
  - source/performance
  - ticker/VIG
---

# VIG Performance Source Note - 2026-07-12

## Source Map

| Priority | Source | Data date / access | Use |
|---|---|---|---|
| 1 | [Vanguard VIG product page](https://investor.vanguard.com/investment-products/etfs/profile/vig) | official performance through 2026-05-31; accessed 2026-07-12 | NAV total return, market-price return, benchmark, annual history and fees |
| 4 | [PortfoliosLab VIG](https://portfolioslab.com/symbol/VIG) | dividend-adjusted daily data; last updated 2026-07-10 | monthly behavior, beta/capture and drawdown context only; secondary source |
| 4 | [Total Real Returns VIG](https://totalrealreturns.com/n/VIG) | dividend-reinvested series through 2026-07-10 | extended 2007-2010 context and drawdown cross-check; secondary source |

## Reporting Scope

Canonical ranking uses official issuer NAV total returns for complete years
2011-2025. The 2006 inception-year observation is partial and is not ranked.
The 2007-2010 extension is retained as secondary context because the captured
Vanguard annual table begins at 2011.

## Currency / Units

- Returns are percentages in USD terms.
- NAV total return includes reinvested income and fund expenses.
- Secondary monthly and drawdown data are dividend-adjusted market-data context.

## Extracted Facts

| Field | Value | Source |
|---|---:|---|
| Fund inception | 2006-04-21 | Vanguard product page |
| Benchmark | Spliced S&P U.S. Dividend Growers Index TR | Vanguard product page |
| Expense ratio | 0.04% as of 2026-05-28 | Vanguard product page |
| 2026 YTD NAV total return | 7.19% as of 2026-05-31 | Vanguard product page |
| 1-year NAV total return | 20.36% as of 2026-05-31 | Vanguard product page |
| 3-year average annual NAV return | 17.37% as of 2026-05-31 | Vanguard product page |
| 5-year average annual NAV return | 10.59% as of 2026-05-31 | Vanguard product page |

## Missing / Unverified Data

- The current source surface does not expose an issuer monthly NAV observation
  file in a durable downloadable form.
- Monthly behavior and drawdown metrics are secondary and should not overwrite
  official NAV returns.

## Handoff For Ingest

- Normalize official 2011-2025 calendar-year NAV returns and the 2026 partial
  snapshot into `raw/funds/ETF_AMEX_VIG_performance.md`.
- Retain the 2007-2010 secondary extension separately.
- Use the common 2021-2025 window for the first cross-ETF matrix.
