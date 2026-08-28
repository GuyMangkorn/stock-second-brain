---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:KBA
ticker: KBA
exchange: NYSE Arca
fund: KraneShares Bosera MSCI China A 50 Connect Index ETF
tracked_index: MSCI China A 50 Connect Index
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-27
fund_facts_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/KBA
  - geography/China
---

# KBA Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

KBA เป็น passive/index-tracking China A-share equity ETF ของ KraneShares ติดตาม `MSCI China A 50 Connect Index` และเริ่มกองทุนเมื่อ `2014-03-04`. Official rolling 10-year NAV Total Return ล่าสุด ณ `2026-07-31` รายงาน CAGR `6.22%` สำหรับช่วง `2016-07-31` ถึง `2026-07-31` ครบ `10.00` ปี; raw NAV endpoints และ cumulative rolling return ไม่ได้เปิดเผย จึงแสดง normalized endpoint ประมาณ `182.84` จาก start `100.00` โดยระบุว่าเป็นการคำนวณจาก CAGR. Latest standardized NAV TR YTD คือ `7.45%` ณ `2026-07-31`; June quarter-end cross-check remains `11.37%` YTD and `6.90%` 10-year CAGR.

## Performance check

- `entity_key`: `NYSE Arca:KBA`
- Fund: KraneShares Bosera MSCI China A 50 Connect Index ETF; asset class `Equity`; total annual fund operating expense `0.79%` gross / `0.56%` net. The current product page says the contractual fee waiver is in effect through `2028-08-01`; the linked August 2025 summary prospectus states `2026-08-01`, so the current product page is used for the latest fee snapshot and the conflict is retained.
- Inception: `2014-03-04`
- Metric: official NAV Total Return, รวม reinvested dividends and capital gains และหัก fund expenses ตาม issuer growth-of-$10,000 disclosure
- Issuer benchmark: `MSCI China A 50 Connect Index`; 50 large-cap Shanghai/Shenzhen A-shares available through Stock Connect
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not issuer benchmark)
- Type note: the prospectus states that the Fund seeks to track the price and yield performance of a specific foreign equity securities index and normally invests at least 80% in underlying-index securities or economically similar instruments. It is passive/index-tracking equity, not bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy or single-stock exposure.
- Exchange note: the current product page displays `Primary Exchange NYSE`, while the official summary prospectus and annual shareholder report identify the `Principal Listing Exchange` as `NYSE Arca`. The canonical key is therefore retained as `NYSE Arca:KBA` and the conflict is disclosed in the source batch.
- Current snapshot: NAV `US$33.32`, closing price `US$33.19`, premium/discount `-0.13%`, and 30-day median bid/ask spread `0.15%`, all as of `2026-08-27`; net assets `US$144,924,108` and shares outstanding `4,350,000` are also as of `2026-08-27`.

### Official 10-year NAV TR window

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative return | CAGR | Disclosure |
|---|---|---:|---:|---:|---:|---:|---|
| 2016-07-31 | 2026-07-31 | 10.00 | 100.00 (normalized) | approx. 182.84 (calculated) | approx. 82.84% (calculated) | 6.22% | Official current product-page 10-year NAV TR CAGR; raw start/end and cumulative rolling NAV TR not disclosed |

Normalized endpoint: `100.00 × (1 + 6.22%)^10.00 = 182.84`; this is calculated from the issuer-reported CAGR, not a raw NAV endpoint and not a proxy.

### Annual NAV Total Return

| Year | KBA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -19.37% | 11.96% |
| 2017 | 28.64% | 21.83% |
| 2018 | -26.25% | -4.38% |
| 2019 | -26.49% | 31.49% |
| 2020 | -17.10% | 18.40% |
| 2021 | 34.50% | 28.71% |
| 2022 | 2.70% | -18.11% |
| 2023 | 16.06% | 26.29% |
| 2024 | 42.39% | 25.02% |
| 2025 | not disclosed | 17.88% |
| 2026 YTD | 7.45% | not comparable; current year not cached |

The official summary prospectus discloses KBA calendar-year NAV TR rows for `2015-2024`; this page uses the complete `2016-2024` subset for the rolling-window comparison. A 2025 calendar-year KBA NAV row was not disclosed in the reviewed official materials, so it remains `not disclosed`. The latest issuer standardized table is as of `2026-07-31`; the June quarter-end table remains a separate cross-check. S&P 500 rows reuse the cached USD Total Return convention as of `2025-12-31`; market-price return is not mixed.

### Window calculations and ranking

- Official rolling 10-year window `2016-07-31` to `2026-07-31`: KBA NAV TR CAGR `6.22%`; normalized endpoint approximately `182.84`; raw endpoints not disclosed. The separate June quarter-end observation is `6.90%`.
- Complete disclosed calendar window `2016-2024`: KBA NAV TR cumulative `6.41%`, CAGR `0.69%` over 9 complete years; S&P 500 TR cumulative `237.91%`, CAGR `14.49%`; KBA trails by approximately `13.80 pp` CAGR.
- Common disclosed window `2021-2024`: KBA NAV TR cumulative `128.27%`, CAGR `22.92%`; S&P 500 TR cumulative `66.41%`, CAGR `13.58%`; KBA leads by approximately `9.34 pp` CAGR. This is a four-year window, not a five-year `2021-2025` comparison, because KBA's 2025 calendar NAV row is not disclosed.
- Up years / down years in `2016-2024`: `5 / 4`.
- Best disclosed complete year: `2024`, `42.39%`; worst disclosed complete year: `2019`, `-26.49%`.
- Current standardized NAV TR YTD: `7.45%` as of `2026-07-31`; the June quarter-end cross-check is `11.37%`. The current-year S&P 500 row is not used because the cached comparison window ends at `2025-12-31`.

## Risk read-through

KBA เป็น China A-share single-country exposure ที่มี Stock Connect/QFI access, China policy/geopolitical, currency, liquidity และ sector-concentration risk. The current index consists of 50 large-cap Shanghai/Shenzhen A-shares, while the fund may also hold cash or other tracking instruments. The fund's index and name changed over time, with the current MSCI China A 50 Connect Index adopted from `2022-01-05`; the 10-year result therefore spans earlier MSCI China A / related index methodologies. Daily NAV history sufficient for fund-level max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

## Sources

- Official KraneShares KBA product and performance page: https://kraneshares.com/etf/kba/ — current fund facts and daily NAV/price as of 2026-08-27; standardized performance as of 2026-07-31 and June quarter-end cross-check.
- Official KraneShares KBA factsheet: https://kraneshares.com/resources/factsheet/kba_factsheet.pdf
- Official KraneShares KBA summary prospectus: https://kraneshares.com/resources/compliance/2026_02_20_kba_summary.prospectus.pdf — principal listing exchange, passive strategy, index methodology, risk disclosures, and calendar rows; its fee-waiver date differs from the current product page.
- Official KraneShares KBA annual shareholder report: https://kraneshares.com/resources/compliance/2026_05_29_kba_annual.TSR.report.pdf — principal listing exchange and prior return disclosure.
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- Latest displayed distributions: `US$0.483155` payable 2025-12-23 and `US$0.511692` payable 2024-12-18; two latest payments total `US$0.994847` per share. These are distributions, not NAV TR.
- ETF source batch: [[ETF_performance_sources_2026-08-29]]
- Navigation: [[China ETF]] | [[ETF Region Index]] | [[ETF Performance Index]]
