---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:GLIN
ticker: GLIN
exchange: NYSE Arca
fund: VanEck India Growth Leaders ETF
tracked_index: MarketGrader India All-Cap Growth Leaders Index (MGINGRNR)
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-24
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/GLIN
  - geography/India
---

# GLIN Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

GLIN เป็น passive/index-tracking India equity ETF ที่ติดตาม MarketGrader India All-Cap Growth Leaders Index ซึ่งใช้ปัจจัย growth, value, profitability และ cash flow ในการจัดอันดับหุ้น. Official rolling 10-year NAV Total Return CAGR คือ `1.92%` สำหรับ `2016-06-30` ถึง `2026-06-30` (`10.00` elapsed years); raw NAV endpoints ไม่ได้เปิดเผย แต่ normalized TR ที่ implied ได้คือประมาณ `100.00 → 120.95`. Annual NAV TR ครบ 10 calendar years `2016-2025` compound เป็น `17.36%` / CAGR `1.61%`. Current issuer YTD ล่าสุดคือ `-4.15%` ณ `2026-07-24`; standardized month-end YTD คือ `0.25%` ณ `2026-06-30`.

## Performance check

- entity_key: `NYSE Arca:GLIN`
- Inception: `2010-08-24`
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index: `MarketGrader India All-Cap Growth Leaders Index (MGINGRNR)`; before market close `2020-04-30`, historical index data reflects the prior `MVIS India Small-Cap Index (MVSCIFTR)`.
- Type gate: supported passive/index-tracking equity ETF. The SEC prospectus explicitly describes a passive/indexing approach, at least 80% index exposure through the fund's Mauritius subsidiary, and no attempt to beat the index.
- Expense ratio: `0.80%` gross and `0.72%` net; contractual expense cap is `0.70%` through at least `2027-05-01`.
- Official rolling 10-year window: start date `2016-06-30`; end date `2026-06-30`; actual years `10.00`; start TR value `100.00` normalized; end TR value `not disclosed` raw / approximately `120.95` implied from the official `1.92%` CAGR; official CAGR `1.92%`.
- Official complete-calendar window: `2016-12-31` to `2025-12-31`; actual years `10.00`; normalized start/end TR `100.00 → 117.36` from the official annual rows; CAGR `1.61%` calculated from those rows.
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not the issuer benchmark).

| Year | GLIN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -4.70% | 11.96% |
| 2017 | 66.88% | 21.83% |
| 2018 | -38.00% | -4.38% |
| 2019 | 0.80% | 31.49% |
| 2020 | -21.65% | 18.40% |
| 2021 | -21.99% | 28.71% |
| 2022 | 29.15% | -18.11% |
| 2023 | 35.50% | 26.29% |
| 2024 | -4.92% | 25.02% |
| 2025 | 16.11% | 17.88% |

Annual NAV rows come from the SEC summary prospectus chart and are NAV total returns before taxes. S&P 500 rows reuse the cached USD Total Return convention as of `2025-12-31`; 2026 is not included because the cached calendar-year series is incomplete.

## Window calculations

- GLIN official rolling `2016-06-30` to `2026-06-30`: CAGR `1.92%`; implied cumulative approximately `20.95%`; raw endpoints `not disclosed`.
- GLIN complete-calendar `2016-2025`: cumulative `17.36%`; CAGR `1.61%`; positive / negative years `6 / 4`; best year `2017 +66.88%`; worst year `2018 -38.00%`.
- GLIN common `2021-2025`: cumulative `50.71%`; CAGR `8.55%`; S&P 500 cumulative `96.17%`; CAGR `14.43%`; GLIN trails by approximately `5.88 pp` CAGR.
- S&P 500 reference `2016-2025`: cumulative `298.33%`; CAGR `14.82%`.
- Current NAV TR YTD: `-4.15%` as of `2026-07-24` from VanEck's current product snapshot. The official June month-end factsheet reports `0.25%` YTD as of `2026-06-30`; the two observations use different as-of dates and are both retained rather than blended.

## Risk read-through

GLIN มี India exposure `100.65%` และ sector หลักคือ financials, industrials, consumer discretionary และ health care ณ `2026-06-30`. ความเสี่ยงหลักคือ India/emerging-market liquidity and foreign-ownership restrictions, currency, factor/model risk, non-diversification, sector concentration, and tracking error. Daily NAV history ที่ยืนยันได้สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้` ใน lean capture.

## Sources

- [VanEck official GLIN product and performance page](https://www.vaneck.com/us/en/investments/india-growth-leaders-etf-glin/) — current NAV/YTD, fund objective, fee and current performance snapshot; current snapshot as of `2026-07-24`.
- [VanEck GLIN fact sheet](https://www.vaneck.com/us/en/investments/india-growth-leaders-etf-glin-fact-sheet.pdf) — official rolling NAV TR and index performance through `2026-06-30`, fee, inception, exchange and exposure.
- [SEC GLIN summary prospectus](https://www.sec.gov/Archives/edgar/data/1137360/000113736026000467/vaneckindiagrowthleaderset.htm) — NYSE Arca listing, passive/indexing strategy, subsidiary/80% policy, index change and annual NAV TR chart; dated `2026-05-01`.
- [VanEck GLIN annual shareholder report](https://vaneck.onlineprospectus.net/VanEck/MOB_library/MOB_data/LIB_SummaryProspectus/glinar/glinar.pdf) — NAV total-return and 10-year hypothetical-value cross-check through `2025-12-31`.
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common USD Total Return reference.
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
