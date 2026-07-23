---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IJPU
ticker: IHRMF
exchange: LSE
fund: iShares MSCI Japan UCITS ETF USD (Dist)
tracked_index: MSCI Japan Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-22
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IHRMF
  - geography/Japan
---

# IHRMF Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

IHRMF เป็น input OTC alias ของ iShares MSCI Japan UCITS ETF USD (Dist); issuer ระบุ canonical London Stock Exchange USD ticker `IJPU`, ISIN `IE00B02KXH56`. กองทุนเป็น physical/replicated passive equity ETF ที่ track MSCI Japan Index (Net). Official iShares page ณ 2026-06-30 ยืนยัน rolling 10-year NAV Total Return CAGR `9.36%` สำหรับ 2016-06-30 ถึง 2026-06-30 หรือ `10.00` elapsed years. Raw NAV endpoints ไม่ได้เปิดเผย; normalized TR start `100.00` และ end ประมาณ `244.67` เป็นค่าคำนวณจาก CAGR ที่ issuer ปัดเศษ. Official calendar NAV rows 2016-2025 และ benchmark rows เปิดเผยครบ; current NAV TR YTD คือ `15.45%` ณ 2026-07-22.

## Performance check

- entity_key: LSE:IJPU
- Input alias: IHRMF; official issuer listing table confirms London Stock Exchange `IJPU` in USD for ISIN `IE00B02KXH56`; no provider slug or guessed exchange is used.
- Inception: 2004-10-01
- Metric: NAV Total Return with gross income reinvested where applicable; NAV performance is separate from market-price return
- Tracked index: MSCI Japan Index (Net)
- Structure: physical, replicated, passive/index-tracking equity ETF; distributing semi-annually; TER `0.12%`
- 10-year NAV TR coverage: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR CAGR: `9.36%` (official issuer annualised return)
- Normalized NAV TR: start `100.00`; end `244.67` (calculated as `100 × (1 + 9.36%)^10`; raw endpoints not disclosed)
- Coverage/source note: official calendar rows are 2016-2025. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed.

| Year | IJPU NAV TR | MSCI Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 1.8% | 2.4% | 11.96% |
| 2017 | 23.3% | 24.0% | 21.83% |
| 2018 | -13.4% | -12.9% | -4.38% |
| 2019 | 19.0% | 19.6% | 31.49% |
| 2020 | 13.8% | 14.5% | 18.40% |
| 2021 | 1.1% | 1.7% | 28.71% |
| 2022 | -17.1% | -16.6% | -18.11% |
| 2023 | 19.7% | 20.3% | 26.29% |
| 2024 | 8.2% | 8.3% | 25.02% |
| 2025 | 24.5% | 24.6% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` over complete calendar years 2016-2025
- Best complete calendar year: 2017, `23.3%`
- Least positive complete calendar year: 2021, `1.1%`
- Worst complete calendar year: 2022, `-17.1%`
- Least bad down year: 2018, `-13.4%`
- Calendar 2016-2025 rows compound to approximately `98.94%` / CAGR `7.12%` using the issuer's displayed one-decimal rows
- Common 2021-2025 rows compound to approximately `35.14%` / CAGR `6.21%`; S&P 500 common-window CAGR is `14.43%`, so IHRMF trails by approximately `8.22 pp`
- Current NAV TR YTD: `15.45%` as of 2026-07-22; NAV `US$24.18` as of 2026-07-22

## Risk read-through

IHRMF มี single-country Japan exposure และ sensitivity ต่อ sector, valuation และ JPY/USD. Official holdings มี `168` ตัว ณ 2026-07-14; 3-year standard deviation `15.00%` ณ 2026-06-30; 3-year beta `0.994`; trailing 12-month distribution yield `1.51%` ณ 2026-07-14. Daily NAV history สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้` ใน lean capture.

## Sources

- [Official iShares IJPU product and performance page](https://www.ishares.com/uk/professional/en/products/251866/ijpn?siteEntryPassthrough=true)
- [Official iShares IJPU factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/ijpn-ishares-msci-japan-ucits-etf-usd-dist-fund-fact-sheet-en-gb.pdf)
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
