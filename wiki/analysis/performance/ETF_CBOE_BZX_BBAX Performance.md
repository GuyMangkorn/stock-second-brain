---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:BBAX
ticker: BBAX
exchange: Cboe BZX
fund: JPMorgan BetaBuilders Developed Asia Pacific ex-Japan ETF
tracked_index: Morningstar Developed Asia Pacific ex-Japan Target Market Exposure Index (net total return)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/BBAX
  - geography/Asia-Pacific
---

# BBAX Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

BBAX เป็น passive/index-tracking developed Asia-Pacific equity ETF แต่เริ่มกองทุนวันที่ 2018-08-07 จึงยังไม่มี `10-year NAV TR`. Official NAV Total Return สำหรับ available period ถึง 2026-06-30 ให้ cumulative `64.48%` และ annualized CAGR `6.50%`; NAV TR YTD อยู่ที่ `8.20%` ณ 2026-06-30. ช่วงปีปฏิทิน 2019-2025 เป็นบวก 6 ปีและลบ 1 ปี โดย best year คือ 2025 `20.73%` และ worst year คือ 2022 `-4.45%`.

## Performance check

- `entity_key: Cboe BZX:BBAX` (ยืนยันจาก Cboe listing และ JPMorgan/SEC fund documents)
- Inception: `2018-08-07` (class launch)
- Metric: `NAV Total Return` รวม dividends/capital gains ที่ reinvested และ fund expenses; ไม่ใช้ market-price return ปนกัน
- Tracked index: `Morningstar Developed Asia Pacific ex-Japan Target Market Exposure Index (net total return)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- `10-year NAV TR unavailable`: inception ถึง 2026-06-30 ครอบคลุมประมาณ `7.90` elapsed years เท่านั้น
- Available-period window: `2018-08-07` to `2026-06-30`
- Normalized TR values: start `100.00`; end `164.48`, derived from JPMorgan's official growth-of-$10,000 ending value `$16,448`; raw NAV TR endpoints are `not disclosed`
- Actual years: `7.90` (`2,884 / 365.25`)
- Available-period cumulative return: `64.48%`
- Available-period CAGR: `6.50%`; formula `(164.48 / 100.00)^(1 / 7.90) - 1`, with endpoint rounded from the official chart
- Coverage/source note: official calendar-year NAV TR rows 2019-2025; S&P 500 rows reuse the cached USD Total Return convention for complete calendar years 2019-2025, as of 2025-12-31

| Year | BBAX NAV TR | S&P 500 TR |
|---|---:|---:|
| 2019 | 18.44% | 31.49% |
| 2020 | 8.20% | 18.40% |
| 2021 | 5.36% | 28.71% |
| 2022 | -4.45% | -18.11% |
| 2023 | 5.60% | 26.29% |
| 2024 | 1.69% | 25.02% |
| 2025 | 20.73% | 17.88% |

BBAX's 2019-2025 annual rows compound to `67.26%` / CAGR `7.62%`, versus S&P 500 TR `205.41%` / CAGR `17.29%`; this common calendar window trails by approximately `9.67 pp` CAGR. In the common 2021-2025 window, BBAX compounds to `30.52%` / CAGR `5.47%`, versus S&P 500 TR `96.17%` / CAGR `14.43%`.

## Up years / Down years

- Up years / Down years: `6 / 1`
- Best: 2025, `20.73%`
- Least positive: 2024, `1.69%`
- Worst: 2022, `-4.45%`
- Least bad down year: 2022, `-4.45%`
- Current YTD NAV TR: `8.20%` as of `2026-06-30`

## Risk read-through

BBAX เป็น passive/index-tracking equity ETF ที่พยายาม replicate ดัชนี Morningstar โดยมี gross/net annual expenses `0.190%`. Exposure หลักอยู่ที่ Australia, Hong Kong, Singapore และ New Zealand; risk summary ของ issuer ระบุ liquidity, currency และความผันผวนของตลาด Asia-Pacific. Fund-level daily drawdown/recovery และ raw NAV TR endpoint history ไม่ได้เปิดเผยในแหล่งข้อมูลที่ตรวจสอบได้. `10-year NAV TR unavailable` และไม่สร้าง proxy แทน.

## Sources

- Official JPMorgan fact sheet (as of 2026-06-30): https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBAX.PDF
- Official Cboe listing: https://www.cboe.com/us/equities/listings/listed_products/issuer_detail/JMAM/
- Official SEC prospectus record identifying `Cboe BZX Exchange, Inc.`: https://www.sec.gov/Archives/edgar/data/1485894/000119312523046804/d439474d485bpos.htm
- Official S&P 500 index page / cached calendar-year TR convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
