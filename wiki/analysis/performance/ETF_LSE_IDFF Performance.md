---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IDFF
input_ticker: IIXFF
ticker: IDFF
exchange: London Stock Exchange
fund: iShares MSCI AC Far East ex-Japan UCITS ETF U.S. Dollar (Distributing)
tracked_index: MSCI All Country World Far East Ex Japan USD Index (USD)
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-09-01
performance_as_of: 2025-12-31 (official calendar rows)
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-27
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-5.md
return_basis: NAV total return; gross income reinvested where applicable
return_currency: USD
primary_region: Asia ex Japan
tags:
  - analysis/etf-performance
  - ticker/IIXFF
  - ticker/IDFF
  - geography/Asia-ex-Japan
---

# IIXFF / IDFF Performance

> [[ETF Region Index]] → [[Asia ex Japan ETF]] → [[ETF Performance Index]]

## Bottom line

IIXFF เป็น input alias ของ iShares MSCI AC Far East ex-Japan UCITS ETF โดย
canonical USD listing ที่ยืนยันได้คือ `LSE:IDFF`. กองทุนเป็น passive physical ETF
ที่ลงทุนใน developed และ emerging East Asia โดยไม่รวม Japan และ India. Official
calendar-year NAV Total Return 2016-2025 สะสม `111.81%` และ rounded-input CAGR
`7.79%†`; ช่วง 2021-2025 สะสม `13.62%` / CAGR `2.59%`. Current official NAV TR
YTD ล่าสุดคือ `+32.28%` ณ 2026-08-26 และ NAV คือ `US$96.75` ณ 2026-08-27.

## Performance check

- `entity_key: LSE:IDFF`; raw card input `IIXFF`; the issuer's USD London Stock Exchange line is `IDFF` (same fund/share-class ISIN `IE00B0M63730`); the product also has other currency/listing lines, including `IFFF`.
- Fund: `iShares MSCI AC Far East ex-Japan UCITS ETF U.S. Dollar (Distributing)`; share-class/fund launch `2005-10-28`; issuer `iShares plc`; methodology `Physical / Replicated`; distribution frequency quarterly.
- Classification: supported `passive-index` equity ETF. Objective is to track companies from developed and emerging East Asia excluding Japan and India; no payoff-defining leverage, inverse, option-income, bond, commodity, or currency structure identified.
- Metric: USD `NAV Total Return`, with gross income reinvested where applicable; market-price return is not mixed.
- Tracked index: `MSCI All Country World Far East Ex Japan USD Index (USD)`. Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark, not the issuer benchmark). Cached S&P rows are as of 2025-12-31.
- 10-year window: `2015-12-31` to `2025-12-31`; normalized TR `100.00 → 211.81`; `Years: 10.00`.
- 10-year NAV TR CAGR: `7.79%†`, calculated from ten official complete calendar-year rows using `(End TR / Start TR)^(1 / Years) - 1`; the dagger marks the rounded-input calendar approximation.
- Current official snapshot: NAV `US$96.75` as of 2026-08-27; NAV TR YTD `+32.28%` as of 2026-08-26; holdings `423`, P/E `21.68x`, P/B `2.68x`, and 12-month trailing distribution yield `1.05%` as of 2026-08-28.
- Coverage/source note: annual rows are from the official June 2026 factsheet; current NAV/YTD and listing/fund facts are from the issuer product page. Exact daily NAV drawdown/recovery is not disclosed in the reviewed sources.

| Year / window | IDFF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 5.50% | 11.96% |
| 2017 | 41.19% | 21.83% |
| 2018 | -15.68% | -4.38% |
| 2019 | 18.66% | 31.49% |
| 2020 | 25.08% | 18.40% |
| 2021 | -8.92% | 28.71% |
| 2022 | -21.94% | -18.11% |
| 2023 | 2.30% | 26.29% |
| 2024 | 11.66% | 25.02% |
| 2025 | 39.91% | 17.88% |
| 2016-2025 cumulative | 111.81% | 298.33% |
| 2016-2025 CAGR | 7.79%† | 14.82% |
| 2021-2025 cumulative | 13.62% | 96.17% |
| 2021-2025 CAGR | 2.59% | 14.43% |

**Up years / Down years**

- Up years / Down years: `7 / 3` across complete 2016-2025 calendar years.
- Best: 2017, `+41.19%`.
- Least positive: 2023, `+2.30%`.
- Worst: 2022, `-21.94%`.
- Least bad down year: 2021, `-8.92%`.
- Current official NAV TR YTD: `+32.28%` as of 2026-08-26; no synchronized current S&P 500 YTD comparison is inferred.

## Risk read-through

IDFF มี high Asia ex-Japan country, China/Taiwan/Korea, technology, emerging-market,
currency and liquidity sensitivity. The issuer reports 3-year beta `0.998` and
standard deviation `21.47%` as of 2026-07-31, alongside `423` holdings. Population
standard deviation calculated from the rounded annual NAV rows is `20.71%` for
2016-2025 and `20.92%` for 2021-2025; this is not an issuer daily-risk field.
Maximum drawdown, recovery duration, downside capture and other compatible
risk-adjusted evidence remain `ไม่พบข้อมูลที่ยืนยันได้` from the reviewed daily
NAV sources. Expense ratio is `0.74%` and the fund distributes income quarterly.

## Sources

- [iShares IFFF/IDFF official product page](https://www.ishares.com/uk/individual/en/products/251848/ishares-msci-ac-far-east-exjapan-ucits-etf) — identity, objective, USD LSE listing, NAV/YTD, holdings, risk fields, expense ratio, benchmark and fund facts; accessed 2026-09-01
- [Official IFFF factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/ifff-ishares-msci-ac-far-east-ex-japan-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) — official 2016-2025 calendar NAV rows and benchmark rows, return basis and fund details as of 2026-06-30
- [MSCI AC Far East ex Japan Index](https://www.msci.com/indexes/index/892200/msci-ac-far-east-ex-japan-index) — underlying index scope and risk/return context
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-5]]
