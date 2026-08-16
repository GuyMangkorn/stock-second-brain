---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:VTWG
ticker: VTWG
exchange: NASDAQ
fund: Vanguard Russell 2000 Growth ETF
updated: 2026-08-16
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VTWG
  - geography/United-States
---

# VTWG Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

VTWG เป็น passive/index-tracking U.S. small-cap growth ETF ที่ติดตาม Russell 2000 Growth Index. ใน complete calendar window 2016-2025 มี 8 ปีบวก / 2 ปีลบ; best คือ 2020 ที่ +34.70% และ worst คือ 2022 ที่ -26.35%. Current official NAV TR YTD อยู่ที่ +16.85% ณ 2026-07-17.

## Performance check

- `entity_key: NASDAQ:VTWG`
- Inception: 2010-09-20
- Expense ratio: 0.06% ณ 2026-06-30
- Metric: `NAV Total Return` รวม reinvested dividends/capital-gain distributions และ fund expenses; USD
- Tracked index (issuer benchmark): Russell 2000 Growth Index
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year window: 2016-06-30 to 2026-06-30
- 10-year NAV TR: issuer-reported cumulative 210.66% / annualized 12.00% ณ 2026-06-30. Raw endpoints ไม่ได้เปิดเผย; normalized TR index representation คือ 100.00 → 310.66 over 10.00 years. Formula: `(310.66 / 100.00)^(1 / 10.00) - 1 = 12.00%`.
- Common calendar window: official 2016-2025 NAV TR cumulative 150.23% / rounded-input CAGR 9.61%; 2021-2025 cumulative 17.08% / CAGR 3.20%.
- Coverage/source note: annual rows are official Vanguard NAV total returns as of 2025-12-31. Current YTD uses the newer official advisor-page observation as of 2026-07-17; earlier official snapshots were 20.04% as of 2026-07-02 and 22.23% as of 2026-06-30, so they are not treated as same-date conflicts.

| Year | VTWG NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 11.40% | 11.96% |
| 2017 | 22.13% | 21.83% |
| 2018 | -9.31% | -4.38% |
| 2019 | 28.59% | 31.49% |
| 2020 | 34.70% | 18.40% |
| 2021 | 2.82% | 28.71% |
| 2022 | -26.35% | -18.11% |
| 2023 | 18.73% | 26.29% |
| 2024 | 15.17% | 25.02% |
| 2025 | 13.07% | 17.88% |

**Up years / Down years**

- Up years / Down years: 8 / 2 in 2016-2025
- Best: 2020, +34.70%
- Least positive: 2021, +2.82%
- Worst: 2022, -26.35%
- Least bad down year: 2018, -9.31%
- Current VTWG NAV TR YTD: +16.85% as of 2026-07-17

## Risk read-through

Issuer factsheet reports 3-year monthly standard deviation 21.30% ณ 2026-06-30; the small-cap growth style therefore carries meaningful cyclicality, liquidity and valuation risk. The 10-year issuer annualized NAV TR is 12.00%, while the rounded 2016-2025 calendar-row CAGR is lower at 9.61% because the windows and endpoints differ. Official daily NAV history sufficient to verify maximum drawdown and recovery was not located, so no numeric proxy is used. The fund is passive and full-replication, distributes quarterly, and its 0.06% expense ratio supports tight tracking but does not remove small-cap downside risk.

## Sources

- [Official Vanguard VTWG product page](https://investor.vanguard.com/investment-products/etfs/profile/vtwg)
- [Official Vanguard advisor VTWG performance page](https://advisors.vanguard.com/investments/products/vtwg/vanguard-russell-2000-growth-etf)
- [Official Vanguard VTWG factsheet, June 30, 2026](https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3353.pdf)
- [Vanguard Total Returns chart, June 30, 2026](https://institutional.vanguard.com/content/dam/inst/iig-transformation/pdf/total_return_chart.pdf)
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-16]] | [[ETF Performance Index]]
