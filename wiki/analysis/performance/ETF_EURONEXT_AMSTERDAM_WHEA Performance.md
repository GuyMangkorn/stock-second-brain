---
type: etf-performance
instrument_type: ETF
entity_key: Euronext Amsterdam:WHEA
input_ticker: SWOOF
input_alias: SWOOF
ticker: WHEA
exchange: Euronext Amsterdam
fund: State Street SPDR MSCI World Health Care UCITS ETF
tracked_index: MSCI World Health Care 35/20 Capped Index
benchmark: S&P 500 Total Return
issuer_benchmark: MSCI World Health Care 35/20 Capped Index
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: linked-predecessor-history
management_evidence: not applicable
risk_evidence: issuer-fields
updated: 2026-09-02
performance_as_of: 2026-07-31
calendar_years_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-31
fund_facts_as_of: 2026-09-01
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-4.md
return_basis: USD NAV net total return; accumulating share class; EUR listing price separate
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SWOOF
  - ticker/WHEA
  - geography/International
  - geography/global-developed
---

# SWOOF / WHEA Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

SWOOF เป็น OTC alias ของ primary Euronext Amsterdam listing `WHEA` ใน State
Street SPDR MSCI World Health Care UCITS ETF. กองทุนเป็น passive, accumulating,
global developed-market health-care equity ETF โดยใช้ USD NAV Total Return เป็น
ฐานหลัก แม้ primary listing ซื้อขายเป็น EUR. Official rolling 10-year NAV TR
annualized อยู่ที่ `8.10%` และ current YTD อยู่ที่ `3.29%` ณ `2026-07-31`;
ช่วง complete 2017-2025 ให้ CAGR `9.83%` เทียบ S&P 500 TR `15.14%`, ขณะที่ช่วง
2021-2025 ให้ CAGR `6.30%` เทียบ `14.43%` เนื่องจาก health-care sector
exposure และช่วงอ่อนตัวในปี 2022.

## Performance check

- `entity_key`: `Euronext Amsterdam:WHEA`; input alias: `SWOOF`; primary listing: Euronext Amsterdam `WHEA`
- ISIN: `IE00BYTRRB94`; fund inception `2016-04-29`; linked performance history begins `2009-02-28`
- TER: `0.30%`; accumulating; base/share-class currency USD; replicated structure
- Current official NAV: `$72.38` as of `2026-08-31`; EUR closing price `€62.31`; AUM `$707.92M`; 113 holdings as of `2026-08-31`
- Metric: `NAV Total Return` net of fund fees, with income reinvested through the accumulating share class; market-price return is separate
- Issuer benchmark: `MSCI World Health Care 35/20 Capped Index`; linked index history uses MSCI World Health Care Index through `2020-11-30` and the capped index thereafter
- Official rolling 10-year NAV TR: `8.10%` annualized, cumulative `117.79%`, as of `2026-07-31`; raw endpoint levels are `not disclosed` in the retrieved issuer table
- Current official NAV TR YTD: `3.29%` as of `2026-07-31`; the `2026-08-31` NAV and EUR closing price are separate current observations
- Coverage/source note: official State Street calendar rows are shown for 2016-2025; `†` marks the predecessor-linked/inception-year context row and it is excluded from complete-year ranking. S&P 500 TR uses the cached USD dividend-reinvested convention for 2016-2025.

| Year | WHEA NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2016 | -6.89%† | 11.96% |
| 2017 | 19.69% | 21.83% |
| 2018 | 2.48% | -4.38% |
| 2019 | 23.34% | 31.49% |
| 2020 | 13.26% | 18.40% |
| 2021 | 19.59% | 28.71% |
| 2022 | -5.56% | -18.11% |
| 2023 | 3.63% | 26.29% |
| 2024 | 1.02% | 25.02% |
| 2025 | 14.78% | 17.88% |

## Up years / Down years

- Complete 2017-2025 window: `8 / 1` up/down years
- Best complete year: 2019, `+23.34%`
- Least positive: 2024, `+1.02%`
- Worst complete year: 2022, `-5.56%`
- Complete 2017-2025 cumulative return / rounded-input CAGR: `132.53% / 9.83%`
- Complete 2021-2025 cumulative return / rounded-input CAGR: `35.71% / 6.30%`
- Current official NAV TR YTD: `+3.29%` as of `2026-07-31`; no same-date current S&P 500 TR observation is asserted.

`†` The fund launched on 29 April 2016 following a merger by absorption; State
Street states that returns before May 2016 reflect the predecessor SSGA Health
Care Index Equity Fund I USD Shares. The row is retained for context, not
treated as a full live-ETF year.

## Risk read-through

WHEA เป็น sector-concentrated health-care ETF: State Street reports current
industry allocation ณ `2026-08-31` เป็น Pharmaceuticals `46.76%`, Biotechnology
`17.27%`, Health Care Equipment & Supplies `14.69%`, Health Care Providers &
Services `12.92%`, Life Sciences Tools & Services `7.78%` และ Health Care
Technology `0.57%`. Issuer-reported 3-year standard deviation is `13.03%` and
tracking error `0.04%` as of `2026-07-31`; pharmaceutical, biotechnology,
regulatory, clinical and country/currency risks can make the path materially
different from a broad-market ETF. Official daily NAV history sufficient for
maximum drawdown and recovery was not verified, so those values remain
`ไม่พบข้อมูลที่ยืนยันได้`. The 10-year figure is issuer annualized NAV TR; it
should not be mixed with the EUR market-price line.

## Sources

- [State Street official WHEA product page](https://www.ssga.com/nl/en_gb/institutional/etfs/state-street-spdr-msci-world-health-care-ucits-etf-whea-na) — identity, primary listing, current NAV/AUM/holdings, fund facts, industry allocation and official performance table; observations through `2026-09-01`
- [State Street WHEA factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-whea-na.pdf) — USD share class, inception, TER, linked-index note, calendar and rolling NAV TR fields; performance as of `2026-07-31`
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references and calculation convention: [[ETF_performance_sources_2026-09-02_run-4]]
