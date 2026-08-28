---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:CNYA
ticker: CNYA
exchange: Cboe BZX
fund: iShares MSCI China A ETF
tracked_index: MSCI China A Inclusion Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-28
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-08-26
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/CNYA
  - geography/China
---

# CNYA Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

CNYA เป็น passive/index-tracking China A-share equity ETF ของ iShares ติดตาม `MSCI China A Inclusion Index (Net)` และเริ่มกองทุนเมื่อ 2016-06-13. Official rolling 10-year NAV Total Return ครอบคลุม 2016-06-30 ถึง 2026-06-30 ครบ `10.00` ปี; cumulative return คือ `91.51%` และ CAGR `6.71%` ต่อปี. Current official NAV TR YTD คือ `3.57%` ณ 2026-08-26; NAV ล่าสุดที่ตรวจสอบได้คือ `USD 36.08` ณ 2026-08-27.

## Performance check

- `entity_key`: `Cboe BZX:CNYA`
- Fund: iShares MSCI China A ETF; asset class `Equity`; expense ratio `0.60%`
- Inception: `2016-06-13`
- Metric: official NAV Total Return, รวม reinvested distributions และหัก fund expenses แล้ว
- Issuer benchmark: MSCI China A Inclusion Index (Net); iShares notes that CNYA began tracking this index on `2018-04-26`, with earlier historical index data for MSCI China A International Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not issuer benchmark)
- Management mode: `passive-index`
- Current NAV: `USD 36.08` as of `2026-08-27`; current NAV TR YTD: `3.57%` as of `2026-08-26`

### Official 10-year NAV TR window

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative return | CAGR | Disclosure |
|---|---|---:|---:|---:|---:|---:|---|
| 2016-06-30 | 2026-06-30 | 10.00 | 100.00 (normalized) | 191.51 (normalized from official cumulative return) | 91.51% | 6.71% | Raw start/end NAV TR values not disclosed by issuer |

Normalized endpoint uses the official cumulative NAV TR `91.51%`: `100.00 × (1 + 91.51%) = 191.51`; it is not a raw NAV value.

### Annual NAV Total Return

| Year | CNYA NAV TR | MSCI China A Inclusion Index (Net) TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not applicable (partial inception year) | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | 2.96% | 3.20% | 28.71% |
| 2022 | -26.31% | -25.90% | -18.11% |
| 2023 | -13.51% | -13.47% | 26.29% |
| 2024 | 11.08% | 11.70% | 25.02% |
| 2025 | 25.59% | 26.48% | 17.88% |
| 2026 YTD (month-end) | 12.01% | 11.74% | not comparable; current year not cached |

Official iShares performance data reviewed here discloses annual NAV/benchmark rows for `2021-2025`; 2016–2020 cells remain `not disclosed` except for the known partial inception marker. The month-end 2026 YTD row is as of `2026-06-30`; current product-page YTD is kept separately because it is as of `2026-08-26`. S&P 500 rows reuse the cached USD Total Return convention as of `2025-12-31`.

### Window calculations and ranking

- Common complete-calendar window `2021-2025`: CNYA NAV TR cumulative `-8.46%`, CAGR `-1.75%`; MSCI China A Inclusion benchmark cumulative `-6.52%`, CAGR `-1.34%`; S&P 500 TR cumulative `96.17%`, CAGR `14.43%`; CNYA trails S&P by approximately `16.18 pp` CAGR.
- Up years / down years in `2021-2025`: `3 / 2`.
- Best complete year: `2025`, `25.59%`; least positive: `2021`, `2.96%`.
- Worst complete year: `2022`, `-26.31%`; least bad down year: `2023`, `-13.51%`.
- Current NAV TR YTD: `3.57%` as of `2026-08-26`; this is a partial-year observation, not a calendar-year ranking.

## Risk read-through

CNYA เป็น single-country China A-share exposure ผ่าน Shanghai/Shenzhen equities. Official page reports `411` holdings as of `2026-08-27`, 3-year standard deviation `19.90%` as of `2026-07-31`, P/E `17.75` and P/B `1.94` as of `2026-08-26`. Stock Connect access, China policy/geopolitical risk, A-share market structure, currency and concentration can increase volatility. Benchmark change on `2018-04-26` ต้องแยก issuer benchmark history ก่อนและหลังการเปลี่ยน index; daily NAV history sufficient for fund-level max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

## Sources

- Official issuer product/performance page (NAV/YTD as of 2026-08-27/2026-08-26; performance table as of 2026-06-30): https://www.ishares.com/us/products/273318/ishares-msci-china-a-etf
- Official iShares factsheet (performance through 2026-06-30): https://www.ishares.com/us/literature/fact-sheet/cnya-ishares-msci-china-a-etf-fund-fact-sheet-en-us.pdf
- Official summary prospectus: https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-china-a-etf-7-31.pdf
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-28]]
- Navigation: [[China ETF]] | [[ETF Region Index]] | [[ETF Performance Index]]
