---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:WDAF
ticker: WDAF
exchange: Nasdaq
fund: WisdomTree Asia Defense Fund
tracked_index: WisdomTree Asia Defense Index (WTADEFN)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/WDAF
  - geography/Asia-Pacific
---

# WDAF Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

WDAF เป็น passive/index-tracking Asia-Pacific thematic equity ETF ที่ติดตาม WisdomTree Asia Defense Index (WTADEFN) และเริ่มกองทุนวันที่ 2025-09-12. จึงยังไม่มี historical NAV TR ครบ 10 ปี. Official NAV Total Return ตั้งแต่ inception ถึง 2026-06-30 อยู่ที่ `+0.56%` และ current standardized YTD อยู่ที่ `+6.77%` ณ วันเดียวกัน. จากช่วงจริง 291 วัน / `0.796731` ปี ค่า CAGR ที่คำนวณได้คือ `+0.70%`; เป็น short-period annualization ไม่ใช่ 10-year performance.

## Performance check

- entity_key: `Nasdaq:WDAF`
- Type gate: ผ่าน — passive/index-tracking Asia-Pacific defense thematic equity ETF
- Metric: issuer NAV Total Return ซึ่งรวม reinvested distributions และ fund expenses ตาม convention ของ issuer
- Inception: `2025-09-12`
- 10-year NAV TR: `10-year NAV TR unavailable`; actual history through 2026-06-30 is `0.796731` years
- Current standardized YTD: `+6.77%` as of `2026-06-30`
- Net expense ratio: `0.45%` as of 2026-07-20

### Available-period NAV TR

WisdomTree reports the since-inception return as a cumulative return because the period is less than one year. Raw daily NAV endpoints are not disclosed in the reviewed official capture, so the end value below is the normalized issuer return, not a raw NAV level.

| Window | Start date | End date | Start TR value | End TR value | Actual years | Cumulative NAV TR | CAGR |
|---|---|---|---:|---:|---:|---:|---:|
| Available period | 2025-09-12 | 2026-06-30 | 100.00 (normalized) | 100.56 (official cumulative) | 0.796731 | +0.56% (official) | +0.70% (derived) |

Calculation: `CAGR = (100.56 / 100.00)^(1 / 0.796731) - 1 = 0.70%`. It is an annualized short-period calculation and must not be labeled as 10-year performance.

### Annual NAV TR and S&P 500 Total Return

WDAF began after the 2024 calendar year and does not have a complete calendar-year NAV TR row. S&P 500 rows use the cached USD Total Return convention for complete calendar years 2016-2025.

| Year | WDAF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not applicable; before inception | -18.11% |
| 2023 | not applicable; before inception | 26.29% |
| 2024 | not applicable; before inception | 25.02% |
| 2025 | not disclosed; incomplete inception year | 17.88% |
| 2026 YTD | +6.77% as of 2026-06-30 | not comparable; current year not cached |

## Up years / Down years

- Up years / Down years: not disclosed because no complete calendar-year NAV TR row exists
- Best / worst year: not disclosed
- 2026 YTD: `+6.77%` as of `2026-06-30`

## Risk read-through

WDAF มี exposure หลักใน South Korea `42.90%`, India `30.36%`, Japan `14.79%`, Australia `5.93%`, Singapore `4.10%` และ Taiwan `1.93%` ณ 2026-07-17. Sector exposure กระจุกใน Industrials `91.02%`, ตามด้วย Information Technology `4.04%` และ Materials `2.93%`. ความเสี่ยงจึงอยู่ที่ defense-sector concentration, country/geopolitical risk, FX, policy/procurement cycle และ emerging-market liquidity.

## Sources

- [WisdomTree WDAF official product page](https://www.wisdomtree.com/us/products/equity/wdaf) — identity, index, inception, fee, NAV TR and holdings; performance through 2026-06-30
- [WisdomTree WDAF factsheet](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-wdaf.pdf) — standardized fund details and return cross-check
- [WisdomTree WDAF investment case](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/investment-case/the-case-for-asia-defense-fund-wdaf.pdf) — Nasdaq listing and index objective
- [WisdomTree Asia Defense Index](https://www.wisdomtree.com/us/indexes/wtadef) — index universe and methodology context
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark convention
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
