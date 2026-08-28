---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:ECNS
ticker: ECNS
exchange: NYSE Arca
fund: iShares MSCI China Small-Cap ETF
tracked_index: MSCI China Small Cap Index (Net)
benchmark: S&P 500 Total Return
inception: 2010-09-28
management_mode: passive-index
updated: 2026-08-28
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-26
nav_as_of: 2026-08-27
market_price_as_of: 2026-08-27
holdings_as_of: 2026-08-27
risk_as_of: 2026-07-31
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/ECNS
  - geography/China
  - style/small-cap
---

# ECNS Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

ECNS มี NAV Total Return สะสม `-13.19%` หรือ CAGR `-2.79%` ใน complete calendar
years 2021-2025 ขณะที่ MSCI China Small Cap Index สะสม `-23.54%` หรือ CAGR
`-5.23%`; current official NAV TR YTD คือ `-9.18%` ณ 26 ส.ค. 2026. ปี 2025
รีบาวด์ `+36.42%` แต่ปี 2022 ลด `-24.77%`, สะท้อนความเสี่ยงของ China small-cap
ที่ยังสูงและไม่ใช่ broad China proxy.

## Performance check

- `entity_key: NYSE Arca:ECNS`
- Fund: iShares MSCI China Small-Cap ETF; inception `2010-09-28`; expense ratio
  `0.59%`; distribution frequency semi-annual
- Metric: `NAV Total Return` ใน USD รวม distributions reinvested และหัก fund
  expenses
- Issuer benchmark: `MSCI China Small Cap Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ ECNS)
- Management mode: `passive-index`; official objective คือ track small-cap Chinese
  equities available to international investors
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`; NAV TR CAGR
  `1.05%`. Issuer ไม่เปิดเผย raw start/end TR values หรือ cumulative return จึง
  ไม่คำนวณ endpoint ซ้ำ
- Current official snapshot: NAV `$29.61` และ closing market price `$29.36` ณ
  `2026-08-27`; 1-day NAV change `+$0.07 (+0.25%)`; NAV TR YTD `-9.18%` ณ
  `2026-08-26`
- Annual coverage: official complete calendar years 2021-2025; ไม่มี `*` หรือ
  `†` markers

| ปี | ECNS NAV TR | MSCI China Small Cap Index (Net) | S&P 500 TR |
|---|---:|---:|---:|
| 2021 | 3.10% | -6.29% | 28.71% |
| 2022 | -24.77% | -24.80% | -18.11% |
| 2023 | -23.28% | -24.86% | 26.29% |
| 2024 | 6.94% | 6.75% | 25.02% |
| 2025 | 36.42% | 35.27% | 17.88% |

S&P 500 rows ใช้ cached USD Total Return convention, dividends reinvested,
reference as-of `2025-12-31`. จากตัวเลขที่แสดง ECNS 2021-2025 cumulative/CAGR
คือ `-13.19%` / `-2.79%`; tracked index คือ `-23.54%` / `-5.23%`; arithmetic
fund-minus-index CAGR gap คือ `+2.44 pp` และไม่เรียกว่า alpha. S&P 500 TR คือ
`96.17%` / `14.43%`; ECNS มี arithmetic CAGR gap `-17.22 pp` เทียบ common
reference นี้.

## Up years / Down years

- Up years / Down years: `3 / 2` ใน 2021-2025
- Best: 2025, `+36.42%`
- Least positive: 2021, `+3.10%`
- Worst: 2022, `-24.77%`
- Least bad down year: 2023, `-23.28%`
- Current YTD: ECNS `-9.18%` NAV TR ณ `2026-08-26`

## Risk read-through

ECNS เป็น passive China small-cap equity ETF มี `266` holdings ณ 27 ส.ค. 2026.
Portfolio characteristics ล่าสุดที่มีคนละ as-of date คือ P/E `11.66x`, P/B
`0.90x` ณ 27 ส.ค.; 3-year standard deviation `26.02%` และ equity beta `0.51`
ณ 31 ก.ค.; 30-day SEC yield `3.57%` และ 12-month trailing yield `6.57%` ณ
31 ก.ค. 2026. Sector exposure ณ 27 ส.ค. คือ Health Care `22.79%`, Industrials
`14.44%`, Information Technology `11.42%`, Consumer Discretionary `11.23%`,
Materials `9.78%`, Real Estate `8.35%` และ Communication `8.29%`.

จึงไวต่อ domestic demand, policy/geopolitical risk, property, FX, liquidity และ
small-cap volatility มากกว่า broad China ETF. Expense และ index return ต่างจาก
กองตามค่าธรรมเนียม, withholding tax, transaction costs, timing และ systematic
fair value; fund-minus-index gap ข้างต้นจึงเป็น tracking/implementation evidence
ไม่ใช่หลักฐานของ manager skill. Official daily NAV TR series สำหรับคำนวณ maximum
drawdown และ recovery โดยตรง: `ไม่พบข้อมูลที่ยืนยันได้`; ไม่ใช้ 52-week price
drawdown หรือ secondary price proxy แทน NAV TR.

## Sources

- [iShares ECNS product page](https://www.ishares.com/us/products/239620/ishares-msci-china-etf) — current NAV/price, YTD NAV TR, exchange, benchmark, holdings, exposures, premium/discount, distributions and fees; current snapshot through 2026-08-27
- [Official ECNS factsheet](https://www.ishares.com/us/literature/fact-sheet/ecns-ishares-msci-china-small-cap-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 annual NAV/index rows, rolling 10-year NAV TR and risk facts as of 2026-06-30
- [ECNS official prospectus](https://www.ishares.com/us/literature/prospectus/p-ishares-trust-emerging-8-31.pdf) — passive objective, NYSE Arca listing, MSCI China Small Cap Index strategy and risks; current prospectus document
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference identity; annual rows reuse the cached skill convention
- [[ETF_performance_sources_2026-08-28]] | [[ETF Performance Index]]
