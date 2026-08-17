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
updated: 2026-08-17
performance_as_of: 2026-07-29
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-29
price_nav_as_of: 2026-07-29
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
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

CPLCF เป็น OTC input alias ของ official USD London listing `CUSS` ของ iShares MSCI USA Small Cap CTB Enhanced ESG UCITS ETF (ISIN `IE00B3VWM098`). กองทุนเป็น passive physical/optimised U.S. small-cap equity ETF. Official iShares annual NAV Total Return 2016-2025 compound เป็น `157.28%` หรือ rounded-input CAGR `9.91%`; 2021-2025 CAGR เป็น `6.73%`. Current official NAV TR YTD คือ `14.97%` ณ 2026-07-29.

## Performance check

- entity_key: LSE:CUSS
- Input alias: CPLCF (OTC); canonical USD listing: `LSE:CUSS`; same fund ISIN `IE00B3VWM098`
- Inception: 2009-07-01
- Metric: NAV Total Return with gross income reinvested where applicable, after ongoing charges
- Tracked index (current issuer benchmark): MSCI USA Small Cap ESG Enhanced Focus CTB Index
- Benchmark history note: the fund changed name/objective and benchmark on 2022-06-01; before that date the benchmark was MSCI USA Small Cap Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- Total Expense Ratio: `0.43%`
- 2016-2025 calendar NAV TR: cumulative `157.28%`; rounded-input CAGR `9.91%`
- 2021-2025 calendar NAV TR: cumulative `38.51%`; rounded-input CAGR `6.73%`
- Current NAV TR YTD: `14.97%` as of 2026-07-29; NAV quote `US$675.97` as of the same date

| Year | CUSS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 19.13% | 11.96% |
| 2017 | 16.49% | 21.83% |
| 2018 | -10.49% | -4.38% |
| 2019 | 26.56% | 31.49% |
| 2020 | 18.15% | 18.40% |
| 2021 | 18.86% | 28.71% |
| 2022 | -16.94% | -18.11% |
| 2023 | 15.63% | 26.29% |
| 2024 | 10.71% | 25.02% |
| 2025 | 9.60% | 17.88% |

S&P 500 rows reuse the project’s cached USD total-return convention for complete calendar years 2016-2025; market-price return is not mixed.

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016-2025
- Best: 2019, `26.56%`
- Least positive: 2025, `9.60%`
- Worst: 2022, `-16.94%`
- Least bad down year: 2018, `-10.49%`
- 2016-2025 rounded-input CAGR: `9.91%`; 2021-2025 rounded-input CAGR: `6.73%`
- Current NAV TR YTD: `14.97%` as of 2026-07-29; secondary S&P 500 current cross-check `10.14%` as of 2026-07-31 is two days later and is not used as a synchronized spread

## Risk read-through

CUSS เป็น U.S. small-cap exposure ที่มี small-cap, cyclicality, liquidity และ ESG-screen/index-methodology risk. Official iShares รายงาน 3-year standard deviation `18.39%` ณ 2026-06-30, 3-year beta `1.000`, holdings `1,510` ณ 2026-07-30 และเป็น accumulating share class. Physical/optimised structure ไม่ได้แปลว่าจะไม่มี tracking difference. Official daily NAV history สำหรับ maximum drawdown และ recovery ไม่ได้ถูกยืนยันใน capture นี้.

## Driver notes

- Confirmed structure: passive physical/optimised exposure to an MSCI USA small-cap ESG-enhanced index; the share class accumulates income rather than distributing it.
- Methodology break: 2022-06-01 benchmark/name change means issuer benchmark comparisons across 2016-2025 are not one continuous benchmark series; common S&P 500 TR is shown separately for consistent cross-ETF reference.
- Observed regime points: 2019 was the strongest complete year at `+26.56%`, while 2022 was the weakest at `-16.94%`. These are return observations, not causal event attribution.
- Alias resolution: CPLCF is preserved as the input alias; durable ownership uses official USD `LSE:CUSS` and ISIN `IE00B3VWM098`.

## Sources

- [iShares official CUSS product page](https://www.ishares.com/uk/individual/en/products/253480/cuss?siteEntryPassthrough=true&switchLocale=y) — official identity, name/benchmark change, listings, ISIN, index, NAV, YTD, expense ratio, risk fields and calendar NAV TR rows
- [iShares official CUSS professional page](https://www.ishares.com/uk/professional/en/products/253480/csuss) — USD share-class facts, holdings, benchmark and risk characteristics
- [iShares official CUSS factsheet](https://www.ishares.com/ch/privatkunden/de/literature/fact-sheet/csuss-ishares-msci-usa-small-cap-ctb-enhanced-esg-ucits-etf-fund-fact-sheet-de-ch.pdf) — official calendar NAV performance and NAV-return definition
- [London Stock Exchange CUSS page](https://www.londonstockexchange.com/stock/CUSS/ishares/company-page) — USD listing cross-check and current listing identity
- [Slickcharts S&P 500 YTD total return](https://www.slickcharts.com/sp500/returns/ytd) — secondary current benchmark cross-check through 2026-07-31
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as-of 2025-12-31
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
