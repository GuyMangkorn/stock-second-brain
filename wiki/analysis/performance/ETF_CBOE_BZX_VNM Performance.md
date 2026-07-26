---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:VNM
ticker: VNM
exchange: Cboe BZX
fund: VanEck Vietnam ETF
tracked_index: MarketVector Vietnam Local Index (MVVNMLTR)
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-24
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VNM
  - geography/Vietnam
---

# VNM Performance

> Navigation: [[ETF Region Index]] → [[Vietnam ETF]] → [[ETF Performance Index]]

## Bottom line

VNM เป็น passive/index-tracking Vietnam equity ETF ที่พยายามติดตาม MarketVector Vietnam Local Index. Official rolling 10-year NAV Total Return CAGR คือ `3.65%` สำหรับ `2016-06-30` ถึง `2026-06-30` (`10.00` elapsed years); raw NAV endpoints ไม่ได้เปิดเผย แต่คำนวณ normalized TR ได้ประมาณ `100.00 → 143.12`. Annual NAV TR ครบ 10 calendar years `2016-2025` compound เป็น `44.54%` / CAGR `3.75%`. Current issuer YTD ล่าสุดคือ `-12.07%` ณ `2026-07-24`; standardized month-end YTD คือ `-1.41%` ณ `2026-06-30`.

## Performance check

- entity_key: `Cboe BZX:VNM`
- Inception: `2009-08-11`
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index: `MarketVector Vietnam Local Index (MVVNMLTR)`; VanEck states the fund seeks to replicate the index before fees and expenses. Index data before market close `2023-03-17` reflects the prior `MVIS Vietnam Index (MVVNMTR)`.
- Expense ratio: `0.66%` gross and net; contractual expense cap is `0.76%` through at least `2027-05-01`.
- Official rolling 10-year window: start date `2016-06-30`; end date `2026-06-30`; actual years `10.00`; start TR value `100.00` normalized; end TR value `not disclosed` raw / approximately `143.12` implied from the official `3.65%` CAGR; official CAGR `3.65%`.
- Implied rolling cumulative return: approximately `43.12%`; this is a calculation from the official CAGR, not a raw endpoint.
- Official complete-calendar window: `2016-12-31` to `2025-12-31`; actual years `10.00`; normalized start/end TR `100.00 → 144.54` from the official annual rows; CAGR `3.75%` calculated from those rows.
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not the issuer benchmark).

| Year | VNM NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -9.78% | 11.96% |
| 2017 | 35.76% | 21.83% |
| 2018 | -14.14% | -4.38% |
| 2019 | 8.86% | 31.49% |
| 2020 | 9.72% | 18.40% |
| 2021 | 22.52% | 28.71% |
| 2022 | -44.47% | -18.11% |
| 2023 | 15.95% | 26.29% |
| 2024 | -10.19% | 25.02% |
| 2025 | 62.42% | 17.88% |

Annual NAV rows come from the SEC summary prospectus chart and are NAV total returns before taxes. S&P 500 rows reuse the cached USD Total Return convention as of `2025-12-31`; 2026 is not included because the cached calendar-year series is incomplete.

## Window calculations

- VNM official rolling `2016-06-30` to `2026-06-30`: CAGR `3.65%`; implied cumulative approximately `43.12%`; raw endpoints `not disclosed`.
- VNM complete-calendar `2016-2025`: cumulative `44.54%`; CAGR `3.75%`; positive / negative years `6 / 4`; best year `2025 +62.42%`; worst year `2022 -44.47%`.
- VNM common `2021-2025`: cumulative `15.07%`; CAGR `2.85%`; S&P 500 cumulative `96.17%`; CAGR `14.43%`; VNM trails by approximately `11.58 pp` CAGR.
- S&P 500 reference `2016-2025`: cumulative `298.33%`; CAGR `14.82%`.
- Current NAV TR YTD: `-12.07%` as of `2026-07-24` from VanEck's current product snapshot. The official June month-end factsheet reports `-1.41%` YTD as of `2026-06-30`; the two observations use different as-of dates and are both retained rather than blended.

## Risk read-through

VNM เป็นกองทุน non-diversified ที่มี exposure Vietnam `99.34%` และ sector หลักเป็น financials, real estate และ consumer staples ณ `2026-06-30`. ความเสี่ยงหลักคือ frontier/emerging-market liquidity, Vietnam political/regulatory and foreign-ownership limits, currency, country concentration, real-estate/financials concentration, and index-tracking risk. Daily NAV history ที่ยืนยันได้สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้` ใน lean capture.

## Sources

- [VanEck official VNM product and performance page](https://www.vaneck.com/us/en/investments/vietnam-etf-vnm/) — current NAV/YTD and fund objective; current snapshot as of `2026-07-24`.
- [VanEck VNM fact sheet](https://www.vaneck.com/us/en/investments/vietnam-etf-vnm-fact-sheet.pdf) — official rolling NAV TR and index performance through `2026-06-30`, fee, inception and exchange field.
- [SEC VNM summary prospectus](https://www.sec.gov/Archives/edgar/data/1137360/000113736026000473/vaneckvietnametfvnmsumpro-.htm) — current principal listing `Cboe BZX`, passive/indexing strategy, 10-year return table and annual NAV TR chart; dated `2026-05-01`.
- [VanEck VNM annual shareholder report](https://vaneck.onlineprospectus.net/VanEck/MOB_library/MOB_data/LIB_SummaryProspectus/vnmar/vnmar.pdf) — NAV total-return basis and 10-year hypothetical-value cross-check through `2025-12-31`.
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common USD Total Return reference.
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
