---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:NORW
ticker: NORW
exchange: NYSE Arca
fund: Global X MSCI Norway ETF
tracked_index: MSCI Norway IMI 25/50 Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-31
current_ytd_source: secondary-dividend-reinvested
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/NORW
  - geography/Norway
---

# NORW Performance

> Navigation: [[ETF Region Index]] → [[Norway ETF]] → [[ETF Performance Index]]

## Bottom line

NORW เป็น passive single-country Norway equity ETF ที่ track `MSCI Norway IMI
25/50 Index`. Official complete calendar rows 2016-2025 ให้ cumulative `NAV
Total Return` `114.25%` และ rounded-input CAGR `7.92%`, เป็นบวก 7 ปีและลบ 3 ปี.
ปีดีที่สุดคือ 2025 ที่ `+32.82%` และแย่ที่สุดคือ 2022 ที่ `-12.92%`; official
rolling 10-year NAV TR CAGR คือ `8.61%` ณ 2026-06-30. Reviewed Global X capture
ยังไม่เปิดเผย current YTD หลัง 2026-06-30; secondary dividend-reinvested YTD
คือ `+25.16%†` ถึง 2026-07-31.

## Performance check

- `entity_key: NYSE Arca:NORW`; inception `2010-11-09`; exchange `NYSE Arca`; CUSIP `37950E101`; ISIN `US37950E1010`.
- Metric: `NAV Total Return` in USD; performance is shown on a total-return basis with gross income reinvested where applicable and fund expenses reflected in NAV returns.
- Tracked index (issuer benchmark): `MSCI Norway IMI 25/50 Index`; Global X states the index was `FTSE Norway 30 Index` from fund inception through 2014-07-14 and `MSCI Norway IMI 25/50 Index` thereafter.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ NORW).
- Total expense ratio and management fee `0.50%`; semi-annual distributions; official NAV `US$36.53`, closing market price `US$36.68`, net assets `US$90.81M`, and 60 holdings as of 2026-08-14.
- Official rolling performance as of 2026-06-30: NAV `1Y 18.70%`, `3Y 18.10%`, `5Y 6.84%`, `10Y 8.61%`, inception `4.26%`; tracked-index returns `19.24%`, `18.74%`, `7.30%`, `8.99%`, `4.79%`.
- Official calendar rows: Global X summary prospectus for 2016-2025; performance before 2021-11-01 reflects the predecessor fund carried into the post-reorganization fund.
- Official MSCI net-index rows are included for tracking context. S&P 500 cache 2016-2025: cumulative `298.33%`; rounded-input CAGR `14.82%` from USD total-return annual rows as of 2025-12-31.
- `†` marks the secondary current YTD fallback. Global X factsheet reports official NAV TR YTD `13.49%` as of 2026-06-30; the latest reviewed issuer page capture did not expose a newer official YTD field. The secondary source reports `25.16%†` with dividends reinvested through 2026-07-31.

| Year | NORW NAV TR | MSCI Norway IMI 25/50 Net | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 17.64% | 17.88% | 11.96% |
| 2017 | 22.04% | 22.25% | 21.83% |
| 2018 | -8.38% | -8.09% | -4.38% |
| 2019 | 12.85% | 13.26% | 31.49% |
| 2020 | 3.50% | 3.85% | 18.40% |
| 2021 | 18.24% | 18.77% | 28.71% |
| 2022 | -12.92% | -12.89% | -18.11% |
| 2023 | 5.01% | 5.52% | 26.29% |
| 2024 | -2.89% | -2.37% | 25.02% |
| 2025 | 32.82% | 33.60% | 17.88% |

## Up years / Down years

- Complete fund rows 2016-2025: `7 / 3` up/down years; cumulative `114.25%`; rounded-input CAGR `7.92%`; population annual-return standard deviation `13.72%`.
- Best: 2025, `+32.82%`; least positive: 2023, `+5.01%`.
- Worst: 2022, `-12.92%`; least bad down year: 2024, `-2.89%`.
- Common 2021-2025 window: NORW cumulative `39.46%` / rounded-input CAGR `6.88%`; tracked-index cumulative `42.40%` / rounded-input CAGR `7.32%`; arithmetic tracking gap approximately `-2.94 pp` cumulative and `-0.45 pp` CAGR.
- Cached S&P 500 TR common-window cumulative `96.17%` / CAGR `14.43%`; the arithmetic difference is a common-reference comparison, not alpha.
- Current YTD: NORW secondary NAV/total-return series `+25.16%†` through 2026-07-31. This is not relabelled as an official Global X YTD field; official issuer YTD remains `+13.49%` at the older 2026-06-30 factsheet date.

## Risk read-through

**10-year NAV CAGR:** `8.61%` ณ 2026-06-30. NORW มี Norway/country และ
NOK-USD FX exposure พร้อม concentration ใน Energy `30.2%`, Financials `25.0%`,
Industrials `12.7%`, Consumer Staples `11.3%` และ Materials `9.2%` ณ 2026-07-31.
Issuer page risk statistics report 3-year standard deviation `15.90%` และ beta
เทียบ S&P 500 `0.44` ณ 2026-07-31; expense ratio คือ `0.50%`. Global X
summary prospectus รายงาน best quarter `+24.12%` สิ้นสุด 2020-12-31 และ worst
quarter `-37.23%` สิ้นสุด 2020-03-31; สองตัวเลขนี้ไม่ใช่ maximum drawdown.
Official daily NAV maximum drawdown และ recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

Latest four cash distributions จาก secondary history คือ `US$2.1048` (ex-date
2026-06-29), `US$0.42969` (2025-12-30), `US$0.60419` (2025-06-27) และ
`US$0.60245` (2024-12-30): sum `US$3.74113`, average `US$0.935283` ต่อรอบ
หรือประมาณ `2.55%` ต่อรอบเทียบ closing price `US$36.68`; issuer 30-day SEC
yield คือ `3.95%` ณ 2026-08-14. Secondary trailing dividend yield คือ `7.17%`
ณ 2026-08-07 และไม่ใช่ forward payout estimate.

## Sources

- [Global X NORW product page](https://www.globalxetfs.com/funds/norw) — identity, NYSE Arca, inception, current NAV/price, net assets, holdings, exposures, risk statistics, rolling performance, fee and SEC yield.
- [Global X NORW fact sheet](https://assets.globalxetfs.com/funds/documents/norw/Fact-Sheet_NORW.pdf) — official NAV total-return definition, official YTD/rolling returns as of 2026-06-30, exchange, fee and sector snapshot.
- [Global X NORW summary prospectus](https://assets.globalxetfs.com/funds/documents/norw/prospectus-regulatory/Summary-Prospectus_NORW.pdf) — official 2016-2025 annual NAV rows, strategy, predecessor continuity and best/worst quarter.
- [MSCI Norway IMI 25/50 Index factsheet](https://www.msci.com/documents/10199/0be0be65-d64d-49cb-b08f-67b6f3a8da49) — official USD net-index annual rows and 2026-06-30 index return/risk context.
- [YTD Return NORW](https://www.ytdreturn.com/norw/) — secondary dividend-reinvested current-YTD fallback through 2026-07-31, marked `†`.
- [StockAnalysis NORW dividend history](https://stockanalysis.com/etf/norw/dividend/) — secondary latest-four distribution cross-check and trailing yield; data source identified as S&P Global Market Intelligence.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
