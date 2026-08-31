---
type: etf-performance
instrument_type: ETF
entity_key: TSX:VIDY
input_ticker: VEXNF
ticker: VIDY
exchange: Toronto Stock Exchange
fund: Vanguard FTSE Developed ex North America High Dividend Yield Index ETF
tracked_index: FTSE Developed ex North America High Dividend Yield Index
benchmark: S&P 500 Total Return
issuer_benchmark: FTSE Developed ex North America High Dividend Yield Index
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: established
management_evidence: not applicable
risk_evidence: issuer-fields
updated: 2026-09-01
performance_as_of: 2026-08-28
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-21
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-2.md
return_basis: CAD NAV total return; market-price return separate
return_currency: CAD
tags:
  - analysis/etf-performance
  - ticker/VEXNF
  - ticker/VIDY
  - geography/International
---

# VEXNF / VIDY Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

VEXNF เป็น OTC alias ของ Vanguard Canada’s official `TSX:VIDY` ซึ่งลงทุนใน
หุ้น developed markets นอก North America และใช้ passive full replication ของ
FTSE Developed ex North America High Dividend Yield Index. Official CAD NAV
ล่าสุดอยู่ที่ `$48.3366` ณ `2026-08-28`; current YTD ที่หาได้เป็น secondary
proxy `19.37%*` ณ `2026-08-21` เพราะ Vanguard page ไม่แสดง YTD ใน text capture.

## Performance check

- `entity_key`: `TSX:VIDY`; input alias: `VEXNF`
- Inception date: `2018-08-21`; asset class: equity; quarterly distributions
- Management fee: `0.28%`; official ETF Facts MER `0.32%` (page also displays RFG/MER `0.31%` under a different/current presentation)
- Current official NAV: `CAD $48.3366` as of `2026-08-28`; market price `CAD $48.45`
- Official ETF Facts since-inception annual compound return: `11.89%` through `2026-05-31`; `$1,000` grew to `$2,395`
- Current YTD: `19.37%*` as of `2026-08-21` from Cboe Canada/ETF Market; official current YTD is `ไม่พบข้อมูลที่ยืนยันได้` in the captured Vanguard page
- Issuer benchmark: `FTSE Developed ex North America High Dividend Yield Index`
- Complete official 2019-2025 rows imply cumulative `127.00%` and rounded-input CAGR `12.42%`

| Year | VIDY NAV TR (CAD) | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2019 | 12.3% | 31.49% |
| 2020 | -2.9% | 18.40% |
| 2021 | 14.0% | 28.71% |
| 2022 | 1.6% | -18.11% |
| 2023 | 15.1% | 26.29% |
| 2024 | 16.1% | 25.02% |
| 2025 | 34.5% | 17.88% |

S&P 500 Total Return เป็น USD common reference เท่านั้น ไม่ใช่ issuer
benchmark และไม่ใช่ currency-aligned comparison กับ CAD VIDY returns.

## Up years / Down years

- Up years / Down years in the complete 2019-2025 window: `6 / 1`
- Best displayed year: 2025, `+34.5%`
- Worst displayed year: 2020, `-2.9%`
- Rounded-input 2019-2025 cumulative return / CAGR: `127.00% / 12.42%`
- Official since-inception annual compound return: `11.89%` through `2026-05-31`

## Risk read-through

The high-dividend screen can tilt country and sector exposure away from a broad
developed-market index; CAD returns also embed the investor’s FX experience.
Official product data as of `2026-07-31` report beta `1.00`, R-squared `1.00`,
standard deviation `9.23%`, and `629` stocks. A fresh daily-NAV maximum drawdown
and recovery period is `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Vanguard Canada official VIDY product page](https://www.vanguard.ca/fr/product/etf/equity/9742/vanguard-ftse-developed-ex-north-america-high-dividend-yield-index-etf)
- [Vanguard VIDY official ETF Facts](https://fund-docs.vanguard.com/VIDY_FTSE_Developed_ex_North_America_High_Dividend_Yield_Index_ETF_ETF_9742_EN_FACTS.pdf)
- [Cboe Canada / ETF Market VIDY data](https://etfmarket.cboe.com/canada/en/fund/VIDY)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-2]]

