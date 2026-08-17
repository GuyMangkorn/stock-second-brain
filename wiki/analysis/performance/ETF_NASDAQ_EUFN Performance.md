---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:EUFN
ticker: EUFN
exchange: NASDAQ
fund: iShares MSCI Europe Financials ETF
tracked_index: MSCI Europe Financials Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EUFN
  - geography/Europe
---

# EUFN Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

EUFN ให้ cumulative `NAV Total Return` ประมาณ `177.80%` ใน complete calendar
years 2016-2025 หรือ rounded-input CAGR `10.76%`; บวก 6 ปีและลบ 4 ปี. ปีดีที่สุด
คือ 2025 `+65.23%` และแย่ที่สุดคือ 2018 `-23.20%`. Current official NAV TR YTD
คือ `+18.15%` ณ 2026-08-14. ใน common window 2021-2025 EUFN ให้ CAGR
`21.63%` เทียบ S&P 500 TR `14.43%`, แต่ official rolling 5Y NAV TR `20.44%`
เท่ากับ tracked index และ tracking gap ยังควรอ่านจาก official rolling series ไม่ใช่
annual arithmetic เพียงอย่างเดียว.

## Performance check

- `entity_key: NASDAQ:EUFN`; inception `2010-01-20`; exchange `NASDAQ`.
- Metric: `NAV Total Return` (USD), distributions reinvested หลังหัก fund expenses.
- Tracked index (issuer benchmark): `MSCI Europe Financials Index (Net)`.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ EUFN).
- Expense ratio `0.49%`; distribution frequency semi-annual; official net assets `US$4.33B`, NAV `US$42.48`, closing price `US$42.57` ณ 2026-08-14.
- Official rolling performance ณ 2026-06-30: NAV TR `1Y 28.45%`, `3Y 32.58%`, `5Y 20.44%`, `10Y 14.36%`, inception `7.03%`; tracked-index `28.99%`, `32.73%`, `20.44%`, `14.42%`, `7.14%`.
- Current official YTD NAV TR: `+18.15%` ณ 2026-08-14. Same-date tracked-index YTD was not disclosed in the reviewed current page.
- Annual coverage: official complete calendar years 2016-2025; 2016-2020 issuer table values are rounded to one decimal and 2021-2025 use official U.S. factsheet/page values to two decimals.
- S&P 500 cache 2016-2025: cumulative `298.33%`; CAGR `14.82%` from rounded annual inputs.

| ปี | EUFN NAV TR | MSCI Europe Financials | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | -3.10% | -3.00% | 11.96% |
| 2017 | 27.20% | 27.50% | 21.83% |
| 2018 | -23.20% | -23.10% | -4.38% |
| 2019 | 20.10% | 20.10% | 31.49% |
| 2020 | -8.20% | -8.00% | 18.40% |
| 2021 | 19.22% | 19.50% | 28.71% |
| 2022 | -8.79% | -9.03% | -18.11% |
| 2023 | 26.18% | 25.78% | 26.29% |
| 2024 | 17.41% | 17.52% | 25.02% |
| 2025 | 65.23% | 65.97% | 17.88% |

## Up years / Down years

- Up years / Down years: `6 / 4` ใน 2016-2025.
- Best: 2025, `+65.23%`; least positive: 2019, `+20.10%`.
- Worst: 2018, `-23.20%`; least bad down year: 2020, `-8.20%`.
- 2016-2025 EUFN cumulative `177.80%` / CAGR `10.76%`; 2021-2025 cumulative `166.18%` / CAGR `21.63%`.
- 2021-2025 S&P 500 TR cumulative `96.17%` / CAGR `14.43%`; EUFN outperformed by about `+7.20 pp` CAGR in this common reference window.
- Current YTD: EUFN NAV `+18.15%` ณ 14 ส.ค. 2026; this is not compared with a same-date S&P or tracked-index return.

## Risk read-through

EUFN เป็น passive developed-Europe financials sector exposure. Portfolio ณ
2026-08-14 มี Banks `59.06%`, Insurance `22.88%`, Financial Services `17.42%`
และ 84 holdings; geography นำโดย United Kingdom `23.79%`, Spain `12.38%`,
Germany `12.11%`, Switzerland `11.31%`, Italy `10.92%`. Official 3-year
standard deviation คือ `15.75%`, equity beta `0.61`, P/E `13.71` และ P/B `1.78`.
Main risks are financial-sector concentration, European rates/credit cycle,
country and FX exposure, and bank/insurer balance-sheet sensitivity. Official
daily NAV maximum drawdown and recovery date are `ไม่พบข้อมูลที่ยืนยันได้`;
the official prospectus reports a worst quarter of `-34.69%` in Q1 2020, which is
not a maximum-drawdown measure.

## Sources

- [iShares EUFN product page](https://www.ishares.com/us/products/239645/ishares-msci-europe-financials-etf) — current YTD, fund facts, exposures, and fees.
- [iShares EUFN factsheet](https://www.ishares.com/us/literature/fact-sheet/eufn-ishares-msci-europe-financials-etf-fund-fact-sheet-en-us.pdf) — official calendar 2021-2025, rolling returns, benchmark, and risk characteristics as of 2026-06-30.
- [BlackRock EUFN calendar-year performance](https://www.ishares.com/ch/professionals/en/products/239645/ishares-msci-europe-financials-etf?switchLocale=Y) — official USD calendar rows 2016-2025.
- [EUFN summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-europe-financials-etf-7-31.pdf) — strategy and worst-quarter disclosure.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
