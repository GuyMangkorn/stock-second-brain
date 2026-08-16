---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:SCHC
ticker: SCHC
exchange: NYSE Arca
fund: Schwab International Small-Cap Equity ETF
tracked_index: FTSE Developed Small Cap ex US Liquid Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-16
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SCHC
  - geography/International
  - geography/international-ex-US
---

# SCHC Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

SCHC เป็น passive/index-tracking international small-cap ETF ที่ติดตาม FTSE
Developed Small Cap ex US Liquid Index (Net). ใน complete calendar window
2016-2025 มี 8 ปีบวก / 2 ปีลบ; cumulative NAV Total Return อยู่ที่ `108.21%`
หรือ rounded-input CAGR `7.61%`, เทียบ S&P 500 TR `298.33%` / `14.82%`.
ปีดีที่สุดคือ 2025 ที่ `+37.73%` และแย่ที่สุดคือ 2022 ที่ `-21.92%`. Current
official NAV TR YTD คือ `+6.15%` ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:SCHC`
- Classification: supported passive/index-tracking equity ETF; issuer describes
  the fund as passive and the prospectus discloses representative sampling.
- Inception: 14 ม.ค. 2010; expense ratio `0.06%` โดย Schwab ระบุว่า effective
  11 มิ.ย. 2026
- Metric: `NAV Total Return` บนฐาน USD รวมการ reinvest dividends และ
  distributions ตาม issuer; fund expenses สะท้อนอยู่ในผลตอบแทนกองทุน
- Tracked index (issuer benchmark): `FTSE Developed Small Cap ex US Liquid Index
  (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ SCHC)
- Official rolling 10-year NAV TR: average annual `8.23%` ณ 30 มิ.ย. 2026;
  raw rolling endpoints และ cumulative return ไม่ได้เปิดเผย จึงไม่สร้าง
  normalized endpoint
- Current NAV: `US$51.24` ณ 14 ส.ค. 2026; product page แสดง bid/ask midpoint
  `US$51.06` และ premium/discount `0.24%` ณ วันเดียวกัน
- Annual coverage: official complete calendar years 2016-2025 จาก Schwab
  factsheet as of 30 มิ.ย. 2026; current YTD ใช้ Schwab monthly performance
  summary as of 31 ก.ค. 2026

| Year | SCHC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 3.17% | 11.96% |
| 2017 | 29.33% | 21.83% |
| 2018 | -18.65% | -4.38% |
| 2019 | 22.96% | 31.49% |
| 2020 | 10.69% | 18.40% |
| 2021 | 12.14% | 28.71% |
| 2022 | -21.92% | -18.11% |
| 2023 | 14.69% | 26.29% |
| 2024 | 1.90% | 25.02% |
| 2025 | 37.73% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2025, `+37.73%`
- Least positive: 2024, `+1.90%`
- Worst: 2022, `-21.92%`
- Least bad down year: 2018, `-18.65%`
- 2016-2025 cumulative/CAGR: SCHC `108.21%` / `7.61%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: SCHC `40.94%` / `7.10%`; S&P 500 TR
  `96.17%` / `14.43%`
- Current SCHC NAV TR YTD: `+6.15%` ณ 31 ก.ค. 2026

## Risk read-through

SCHC ให้ developed-market small-cap exposure นอกสหรัฐฯ จึงมี small-cap,
country, currency และ liquidity sensitivity สูงกว่ากองทุน developed-market
broad equity. Official product page แสดง holdings `2,202` ณ 13 ส.ค. 2026,
portfolio turnover `25.85%` และ three-year standard deviation `16.57%` ณ
31 ก.ค. 2026. Factsheet ที่ปิด ณ 30 มิ.ย. 2026 รายงาน standard deviation
`16.73%`; ความต่างนี้เป็นคนละ dated snapshot ไม่ใช่ source conflict.

Official rolling 10-year NAV TR average annual return `8.23%` ณ 30 มิ.ย. 2026
ยังไม่มี raw endpoints ให้คำนวณ cumulative แบบ reproducible. Official daily NAV
history ที่เพียงพอสำหรับ maximum drawdown และ recovery ยังไม่ถูกยืนยัน จึงไม่ใช้
ตัวเลข secondary proxy ในหน้านี้.

## Sources

- [Schwab SCHC product page](https://www.schwabassetmanagement.com/products/schc) — identity, objective, current NAV/quote, expense ratio, holdings, turnover and current performance
- [Schwab ETF Investment Performance Summary](https://www.schwabassetmanagement.com/resource/etf-investment-performance-summary) — monthly and quarterly official return snapshots through 31 Jul 2026
- [Official SCHC fact sheet](https://www.schwabassetmanagement.com/resource/schc-fact-sheet) — official 2016-2025 calendar NAV rows, return basis and 3-year risk statistic as of 30 Jun 2026
- [SCHC summary prospectus](https://www.sec.gov/Archives/edgar/data/1454889/000110465926020712/tm266454-8_497k.htm) — index objective, sampling method and risk disclosures
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-16]] | [[ETF Performance Index]]
