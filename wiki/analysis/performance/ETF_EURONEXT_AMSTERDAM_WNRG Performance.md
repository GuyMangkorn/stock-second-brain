---
type: etf-performance
instrument_type: ETF
entity_key: Euronext Amsterdam:WNRG
input_ticker: SMWFF
input_alias: SMWFF
ticker: WNRG
exchange: Euronext Amsterdam
fund: State Street SPDR MSCI World Energy UCITS ETF
tracked_index: MSCI World Energy 35/20 Capped Index
benchmark: S&P 500 Total Return
issuer_benchmark: MSCI World Energy 35/20 Capped Index
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
  - ticker/SMWFF
  - ticker/WNRG
  - geography/International
  - geography/global-developed
---

# SMWFF / WNRG Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

SMWFF เป็น OTC alias ของ primary Euronext Amsterdam listing `WNRG` ใน State
Street SPDR MSCI World Energy UCITS ETF. กองทุนเป็น passive, accumulating,
global developed-market energy equity ETF โดยใช้ USD NAV Total Return เป็นฐาน
หลัก แม้ primary listing ซื้อขายเป็น EUR. Official rolling 10-year NAV TR
annualized อยู่ที่ `9.57%` และ current YTD อยู่ที่ `33.61%` ณ `2026-07-31`;
ช่วง complete 2017-2025 ให้ CAGR `5.92%` เทียบ S&P 500 TR `15.14%`, แต่ช่วง
2021-2025 ให้ CAGR `19.81%` เทียบ `14.43%` เนื่องจาก energy-cycle exposure สูง.

## Performance check

- `entity_key`: `Euronext Amsterdam:WNRG`; input alias: `SMWFF`; primary listing: Euronext Amsterdam `WNRG`
- ISIN: `IE00BYTRR863`; fund inception `2016-04-29`; linked performance history begins `2009-01-31`
- TER: `0.30%`; accumulating; base/share-class currency USD; replicated structure
- Current official NAV: `$78.07` as of `2026-08-31`; AUM `$574.72M`; 52 holdings as of `2026-08-31`
- Metric: `NAV Total Return` net of fund fees, with income reinvested through the accumulating share class; market-price return is separate
- Issuer benchmark: `MSCI World Energy 35/20 Capped Index`; linked index history uses MSCI World Energy Index through `2020-11-30` and the capped index thereafter
- Official rolling 10-year NAV TR: `9.57%` annualized, cumulative `149.29%`, as of `2026-07-31`; raw endpoint levels are `not disclosed` in the retrieved issuer table
- Current official NAV TR YTD: `33.61%` as of `2026-07-31`; the `2026-08-31` NAV level is a separate current price/NAV observation
- Coverage/source note: official State Street calendar rows are shown for 2016-2025; `†` marks the predecessor-linked/inception-year context row and it is excluded from complete-year ranking. S&P 500 TR uses the cached USD dividend-reinvested convention for 2016-2025.

| Year | WNRG NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2016 | 26.33%† | 11.96% |
| 2017 | 5.24% | 21.83% |
| 2018 | -15.80% | -4.38% |
| 2019 | 11.37% | 31.49% |
| 2020 | -31.10% | 18.40% |
| 2021 | 40.49% | 28.71% |
| 2022 | 46.31% | -18.11% |
| 2023 | 2.79% | 26.29% |
| 2024 | 2.88% | 25.02% |
| 2025 | 13.56% | 17.88% |

## Up years / Down years

- Complete 2017-2025 window: `7 / 2` up/down years
- Best complete year: 2022, `+46.31%`
- Least positive: 2023, `+2.79%`
- Worst complete year: 2020, `-31.10%`
- Least bad down year: 2018, `-15.80%`
- Complete 2017-2025 cumulative return / rounded-input CAGR: `67.84% / 5.92%`
- Complete 2021-2025 cumulative return / rounded-input CAGR: `146.85% / 19.81%`
- Current official NAV TR YTD: `+33.61%` as of `2026-07-31`; no same-date current S&P 500 TR observation is asserted.

`†` The fund launched on 29 April 2016 after a merger by absorption; State Street
states that returns before May 2016 reflect the predecessor SSGA Energy Index
Equity Fund I USD Shares. The row is retained for context, not treated as a
full live-ETF year.

## Risk read-through

WNRG เป็น sector-concentrated energy ETF: State Street reports `94.03%` in Oil,
Gas & Consumable Fuels and `5.97%` in Energy Equipment & Services as of
`2026-08-31`. Issuer-reported 3-year standard deviation is `18.06%` and
tracking error `0.08%` as of `2026-07-31`; concentration, commodity-price,
geopolitical, country, currency and large-cap energy risks can make the path
materially different from a broad-market ETF. Official daily NAV history
sufficient for maximum drawdown and recovery was not verified, so those values
remain `ไม่พบข้อมูลที่ยืนยันได้`. The 10-year figure is issuer annualized NAV TR;
it should not be mixed with the EUR market-price line.

## Sources

- [State Street official WNRG product page](https://www.ssga.com/ie/en_gb/institutional/etfs/state-street-spdr-msci-world-energy-ucits-etf-wnrg-na) — identity, primary listing, current NAV/AUM/holdings, fund facts and official performance table; observations through `2026-09-01`
- [State Street WNRG factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-wnrg-na.pdf) — USD share class, inception, TER, linked-index note, calendar and rolling NAV TR fields; performance as of `2026-07-31`
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references and calculation convention: [[ETF_performance_sources_2026-09-02_run-4]]
