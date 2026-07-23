---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:GSJY
ticker: GSJY
exchange: NYSE Arca
fund: Goldman Sachs ActiveBeta Japan Equity ETF
tracked_index: Goldman Sachs ActiveBeta Japan Equity Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/GSJY
  - geography/Japan
---

# GSJY Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

GSJY เป็น rules-based smart-beta, passive/index-tracking Japan equity ETF ที่ติดตาม Goldman Sachs ActiveBeta Japan Equity Index. แม้ชื่อมีคำว่า ActiveBeta แต่ official prospectus ระบุว่า fund `is not actively managed`; จึงผ่าน passive equity gate. Official factsheet ณ 2026-06-30 ระบุ rolling 10-year NAV Total Return CAGR `9.29%` สำหรับ 2016-06-30 ถึง 2026-06-30 หรือ 10.00 elapsed years. Raw NAV TR endpoints ไม่ได้เปิดเผย; normalized start `100.00` และ end ประมาณ `243.11` เป็นค่าที่คำนวณจาก CAGR ที่ issuer ปัดเศษ. Calendar-year NAV rows ที่ยืนยันได้เริ่ม 2017 เพราะ inception คือ 2016-03-02; 2016 จึงไม่ถูกเรียกว่า complete calendar year. Current standardized NAV YTD คือ `12.86%` ณ 2026-06-30.

## Performance check

- entity_key: NYSE Arca:GSJY
- Inception: 2016-03-02
- Metric: NAV Total Return including reinvested distributions and fund expenses; Goldman Sachs states fund performance reflects reinvestment of distributions and NAV calculation assumes management fees and operating expenses
- Tracked index (issuer benchmark): Goldman Sachs ActiveBeta Japan Equity Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR CAGR: `9.29%` (official issuer average annual total return)
- Normalized NAV TR: start `100.00`; end `243.11` (calculated as `100 × (1 + 9.29%)^10`; raw endpoints not disclosed)
- Coverage/source note: official calendar rows are available for 2017-2025; 2016 is an inception-year partial and is not treated as a complete calendar year. Goldman Sachs' ActiveBeta Index is quarterly reconstituted across value, momentum, quality and low-volatility factors. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed.

| Year | GSJY NAV TR | ActiveBeta Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed (partial inception year) | not disclosed | 11.96% |
| 2017 | 24.52% | 23.99% | 21.83% |
| 2018 | -10.52% | -12.88% | -4.38% |
| 2019 | 18.28% | 19.61% | 31.49% |
| 2020 | 12.52% | 14.44% | 18.40% |
| 2021 | 0.60% | 1.71% | 28.71% |
| 2022 | -15.60% | -16.65% | -18.11% |
| 2023 | 18.92% | 20.32% | 26.29% |
| 2024 | 9.09% | 8.28% | 25.02% |
| 2025 | 25.07% | 24.60% | 17.88% |

## Up years / Down years

- Up years / Down years: `6 / 3` over the nine complete calendar years 2017-2025; 2016 excluded as inception-year partial
- Best complete calendar year: 2017, `24.52%`
- Least positive complete calendar year: 2021, `0.60%`
- Worst complete calendar year: 2022, `-15.60%`
- Least bad down year: 2018, `-10.52%`
- Complete calendar 2017-2025 cumulative/CAGR: `104.29% / 8.26%`
- Common 2021-2025 cumulative/CAGR: `37.76% / 6.62%`; positive / negative `3 / 2`
- Current YTD: `12.86%` as of 2026-06-30; latest NAV: `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed official capture

## Risk read-through

GSJY มี 155 holdings และ net assets US$83.19 million ณ 2026-06-30. Sector weights ได้แก่ Industrials `23.8%`, Information Technology `20.7%`, Financials `18.7%`, และ Consumer Discretionary `14.5%`. Total expense ratio คือ `0.25%`; distributions paid quarterly. ความเสี่ยงหลักคือ Japan/country/sector/FX และ factor/smart-beta concentration. Official prospectus ระบุว่า index methodology ใช้ assumptions/estimates และ tracking difference อาจมาจาก transaction costs, expenses และปัจจัยอื่น. Daily NAV history สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official Goldman Sachs factsheet: https://am.gs.com/public-assets/documents/5747f795-24d6-11ef-870d-ed3a247c783e
- Official Goldman Sachs summary prospectus: https://am.gs.com/public-assets/documents/179d857b-24e3-11ef-ad18-377468fbef87?view=true
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
