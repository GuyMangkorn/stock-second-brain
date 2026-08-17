---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:FYX
ticker: FYX
exchange: Nasdaq
fund: First Trust Small Cap Core AlphaDEX® Fund
tracked_index: Nasdaq AlphaDEX Small Cap Core™ Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-06-30
annual_rows_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-08-03
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FYX
  - geography/United-States
---

# FYX Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

FYX ให้ผลตอบแทนแบบ `NAV Total Return` สะสม `183.16%` หรือ rounded-input CAGR `10.97%` ในช่วง 2016-2025 เทียบกับ S&P 500 Total Return ที่ `298.33%` และ CAGR `14.82%`. ช่วง 2021-2025 สะสม `55.67%` หรือ CAGR `9.25%` เทียบกับ S&P 500 ที่ `96.17%` และ CAGR `14.43%`; มี 8 ปีบวกและ 2 ปีลบ. Current official NAV TR YTD คือ `28.10%` ณ `2026-06-30`.

## Performance check

- entity_key: `NASDAQ:FYX`
- Fund: First Trust Small Cap Core AlphaDEX® Fund
- Classification: passive, rules-based enhanced-index U.S. small-cap equity ETF
- Inception: `2007-05-08`; primary listing: Nasdaq
- Expense ratio: `0.58%`; contractual cap `0.70%` at least through `2026-11-30`
- Issuer benchmark: Nasdaq AlphaDEX Small Cap Core™ Index (`NQDXUSSCT`), reconstituted and rebalanced quarterly
- Index methodology: Nasdaq ranks the Nasdaq US 700 Small Cap universe on growth/value factors, selects the top 525 names, and weights them by ranking quintile. This is an enhanced indexing methodology, not discretionary active management.
- NAV Total Return: USD NAV return with distributions reinvested and fund expenses reflected in NAV.
- Common benchmark: S&P 500 Total Return, USD, dividends reinvested; cached reference as of `2025-12-31`.
- 10-year window: `2016-06-30` to `2026-06-30`; issuer rolling 10-year NAV TR CAGR `13.26%` as of `2026-06-30`. Raw start/end NAV TR values are not disclosed in the reviewed issuer capture, so this issuer field is kept separate from the 2016-2025 calendar CAGR `10.97%`.
- Current quote snapshot: NAV `US$144.29` and market price `US$144.27` as of `2026-08-03`.
- Coverage/source note: all 2016-2025 annual rows below are official First Trust factsheet observations; 2026 YTD is a partial period and is excluded from annual ranking.

### Annual NAV TR

| Year | FYX NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 22.72% | 11.96% |
| 2017 | 14.45% | 21.83% |
| 2018 | -10.26% | -4.38% |
| 2019 | 21.04% | 31.49% |
| 2020 | 19.23% | 18.40% |
| 2021 | 27.48% | 28.71% |
| 2022 | -18.39% | -18.11% |
| 2023 | 18.12% | 26.29% |
| 2024 | 12.20% | 25.02% |
| 2025 | 12.90% | 17.88% |

2016-2025 FYX compound คือ `183.16%` และ rounded-input CAGR `10.97%`; 2021-2025 compound คือ `55.67%` และ CAGR `9.25%`. S&P 500 cached compound อยู่ที่ `298.33%` / `14.82%` และ `96.17%` / `14.43%` ตามลำดับ. สูตรคือ `CAGR = product(1 + annual return)^(1 / number of years) - 1`.

## Up years / Down years

- 2016-2025: 8 up years and 2 down years
- Best year: `2021`, `+27.48%`
- Least-positive year: `2024`, `+12.20%`
- Worst year: `2022`, `-18.39%`
- Least-bad down year: `2018`, `-10.26%`
- Current YTD: `+28.10%` as of `2026-06-30`; no synchronized current-year S&P 500 row is used because the cached benchmark ends at 2025-12-31.

## Risk read-through

FYX เป็น U.S. small-cap rules-based ETF ที่มีความเสี่ยงจาก small-cap cyclicality, growth/value rotation, quarterly turnover, sector concentration, liquidity และการที่ index fund ไม่ลด exposure ในช่วงตลาดขาลง. First Trust reports 3-year standard deviation `19.91%`, beta `1.02`, Sharpe ratio `0.87`, and correlation `0.99` versus the S&P SmallCap 600 Index, all as of `2026-06-30`. Prospectus risk history records a best quarter of `+33.21%` in Q4 2020 and a worst quarter of `-36.40%` in Q1 2020. Official daily NAV history sufficient for a numeric maximum drawdown and recovery calculation was not verified, so no drawdown proxy is saved.

## Recent distributions

| Ex-date | Payable date | Distribution (USD) |
|---|---|---:|
| 2026-06-25 | 2026-06-30 | 0.4369 |
| 2026-03-26 | 2026-03-31 | 0.2029 |

The reviewed official distribution page exposed the two 2026 records above; older rows were not required to calculate NAV Total Return and are not inferred.

## Sources

- [First Trust FYX product page](https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FYX)
- [First Trust FYX factsheet, as of 2026-06-30](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=b4ab133b-7d16-4b63-81f3-83640709b936)
- [First Trust Exchange-Traded AlphaDEX Fund prospectus](https://www.ftportfolios.com/Funds/ETF/Prospectus/FYT)
- [First Trust FYX historical pricing](https://www.ftportfolios.com/Retail/Etf/EtfPriceHistory.aspx?Ticker=FYX)
- [First Trust FYX distribution history](https://www.ftportfolios.com/Retail/Etf/EtfDividHistory.aspx?Ticker=FYX)
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
