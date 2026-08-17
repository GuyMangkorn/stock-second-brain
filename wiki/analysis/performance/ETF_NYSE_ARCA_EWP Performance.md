---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWP
ticker: EWP
exchange: NYSE Arca
fund: iShares MSCI Spain ETF
tracked_index: MSCI Spain 25/50 Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-30
price_nav_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWP
  - geography/Spain
---

# EWP Performance

> Navigation: [[ETF Region Index]] → [[Spain ETF]] → [[ETF Performance Index]]

## Bottom line

EWP ให้ cumulative `NAV Total Return` ประมาณ `162.48%` ในปี 2016-2025 หรือ
CAGR `10.13%`; บวก 6 ปีและลบ 4 ปี เทียบ S&P 500 TR CAGR `14.82%`. ปีดีที่สุด
คือ 2025 `+77.12%`; แย่ที่สุดคือ 2018 `-15.07%`. Latest official 2026 YTD
คือ `+16.14%` ณ 30 ก.ค. 2026; S&P 500 TR cross-check ล่าสุด `+14.54%` ณ
17 ส.ค. 2026 เป็นคนละวัน จึงไม่ใช้เป็น same-date spread.

## Performance check

- `entity_key: NYSE Arca:EWP`
- Inception: 12 มี.ค. 1996
- Metric: `NAV Total Return` (USD), distributions reinvested หลังหัก fund expenses
- Tracked index (issuer benchmark): `MSCI Spain 25/50 Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ EWP)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `12.76%`; Start TR value: `100.00`; End TR value:
  `332.40`; Years: `10.00`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`; End TR เป็น normalized
  calculation จาก official cumulative `232.40%`, ไม่ใช่ raw index level
- Annual coverage: official complete calendar years 2016-2025; ไม่มี `*` หรือ
  `†`. ปี 2016-2020 มาจาก issuer summary prospectus chart และปี 2021-2025 จาก
  iShares fact sheet; 2016-2025 CAGR คำนวณจาก disclosed rounded annual inputs
- S&P 500 cache 2016-2025: cumulative `298.33%`; CAGR `14.82%` จาก rounded
  annual inputs

| ปี | EWP NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -2.18% | 11.96% |
| 2017 | 26.97% | 21.83% |
| 2018 | -15.07% | -4.38% |
| 2019 | 10.94% | 31.49% |
| 2020 | -3.14% | 18.40% |
| 2021 | 0.10% | 28.71% |
| 2022 | -5.34% | -18.11% |
| 2023 | 29.80% | 26.29% |
| 2024 | 6.30% | 25.02% |
| 2025 | 77.12% | 17.88% |

## Up years / Down years

- Up years / Down years: `6 / 4` ใน 2016-2025
- Best: 2025, `+77.12%`
- Least positive: 2021, `+0.10%`
- Worst: 2018, `-15.07%`
- Least bad down year: 2016, `-2.18%`
- 2021-2025 common-window cumulative: EWP `131.57%`, CAGR `18.29%`; S&P 500
  TR `96.17%`, CAGR `14.43%`
- Current YTD: EWP `+16.14%` NAV TR as of 30 ก.ค. 2026; NAV `61.36` and
  closing price `61.48` as of 31 ก.ค. 2026. S&P 500 TR `+14.54%` as of 17 ส.ค.
  2026 is a fresh but non-matched-date reference.

## Risk read-through

**10-year NAV CAGR:** `12.76%` ณ 30 มิ.ย. 2026. EWP เป็น Spain single-country
equity ที่กระจุกใน Financials `43.70%`, Utilities `24.16%` และ Industrials
`13.91%` ณ 30 มิ.ย. 2026; มี 23 holdings และ EUR/USD exposure. Official 3-year
standard deviation คือ `16.33%` และ equity beta `0.49` ณ วันเดียวกัน. Expense
ratio `0.50%` เป็น cost drag สำคัญ. Official daily NAV maximum drawdown และ
recovery ยัง `ไม่พบข้อมูลที่ยืนยันได้`. EWP เริ่มติดตาม MSCI Spain 25/50 Index
(Net) เมื่อ 12 ก.พ. 2013; ก่อนหน้านั้น historical index data ใช้ MSCI Spain
Index (Net).

## Sources

- [iShares EWP product page](https://www.ishares.com/us/products/239683/ishares-msci-spain-capped-etf?qt=EWP) — fund facts, rolling/current performance, NAV/price, fee and exchange
- [iShares EWP fact sheet](https://www.ishares.com/us/literature/fact-sheet/ewp-ishares-msci-spain-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 NAV rows, rolling returns and risk snapshot
- [iShares EWP summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-spain-capped-etf-8-31.pdf) — official 2016-2020 calendar rows and index history
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common USD total-return benchmark definition
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
