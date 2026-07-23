---
type: etf-performance
instrument_type: ETF
entity_key: LSE:SAUS
ticker: ISSSF
exchange: LSE
fund: iShares MSCI Australia UCITS ETF
tracked_index: MSCI Australia Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/ISSSF
  - geography/Australia
---

# ISSSF Performance

> Navigation: [[ETF Region Index]] → [[Australia ETF]] → [[ETF Performance Index]]

## Bottom line

ISSSF เป็น OTC alias ของ iShares MSCI Australia UCITS ETF ซึ่งมี canonical
listing เป็น `LSE:SAUS`. กองเป็น passive, physically replicated/index-tracking
equity ETF ที่ติดตาม MSCI Australia Index (Net). Official rolling NAV Total
Return 10 ปี ณ 2026-06-30 อยู่ที่ cumulative `121.17%` และ CAGR `8.26%` จาก
normalized TR 100.00 เป็น 221.17 ใน 10.00 ปี. Official calendar NAV TR rows
2016-2025 compound ได้ `109.27%` หรือ CAGR `7.66%`; common window 2021-2025
ได้ CAGR `6.24%` เทียบกับ S&P 500 TR `14.43%`. Current NAV TR YTD ล่าสุดที่
ยืนยันได้คือ `10.27%` ณ 2026-07-21.

## Performance check

- input ticker: ISSSF
- entity_key: LSE:SAUS
- Inception: 2010-01-22
- Metric: NAV Total Return with gross income reinvested where applicable; NAV performance is kept separate from market price
- Tracked index (issuer benchmark): MSCI Australia Index (Net)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year window: 2016-06-30 to 2026-06-30
- 10-year NAV TR CAGR: 8.26%; start TR value 100.00 and end TR value 221.17 เป็น normalized levels จาก official cumulative return; actual years 10.00
- Formula: (221.17 / 100.00)^(1 / 10.00) - 1 = 8.26%
- Calendar-row calculation: official rows 2016-2025 compound to 109.27% and CAGR 7.66%; rows 2021-2025 compound to 35.36% and CAGR 6.24%
- Coverage/source note: rolling return is as of 2026-06-30; annual rows are as of 2025-12-31; current YTD is as of 2026-07-21. Raw NAV endpoint levels are not disclosed.

| Year | ISSSF / SAUS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 11.00% | 11.96% |
| 2017 | 19.60% | 21.83% |
| 2018 | -12.30% | -4.38% |
| 2019 | 22.50% | 31.49% |
| 2020 | 8.40% | 18.40% |
| 2021 | 9.00% | 28.71% |
| 2022 | -5.70% | -18.11% |
| 2023 | 14.30% | 26.29% |
| 2024 | 0.80% | 25.02% |
| 2025 | 14.30% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ SAUS;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31.

## Up years / Down years

- Up years / Down years: 8 / 2
- Best: 2019, +22.50%
- Least positive: 2024, +0.80%
- Worst: 2018, -12.30%
- Least bad down year: 2022, -5.70%
- Current YTD: +10.27% as of 2026-07-21

## Risk read-through

SAUS เป็น single-country Australia equity ETF จึงมี country, currency,
commodity และ sector concentration. Expense ratio อยู่ที่ 0.50%; official
page ระบุ 47 holdings และ 3-year standard deviation 17.36% ณ 2026-06-30.
Daily NAV history สำหรับการคำนวณ max drawdown และ recovery: ไม่พบข้อมูลที่
ยืนยันได้ใน lean capture.

## Sources

- Official issuer product and performance page:
  https://www.ishares.com/uk/professional/en/products/251851/ishares-msci-australia-ucits-etf
- Official issuer factsheet:
  https://www.ishares.com/uk/individual/en/literature/fact-sheet/saus-ishares-msci-australia-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y
- Official S&P 500 index page:
  https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
