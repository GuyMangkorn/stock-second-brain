---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IWDA
input_ticker: IRRRF
ticker: IWDA
exchange: London Stock Exchange
fund: iShares Core MSCI World UCITS ETF U.S. Dollar (Accumulating)
tracked_index: MSCI World Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-30
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-27
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; gross income reinvested; net of ongoing charges
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IWDA
  - ticker/IRRRF
  - geography/International
---

# IRRRF / IWDA ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IRRRF เป็น OTC input alias ของ official USD listing `LSE:IWDA` ของ iShares
Core MSCI World UCITS ETF (USD Accumulating). กองทุนเป็น passive,
physical-optimized, accumulating developed-market equity ETF, TER `0.20%`,
เริ่ม share class เมื่อ 25 ก.ย. 2009 และติดตาม `MSCI World Index (Net)`.

จาก official complete calendar NAV Total Return rows ช่วง 2016-2025 ผลตอบแทน
สะสมคือ `217.74%` หรือ rounded-input CAGR `12.26%†`; ช่วง 2021-2025 สะสม
`77.99%` หรือ CAGR `5.94%`, positive/negative years `4 / 1`. ในช่วง 2016-2025
S&P 500 Total Return ซึ่งเป็น common USD reference ทำได้ `298.33%` หรือ CAGR
`14.82%`; นี่ไม่ใช่ tracked index ของ IWDA. Current official NAV TR YTD คือ
`+13.67%` ณ 27 ส.ค. 2026 และ NAV คือ `US$148.01` ณ 28 ส.ค. 2026.

## Performance check

- `entity_key: LSE:IWDA`; input card ticker: `IRRRF` (OTC alias); official USD listing: London Stock Exchange `IWDA`
- ISIN: `IE00B4L5Y983`; share-class launch: 25 ก.ย. 2009; asset class: equity
- Metric: `NAV Total Return` รวมเงินปันผลและ capital gains ที่ reinvested และหัก ongoing charges; currency USD
- Management mode: `passive-index-tracking`; structure: UCITS Ireland, physical optimized replication, accumulating
- Tracked index: `MSCI World Index (Net)`; common benchmark: `S&P 500 Total Return` (USD, dividends reinvested)
- 10-year calendar window: `2015-12-31` to `2025-12-31`, represented by ten complete official calendar returns from 2016-2025; this is not an issuer rolling-endpoint field
- Normalized TR endpoints: `100.00 → 317.74`; years `10.00`; formula `(End TR / Start TR)^(1 / Years) - 1`; CAGR `12.26%†`
- 2021-2025 IWDA compound `77.99%` / rounded-input CAGR `5.94%`; S&P 500 cache compound `96.17%` / CAGR `14.43%`
- Coverage note: official iShares factsheet rows are rounded observations; `†` marks the calculated CAGR from those displayed inputs. No secondary proxy is used.

| Year | IWDA NAV TR | MSCI World Net | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 7.73% | 7.51% | 11.96% |
| 2017 | 22.45% | 22.40% | 21.83% |
| 2018 | -8.65% | -8.71% | -4.38% |
| 2019 | 27.76% | 27.67% | 31.49% |
| 2020 | 15.95% | 15.90% | 18.40% |
| 2021 | 21.90% | 21.82% | 28.71% |
| 2022 | -18.03% | -18.14% | -18.11% |
| 2023 | 23.86% | 23.79% | 26.29% |
| 2024 | 18.70% | 18.67% | 25.02% |
| 2025 | 21.16% | 21.09% | 17.88% |

**Up years / Down years**

- Complete 2016-2025 years: `8 / 2`; 2021-2025 years: `4 / 1`
- Best: 2019, **+27.76%**; least positive: 2016, **+7.73%**
- Worst: 2022, **-18.03%**; least bad down year: 2018, **-8.65%**
- Current YTD: **+13.67% NAV**, as of **2026-08-27**
- IWDA beat the S&P 500 common reference in 2017, 2022 and 2025 (`3 / 10` complete years); this arithmetic comparison is not a manager-skill claim.

## Risk read-through

IWDA กระจาย across developed-market large-/mid-cap equities แต่ยังไวต่อ
mega-cap, country, sector, currency, foreign-market และ valuation risk. Official
portfolio data reports `1,278` holdings ณ 27 ส.ค. 2026; share-class net assets
อยู่ที่ `US$148,885,441,084` ณ 28 ส.ค. 2026. Official 3-year standard deviation
คือ `12.42%` ณ 31 ก.ค. 2026 และ beta `0.999` ณ 27 ส.ค. 2026. Accumulating
structure reinvests income rather than paying a cash distribution.

Official daily NAV Total Return series ที่เพียงพอสำหรับ maximum drawdown และ
recovery ยัง `ไม่พบข้อมูลที่ยืนยันได้`; จึงไม่แทนที่ด้วย market-price หรือ
secondary proxy. TER `0.20%` เป็น ongoing cost ที่กด tracking result เทียบกับ
MSCI World Net.

## Sources

- [iShares IWDA product and performance page](https://www.ishares.com/uk/individual/en/products/251882/ishares-msci-world-ucits-etf-acc) — official identity, USD/London listing, ISIN, launch, current NAV/YTD, holdings, net assets, benchmark, structure and risk fields
- [iShares Core MSCI World UCITS ETF factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/swda-ishares-core-msci-world-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) — official 2016-2025 NAV/index rows, return definition, TER and dated fund facts
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common USD total-return benchmark for 2016-2025
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
