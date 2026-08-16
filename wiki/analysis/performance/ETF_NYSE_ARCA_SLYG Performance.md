---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:SLYG
ticker: SLYG
exchange: NYSE Arca
fund: State Street SPDR S&P 600 Small Cap Growth ETF
tracked_index: S&P SmallCap 600 Growth Index
benchmark: S&P 500 Total Return
updated: 2026-08-16
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-07-17
fund_facts_as_of: 2026-07-20
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SLYG
  - geography/United-States
---

# SLYG Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

SLYG เป็น passive/index-tracking U.S. small-cap growth ETF ที่ติดตาม `S&P
SmallCap 600 Growth Index`. ใน complete calendar window 2016-2025 ตาราง
secondary total-return proxy ให้ 8 ปีบวก / 2 ปีลบ, cumulative `152.01%` และ
rounded-input CAGR `9.68%`, เทียบ S&P 500 TR `298.33%` / `14.82%`. ปีดีที่สุดคือ
2021 ที่ `+22.42%*` และแย่ที่สุดคือ 2022 ที่ `-21.26%*`; official NAV TR YTD
ล่าสุดที่ยืนยันได้คือ `+26.92%` ณ 30 มิ.ย. 2026.

## Performance check

- `entity_key: NYSE Arca:SLYG`
- Classification: supported passive/index-tracking equity ETF using index
  sampling; exchange NYSE Arca
- Inception: 25 ก.ย. 2000; expense ratio `0.15%`; quarterly distribution
- Metric: `NAV Total Return` บนฐาน USD รวม reinvested dividends และ capital
  gains; performance net of fund expenses ตาม issuer disclosure
- Tracked index (issuer benchmark): `S&P SmallCap 600 Growth Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ SLYG)
- Official rolling 10-year NAV TR: issuer average annual `11.89%` ณ 30 มิ.ย.
  2026; raw rolling endpoints ไม่ได้เปิดเผย จึงไม่คำนวณ endpoint CAGR ซ้ำ
- Current official NAV TR YTD: `26.92%` ณ 30 มิ.ย. 2026; latest displayed NAV
  `US$115.32` ณ 17 ก.ค. 2026 เป็น quote context ไม่ใช่ return input
- Coverage/source note: issuer annual rows ไม่ได้เปิดเผยใน text extract ที่
  ตรวจสอบ; annual rows ด้านล่างจึงใช้ ETFreplay secondary dividend-reinvested
  proxy และทำเครื่องหมาย `*` ทุกปี. Partial 2026 YTD แยกออกจาก ranking.

| Year | SLYG NAV TR* | S&P 500 TR |
|---|---:|---:|
| 2016 | 22.16%* | 11.96% |
| 2017 | 14.53%* | 21.83% |
| 2018 | -4.19%* | -4.38% |
| 2019 | 20.98%* | 31.49% |
| 2020 | 19.48%* | 18.40% |
| 2021 | 22.42%* | 28.71% |
| 2022 | -21.26%* | -18.11% |
| 2023 | 17.27%* | 26.29% |
| 2024 | 9.38%* | 25.02% |
| 2025 | 5.19%* | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025; `*` คือ secondary proxy
- Best: 2021, `+22.42%*`
- Least positive: 2025, `+5.19%*`
- Worst: 2022, `-21.26%*`
- Least bad down year: 2018, `-4.19%*`
- 2016-2025 cumulative/CAGR: SLYG `152.01%` / `9.68%*`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: SLYG `30.06%` / `5.40%*`; S&P 500 TR
  `96.17%` / `14.43%`
- Current SLYG NAV TR YTD: `+26.92%` ณ 30 มิ.ย. 2026

## Risk read-through

Issuer rolling 10-year NAV TR เฉลี่ยต่อปีอยู่ที่ `11.89%` ณ 30 มิ.ย. 2026 แต่
ตัวเลขนี้ไม่มี raw endpoints ให้คำนวณซ้ำ. SLYG มี small-cap/growth/cyclicality
และ liquidity sensitivity; issuer ระบุ 350 holdings ณ 17 ก.ค. 2026. ETFreplay
รายงาน secondary annualized daily-return volatility `17.9%` ณ 20 ก.ค. 2026
ซึ่งใช้เป็น context เท่านั้น ไม่ใช่ official NAV risk statistic. ไม่พบข้อมูลที่
ยืนยันได้สำหรับ official daily NAV maximum drawdown และ recovery จึงไม่ใส่
ตัวเลข proxy ปนกับ NAV TR ranking. Expense ratio `0.15%` เป็นแรง drag ต่อ
tracking และผลตอบแทนสุทธิ.

## Sources

- [Official State Street SLYG product page](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-600-small-cap-growth-etf-slyg) — identity, exchange, inception, benchmark, expense ratio, official NAV TR/YTD and rolling fields
- [Official SLYG fact sheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-slyg.pdf) — passive/index approach, return basis, fund facts and risk disclosures as of 30 Jun 2026
- [Secondary ETFreplay SLYG history](https://www.etfreplay.com/etf/slyg) — 2016-2025 dividend-reinvested annual proxy and secondary volatility, data as of 20 Jul 2026
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-16]] | [[ETF Performance Index]]
