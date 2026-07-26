---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:KGRN
ticker: KGRN
exchange: NYSE Arca
fund: KraneShares MSCI China Clean Technology Index ETF
tracked_index: MSCI China IMI Environment 10/40 Index (USD Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/KGRN
  - geography/China
---

# KGRN Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

KGRN เป็น passive/index-tracking China clean-technology equity ETF ที่ติดตาม MSCI China IMI Environment 10/40 Index (USD Net) และเริ่มกองทุนวันที่ 2017-10-12. จึงยังไม่มี historical NAV TR ครบ 10 ปี. Official NAV TR ตั้งแต่ inception ถึง 2026-06-30 อยู่ที่ `+7.53%` cumulative และ `+0.84%` annualized; current standardized NAV TR YTD อยู่ที่ `-13.22%` ณ 2026-06-30.

## Performance check

- entity_key: `NYSE Arca:KGRN`
- Type gate: ผ่าน — passive/index-tracking China clean-technology thematic equity ETF
- Metric: fund NAV Total Return ซึ่งรวม reinvested distributions และ fund expenses ตาม convention ของ issuer
- Inception: `2017-10-12`
- 10-year NAV TR: `10-year NAV TR unavailable`; actual history through 2026-06-30 is `8.714758` years
- Current standardized NAV TR YTD: `-13.22%` as of `2026-06-30`
- Total expense ratio: `0.79%`
- Exchange conflict: current product page displays `NYSE`, while formal shareholder-report/listing documents identify `NYSE Arca`; `NYSE Arca:KGRN` is retained as canonical.

### Available-period NAV TR

Raw NAV endpoints are not disclosed in the reviewed official capture. The normalized endpoint below uses the issuer's since-inception cumulative NAV TR.

| Window | Start date | End date | Start TR value | End TR value | Actual years | Cumulative NAV TR | CAGR / annualized |
|---|---|---|---:|---:|---:|---:|---:|
| Available period | 2017-10-12 | 2026-06-30 | 100.00 (normalized) | 107.53 (official cumulative) | 8.714758 | +7.53% (official) | +0.84% (official) |

Calculation: `107.53 = 100.00 × (1 + 0.0753)`; actual years are `3,183 / 365.2425 = 8.714758`. The issuer's annualized figure is used as the primary CAGR metric.

### Annual NAV TR and S&P 500 Total Return

KraneShares' current official performance history does not disclose complete calendar-year NAV TR rows. The 2025 shareholder report's `27.07%` is a fiscal-year period ended 2025-03-31, not calendar 2025, so it is not inserted as a calendar-year return. S&P 500 rows use the cached USD Total Return convention for complete calendar years 2016-2025.

| Year | KGRN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not disclosed; incomplete inception year | 21.83% |
| 2018 | not disclosed | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | not disclosed | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed; fiscal-year observation not calendar-comparable | 17.88% |
| 2026 YTD | -13.22% as of 2026-06-30 | not comparable; current year not cached |

## Up years / Down years

- Up years / Down years: not disclosed because complete calendar-year NAV TR rows are not disclosed
- Best / worst calendar year: not disclosed
- Available-period cumulative/CAGR: `+7.53%` / `+0.84%` official from 2017-10-12 to 2026-06-30
- Current standardized YTD: `-13.22%` as of `2026-06-30`

## Risk read-through

KGRN เป็น thematic China equity ที่เน้นบริษัทซึ่งมีรายได้อย่างน้อย 50% จากผลิตภัณฑ์หรือบริการด้านสิ่งแวดล้อม โดย index ครอบคลุม Alternative Energy, Sustainable Water, Pollution Prevention และ Energy Efficiency. ความเสี่ยงหลักคือ China policy/geopolitical risk, clean-tech cycle, subsidy/regulatory changes, sector concentration, valuation, FX และ emerging-market liquidity.

## Sources

- [KraneShares KGRN official product/performance page](https://kraneshares.com/etf/kgrn/) — identity, index, current performance, inception, fee and exchange-page conflict
- [KraneShares KGRN factsheet](https://kraneshares.com/resources/factsheet/kgrn_factsheet.pdf) — passive/index-tracking classification and index methodology
- [KraneShares KGRN annual shareholder report](https://kraneshares.com/resources/compliance/2025_05_28_kgrn_annual.TSR.report.pdf) — formal principal exchange and fiscal-year context
- [KraneShares KGRN listing announcement](https://kraneshares.com/kraneshares-msci-china-environment-etf-ticker-kgrn-lists-on-the-new-york-stock-exchange/) — original listing and index objective
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark convention
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
