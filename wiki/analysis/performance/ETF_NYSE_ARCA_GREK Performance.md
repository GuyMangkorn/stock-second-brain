---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:GREK
ticker: GREK
exchange: NYSE Arca
fund: Global X MSCI Greece ETF
tracked_index: MSCI All Greece Select 25/50 Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-07-27
fund_facts_as_of: 2026-07-27
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/GREK
  - geography/Greece
---

# GREK Performance

> Navigation: [[ETF Region Index]] → [[Greece ETF]] → [[ETF Performance Index]]

## Bottom line

GREK ให้ cumulative `NAV Total Return` ประมาณ `255.67%` ใน complete calendar
years 2016-2025 จาก secondary annual proxy หรือ rounded-input CAGR `13.53%`;
บวก 7 ปีและลบ 3 ปี. ปีดีที่สุดคือ 2025 `+75.10%*` และแย่ที่สุดคือ 2018
`-29.90%*`. Current NAV TR YTD จาก secondary cross-check คือ `+22.00%*` ณ
2026-07-31; issuer current capture ไม่แสดงตัวเลข YTD เดียวกัน. Official rolling
10Y NAV TR ณ 2026-06-30 คือ `17.01%` เทียบ tracked index `17.76%` หรือ gap
`-0.75 pp`; rolling 5Y คือ `26.03%` เทียบ `26.83%` หรือ `-0.80 pp`.

## Performance check

- `entity_key: NYSE Arca:GREK`; inception `2011-12-07`; exchange `NYSE Arca`.
- Metric: `NAV Total Return` (USD), distributions reinvested หลังหัก fund expenses.
- Tracked index (issuer benchmark): `MSCI All Greece Select 25/50 Index`; fund is
  non-diversified and seeks to track the index rather than outperform it.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ GREK).
- Total expense ratio `0.56%` (`0.55%` management fee plus `0.01%` other expenses);
  at least 80% of assets are invested in index constituents, ADRs/GDRs, or
  companies economically tied to Greece.
- Official Global X product snapshot as of 2026-07-27: NAV `US$77.44`, market
  price `US$78.08`, net assets `US$289.29M`; trading snapshot as of 2026-07-24
  reported 32 holdings and a 30-day median bid/ask spread of `0.43%`.
- Official rolling performance as of 2026-06-30: NAV TR `1Y 33.59%`, `3Y 31.38%`,
  `5Y 26.03%`, `10Y 17.01%`, since inception `5.71%`; tracked-index returns
  `34.54%`, `32.28%`, `26.83%`, `17.76%`, since inception `6.55%`.
- The SEC standardized table as of 2025-12-31 separately reported fund/index
  `1Y 75.12% / 76.40%`, `5Y 24.58% / 25.34%`, and `10Y 13.54% / 14.20%`.
- Annual rows below are secondary NAV total-return proxy rows because the SEC
  annual chart was image-based and no numeric issuer calendar table was exposed
  in the reviewed capture. They are not used as strict official ranking evidence.
- S&P 500 cache 2016-2025: cumulative `298.33%`; CAGR `14.82%` from rounded annual inputs.

| ปี | GREK NAV TR* | MSCI All Greece Select 25/50 | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | -1.20% | ไม่พบข้อมูลที่ยืนยันได้ | 11.96% |
| 2017 | 32.20% | ไม่พบข้อมูลที่ยืนยันได้ | 21.83% |
| 2018 | -29.90% | ไม่พบข้อมูลที่ยืนยันได้ | -4.38% |
| 2019 | 49.30% | ไม่พบข้อมูลที่ยืนยันได้ | 31.49% |
| 2020 | -13.30% | ไม่พบข้อมูลที่ยืนยันได้ | 18.40% |
| 2021 | 5.70% | ไม่พบข้อมูลที่ยืนยันได้ | 28.71% |
| 2022 | 3.00% | ไม่พบข้อมูลที่ยืนยันได้ | -18.11% |
| 2023 | 43.50% | ไม่พบข้อมูลที่ยืนยันได้ | 26.29% |
| 2024 | 9.70% | ไม่พบข้อมูลที่ยืนยันได้ | 25.02% |
| 2025 | 75.10% | ไม่พบข้อมูลที่ยืนยันได้ | 17.88% |

`*` = secondary AAII annual NAV total-return rows, as of 2026-06-30; official
rolling returns remain the primary evidence.

## Up years / Down years

- Up years / Down years: `7 / 3` ใน secondary 2016-2025 rows.
- Best: 2025, `+75.10%*`; least positive: 2022, `+3.00%*`.
- Worst: 2018, `-29.90%*`; least bad down year: 2016, `-1.20%*`.
- 2016-2025 GREK secondary proxy cumulative `255.67%` / rounded-input CAGR `13.53%`;
  2021-2025 cumulative `200.09%` / rounded-input CAGR `24.58%`; all five years
  were positive.
- 2021-2025 S&P 500 TR cumulative `96.17%` / CAGR `14.43%`; the arithmetic
  common-reference CAGR difference is about `+10.15 pp`, not manager alpha.
- Current YTD secondary NAV TR is `+22.00%*` as of 2026-07-31 and is kept separate
  from the official 2026-06-30 rolling fields.

## Risk read-through

GREK เป็น passive, non-diversified Greece equity exposure with material banking
and country concentration. Portfolio ณ 2026-06-30 มี Financials `48.3%`,
Industrials `19.0%`, Utilities `9.9%`, Consumer Discretionary `8.6%`, Energy
`5.6%`, Communication `3.9%`, Materials `2.8%`, Real Estate `1.0%` และ Staples
`0.9%`. Official risk statistics reported S&P 500 beta `1.08`, NASDAQ-100 beta
`0.68`, MSCI EAFE beta `1.09`, MSCI EM beta `0.68`, and standard deviation
`19.60%` as of 2026-06-30. The SEC disclosed best quarter `+31.50%` (Q4 2020)
and worst quarter `-44.00%` (Q1 2020); these are not maximum-drawdown measures.
Official daily NAV maximum drawdown and recovery date are `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Global X GREK product page](https://www.globalxetfs.com/funds/grek) — objective, index, current product snapshot, rolling performance, portfolio and risk fields.
- [GREK SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1432353/000143235326000191/a497kmscigreece.htm) — exchange, fee, strategy, non-diversified status, standardized performance, and best/worst quarter.
- [AAII GREK performance page](https://www.aaii.com/etf/ticker/GREK?via=emailsignup-readmore) — secondary annual NAV total-return rows and rolling cross-check.
- [Schwab GREK performance page](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=grek) — secondary current price and NAV/benchmark cross-check through 2026-07-31.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
