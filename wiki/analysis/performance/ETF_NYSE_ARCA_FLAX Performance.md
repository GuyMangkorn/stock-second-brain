---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLAX
ticker: FLAX
exchange: NYSE Arca
fund: Franklin FTSE Asia ex Japan ETF
tracked_index: FTSE Asia ex Japan Capped Index-NR
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FLAX
  - geography/Asia-ex-Japan
---

# FLAX Performance

> Navigation: [[ETF Region Index]] → [[Asia ex Japan ETF]] → [[ETF Performance Index]]

## Bottom line

FLAX เป็น passive/index-tracking equity ETF ที่ติดตาม FTSE Asia ex Japan Capped Index-NR และมี expense ratio `0.19%`. กองทุนเริ่มวันที่ `2018-02-06` จึงยังไม่มี 10-year NAV Total Return: official 10-year field เป็น `—`. Available-period NAV TR จาก `2018-02-06` ถึง `2026-06-30` ครอบคลุมประมาณ `8.39` elapsed years และ issuer รายงาน average annual return `7.85%`; raw NAV TR endpoints ไม่ได้เปิดเผย จึงแสดง normalized endpoint ที่คำนวณจาก CAGR อย่างชัดเจน ไม่ใช่ raw NAV.

สำหรับ complete calendar years `2019-2025`, FLAX NAV TR compound return คือ `77.17%` หรือ CAGR `8.51%`, เทียบกับ S&P 500 Total Return `205.41%` หรือ `17.29%`. Current standardized NAV TR YTD คือ `24.71%` ณ `2026-06-30`.

## Performance check

- `entity_key`: `NYSE Arca:FLAX`
- Fund: Franklin FTSE Asia ex Japan ETF
- Asset class / type: Equity / Indexed
- Inception: `2018-02-06`
- Expense ratio: `0.19%`
- Tracked index: FTSE Asia ex Japan Capped Index-NR
- Strategy: passive/indexing; prospectus states that the fund invests at least 80% of assets in index component securities or related depositary receipts and may use replication or representative sampling.
- Primary metric: official NAV Total Return, including reinvested distributions and fund expenses.
- `10-year NAV TR`: unavailable; issuer reports `—` because fund history is shorter than 10 years.
- Available-period coverage: `2018-02-06` to `2026-06-30`, approximately `8.39` years.
- Official available-period NAV TR CAGR: `7.85%`.
- Raw start/end NAV TR values: `ไม่พบข้อมูลที่ยืนยันได้`.
- Normalized illustration from the official CAGR: start `100.00`, end approximately `188.58`; this is a calculated normalized value, not a disclosed NAV endpoint.
- Current standardized NAV TR YTD: `24.71%` as of `2026-06-30`.
- Market-price returns are not mixed into the NAV TR metric.

## Annual NAV total return

Official calendar-year rows are disclosed from `2019` onward; `2018` is an incomplete inception year and is not presented as a complete calendar-year return.

| Year | FLAX NAV TR | FTSE Asia ex Japan Capped Index-NR | S&P 500 TR |
|---|---:|---:|---:|
| 2018 | not disclosed (partial inception year) | not disclosed | not comparable; ETF partial |
| 2019 | 17.32% | 17.60% | 31.49% |
| 2020 | 24.96% | 25.40% | 18.40% |
| 2021 | -3.72% | -3.10% | 28.71% |
| 2022 | -19.01% | -18.86% | -18.11% |
| 2023 | 6.39% | 7.04% | 26.29% |
| 2024 | 10.92% | 11.75% | 25.02% |
| 2025 | 31.33% | 31.67% | 17.88% |
| 2026 YTD | 24.71% | 24.30% | not comparable; current year not cached |

### Window calculations

| Window | FLAX NAV TR | S&P 500 TR | FLAX minus S&P CAGR |
|---|---:|---:|---:|
| 2019-2025 | cumulative `77.17%`; CAGR `8.51%` | cumulative `205.41%`; CAGR `17.29%` | `-8.78 pp` |
| 2021-2025 | cumulative `20.85%`; CAGR `3.86%` | cumulative `96.17%`; CAGR `14.43%` | `-10.57 pp` |

Formula: `CAGR = (Π(1 + annual return))^(1/n) - 1`. S&P 500 rows use the cached USD Total Return convention for complete calendar years `2016-2025`, with dividends reinvested and as-of `2025-12-31`; 2026 is not used in the S&P comparison because the current-year cache is not complete.

## Up years / Down years

For the seven complete disclosed years `2019-2025`, FLAX had `5` up years and `2` down years.

- Best year: `2025`, `31.33%`
- Worst year: `2022`, `-19.01%`
- Current YTD: `24.71%` as of `2026-06-30`

## Risk read-through

The fund is concentrated in Asia ex Japan equities. As of `2026-06-30`, the largest country exposures were Taiwan `28.97%`, South Korea `24.81%`, China `22.63%`, and India `13.69%`; Information Technology was `47.69%` of the portfolio. Official 3-year NAV-return standard deviation was `18.07%`. Daily NAV history sufficient to calculate maximum drawdown and recovery duration: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official issuer product page: https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26346/SINGLCLASS/franklin-ftse-asia-ex-japan-etf/FLAX
- Official June 2026 factsheet: https://www.franklintempleton.com/forms-literature/download/FLAX-FF
- Official passive-funds prospectus: https://www.franklintempleton.com/forms-literature/download/ETF5-P
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- Dated source batch: [[ETF_performance_sources_2026-07-24]]
