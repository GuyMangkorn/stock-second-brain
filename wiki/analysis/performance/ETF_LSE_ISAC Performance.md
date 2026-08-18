---
type: etf-performance
instrument_type: ETF
entity_key: LSE:ISAC
input_ticker: ISACF
ticker: ISAC
exchange: London Stock Exchange
fund: iShares MSCI ACWI UCITS ETF U.S. Dollar (Accumulating)
tracked_index: MSCI All Country World Index (Net)
benchmark: MSCI All Country World Index (Net)
management_mode: passive-index-tracking
updated: 2026-08-19
performance_as_of: 2025-12-31
rolling_performance_as_of: 2026-07-31
current_ytd_as_of: 2026-08-17
price_nav_as_of: 2026-08-17
fund_facts_as_of: 2026-08-17
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; gross income reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/ISAC
  - ticker/ISACF
  - geography/International
---

# ISACF / ISAC ETF Performance

> [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

ISACF เป็น OTC input alias ที่ resolve ด้วย ISIN IE00B6R52259 ไปยัง official
USD listing LSE:ISAC ของ iShares MSCI ACWI UCITS ETF (USD Accumulating).
กองทุนเป็น passive physical optimized, accumulating, TER 0.20%, เปิดตัว
share class เมื่อ 21 Oct 2011 และติดตาม MSCI All Country World Index (Net)
ซึ่งครอบคลุม developed และ emerging markets.

จาก official annual NAV Total Return rows ที่ครบ 2016-2025 ผลตอบแทนสะสมคือ
201.54% และ rounded-input calendar CAGR คือ 11.67%†; ใน common window
2021-2025 ผลตอบแทนสะสมคือ 70.69% หรือ CAGR 11.29%, positive/negative
years 4/1. Current official product page รายงาน NAV TR YTD 15.06% และ
NAV USD 124.95 ณ 2026-08-17. Official July factsheet รายงาน YTD 11.42%
ณ 2026-07-31; ตัวเลขสองชุดเป็นคนละ as-of snapshot ไม่ใช่ source conflict.

† เป็น CAGR ที่คำนวณจาก rounded official calendar rows ไม่ใช่ issuer
rolling 10-year field. กองทุนจึงเหมาะเป็น broad global equity core ในเชิง
suitability เท่านั้น; ผลลัพธ์ยังไวต่อ global mega-cap, country/sector mix,
emerging-market, FX, liquidity และ counterparty risks.

## Identity and structure

| Field | Verified value |
|---|---|
| Input ticker | ISACF |
| Official listing | LSE:ISAC, London Stock Exchange, USD line |
| ISIN | IE00B6R52259 |
| Fund | iShares MSCI ACWI UCITS ETF (USD Accumulating) |
| Share-class launch | 2011-10-21 |
| Structure | UCITS; Ireland; physical optimized replication |
| Management mode | Passive index-tracking |
| Benchmark | MSCI All Country World Index (Net) |
| TER | 0.20% |
| Accumulation | Accumulating share class; income reinvested in NAV total return |
| Latest product-page NAV | USD 124.95 as of 2026-08-17 |
| Holdings | 1,693 as of 2026-08-17; July factsheet 1,695 as of 2026-07-31 |
| Return currency | USD |

## Official calendar performance

Official iShares July factsheet reports Share Class NAV Total Return and the
MSCI ACWI Net benchmark in USD. The table preserves the issuer's rounded
annual observations; calculations use these displayed inputs.

| Year | ISAC NAV TR | MSCI ACWI Net |
|---|---:|---:|
| 2016 | 7.82% | 7.86% |
| 2017 | 23.94% | 23.97% |
| 2018 | -9.52% | -9.41% |
| 2019 | 26.37% | 26.60% |
| 2020 | 15.62% | 16.25% |
| 2021 | 18.71% | 18.54% |
| 2022 | -18.19% | -18.36% |
| 2023 | 22.35% | 22.20% |
| 2024 | 17.35% | 17.49% |
| 2025 | 22.41% | 22.34% |

### Calculated windows

| Window / metric | ISAC | Official benchmark |
|---|---:|---:|
| 2016-2025 cumulative | 201.54% | not calculated for index in this page |
| 2016-2025 rounded-input CAGR | 11.67%† | not calculated for index in this page |
| 2021-2025 cumulative | 70.69% | 69.98% |
| 2021-2025 rounded-input CAGR | 11.29% | 11.19% |
| 2021-2025 annual-return standard deviation, population | 15.49% | not calculated |
| Positive / negative years, 2021-2025 | 4 / 1 | 4 / 1 |
| Best / worst year, 2021-2025 | 2025 +22.41% / 2022 -18.19% | 2025 +22.34% / 2022 -18.36% |

## Current and rolling official fields

As-of dates are intentionally separate because the product page is more
current than the July factsheet.

| Metric | Value | As of | Basis |
|---|---:|---|---|
| Current NAV TR YTD | 15.06% | 2026-08-17 | official product page |
| NAV | USD 124.95 | 2026-08-17 | official product page |
| Factsheet YTD | 11.42% | 2026-07-31 | official July factsheet |
| 1-year NAV TR | 22.22% | 2026-07-31 | official July factsheet |
| 3-year annualized NAV TR | 18.33% | 2026-07-31 | official July factsheet |
| 5-year annualized NAV TR | 10.95% | 2026-07-31 | official July factsheet |
| Since-inception annualized NAV TR | 11.17% | 2026-07-31 | official July factsheet |
| 3-year standard deviation | 12.61% | 2026-07-31 | official product page |
| 3-year beta | 0.998 | 2026-07-31 | official product page |

## Benchmark tracking and common reference

Fund-minus-benchmark observations from the official displayed rows are
+0.17, +0.17, +0.15, -0.14, and +0.07 percentage points for 2021-2025.
These are passive tracking observations after fees and rounding; they are not
labeled alpha or manager skill.

The cached S&P 500 Total Return convention is retained only as a common USD
reference: 2021 28.71%, 2022 -18.11%, 2023 26.29%, 2024 25.02%, and
2025 17.88%, compounding to 96.17% or CAGR 14.43%. It is not the
strategy-appropriate benchmark for this fund and is not used to infer skill.

## Risk read-through

The official product page identifies global equity, country and sector
concentration, emerging-market, currency, liquidity and counterparty risks.
The official 3-year standard deviation is 12.61% and beta is 0.998 as of
2026-07-31. The fund held 1,693 positions on the product-page snapshot and
1,695 on the July factsheet snapshot; the count difference is date-related.
Official daily NAV maximum drawdown and recovery date were not disclosed in the
reviewed sources.

## Sources

- [iShares product page](https://www.ishares.com/uk/individual/en/products/251850/ishares-msci-acwi-ucits-etf) — official identity, LSE USD listing, ISIN, launch, current NAV/YTD, holdings, benchmark and risk fields.
- [iShares July 2026 factsheet](https://www.ishares.com/nl/particuliere-belegger/nl/literature/fact-sheet/ssac-ishares-msci-acwi-ucits-etf-fund-fact-sheet-en-nl.pdf?siteEntryPassthrough=true&switchLocale=y) — official annual NAV/benchmark rows, rolling performance, TER, holdings and dated fund facts as of 2026-07-31.
- [[ETF_performance_sources_2026-08-19]] — source map, raw observations, calculations, reconciliation and scheduled-local verification record.

## Follow-up

- Refresh current NAV/YTD using the official product page on the next run; preserve the July factsheet snapshot as historical evidence.
- Verify official daily NAV drawdown/recovery if iShares publishes a suitable dated series.
- Keep the official MSCI ACWI Net benchmark separate from the cached S&P 500 common reference.
