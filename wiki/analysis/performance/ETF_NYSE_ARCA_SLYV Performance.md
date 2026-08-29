---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:SLYV
ticker: SLYV
exchange: NYSE Arca
fund: State Street SPDR S&P 600 Small Cap Value ETF
tracked_index: S&P SmallCap 600 Value Index
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2026-08-27
standardized_performance_as_of: 2026-07-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
secondary_current_ytd_as_of: 2026-08-27
price_nav_as_of: 2026-08-27
fund_facts_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: official State Street NAV total return; secondary dividend-reinvested proxy for current cross-checks
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SLYV
  - geography/United-States
---

# SLYV Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

SLYV เป็น passive/index-tracking U.S. small-cap value ETF ที่ติดตาม `S&P
SmallCap 600 Value Index` ด้วย sampling. Latest official State Street
standardized NAV TR ณ 31 ก.ค. 2026 ให้ YTD `20.17%` และ rolling 10-year
`10.06%`; current fund snapshot ณ 27 ส.ค. ให้ NAV `US$110.06`, AUM
`US$5,046.52M` และ 461 holdings. Secondary dividend-reinvested total return
YTD ล่าสุดอยู่ที่ `22.15%` ถึง 27 ส.ค. แต่ไม่ผสมกับ official July window.
ใน complete calendar window 2016-2025 มี 8 ปีบวก / 2 ปีลบ; cumulative NAV
Total Return คือ `147.73%` หรือ rounded-input CAGR `9.50%`, เทียบ S&P 500 TR
`298.33%` / `14.82%`.

## Performance check

- `entity_key: NYSE Arca:SLYV`
- Classification: supported passive/index-tracking equity ETF using a
  representative-sampling approach; exchange NYSE Arca
- Inception: 25 ก.ย. 2000; expense ratio `0.15%`; quarterly distribution
- Metric: `NAV Total Return` บนฐาน USD รวม reinvested dividends และ capital
  gains; SSGA ระบุว่าเป็นผลตอบแทน net of fees และ market-price return แยกต่างหาก
- Tracked index (issuer benchmark): `S&P SmallCap 600 Value Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ SLYV)
- Official State Street standardized NAV TR as of `2026-07-31`: YTD `20.17%`,
  1Y `36.94%`, 3Y annualized `12.35%`, 5Y `7.98%`, 10Y annualized `10.06%`
  and since inception `10.77%`; raw rolling endpoints are not disclosed, so
  the issuer average-annual field is not recomputed from annual rows.
- Official current fund snapshot as of `2026-08-27`: NAV `US$110.06`, market
  close `US$110.07`, bid/ask midpoint `US$110.09`, AUM `US$5,046.52M` and 461
  holdings. Fund characteristics are P/B `1.55`, FY1 P/E `12.67`, weighted
  average market cap `US$4,111.42M` and estimated 3-5 year EPS growth `16.28%`.
- Current secondary dividend-reinvested YTD cross-check is `22.15%` through
  `2026-08-27`; YTDReturn reports `22.10%` through 2026-08-26. These later
  fields are context only and are not substitutes for official July NAV TR.

### Official standardized performance

| Window | SLYV NAV TR | SLYV market value | S&P SmallCap 600 Value Index |
|---|---:|---:|---:|
| 1 month | -0.56% | -0.59% | -0.55% |
| QTD | -0.56% | -0.59% | -0.55% |
| YTD | 20.17% | 20.17% | 20.27% |
| 1 year | 36.94% | 36.98% | 37.16% |
| 3 years annualized | 12.35% | 12.34% | 12.50% |
| 5 years annualized | 7.98% | 7.99% | 8.14% |
| 10 years annualized | 10.06% | 10.05% | 10.19% |
| Since inception annualized | 10.77% | 10.78% | 10.47% |

Official State Street table as of 2026-07-31; returns assume reinvestment of
dividends/capital gains and are net of fund expenses. The linked index is the
issuer benchmark; S&P 500 TR remains only a common reference.

| Year | SLYV NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.14% | 11.96% |
| 2017 | 11.45% | 21.83% |
| 2018 | -12.69% | -4.38% |
| 2019 | 24.31% | 31.49% |
| 2020 | 2.60% | 18.40% |
| 2021 | 30.66% | 28.71% |
| 2022 | -11.13% | -18.11% |
| 2023 | 14.71% | 26.29% |
| 2024 | 7.28%* | 25.02% |
| 2025 | 6.52%* | 17.88% |

`*` ปี 2024–2025 ใช้ secondary standardized total-return rows จาก ETFReplay
และมี TotalRealReturns ช่วย corroborate; official SEC prospectus rows ที่ใช้ใน
ตารางครอบคลุมถึง 2023.

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2016, `+31.14%`; least positive: 2025, `+6.52%`
- Worst: 2018, `-12.69%`; least bad down year: 2022, `-11.13%`
- 2016-2025 cumulative/CAGR: SLYV `147.73%` / `9.50%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: SLYV `52.21%` / `8.77%`; S&P 500 TR
  `96.17%` / `14.43%`
- 2025 relative to S&P 500 TR: `6.52% - 17.88% = -11.36 pp`
- Latest official SLYV NAV TR YTD: `+20.17%` ณ 31 ก.ค. 2026; later secondary
  dividend-reinvested YTD cross-check: `+22.15%` through 27 ส.ค. 2026

## Risk read-through

SLYV มีหุ้น `461` รายการ ณ 27 ส.ค. 2026 และ exposure หลักอยู่ใน Financials
`21.66%`, Consumer Discretionary `15.63%`, Industrials `14.54%`, Information
Technology `10.77%`, Energy `7.17%` และ Real Estate `6.95%`. Small-cap/value
factor, sector rotation, liquidity และ valuation risk จึงมีความสำคัญ; SSGA
ระบุว่าหุ้น value อาจ underperform และ small-cap companies มีความผันผวน/สภาพ
คล่องสูงกว่า. Secondary total-return history ระบุ current drawdown `-1.92%`
จาก high ณ 14 ส.ค. 2026 แต่ไม่ใช่ official NAV drawdown. Official daily NAV
history ที่เพียงพอสำหรับ maximum drawdown และ recovery ยังไม่ถูกยืนยัน จึงไม่ใช้
ตัวเลข proxy ปนกับ NAV TR ranking.

## Sources

- [Official State Street SLYV product page](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-600-small-cap-value-etf-slyv) — identity, current NAV/AUM/price/holdings/characteristics, risk fields and July standardized performance
- [Official State Street SLYV fact sheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-slyv.pdf) — return basis, benchmark, inception, expense ratio, exchange and methodology context
- [SEC-hosted SLYV summary prospectus](https://www.sec.gov/Archives/edgar/data/1064642/000119312524242957/R25.htm) — strategy, risk and official annual rows through 2023
- [ETFReplay SLYV history](https://www.etfreplay.com/etf/slyv) — secondary 2024–2025 complete-year rows
- [TotalRealReturns SLYV history](https://totalrealreturns.com/n/SLYV) — secondary corroboration for annual total returns
- [YTDReturn SLYV](https://www.ytdreturn.com/slyv/) — secondary dividend-reinvested current YTD cross-check
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
