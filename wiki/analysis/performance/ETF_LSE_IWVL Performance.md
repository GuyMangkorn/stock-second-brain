---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IWVL
input_ticker: ISMVF
ticker: IWVL
exchange: London Stock Exchange
fund: iShares Edge MSCI World Value Factor UCITS ETF
tracked_index: MSCI World Enhanced Value Index (Net)
benchmark: S&P 500 Total Return
issuer_benchmark: MSCI World Enhanced Value Index (Net)
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: established
management_evidence: not applicable
risk_evidence: issuer-fields
updated: 2026-09-01
performance_as_of: 2026-08-28
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-2.md
return_basis: NAV total return; accumulating share class; gross income reinvested where applicable
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/ISMVF
  - ticker/IWVL
  - geography/International
---

# ISMVF / IWVL Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

ISMVF เป็น OTC alias ของ USD listing `LSE:IWVL` ในกอง iShares Edge MSCI World
Value Factor UCITS ETF. กองเป็น passive value-factor exposure ใน developed
markets ทั่วโลก โดยใช้ physical replication และ accumulating share class.
Official NAV total return YTD อยู่ที่ `36.23%` ณ `2026-08-28`; ไม่ควรอ่านเป็น
ผลตอบแทนของ broad developed-market index เพราะ value factor อาจ underperform
ในช่วงที่ growth นำตลาด.

## Performance check

- `entity_key`: `LSE:IWVL`; input alias: `ISMVF`
- Share-class launch: `2014-10-03`; domicile: Ireland
- TER: `0.25%`
- Current official NAV: `$81.52` as of `2026-08-28`; net assets `$7,208,692,355`
- Metric: NAV Total Return in USD; accumulating share class; market-price return is separate
- Official current YTD: `36.23%` as of `2026-08-28`
- Issuer benchmark: `MSCI World Enhanced Value Index (Net)`
- Ten official rounded annual rows imply cumulative `146.88%` and CAGR `9.46%`

| Year | IWVL NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2016 | 8.14% | 11.96% |
| 2017 | 22.16% | 21.83% |
| 2018 | -13.90% | -4.38% |
| 2019 | 19.13% | 31.49% |
| 2020 | -3.93% | 18.40% |
| 2021 | 20.03% | 28.71% |
| 2022 | -9.96% | -18.11% |
| 2023 | 19.41% | 26.29% |
| 2024 | 5.25% | 25.02% |
| 2025 | 39.63% | 17.88% |

S&P 500 Total Return เป็น common USD reference ไม่ใช่ IWVL’s issuer
benchmark. Annual rows มาจาก iShares July 2026 factsheet.

## Up years / Down years

- Up years / Down years in 2016-2025: `7 / 3`
- Best displayed year: 2025, `+39.63%`
- Worst displayed year: 2018, `-13.90%`
- Rounded-input 2016-2025 cumulative return / CAGR: `146.88% / 9.46%`

## Risk read-through

The value-factor screen can create country, sector, style, and tracking
concentration relative to a broad MSCI World ex-US portfolio. Official product
data report 3-year beta `0.998` and standard deviation `16.00%` as of
`2026-07-31`, with `399` holdings in the latest snapshot. Currency, UCITS,
European listing, liquidity, and premium/discount risks remain. A fresh daily
NAV maximum drawdown and recovery period is `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [iShares official IWVL product page](https://www.ishares.com/uk/professionals/en/products/270048/ishares-msci-world-value-factor-ucits-etf?shortLocale=en_GB)
- [iShares IWVL July 2026 factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/iwvl-ishares-edge-msci-world-value-factor-ucits-etf-fund-fact-sheet-en-gb.pdf)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-2]]

