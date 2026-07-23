---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWY
ticker: EWY
exchange: NYSE Arca
fund: iShares MSCI South Korea ETF
tracked_index: MSCI Korea 25/50 Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-23
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
primary_region: South Korea
tags:
  - analysis/etf-performance
  - ticker/EWY
  - geography/South-Korea
---

# EWY Performance

> Navigation: [[ETF Region Index]] → [[South Korea ETF]] → [[ETF Performance Index]]

## Bottom line

EWY มี official annual `NAV Total Return` ครบปี 2016-2025: เป็นบวก 6 ปีและลบ 4 ปี; best คือ 2025 `+97.57%` และ worst คือ 2022 `-26.70%`. Official rolling 10-year NAV TR CAGR อยู่ที่ `16.72%` สำหรับช่วง 2016-06-30 ถึง 2026-06-30; current NAV YTD คือ `+75.82%` ณ 2026-07-21.

## Performance check

- `entity_key: NYSE Arca:EWY` (issuer ระบุ Exchange เป็น NYSE Arca)
- Inception: 2000-05-09
- Classification: passive/index-tracking single-country South Korea equity ETF
- Metric: `NAV Total Return` รวม distributions reinvested และ fund expenses
- Issuer benchmark: `MSCI Korea 25/50 Index (Net)`
- Expense ratio: `0.59%`; distribution frequency: annual
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year window: `2016-06-30` to `2026-06-30`; actual years: `10.00`
- 10-year NAV TR CAGR: `16.72%`; Start TR value: `100.00` (normalized); End TR value: `469.17` (normalized from official cumulative return `369.17%`); raw NAV TR endpoints: `ไม่พบข้อมูลที่ยืนยันได้`
- Formula: `(469.17 / 100.00)^(1 / 10.00) - 1 = 16.72%` using the official cumulative-return display, rounded
- Coverage/source note: official issuer calendar-year rows 2016-2025; 2016-2020 are shown by the issuer to one decimal, while the US factsheet shows 2021-2025 to two decimals. Exact June-to-June S&P 500 TR is not disclosed; the table uses the cached 2016-2025 calendar-year S&P 500 TR convention.

| Year | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.10% | 11.96% |
| 2017 | 44.40% | 21.83% |
| 2018 | -20.30% | -4.38% |
| 2019 | 8.30% | 31.49% |
| 2020 | 39.70% | 18.40% |
| 2021 | -7.56% | 28.71% |
| 2022 | -26.70% | -18.11% |
| 2023 | 19.05% | 26.29% |
| 2024 | -20.79% | 25.02% |
| 2025 | 97.57% | 17.88% |

**Up years / Down years**

- Up years / Down years: 6 / 4
- Best: 2025, `+97.57%`
- Least positive: 2019, `+8.30%`
- Worst: 2022, `-26.70%`
- Least bad down year: 2021, `-7.56%`
- 2016-2025 annual-row cumulative / CAGR: `+135.42% / 8.94%` from rounded official calendar rows; this is separate from the rolling 10-year CAGR above
- 2021-2025 annual-row CAGR: `4.77%`
- Current YTD: `+75.82%` as of 2026-07-21

## Risk read-through

EWY มี rolling 10-year NAV TR CAGR `16.72%`, แต่ annual profile ผันผวนมาก: official 3-year standard deviation `41.20%` และ equity beta `1.87` ณ 2026-06-30. เป็น single-country exposure ที่มี Information Technology `50.63%` ณ 2026-07-22 จึงไวต่อ South Korea equity cycle, semiconductor concentration และ KRW/USD. Expense ratio `0.59%` ถูกหักใน NAV Total Return. Official daily NAV series สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [iShares US product page — EWY](https://www.ishares.com/us/products/239681/ishares-msci-south-korea-capped-etf) — identity, exchange, benchmark, inception, current NAV/YTD, fee, risk statistics; accessed 2026-07-23; current observations as of 2026-07-22 / 2026-07-21.
- [iShares UK professional performance page — EWY](https://www.ishares.com/uk/professional/en/products/239681/ewy?siteEntryPassthrough=true&switchLocale=y) — official calendar rows 2016-2025, rolling 10-year cumulative/annualized performance; performance as of 2026-06-30.
- [iShares EWY US factsheet](https://www.ishares.com/us/literature/fact-sheet/ewy-ishares-msci-south-korea-etf-fund-fact-sheet-en-us.pdf) — official NAV rows 2021-2025, performance definition and fee; factsheet as of 2026-06-30.
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark identity; annual rows reuse the cached 2016-2025 USD Total Return convention as of 2025-12-31.
- Source batch: [[ETF_performance_sources_2026-07-23]]
