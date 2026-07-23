---
type: etf-performance
instrument_type: ETF
entity_key: LSE:CJPU
ticker: IMSCF
exchange: LSE
fund: iShares MSCI Japan UCITS ETF
tracked_index: MSCI Japan Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IMSCF
  - geography/Japan
---

# IMSCF Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

IMSCF เป็น input OTC alias ของ iShares MSCI Japan UCITS ETF; official listing ระบุ canonical London Stock Exchange USD ticker `CJPU`, ISIN `IE00B53QDK08`. กองทุนเป็น physical/replicated passive equity ETF ที่ track MSCI Japan Index (Net). Official iShares page ณ 2026-06-30 ยืนยัน rolling 10-year NAV Total Return CAGR `9.46%` สำหรับ 2016-06-30 ถึง 2026-06-30 หรือ `10.00` elapsed years. Raw NAV endpoints ไม่ได้เปิดเผย; normalized TR start `100.00` และ end ประมาณ `246.92` เป็นค่าคำนวณจาก CAGR ที่ issuer ปัดเศษ. Official calendar NAV rows 2016-2025 และ benchmark rows เปิดเผยครบ; current NAV TR YTD คือ `12.11%` ณ 2026-07-17.

## Performance check

- entity_key: LSE:CJPU
- Input alias: IMSCF; official issuer listing table confirms London Stock Exchange `CJPU` in USD for ISIN `IE00B53QDK08`; no provider slug or guessed exchange is used.
- Inception: 2010-01-11
- Metric: NAV Total Return with gross income reinvested where applicable; NAV performance is separate from market-price return
- Tracked index: MSCI Japan Index (Net)
- Structure: physical, replicated, passive/index-tracking equity ETF; accumulating; TER `0.12%`
- 10-year NAV TR coverage: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR CAGR: `9.46%` (official issuer annualised return)
- Normalized NAV TR: start `100.00`; end `246.92` (calculated as `100 × (1 + 9.46%)^10`; raw endpoints not disclosed)
- Coverage/source note: official calendar rows are 2016-2025. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed.

| Year | CJPU NAV TR | MSCI Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 1.9% | 2.4% | 11.96% |
| 2017 | 23.4% | 24.0% | 21.83% |
| 2018 | -13.3% | -12.9% | -4.38% |
| 2019 | 19.1% | 19.6% | 31.49% |
| 2020 | 14.0% | 14.5% | 18.40% |
| 2021 | 1.2% | 1.7% | 28.71% |
| 2022 | -17.0% | -16.6% | -18.11% |
| 2023 | 19.8% | 20.3% | 26.29% |
| 2024 | 8.2% | 8.3% | 25.02% |
| 2025 | 24.5% | 24.6% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` over complete calendar years 2016-2025
- Best complete calendar year: 2017, `23.4%`
- Least positive complete calendar year: 2021, `1.2%`
- Worst complete calendar year: 2022, `-17.0%`
- Least bad down year: 2018, `-13.3%`
- Calendar 2016-2025 rows compound to approximately `100.65%` / CAGR `7.21%` using the issuer's displayed one-decimal rows
- Common 2021-2025 rows compound to approximately `35.55%` / CAGR `6.27%`; S&P 500 common-window CAGR is `14.43%`, so IMSCF trails by approximately `8.16 pp`
- Current NAV TR YTD: `12.11%` as of 2026-07-17; NAV `US$277.43` as of 2026-07-20

## Risk read-through

IMSCF มี single-country Japan exposure และ sensitivity ต่อ sector, valuation และ JPY/USD. Official holdings มี `168` ตัว ณ 2026-07-17; 3-year standard deviation `15.00%` ณ 2026-06-30; 3-year beta `0.994`. Daily NAV history สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้` ใน lean capture.

## Sources

- [Official iShares CJPU product and performance page](https://www.ishares.com/uk/professional/en/products/253732/ishares-msci-japan-ucits-etf?siteEntryPassthrough=true&switchLocale=y)
- [Official iShares CJPU factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/csjp-ishares-msci-japan-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y)
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
