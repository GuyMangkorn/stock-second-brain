---
type: etf-performance
instrument_type: ETF
entity_key: LSE:WSML
ticker: WSML
input_ticker: IMWSF
input_alias: IMWSF
exchange: London Stock Exchange
fund: iShares MSCI World Small Cap UCITS ETF
tracked_index: MSCI World Small Cap Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-09-02
performance_as_of: 2026-08-28
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-28
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-1.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/WSML
  - ticker/IMWSF
  - geography/International
  - geography/global-developed
---

# IMWSF / WSML Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

WSML เป็น official USD London Stock Exchange line ของ iShares MSCI World Small
Cap UCITS ETF; `IMWSF` เป็น legacy OTC alias ของ share class เดียวกัน. กองทุนเป็น
passive, physical, accumulating global developed small-cap equity ETF. กองทุนเริ่ม
เมื่อ 27 มี.ค. 2018 จึงยังมีประวัติไม่ครบ 10 ปี.
Official complete calendar-year NAV Total Return 2019-2025 compound เป็น
`105.92%` หรือ rounded-input CAGR `10.87%`, เทียบกับ S&P 500 TR `205.41%` /
`17.29%`. ช่วง 2021-2025 WSML ทำ CAGR `7.17%` เทียบกับ S&P 500 `14.43%`;
latest official NAV TR YTD คือ `+17.53%` ณ 28 ส.ค. 2026.

## Performance check

- `entity_key: LSE:WSML`; input card ticker: `WSML`; legacy OTC alias: `IMWSF`; official USD listing: London Stock Exchange `WSML`
- Classification: supported passive/index-tracking global developed-markets small-cap equity UCITS ETF
- ISIN `IE00BF4RFH31`; inception: 27 มี.ค. 2018; total expense ratio `0.35%`; income treatment: accumulating; replication: physical/optimised
- Metric: `NAV Total Return` on NAV basis with gross income reinvested where applicable; currency USD
- Tracked index (issuer benchmark): `MSCI World Small Cap Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของกองทุน)
- 10-year NAV TR: `not applicable (<10y history)`; 2018 inception-year row is not disclosed and is not treated as a complete calendar year
- 2019-2025 calendar NAV TR: cumulative `105.92%`; rounded-input CAGR `10.87%`
- 2021-2025 calendar NAV TR: cumulative `41.39%`; rounded-input CAGR `7.17%`
- Issuer index 2019-2025: cumulative `106.54%`; rounded-input CAGR `10.92%`; 2021-2025 CAGR `7.14%`
- Latest current NAV TR YTD: `+17.53%` as of 28 ส.ค. 2026; the latest official factsheet separately reports `+13.88%` as of 31 ก.ค. 2026, which is an earlier observation rather than a same-date conflict
- Coverage/source note: official iShares factsheet provides complete calendar rows 2019-2025 and the July month-end YTD field; the current product page provides the newer 28 ส.ค. YTD field. S&P annual rows reuse the cached USD Total Return convention as of 31 ธ.ค. 2025.

| Year | WSML NAV TR | MSCI World Small Cap Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2019 | 25.73% | 26.19% | 31.49% |
| 2020 | 15.83% | 15.96% | 18.40% |
| 2021 | 15.81% | 15.75% | 28.71% |
| 2022 | -18.64% | -18.75% | -18.11% |
| 2023 | 16.02% | 15.76% | 26.29% |
| 2024 | 7.93% | 8.15% | 25.02% |
| 2025 | 19.84% | 19.88% | 17.88% |

## Up years / Down years

- Up years / Down years: `6 / 1` across complete calendar years 2019-2025
- Best: 2019, `+25.73%`; least positive: 2024, `+7.93%`
- Worst: 2022, `-18.64%`; least bad down year: 2022, `-18.64%`
- 2019-2025 CAGR: `10.87%`; 2021-2025 CAGR: `7.17%`
- Latest current YTD: official NAV TR `+17.53%` as of 28 ส.ค. 2026. No same-date current S&P 500 TR observation is asserted; the cached benchmark remains limited to complete 2016-2025 calendar years.
- Latest official NAV: `US$10.62` as of 28 ส.ค. 2026; the legacy OTC alias price is not mixed into NAV Total Return ranking.

## Risk read-through

WSML กระจาย across developed-market small caps จึงมี small-cap liquidity,
country, currency, equity-market และ tracking-error risk. Official iShares
portfolio data reports 3-year standard deviation `16.17%` and beta `1.000` as of
31 ก.ค. 2026, with `3,548` holdings as of 28 ส.ค. 2026. At the factsheet's
31 ก.ค. 2026 window, fund NAV TR `13.88%` slightly exceeded issuer index
`13.85%` by `0.03 pp`; the newer product-page YTD `17.53%` is kept separately.
Official daily NAV history sufficient for maximum drawdown and recovery was not
verified in this lean capture, so the values remain `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [iShares official WSML product page](https://www.ishares.com/uk/professionals/en/products/296576/ishares-msci-world-small-cap-ucits-etf-usd-%28acc%29-fund) — official USD share-class identity, listings, current NAV/YTD, benchmark, TER, structure, holdings and risk metrics; current observations through 28 ส.ค. 2026
- [iShares official WSML factsheet](https://www.ishares.com/gls-download/literature/fact-sheet/wsml-ishares-msci-world-small-cap-ucits-etf-fund-fact-sheet-en-gb.pdf) — ISIN, launch, USD accumulating share class, annual NAV/index rows, July YTD and listing table; performance as of 31 ก.ค. 2026
- [Fidelity IMWSF OTC profile](https://digital.fidelity.com/prgw/digital/research/quote/dashboard/summary?symbol=IMWSF) — secondary OTC alias / ISIN cross-check; not used for NAV Total Return ranking
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); cached reference as of 31 ธ.ค. 2025
- ETF source batch: [[ETF_performance_sources_2026-09-02_run-1]] | [[ETF Performance Index]]
