---
type: etf-performance
instrument_type: ETF
entity_key: LSE:ISEU
input_ticker: IMSEF
ticker: ISEU
exchange: London Stock Exchange
fund: iShares Core MSCI Europe UCITS ETF (EUR Distributing)
tracked_index: MSCI Europe Index
benchmark: MSCI Europe Index
management_mode: passive-index-tracking
updated: 2026-08-19
performance_as_of: 2025-12-31
rolling_performance_as_of: 2026-07-31
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-17
fund_facts_as_of: 2026-08-17
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; gross income reinvested; net of expenses
return_currency: EUR
tags:
  - analysis/etf-performance
  - ticker/ISEU
  - ticker/IMSEF
  - geography/Europe
---

# IMSEF / ISEU ETF Performance

> [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

IMSEF เป็น OTC input alias ของ iShares Core MSCI Europe UCITS ETF (EUR
Distributing), ISIN IE00B1YZSC51. iShares listing table ยืนยันว่า official
London Stock Exchange USD-traded line คือ ISEU; share class currency และ NAV
return basis ยังคงเป็น EUR. จึงต้องแยก USD เป็น listing currency ไม่ใช่
performance currency.

จาก official annual EUR NAV Total Return rows ที่ครบ 2016-2025 ผลตอบแทนสะสม
คือ 113.94% และ rounded-input calendar CAGR คือ 7.90%†. ใน common window
2021-2025 ผลตอบแทนสะสมคือ 72.27% หรือ CAGR 11.49%, positive/negative years
4/1. Current official product page รายงาน NAV TR YTD 13.81% ณ 2026-08-14
และ NAV EUR 41.11 ณ 2026-08-17. Official July factsheet รายงาน YTD 12.05%
ณ 2026-07-31; เป็นคนละ as-of snapshot ไม่ใช่ source conflict.

† เป็น CAGR ที่คำนวณจาก rounded official calendar rows ไม่ใช่ issuer rolling
10-year field. กองทุนเป็น passive physical optimized, TER 0.12%, distributing
quarterly และมี broad developed-Europe exposure. ความเสี่ยงหลักคือ equity
market, country/sector mix, FX, counterparty และความแตกต่างระหว่าง NAV
return ใน EUR กับราคาซื้อขายบน USD line.

## Identity and structure

| Field | Verified value |
|---|---|
| Input ticker | IMSEF |
| Official listing | LSE:ISEU, London Stock Exchange, USD line |
| Share-class identity | iShares Core MSCI Europe UCITS ETF (EUR Distributing) |
| ISIN | IE00B1YZSC51 |
| Share-class launch | 2007-07-06 |
| Fund | iShares Core MSCI Europe UCITS ETF |
| Structure | UCITS; Ireland; physical optimized replication |
| Management mode | Passive index-tracking |
| Benchmark | MSCI Europe Index |
| Share-class currency | EUR |
| Listing currency | USD on LSE ISEU line |
| TER | 0.12% |
| Income | Distributing; quarterly |
| Latest product-page NAV | EUR 41.11 as of 2026-08-17 |
| Holdings | 396 as of 2026-08-14 |
| Return currency | EUR |

## Official calendar performance

Official iShares July factsheet reports EUR Share Class NAV Total Return and
the EUR MSCI Europe benchmark. The table preserves the issuer's rounded annual
observations; calculations use these displayed inputs.

| Year | ISEU NAV TR | MSCI Europe |
|---|---:|---:|
| 2016 | 2.65% | 2.58% |
| 2017 | 10.29% | 10.24% |
| 2018 | -10.42% | -10.57% |
| 2019 | 26.42% | 26.05% |
| 2020 | -3.14% | -3.32% |
| 2021 | 25.44% | 25.13% |
| 2022 | -9.23% | -9.49% |
| 2023 | 16.13% | 15.83% |
| 2024 | 8.87% | 8.59% |
| 2025 | 19.67% | 19.39% |

### Calculated windows

| Window / metric | ISEU | Official benchmark |
|---|---:|---:|
| 2016-2025 cumulative | 113.94% | 109.60% |
| 2016-2025 rounded-input CAGR | 7.90%† | 7.68% |
| 2021-2025 cumulative | 72.27% | 70.07% |
| 2021-2025 rounded-input CAGR | 11.49% | 11.21% |
| 2021-2025 annual-return standard deviation, population | 11.97% | 11.96% |
| Positive / negative years, 2021-2025 | 4 / 1 | 4 / 1 |
| Best / worst year, 2021-2025 | 2025 +19.67% / 2022 -9.23% | 2025 +19.39% / 2022 -9.49% |

## Current and rolling official fields

As-of dates are intentionally separate because the product page has a later
NAV snapshot than the current YTD field and the July factsheet.

| Metric | Value | As of | Basis |
|---|---:|---|---|
| Current NAV TR YTD | 13.81% | 2026-08-14 | official product page |
| NAV | EUR 41.11 | 2026-08-17 | official product page |
| Factsheet YTD | 12.05% | 2026-07-31 | official July factsheet |
| 1-year NAV TR | 22.36% | 2026-07-31 | official July factsheet |
| 3-year annualized NAV TR | 14.28% | 2026-07-31 | official July factsheet |
| 5-year annualized NAV TR | 10.40% | 2026-07-31 | official July factsheet |
| Since-inception annualized NAV TR | 5.41% | 2026-07-31 | official July factsheet |
| 3-year standard deviation | 10.59% | 2026-07-31 | official product page |
| 3-year beta | 1.002 | 2026-07-31 | official product page |

## Benchmark tracking and currency basis

Fund-minus-benchmark observations from the official displayed rows are
+0.31, +0.26, +0.30, +0.28, and +0.28 percentage points for 2021-2025.
These are passive tracking observations after fees and rounding; they are not
labeled alpha or manager skill.

The cached S&P 500 Total Return convention remains a separate USD common
reference. It is not compared arithmetically with ISEU's EUR NAV returns because
the currencies and market exposures differ. The official MSCI Europe benchmark
is the strategy-appropriate comparator for this share class.

## Risk read-through

The official sources identify equity-market and counterparty risks, and the
product is exposed to developed-Europe country, sector and currency movements.
The official page's current sector snapshot includes financials, industrials,
health care and information technology among the largest sectors; allocations
are subject to change. The official 3-year standard deviation is 10.59% and
beta is 1.002 as of 2026-07-31. Official daily NAV maximum drawdown and
recovery date were not disclosed in the reviewed sources.

## Sources

- [iShares product page](https://www.ishares.com/uk/individual/en/products/251860/ishares-msci-%20europe-ucits-etf-inc-fund) — official identity, share class, current NAV/YTD, holdings, benchmark, risk fields and LSE listing table.
- [iShares July 2026 factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/imeu-ishares-core-msci-europe-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) — official EUR annual NAV/benchmark rows, rolling performance, TER, holdings and dated fund facts.
- [DTCC OTC notice](https://www.dtcc.com/-/media/Files/pdf/2016/5/16/OTC-094.pdf) — OTC symbol IMSEF and iShares II plc MSCI Europe EUR UCITS ETF identity cross-check.
- [[ETF_performance_sources_2026-08-19]] — source map, raw observations, calculations, reconciliation and scheduled-local verification record.

## Follow-up

- Refresh the official product-page YTD and NAV together on the next run, retaining the July factsheet snapshot.
- Verify official daily NAV drawdown/recovery if a suitable dated series becomes available.
- Keep the EUR NAV return, USD LSE listing currency and any USD market-price observation separate.
