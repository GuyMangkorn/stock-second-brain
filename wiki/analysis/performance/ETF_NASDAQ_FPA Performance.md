---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:FPA
ticker: FPA
exchange: Nasdaq
fund: First Trust Asia Pacific ex-Japan AlphaDEX Fund
tracked_index: Nasdaq AlphaDEX Asia Pacific Ex-Japan Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FPA
  - geography/Asia-Pacific
---

# FPA Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

FPA เป็น passive/index-tracking equity ETF และ First Trust prospectus ระบุว่าเป็น index fund ที่ไม่ได้บริหารแบบ active. กองทุนติดตาม Nasdaq AlphaDEX Asia Pacific Ex-Japan Index ซึ่งเป็น enhanced index ที่ใช้ AlphaDEX stock-selection methodology. Official rolling 10-year NAV Total Return CAGR คือ `10.31%` สำหรับ `2016-06-30` ถึง `2026-06-30` ครบ `10.00 elapsed years`. Annual NAV TR rows `2016-2025` compound เป็น `89.03%` หรือ CAGR `6.57%`; common `2021-2025` compound เป็น `41.79%` หรือ CAGR `7.23%`, เทียบกับ S&P 500 TR `96.17%` หรือ `14.43%`.

## Performance check

- entity_key: `NASDAQ:FPA`
- Fund: First Trust Asia Pacific ex-Japan AlphaDEX Fund
- Inception: `2011-04-18`
- Asset class / type: International equity; passive/index fund
- Tracked index: Nasdaq AlphaDEX Asia Pacific Ex-Japan Index
- Expense ratio: `0.80%` as of `2026-05-01`
- Metric: NAV Total Return with distributions reinvested and fund expenses reflected in fund returns
- Official 10-year window: `2016-06-30` → `2026-06-30`
- Actual elapsed years: `10.00`
- Official 10-year NAV TR CAGR: `10.31%`
- Raw start/end NAV TR values and rolling cumulative return: `not disclosed` in the reviewed official capture
- Current standardized NAV TR YTD: `42.71%` as of `2026-06-30`; later date-to-date YTD is not disclosed in the reviewed official capture
- Issuer benchmark: Nasdaq AlphaDEX Asia Pacific Ex-Japan Index; common comparison benchmark: S&P 500 Total Return (USD, dividends reinvested)
- Index methodology break: underlying index changed from Defined Asia Pacific Ex-Japan Index to Nasdaq AlphaDEX Asia Pacific Ex-Japan Index on `2015-10-13`; pre-change history is retained as issuer-reported fund NAV TR and is not presented as a pure current-index backtest

### Annual NAV Total Return

First Trust's prospectus provides complete calendar-year NAV total returns for `2016-2025`. S&P 500 TR rows use the cached USD Total Return convention as of `2025-12-31`.

| Year | FPA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 0.29% | 11.96% |
| 2017 | 35.93% | 21.83% |
| 2018 | -20.71% | -4.38% |
| 2019 | 7.35% | 31.49% |
| 2020 | 14.89% | 18.40% |
| 2021 | 2.75% | 28.71% |
| 2022 | -15.62% | -18.11% |
| 2023 | 10.67% | 26.29% |
| 2024 | 3.84% | 25.02% |
| 2025 | 42.31% | 17.88% |

### Calculations and comparison

- FPA NAV TR `2016-2025`: cumulative `89.03%`, CAGR `6.57%`
- S&P 500 TR `2016-2025`: cumulative `298.33%`, CAGR `14.82%`
- FPA NAV TR `2021-2025`: cumulative `41.79%`, CAGR `7.23%`
- S&P 500 TR `2021-2025`: cumulative `96.17%`, CAGR `14.43%`
- Common-window relative CAGR: FPA trails S&P 500 TR by approximately `7.20 percentage points`

## Up years / Down years

- Complete years `2016-2025`: up `8`, down `2`
- Best year: `2025`, `42.31%`
- Worst year: `2018`, `-20.71%`
- Common years `2021-2025`: up `4`, down `1`
- Official rolling 10-year NAV TR CAGR: `10.31%` as of `2026-06-30`
- Current standardized NAV TR YTD: `42.71%` as of `2026-06-30`

## Risk read-through

FPA มีประมาณ `100` holdings excluding cash as of `2026-06-23`; country exposure หลักคือ South Korea `57.49%`, Hong Kong `25.27%`, Australia `9.65%`, Singapore `5.87%`, Taiwan `1.24%`, และ China `0.48%`. Three-year standard deviation คือ `24.53%` as of `2026-05-29`. ความเสี่ยงหลักคือ Asia-Pacific concentration, country/FX risk, small- and mid-cap volatility และ index-methodology turnover. Daily NAV history ที่ยืนยันได้เพียงพอสำหรับ max drawdown/recovery ไม่ได้เปิดเผยใน reviewed capture.

## Sources

- Official product/performance page: [First Trust Asia Pacific ex-Japan AlphaDEX Fund](https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FPA)
- Official monthly performance report: [First Trust ETF Monthly Performance Report](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=b363655b-cc73-4f42-a7b1-4c1e00306c7c)
- Official prospectus: [First Trust Exchange-Traded AlphaDEX Fund II prospectus](https://www.ftportfolios.com/LoadContent/gradkqbz8r4y)
- Official fund documents route: [FPA fund documents](https://www.ftportfolios.com/fund-documents/etf/FPA)
- Common reference benchmark: [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); annual rows use the cached USD Total Return convention as of `2025-12-31`
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
