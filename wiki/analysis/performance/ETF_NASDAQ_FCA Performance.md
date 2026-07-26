---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:FCA
ticker: FCA
exchange: Nasdaq
fund: First Trust China AlphaDEX Fund
tracked_index: Nasdaq AlphaDEX China Index (NQDXCNN)
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FCA
  - geography/China
---

# FCA Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

FCA เป็น passive/index-tracking China equity ETF ที่ติดตาม Nasdaq AlphaDEX China Index. Official First Trust monthly performance report ระบุ rolling 10-year NAV Total Return CAGR `8.19%` สำหรับ `2016-06-30` ถึง `2026-06-30`; current NAV TR YTD อยู่ที่ `-1.23%` ณ `2026-06-30`. Annual NAV TR rows ครบ `2016-2025` ให้ CAGR ที่คำนวณจาก rounded rows `7.28%`, ขณะที่ S&P 500 TR ในช่วงปฏิทินเดียวกันอยู่ที่ `14.82%`.

## Performance check

- entity_key: `Nasdaq:FCA`
- Fund: First Trust China AlphaDEX Fund
- Inception: `2011-04-18`
- Primary listing: Nasdaq
- Total expense ratio: `0.80%` (official factsheet as of `2025-12-31`)
- Tracked index: Nasdaq AlphaDEX China Index (`NQDXCNN`); index inception `2015-05-18`
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Official 10-year window: `2016-06-30` to `2026-06-30`, exactly `10.00` elapsed years
- Official 10-year NAV TR CAGR: `8.19%`
- Raw start/end NAV TR values: not disclosed in the reviewed official performance table
- Implied normalized endpoint: `100.00 × (1 + 0.0819)^10 = 219.72`; this is a calculation from the published CAGR, not a raw NAV/TR endpoint
- Current NAV TR YTD: `-1.23%` as of `2026-06-30`
- Official month-end 10-year benchmark fields: Nasdaq AlphaDEX China Index `9.38%`; the S&P 500 comparison below uses the cached USD Total Return convention

| Year | FCA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -4.96% | 11.96% |
| 2017 | 58.35% | 21.83% |
| 2018 | -17.87% | -4.38% |
| 2019 | 17.34% | 31.49% |
| 2020 | 13.58% | 18.40% |
| 2021 | -1.18% | 28.71% |
| 2022 | -17.10% | -18.11% |
| 2023 | -9.32% | 26.29% |
| 2024 | 15.43% | 25.02% |
| 2025 | 42.95% | 17.88% |
| **2016-2025 compound / CAGR** | **101.92% / 7.28%** | **298.33% / 14.82%** |
| **2021-2025 compound / CAGR** | **22.58% / 4.16%** | **96.17% / 14.43%** |
| 2026 YTD | -1.23% as of 2026-06-30 | not comparable; current year is outside the cached complete-year window |

The annual table uses First Trust's official NAV-based calendar-year returns. First Trust's factsheet shows a conflicting `2025` value of `43.51%` and `2024` value of `14.98%`; the annual shareholder report and May 2026 summary prospectus both report `2025 = 42.95%`, so the audited/reporting documents are used here and the conflict is disclosed in the source batch.

## Up years / Down years

- 2016-2025 up years / down years: `5 / 5`
- Best year: `2017`, `+58.35%`
- Least positive year: `2024`, `+15.43%`
- Worst year: `2022`, `-17.10%`
- Least bad down year: `2021`, `-1.18%`
- 10-year CAGR difference versus S&P 500 TR: `-6.63` percentage points (`8.19%` versus `14.82%`)

## Risk read-through

FCA uses a rules-based AlphaDEX selection process but remains concentrated in China country, VIE/ADR, sector, regulatory, geopolitical and FX risks. The index reconstitutes and rebalances semi-annually. The current benchmark/index was introduced on `2015-07-14`; First Trust warns that pre-change historical returns are not necessarily representative of performance under the current index. Holdings are exposed to China policy, trade restrictions, depositary-receipt liquidity, foreign-market timing and emerging-market volatility.

## Sources

- [First Trust FCA official product/performance page](https://www.ftportfolios.com/Retail/etf/ETFsummary.aspx?Ticker=FCA)
- [First Trust FCA factsheet](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=091b3012-692d-4750-966f-8e1e69ce35bf)
- [First Trust monthly performance report, returns as of 2026-06-30](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=b363655b-cc73-4f42-a7b1-4c1e00306c7c)
- [FCA May 2026 summary prospectus](https://www.sec.gov/Archives/edgar/data/1510337/000144554626003311/fca_497k.htm)
- [FCA 2025 annual shareholder report](https://www.sec.gov/Archives/edgar/data/1510337/000144554626001916/adex2_ncsr.htm)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
