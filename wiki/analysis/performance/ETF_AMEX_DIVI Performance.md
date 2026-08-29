---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DIVI
ticker: DIVI
exchange: NYSE Arca
fund: Franklin International Core Dividend Tilt Index ETF
tracked_index: Morningstar Developed Markets ex-North America Dividend Enhanced Select Index-NR
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2026-07-31
current_ytd_as_of: 2026-08-21
current_nav_as_of: 2026-08-21
fund_facts_as_of: 2026-08-21
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/DIVI
---

# DIVI Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]
> Entity: [[ETF_AMEX_DIVI]]

## Bottom line

DIVI เป็น passive/index-tracking international equity ETF ที่ใช้ dividend/value
tilt และให้ผลตอบแทนเป็นบวก `7 จาก 9` complete calendar years ในช่วง 2017-2025.
Franklin รายงาน rolling 10-year NAV Total Return CAGR `11.13%` ณ 2026-07-31
(ไม่เปิดเผย raw endpoints) และ current NAV TR YTD `16.62%` ณ 2026-08-21. ปีดีที่สุด
คือ 2025 ที่ `+34.51%`; ปีที่แย่ที่สุดคือ 2018 ที่ `-6.18%`.

## Performance check

- `entity_key`: `NYSE Arca:DIVI`
- Fund: Franklin International Core Dividend Tilt Index ETF; `Equity`; expense ratio `0.09%`
- Inception: `2016-06-01`
- Metric: official `NAV Total Return`, รวมการ reinvest distributions และหัก fund expenses
- Issuer benchmark: `Morningstar Developed Markets ex-North America Dividend Enhanced Select Index-NR`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark, not issuer benchmark)
- Type note: Franklin ระบุว่า fund เป็น `Indexed` และมุ่งติดตาม underlying index ของ developed markets ex-North America; futures/swaps/FX forwards ที่อนุญาตเพื่อ implementation ไม่เปลี่ยน classification เป็น passive equity ETF

### Official 10-year NAV TR window

| Window end | Actual years | NAV TR CAGR | Disclosure |
|---|---:|---:|---|
| 2026-07-31 | 10.00 | 11.13% | Issuer-reported average annual NAV return; raw start/end TR values and cumulative return not disclosed |

Franklin's performance convention assumes reinvestment of all distributions and
deduction of fund expenses. The rolling 10-year field is not reconstructed from
unavailable raw endpoints.

### Annual NAV Total Return

| Year | DIVI NAV TR | Morningstar Dividend Enhanced Select Index-NR | S&P 500 TR |
|---|---:|---:|---:|
| 2017 | 12.82% | 13.21% | 21.83% |
| 2018 | -6.18% | -5.75% | -4.38% |
| 2019 | 22.66% | 23.21% | 31.49% |
| 2020 | 1.55% | 1.86% | 18.40% |
| 2021 | 17.22% | 17.63% | 28.71% |
| 2022 | -1.74% | -1.43% | -18.11% |
| 2023 | 19.23% | 18.96% | 26.29% |
| 2024 | 2.36% | 2.28% | 25.02% |
| 2025 | 34.51% | 34.32% | 17.88% |

Franklin's official factsheet publishes the 2017-2025 calendar rows; 2016 is
the inception year and is shown as unavailable rather than ranked. The S&P 500
rows use the cached USD Total Return convention for the same complete calendar
years, as of 2025-12-31.

### Window calculations and ranking

- Common `2021-2025`: DIVI NAV compound `89.08%`, CAGR `13.59%`; S&P 500 TR compound `96.17%`, CAGR `14.43%`.
- `2017-2025`: DIVI compound `149.29%`, rounded-input CAGR `10.68%`; S&P 500 TR compound `255.78%`, CAGR `15.14%`.
- Up years / down years in `2017-2025`: `7 / 2`.
- Best: `2025`, `+34.51%`; least positive: `2024`, `+2.36%`.
- Worst: `2018`, `-6.18%`; least bad down year: `2022`, `-1.74%`.
- Current NAV TR YTD: `16.62%` as of `2026-08-21`; current NAV: `USD 44.55` as of `2026-08-21`.

## Risk read-through

DIVI เป็น developed-markets ex-North America dividend/value tilt ไม่ใช่ high-yield
หรือ crisis-protection vehicle. Franklin's latest product snapshot shows total
net assets `USD 2.77B` as of 2026-08-23, geographic exposure Europe `59.34%`,
Asia `28.58%`, Australia/New Zealand `9.13%` as of 2026-08-20, 30-Day SEC Yield
`3.01%` as of 2026-07-31, and distribution rate at NAV `2.98%` as of 2026-08-21.
Expense ratio is `0.09%`; distributions are quarterly. Secondary adjusted-price
total-return evidence reports maximum drawdown about `-27.76%` on 2020-03-12 and
`207` trading sessions to recover. This is a secondary price-plus-distributions
proxy, not a fund-level official NAV series; official daily NAV data sufficient
for an independently reproducible max drawdown, recovery, or volatility measure
is `ไม่พบข้อมูลที่ยืนยันได้`.

The main behavior remains country, sector, FX, and value/dividend-factor
sensitivity. The latest official factsheet held `417` positions as of 2026-06-30;
the current performance snapshot does not provide a newer complete holdings file.

## Sources

- Official Franklin DIVI product/performance page: https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/21412/SINGLCLASS/franklin-international-core-dividend-tilt-index-etf/DIVI?role=fp
- Official Franklin DIVI factsheet: https://www.franklintempleton.com/forms-literature/download/DIVI-FF
- Secondary PortfoliosLab drawdown page: https://portfolioslab.com/symbol/DIVI
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-29]]
- Navigation: [[International ETF]] | [[ETF Region Index]] | [[ETF Performance Index]]
