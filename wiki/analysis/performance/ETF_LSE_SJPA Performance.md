---
type: etf-performance
instrument_type: ETF
entity_key: LSE:SJPA
ticker: SJPA
exchange: LSE
input_alias: IHREF (OTC)
fund: iShares Core MSCI Japan IMI UCITS ETF
tracked_index: MSCI Japan Investable Market Net Index (USD)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-17
price_nav_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return (USD)
tags:
  - analysis/etf-performance
  - ticker/SJPA
  - ticker/IHREF
  - geography/Japan
---

# SJPA Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

Input `IHREF` เป็น OTC alias ของ iShares Core MSCI Japan IMI UCITS ETF; issuer
ยืนยัน primary listing `SJPA` บน London Stock Exchange สำหรับ ISIN
`IE00B4L5YX21`. กองทุนเป็น passive physical equity ETF ที่ติดตาม MSCI Japan
Investable Market Net Index (USD). Official rolling 10-year NAV Total Return ณ
2026-06-30 อยู่ที่ cumulative 147.80% และ CAGR 9.50%; latest current
date-to-date NAV Total Return YTD อยู่ที่ 12.55% ณ 2026-07-17.

## Performance check

- entity_key: LSE:SJPA
- Input alias: IHREF (OTC); canonical issuer/exchange listing: SJPA (LSE)
- Inception: 2009-09-25
- Expense ratio: 0.12% Total Expense Ratio (issuer product data; exact fee as-of date not separately disclosed)
- Metric: NAV Total Return (USD); issuer states performance is on a NAV basis with gross income reinvested where applicable. Fund-expense treatment is not separately broken out in the selected performance extract.
- Tracked index (issuer benchmark): MSCI Japan Investable Market Net Index (USD)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year coverage: official rolling performance from 2016-06-30 to 2026-06-30; actual years 10.00
- Start TR value: 100.00 normalized; End TR value: 247.80 normalized, derived from official cumulative return 147.80%; raw NAV endpoints are not disclosed
- 10-year NAV TR CAGR: 9.50% issuer-reported average annual NAV Total Return
- Formula: (End TR / Start TR)^(1 / Years) - 1 = (247.80 / 100.00)^(1 / 10.00) - 1 = approximately 9.50%
- Coverage/source note: official issuer calendar rows 2021-2025 are corroborated to two decimals by the issuer factsheet; the current product page displays the same calendar series rounded to one decimal. The normalized endpoint is derived from the rounded official cumulative metric, not a proxy or market-price return.

| Year | SJPA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 0.92% | 28.71% |
| 2022 | -15.88% | -18.11% |
| 2023 | 18.86% | 26.29% |
| 2024 | 7.47% | 25.02% |
| 2025 | 25.36% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ SJPA;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31. ช่วง annual
comparison ที่เปิดเผยตรงกันคือ 2021-2025.

## Up years / Down years

- Up years / Down years: 4 / 1 ใน complete rows ที่ issuer เปิดเผย
- Best: 2025, +25.36%
- Least positive: 2021, +0.92%
- Worst: 2022, -15.88%
- Least bad down year: 2022, -15.88%
- 2021-2025 cumulative / CAGR: 35.94% / 6.33%; S&P 500 TR: 96.17% / 14.43%
- Current date-to-date YTD: 12.55% NAV as of 2026-07-17
- Standardized month-end YTD: 15.88% NAV as of 2026-06-30; kept separate from the later date-to-date observation

## Risk read-through

SJPA ให้ broad Japan exposure ครอบคลุม large-, mid- และ small-cap companies;
issuerรายงาน 955 holdings ณ 2026-07-17. กองทุนเป็น accumulating share class
และมี 3-year standard deviation 14.81% กับ equity beta 0.993 ณ 2026-06-30.
ความเสี่ยงหลักคือ Japan country/sector concentration, equity volatility และ
FX sensitivity ของนักลงทุนที่ใช้สกุลเงินอื่นนอก USD. Daily NAV history สำหรับ
คำนวณ max drawdown และ recovery: ไม่พบข้อมูลที่ยืนยันได้.

## Sources

- Official iShares product/performance page: https://www.ishares.com/uk/professional/en/products/251867/ishares-core-msci-japan-imi-ucits-etf?siteEntryPassthrough=true&switchLocale=y
- Official iShares SJPA factsheet: https://www.ishares.com/uk/individual/en/literature/fact-sheet/sjpa-ishares-core-msci-japan-imi-ucits-etf-fund-fact-sheet-en-gb.pdf
- Secondary OTC alias identity: https://stockanalysis.com/quote/otc/IHREF/ (used only to corroborate the input alias, not for performance numbers)
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-23]] | [[ETF Performance Index]]
