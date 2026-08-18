---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLEE
input_ticker: FLEE
ticker: FLEE
exchange: NYSE Arca
fund: Franklin FTSE Europe ETF
tracked_index: FTSE Developed Europe Capped Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_5y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-30
price_nav_as_of: 2026-08-07
fund_facts_as_of: 2026-08-06
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; dividends and capital gains distributions reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FLEE
  - geography/Europe
---

# FLEE Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`FLEE` คือ Franklin FTSE Europe ETF ที่จดทะเบียนบน NYSE Arca และเป็น
`passive-index` broad developed-Europe equity ETF สำหรับหุ้น large- และ
mid-cap โดยติดตาม `FTSE Developed Europe Capped Index`. กองทุนเริ่มเมื่อ
2 พ.ย. 2017 จึงยังไม่มี 10-year window ที่ครบถ้วน. Official complete-calendar
NAV rows ปี 2018-2025 compound ได้ `85.42%` หรือ rounded-input CAGR `8.02%`;
ช่วงร่วม 2021-2025 ได้ `65.12%` หรือ `10.55%` ต่อปี. Franklin rolling 5-year
NAV return คือ `9.73%` ณ 30 มิ.ย. 2026 และ latest official NAV TR YTD คือ
`+9.91%` ณ 30 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:FLEE`; official fund name, ticker, CUSIP `35473P652`, ISIN `US35473P6521`, NYSE Arca listing, and inception `2 พ.ย. 2017` are confirmed by Franklin and the SEC summary prospectus.
- Classification: `passive-index`. The SEC prospectus states that FLEE seeks to track the FTSE Developed Europe Capped Index, invests at least 80% in index components or depositary receipts, and may use representative sampling.
- Metric: Franklin `NAV total return` assumes reinvestment of distributions and deducts fund expenses. `S&P 500 Total Return` is a common USD reference only, not FLEE's tracked index.
- Tracked index: `FTSE Developed Europe Capped Index-NR`, a free-float-adjusted market-capitalization index of large- and mid-cap stocks from developed European countries with issuer-weight caps.
- Expense ratio: `0.09%`; distribution frequency: semi-annual; index reconstitution: semi-annual.
- Latest official performance: the Franklin product page reports NAV TR `1Y 18.91%`, `3Y 16.66%`, `5Y 9.73%`, and since inception `8.54%` as of 30 มิ.ย. 2026. The same page reports current NAV TR YTD `9.91%` as of 30 ก.ค. 2026; the factsheet's older 30 มิ.ย. YTD is `7.82%`, so the dates are kept separate rather than treated as a conflict.
- Official product snapshot as of 7 ส.ค. 2026: NAV `$40.28` and market price `$40.26`. Total net assets were `$120.83M` as of 9 ส.ค. 2026; 498 holdings, P/E `18.35x`, and P/B `2.65x` were reported as of 6 ส.ค. 2026.
- Official factsheet snapshot as of 30 มิ.ย. 2026: 3-year NAV standard deviation `13.63%`; country weights included United Kingdom `20.67%`, France `14.50%`, Germany `12.92%`, Switzerland `12.49%`, and Netherlands `8.80%`; sector weights included Financials `25.33%`, Industrials `18.96%`, Health Care `12.83%`, and Information Technology `9.40%`.

| Year | FLEE NAV TR (USD) | FTSE Developed Europe Capped Index-NR (USD) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2018 | -14.81% | -14.97% | -4.38% |
| 2019 | 24.09% | 23.84% | 31.49% |
| 2020 | 6.23% | 6.05% | 18.40% |
| 2021 | 16.21% | 16.05% | 28.71% |
| 2022 | -15.51% | -15.77% | -18.11% |
| 2023 | 20.93% | 20.23% | 26.29% |
| 2024 | 2.35% | 2.24% | 25.02% |
| 2025 | 35.87% | 35.58% | 17.88% |

Coverage/source note: FLEE and FTSE index rows are official Franklin calendar-year
returns for periods ended 31 ธ.ค. 2025. Current rolling, YTD, price, holdings,
portfolio and risk fields use their separately stated as-of dates. S&P 500 rows
are the cached USD total-return convention, dividends reinvested, as of
31 ธ.ค. 2025.

Official FLEE rows compound to `85.42%` / rounded-input CAGR `8.02%` for
2018-2025 and `65.12%` / `10.55%` for 2021-2025. The FTSE benchmark rows
compound to `81.92%` / `7.77%` and `62.91%` / `10.25%`; fund-minus-index
differences of approximately `+0.25 pp` and `+0.30 pp` are passive tracking
observations, not alpha. Cached S&P 500 TR compounds to `192.03%` / `14.33%`
for 2018-2025 and `96.17%` / `14.43%` for 2021-2025, so FLEE trails that common
reference by approximately `-6.31 pp` and `-3.88 pp` of CAGR.

The issuer rolling 5-year NAV return of `9.73%` as of 30 มิ.ย. 2026 is kept
separate from the `8.02%` calendar-derived CAGR because the windows and as-of
dates differ.

**Up years / Down years**

- Complete 2018-2025 NAV TR up/down: `6 / 2`
- Best NAV TR year: 2025, `+35.87%`
- Least positive year: 2024, `+2.35%`
- Worst NAV TR year: 2018, `-14.81%`
- Least bad down year: 2022, `-15.51%`
- Population standard deviation of the eight complete annual NAV returns: `17.18%`; the issuer's separate 3-year monthly standard deviation is `13.63%`.

## Risk read-through

FLEE กระจาย across developed Europe แต่ยังมี country และ sector concentration
โดย UK, France, Germany, Switzerland และ Netherlands รวมกันมากกว่าสองในสาม
ของ portfolio ใน factsheet ณ 30 มิ.ย. 2026. ความเสี่ยงหลักคือ European macro,
EUR/GBP/CHF-USD FX, foreign-market and regional political risk, large-/mid-cap
cyclicality, financials/industrials exposure และ passive tracking error. Official
daily NAV maximum drawdown และ recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Franklin FLEE product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26349/SINGLCLASS/franklin-ftse-europe-etf/FLEE) — official identity, rolling/YTD returns, price/NAV, assets, holdings, portfolio statistics and current dates.
- [Franklin FLEE factsheet](https://www.franklintempleton.com/forms-literature/download/FLEE-FF) — official calendar fund/index rows, benchmark, fee, country/sector exposures and 3-year risk statistics as of 30 มิ.ย. 2026.
- [SEC FLEE summary prospectus](https://www.sec.gov/Archives/edgar/data/1655589/000137949117007135/filing134981077.htm) — official exchange, objective, passive/indexing approach, 80% policy and regional/foreign-security risks.
- S&P 500 Total Return 2018-2025 cached convention from the workflow; USD dividends reinvested, as of 31 ธ.ค. 2025.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
