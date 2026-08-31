---
type: etf-performance
instrument_type: ETF
entity_key: Euronext Amsterdam:WTCH
input_ticker: WTTHF
ticker: WTCH
exchange: Euronext Amsterdam
fund: State Street SPDR MSCI World Technology UCITS ETF
tracked_index: MSCI World Information Technology 35/20 Capped Index
benchmark: S&P 500 Total Return
issuer_benchmark: MSCI World Information Technology 35/20 Capped Index
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: linked-predecessor-history
management_evidence: not applicable
risk_evidence: issuer-fields
updated: 2026-09-01
performance_as_of: 2026-07-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-2.md
return_basis: USD NAV net total return; accumulating share class; EUR listing price separate
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/WTTHF
  - ticker/WTCH
  - geography/International
---

# WTTHF / WTCH Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

WTTHF เป็น OTC alias ของ primary Euronext Amsterdam listing `WTCH` ใน State
Street SPDR MSCI World Technology UCITS ETF. กองเป็น passive, accumulating,
global developed-market technology exposure โดยใช้ USD NAV total return เป็น
ฐานหลัก แม้ listing จะซื้อขายเป็น EUR. Official NAV TR ให้ YTD `16.31%` และ
10-year annualized `22.73%` ณ `2026-07-31`; ตัวเลขสูงมาพร้อม sector
concentration และ volatility ที่สูงกว่ากอง developed-market broad market.

## Performance check

- `entity_key`: `Euronext Amsterdam:WTCH`; input alias: `WTTHF`
- ISIN: `IE00BYTRRD19`; fund inception `2016-04-29`; linked performance inception `2009-02-28`
- TER: `0.30%`; accumulating; base currency USD
- Current official NAV: `$271.16` as of `2026-08-28`; AUM `$1,239.66M`; 135 holdings as of `2026-08-27`
- Official net NAV TR as of `2026-07-31`: YTD `16.31%`; 1-year `27.07%`; 3-year annualized `26.94%`; 5-year `17.45%`; 10-year `22.73%`; since performance inception `20.55%`
- Issuer benchmark: `MSCI World Information Technology 35/20 Capped Index`
- Complete live/official rows 2017-2025 imply cumulative `536.70%` and rounded-input CAGR `22.84%`

| Year | WTCH NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2016 | 11.30%† | 11.96% |
| 2017 | 37.94% | 21.83% |
| 2018 | -2.74% | -4.38% |
| 2019 | 47.39% | 31.49% |
| 2020 | 43.31% | 18.40% |
| 2021 | 29.62% | 28.71% |
| 2022 | -30.85% | -18.11% |
| 2023 | 53.34% | 26.29% |
| 2024 | 32.71% | 25.02% |
| 2025 | 23.18% | 17.88% |

`†` State Street links pre-May 2016 performance to a predecessor fund, so the
2016 row is context rather than a full live-ETF year. S&P 500 Total Return is
only a common USD reference, not WTCH’s issuer benchmark.

## Up years / Down years

- Up years / Down years in the complete 2017-2025 window: `7 / 2`
- Best displayed complete year: 2023, `+53.34%`
- Worst displayed complete year: 2022, `-30.85%`
- Rounded-input 2017-2025 cumulative return / CAGR: `536.70% / 22.84%`
- Official rolling 10-year NAV CAGR: `22.73%` as of `2026-07-31`

## Risk read-through

Technology-sector and issuer concentration can make WTCH materially more
volatile than a broad developed-market ETF. Official data report 3-year
standard deviation `21.61%` and tracking error `0.08%` as of `2026-07-31`; the
latest holdings count is `135`. USD NAV returns should not be compared directly
with a EUR market-price return without FX alignment. A fresh daily-NAV maximum
drawdown and recovery period is `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [State Street official WTCH product page](https://www.ssga.com/uk/en_gb/institutional/etfs/state-street-spdr-msci-world-technology-ucits-etf-wtch-na)
- [State Street WTCH factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-wtch-na.pdf)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-2]]

