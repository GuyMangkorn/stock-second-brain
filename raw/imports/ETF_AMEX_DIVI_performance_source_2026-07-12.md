---
type: source-note
instrument_type: ETF
entity_key: AMEX:DIVI
ticker: DIVI
source_profile: performance-history
accessed: 2026-07-12
normalized_output: raw/funds/ETF_AMEX_DIVI_performance.md
tags:
  - source/etf
  - source/performance
  - ticker/DIVI
---

# DIVI Performance Source Note - 2026-07-12

## Source Map

| Priority | Source | Data date / access | Use |
|---|---|---|---|
| 1 | [Franklin DIVI factsheet](https://www.franklintempleton.com/forms-literature/download/DIVI-FF) | official factsheet 2026-06-30; accessed 2026-07-12 | NAV total return, market-price return, underlying index, annual history and risk statistics |
| 1 | [Existing DIVI official source note](raw/imports/ETF_AMEX_DIVI_fund_source_2026-07-12.md) | official source map captured 2026-07-12 | identity, methodology and source provenance |
| 4 | [PortfoliosLab DIVI](https://portfolioslab.com/symbol/DIVI) | dividend-adjusted daily data; last updated 2026-07-11 | monthly behavior and drawdown context only; secondary source |

## Reporting Scope

Canonical ranking uses official issuer NAV total returns for complete years
2017-2025. 2016 is inception-year context and is not ranked because the
factsheet does not provide a complete calendar-year return.

## Currency / Units

- Returns are percentages in USD terms.
- NAV total return assumes reinvested distributions and deducts fund expenses.
- The underlying index return is pre-fee and is not interchangeable with NAV
  total return.
- Secondary monthly and drawdown data are dividend-adjusted market-data context.

## Extracted Facts

| Field | Value | Source |
|---|---:|---|
| Fund inception | 2016-06-01 | Franklin factsheet |
| Benchmark | Morningstar Developed Markets ex-North America Dividend Enhanced Select Index-NR | Franklin factsheet |
| Expense ratio | 0.09% | Franklin factsheet |
| 2026 YTD NAV total return | 11.38% as of 2026-06-30 | Franklin factsheet |
| 1-year NAV total return | 24.65% as of 2026-06-30 | Franklin factsheet |
| 3-year average annual NAV return | 18.01% as of 2026-06-30 | Franklin factsheet |
| 5-year average annual NAV return | 13.68% as of 2026-06-30 | Franklin factsheet |
| 3-year standard deviation | 13.14% as of 2026-06-30 | Franklin factsheet |

## Missing / Unverified Data

- A complete issuer monthly NAV observation file was not captured in this
  performance pass.
- Monthly behavior and drawdown metrics are secondary and should not overwrite
  official NAV returns.

## Handoff For Ingest

- Normalize official 2017-2025 calendar-year NAV returns and the 2026 partial
  snapshot into `raw/funds/ETF_AMEX_DIVI_performance.md`.
- Use the common 2021-2025 window for the first cross-ETF matrix.
