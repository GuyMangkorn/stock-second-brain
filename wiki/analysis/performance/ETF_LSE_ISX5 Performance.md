---
type: etf-performance
instrument_type: ETF
entity_key: LSE:ISX5
input_ticker: IVVPF
ticker: ISX5
exchange: London Stock Exchange
fund: iShares Core EURO STOXX 50 UCITS ETF
tracked_index: STOXX Eurozone 50 (Net Return)
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: not-issuer-disclosed
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; gross income reinvested; fund expenses reflected in NAV
return_currency: EUR share-class NAV; S&P 500 reference is USD
tags:
  - analysis/etf-performance
  - ticker/ISX5
  - ticker/IVVPF
  - geography/Europe
---

# ISX5 Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`IVVPF` เป็น OTC input alias ของ official USD London Stock Exchange line
`LSE:ISX5` สำหรับ iShares Core EURO STOXX 50 UCITS ETF, ISIN
`IE00B53L3W79`. กองทุนเป็น passive, physical, accumulating UCITS equity ETF
ที่ติดตาม `STOXX Eurozone 50 (Net Return)`. Official 2016-2025 NAV TR rows
ให้ cumulative `138.31%` และ rounded-input calendar CAGR `9.07%`; มี 7 ปีบวก
และ 3 ปีลบ. Common 2021-2025 ให้ cumulative `88.08%` / CAGR `13.47%` เทียบ
S&P 500 TR `96.17%` / `14.43%` โดยต้องระวังว่า share-class NAV เป็น EUR
ขณะที่ common reference เป็น USD. Latest official NAV TR YTD คือ `15.37%`
ณ 14 ส.ค. 2026.

## Performance check

- `entity_key: LSE:ISX5`; `input_ticker: IVVPF`. The issuer listing table maps
  the same ISIN's USD London line to `ISX5`; the OTC symbol is retained only as
  an input alias.
- Classification: `passive-index`; physically replicated, accumulating,
  Ireland-domiciled UCITS equity ETF. Share-class inception: 26 ม.ค. 2010;
  total expense ratio `0.10%`.
- Metric: issuer `NAV Total Return` with gross income reinvested where
  applicable; market-price return is not mixed.
- Tracked index: `STOXX Eurozone 50 (Net Return)`. Issuer factsheet calendar
  rows are shown beside the common `S&P 500 Total Return` reference.
- Current official snapshot: NAV `€254.66` and NAV TR YTD `15.37%` as of
  14 ส.ค. 2026; net assets `€7.98bn` and 50 holdings as of 14 ส.ค. 2026.
- Official rolling fields from the July 2026 factsheet: 5-year annualised NAV
  TR `12.45%`, 3-year annualised `15.62%`, and since-inception annualised
  `8.43%`, all as of 31 ก.ค. 2026.
- Income structure: `Accumulating`; no cash distribution or yield is inferred.

| Year | ISX5 NAV TR (EUR) | STOXX Eurozone 50 NR (EUR) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2016 | 4.37% | 3.72% | 11.96% |
| 2017 | 9.70% | 9.15% | 21.83% |
| 2018 | -11.56% | -12.03% | -4.38% |
| 2019 | 28.86% | 28.20% | 31.49% |
| 2020 | -2.89% | -3.20% | 18.40% |
| 2021 | 23.98% | 23.34% | 28.71% |
| 2022 | -9.04% | -9.49% | -18.11% |
| 2023 | 22.78% | 22.23% | 26.29% |
| 2024 | 11.54% | 11.01% | 25.02% |
| 2025 | 21.78% | 21.20% | 17.88% |

Official iShares rows are complete calendar-year NAV returns from the July 2026
factsheet. The S&P 500 rows reuse the cached USD Total Return convention as of
2025-12-31; currencies and tracked-index definitions remain separate.

## Up years / Down years

- Complete 2016-2025 NAV TR up/down: `7 / 3`
- Best NAV TR year: 2019, `+28.86%`
- Least positive year: 2016, `+4.37%`
- Worst NAV TR year: 2018, `-11.56%`
- Least bad down year: 2022, `-9.04%`
- 2016-2025 cumulative/CAGR: `138.31%` / `9.07%`; CAGR is compounded from
  rounded official annual inputs, not an issuer-labeled rolling-10-year field.
- Common 2021-2025 NAV TR cumulative/CAGR: `88.08%` / `13.47%`.
- Common 2021-2025 tracked-index cumulative/CAGR: `83.59%` / `12.92%`;
  arithmetic difference is approximately `+0.55 pp` CAGR and is not alpha.
- Latest official NAV TR YTD: `+15.37%` as of 14 ส.ค. 2026.

## Risk read-through

ISX5 provides concentrated large-cap Eurozone exposure: the official 14 ส.ค.
2026 snapshot was led by Financials `28.29%`, Industrials `22.17%`, and
Information Technology `14.98%`. Official 3-year standard deviation was
`12.53%` as of 31 ก.ค. 2026, with beta `1.003`; the displayed 2016-2025
annual-return population standard deviation is `13.71%` from the ten official
rows. The fund's 0.10% TER and accumulating structure support low cash-flow
friction, but country, sector, EUR/USD and Eurozone macro risks remain. A
daily-NAV maximum drawdown and recovery date were not disclosed in the reviewed
official capture, so no price-only proxy is substituted.

## Sources

- [iShares Core EURO STOXX 50 UCITS ETF product page](https://www.ishares.com/uk/individual/en/products/253712/CSSX5E?siteEntryPassthrough=true) — official listings, ISIN, NAV/YTD, fund facts, risk snapshot and exposure
- [iShares CSX5 factsheet, July 2026](https://www.ishares.com/gls-download/literature/fact-sheet/cssx5e-ishares-core-euro-stoxx-50-ucits-etf-fund-fact-sheet-en-gb.pdf) — official 2016-2025 NAV/index rows, rolling returns, structure and trading information
- [Boursorama IVVPF quote](https://www.boursorama.com/bourse/trackers/cours/3kIVVPF/) — OTC alias and ISIN cross-check only; not primary NAV performance evidence
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
