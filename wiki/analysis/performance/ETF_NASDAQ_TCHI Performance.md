---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:TCHI
ticker: TCHI
exchange: NASDAQ
fund: iShares MSCI China Multisector Tech ETF
tracked_index: MSCI China Technology Sub-Industries Select Capped Index (USD) (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/TCHI
  - geography/China
---

# TCHI Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

TCHI เป็น passive/index-tracking China technology equity ETF ที่ติดตาม MSCI China Technology Sub-Industries Select Capped Index (USD) (Net) และเริ่มกองทุนวันที่ 2022-01-25. จึงยังไม่มี historical NAV TR ครบ 10 ปี. Official NAV TR ตั้งแต่ inception ถึง 2026-06-30 อยู่ที่ `+18.39%` cumulative และ `+3.88%` average annual; latest current NAV TR YTD อยู่ที่ `-0.45%` ณ 2026-07-17. Month-end standardized YTD ที่ 2026-06-30 คือ `+13.46%` เป็นคนละ as-of date และไม่ควรนำมาผสมกับ current YTD.

## Performance check

- entity_key: `NASDAQ:TCHI`
- Type gate: ผ่าน — passive/index-tracking China technology equity ETF
- Metric: iShares NAV Total Return ซึ่งสะท้อน reinvested distributions และหัก fund expenses ตาม performance convention ของ issuer
- Inception: `2022-01-25`
- 10-year NAV TR: `10-year NAV TR unavailable`; actual history through 2026-06-30 is `4.427196` years
- Latest current NAV TR YTD: `-0.45%` as of `2026-07-17`
- Standardized month-end YTD: `+13.46%` as of `2026-06-30`
- Expense ratio: `0.59%`

### Available-period NAV TR

| Window | Start date | End date | Start TR value | End TR value | Actual years | Cumulative NAV TR | CAGR / average annual |
|---|---|---|---:|---:|---:|---:|---:|
| Available period | 2022-01-25 | 2026-06-30 | 100.00 (normalized) | 118.39 (official cumulative) | 4.427196 | +18.39% (official) | +3.88% (official; derived endpoint CAGR ≈ +3.89%) |

The normalized endpoint is `100.00 × (1 + 0.1839) = 118.39`; actual years are `1,617 / 365.2425 = 4.427196`. The small difference between issuer average annual `3.88%` and endpoint-derived `3.89%` is rounding.

### Annual NAV TR and S&P 500 Total Return

Complete TCHI calendar-year NAV TR rows are disclosed for 2023-2025. 2022 is an incomplete inception year. S&P 500 rows use the cached USD Total Return convention for complete calendar years 2016-2025.

| Year | TCHI NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not disclosed; incomplete inception year | -18.11% |
| 2023 | -5.69% | 26.29% |
| 2024 | 9.08% | 25.02% |
| 2025 | 33.36% | 17.88% |
| 2026 YTD | -0.45% as of 2026-07-17 | not comparable; current year not cached |

The issuer's standardized month-end table reports `+13.46%` YTD as of 2026-06-30; it is retained separately from the later date-to-date/current page value.

## Up years / Down years

- Up years / Down years: `2 / 1` among disclosed complete calendar rows (2023-2025)
- Best disclosed year: 2025, `+33.36%`
- Least positive disclosed year: 2024, `+9.08%`
- Worst disclosed year: 2023, `-5.69%`
- Available-period cumulative/CAGR: `+18.39%` / `+3.88%` official from 2022-01-25 to 2026-06-30
- Latest current YTD: `-0.45%` as of `2026-07-17`

## Risk read-through

TCHI มี 189 holdings และกระจุกใน Information Technology `52.89%`, Communication `19.14%`, Consumer Discretionary `18.42%` และ Industrials `8.28%` ณ 2026-07-17. ความเสี่ยงหลักคือ China policy/geopolitical risk, technology valuation, sector concentration, ADR/H-share/A-share access, FX และ emerging-market liquidity. iShares ระบุว่าความแตกต่างระหว่าง ETF total return กับ benchmark อาจมาจาก systematic fair value.

## Sources

- [iShares TCHI official product and performance page](https://www.ishares.com/us/products/325390/ishares-msci-china-multisector-tech-etf) — identity, exchange, index, inception, NAV TR, current YTD and exposures
- [iShares TCHI factsheet](https://www.ishares.com/us/literature/fact-sheet/tchi-ishares-msci-china-multisector-tech-etf-fund-fact-sheet-en-us.pdf) — classification and fund-detail cross-check
- [iShares TCHI summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-china-multisector-tech-etf-8-31.pdf) — formal objective and index tracking
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark convention
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
