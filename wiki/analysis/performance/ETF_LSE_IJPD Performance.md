---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IJPD
ticker: ISRVF
exchange: LSE
fund: iShares MSCI Japan USD Hedged UCITS ETF (Acc)
tracked_index: MSCI Japan 100% Hedged to USD Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-23
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-20
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
primary_region: Japan
tags:
  - analysis/etf-performance
  - ticker/ISRVF
  - geography/Japan
---

# ISRVF Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

`ISRVF` เป็น input OTC alias ของ share class ที่ official iShares ระบุเป็น
`LSE:IJPD`, ISIN `IE00BCLWRG39`; ใช้ `LSE:IJPD` เป็น canonical entity_key.
กองทุนเป็น passive, physical/optimised, single-country Japan equity ETF ที่
hedge JPY กลับเป็น USD รายเดือน. Official iShares performance table รายงาน
rolling 10-year NAV Total Return cumulative `381.35%` และ CAGR `17.02%` ณ
`2026-06-30`; current YTD ล่าสุดที่ยืนยันได้คือ `17.84%` ณ `2026-07-20`.

## Performance check

- Input ticker: `ISRVF` (OTC alias; not used as the canonical exchange key)
- entity_key: `LSE:IJPD`
- Inception: `2013-09-30`
- Classification: passive, index-tracking, single-country Japan equity ETF
- Replication: physical, optimised
- Metric: NAV Total Return; performance shown on NAV basis with gross income reinvested where applicable
- Tracked index: `MSCI Japan 100% Hedged to USD Index (Net)`
- Total expense ratio: `0.64%`
- Distribution: accumulating
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year window: `2016-06-30` to `2026-06-30`
- Actual elapsed years: `10.00`
- Official 10-year cumulative NAV TR: `381.35%`
- Normalized start/end TR values: `100.00` / `481.35`; raw NAV endpoint levels are `ไม่พบข้อมูลที่ยืนยันได้`
- Formula: `(481.35 / 100.00)^(1 / 10.00) - 1 = 17.02%`
- Current YTD NAV TR: `17.84%` as of `2026-07-20`

| Year | ISRVF / IJPD NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -1.90% | 11.96% |
| 2017 | 20.70% | 21.83% |
| 2018 | -14.10% | -4.38% |
| 2019 | 20.40% | 31.49% |
| 2020 | 9.00% | 18.40% |
| 2021 | 12.80% | 28.71% |
| 2022 | -2.70% | -18.11% |
| 2023 | 34.50% | 26.29% |
| 2024 | 25.60% | 25.02% |
| 2025 | 27.70% | 17.88% |

Annual ETF rows are the official iShares calendar-year NAV display as of
`2026-06-30`; the issuer displays these rows to one decimal, shown here with
two decimal places without implying extra precision. S&P 500 rows use the
cached USD Total Return convention as of `2025-12-31`. The exact June-to-June
S&P 500 TR for the rolling 10-year window is `not disclosed`.

## Up years / Down years

Among the complete official ETF rows for `2016-2025`:

- Up years / Down years: `7 / 3`
- Best: `2023 +34.50%`
- Least positive: `2019 +20.40%`
- Worst: `2018 -14.10%`
- Least bad down year: `2022 -2.70%`
- 2016-2025 cumulative return from rounded annual rows: `+216.04%`
- 2016-2025 annualized return: `12.20%` over `10` calendar years
- 2021-2025 cumulative return: `+136.77%`
- 2021-2025 annualized return: `18.81%` over `5` calendar years
- Current YTD: `17.84%` as of `2026-07-20`

The `12.20%` calendar-row CAGR differs from the official `17.02%` rolling
June-to-June CAGR because the windows and endpoint dates differ.

## Risk read-through

The official 10-year NAV TR CAGR is `17.02%`, but the fund remains a
single-country Japan equity exposure with sector, country and currency risk.
The JPY/USD hedge uses derivatives to reduce currency fluctuations; this is a
hedging overlay, not a derivative-heavy investment strategy, and it can create
hedge cost, basis risk and counterparty risk. iShares reports 3-year beta
`0.993` and standard deviation `13.81%` as of `2026-06-30`. Daily NAV history
sufficient to reproduce max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [iShares UK professional IJPD page](https://www.ishares.com/uk/professional/en/products/257514/ijpd?siteEntryPassthrough=true) — canonical listing, NAV Total Return, annual/rolling performance, benchmark, structure, risk and current NAV/YTD; performance as of `2026-06-30`, current YTD/NAV snapshot as of `2026-07-20`
- [iShares IJPD factsheet](https://www.ishares.com/ch/individual/en/literature/fact-sheet/ijpd-ishares-msci-japan-usd-hedged-ucits-etf-acc-fund-fact-sheet-en-ch.pdf) — passive classification, physical/optimised structure, accumulating income, fee and performance definition; performance as of `2026-02-28`
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention — common USD total-return reference
- ETF source batch: [[ETF_performance_sources_2026-07-23]] | [[ETF Performance Index]]
