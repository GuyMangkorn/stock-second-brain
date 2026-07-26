---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IMVP
ticker: IMVP
exchange: NYSE Arca
fund: Invesco India ETF
tracked_index: Bloomberg India MVP Index
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2025-12-31
current_ytd_as_of: not disclosed
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IMVP
  - geography/India
---

# IMVP Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

IMVP เป็น passive/index-tracking India equity ETF ของ Invesco ที่จดทะเบียนบน
NYSE Arca. Official NAV Total Return 10-year CAGR ที่ยืนยันได้คือ `9.19%`
สำหรับช่วง `2015-12-31` ถึง `2025-12-31` (`10.00` ปี) โดยใช้ annual NAV TR
rows ที่ครอบคลุม complete calendar years `2016-2025`. Current 2026 NAV TR YTD
ยัง `not disclosed` ใน official capture ล่าสุด; ไม่ใช้ตัวเลข secondary แทน.

## Performance check

- entity_key: `NYSE Arca:IMVP`
- Inception: `2008-03-05`
- Structure: passive/index-tracking, non-diversified India equity ETF; Invesco
  states the shares are not actively managed and the fund generally invests at
  least 90% in index securities/ADRs/GDRs.
- Metric: issuer NAV Total Return, reflecting distributions under the fund's
  total-return methodology and fund expenses.
- Tracked index: `Bloomberg India MVP Index` after the February 2026 change.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark, not IMVP's tracked index).
- Official 10-year window: `2015-12-31` to `2025-12-31`
- Actual elapsed years: `10.00`
- Start/end normalized TR values: `100.00` / `240.90`; raw issuer NAV index
  endpoints are `not disclosed`. End value is calculated as
  `100 × (1 + 9.19%)^10` from the issuer's displayed 10-year NAV CAGR.
- Official 10-year NAV TR CAGR: `9.19%`
- Current 2026 NAV TR YTD: `not disclosed` as of `2026-07-26`; the reviewed
  official Invesco capture did not expose a numeric post-change YTD value.

| Year | IMVP / PIN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 0.11% | 11.96% |
| 2017 | 37.12% | 21.83% |
| 2018 | -8.10% | -4.38% |
| 2019 | 4.83% | 31.49% |
| 2020 | 18.96% | 18.40% |
| 2021 | 23.94% | 28.71% |
| 2022 | -9.54% | -18.11% |
| 2023 | 22.61% | 26.29% |
| 2024 | 9.52% | 25.02% |
| 2025 | 1.72% | 17.88% |

Annual fund rows are official Invesco NAV performance rows reported under the
former ticker `PIN`; the legal fund is the same fund that changed ticker to
`IMVP`. S&P 500 rows reuse the cached USD Total Return convention as of
`2025-12-31`.

## Up years / Down years

- Up years / Down years: `8 / 2` over complete calendar years `2016-2025`
- Best: `2017`, `+37.12%`
- Least positive: `2016`, `+0.11%`
- Worst: `2018`, `-8.10%`
- Least bad down year: `2022`, `-9.54%`
- 2016-2025 cumulative/CAGR: IMVP `140.92%` / `9.19%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: IMVP `53.14%` / `8.90%`; S&P 500 TR
  `96.17%` / `14.43%`; IMVP trails by approximately `5.53 pp` CAGR
- Current YTD: `not disclosed`; no annualization or proxy is created

## Methodology and data gap

The official SEC supplement says that after close on/about `2026-02-20` and
effective on/about `2026-02-23`, the fund changed ticker from `PIN` to `IMVP`,
replaced `FTSE India Quality and Yield Select Index` with `Bloomberg India MVP
Index`, and changed its strategy to generally invest at least 90% in the new
index and related ADRs/GDRs. Therefore, the 10-year result and 2016-2025 table
are official historical NAV TR for the same legal fund, but the old period
predates the current index. They are not presented as a backfilled proxy for
the post-change Bloomberg index. Current post-change 2026 NAV TR YTD is
`not disclosed` in the reviewed official capture.

## Risk read-through

India single-country and non-diversified exposure can produce concentration,
foreign-market, currency, political, liquidity and factor-model risks. The
official Q4 2025 sheet reported a `0.78%` total expense ratio; current
post-change fee details were not re-stated in the reviewed capture.

## Sources

- [Official Invesco Q4 2025 performance PDF](https://www.invesco.com/us-rest/contentdetail?contentId=7d42fd05f0e21410VgnVCM100000c2f1bf0aRCRD) — fund inception, NYSE Arca listing, passive status, fee, NAV total-return performance as of 2025-12-31, 10-year CAGR and 2016-2025 annual rows
- [Official SEC current summary prospectus](https://www.sec.gov/Archives/edgar/data/1419139/000119312526062436/d71791d497k.htm) — current IMVP identity, Bloomberg India MVP Index, passive/index-tracking strategy and NYSE Arca listing
- [Official SEC index/ticker-change supplement](https://www.sec.gov/Archives/edgar/data/1419139/000110465925123131/tm2533678d1_497.htm) — PIN → IMVP and FTSE → Bloomberg index change effective February 2026
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention — common USD total-return reference
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
