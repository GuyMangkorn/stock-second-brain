---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWO
ticker: EWO
exchange: NYSE Arca
fund: iShares MSCI Austria ETF
tracked_index: MSCI Austria IMI 25/50 Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-11
price_nav_as_of: 2026-08-12
fund_facts_as_of: 2026-08-12
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EWO
  - geography/Austria
---

# EWO Performance

> Navigation: [[ETF Region Index]] → [[Austria ETF]] → [[ETF Performance Index]]

## Bottom line

EWO ให้ cumulative `NAV Total Return` ประมาณ `217.16%` ใน complete calendar
years 2016-2025 หรือ rounded-input CAGR `12.23%`; บวก 7 ปีและลบ 3 ปี. ปีดีที่สุด
คือ 2025 `+72.85%` และแย่ที่สุดคือ 2018 `-23.20%`. Current official NAV TR YTD
คือ `+25.85%` ณ 2026-08-11. ใน common window 2021-2025 EWO ให้ CAGR
`17.28%` เทียบ S&P 500 TR `14.43%`; official rolling 5Y NAV TR `17.46%`
เทียบ tracked index `17.41%` หรือ gap `+0.05 pp`.

## Performance check

- `entity_key: NYSE Arca:EWO`; inception `1996-03-12`; exchange `NYSE Arca`.
- Metric: `NAV Total Return` (USD), distributions reinvested หลังหัก fund expenses.
- Tracked index (issuer benchmark): `MSCI Austria IMI 25/50 Index (Net)`; index changed from MSCI Austria Investable Market Index on 2013-02-12.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ EWO).
- Expense ratio `0.49%`; distribution frequency semi-annual; official net assets `US$204.1M`, NAV `US$43.88` ณ 2026-08-12, closing price `US$43.72` ณ 2026-08-11.
- Official rolling performance ณ 2026-06-30: NAV TR `1Y 46.02%`, `3Y 34.15%`, `5Y 17.46%`, `10Y 15.59%`; tracked-index `47.39%`, `34.39%`, `17.41%`, `15.61%`.
- Current official YTD NAV TR: `+25.85%` ณ 2026-08-11. Same-date tracked-index YTD was not disclosed in the reviewed current page.
- Annual coverage: official complete calendar years 2016-2025; 2016-2020 issuer table values are rounded to one decimal and 2021-2025 use official U.S. factsheet/page values to two decimals.
- S&P 500 cache 2016-2025: cumulative `298.33%`; CAGR `14.82%` from rounded annual inputs.

| ปี | EWO NAV TR | MSCI Austria IMI 25/50 | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 7.10% | 7.40% | 11.96% |
| 2017 | 52.50% | 52.80% | 21.83% |
| 2018 | -23.20% | -23.20% | -4.38% |
| 2019 | 17.70% | 17.90% | 31.49% |
| 2020 | -3.20% | -3.50% | 18.40% |
| 2021 | 30.74% | 31.65% | 28.71% |
| 2022 | -21.67% | -22.13% | -18.11% |
| 2023 | 19.88% | 19.30% | 26.29% |
| 2024 | 4.58% | 4.25% | 25.02% |
| 2025 | 72.85% | 74.54% | 17.88% |

## Up years / Down years

- Up years / Down years: `7 / 3` ใน 2016-2025.
- Best: 2025, `+72.85%`; least positive: 2024, `+4.58%`.
- Worst: 2018, `-23.20%`; least bad down year: 2020, `-3.20%`.
- 2016-2025 EWO cumulative `217.16%` / CAGR `12.23%`; 2021-2025 cumulative `121.92%` / CAGR `17.28%`.
- 2021-2025 S&P 500 TR cumulative `96.17%` / CAGR `14.43%`; EWO outperformed by about `+2.85 pp` CAGR in this common reference window.
- Current YTD: EWO NAV `+25.85%` ณ 11 ส.ค. 2026; this is not compared with a same-date S&P or tracked-index return.

## Risk read-through

EWO เป็น passive single-country Austria equity exposure. Portfolio ณ
2026-08-11 มี Financials `50.04%`, Industrials `14.23%`, Materials `11.00%`,
Energy `9.44%`, Utilities `5.96%` และ 21 holdings. Official 3-year standard
deviation คือ `15.22%`, equity beta `0.51`, P/E `14.76` และ P/B `1.61`.
Main risks are Austria country concentration, financials/industrial/materials
sector concentration, EUR/USD FX, and lower liquidity than broad Europe ETFs.
Official daily NAV maximum drawdown and recovery date are `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [iShares EWO product page](https://www.ishares.com/us/products/239609/ishares-msci-austria-etf) — current YTD, fund facts, exposures, and fees.
- [iShares EWO factsheet](https://www.ishares.com/us/literature/fact-sheet/ewo-ishares-msci-austria-etf-fund-fact-sheet-en-us.pdf) — official calendar 2021-2025, rolling returns, benchmark, index transition, and risk characteristics as of 2026-06-30.
- [BlackRock EWO calendar-year performance](https://www.ishares.com/ch/professionals/en/products/239609/ishares-msci-austria-capped-etf?switchLocale=Y) — official USD calendar rows 2016-2025.
- [EWO summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-austria-capped-etf-8-31.pdf) — strategy and risk disclosures.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
