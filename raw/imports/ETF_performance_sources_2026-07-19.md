---
type: source-batch
topic: ETF performance
accessed: 2026-07-19
canonical_outputs:
  - wiki/analysis/performance/ETF_NYSE_ARCA_DVYA Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_IDX Performance.md
  - wiki/analysis/performance/ETF Performance Index.md
tags:
  - source/etf
  - ticker/DVYA
  - ticker/IDX
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

## IDX Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:IDX` | [VanEck IDX product page](https://www.vaneck.com/us/en/investments/indonesia-index-etf-idx?audience=retail&country=us) | Fund identity, exchange, benchmark, inception, current NAV/YTD, fees, holdings, sector/country exposure and distributions | NAV/YTD/holdings 2026-07-16; sector/country 2026-06-30 |
| `NYSE Arca:IDX` | [VanEck IDX fact sheet](https://www.vaneck.com/us/en/investments/indonesia-index-etf-idx-fact-sheet.pdf) | Official rolling NAV Total Return, valuation, top-10 concentration, risk and expense detail | 2026-06-30 |
| `NYSE Arca:IDX` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1137360/000113736026000469/vaneckindonesiaindexetfidx.htm) | Objective, calendar-year chart, and emerging-market/small-cap/liquidity risk disclosures | Filed 2026-05 |
| `NYSE Arca:IDX` | [FinanceCharts performance](https://www.financecharts.com/etfs/IDX/performance) | Secondary total-return proxy used only to fill annual table because the official chart values are not text-extractable | Accessed 2026-07-19 |
| `NYSE Arca:IDX` | [Charles Schwab summary](https://www.schwab.wallst.com/Prospect/Research/etfs/summary.asp?symbol=IDX) | Secondary market price, closing NAV, premium/discount and 52-week range | Close 2026-07-17 |
| `Indonesia macro` | [BPS Q1 2026 GDP, labor and demographics](https://www.bps.go.id/en/news/2026/05/06/910/ekonomi-indonesia-resilien-dan-tumbuh-solid--pada-triwulan-1-2026.html) | GDP growth, unemployment, employment structure, population and TFR | GDP/labor Q1-Feb 2026; SUPAS 2025 |
| `Indonesia macro` | [Bank Indonesia BI-Rate indicator](https://www.bi.go.id/en/statistik/indikator/bi-rate.aspx) | Policy rate history and latest BI-Rate | 2026-06-18 |
| `Indonesia macro` | [BPS June 2026 inflation](https://www.bps.go.id/en/pressrelease/2026/07/01/2590/inflasi-year-on-year--y-on-y--pada-juni-2026-sebesar-3-34-persen-.html) | Headline/core inflation | 2026-06 |
| `Indonesia governance` | [Transparency International CPI 2025 Asia-Pacific](https://www.transparency.org/en/press/corruption-perceptions-index-2025-stalling-anti-corruption-progress-asia-pacific-public-anger-surges) and [KPK SPI dashboard](https://spi.kpk.go.id/dashboard/hasil/) | Corruption perception and public-sector integrity context | CPI 2025; SPI 2025 |
| `Indonesia cost of living` | [BPS consumption expenditure](https://www.bps.go.id/en/publication/2026/05/29/057b21b35bc236c5ede9d160/expenditure-for-consumption-of-indonesia-september-2025.html), [Katadata summary](https://databoks.katadata.co.id/produk-konsumen/statistik/6a18ecc8f1404/pengeluaran-warga-ri-untuk-rokok-melampaui-belanja-beras-pada-september-2025), and [Numbeo Jakarta](https://www.numbeo.com/cost-of-living/in/Jakarta) | National food-spending and indicative Jakarta urban cost context | Sep 2025; Jun 2026 |

## IDX Verified Facts And Calculations

- Entity resolution: `IDX` is `VanEck Indonesia Index ETF`, primary listing `NYSE Arca:IDX`; it is not the Indonesian `IDX Composite` index.
- Return definition: official USD NAV Total Return includes reinvested distributions and fund expenses. Official rolling NAV returns as of 2026-06-30 are 1Y `-30.93%`, 3Y annualized `-15.82%`, 5Y annualized `-8.96%`, 10Y annualized `-5.49%`, and since inception `3.04%`.
- Latest official NAV/YTD: `$10.65` / `-36.18%` as of 2026-07-16. Current total net assets are `$31.41M`; gross/net expense ratios are `0.86%` / `0.57%`, with the net cap stated through at least 2027-05-01.
- Latest secondary close: market price `$10.90`, closing NAV `$10.86`, premium/discount `0.37%`, 52-week range `$9.51-$17.55`, and 10-day average volume `38,461` as of 2026-07-17.
- Secondary 2016-2025 annual proxy rows are `16.67%, 19.25%, -10.46%, 6.13%, -7.45%, -2.60%, -9.39%, 1.97%, -9.75%, 13.83%`; proxy cumulative/CAGR are `13.13%` / `1.24%`; 2021-2025 cumulative/CAGR are `-7.55%` / `-1.56%`; up/down count is `5/5`.
- Price drawdown proxy: `(10.90 / 17.55) - 1 = -37.89%`; this is price versus the secondary 52-week high, not official maximum drawdown or NAV Total Return drawdown.
- Ex-post real policy-rate approximation: `5.75% BI-Rate - 3.34% June headline CPI = +2.41 percentage points`; this is a simple diagnostic, not a market-implied real rate.
- Macro facts: Q1 2026 GDP `5.61%` y/y; employed `147.67M`; unemployment `4.68%`; population `284.67M`; TFR `2.13`; CPI corruption score `34/100`; KPK local-government SPI `71.33` classified vulnerable. Food spending `~Rp804,430/person/month` is BPS-based secondary reporting; Jakarta single-person cost `~Rp8.44M/month excluding rent` is a crowd-sourced Numbeo estimate and is not a national average.

## IDX Gaps And Interpretation

- Official annual NAV TR values for 2016-2025 are not available as text in the issuer factsheet/product page; the SEC prospectus chart is an image. The annual table is therefore marked `*` and kept separate from official rolling NAV metrics.
- Official raw 10-year NAV TR endpoints, daily NAV TR index levels, maximum drawdown and recovery date: `ไม่พบข้อมูลที่ยืนยันได้`.
- The July 17 market-price gain is a secondary one-day observation and does not confirm a trend change. Sustainable reversal requires concurrent improvement in rate/FX conditions, foreign flows, bank earnings/credit, and governance risk premium.

## Benchmark Cache Sources

- [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true) — 2016-2019 reference rows
- [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf) — 2018-2022 rows
- [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/) — 2021 row
- [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — 2022-2025 rows
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index definition and methodology
