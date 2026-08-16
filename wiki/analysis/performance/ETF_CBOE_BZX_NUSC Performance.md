---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:NUSC
ticker: NUSC
exchange: Cboe BZX
fund: Nuveen ESG Small-Cap ETF
tracked_index: Nuveen ESG USA Small-Cap Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-06-30
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-06-26
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/NUSC
  - geography/United-States
---

# NUSC Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

NUSC เป็น passive/index-tracking U.S. small-cap ESG equity ETF ที่ติดตาม
Nuveen ESG USA Small-Cap Index. กองทุนเริ่มเมื่อ 13 ธ.ค. 2016 จึงยังมีประวัติ
ไม่ครบ 10 ปี ณ 30 มิ.ย. 2026. Official complete calendar-year NAV Total Return
2017-2025 compound เป็น `116.65%` หรือ rounded-input CAGR `8.97%`, เทียบกับ
S&P 500 TR `255.78%` / `15.14%`. ช่วง 2021-2025 NUSC ทำ CAGR `5.51%` เทียบกับ
S&P 500 `14.43%`; current NAV TR YTD ล่าสุดคือ `+16.76%` ณ 30 มิ.ย. 2026.

## Performance check

- `entity_key: Cboe BZX:NUSC`; primary exchange: Cboe BZX Exchange
- Classification: supported passive/index-tracking U.S. small-cap ESG equity ETF
- Inception: 13 ธ.ค. 2016; total expense ratio `0.31%`; distribution frequency: annually
- Metric: `NAV Total Return` รวม reinvested distributions และ fund expenses; currency USD
- Tracked index (issuer benchmark): `Nuveen ESG USA Small-Cap Index`; index provider MSCI
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของกองทุน)
- 10-year NAV TR: `not applicable (<10y history)`; inception-year 2016 เป็น partial period และไม่ถูกนำไปคำนวณ complete-year CAGR
- 2017-2025 calendar NAV TR: cumulative `116.65%`; rounded-input CAGR `8.97%`
- 2021-2025 calendar NAV TR: cumulative `30.77%`; rounded-input CAGR `5.51%`
- Issuer index 2017-2025: cumulative `123.26%`; rounded-input CAGR `9.33%`; 2021-2025 CAGR `5.79%`
- Current NAV TR YTD: `+16.76%` และ issuer-index YTD `+16.94%`, ทั้งคู่ as of 30 มิ.ย. 2026
- Coverage/source note: official Nuveen factsheet ให้ calendar rows 2017-2025 และ current YTD ถึง 30 มิ.ย. 2026; S&P annual rows ใช้ cached USD Total Return convention as of 31 ธ.ค. 2025. ไม่ใช้ proxy หรือ relabel partial 2016 เป็น full year

| Year | NUSC NAV TR | Nuveen ESG USA Small-Cap Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2017 | 16.62% | 17.13% | 21.83% |
| 2018 | -9.28% | -8.88% | -4.38% |
| 2019 | 26.82% | 27.37% | 31.49% |
| 2020 | 23.48% | 23.97% | 18.40% |
| 2021 | 17.83% | 18.26% | 28.71% |
| 2022 | -17.68% | -17.55% | -18.11% |
| 2023 | 15.50% | 15.80% | 26.29% |
| 2024 | 8.48% | 8.79% | 25.02% |
| 2025 | 7.60% | 7.85% | 17.88% |

## Up years / Down years

- Up years / Down years: `7 / 2` across complete calendar years 2017-2025
- Best: 2019, `+26.82%`; least positive: 2025, `+7.60%`
- Worst: 2022, `-17.68%`; least bad down year: 2018, `-9.28%`
- 2017-2025 CAGR: `8.97%`; 2021-2025 CAGR: `5.51%`
- Current YTD: official NAV TR `+16.76%` versus issuer index `+16.94%`, a `-0.18 pp` gap on the same 30 มิ.ย. 2026 as-of date. Current S&P YTD is not used because the cached common-benchmark window ends 2025-12-31.
- Latest official quote snapshot: market price `US$51.56` and NAV `US$51.67` as of 26 มิ.ย. 2026; quote data is not mixed into the NAV Total Return ranking.

## Risk read-through

NUSC มี small-cap, ESG-screen, equity-market และ tracking-error risk. SEC summary
prospectus ระบุ highest quarterly return `+29.98%` ในไตรมาสสิ้นสุด 31 ธ.ค. 2020
และ lowest `-30.76%` ในไตรมาสสิ้นสุด 31 มี.ค. 2020. Current YTD NAV ต่ำกว่า
issuer index `0.18 pp`, สอดคล้องกับผลกระทบจาก fund expenses และ implementation
ของกองทุน แต่ไม่ใช่ attribution แบบ causal. Official daily NAV history เพียงพอ
สำหรับคำนวณ maximum drawdown และ recovery ยังไม่พบใน reviewed capture จึงเขียน
เป็น `ไม่พบข้อมูลที่ยืนยันได้` และไม่สร้างตัวเลข proxy.

## Sources

- [Nuveen official NUSC factsheet](https://documents.nuveen.com/Documents/Nuveen/Viewer.aspx?uniqueId=8238272c-9326-4c32-93cb-40d80e4fc4a9) — identity, passive approach, Cboe listing, fee, official NAV/index calendar rows, current YTD and risk context; as of 30 มิ.ย. 2026
- [Nuveen official NUSC product page](https://www.nuveen.com/en-us/exchange-traded-funds/nusc-nuveen-esg-small-cap-etf) — fund identity, exchange, fee, inception, NAV/price snapshot and product methodology; product-page performance table rendered no records in the reviewed capture, so numeric performance uses the official factsheet
- [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1635073/000119312526080215/d91437d497k.htm) — Cboe BZX listing, passive objective, fees, index strategy and corroborating 2017-2025 annual returns / best-worst quarters
- [MSCI Nuveen ESG USA Small-Cap Index](https://www.msci.com/indexes/index/711741/nuveen-esg-usa-small-cap-index) — issuer benchmark identity
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); cached reference as of 31 ธ.ค. 2025
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
