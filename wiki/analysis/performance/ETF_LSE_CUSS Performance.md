---
type: etf-performance
instrument_type: ETF
entity_key: LSE:CUSS
ticker: CUSS
input_alias: CPLCF
exchange: London Stock Exchange
fund: iShares MSCI USA Small Cap CTB Enhanced ESG UCITS ETF USD (Acc)
tracked_index: MSCI USA Small Cap ESG Enhanced Focus CTB Index
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2026-07-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/CUSS
  - ticker/CPLCF
  - geography/United-States
---

# CUSS Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

CPLCF เป็น OTC input alias ของ official USD London listing `CUSS` ของ iShares MSCI USA Small Cap CTB Enhanced ESG UCITS ETF (ISIN `IE00B3VWM098`). กองทุนเป็น passive physical/optimised U.S. small-cap equity ETF. Official iShares July factsheet annual NAV Total Return 2016-2025 compound เป็น `157.28%` หรือ rounded-input CAGR `9.91%`; 2021-2025 CAGR เป็น `6.73%`. Current official product-page capture แสดง NAV `US$708.60` ณ 2026-08-27 และ NAV TR YTD `20.54%` ณ 2026-08-26; July standardized YTD ที่เป็นคนละ window คือ `16.40%` ณ 2026-07-31.

## Performance check

- entity_key: LSE:CUSS
- Input alias: CPLCF (OTC); canonical USD listing: `LSE:CUSS`; same fund ISIN `IE00B3VWM098`; Bloomberg `CUSS LN`; RIC `CUSS.L`
- Inception: 2009-07-01
- Metric: NAV Total Return with gross income reinvested where applicable, after ongoing charges
- Tracked index (current issuer benchmark): MSCI USA Small Cap ESG Enhanced Focus CTB Index
- Benchmark history note: the fund changed name/objective and benchmark on 2022-06-01; before that date the benchmark was MSCI USA Small Cap Index, while the current benchmark is MSCI USA Small Cap ESG Enhanced Focus CTB Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- Total Expense Ratio: `0.43%`
- 2016-2025 calendar NAV TR: cumulative `157.28%`; rounded-input CAGR `9.91%`
- 2021-2025 calendar NAV TR: cumulative `38.51%`; rounded-input CAGR `6.73%`
- Current NAV TR YTD: `20.54%` as of 2026-08-26; current NAV quote `US$708.60` as of 2026-08-27
- July standardized NAV TR YTD: `16.40%` as of 2026-07-31; the later current field is retained separately and is not backfilled into the July table
- July standardized fund/index 5-year NAV TR: `6.84%` / `6.99%` annualized; the factsheet does not expose a July 10-year annualized field, so the 10-year calendar-window CAGR below is calculated from the complete annual rows

| Year | CUSS NAV TR | iShares issuer benchmark TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 19.13% | 19.15% | 11.96% |
| 2017 | 16.49% | 16.75% | 21.83% |
| 2018 | -10.49% | -10.40% | -4.38% |
| 2019 | 26.56% | 26.74% | 31.49% |
| 2020 | 18.15% | 18.32% | 18.40% |
| 2021 | 18.86% | 19.11% | 28.71% |
| 2022 | -16.94% | -16.79% | -18.11% |
| 2023 | 15.63% | 15.53% | 26.29% |
| 2024 | 10.71% | 11.02% | 25.02% |
| 2025 | 9.60% | 9.77% | 17.88% |

The iShares issuer benchmark rows are the official comparison series, but the benchmark changed from MSCI USA Small Cap Index to MSCI USA Small Cap ESG Enhanced Focus CTB Index on 2022-06-01. S&P 500 rows reuse the project’s cached USD total-return convention for complete calendar years 2016-2025; market-price return is not mixed.

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016-2025
- Best: 2019, `26.56%`
- Least positive: 2025, `9.60%`
- Worst: 2022, `-16.94%`
- Least bad down year: 2018, `-10.49%`
- 2016-2025 rounded-input CAGR: `9.91%`; 2021-2025 rounded-input CAGR: `6.73%`
- July standardized NAV TR YTD: `16.40%` as of 2026-07-31; current official NAV TR YTD: `20.54%` as of 2026-08-26; these are separate windows and are not treated as a synchronized spread
- Current official NAV: `US$708.60` as of 2026-08-27

## Risk read-through

CUSS เป็น U.S. small-cap exposure ที่มี small-cap, cyclicality, liquidity และ ESG-screen/index-methodology risk. Official iShares current page reports holdings `1,509`, P/B `2.62`, P/E `21.42` and net assets `US$3.257B` as of 2026-08-24; the July factsheet reports 3-year standard deviation `18.55%`, 3-year beta `1.00`, holdings `1,510`, P/B `2.54x` and P/E `21.23x` as of 2026-07-31/2026-08-07. The share class is accumulating and physical/optimised; that structure does not eliminate tracking difference. Official daily NAV history for maximum drawdown and recovery was not verified.

## Driver notes

- Confirmed structure: passive physical/optimised exposure to an MSCI USA small-cap ESG-enhanced index; the share class accumulates income rather than distributing it.
- Methodology break: 2022-06-01 benchmark/name change means issuer benchmark comparisons across 2016-2025 are not one continuous benchmark series; common S&P 500 TR is shown separately for consistent cross-ETF reference.
- Observed regime points: 2019 was the strongest complete year at `+26.56%`, while 2022 was the weakest at `-16.94%`. These are return observations, not causal event attribution.
- Benchmark context: the 2022 index/name change limits interpretation of long-window fund-minus-benchmark differences; current benchmark comparison is retained with that methodology break visible.
- Alias resolution: CPLCF is preserved as the input alias; durable ownership uses official USD `LSE:CUSS` and ISIN `IE00B3VWM098`.

## Sources

- [BlackRock/iShares official CUSS product page](https://www.blackrock.com/uk/individual/products/253480/ishares-msci-usa-small-cap-ctb-enhanced-esg-ucits-etf) — official current NAV/YTD, identity, name/benchmark change, listings, ISIN, index, expense ratio, risk fields and calendar NAV TR rows
- [iShares official CUSS professional page](https://www.ishares.com/uk/professional/en/products/253480/csuss) — USD share-class facts, holdings, benchmark and risk characteristics
- [iShares official July CUSS USD factsheet](https://www.ishares.com/gls-download/literature/fact-sheet/csuss-ishares-msci-usa-small-cap-ctb-enhanced-esg-ucits-etf-fund-fact-sheet-en-gb.pdf) — official calendar NAV/benchmark performance, July standardized returns and NAV-return definition
- [London Stock Exchange CUSS page](https://www.londonstockexchange.com/stock/CUSS/ishares/company-page) — USD listing cross-check and current listing identity
- [Slickcharts S&P 500 YTD total return](https://www.slickcharts.com/sp500/returns/ytd) — secondary current benchmark cross-check through 2026-07-31
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as-of 2025-12-31
- ETF source batch: [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
