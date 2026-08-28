---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWS
ticker: EWS
exchange: NYSE Arca
fund: iShares MSCI Singapore ETF
tracked_index: MSCI Singapore 25/50 Index
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-08-25
current_nav_as_of: 2026-08-26
fund_facts_as_of: 2026-08-26
risk_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWS
  - geography/Singapore
---

# EWS Performance

> Navigation: [[ETF Region Index]] → [[Singapore ETF]] → [[ETF Performance Index]]

## Bottom line

EWS เป็น passive/index-tracking Singapore equity ETF ของ iShares ติดตาม `MSCI Singapore 25/50 Index` และเริ่มกองทุนเมื่อ 1996-03-12. Official rolling 10-year NAV Total Return ณ 2026-06-30 รายงาน cumulative `112.54%` และ CAGR `7.83%` สำหรับช่วง 2016-06-30 ถึง 2026-06-30 ครบ `10.00` ปี; raw NAV endpoints ไม่ได้เปิดเผย จึงใช้ normalized endpoint `212.54` จาก cumulative return ที่ issuer เปิดเผย. Current NAV TR YTD ล่าสุดที่พบคือ `26.53%` ณ 2026-08-25 และ NAV อยู่ที่ `USD 34.12` ณ 2026-08-26.

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
| 2016 | 1.10% | 1.50% | 11.96% |
| 2017 | 33.80% | 34.30% | 21.83% |
| 2018 | -11.00% | -10.40% | -4.38% |
| 2019 | 13.90% | 14.30% | 31.49% |
| 2020 | -8.20% | -7.70% | 18.40% |
| 2021 | 5.22% | 5.65% | 28.71% |
| 2022 | -9.15% | -8.76% | -18.11% |
| 2023 | 5.27% | 6.10% | 26.29% |
| 2024 | 22.53% | 23.15% | 25.02% |
| 2025 | 31.56% | 32.17% | 17.88% |
| 2026 YTD | 26.53% | not disclosed | not comparable; current year not cached |

The official BlackRock/iShares product page exposes annual Fund NAV and issuer-index rows for `2016-2025`; the `2016-2020` rows are displayed to one decimal place, while the current factsheet gives more precise `2021-2025` rows. The benchmark changed to `MSCI Singapore 25/50 Index (Net)` on `2016-12-01`; pre-change benchmark history remains separately labelled. Current YTD is as of `2026-08-25`.

### Window calculations and ranking

- Official rolling 10-year window `2016-06-30` to `2026-06-30`: EWS cumulative `112.54%`, CAGR `7.83%`; issuer benchmark cumulative `123.40%`, CAGR `8.37%`; raw NAV endpoints not disclosed.
- Common disclosed calendar window `2021-2025`: EWS NAV TR cumulative `62.22%`, CAGR `10.16%`; MSCI Singapore 25/50 Index cumulative `67.32%`, CAGR `10.83%`; S&P 500 TR cumulative `96.17%`, CAGR `14.43%`; EWS trails S&P by approximately `4.27 pp` CAGR.
- Up years / down years in `2021-2025`: `4 / 1`.
- Best disclosed year: `2025`, `31.56%`; least positive: `2021`, `5.22%`.
- Worst disclosed year: `2022`, `-9.15%`; least bad down year: `2022`, `-9.15%`.
- Rounded-input calendar `2016-2025` CAGR is `7.40%`; this is separate from the issuer's rolling 10-year CAGR because the early annual rows are rounded to one decimal place.
- Current NAV TR YTD: `26.53%` as of `2026-08-25`; NAV `USD 34.12` as of `2026-08-26`.

## Risk read-through

EWS เป็น Singapore single-country equity exposure. iShares reports net assets `$1.20B`, 17 holdings and NAV `USD 34.12` as of `2026-08-26`; the latest detailed sector snapshot as of `2026-08-12` was Financials `54.43%`, Industrials `20.51%`, Real Estate `7.91%`, and Consumer Discretionary `5.64%`. The 3-year standard deviation was `12.34%` as of `2026-07-31`; expense ratio is `0.50%`. Singapore country concentration, financials/industrial/real-estate exposure, currency and regional trade sensitivity can increase volatility. Daily NAV history sufficient for fund-level max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

## Sources

- Official iShares EWS product page: https://www.ishares.com/us/products/239678/ishares-msci-singapore-capped-etf
- Official BlackRock/iShares EWS performance and facts page: https://www.blackrock.com/il/intermediaries/en/products/239678/ishares-msci-singapore-etf
- Official iShares EWS factsheet: https://www.ishares.com/us/literature/fact-sheet/ews-ishares-msci-singapore-etf-fund-fact-sheet-en-us.pdf
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-29]]
- Navigation: [[Singapore ETF]] | [[ETF Region Index]] | [[ETF Performance Index]]
