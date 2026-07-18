---
type: source-batch
topic: ETF performance
accessed: 2026-07-19
canonical_outputs:
  - wiki/analysis/performance/ETF_NYSE_ARCA_DVYA Performance.md
  - wiki/analysis/performance/ETF Performance Index.md
tags:
  - source/etf
  - ticker/DVYA
---

# ETF Performance Source Batch - 2026-07-19

## DVYA Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:DVYA` | [iShares DVYA product page](https://www.ishares.com/us/individual/products/239443/ishares-asiapacific-dividend-etf) | Fund identity, exchange, benchmark, inception, current NAV/price, YTD NAV TR, fees, holdings, sector/geography exposure, premium/discount and distribution frequency | NAV 2026-07-17; YTD/price/holdings/exposure/premium-discount 2026-07-16; rolling performance/risk 2026-06-30 |
| `NYSE Arca:DVYA` | [Official DVYA factsheet](https://www.ishares.com/us/literature/fact-sheet/dvya-ishares-asiapacific-dividend-etf-fund-fact-sheet-en-us.pdf) | Official NAV total-return definition, annual NAV TR 2021-2025, standardized 10-year NAV TR, benchmark, expense ratio and index-change note | Factsheet 2026-03-31; annual rows through 2025-12-31 |
| `NYSE Arca:DVYA` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/930667/000119312525192514/d904293d497k.htm) | Passive/index-tracking investment objective, NYSE Arca listing and risk disclosure | 2025-08-29 |
| `Common benchmark` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Common-reference benchmark identity; annual rows use the cached USD total-return convention | Cache as-of 2025-12-31 |

## DVYA Verified Fund Facts And As-of Register

- Entity resolution: user alias `AMEX-DVYA` resolves to the official primary listing
  `NYSE Arca:DVYA`; fund name `iShares Asia/Pacific Dividend ETF`; listing currency
  USD; fund launch date `2012-02-23`.
- Instrument: passive, index-tracking developed Asia-Pacific equity ETF; issuer
  benchmark `Dow Jones Asia/Pacific Select Dividend 50 Index (Net)`.
- Return basis: official USD `NAV Total Return`, with dividends and capital-gains
  distributions reinvested and fund expenses deducted. Market-price return is kept
  separate.
- Expense ratio: `0.49%`; distribution frequency: quarterly.
- Latest official NAV: `$49.52` as of `2026-07-17`; closing market price `$49.39`
  as of `2026-07-16`; issuer-reported premium/discount `-0.17%` as of `2026-07-16`.
- Latest official NAV Total Return YTD: `+14.28%` as of `2026-07-16`.
- Official rolling 10-year NAV TR as of `2026-06-30`: CAGR `6.90%`, cumulative
  return `94.89%`; normalized check `100.00 -> 194.89` over `10.00` years. Raw
  daily NAV TR endpoint values are not exposed by the issuer.
- Risk/portfolio snapshot: 50 holdings as of `2026-07-16`; 3-year standard deviation
  `13.57%` and equity beta `0.54` as of `2026-06-30`; Financials `33.79%`, Australia
  `42.56%`, Hong Kong `24.78%` and Singapore `19.35%` as of `2026-07-16`.

## DVYA Official Annual NAV Total Return Inputs

| Year | DVYA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 4.23% | 28.71% |
| 2022 | -2.12% | -18.11% |
| 2023 | 13.96% | 26.29% |
| 2024 | 5.99% | 25.02% |
| 2025 | 30.16% | 17.88% |

DVYA rows are official complete-calendar-year NAV Total Return from the iShares
factsheet as of `2026-03-31`; S&P 500 rows reuse the cached USD Total Return
convention with dividends reinvested and reference as-of `2025-12-31`.

## DVYA Calculations And Gaps

- 2021-2025 DVYA cumulative/CAGR: `60.39%` / `9.91%`; up/down `4 / 1`.
- S&P 500 TR 2021-2025 cumulative/CAGR: `96.17%` / `14.43%`.
- Rolling 10-year check: `(194.89 / 100.00)^(1 / 10.00) - 1 = 6.90%`; the
  normalized endpoint uses the issuer's reported cumulative return, not an
  inferred daily NAV series.
- Official daily NAV Total Return index levels, maximum drawdown and recovery date:
  `ไม่พบข้อมูลที่ยืนยันได้`. No secondary dividend-reinvested proxy is used in
  the NAV rankings.
- The issuer states that the underlying index changed from the Dow Jones
  Asia/Pacific Select Dividend 30 Index to the Select Dividend 50 Index on
  `2020-06-22`; all annual rows used here are after the change.

## Benchmark Cache Sources

- [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true) — 2016-2019 reference rows
- [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf) — 2018-2022 rows
- [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/) — 2021 row
- [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — 2022-2025 rows
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index definition and methodology
