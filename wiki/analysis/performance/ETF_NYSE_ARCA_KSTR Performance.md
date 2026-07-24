---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:KSTR
ticker: KSTR
exchange: NYSE Arca
fund: KraneShares China Technology & Semiconductor STAR 50 Index ETF
tracked_index: SSE Science and Technology Innovation Board 50 Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/KSTR
  - geography/China
---

# KSTR Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

KSTR เป็น passive/index-tracking China STAR Market technology/semiconductor equity ETF ของ KraneShares ติดตาม SSE Science and Technology Innovation Board 50 Index และเริ่มกองทุนเมื่อ 2021-01-26. ณ 2026-06-30 มีประวัติประมาณ 5.43 ปี จึงระบุ `10-year NAV TR unavailable`. Official available-period NAV TR ตั้งแต่ inception ให้ cumulative return `27.40%` และ annualized return `4.56%`; current NAV TR YTD คือ `71.70%` ณ 2026-06-30.

## Performance check

- entity_key: NYSE Arca:KSTR
- Inception: 2021-01-26
- Metric: official NAV Total Return; distributions are reinvested and fund expenses are reflected in the growth-of-$10,000/NAV performance convention
- Tracked index (issuer benchmark): SSE Science and Technology Innovation Board 50 Index
- Gross / net expense ratio: 0.89% / 0.65%
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- Coverage: approximately 5.43 elapsed years from 2021-01-26 to 2026-06-30; `10-year NAV TR unavailable`
- Coverage/source note: annual NAV TR rows are not disclosed in the reviewed official capture; S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed

### Available-period NAV TR window

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative return | Annualized return | Disclosure |
|---|---|---:|---:|---:|---:|---:|---|
| 2021-01-26 | 2026-06-30 | approx. 5.43 | 100.00 (normalized) | 127.40 (derived from official cumulative) | 27.40% | 4.56% official | Raw NAV endpoints not disclosed |

`127.40 = 100.00 × (1 + 27.40%)`; this is a transparent normalization of the official since-inception NAV TR, not a proxy.

| Year | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | not disclosed (partial inception year) | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |
| 2026 YTD | 71.70% as of 2026-06-30 | not comparable; current year not cached |

## Window read-through

- 10-year NAV TR CAGR: unavailable because official inception is 2021-01-26 and the fund had only approximately 5.43 years of history as of 2026-06-30.
- Available-period official NAV TR: cumulative `27.40%`, annualized `4.56%`, 2021-01-26 to 2026-06-30.
- Best/worst calendar-year ranking and 2021-2025 CAGR: not disclosed because the reviewed official sources do not provide complete calendar NAV TR rows.
- Current YTD NAV TR: `71.70%` as of 2026-06-30; S&P 500 current-year comparison is not used because the cached benchmark window ends 2025-12-31.

## Risk read-through

KSTR เป็น non-diversified China A-share/STAR Market equity ETF ที่มี 53 holdings และ Information Technology exposure `92.90%` ณ 2026-06-30. ความเสี่ยงหลักคือ technology/sector concentration, China/A-share access, policy/geopolitical, currency และ liquidity risk. Daily NAV TR history สำหรับคำนวณ drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้` ใน official capture รอบนี้.

## Sources

- Official issuer source: https://kraneshares.com/etf/kstr/
- Official factsheet: https://kraneshares.com/resources/factsheet/kstr_factsheet.pdf
- Official annual shareholder report: https://kraneshares.com/resources/compliance/2026_05_29_kstr_annual.TSR.report.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
