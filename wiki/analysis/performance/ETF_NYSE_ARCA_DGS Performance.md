---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DGS
ticker: DGS
exchange: NYSE Arca
fund: WisdomTree Emerging Markets SmallCap Dividend Fund
tracked_index: WisdomTree Emerging Markets SmallCap Dividend Index (WTEMSC)
benchmark: S&P 500 Total Return
updated: 2026-08-16
performance_as_of: 2026-07-31
annual_rows_as_of: 2026-03-31
current_ytd_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/DGS
  - geography/Emerging-Markets
---

# DGS Performance

> Navigation: [[ETF Region Index]] → [[Emerging Markets ETF]] → [[ETF Performance Index]]

## Bottom line

DGS เป็น passive/index-tracking equity ETF ของ WisdomTree ที่ลงทุนใน emerging-markets small-cap dividend exposure และมี expense ratio 0.58%. จาก annual NAV Total Return ที่เปิดเผยครบปี 2016–2025 ผลตอบแทนสะสมที่คำนวณจาก rounded inputs อยู่ที่ 138.91% หรือ CAGR 9.10% เทียบกับ S&P 500 Total Return 298.33% หรือ 14.82%. Current NAV TR YTD อยู่ที่ 8.86% ณ 2026-07-31; issuer รายงาน 10-year average annual NAV TR 8.31% ณ วันเดียวกัน.

## Performance check

- entity_key: NYSE Arca:DGS
- Fund: WisdomTree Emerging Markets SmallCap Dividend Fund
- Asset class / type: Equity / Indexed; passive/index-tracking
- Inception: 2007-10-30
- Expense ratio: 0.58% gross / 0.58% net
- Tracked index: WisdomTree Emerging Markets SmallCap Dividend Index (Bloomberg symbol WTEMSC)
- Strategy: กองทุนมุ่งติดตาม price and yield performance ของดัชนี WTEMSC ก่อนหักค่าธรรมเนียมและค่าใช้จ่าย
- Primary metric: official NAV Total Return รวมการ reinvest distributions และสะท้อน fund expenses ใน NAV; USD; แยกจาก market-price return
- 10-year NAV TR: issuer-reported average annual NAV Total Return 8.31% ณ 2026-07-31; issuer ไม่ได้เปิดเผย raw start/end TR values, exact endpoint dates, หรือ elapsed years ในข้อมูลที่ตรวจสอบได้
- Annual NAV TR rows: official DGS presentation dated 2026-03-31; current/YTD fields below use the later issuer performance snapshot as of 2026-07-31
- Benchmark note: S&P 500 rows use cached USD Total Return convention as of 2025-12-31; 2026 current-year benchmark ไม่ได้ใช้เพราะไม่มี current cache

| Year | DGS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 14.91% | 11.96% |
| 2017 | 35.48% | 21.83% |
| 2018 | -15.39% | -4.38% |
| 2019 | 17.28% | 31.49% |
| 2020 | 4.14% | 18.40% |
| 2021 | 15.60% | 28.71% |
| 2022 | -12.15% | -18.11% |
| 2023 | 18.92% | 26.29% |
| 2024 | 2.13% | 25.02% |
| 2025 | 20.40% | 17.88% |
| 2026 YTD | 8.86% | not comparable; current-year cache not available |

### Window calculations

| Window | DGS NAV TR | S&P 500 TR | DGS minus S&P CAGR |
|---|---:|---:|---:|
| 2016–2025 | cumulative 138.91%; CAGR 9.10% | cumulative 298.33%; CAGR 14.82% | -5.72 pp |
| 2021–2025 | cumulative 48.50%; CAGR 8.23% | cumulative 96.17%; CAGR 14.43% | -6.20 pp |

Formula: CAGR = product(1 + annual return)^(1 / number of years) - 1. DGS calculations use disclosed rounded annual NAV TR rows; cumulative and CAGR figures are rounded-input approximations. S&P 500 is a common reference benchmark, not the fund's issuer benchmark.

### Up years / Down years

For complete calendar years 2016–2025, DGS had 8 up years and 2 down years.

- Best year: 2017, 35.48%
- Least positive year: 2024, 2.13%
- Worst year: 2018, -15.39%
- Least bad down year: 2022, -12.15%
- Current YTD: 8.86% as of 2026-07-31

## Risk read-through

Issuer-reported 10-year average annual NAV TR is 8.31% as of 2026-07-31, while the rounded 2021–2025 annual profile compounds to 8.23% CAGR. The exposure is structurally sensitive to emerging-market country risk, FX, small-cap liquidity and dividend/value regimes. Official prospectus observations show a best quarter of +20.84% in 2Q2020 and a worst quarter of -30.56% in 1Q2020; these are quarterly NAV TR observations, not a maximum-drawdown series.

Official daily NAV history sufficient to calculate maximum drawdown and recovery is ไม่พบข้อมูลที่ยืนยันได้. Conflicting secondary drawdown series were reviewed but are not retained because the series definitions and source reconciliation are unresolved; no secondary proxy is used in the annual ranking.

The latest verified NAV was 63.900 USD and market price was 63.570 USD, a -0.519% discount to NAV, both as of 2026-08-14; these are point-in-time values, not NAV TR.

Recent cash distributions were 0.84000 USD ex/pay 2026-06-25/2026-06-29, 0.20000 USD ex/pay 2026-03-26/2026-03-30, 0.57891 USD ex/pay 2025-12-26/2025-12-30, and 0.79500 USD ex/pay 2025-09-25/2025-09-29. They are not added again to NAV TR because the total-return series assumes reinvestment.

## Sources

- Official WisdomTree product page: https://www.wisdomtree.com/us/products/equity/dgs
- Official WisdomTree factsheet: https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-dgs-1068.pdf
- Official DGS presentation / annual NAV TR rows, dated 2026-03-31: https://www.wisdomtree.com/us/media/dgs-presentation
- SEC summary prospectus: https://www.sec.gov/Archives/edgar/data/1350487/000121465925011290/dgs73125497k.htm
- Official WisdomTree index page: https://www.wisdomtree.com/us/indexes/WTEMSC
- S&P 500 official index page and cached convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- Cached S&P source references: https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/; https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/
