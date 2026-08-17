---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FDD
ticker: FDD
exchange: NYSE Arca
fund: First Trust STOXX European Select Dividend Index Fund
tracked_index: STOXX Europe Select Dividend 30 Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-07-23
fund_facts_as_of: 2026-07-23
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FDD
  - geography/Europe
---

# FDD Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

FDD เป็น passive Europe high-dividend equity ETF ที่ track `STOXX Europe Select
Dividend 30 Index`. Official issuer performance list ณ 2026-07-31 รายงาน
10-year NAV Total Return annualised `10.86%` และ current NAV TR YTD `+18.51%`.
จาก official calendar NAV rows 2016-2025 แบบ rounded inputs FDD ให้ cumulative
`139.09%` และ CAGR `9.11%`; ช่วงร่วม 2021-2025 ให้ cumulative `79.20%` และ
CAGR `12.37%`, ต่ำกว่า S&P 500 TR common reference ที่ `14.43%`.

## Performance check

- `entity_key: NYSE Arca:FDD`; inception `2007-08-27`; exchange `NYSE Arca`; CUSIP `33735T109`; ISIN `US33735T1097`.
- Metric: `NAV Total Return` in USD; distributions are reinvested and fund expenses are reflected in NAV performance.
- Tracked index: `STOXX Europe Select Dividend 30 Index`; the index selects 30 dividend-paying stocks from STOXX Europe 600 across European countries using dividend-growth, payout and yield screens.
- Expense ratio `0.56%` as of 2026-02-02; the issuer states an expense cap of `0.60%` through at least 2027-01-31. An older saved page showed `0.58%`; the current issuer disclosure is used and the conflict is retained in the source batch.
- Current issuer fund data as of 2026-07-23: NAV `US$19.25`, market price `US$19.25`, total net assets `US$853.05M`, and 30 holdings.
- Official issuer performance list as of 2026-07-31: NAV TR `3M 8.27%`, `YTD 18.51%`, `1Y 38.57%`, `3Y 26.57%`, `5Y 13.10%`, `10Y 10.86%`, and since inception `2.84%`.
- Annual NAV TR rows are official issuer rows captured through 2025; S&P 500 TR is a common reference only and is not FDD's tracked index or evidence of manager skill.

| Year | FDD NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 2.58% | 11.96% |
| 2017 | 19.04% | 21.83% |
| 2018 | -8.83% | -4.38% |
| 2019 | 23.09% | 31.49% |
| 2020 | -2.64% | 18.40% |
| 2021 | 15.07% | 28.71% |
| 2022 | -15.67% | -18.11% |
| 2023 | 13.42% | 26.29% |
| 2024 | 0.60% | 25.02% |
| 2025 | 61.85% | 17.88% |

## Up years / Down years

- Complete fund rows 2016-2025: `7 / 3` up/down years; rounded-input cumulative `139.09%`; rounded-input CAGR `9.11%`; population annual-return standard deviation `20.71%`.
- Best: 2025, `+61.85%`; worst: 2022, `-15.67%`; average positive year `19.38%`.
- Common 2021-2025 window: rounded-input cumulative `79.20%` / CAGR `12.37%`; cached S&P 500 TR cumulative `96.17%` / CAGR `14.43%`; FDD trails by approximately `-2.05 pp` CAGR. This is a common-reference comparison, not alpha.
- Current YTD: FDD NAV TR `+18.51%` as of 2026-07-31. A same-date S&P 500 current-YTD pairing was not used.

## Risk read-through

FDD มี concentration สูงใน Financials `57.23%`, Consumer Discretionary `15.31%`
และ Industrials `9.58%` ณ 2026-06-17. Country exposure กระจุกใน Netherlands
`22.79%`, France `21.76%` และ UK `20.21%`; จึงมี country, EUR/GBP-USD FX,
dividend-factor, rate และ sector-concentration risk. Top holdings ณ 2026-07-23
รวม LGEN `6.10%`, Taylor Wimpey `4.51%`, Aker BP `4.40%`, B&M `4.38%` และ
Teleperformance `4.36%`. Issuer 30-day SEC yield คือ `4.33%` และ 12-month
distribution rate `5.45%` ณ 2026-06-30. Official daily NAV maximum drawdown
และ recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [First Trust FDD product and performance page](https://www.ftportfolios.com/retail/etf/etfsummary.aspx?Ticker=FDD) — fund facts, NAV/price, holdings, exposures, distribution fields and product methodology.
- [First Trust ETF performance list](https://www.ftportfolios.com/retail/etf/etflist.aspx?DisplayType=PerformanceNav&Type=Dividend) — current standardized NAV performance as of 2026-07-31.
- [First Trust FDD prospectus](https://www.ftportfolios.com/Funds/ETF/Prospectus/FAN) — annual NAV TR history and return definitions.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
