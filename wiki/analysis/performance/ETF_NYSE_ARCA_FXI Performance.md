---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FXI
ticker: FXI
exchange: NYSE Arca
fund: iShares China Large-Cap ETF
tracked_index: FTSE China 50 Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-29
annual_performance_as_of: 2025-12-31
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-26
nav_as_of: 2026-08-26
market_price_as_of: 2026-08-26
distribution_as_of: 2026-06-15
fund_facts_as_of: 2026-08-26
risk_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FXI
  - geography/China
  - style/large-cap
---

# FXI Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

FXI ให้ official NAV Total Return ติดลบใน 3 จาก 5 ปีช่วง 2021-2025; สะสม
`-8.08%` หรือ CAGR `-1.67%` เทียบกับ S&P 500 TR ที่ `+96.17%` หรือ `14.43%`.
ปีดีที่สุดคือ 2024 ที่ `+30.10%` และแย่ที่สุดคือ 2021 ที่ `-21.04%`. 10-year
NAV TR CAGR ของ iShares อยู่ที่ `1.75%` ณ 30 มิ.ย. 2026; current YTD ล่าสุดอยู่ที่
`-6.68%` ณ 26 ส.ค. 2026 และ current NAV อยู่ที่ `USD 35.63` ณ วันเดียวกัน.

## Performance check

- `entity_key: NYSE Arca:FXI`
- Fund: iShares China Large-Cap ETF; inception `5 ต.ค. 2004`; expense ratio `0.73%`
- Metric: `NAV Total Return` รวม distributions reinvested และหัก fund expenses
- Tracked index (issuer benchmark): `FTSE China 50 Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ FXI)
- 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `1.75%` ณ 30 มิ.ย. 2026; issuer cumulative return `18.94%`.
  Normalized endpoints คือ `Start TR value: 100.00` และ `End TR value: 118.94`,
  `Years: 10.00`; raw daily NAV TR endpoints ไม่ได้เปิดเผย
- Formula: `(118.94 / 100.00)^(1 / 10.00) - 1 = 1.75%`; endpoints เป็นการ normalize
  จาก cumulative return ที่ issuer รายงาน ไม่ใช่ raw daily NAV TR series
- Coverage/source note: annual rows เป็น official complete-calendar-year NAV TR
  2021-2025; S&P 500 rows ใช้ cached USD Total Return convention ณ 31 ธ.ค. 2025

| ปี | FXI NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | -21.04% | 28.71% |
| 2022 | -20.40% | -18.11% |
| 2023 | -12.87% | 26.29% |
| 2024 | 30.10% | 25.02% |
| 2025 | 29.01% | 17.88% |

FXI 2021-2025 cumulative/CAGR คือ `-8.08%` / `-1.67%`; S&P 500 TR คือ
`96.17%` / `14.43%`. FXI beat the common benchmark ในปี 2024-2025 แต่ lagged
ในปี 2021-2023.

## Up years / Down years

- Up years / Down years: `2 / 3` ใน 2021-2025
- Best: 2024, `+30.10%`
- Least positive: 2025, `+29.01%`
- Worst: 2021, `-21.04%`
- Least bad down year: 2023, `-12.87%`
- Current YTD: `-6.68%` NAV ณ 26 ส.ค. 2026; latest NAV คือ `$35.63` และ closing
  market price `$35.55` โดย issuer รายงาน premium/discount `-0.23%`

## Risk read-through

10-year NAV TR CAGR เพียง `1.75%` สะท้อนว่า long-term outcome ยังต่ำเมื่อเทียบกับ
ความเสี่ยงของ single-country equity. 3-year standard deviation อยู่ที่ `22.02%`
ณ 31 ก.ค. 2026; กองมี 50 holdings ณ 26 ส.ค. โดย sector ใหญ่คือ Financials
`35.32%`, Consumer Discretionary `26.13%` และ Communication `15.33%`. Equity beta
อยู่ที่ `0.26` ณ 31 ก.ค. 2026. FXI จึงเป็น
China large-cap exposure ที่ไวต่อ policy, country risk, FX และ valuation มากกว่า
กอง global ที่กระจายประเทศ. Expense ratio คือ `0.73%`; distribution frequency คือ
semi-annual และ trailing yield `1.86%` ณ 31 ก.ค. 2026.

Secondary dividend-reinvested total-return proxy ระบุ maximum drawdown `-72.68%`
เมื่อ 27 ต.ค. 2008 และใช้ `3,094` trading sessions เพื่อ recover ถึง ก.พ. 2021;
last dated drawdown snapshot ที่แหล่งเดียวกันรายงานคือ `-29.28%` ณ 8 ก.ค. 2026. ตัวเลขนี้เป็น
secondary adjusted-total-return proxy ไม่ใช่ official NAV drawdown/recovery series.

## Data notes

- Latest distribution ที่ตรวจสอบได้คือ `$0.263439` ต่อหุ้น, ex-date 15 มิ.ย. 2026,
  payable 18 มิ.ย. 2026; NAV Total Return รวมเงินปันผลแล้ว จึงไม่ควรนับซ้ำ
- Current FXI YTD (`-6.68%`) ใช้ US BlackRock snapshot ณ 26 ส.ค. 2026 ซึ่งใหม่กว่า
  regional AE snapshot ที่รายงาน `-6.85%` ณ 25 ส.ค. 2026; เก็บความต่างตาม as-of/site
  ไว้เป็น source conflict ที่ยังไม่ควร reconcile ด้วย arithmetic.
- Official daily NAV TR index levels สำหรับคำนวณ drawdown/recovery โดยตรง:
  `ไม่พบข้อมูลที่ยืนยันได้`

## Sources

- [BlackRock FXI product page](https://www.blackrock.com/us/individual/products/239536/ishares-china-large-cap-etf) — identity, exchange, benchmark, inception, annual NAV TR, standardized performance, distributions and fees
- [BlackRock FXI current fund data](https://www.blackrock.com/us/individual/products/overview-v3-ishares-fund-data?portfolioId=239536&seoSlug=ishares-china-largecap-etf) — current NAV/price, YTD NAV TR, assets, holdings, sector mix, standard deviation, beta and premium/discount
- [Official FXI factsheet](https://www.blackrock.com/us/individual/literature/fact-sheet/fxi-ishares-china-large-cap-etf-fund-fact-sheet-en-us.pdf) — official annual NAV TR, return definition, standardized performance and fund facts
- [iShares FXI summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-china-large-cap-etf-7-31.pdf) — passive/index-tracking objective and risk disclosures
- [Total Real Returns FXI](https://totalrealreturns.com/n/FXI) — secondary dividend-reinvested history, drawdown and recovery proxy
- [BlackRock AE FXI page](https://www.blackrock.com/ae/intermediaries/products/239536/ishares-china-largecap-etf) — regional snapshot retained for as-of reconciliation; it displayed NAV TR YTD `-6.85%` as of 25 ส.ค. 2026
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index identity, methodology and total-return ticker; annual rows reuse cached skill convention
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
