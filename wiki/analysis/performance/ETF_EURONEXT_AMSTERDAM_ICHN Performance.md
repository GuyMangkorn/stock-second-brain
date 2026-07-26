---
type: etf-performance
instrument_type: ETF
entity_key: Euronext Amsterdam:ICHN
ticker: ICHN
input_ticker: ISVBF
exchange: Euronext Amsterdam
fund: iShares MSCI China UCITS ETF USD (Acc)
tracked_index: MSCI China Index (USD)
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/ISVBF
  - ticker/ICHN
  - geography/China
---

# ISVBF / ICHN Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

Input `ISVBF` is an OTC alias for the same USD accumulating share class
identified by ISIN `IE00BJ5JPG56`. The official iShares listing used as the
canonical exchange-qualified identity is `Euronext Amsterdam:ICHN`; the same
share class is also cross-listed as `SIX Swiss Exchange:ICHN`, `Xetra:ICGA`,
and on Mexico/Colombia venues. It is a passive physical China equity ETF with
share-class launch `2019-06-20`, so `10-year NAV TR unavailable`.

Official iShares NAV Total Return annual rows are available for complete
calendar years `2020-2025`; those displayed rows compound to `8.36%` and a
six-year annualized return of `1.35%`. This is an available complete-calendar
window, not a 10-year result. Current official NAV TR YTD is `-8.79%` as of
`2026-07-21`.

## Performance check

- entity_key: `Euronext Amsterdam:ICHN`
- Input alias: `ISVBF`; official share-class ISIN: `IE00BJ5JPG56`
- Inception/share-class launch: `2019-06-20`
- Structure: passive, physical/replicated, accumulating China equity ETF
- Metric: NAV Total Return with gross income reinvested where applicable and
  fund expenses reflected in NAV performance; market-price return is separate
- Tracked index: `MSCI China Index (USD)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark, not the fund's tracked index)
- 10-year NAV TR: `unavailable`; share-class history is shorter than 10 years
- Available complete-calendar window: `2020-01-01` to `2025-12-31`
- Actual elapsed years: `6.00`
- Normalized start/end TR values: `100.00` / `108.36`; raw issuer NAV index
  endpoints are `not disclosed`. End value is calculated from the published
  annual NAV rows: `100 × Π(1 + annual NAV TR)`.
- Available-window cumulative/CAGR: `8.36%` / `1.35%`; no claim is made that
  this is 10-year performance.
- Latest rolling 12-month NAV TR: `-5.07%` for `2025-06-30` to `2026-06-30`
- Current official NAV TR YTD: `-8.79%` as of `2026-07-21`; current NAV `US$5.61`
  as of the same date

| Year | ICHN NAV TR | MSCI China benchmark TR | S&P 500 TR |
|---|---:|---:|---:|
| 2020 | 29.10% | 29.50% | 18.40% |
| 2021 | -22.00% | -21.70% | 28.71% |
| 2022 | -22.10% | -21.90% | -18.11% |
| 2023 | -11.40% | -11.20% | 26.29% |
| 2024 | 19.20% | 19.40% | 25.02% |
| 2025 | 30.80% | 31.20% | 17.88% |

The iShares table does not disclose calendar rows for `2016-2019`; those
missing years are not filled with proxies. The S&P 500 rows reuse the cached
USD Total Return convention as of `2025-12-31`.

### Rolling 12-month observations

| Window ending | ICHN NAV TR | MSCI China benchmark TR |
|---|---:|---:|
| 2022-06-30 | -32.05% | -31.79% |
| 2023-06-30 | -16.98% | -16.82% |
| 2024-06-30 | -1.82% | -1.62% |
| 2025-06-30 | 33.41% | 33.78% |
| 2026-06-30 | -5.07% | -4.94% |

## Up years / Down years

- Up years / Down years: `3 / 3` over complete calendar years `2020-2025`
- Best: `2025`, `+30.80%`
- Least positive: `2024`, `+19.20%`
- Worst: `2022`, `-22.10%`
- Least bad down year: `2023`, `-11.40%`
- 2020-2025 cumulative/CAGR: ICHN `8.36%` / `1.35%`; S&P 500 TR
  `132.26%` / `15.08%`
- 2021-2025 cumulative/CAGR: ICHN `-16.06%` / `-3.44%`; S&P 500 TR
  `96.17%` / `14.43%`; ICHN trails by approximately `17.87 pp` CAGR
- Full inception-to-date raw NAV endpoints and a directly calculated
  `2019-06-20` to current CAGR: `not disclosed`; no annualization is inferred
  from incomplete 2019 data.

## Methodology and data gaps

The official iShares page identifies the share class as accumulating, physical
and replicated, with `0.28%` TER and benchmark `MSCI China Index (USD)`. The
official listing table maps ISIN `IE00BJ5JPG56` to USD `ICHN` on Euronext
Amsterdam and SIX, and to EUR `ICGA` on Xetra. The OTC input alias is retained
in frontmatter and the page title, while the issuer/exchange-qualified key is
used for the canonical page. No 2016-2019 annual rows or raw NAV endpoint
levels are invented.

## Risk read-through

This is a single-country China equity fund with emerging-market, currency,
regulatory, liquidity and concentration risks. The accumulating share class
has a `0.28%` TER. Official daily NAV Total Return drawdown and recovery dates
are `not disclosed`; no secondary proxy is substituted.

## Sources

- [Official iShares ICHN product and performance page](https://www.ishares.com/uk/professional/en/products/308751/ishares-msci-china-ucits-etf?siteEntryPassthrough=true&switchLocale=y) — identity, ISIN, official listings, inception, asset class, TER, benchmark, NAV TR definition, annual rows, rolling 12-month rows, current NAV/YTD and as-of dates
- [Official iShares ICHN factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/ichn-ishares-msci-china-ucits-etf-fund-fact-sheet-en-gb.pdf) — passive/physical/replicated classification, accumulating share class, fee, benchmark and share-class launch
- [Official Euronext Amsterdam instrument page](https://live.euronext.com/en/product/etfs/IE00BJ5JPG56-XAMC/market-information) — canonical exchange/ticker, ISIN, legal name, USD trading line and launch/listing cross-check
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention — common USD total-return reference
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
