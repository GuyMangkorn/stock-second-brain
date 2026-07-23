---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLKR
ticker: FLKR
exchange: NYSE Arca
issuer: Franklin Templeton
fund: Franklin FTSE South Korea ETF
tracked_index: FTSE South Korea Capped Index-NR
benchmark: S&P 500 Total Return
inception: 2017-11-02
expense_ratio: 0.09%
updated: 2026-07-24
performance_as_of: 2026-05-31
current_ytd_as_of: 2026-07-07
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FLKR
  - geography/South-Korea
---

# FLKR Performance

> Navigation: [[ETF Region Index]] → [[South Korea ETF]] → [[ETF Performance Index]]

## Bottom line

FLKR เป็น passive/index-tracking equity ETF ที่ติดตาม FTSE South Korea Capped Index-NR. Official inception คือ 2017-11-02 จึงยังไม่ครบ `10.00 elapsed years` ณ 2026-07-24 และ issuer แสดง 10-year NAV return เป็น `—`. Official complete calendar-year NAV Total Return ที่ยืนยันได้คือ 2018-2025: cumulative `53.85%` และ CAGR `5.53%`. Current official NAV TR YTD คือ `86.35%` ณ 2026-07-07.

## Performance check

- entity_key: `NYSE Arca:FLKR`
- Classification: supported passive/index-tracking equity ETF
- Inception: `2017-11-02`; elapsed to 2026-07-24: `8.72 years` / `3,186 days`
- Issuer benchmark: `FTSE South Korea Capped Index-NR`
- Metric: NAV Total Return รวม reinvested distributions และหัก fund expenses ตาม issuer disclosure
- Expense ratio: `0.09%` (as of 2025-08-01)
- Benchmark comparison: S&P 500 Total Return เป็น common USD reference benchmark ไม่ใช่ tracked index ของ FLKR
- 10-year NAV TR: `unavailable`; official product page shows `—` for 10 years and inception is under 10 years
- Coverage/source note: official complete calendar years 2018-2025; 2017 inception-year partial ถูกตัดออกจาก annual ranking

## Available-period NAV Total Return

Official annual NAV Return rows cover eight complete calendar years. Raw NAV/TR endpoint levels ไม่เปิดเผย จึงใช้ annual total-return observations ที่ issuer เผยแพร่โดยตรง; ไม่สร้าง 10-year proxy.

| Start date | End date | Start normalized TR | End normalized TR | Actual years | Cumulative | CAGR |
|---|---|---:|---:|---:|---:|---:|
| 2018-01-01 | 2025-12-31 | 100.00 | 153.85 | 8.00 calendar years | 53.85% | 5.53% |

Formula: `Π(1 + annual NAV TR) - 1 = 53.85%`; `153.85^(1 / 8.00) - 1 = 5.53%`. This is available-period performance, not 10-year NAV TR.

## Annual NAV Total Return vs S&P 500 Total Return

ตัวเลข FLKR เป็น official issuer NAV Total Return; S&P 500 เป็น cached USD Total Return convention ที่ reinvest dividends และใช้เป็น common comparison ณ 2025-12-31.

| Year | FLKR NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -20.34% | -4.38% |
| 2019 | 8.05% | 31.49% |
| 2020 | 42.82% | 18.40% |
| 2021 | -6.59% | 28.71% |
| 2022 | -28.31% | -18.11% |
| 2023 | 20.99% | 26.29% |
| 2024 | -19.46% | 25.02% |
| 2025 | 91.79% | 17.88% |
| **2021-2025 cumulative / CAGR** | **25.15% / 4.59%** | **96.17% / 14.43%** |

FLKR trailing S&P 500 by approximately `9.84 percentage points` in 2021-2025 CAGR. Across 2018-2025, up years / down years คือ `4 / 4`; best yearคือ 2025 `+91.79%`, least positiveคือ 2019 `+8.05%`, worstคือ 2022 `-28.31%`, และ least bad down yearคือ 2021 `-6.59%`.

## Current snapshot and risk read-through

- NAV: `US$59.71` และ NAV TR YTD: `+86.35%` ณ 2026-07-07; market price `US$59.44` เป็นคนละ return basis และไม่ถูกรวมกับ NAV TR.
- Holdings: `157` ณ 2026-07-07; Information Technology `50.09%`, Industrials `19.87%`, Financials `11.55%` ณ วันเดียวกัน.
- 3-year NAV standard deviation จาก official factsheet: `34.71%` ณ 2026-03-31. Profile จึงมี country/sector/semiconductor และ FX sensitivity สูง.
- 10-year NAV TR และ raw start/end NAV levels: `ไม่พบข้อมูลที่ยืนยันได้` เพราะกองทุนเริ่มปี 2017 และ issuer แสดง 10-year field เป็น `—`; ไม่มี daily drawdown/recovery calculation ใน lean page.

## Sources

- Official issuer source: [Franklin FTSE South Korea ETF product and performance page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26353/SINGLCLASS/franklin-ftse-south-korea-etf/FLKR)
- Official factsheet: [Franklin FLKR factsheet](https://www.franklintempleton.com/forms-literature/download/FLKR-FF)
- Official S&P source: [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-07-24]]
- Cross-ETF index: [[ETF Performance Index]]
