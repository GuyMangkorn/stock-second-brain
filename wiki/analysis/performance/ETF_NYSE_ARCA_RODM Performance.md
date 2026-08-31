---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:RODM
input_ticker: RODM
ticker: RODM
exchange: NYSE Arca
fund: Hartford Multifactor Developed Markets (ex-US) ETF
tracked_index: Hartford Risk-Optimized Multifactor Developed Markets (ex-US) Index
benchmark: S&P 500 Total Return
issuer_benchmark: Hartford Risk-Optimized Multifactor Developed Markets (ex-US) Index
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: established
management_evidence: not applicable
risk_evidence: issuer-fields
updated: 2026-09-01
performance_as_of: 2026-07-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-2.md
return_basis: NAV total return; issuer performance convention; market-price return separate
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/RODM
  - geography/International
---

# RODM Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

RODM เป็น passive multifactor ETF สำหรับ developed markets ex-US โดยติดตาม
Hartford Risk-Optimized Multifactor Developed Markets (ex-US) Index. Official
NAV total return ล่าสุดที่ตรวจได้ให้ YTD `14.01%` และ 1-year `26.64%` ณ
`2026-07-31`; official rolling 10-year NAV CAGR อยู่ที่ `9.07%`. ผลลัพธ์จึง
สะท้อนทั้ง factor tilt และความเสี่ยงของหุ้นต่างประเทศ ไม่ใช่ broad-market
exposure แบบไม่มี tilt.

## Performance check

- `entity_key`: `NYSE Arca:RODM`
- Inception date: `2015-02-25`
- Expense ratio: `0.29%` total operating expense
- Current official NAV: `$42.00` as of `2026-08-28`; net assets `$1,650,684,642`
- Metric: NAV Total Return in USD; market-price return is separate
- Official current performance as of `2026-07-31`: YTD `14.01%`; 1-year `26.64%`; 3-year annualized `19.47%`; 5-year annualized `10.30%`; 10-year annualized `9.07%`; since inception annualized `8.02%`
- Issuer benchmark: Hartford Risk-Optimized Multifactor Developed Markets (ex-US) Index
- Ten displayed rounded annual rows imply cumulative `118.17%` and CAGR `8.11%`; this is an approximation because 2025 is a secondary proxy (`*`)

| Year | RODM NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2016 | 3.25% | 11.96% |
| 2017 | 25.75% | 21.83% |
| 2018 | -9.74% | -4.38% |
| 2019 | 17.10% | 31.49% |
| 2020 | -0.22% | 18.40% |
| 2021 | 10.82% | 28.71% |
| 2022 | -14.37% | -18.11% |
| 2023 | 15.77% | 26.29% |
| 2024 | 8.07% | 25.02% |
| 2025 | 34.20%* | 17.88% |

`*` 2025 RODM row is a secondary AAII proxy as of `2026-06-30`; 2016-2024
rows are from Hartford’s summary prospectus. S&P 500 Total Return is only a
common USD reference, not RODM’s issuer benchmark.

## Up years / Down years

- Up years / Down years in 2016-2025: `7 / 3`
- Best displayed year: 2025, `+34.20%*`
- Worst displayed year: 2022, `-14.37%`
- Rounded-input 2016-2025 CAGR: `8.11%` (approximation)
- Official rolling 10-year NAV CAGR: `9.07%` as of `2026-07-31`

## Risk read-through

Issuer risk fields as of `2026-07-31` report 5-year standard deviation `13.94%`,
beta `0.87`, Sharpe `0.51`, information ratio `0.16`, and up/down capture
`91.55% / 84.16%`. The factor design can lag a capitalization-weighted
developed-market index for long periods, while non-US currency, country,
liquidity, and trading risks remain. A fresh daily-NAV maximum drawdown and
recovery period is `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Hartford official RODM fund page](https://www.hartfordfunds.com/funds/rodm.html)
- [Hartford RODM 2025 summary prospectus](https://www.hartfordfunds.com/dam/en/docs/pub/funddocuments/regulatorydocument/summaryprospectus/SUM-RODM.pdf)
- [AAII RODM data](https://www.aaii.com/fund/ticker/RODM)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-2]]

