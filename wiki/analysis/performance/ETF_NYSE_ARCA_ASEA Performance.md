---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:ASEA
ticker: ASEA
exchange: NYSE Arca
fund: Global X FTSE Southeast Asia ETF
tracked_index: FTSE/ASEAN 40 Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-05-31
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/ASEA
  - geography/Southeast-Asia
---

# ASEA Performance

> Navigation: [[ETF Region Index]] → [[Southeast Asia ETF]] → [[ETF Performance Index]]

## Bottom line

ASEA เป็น passive/index-tracking Southeast Asia equity ETF ของ Global X ติดตาม `FTSE/ASEAN 40 Index` และเริ่มกองทุนเมื่อ 2011-02-16. Official rolling 10-year NAV Total Return ณ 2026-06-30 รายงาน CAGR `7.12%` สำหรับช่วง 2016-06-30 ถึง 2026-06-30 ครบ `10.00` ปี; raw endpoints และ cumulative rolling return ไม่ได้เปิดเผย จึง normalize ได้เพียงประมาณ 198.93 จาก 100.00. Latest official factsheet NAV TR YTD คือ `8.67%` ณ 2026-05-31; product-page capture ณ 2026-06-30 ไม่ได้เปิดเผย YTD แยกต่างหาก.

## Performance check

- `entity_key`: `NYSE Arca:ASEA`
- Fund: Global X FTSE Southeast Asia ETF; asset class `Equity`; total expense ratio `0.65%`
- Inception: `2011-02-16`
- Metric: official NAV Total Return, รวม reinvested distributions และ fund expenses ตาม total-return disclosure
- Issuer benchmark: FTSE/ASEAN 40 Index; 40 largest and most liquid companies across Singapore, Malaysia, Indonesia, Thailand and the Philippines
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not issuer benchmark)
- Type note: Global X prospectus explicitly describes an indexing approach and at-least-80% policies in index securities/related ADRs or GDRs and economically tied ASEAN equities; it is not an active, leveraged, inverse, option-income, derivative-heavy, bond, commodity, multi-asset or single-stock ETF.

### Official 10-year NAV TR window

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative return | CAGR | Disclosure |
|---|---|---:|---:|---:|---:|---:|---|
| 2016-06-30 | 2026-06-30 | 10.00 | 100.00 (normalized) | approx. 198.93 (calculated from official CAGR) | approx. 98.93% (calculated) | 7.12% | Raw start/end and cumulative rolling NAV TR not disclosed |

สูตร normalized endpoint: `100.00 × (1 + 7.12%)^10.00 = 198.93`; ค่านี้เป็นการคำนวณจาก issuer-reported 10-year CAGR ไม่ใช่ raw NAV และไม่ใช่ proxy.

### Annual NAV Total Return

| Year | ASEA NAV TR | FTSE/ASEAN 40 Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 8.39% | not disclosed | 11.96% |
| 2017 | 31.89% | not disclosed | 21.83% |
| 2018 | -6.35% | not disclosed | -4.38% |
| 2019 | 7.78% | not disclosed | 31.49% |
| 2020 | -8.05% | not disclosed | 18.40% |
| 2021 | 5.26% | not disclosed | 28.71% |
| 2022 | 5.16% | not disclosed | -18.11% |
| 2023 | 4.43% | not disclosed | 26.29% |
| 2024 | 11.42% | not disclosed | 25.02% |
| 2025 | 18.46% | not disclosed | 17.88% |
| 2026 YTD | 8.67% | not disclosed | not comparable; current year not cached |

ASEA NAV rows `2016-2025` come from the official Global X March 2026 summary prospectus annual-return chart. The 2026 YTD figure comes from the official factsheet as of `2026-05-31`; no value is extrapolated to 2026-07-24. S&P 500 rows reuse the cached USD Total Return convention as of `2025-12-31`.

### Window calculations and ranking

- Complete calendar window `2016-2025`: ASEA NAV TR cumulative `102.43%`, CAGR `7.31%` over 10 complete years; S&P 500 TR cumulative `298.33%`, CAGR `14.82%`; ASEA trails by approximately `7.51 pp` CAGR.
- Common disclosed window `2021-2025`: ASEA NAV TR cumulative `52.57%`, CAGR `8.82%`; S&P 500 TR cumulative `96.17%`, CAGR `14.43%`; ASEA trails by approximately `5.61 pp` CAGR.
- Up years / down years in `2016-2025`: `8 / 2`.
- Best disclosed complete year: `2017`, `31.89%`; least positive: `2023`, `4.43%`.
- Worst disclosed complete year: `2020`, `-8.05%`; least bad down year: `2018`, `-6.35%`.
- Latest official NAV TR YTD: `8.67%` as of `2026-05-31`; current product-page capture as of `2026-06-30` does not disclose a separate YTD field.

## Risk read-through

ASEA เป็น non-diversified Southeast Asia regional equity exposure. Global X reports `40` holdings and net assets about `$98.02M` as of `2026-07-22`, with total expense ratio `0.65%`; the product page reports financials at `61.2%` of equity exposure as of `2026-06-30`. Country, currency, emerging-market liquidity, policy, and financial-sector concentration can increase volatility. Daily NAV history sufficient for fund-level max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

## Sources

- Official Global X product page: https://www.globalxetfs.com/funds/asea
- Official Global X factsheet: https://assets.globalxetfs.com/funds/documents/asea/Fact-Sheet_ASEA.pdf
- Official Global X 2026 summary prospectus: https://assets.globalxetfs.com/funds/documents/asea/prospectus-regulatory/Summary-Prospectus_ASEA.pdf
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]]
- Navigation: [[Southeast Asia ETF]] | [[ETF Region Index]] | [[ETF Performance Index]]
