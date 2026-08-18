---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWN
ticker: EWN
exchange: NYSE Arca
fund: iShares MSCI Netherlands ETF
tracked_index: MSCI Netherlands IMI 25/50 Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-30
price_nav_as_of: 2026-07-31
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EWN
  - geography/Netherlands
---

# EWN Performance

> Navigation: [[ETF Region Index]] → [[Netherlands ETF]] → [[ETF Performance Index]]

## Bottom line

EWN เป็น passive single-country Netherlands equity ETF ที่ track `MSCI
Netherlands IMI 25/50 Index (Net)`. Official complete calendar rows 2016-2025
ให้ cumulative `NAV Total Return` `197.74%` และ rounded-input CAGR `11.53%`,
เป็นบวก 8 ปีและลบ 2 ปี. ปีดีที่สุดคือ 2025 ที่ `+34.32%` และแย่ที่สุดคือ 2022
ที่ `-24.12%`; official rolling 10-year NAV TR CAGR คือ `14.28%` ณ 2026-06-30
และ current NAV TR YTD คือ `+19.46%` ณ 2026-07-30.

## Performance check

- `entity_key: NYSE Arca:EWN`; inception `1996-03-12`; exchange `NYSE Arca`; CUSIP `464286814`.
- Metric: `NAV Total Return` in USD; returns assume reinvestment of dividends/distributions and reflect fund expenses.
- Tracked index (issuer benchmark): `MSCI Netherlands IMI 25/50 Index (Net)`; index data before 2017-09-01 is the MSCI Netherlands Investable Market Index (Net), and the current index applies thereafter.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ EWN).
- Expense ratio `0.50%`; management fee `0.49%`; semi-annual distributions; official NAV `US$66.97`, closing price `US$66.82`, net assets `US$686.49M`, and 55 holdings as of 2026-07-31.
- Official rolling performance as of 2026-06-30: NAV `1Y 35.10%`, `3Y 21.05%`, `5Y 10.39%`, `10Y 14.28%`, inception `7.86%`; tracked-index returns `36.15%`, `21.63%`, `10.93%`, `14.81%`.
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`; cumulative NAV TR `279.85%` implies `Start TR value: 100.00` and `End TR value: 379.85`, with `Years: 10.00`.
- 10-year NAV TR CAGR: `14.28%`; Formula: `(End TR / Start TR)^(1 / Years) - 1`.
- Annual coverage: official 2016-2020 rows from the iShares summary prospectus and official 2021-2025 rows from the current iShares product/factsheet capture. The international iShares calendar page provides rounded one-decimal tracked-index rows for 2016-2020; exact 2021-2025 fund/index rows are retained from the U.S. product page/factsheet.
- S&P 500 cache 2016-2025: cumulative `298.33%`; rounded-input CAGR `14.82%` from USD total-return annual rows as of 2025-12-31.

| Year | EWN NAV TR | MSCI Netherlands IMI 25/50 | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 3.91% | 4.6% | 11.96% |
| 2017 | 33.40% | 33.9% | 21.83% |
| 2018 | -14.99% | -14.6% | -4.38% |
| 2019 | 31.34% | 32.0% | 31.49% |
| 2020 | 24.19% | 24.8% | 18.40% |
| 2021 | 22.39% | 23.28% | 28.71% |
| 2022 | -24.12% | -24.49% | -18.11% |
| 2023 | 21.34% | 22.46% | 26.29% |
| 2024 | 2.34% | 3.14% | 25.02% |
| 2025 | 34.32% | 35.15% | 17.88% |

## Up years / Down years

- Complete fund rows 2016-2025: `8 / 2` up/down years; cumulative `197.74%`; rounded-input CAGR `11.53%`; population annual-return standard deviation `19.61%`.
- Best: 2025, `+34.32%`; least positive: 2024, `+2.34%`.
- Worst: 2022, `-24.12%`; least bad down year: 2018, `-14.99%`.
- Common 2021-2025 window: EWN cumulative `54.90%` / rounded-input CAGR `9.15%`; tracked-index cumulative `58.90%` / rounded-input CAGR `9.71%`; arithmetic tracking gap approximately `-0.56 pp`.
- Cached S&P 500 TR common-window cumulative `96.17%` / CAGR `14.43%`; the arithmetic difference is a common-reference comparison, not alpha.
- Current YTD: EWN NAV TR `+19.46%` ณ 2026-07-30. A separate iShares international-locale capture reports `+18.46%` as of 2026-07-31; the U.S. USD product-page figure is used as primary and the conflict remains disclosed in the source batch.

## Risk read-through

**10-year NAV CAGR:** `14.28%` ณ 2026-06-30. EWN มี Netherlands/country และ
EUR-USD FX exposure พร้อม sector concentration ใน Information Technology
`36.57%`, Financials `22.07%`, Industrials `12.35%` และ Consumer Staples
`10.45%` ณ 2026-07-24. Official 3-year standard deviation คือ `18.76%` และ
equity beta `0.99` ณ 2026-06-30; expense ratio คือ `0.50%`. Summary prospectus
รายงาน best quarter `+25.30%` ใน Q2 2020 และ worst quarter `-22.21%` ใน Q1 2020;
สองตัวเลขนี้ไม่ใช่ maximum drawdown. Official daily NAV maximum drawdown และ
recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

Latest four official cash distributions คือ `US$0.676501` (2026-06-15),
`US$2.160893` (2025-12-16), `US$0.708587` (2025-06-16) และ `US$0.397063`
(2024-12-17): sum `US$3.943044`, average `US$0.985761` ต่อรอบ หรือประมาณ
`1.48%` ต่อรอบเทียบ closing price `US$66.82`; issuer 12m trailing yield คือ
`3.90%` ณ 2026-06-30.

## Sources

- [iShares EWN U.S. product page](https://www.ishares.com/us/products/239671/ishares-msci-netherlands-etf?fundSearch=true&qt=EWN) — identity, NYSE Arca, inception, current NAV/price, YTD, rolling/cumulative/calendar performance, holdings, exposures, fees and distributions.
- [iShares EWN fact sheet](https://www.ishares.com/us/literature/fact-sheet/ewn-ishares-msci-netherlands-etf-fund-fact-sheet-en-us.pdf) — official NAV return definition, 2021-2025 rows, annualized returns, exchange, fees and risk characteristics.
- [iShares EWN summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-netherlands-etf-8-31.pdf) — 2016-2020 annual NAV rows, strategy, return definition, index splice and best/worst quarter.
- [iShares EWN international calendar page](https://www.ishares.com/ch/professionals/en/products/239671/ishares-msci-netherlands-etf?switchLocale=Y) — rounded official 2016-2025 USD calendar rows and current-locale conflict noted above.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
