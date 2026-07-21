---
type: source-batch
topic: ETF performance
accessed: 2026-07-21
canonical_outputs:
  - wiki/analysis/performance/ETF_NYSE_ARCA_EWH Performance.md
  - wiki/analysis/comparisons/Hong Kong ETF.md
  - wiki/analysis/performance/ETF Performance Index.md
  - wiki/analysis/comparisons/ETF Region Index.md
tags:
  - source/etf
  - ticker/EWH
  - geography/Hong-Kong
---

# ETF Performance Source Batch - 2026-07-21

## EWH Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:EWH` | [iShares EWH product page](https://www.ishares.com/us/products/239657/ishares-msci-hong-kong-etf) | Fund identity, exchange, benchmark, inception, current NAV/price, YTD NAV TR, fees, holdings, exposure, risk and distributions | NAV/price/net assets 2026-07-20; YTD NAV TR 2026-07-17; holdings/exposure 2026-07-17; rolling performance/risk/yield 2026-06-30 |
| `NYSE Arca:EWH` | [Official EWH factsheet](https://www.ishares.com/us/literature/fact-sheet/ewh-ishares-msci-hong-kong-etf-fund-fact-sheet-en-us.pdf) | Official NAV Total Return definition, annual NAV TR 2021-2025, benchmark, inception, expense ratio and fund characteristics | Factsheet 2026-03-31; annual rows through 2025-12-31 |
| `NYSE Arca:EWH` | [iShares EWH international performance table](https://www.ishares.com/uk/professional/en/products/239657/ishares-msci-hong-kong-etf?siteEntryPassthrough=true&switchLocale=y) | Official complete calendar NAV/Total Return rows 2016-2025 and rolling performance context; 2016-2020 rows displayed to one decimal | Current table accessed 2026-07-21; annual rows through 2025-12-31; rolling snapshot as of 2026-03-31 in this regional view |
| `NYSE Arca:EWH` | [EWH summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-hong-kong-etf-8-31.pdf) | Passive/index-tracking objective, NYSE Arca listing and single-country/international risk disclosures | Prospectus dated 2025-12-30 |
| `Secondary drawdown` | [Lazy Portfolio ETF EWH](https://www.lazyportfolioetf.com/etf/ishares-msci-hong-kong-etf-ewh/) | Dividend-reinvested monthly proxy for maximum drawdown and recovery; not official NAV TR and assumes no fees or capital-gains taxes | Accessed 2026-07-21; series through 2026-06-30 |
| `Common benchmark current YTD` | [Slickcharts S&P 500 YTD](https://www.slickcharts.com/sp500/returns/ytd) | Secondary current S&P 500 Total Return snapshot | Market close 2026-07-20 |
| `Common benchmark definition` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | S&P 500 identity and methodology; annual rows reuse cached USD Total Return convention | Current page accessed 2026-07-21; annual cache as-of 2025-12-31 |

## EWH Verified Fund Facts And As-of Register

- Entity resolution: `EWH` is `iShares MSCI Hong Kong ETF`, primary listing `NYSE Arca:EWH`; listing currency USD; fund inception `1996-03-12`.
- Instrument: passive, index-tracking Hong Kong single-country equity ETF; issuer benchmark `MSCI Hong Kong 25-50 Index (USD) (Net)`; asset class Equity; 26 holdings as of 2026-07-17.
- Return basis: official USD `NAV Total Return`, with distributions reinvested where applicable and fund expenses deducted. Market-price return is kept separate.
- Expense ratio: `0.50%`; distribution frequency: semi-annual.
- Latest official NAV/price: `$22.16` / `$22.14` as of 2026-07-20; issuer premium/discount `-0.09%` as of 2026-07-20.
- Latest official NAV Total Return YTD: `+5.44%` as of 2026-07-17.
- Official rolling NAV performance as of 2026-06-30: 10-year CAGR `4.20%`, cumulative return `50.95%`; normalized check `100.00 -> 150.95` over `10.00` years. Raw daily TR endpoint values are not exposed.
- Portfolio/risk snapshot: 3-year standard deviation `19.08%` and equity beta `0.45` as of 2026-06-30; sector exposure as of 2026-07-17 includes Insurance `20.99%`, Financial Services `16.75%`, Capital Goods `15.40%`, Real Estate Management & Development `14.01%`, and Utilities `11.88%`.
- Latest verified cash distributions: `$0.350114` ex/pay 2026-06-15/2026-06-18; `$0.685496` ex/pay 2025-12-16/2025-12-19; `$0.418504` ex/pay 2025-06-16/2025-06-20; `$0.344493` ex/pay 2024-12-17/2024-12-20. All are USD/share income distributions; latest four average `$0.449652` per round, not a forecast. Issuer 12m trailing yield is `4.95%` as of 2026-06-30.

## EWH Official Annual NAV Total Return Inputs

| Year | EWH NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 1.80% | 11.96% |
| 2017 | 35.60% | 21.83% |
| 2018 | -8.30% | -4.38% |
| 2019 | 9.70% | 31.49% |
| 2020 | 4.60% | 18.40% |
| 2021 | -3.43% | 28.71% |
| 2022 | -6.72% | -18.11% |
| 2023 | -14.04% | 26.29% |
| 2024 | 0.10% | 25.02% |
| 2025 | 34.89% | 17.88% |

EWH rows are official complete-calendar-year NAV/Total Return. The international iShares table displays 2016-2020 to one decimal; the US product/factsheet shows 2021-2025 NAV rows to two decimals. S&P 500 rows reuse the cached USD Total Return convention with dividends reinvested and reference as-of 2025-12-31.

## EWH Calculations And Gaps

- 2016-2025 EWH cumulative/CAGR: `51.86%` / `4.27%`; up/down `6 / 4`. Calculation: `Π(1 + annual TR) - 1 = 51.8645%`; `(1 + 0.5186445)^(1 / 10) - 1 = 4.2667%`, displayed to two decimals. Because 2016-2020 source rows are rounded to one decimal, this is approximate from published official rows.
- 2021-2025 EWH cumulative/CAGR: `4.55%` / `0.89%`; S&P 500 TR `96.17%` / `14.43%`.
- S&P 500 TR 2016-2025 cumulative/CAGR: `298.33%` / `14.82%`; S&P 500 is a common reference, not EWH's tracked index.
- Rolling 10-year check: issuer cumulative `50.95%` normalized as `100.00 -> 150.95` over `10.00` years; `(150.95 / 100.00)^(1 / 10.00) - 1 = 4.20%`.
- Current S&P 500 TR YTD: `+9.43%` as of `2026-07-20` from Slickcharts; EWH current NAV TR YTD is `+5.44%` as of `2026-07-17`, so the comparison is not same-date.
- Secondary drawdown proxy: maximum drawdown `-65.56%` from peak `1997-08` to trough `1998-08`; recovery/new high `2006-03`, `104` months total. The proxy is a monthly USD dividend-reinvested simulation through 2026-06-30 that assumes no fees or capital-gains taxes; it is not official NAV TR.
- Official daily NAV Total Return index levels, maximum drawdown and recovery date: `ไม่พบข้อมูลที่ยืนยันได้`.

## Cached S&P 500 TR Sources

- [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true) — 2016-2019 reference rows
- [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf) — 2018-2022 rows
- [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/) — 2021 row
- [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — 2022-2025 rows
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index definition and methodology
