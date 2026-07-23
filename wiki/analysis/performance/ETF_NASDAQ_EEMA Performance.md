---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:EEMA
ticker: EEMA
exchange: NASDAQ
fund: iShares MSCI Emerging Markets Asia ETF
tracked_index: MSCI EM Asia Custom Capped Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-22
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EEMA
  - geography/Emerging-Markets
---

# EEMA Performance

> Navigation: [[ETF Region Index]] → [[Emerging Markets ETF]] → [[ETF Performance Index]]

## Bottom line

EEMA เป็น passive/index-tracking equity ETF ที่ติดตาม MSCI EM Asia Custom Capped Index (Net). Official iShares ระบุ rolling 10-year NAV Total Return cumulative `172.29%` และ CAGR `10.54%` ณ 2026-06-30 ครอบคลุม 10.00 elapsed years. เนื่องจาก issuer ไม่เปิดเผย raw NAV TR endpoints จึงแสดง normalized start `100.00` และ end `272.29` จาก official cumulative return. Calendar-year NAV TR 2016-2025 compound เป็น `121.24%` และ CAGR `8.26%`; common 2021-2025 compound เป็น `17.94%` และ CAGR `3.36%`. Current NAV YTD ล่าสุดคือ `20.51%` ณ 2026-07-22.

## Performance check

- entity_key: NASDAQ:EEMA
- Inception: 2012-02-08
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index (issuer benchmark): MSCI EM Asia Custom Capped Index (Net)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR cumulative: `172.29%`; normalized TR start `100.00`, end `272.29`
- 10-year NAV TR CAGR: `10.54%` (official issuer average annual total return)
- Coverage/source note: 2016-2020 NAV rows are from the official summary prospectus; 2021-2025 NAV rows are from the current official performance page/factsheet. The issuer discloses an index change on 2018-06-01: historical index data before that date is MSCI Emerging Markets Asia Index (Net), and data after is MSCI EM Asia Custom Capped Index (Net). S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed.

| Year | EEMA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 5.59% | 11.96% |
| 2017 | 41.94% | 21.83% |
| 2018 | -15.54% | -4.38% |
| 2019 | 18.36% | 31.49% |
| 2020 | 25.20% | 18.40% |
| 2021 | -4.19% | 28.71% |
| 2022 | -21.45% | -18.11% |
| 2023 | 6.98% | 26.29% |
| 2024 | 10.71% | 25.02% |
| 2025 | 32.32% | 17.88% |

## Up years / Down years

- Up years / Down years: `7 / 3` over calendar years 2016-2025
- Best: 2017, `41.94%`
- Least positive: 2016, `5.59%`
- Worst: 2022, `-21.45%`
- Least bad down year: 2018, `-15.54%`
- Calendar 2016-2025 cumulative/CAGR: `121.24% / 8.26%`
- Common 2021-2025 cumulative/CAGR: `17.94% / 3.36%`; positive / negative `3 / 2`
- Current YTD: `20.51%` as of 2026-07-22; latest NAV `US$112.84` on the same date

## Risk read-through

EEMA มี 879 holdings ณ 2026-07-22 และกระจายหลักไป China `31.53%`, Taiwan `31.06%`, South Korea `16.82%`, และ India `16.09%`. Sector concentration อยู่ที่ Information Technology `40.56%` และ Financials `16.93%`. Expense ratio คือ `0.49%`; standard deviation 3-year `17.00%` ณ 2026-06-30. ความเสี่ยงหลักคือ emerging-market/country/FX, China/Taiwan/Korea concentration และ tracking difference จาก fees, withholding tax, fair valuation และ index change. Daily NAV history สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official issuer product and performance page: https://www.ishares.com/us/products/239629/ishares-msci-emerging-markets-asia-etf
- Official issuer factsheet: https://www.ishares.com/us/literature/fact-sheet/eema-ishares-msci-emerging-markets-asia-etf-fund-fact-sheet-en-us.pdf
- Official summary prospectus: https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-emerging-markets-asia-etf-8-31.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
