---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWM
input_ticker: EWM
ticker: EWM
exchange: NYSE Arca
fund: iShares MSCI Malaysia ETF
tracked_index: MSCI Malaysia Index
benchmark: S&P 500 Total Return
inception: 1996-03-12
management_mode: passive-index
updated: 2026-08-28
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-25
nav_as_of: 2026-08-26
market_price_as_of: 2026-08-26
holdings_as_of: 2026-08-26
risk_as_of: 2026-07-31
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return; dividends and capital gains reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EWM
  - geography/Malaysia
---

# EWM Performance

> Navigation: [[ETF Region Index]] → [[Malaysia ETF]] → [[ETF Performance Index]]

## Bottom line

EWM คือ iShares MSCI Malaysia ETF ที่จดทะเบียนบน `NYSE Arca` และเป็น
passive, single-country equity ETF ซึ่งติดตาม `MSCI Malaysia Index`. Official
rolling 10-year NAV Total Return จาก 2016-06-30 ถึง 2026-06-30 มี cumulative
`24.54%` และ CAGR `2.22%`; official 2021-2025 NAV TR จาก rounded rows สะสม
`16.86%` หรือ CAGR `3.17%`. Current official NAV TR YTD ล่าสุดคือ `6.15%`
ณ 25 ส.ค. 2026 และ latest NAV คือ `USD 28.86` ณ 26 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:EWM`; Fund: iShares MSCI Malaysia ETF; inception
  `1996-03-12`; expense ratio `0.50%`; semi-annual distributions
- Metric: issuer `NAV Total Return` in USD, with dividends and capital gains
  reinvested and fund expenses deducted; market-price return is not mixed into
  NAV calculations
- Issuer benchmark: `MSCI Malaysia Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ strategy-appropriate benchmark ของ Malaysia single-country ETF)
- Management mode: `passive-index`; official objective คือ track an index
  composed of Malaysian equities
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`, `10.00 elapsed
  years`; NAV TR cumulative `24.54%`, CAGR `2.22%`; normalized endpoints are
  `100.00` and `124.54` from the issuer cumulative return
- Current official snapshot: NAV `$28.86`, closing market price `$29.00`, and
  1-day NAV change `+$0.34 (+1.18%)` as of `2026-08-26`; net assets
  `$328,954,869`; premium/discount `+0.50%`; current YTD NAV TR `6.15%` as of
  `2026-08-25`
- Annual coverage: complete official calendar years 2021-2025; no `*` or `†`
  markers. Earlier annual rows are not surfaced in the reviewed current
  official capture and remain `ไม่พบข้อมูลที่ยืนยันได้`.

| ปี | EWM NAV TR | MSCI Malaysia Index | S&P 500 TR |
|---|---:|---:|---:|
| 2021 | -6.30% | -6.24% | 28.71% |
| 2022 | -6.25% | -5.78% | -18.11% |
| 2023 | -4.01% | -3.49% | 26.29% |
| 2024 | 20.13% | 20.75% | 25.02% |
| 2025 | 15.37% | 15.45% | 17.88% |

S&P 500 rows ใช้ cached USD Total Return convention, dividends reinvested,
reference as-of `2025-12-31`. EWM 2021-2025 NAV rows compound to `16.86%` /
`3.17%`; tracked index rows compound to `18.85%` / `3.51%`; arithmetic
fund-minus-index CAGR gap คือ `-0.35 pp` และไม่เรียกว่า alpha. Cached S&P 500
TR คือ `96.17%` / `14.43%`, จึงมี arithmetic EWM gap `-11.26 pp` เทียบ common
reference นี้. Rolling issuer benchmark for the same 10-year window is `28.92%`
cumulative / `2.57%` annualized, or `-0.35 pp` versus EWM CAGR.

## Up years / Down years

- Complete 2021-2025 NAV TR up/down: `2 / 3`
- Best NAV TR year: 2024, `+20.13%`
- Least positive year: 2025, `+15.37%`
- Worst NAV TR year: 2021, `-6.30%`
- Least bad down year: 2023, `-4.01%`
- Current official NAV TR YTD: `+6.15%` as of `2026-08-25`

## Risk read-through

EWM เป็น single-country Malaysia equity ETF ที่กระจุกตัวใน Financials
`51.59%`, Utilities `14.42%`, Industrials `9.90%`, Materials `8.22%`,
Consumer Staples `7.32%`, Communication `5.32%`, Health Care `2.95%` และ
cash/derivatives `0.28%` ณ 26 ส.ค. 2026; มี `21` holdings, P/E `15.40` และ
P/B `1.62` ณ 26 ส.ค.; 3-year standard deviation `12.80%` และ beta `0.27` ณ
31 ก.ค.; 30-day SEC yield `3.53%` และ 12-month trailing yield `3.56%` ณ
31 ก.ค. 2026.

ความเสี่ยงหลักคือ Malaysia/country concentration, financials/utilities/materials
concentration, MYR/USD FX, emerging-market policy and liquidity sensitivity,
systematic fair-value pricing และ equity volatility. Fund-minus-index gap เป็น
tracking/fee/timing evidence ไม่ใช่ manager skill. Official daily NAV series
สำหรับคำนวณ maximum drawdown และ recovery date: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Official iShares EWM product page](https://www.ishares.com/us/products/239669/ishares-msci-malaysia-etf) — current NAV/price/YTD, exchange, benchmark, assets, holdings, exposures, rolling performance, fees and distributions; later official capture through 2026-08-26
- [Official EWM factsheet](https://www.ishares.com/us/literature/fact-sheet/ewm-ishares-msci-malaysia-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 NAV/index rows, rolling 10-year fields, return definitions, fee, launch, holdings and benchmark as of 2026-06-30
- [SEC EWM summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-malaysia-etf-8-31.pdf) — formal fund identity, passive/index objective, listing and fee disclosures
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference identity; annual rows reuse the cached skill convention
- [[ETF_performance_sources_2026-08-28]] | [[ETF Performance Index]]
