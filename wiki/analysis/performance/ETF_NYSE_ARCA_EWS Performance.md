---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWS
ticker: EWS
exchange: NYSE Arca
fund: iShares MSCI Singapore ETF
tracked_index: MSCI Singapore 25/50 Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWS
  - geography/Singapore
---

# EWS Performance

> Navigation: [[ETF Region Index]] → [[Singapore ETF]] → [[ETF Performance Index]]

## Bottom line

EWS เป็น passive/index-tracking Singapore equity ETF ของ iShares ติดตาม `MSCI Singapore 25/50 Index` และเริ่มกองทุนเมื่อ 1996-03-12. Official rolling 10-year NAV Total Return ณ 2026-06-30 รายงาน cumulative `112.54%` และ CAGR `7.83%` สำหรับช่วง 2016-06-30 ถึง 2026-06-30 ครบ `10.00` ปี; raw NAV endpoints ไม่ได้เปิดเผย จึงใช้ normalized endpoint `212.54` จาก cumulative return ที่ issuer เปิดเผย. Current NAV TR YTD คือ `16.50%` ณ 2026-07-21.

## Performance check

- `entity_key`: `NYSE Arca:EWS`
- Fund: iShares MSCI Singapore ETF; asset class `Equity`; expense ratio `0.50%`
- Inception: `1996-03-12`
- Metric: official NAV Total Return, รวม reinvested distributions และ fund expenses ตาม iShares performance disclosure
- Issuer benchmark: MSCI Singapore 25/50 Index; current product page reports benchmark 10-year NAV/benchmark returns separately
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not issuer benchmark)
- Type note: iShares states EWS seeks to track an index composed of Singaporean equities; it is passive/index-tracking single-country equity, not bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy or single-stock exposure.

### Official 10-year NAV TR window

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative return | CAGR | Disclosure |
|---|---|---:|---:|---:|---:|---:|---|
| 2016-06-30 | 2026-06-30 | 10.00 | 100.00 (normalized) | 212.54 (from official cumulative return) | 112.54% | 7.83% | Raw NAV start/end values not disclosed |

Normalized endpoint `212.54` is `100.00 × (1 + 112.54%)`, derived from the official iShares cumulative NAV Total Return; it is not a proxy.

### Annual NAV Total Return

| Year | EWS NAV TR | MSCI Singapore 25/50 Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | 5.22% | 5.65% | 28.71% |
| 2022 | -9.15% | -8.76% | -18.11% |
| 2023 | 5.27% | 6.10% | 26.29% |
| 2024 | 22.53% | 23.15% | 25.02% |
| 2025 | 31.56% | 32.17% | 17.88% |
| 2026 YTD | 16.50% | not disclosed | not comparable; current year not cached |

The official iShares capture discloses Fund NAV and benchmark annual rows for `2021-2025`; `2016-2020` Fund NAV rows are not disclosed in the reviewed current materials. The benchmark change to `MSCI Singapore 25/50 Index (Net)` occurred on `2016-12-01`; benchmark rows remain separate from the NAV TR metric. Current YTD is as of `2026-07-21`.

### Window calculations and ranking

- Official rolling 10-year window `2016-06-30` to `2026-06-30`: EWS cumulative `112.54%`, CAGR `7.83%`; issuer benchmark cumulative `123.40%`, CAGR `8.37%`; raw NAV endpoints not disclosed.
- Common disclosed calendar window `2021-2025`: EWS NAV TR cumulative `62.22%`, CAGR `10.16%`; MSCI Singapore 25/50 Index cumulative `67.32%`, CAGR `10.83%`; S&P 500 TR cumulative `96.17%`, CAGR `14.43%`; EWS trails S&P by approximately `4.27 pp` CAGR.
- Up years / down years in `2021-2025`: `4 / 1`.
- Best disclosed year: `2025`, `31.56%`; least positive: `2021`, `5.22%`.
- Worst disclosed year: `2022`, `-9.15%`; least bad down year: `2022`, `-9.15%`.
- Current NAV TR YTD: `16.50%` as of `2026-07-21`.

## Risk read-through

EWS เป็น Singapore single-country equity exposure. iShares reports net assets about `$1.01B` as of `2026-07-20/21`, `0.50%` expense ratio, and sector exposure as of `2026-07-21` of Financials `54.64%`, Industrials `21.01%`, Real Estate `8.29%`, and Cash/Derivatives `0.21%`. Singapore country concentration, financials/industrial/real-estate exposure, currency and regional trade sensitivity can increase volatility. Daily NAV history sufficient for fund-level max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

## Sources

- Official iShares EWS product page: https://www.ishares.com/us/products/239678/ishares-msci-singapore-capped-etf
- Official iShares EWS factsheet: https://www.ishares.com/us/literature/fact-sheet/ews-ishares-msci-singapore-etf-fund-fact-sheet-en-us.pdf
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]]
- Navigation: [[Singapore ETF]] | [[ETF Region Index]] | [[ETF Performance Index]]
