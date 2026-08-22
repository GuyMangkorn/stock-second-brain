---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWX
ticker: EWX
exchange: NYSE Arca
fund: State Street SPDR S&P Emerging Markets Small Cap ETF
tracked_index: S&P Emerging Under USD2 Billion Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-07-31
calendar_years_as_of: 2026-07-08
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return where official; secondary dividend-reinvested proxy for calendar rows
tags:
  - analysis/etf-performance
  - ticker/EWX
  - geography/Emerging-Markets
---

# EWX Performance

> Navigation: [[ETF Region Index]] → [[Emerging Markets ETF]] → [[ETF Performance Index]]

## Bottom line

EWX เป็น passive/index-tracking emerging-markets small-cap equity ETF ของ State
Street ที่ติดตาม `S&P Emerging Under USD2 Billion Index` และมี gross expense
ratio `0.65%`. Official issuer รายงาน 10-year NAV Total Return average annual
`7.95%` และ current NAV TR YTD `3.91%` ณ 2026-07-31. เนื่องจาก official
capture ไม่เปิดเผย complete calendar-year NAV rows ตาราง 2016-2025 ใช้
secondary dividend-reinvested total-return proxy* และไม่ถูก relabel เป็น NAV
performance.

## Performance check

- `entity_key`: `NYSE Arca:EWX`
- Inception: 2008-05-12
- Expense ratio: `0.65%` gross
- Metric: official NAV Total Return includes reinvested distributions and fund expenses; USD; market-price return remains separate
- Tracked index (issuer benchmark): `S&P Emerging Under USD2 Billion Index`
- Management mode: `passive-index`
- Strategy: sampling strategy; at least 80% in index securities/ADRs/GDRs; incidental futures may be used for index tracking and cash flows
- 10-year NAV TR: official issuer-reported average annual `7.95%` as of 2026-07-31; raw rolling endpoints and exact elapsed years are not disclosed
- Current official NAV TR YTD: `3.91%` as of 2026-07-31
- Common calendar window: secondary total-return proxy 2016-2025 cumulative `128.55%` / rounded-input CAGR `8.62%`; not official NAV rows
- 2021-2025 secondary proxy cumulative `46.36%` / CAGR `7.92%`; S&P 500 cached 2021-2025 cumulative `96.17%` / CAGR `14.43%`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark); not the issuer tracking benchmark
- Coverage/source note: State Street official performance is NAV-based, net of fees, and assumes reinvestment. ETFreplay rows marked `*` are a single secondary dividend-reinvested total-return proxy, not issuer NAV rows. FinanceCharts showed small `0.01–0.03 pp` differences and was not mixed.

| Year | EWX secondary total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.94% | 11.96% |
| 2017 | 34.10% | 21.83% |
| 2018 | -18.74% | -4.38% |
| 2019 | 15.59% | 31.49% |
| 2020 | 14.86% | 18.40% |
| 2021 | 18.16% | 28.71% |
| 2022 | -15.00% | -18.11% |
| 2023 | 18.15% | 26.29% |
| 2024 | 6.84% | 25.02% |
| 2025 | 15.44% | 17.88% |

`*` Annual EWX values are ETFreplay dividend-adjusted total-return observations,
not issuer-published NAV rows. S&P 500 rows reuse the cached USD Total Return
convention as of 2025-12-31.

## Up years / Down years

- Up years / Down years: `8 / 2` in the complete 2016-2025 proxy window
- Best: 2017, `+34.10%`*
- Least positive: 2016, `+7.94%`*
- Worst: 2018, `-18.74%`*
- Least bad down year: 2022, `-15.00%`*
- 2016-2025 rounded-input CAGR: `8.62%`*; 2021-2025: `7.92%`*
- Current official NAV TR YTD: `+3.91%` as of 2026-07-31

## Risk read-through

EWX มี emerging-market, FX, China/Taiwan, small-cap, liquidity, technology และ
non-diversification risk. State Street prospectus รายงาน best quarter `+25.82%`
ใน Q2 2020 และ worst quarter `-28.68%` ใน Q1 2020. Official page รายงาน 3,381
holdings และ country weights Taiwan `31.79%`, India `18.50%`, China `17.82%`,
ทั้งหมด as of 2026-08-14. Latest official NAV คือ `$72.25` และ market price
`$71.89` ณ 2026-08-14; เป็น point-in-time values ไม่ใช่ NAV TR. Official daily
NAV history ที่ยืนยันได้สำหรับคำนวณ max drawdown และ recovery ยังไม่พบข้อมูลที่
ยืนยันได้ จึงไม่ใช้ secondary proxy สร้างตัวเลข NAV drawdown/recovery.

## Sources

- [Official State Street EWX product/performance page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-emerging-markets-small-cap-etf-ewx) — identity, index, passive strategy, current fund fields and official rolling performance.
- [Official EWX factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-ewx.pdf) — standardized NAV, market-price and index performance through 2026-06-30.
- [SEC EWX summary prospectus](https://www.sec.gov/Archives/edgar/data/1168164/000119312526031211/d87745d497k.htm) — fees, passive strategy, index construction, risks and best/worst quarters.
- [ETFreplay EWX annual total-return table](https://www.etfreplay.com/etf/ewx) — secondary dividend-adjusted calendar-year proxy.
- [FinanceCharts EWX performance table](https://www.financecharts.com/etfs/EWX/performance) — secondary cross-check; not mixed into the annual proxy.
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition.
- Cached S&P 500 TR references: historical S&P 500 research and market-attributes sources retained by the ETF performance convention.
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
