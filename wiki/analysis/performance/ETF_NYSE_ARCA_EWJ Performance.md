---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWJ
ticker: EWJ
exchange: NYSE Arca
fund: iShares MSCI Japan ETF
tracked_index: MSCI Japan Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-18
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-16
price_nav_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-18.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWJ
  - geography/Japan
---

# EWJ Performance

## Bottom line

EWJ ให้ official `NAV Total Return` เป็นบวก 8 จาก 10 complete calendar years
2016-2025; การทบต้นจาก annual rows ให้ cumulative `101.00%` หรือ CAGR `7.23%`.
ปีดีที่สุดคือ 2025 ที่ `+25.92%` และแย่ที่สุดคือ 2022 ที่ `-17.36%`. Current YTD
ล่าสุดคือ `+14.28%` ณ 16 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:EWJ`
- Inception: 12 มี.ค. 1996
- Metric: `NAV Total Return` รวม dividends/distributions reinvested และหัก fund expenses
- Tracked index (issuer benchmark): `MSCI Japan Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ EWJ)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `9.54%`; Start TR value: `100.00`; End TR value: `248.81`;
  Years: `10.00`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`; official cumulative return ใน
  rolling window คือ `148.81%`
- Annual coverage: official complete calendar years 2016-2025; ไม่มี `*` หรือ `†`.
  ปี 2016-2024 ใช้ Summary Prospectus และปี 2025 ใช้ issuer performance page.
- S&P 500 cache 2016-2025: cumulative `298.33%`; CAGR `14.82%` จาก rounded annual inputs

| ปี | EWJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 1.96% | 11.96% |
| 2017 | 23.56% | 21.83% |
| 2018 | -13.17% | -4.38% |
| 2019 | 19.19% | 31.49% |
| 2020 | 14.03% | 18.40% |
| 2021 | 1.56% | 28.71% |
| 2022 | -17.36% | -18.11% |
| 2023 | 19.78% | 26.29% |
| 2024 | 6.80% | 25.02% |
| 2025 | 25.92% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2025, `+25.92%`
- Least positive: 2021, `+1.56%`
- Worst: 2022, `-17.36%`
- Least bad down year: 2018, `-13.17%`
- 2021-2025 cumulative / CAGR: EWJ `35.20%` / `6.22%`; S&P 500 TR
  `96.17%` / `14.43%`
- Current YTD: `+14.28%` NAV ณ 16 ก.ค. 2026; same-date official S&P 500 TR YTD
  `ไม่พบข้อมูลที่ยืนยันได้`

## Risk read-through

Official rolling 10-year NAV CAGR `9.54%` ณ 30 มิ.ย. 2026 สูงกว่า calendar-year
CAGR `7.23%` เพราะเป็นคนละ endpoint/window. EWJ เป็น passive single-country Japan
large/mid-cap equity และไม่ได้ hedge JPY/USD; จึงมี Japan, trade-cycle, sector และ
FX sensitivity. Official 3-year standard deviation คือ `13.32%` และ expense ratio
`0.49%`. Secondary dividend-adjusted market-price proxy รายงาน 10-year max drawdown
`-33.14%*` ที่ trough ต.ค. 2022 และ recovery มี.ค. 2024; ไม่ใช่ official NAV drawdown.

## Sources

- [iShares EWJ product page](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf) — identity, exchange, benchmark, current NAV/YTD, official annual and rolling performance, expense ratio, and risk metrics
- [Official EWJ Summary Prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-japan-etf-8-31.pdf) — official 2016-2024 calendar returns, reinvestment convention, passive indexing policy, and risks
- [iShares EWJ fact sheet](https://www.ishares.com/us/literature/fact-sheet/ewj-ishares-msci-japan-etf-fund-fact-sheet-en-us.pdf) — official return definition and 2021-2025 calendar-year cross-check
- [PortfoliosLab EWJ](https://portfolioslab.com/symbol/EWJ) — secondary dividend-adjusted market-price drawdown and recovery proxy, updated 2026-07-14
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference index identity
- [[ETF_performance_sources_2026-07-18]] | [[ETF Performance Index]]
