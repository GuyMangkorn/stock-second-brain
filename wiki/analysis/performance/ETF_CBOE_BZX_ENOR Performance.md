---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:ENOR
ticker: ENOR
exchange: Cboe BZX
fund: iShares MSCI Norway Capped ETF
tracked_index: MSCI Norway IMI 25/50 Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-17
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/ENOR
  - geography/Norway
---

# ENOR Performance

> Navigation: [[ETF Region Index]] → [[Norway ETF]] → [[ETF Performance Index]]

## Bottom line

ENOR เป็น passive single-country Norway equity ETF ที่ track `MSCI Norway IMI
25/50 Index (Net)`. Official complete calendar rows 2016-2025 ให้ cumulative
`NAV Total Return` `113.09%` และ rounded-input CAGR `7.86%`, เป็นบวก 7 ปีและลบ
3 ปี. ปีดีที่สุดคือ 2025 ที่ `+32.58%` และแย่ที่สุดคือ 2022 ที่ `-12.58%`; official
rolling 10-year NAV TR CAGR คือ `8.63%` ณ 2026-06-30 และ current NAV TR YTD คือ
`+30.82%` ณ 2026-08-14.

## Performance check

- `entity_key: Cboe BZX:ENOR`; inception `2012-01-23`; exchange `Cboe BZX`; CUSIP `46429B499`.
- Metric: `NAV Total Return` in USD; returns assume reinvestment of dividends/distributions and reflect fund expenses.
- Tracked index (issuer benchmark): `MSCI Norway IMI 25/50 Index (Net)`.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ ENOR).
- Expense ratio and management fee `0.53%`; semi-annual distributions; official NAV `US$36.24`, closing price `US$36.25`, net assets `US$88.78M`, and 60 holdings as of 2026-08-14/17.
- Official rolling performance as of 2026-06-30: NAV `1Y 19.10%`, `3Y 18.50%`, `5Y 7.00%`, `10Y 8.63%`, inception `5.03%`; tracked-index returns `19.24%`, `18.73%`, `7.29%`, `8.98%`, `5.36%`.
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`; cumulative NAV TR `128.90%` implies `Start TR value: 100.00` and `End TR value: 228.90`, with `Years: 10.00`.
- 10-year NAV TR CAGR: `8.63%`; Formula: `(End TR / Start TR)^(1 / Years) - 1`.
- Annual coverage: official 2016-2020 rows from the iShares summary prospectus and official 2021-2025 rows from the current iShares product/factsheet capture. The international iShares calendar page provides rounded one-decimal tracked-index rows for 2016-2020; exact 2021-2025 fund/index rows are retained from the U.S. product page/factsheet.
- S&P 500 cache 2016-2025: cumulative `298.33%`; rounded-input CAGR `14.82%` from USD total-return annual rows as of 2025-12-31.

| Year | ENOR NAV TR | MSCI Norway IMI 25/50 | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 17.76% | 17.9% | 11.96% |
| 2017 | 21.89% | 22.2% | 21.83% |
| 2018 | -8.54% | -8.1% | -4.38% |
| 2019 | 12.75% | 13.3% | 31.49% |
| 2020 | 3.49% | 3.9% | 18.40% |
| 2021 | 17.95% | 18.77% | 28.71% |
| 2022 | -12.58% | -12.89% | -18.11% |
| 2023 | 4.55% | 5.52% | 26.29% |
| 2024 | -2.67% | -2.37% | 25.02% |
| 2025 | 32.58% | 33.60% | 17.88% |

## Up years / Down years

- Complete fund rows 2016-2025: `7 / 3` up/down years; cumulative `113.09%`; rounded-input CAGR `7.86%`; population annual-return standard deviation `13.61%`.
- Best: 2025, `+32.58%`; least positive: 2023, `+4.55%`.
- Worst: 2022, `-12.58%`; least bad down year: 2018, `-8.54%`.
- Common 2021-2025 window: ENOR cumulative `39.11%` / rounded-input CAGR `6.82%`; tracked-index cumulative `42.40%` / rounded-input CAGR `7.32%`; arithmetic tracking gap approximately `-3.29 pp` cumulative and `-0.50 pp` CAGR.
- Cached S&P 500 TR common-window cumulative `96.17%` / CAGR `14.43%`; the arithmetic difference is a common-reference comparison, not alpha.
- Current YTD: ENOR NAV TR `+30.82%` ณ 2026-08-14. Older iShares captures have earlier as-of dates and are not mixed into this current YTD figure.

## Risk read-through

**10-year NAV CAGR:** `8.63%` ณ 2026-06-30. ENOR มี Norway/country และ
NOK-USD FX exposure พร้อม concentration ใน Energy `30.67%`, Financials `23.44%`,
Industrials `14.76%`, Consumer Staples `10.84%` และ Materials `8.85%` ณ
2026-08-14. Official 3-year standard deviation คือ `18.04%` และ equity beta
`0.19` ณ 2026-07-31; fact-sheet snapshot ณ 2026-06-30 รายงาน `17.73%` และ `0.24`.
Expense ratio คือ `0.53%`. Summary prospectus รายงาน best quarter `+24.23%` ใน
Q4 2020 และ worst quarter `-37.24%` ใน Q1 2020; สองตัวเลขนี้ไม่ใช่ maximum
drawdown. Official daily NAV maximum drawdown และ recovery date ยัง
`ไม่พบข้อมูลที่ยืนยันได้`.

Latest four official cash distributions คือ `US$1.560525` (2026-06-15),
`US$0.278392` (2025-12-16), `US$0.572276` (2025-06-16) และ `US$0.543072`
(2024-12-17): sum `US$2.954265`, average `US$0.738566` ต่อรอบ หรือประมาณ
`2.04%` ต่อรอบเทียบ closing price `US$36.25`; issuer trailing yield คือ
`5.28%` ณ 2026-07-31.

## Sources

- [iShares ENOR U.S. product page](https://www.ishares.com/us/products/239673/ishares-msci-norway-capped-etf) — identity, Cboe BZX, inception, current NAV/price, YTD, rolling/cumulative/calendar performance, holdings, exposures, fees and distributions.
- [iShares ENOR fact sheet](https://www.ishares.com/us/literature/fact-sheet/enor-ishares-msci-norway-etf-fund-fact-sheet-en-us.pdf) — official NAV return definition, 2021-2025 rows, annualized returns, exchange, fees and risk characteristics.
- [iShares ENOR summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-norway-capped-etf-8-31.pdf) — 2015-2020 annual NAV rows, strategy, return definition and best/worst quarter.
- [iShares ENOR international calendar page](https://www.ishares.com/ch/professionals/en/products/239673/ishares-msci-norway-capped-etf?switchLocale=Y) — rounded official 2016-2025 USD calendar rows and index cross-check.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
