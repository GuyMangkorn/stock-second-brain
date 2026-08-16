---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VIOV
ticker: VIOV
exchange: NYSE Arca
fund: Vanguard S&P Small-Cap 600 Value ETF
tracked_index: S&P SmallCap 600 Value Index
benchmark: S&P 500 Total Return
updated: 2026-08-16
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-20
price_nav_as_of: 2026-07-02
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/VIOV
  - geography/United-States
---

# VIOV Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

VIOV เป็น passive/index-tracking U.S. small-cap value ETF ที่ติดตาม `S&P
SmallCap 600 Value Index` ด้วย full replication. ใน complete calendar window
2016-2025 มี 8 ปีบวก / 2 ปีลบ; cumulative NAV Total Return ที่คำนวณจาก annual
rows คือ `148.69%` หรือ rounded-input CAGR `9.54%`, เทียบ S&P 500 TR
`298.33%` / `14.82%`. ปีดีที่สุดคือ 2021 ที่ `+30.74%` และแย่ที่สุดคือ 2018 ที่
`-12.77%`. Current official NAV TR YTD ที่ยืนยันได้ล่าสุดคือ `+20.27%` ณ
20 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:VIOV`
- Classification: supported passive/index-tracking equity ETF using a
  full-replication approach; exchange NYSE Arca
- Inception: 7 ก.ย. 2010; expense ratio `0.10%`; quarterly distribution
- Metric: `NAV Total Return` บนฐาน USD รวม reinvested dividends และ capital
  gains; figures เป็น pre-tax และ net of expenses ตาม issuer disclosure
- Tracked index (issuer benchmark): `S&P SmallCap 600 Value Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ VIOV)
- Official rolling 10-year NAV TR: average annual `10.72%` และ cumulative
  `176.76%` ณ 30 มิ.ย. 2026; raw rolling endpoints ไม่ได้เปิดเผย จึงไม่คำนวณซ้ำ
- Current official NAV TR YTD: `20.27%` ณ 20 ก.ค. 2026; fact sheet month-end
  snapshot คือ `20.92%` ณ 30 มิ.ย. 2026 และเก็บเป็นคนละ as-of date
- Latest NAV / market price ที่ยืนยันได้: `116.27 / 116.17` ณ 2 ก.ค. 2026

| Year | VIOV NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.07% | 11.96% |
| 2017 | 11.50% | 21.83% |
| 2018 | -12.77% | -4.38% |
| 2019 | 24.40% | 31.49% |
| 2020 | 2.70% | 18.40% |
| 2021 | 30.74% | 28.71% |
| 2022 | -11.19% | -18.11% |
| 2023 | 14.75% | 26.29% |
| 2024 | 7.45% | 25.02% |
| 2025 | 6.66% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2021, `+30.74%`; least positive: 2025, `+6.66%`
- Worst: 2018, `-12.77%`; least bad down year: 2022, `-11.19%`
- 2016-2025 cumulative/CAGR: VIOV `148.69%` / `9.54%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: VIOV `52.70%` / `8.83%`; S&P 500 TR
  `96.17%` / `14.43%`
- 2025 relative to S&P 500 TR: `6.66% - 17.88% = -11.22 pp`

## Risk read-through

VIOV มีหุ้น `462` รายการ, turnover `47.2%` และ standard deviation `19.92%`
ณ 30 มิ.ย. 2026. Exposure เป็น small-cap/value และมีน้ำหนัก sector หลักใน
Financials `21.6%`, Consumer Discretionary `15.9%`, Industrials `13.0%` และ
Information Technology `12.6%`; จึงไวต่อวัฏจักรเศรษฐกิจ style rotation, sector
และ liquidity risk. Vanguard ระบุว่าราคาของ small-cap ETF อาจผันผวนมากกว่า
large-cap ETF. Official daily NAV history ที่เพียงพอสำหรับ maximum drawdown
และ recovery ยังไม่ถูกยืนยัน จึงไม่ใช้ตัวเลข secondary proxy.

## Sources

- [Official Vanguard VIOV product page](https://investor.vanguard.com/investment-products/etfs/profile/viov) — identity, annual NAV rows, rolling/cumulative fields, current NAV and market-price snapshot
- [Official Vanguard VIOV fact sheet](https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3346.pdf) — return basis, benchmark, inception, expense ratio, exchange, holdings and risk snapshot as of 30 Jun 2026
- [Official Vanguard advisor VIOV page](https://advisors.vanguard.com/investments/products/viov/vanguard-sp-small-cap-600-value-etf) — latest verified NAV TR YTD as of 20 Jul 2026
- [SEC-hosted VIOV summary prospectus](https://www.sec.gov/Archives/edgar/data/891190/000168386324009372/f40257d1.htm) — exchange, objective and indexing strategy
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-16]] | [[ETF Performance Index]]
