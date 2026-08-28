---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:INDA
ticker: INDA
exchange: Cboe BZX
fund: iShares MSCI India ETF
tracked_index: MSCI India Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-28
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-26
fund_facts_as_of: 2026-08-26
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return; gross income reinvested; fund expenses reflected in NAV
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/INDA
  - geography/India
---

# INDA Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

INDA เป็น iShares MSCI India ETF, canonical `Cboe BZX:INDA`, กองทุน
passive/index-tracking equity ETF ที่ติดตาม `MSCI India Index (Net)`. Official
rolling 10-year NAV Total Return ครอบคลุม 2016-06-30 ถึง 2026-06-30 ครบ
`10.00` ปี; cumulative return คือ `98.09%` และ CAGR `7.07%` ต่อปี. Current
official NAV TR YTD คือ `-8.44%` ณ 2026-08-26; NAV ล่าสุดที่ตรวจสอบได้คือ
`USD 49.56` ณ 2026-08-26.

## Performance check

- `entity_key`: `Cboe BZX:INDA`
- Fund: iShares MSCI India ETF; asset class `Equity`; expense ratio `0.61%`
- Inception: `2012-02-02`
- Metric: official NAV Total Return, รวม reinvested distributions และหัก fund expenses แล้ว
- Tracked index (issuer benchmark): `MSCI India Index (Net)`
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not issuer benchmark)
- Management mode: `passive-index`
- 10-year NAV TR coverage: `2016-06-30` to `2026-06-30`; actual years `10.00`
- 10-year NAV TR cumulative / CAGR: `98.09%` / `7.07%` (official iShares)
- Normalized NAV TR: start `100.00`; end `198.09` (official cumulative return; raw NAV endpoints are not disclosed)
- Official rolling annualised NAV TR fields as of `2026-06-30`: 1-year `-11.39%`, 3-year `4.41%`, 5-year `3.64%`, 10-year `7.07%`, and since inception `5.72%`
- Available official calendar rows 2021-2025 compound to `45.55%` / CAGR `7.80%`; issuer benchmark rows compound to `60.22%` / CAGR `9.89%`; S&P 500 rows in the same window compound to `96.17%` / CAGR `14.43%`
- Current snapshot: NAV `USD 49.56`, closing price `USD 49.75`, net assets `USD 6,613,614,143`, and `167` holdings, all as of `2026-08-26`; current NAV TR YTD is `-8.44%` as of `2026-08-26`.

| Year | INDA NAV TR | MSCI India Index (Net) TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | 22.41% | 26.23% | 28.71% |
| 2022 | -9.38% | -7.95% | -18.11% |
| 2023 | 17.49% | 20.81% | 26.29% |
| 2024 | 8.99% | 11.22% | 25.02% |
| 2025 | 2.47% | 2.62% | 17.88% |
| 2026 YTD (month-end) | -9.09% | not disclosed | not comparable; current year not cached |

Official iShares calendar rows in the reviewed capture cover 2021-2025;
2016-2020 annual rows were not disclosed, so no proxy was created. The
month-end 2026 YTD row is as of `2026-06-30`; current product-page YTD is kept
separately because it is as of `2026-08-26`. S&P 500 เป็น common reference
benchmark ไม่ใช่ issuer benchmark ของ INDA; ตารางใช้ cached USD Total Return
convention สำหรับ 2016-2025.

## Common-window comparison

- INDA 2021-2025 NAV TR cumulative / CAGR: `45.55%` / `7.80%`
- MSCI India Index (Net) 2021-2025 cumulative / CAGR: `60.22%` / `9.89%`; INDA trails its issuer benchmark by approximately `2.09 pp` CAGR.
- S&P 500 2021-2025 TR cumulative / CAGR: `96.17%` / `14.43%`
- INDA trails the S&P 500 common reference by approximately `6.63 pp` CAGR in the common calendar window.
- Up years / Down years in 2021-2025: `4 / 1`
- Best year: 2021, `22.41%`; least positive year: 2025, `2.47%`
- Worst year: 2022, `-9.38%`
- Current official NAV TR YTD: `-8.44%` as of `2026-08-26`; latest NAV `US$49.56` as of `2026-08-26`

## Risk read-through

INDA เป็น single-country India equity ETF; official data ณ 2026-08-26 มี 167
holdings, net assets `USD 6,613,614,143`, expense ratio `0.61%`, 3-year
standard deviation `14.09%`, P/E `22.80` และ P/B `3.30`. Sector breakdown ที่
สอดคล้องกับ current canonical product-page snapshot เป็น `not disclosed` ใน
capture นี้. ความเสี่ยงหลักคือ India/country, valuation, currency, policy และ
sector concentration. Daily NAV history ที่ยืนยันได้เพียงพอสำหรับ max drawdown
และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official iShares product and performance page: https://www.ishares.com/us/products/239659/INDA
- Official iShares factsheet: https://www.ishares.com/us/literature/fact-sheet/inda-ishares-msci-india-etf-fund-fact-sheet-en-us.pdf
- Official iShares summary prospectus: https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-india-etf-8-31.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-28]] | [[ETF Performance Index]]
