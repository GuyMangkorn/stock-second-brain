---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:SCHA
ticker: SCHA
exchange: NYSE Arca
fund: Schwab U.S. Small-Cap ETF
tracked_index: Dow Jones U.S. Small-Cap Total Stock Market Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-07-31
annual_rows_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
rolling_10y_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/SCHA
  - geography/United-States
---

# SCHA Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

SCHA มี official NAV Total Return YTD `18.27%` ณ `2026-07-31` และ official
rolling 10-year NAV TR annualized `10.48%` ณ วันเดียวกัน. Schwab's full
calendar-year NAV table was not exposed in the reviewed issuer capture, so the
2016-2025 comparison below uses a secondary total-return proxy: cumulative
`152.02%` / rounded-input CAGR `9.68%`, versus S&P 500 TR `298.33%` / CAGR
`14.82%`. The same proxy gives 2021-2025 cumulative `37.23%` / CAGR `6.53%`,
versus S&P 500 `96.17%` / CAGR `14.43%`.

## Performance check

- entity_key: `NYSE Arca:SCHA`
- Fund: Schwab U.S. Small-Cap ETF
- Classification: passive, index-tracking U.S. small-cap equity ETF
- Inception: `2009-11-03`; primary listing: NYSE Arca
- Expense ratio: `0.03%`; Schwab states this operating expense ratio became effective `2026-06-11`
- Issuer benchmark: Dow Jones U.S. Small-Cap Total Stock Market Index; the index covers companies ranked 751-2,500 by full market capitalization and is float-adjusted market-cap weighted.
- Indexing approach: under normal circumstances at least 90% of net assets are invested in index securities; the fund generally seeks replication but may use sampling.
- NAV Total Return: USD NAV return with dividends and capital gains reinvested, net of fund expenses.
- Official current snapshot: NAV `US$35.64` and total net assets `US$23.67bn` as of `2026-08-14`; market price `US$35.65` at the same close from Schwab's ETF research page.
- Current official fields as of `2026-07-31`: NAV YTD `18.27%`, 1-year `31.71%`, 3-year annualized `14.88%`, 5-year annualized `7.25%`, and 10-year annualized `10.48%`.
- Common benchmark: S&P 500 Total Return, USD, dividends reinvested; cached complete-year reference as of `2025-12-31`.
- Annual-row caveat: the SCHA rows below are secondary proxy observations from ETFReplay's dividend-reinvested annual-return history, not issuer annual NAV rows. They are marked `*` and are not relabelled as official.

### Annual NAV TR

| Year | SCHA NAV TR* | S&P 500 TR |
|---|---:|---:|
| 2016 | 19.97%* | 11.96% |
| 2017 | 14.93%* | 21.83% |
| 2018 | -11.77%* | -4.38% |
| 2019 | 26.50%* | 31.49% |
| 2020 | 19.34%* | 18.40% |
| 2021 | 16.45%* | 28.71% |
| 2022 | -19.81%* | -18.11% |
| 2023 | 18.46%* | 26.29% |
| 2024 | 11.16%* | 25.02% |
| 2025 | 11.60%* | 17.88% |

The proxy compound for 2016-2025 is `152.02%` and rounded-input CAGR
`9.68%`; for 2021-2025 it is `37.23%` and CAGR `6.53%`. S&P 500 cached
compounds are `298.33%` / `14.82%` and `96.17%` / `14.43%`. Formula:
`CAGR = product(1 + annual return)^(1 / number of years) - 1`.

## Up years / Down years

- 2016-2025 proxy: 8 up years and 2 down years
- Best proxy year: `2019`, `+26.50%`
- Least-positive proxy year: `2025`, `+11.60%`
- Worst proxy year: `2022`, `-19.81%`
- Least-bad proxy down year: `2018`, `-11.77%`
- Current official YTD: `+18.27%` as of `2026-07-31`; no same-date S&P 500 current-year row is used because the cached benchmark ends at 2025-12-31.

## Risk read-through

SCHA เป็น passive U.S. small-cap broad equity ETF จึงมี small-cap volatility,
cyclicality, market-cap rotation และ downside exposure; prospectus ระบุว่า
index fund ไม่ลด market exposure ในช่วงตลาดขาลง. Schwab reports 3-year beta
`1.00` and standard deviation `19.78%` as of `2026-07-31`, with `1,711`
holdings as of `2026-08-13` and portfolio turnover `13.99%` as of
`2026-07-31`. Schwab's official performance capture reports best three-month
return `+33.21%` and worst three-month return `-31.61%`; official daily NAV
history sufficient for a numeric maximum drawdown and recovery calculation was
not verified, so no daily drawdown proxy is saved.

## Recent distributions

| Ex-date | Payable date | Distribution (USD) |
|---|---|---:|
| 2026-06-24 | 2026-06-29 | 0.1004 |
| 2026-03-25 | 2026-03-30 | 0.0384 |

These are official Schwab distribution records; distributions are not added
again to the NAV Total Return calculations.

## Sources

- [Schwab SCHA product page](https://www.schwabassetmanagement.com/products/scha) — official objective, index, expense ratio, current NAV/AUM/holdings, current NAV returns, risk fields and distributions
- [Schwab SCHA documents](https://www.schwabassetmanagement.com/products/scha/documents) — official factsheet, performance summary, reports and distribution links
- [Schwab SCHA ETF research](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=scha) — official Schwab research capture for 2026-07-31 current returns and best/worst three-month observations
- [SEC SCHA summary prospectus](https://www.sec.gov/Archives/edgar/data/1454889/000110465925123320/tm2526338-13_497k.htm) — objective, 90% index policy, indexing strategy and small-cap/index risks
- [ETFReplay SCHA annual total-return history](https://www.etfreplay.com/etf/scha) — secondary dividend-reinvested annual proxy rows, not treated as official issuer NAV rows
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
