---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:VTWV
ticker: VTWV
exchange: NASDAQ
fund: Vanguard Russell 2000 Value ETF
updated: 2026-08-16
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VTWV
  - geography/United-States
---

# VTWV Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

VTWV เป็น passive/index-tracking U.S. small-cap value ETF ที่ติดตาม Russell 2000 Value Index. ใน complete calendar window 2016-2025 มี 8 ปีบวก / 2 ปีลบ; best คือ 2016 ที่ +31.55% และ worst คือ 2022 ที่ -14.56%. Current official NAV TR YTD อยู่ที่ +23.63% ณ 2026-07-17.

## Performance check

- `entity_key: NASDAQ:VTWV`
- Inception: 2010-09-20
- Expense ratio: 0.06% ณ 2026-06-30
- Metric: `NAV Total Return` รวม reinvested dividends/capital-gain distributions และ fund expenses; USD
- Tracked index (issuer benchmark): Russell 2000 Value Index
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year window: 2016-06-30 to 2026-06-30
- 10-year NAV TR: issuer-reported average annual 10.86% ณ 2026-06-30; raw endpoints และ cumulative total return ไม่ได้เปิดเผย จึงไม่คำนวณ normalized endpoint
- Common calendar window: official 2016-2025 NAV TR cumulative 141.46% / rounded-input CAGR 9.22%; 2021-2025 cumulative 52.63% / CAGR 8.83%.
- Coverage/source note: annual rows 2016-2024 มาจาก official Vanguard prospectus chart และ 2025 row มาจาก official Vanguard Total Returns snapshot ณ 2025-12-31. Current YTD ใช้ newer official advisor-page observation ณ 2026-07-17; earlier official factsheet snapshot คือ 22.99% ณ 2026-06-30 จึงไม่ถือเป็น same-date conflict.

| Year | VTWV NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.55% | 11.96% |
| 2017 | 7.78% | 21.83% |
| 2018 | -12.92% | -4.38% |
| 2019 | 22.33% | 31.49% |
| 2020 | 4.74% | 18.40% |
| 2021 | 28.13% | 28.71% |
| 2022 | -14.56% | -18.11% |
| 2023 | 14.66% | 26.29% |
| 2024 | 7.98% | 25.02% |
| 2025 | 12.61% | 17.88% |

**Up years / Down years**

- Up years / Down years: 8 / 2 in 2016-2025
- Best: 2016, +31.55%
- Least positive: 2020, +4.74%
- Worst: 2022, -14.56%
- Least bad down year: 2018, -12.92%
- Current VTWV NAV TR YTD: +23.63% as of 2026-07-17

## Risk read-through

Issuer factsheet reports 3-year monthly standard deviation 19.42% ณ 2026-06-30; small-cap value exposure therefore carries meaningful cyclicality, liquidity and valuation-style risk. The 10-year issuer average annual NAV TR is 10.86%, while the rounded 2016-2025 calendar-row CAGR is lower at 9.22% because the windows and endpoints differ. Official daily NAV history sufficient to verify maximum drawdown and recovery was not located, so no numeric proxy is used. The fund is passive and full-replication, distributes quarterly, and its 0.06% expense ratio supports tracking but does not remove small-cap downside risk.

## Sources

- [Official Vanguard VTWV product page](https://investor.vanguard.com/investment-products/etfs/profile/vtwv)
- [Official Vanguard advisor VTWV performance page](https://advisors.vanguard.com/investments/products/vtwv/vanguard-russell-2000-value-etf)
- [Official Vanguard VTWV factsheet, June 30, 2026](https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3352.pdf)
- [Official Vanguard Russell ETFs prospectus chart](https://fund-docs.vanguard.com/p3348.pdf)
- [SEC summary prospectus for VTWV](https://www.sec.gov/Archives/edgar/data/1021882/000119312525325212/f43593d1.htm)
- [Vanguard Total Returns chart](https://institutional.vanguard.com/content/dam/inst/iig-transformation/pdf/total_return_chart.pdf)
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-16]] | [[ETF Performance Index]]

