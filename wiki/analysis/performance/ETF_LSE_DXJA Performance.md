---
type: etf-performance
instrument_type: ETF
entity_key: LSE:DXJA
ticker: WDTRF
exchange: LSE
fund: WisdomTree Japan Equity UCITS ETF - USD Hedged Acc
tracked_index: WisdomTree Japan Hedged Equity UCITS Index
benchmark: S&P 500 Total Return
updated: 2026-07-23
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
primary_region: Japan
tags:
  - analysis/etf-performance
  - ticker/WDTRF
  - geography/Japan
---

# WDTRF Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

`WDTRF` เป็น input OTC alias ของ share class ที่ official WisdomTree ระบุเป็น
`LSE:DXJA`, ISIN `IE00BYQCZD50`; ใช้ `LSE:DXJA` เป็น canonical entity_key.
กองทุนเป็น passive/index-tracking Japan equity ETF แบบ accumulating และ
physical fully replicated. Official factsheet ณ `2026-06-30` รายงาน current
YTD NAV Total Return `21.90%`, since-inception NAV TR CAGR `17.07%`, และ annual
NAV performance ครบ `2018-2025`. ประวัติจาก inception `2017-03-07` ถึง
`2026-06-30` มี `9.31` ปี จึงยังไม่ครบ 10-year window.

## Performance check

- Input ticker: `WDTRF` (OTC alias; not used as the canonical exchange key)
- entity_key: `LSE:DXJA`
- Inception: `2017-03-07`
- Classification: passive, index-tracking, single-country Japan equity ETF
- Replication: physical, fully replicated
- Metric: NAV Total Return / official calendar performance net of fees; accumulating share class retains income in NAV
- Tracked index: `WisdomTree Japan Hedged Equity UCITS Index`
- Total expense ratio: `0.48%` as of `2026-07-22`
- Distribution frequency: `N/A` (accumulating)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR: `unavailable (<10.00 elapsed years)`
- Available period: `2017-03-07` to `2026-06-30`, actual elapsed `9.31` years
- Official since-inception NAV TR CAGR: `17.07%` as of `2026-06-30`; raw TR endpoint levels are `not disclosed`
- Current YTD NAV TR: `21.90%` as of `2026-06-30`

| Year | WDTRF / DXJA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -18.62% | -4.38% |
| 2019 | 18.47% | 31.49% |
| 2020 | 2.79% | 18.40% |
| 2021 | 18.04% | 28.71% |
| 2022 | 6.58% | -18.11% |
| 2023 | 40.52% | 26.29% |
| 2024 | 30.79% | 25.02% |
| 2025 | 31.14% | 17.88% |

Annual ETF rows are official WisdomTree calendar-year performance net of fees;
2017 is omitted as an inception-year partial. S&P 500 rows use the cached USD
Total Return convention as of `2025-12-31`, matched to the complete ETF years.

## Up years / Down years

Among the complete official ETF rows for `2018-2025`:

- Up years / Down years: `7 / 1`
- Best: `2023 +40.52%`
- Least positive: `2020 +2.79%`
- Worst: `2018 -18.62%`
- Least bad down year: `2018 -18.62%`
- 2018-2025 cumulative return: `+200.49%`
- 2018-2025 annualized return: `14.74%` over `8` complete calendar years
- 2021-2025 cumulative return: `+203.22%`
- 2021-2025 annualized return: `24.84%` over `5` complete calendar years
- Current YTD: `21.90%` as of `2026-06-30`

Calendar-row CAGR is calculated from rounded official annual inputs and is not
the same measurement as the official since-inception CAGR. Exact date-to-date
S&P 500 TR for the available since-inception window is `not disclosed`.

## Risk read-through

The available-period NAV TR profile is strong, but this is a concentrated
single-country Japan equity strategy with dividend/export tilt, financials and
industrials exposure, and USD/JPY hedging. WisdomTree states that the hedge uses
currency forward contracts; hedge cost and basis risk can cause results to
diverge from unhedged Japan equity. The accumulating structure means no cash
distribution is paid to investors in the source schedule; income is retained in
NAV. Daily NAV history sufficient to reproduce max drawdown and recovery is
`ไม่พบข้อมูลที่ยืนยันได้` in the sources used for this queue row.

## Sources

- [WisdomTree UK DXJA product page](https://www.wisdomtree.com/gb/products/equities/wisdomtree-japan-equity-ucits-etf---usd-hedged-acc) — canonical listing, current NAV/AUM, TER, structure, holdings and risk context; product data as of `2026-07-22`
- [WisdomTree DXJA factsheet](https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BYQCZD50/) — official NAV performance, annual rows, index and inception data; document date `2026-06-30`
- [London Stock Exchange DXJA company page](https://www.londonstockexchange.com/stock/DXJA/wisdomtree/company-page) — exchange/listing verification for `LSE:DXJA`
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention — common USD total-return reference
- ETF source batch: [[ETF_performance_sources_2026-07-23]] | [[ETF Performance Index]]
