---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DGIN
ticker: DGIN
exchange: NYSE Arca
fund: VanEck Digital India ETF
tracked_index: MVIS Digital India Index (MVDINDTR)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-05-31
current_ytd_as_of: 2026-06-23
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/DGIN
  - geography/India
---

# DGIN Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

DGIN เป็น passive/index-tracking equity ETF ที่ติดตาม MVIS Digital India Index (MVDINDTR) และเริ่มกองทุนวันที่ 2022-02-15 จึงยังไม่มี historical NAV TR ครบ 10 ปี. Official standardized performance ให้ since-inception NAV TR average annual return `-0.37%` ถึง 2026-05-31; ค่า YTD ล่าสุดบน official product page คือ `-14.23%` ณ 2026-06-23. ตัวเลขนี้เป็นคนละ as-of date และไม่ควรนำมาผสมเป็นช่วงเดียวกัน.

## Performance check

- entity_key: `NYSE Arca:DGIN`
- Type gate: ผ่าน — passive/index-tracking India thematic equity ETF
- Metric: issuer NAV Total Return ซึ่งรวม reinvested distributions และ fund expenses ตาม convention ของ issuer
- Inception: `2022-02-15`
- 10-year NAV TR: `10-year NAV TR unavailable`; actual history through 2026-05-31 is `4.287562` years
- Latest current YTD: `-14.23%` as of `2026-06-23`
- Expense ratio: `0.70%` on the current official product page

### Available-period NAV TR

Raw NAV endpoints are not disclosed in the reviewed official capture. The endpoint below is therefore normalized from the issuer's rounded since-inception average annual NAV TR; it is not a 10-year result.

| Window | Start date | End date | Start TR value | End TR value | Actual years | Cumulative NAV TR | CAGR / average annual |
|---|---|---|---:|---:|---:|---:|---:|
| Available period | 2022-02-15 | 2026-05-31 | 100.00 (normalized) | 98.42 (derived) | 4.287562 | approximately -1.58% (derived) | -0.37% (official) |

Calculation: `98.42 = 100 × (1 - 0.0037)^4.287562`; derived cumulative return is approximate because the issuer reports the CAGR rounded to two decimals.

### Annual NAV TR and S&P 500 Total Return

VanEck's reviewed official capture does not disclose complete calendar-year NAV TR rows for 2023-2025. 2022 is an incomplete inception year. S&P 500 rows use the cached USD Total Return convention for complete calendar years 2016-2025.

| Year | DGIN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not disclosed; incomplete inception year | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |
| 2026 YTD | -14.23% as of 2026-06-23 | not comparable; current year not cached |

The same VanEck performance page also contains an older/stale block showing `-25.12%` YTD and `-3.25%` life NAV return, consistent with a 2026-03-31 fund-profile snapshot. It is not mixed into the latest record; the dated May factsheet and June 23 product snapshot are retained as the source-quality choice.

## Up years / Down years

- Up years / Down years: not disclosed because complete annual NAV TR rows are not disclosed
- Best / worst year: not disclosed
- 2026 YTD: `-14.23%` as of `2026-06-23`

## Risk read-through

DGIN มี exposure อินเดีย 100% และกระจุกใน Communication Services `33.07%`, Financials `26.21%`, Consumer Discretionary `21.41%` ณ 2026-05-31. จึงไวต่อ India country risk, sector concentration, valuation, FX และ emerging-market liquidity. VanEck ยังเปิดเผยการเปลี่ยนแปลง methodology ของ MVIS Digital India Index มีผล 2026-03-20; ผลตอบแทนก่อนและหลังจุดเปลี่ยนอาจไม่ใช่ strategy history ที่เหมือนกันทั้งหมด.

## Sources

- [VanEck DGIN official product page](https://www.vaneck.com/us/en/investments/digital-india-etf-dgin/overview/) — identity, exchange, index, inception, current YTD and fee; current snapshot as of 2026-06-23
- [VanEck DGIN official performance page](https://www.vaneck.com/us/en/investments/digital-india-etf-dgin/performance/) — NAV TR average annual table and sector/country data
- [VanEck DGIN factsheet](https://www.vaneck.com/us/en/investments/digital-india-etf-dgin-fact-sheet.pdf) — standardized performance as of 2026-05-31
- [SEC DGIN summary prospectus](https://www.sec.gov/Archives/edgar/data/1137360/000113736023000421/vaneckdigitalindiaetfdgin-.htm) — formal listing and index objective
- [SEC DGIN index-methodology supplement](https://www.sec.gov/Archives/edgar/data/1137360/000113736026000237/ck0001137360-20260227.htm) — methodology change effective 2026-03-20
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark convention
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
