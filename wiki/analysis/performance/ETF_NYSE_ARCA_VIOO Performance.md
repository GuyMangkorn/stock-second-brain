---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VIOO
ticker: VIOO
exchange: NYSE Arca
fund: Vanguard S&P Small-Cap 600 ETF
tracked_index: S&P SmallCap 600 Index
benchmark: S&P 500 Total Return
updated: 2026-08-16
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-17
price_nav_as_of: not disclosed
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/VIOO
  - geography/United-States
---

# VIOO Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

VIOO เป็น passive/index-tracking U.S. small-cap ETF ที่ติดตาม `S&P SmallCap
600 Index` และมี broad exposure ข้าม growth/value. ใน complete calendar window
2016-2025 มี 8 ปีบวก / 2 ปีลบ; cumulative NAV Total Return ที่คำนวณจาก annual
rows คือ `153.93%` หรือ CAGR `9.77%`, เทียบ S&P 500 TR `298.33%` / `14.82%`.
ปีดีที่สุดคือ 2021 ที่ `+26.67%` และแย่ที่สุดคือ 2022 ที่ `-16.20%`. Current
official NAV TR YTD ที่ยืนยันได้ล่าสุดคือ `+22.03%` ณ 17 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:VIOO`
- Classification: supported passive/index-tracking equity ETF using a
  full-replication approach; exchange NYSE Arca
- Inception: 7 ก.ย. 2010; expense ratio `0.07%`; annual distribution
- Metric: `NAV Total Return` บนฐาน USD รวม reinvested dividends และ capital
  gains; fund expenses สะท้อนอยู่ในผลตอบแทนตาม issuer disclosure
- Tracked index (issuer benchmark): `S&P SmallCap 600 Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ VIOO)
- Official rolling 10-year NAV TR: average annual `11.47%` ณ 30 มิ.ย. 2026;
  raw rolling endpoints ไม่ได้เปิดเผย จึงไม่คำนวณซ้ำเป็น CAGR
- Current official NAV TR YTD: `22.03%` ณ 17 ก.ค. 2026; official 1-year NAV TR
  `37.46%` ณ 30 มิ.ย. 2026
- Latest NAV/market-price quote ใน source extracts ที่ตรวจสอบได้: `ไม่พบข้อมูลที่ยืนยันได้`;
  ไม่มีการใช้ quote ใน calculations

| Year | VIOO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 26.44% | 11.96% |
| 2017 | 13.31% | 21.83% |
| 2018 | -8.57% | -4.38% |
| 2019 | 22.72% | 31.49% |
| 2020 | 11.43% | 18.40% |
| 2021 | 26.67% | 28.71% |
| 2022 | -16.20% | -18.11% |
| 2023 | 16.00% | 26.29% |
| 2024 | 8.62% | 25.02% |
| 2025 | 5.99% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2021, `+26.67%`
- Least positive: 2025, `+5.99%`
- Worst: 2022, `-16.20%`
- Least bad down year: 2018, `-8.57%`
- 2016-2025 cumulative/CAGR: VIOO `153.93%` / `9.77%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: VIOO `41.76%` / `7.23%`; S&P 500 TR
  `96.17%` / `14.43%`
- Current VIOO NAV TR YTD: `+22.03%` ณ 17 ก.ค. 2026

## Risk read-through

VIOO กระจายไปยังหุ้น small-cap สหรัฐฯ `607` รายการ ณ 30 มิ.ย. 2026 และ
มี three-year standard deviation `19.44%` กับ turnover `21.8%` ณ วันเดียวกัน.
Sector mix กระจุกใน Financials `18.4%`, Industrials `17.2%`, Information
Technology `14.0%` และ Consumer Discretionary `13.7%`; จึงยังมี
small-cap, cyclicality, liquidity และ sector-sensitivity แม้จะ diversified
ข้าม growth/value. Vanguard ระบุว่าราคาของ small-cap ETF อาจผันผวนมากกว่า
large-cap ETF. Official daily NAV history ที่เพียงพอสำหรับ maximum drawdown และ
recovery ยังไม่ถูกยืนยัน จึงไม่ใช้ตัวเลข secondary proxy.

## Sources

- [Official Vanguard VIOO product page](https://investor.vanguard.com/investment-products/etfs/profile/vioo) — identity, tracked index, annual NAV rows, benchmark rows, rolling and cumulative return fields
- [Official VIOO fact sheet](https://fund-docs.vanguard.com/F3345.pdf) — return basis, 2016-2025/rolling performance, inception, expense ratio, exchange, holdings and risk snapshot as of 30 Jun 2026
- [Official Vanguard advisor VIOO page](https://advisors.vanguard.com/investments/products/vioo/vanguard-sp-small-cap-600-etf) — latest verified NAV TR YTD as of 17 Jul 2026 and expense ratio
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-16]] | [[ETF Performance Index]]
