---
type: source-batch
topic: ETF performance
accessed: 2026-07-19
canonical_outputs:
  - wiki/analysis/performance/ETF_NYSE_ARCA_DVYA Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_IDX Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_FXI Performance.md
  - wiki/analysis/performance/ETF_NASDAQ_INDY Performance.md
  - wiki/analysis/performance/ETF Performance Index.md
tags:
  - source/etf
  - ticker/DVYA
  - ticker/IDX
  - ticker/FXI
  - ticker/INDY
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

## INDY Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NASDAQ:INDY` | [iShares INDY product page](https://www.ishares.com/us/products/239758/ishares-india-50-etf) | Fund identity, NASDAQ listing, Nifty 50 benchmark, inception, current NAV/price, YTD NAV TR, fees, holdings, sector exposure, risk and distributions | NAV/price/holdings/exposure 2026-07-16 to 2026-07-17; YTD 2026-07-16; rolling performance/risk 2026-06-30 |
| `NASDAQ:INDY` | [Official iShares INDY factsheet](https://www.ishares.com/us/literature/fact-sheet/indy-ishares-india-50-etf-fund-fact-sheet-en-us.pdf) | Official NAV total-return definition, annual NAV TR 2021-2025, benchmark, inception, expense ratio and risk facts | Factsheet 2026-03-31; annual rows through 2025-12-31 |
| `NASDAQ:INDY` | [BlackRock INDY factsheet as of 2025-06-30](https://www.blackrock.com/americas-offshore/en/literature/fact-sheet/indy-ishares-india-50-etf-fund-fact-sheet-en-lm.pdf) | Official 2020 calendar NAV TR row used to extend complete-year coverage | Factsheet 2025-06-30 |
| `NASDAQ:INDY` | [iShares INDY summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-india-50-etf-3-31.pdf) | Passive/index-tracking objective and India single-country equity risk disclosures | Prospectus accessed 2026-07-19 |
| `Common benchmark` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Common-reference benchmark identity; annual rows reuse the cached USD total-return convention | Cache as-of 2025-12-31 |

## INDY Verified Facts And As-of Register

- Entity resolution: user alias `INDY (india) ETF 50` resolves to `iShares India 50 ETF`, primary listing `NASDAQ:INDY`; listing currency USD; fund inception `2009-11-18`.
- Instrument: passive, index-tracking India large-cap equity ETF; issuer benchmark `Nifty 50 Index`; 50 holdings.
- Return basis: official USD `NAV Total Return`, with dividends and capital-gains distributions reinvested and fund expenses deducted. Market-price return is kept separate.
- Expense ratio: `0.65%`; distribution frequency: semi-annual.
- Latest official NAV: `$43.50` as of `2026-07-17`; closing market price `$43.37`; premium/discount `-0.29%`; 1-day NAV change `+$0.48` / `+1.12%`.
- Latest official NAV Total Return YTD: `-12.32%` as of `2026-07-16`.
- Official rolling NAV performance as of `2026-06-30`: 1-year `-13.27%`, 3-year annualized `1.84%`, 5-year annualized `2.45%`, 10-year annualized `6.67%`, and since inception `4.94%`. The same issuer table reports 10-year cumulative return `90.75%`; raw daily TR endpoints are not exposed.
- Portfolio/risk snapshot: 50 holdings; 3-year standard deviation `13.37%` and equity beta `0.38` as of `2026-06-30`; Financials `36.95%` as of `2026-07-16`.
- Latest verified distribution: `$0.099016` per share, ex-date `2026-06-15`, payable `2026-06-18`; trailing yield `0.85%` as of `2026-06-30`.

## INDY Official Annual NAV Total Return Inputs

| Year | INDY NAV TR | S&P 500 TR |
|---|---:|---:|
| 2020 | 10.67% | 18.40% |
| 2021 | 19.28% | 28.71% |
| 2022 | -7.86% | -18.11% |
| 2023 | 17.05% | 26.29% |
| 2024 | 4.02% | 25.02% |
| 2025 | 4.42% | 17.88% |

INDY 2020 is an official complete-calendar-year NAV row from the BlackRock
factsheet as of 2025-06-30; 2021-2025 rows are official complete-calendar-year
NAV Total Return from the iShares product page/factsheet. S&P 500 rows reuse the
cached USD Total Return convention with dividends reinvested and reference
as-of `2025-12-31`.

## INDY Calculations And Gaps

- 2020-2025 INDY cumulative/CAGR: `54.64%` / `7.54%`; up/down `5 / 1`.
- 2021-2025 INDY cumulative/CAGR: `39.73%` / `6.92%`; up/down `4 / 1`.
- S&P 500 TR 2021-2025 cumulative/CAGR: `96.17%` / `14.43%`; S&P 500 is a common reference, not INDY's tracked index.
- Rolling 10-year check: issuer cumulative `90.75%` normalized as `100.00 -> 190.75` over `10.00` years; `(190.75 / 100.00)^(1 / 10.00) - 1 = 6.67%`.
- Official annual NAV TR rows for 2016-2019 are `ไม่พบข้อมูลที่ยืนยันได้` in the current issuer capture; no secondary proxy is inserted into the NAV ranking.
- Official raw 10-year NAV TR endpoints, daily NAV TR index levels, maximum drawdown and recovery date: `ไม่พบข้อมูลที่ยืนยันได้`. Price-based or secondary drawdown would not be interchangeable with NAV TR.

## Benchmark Cache Sources

- [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true) — 2016-2019 reference rows
- [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf) — 2018-2022 rows
- [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/) — 2021 row
- [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — 2022-2025 rows
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index definition and methodology

## FXI Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:FXI` | [iShares FXI product page](https://www.ishares.com/us/products/239536/FXI) | Fund identity, exchange, benchmark, inception, current NAV/price, YTD NAV TR, fees, holdings, sector exposure, premium/discount, trailing yield and distributions | NAV/price/premium-discount 2026-07-17; YTD/holdings 2026-07-16; standardized performance/risk/yield 2026-06-30 |
| `NYSE Arca:FXI` | [Official FXI factsheet](https://www.ishares.com/us/literature/fact-sheet/fxi-ishares-china-large-cap-etf-fund-fact-sheet-en-us.pdf) | Official NAV total-return definition, annual NAV TR 2021-2025, benchmark, inception, expense ratio and risk facts | Factsheet 2026-03-31; annual rows through 2025-12-31 |
| `NYSE Arca:FXI` | [iShares FXI summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-china-large-cap-etf-7-31.pdf) | Passive/index-tracking objective, NYSE Arca listing and China large-cap risk disclosures | 2025-11-28 |
| `Secondary drawdown` | [Total Real Returns FXI](https://totalrealreturns.com/n/FXI) | Dividend-reinvested adjusted-total-return proxy for maximum drawdown, recovery and current drawdown; not official NAV TR | Accessed 2026-07-19; history through 2026-07-08 |
| `Common benchmark current YTD` | [Slickcharts S&P 500 YTD](https://www.slickcharts.com/sp500/returns/ytd) | Secondary S&P 500 Total Return current YTD snapshot because the official current Total Return value was not text-extractable in the capture | Market close 2026-07-17 |
| `Common benchmark definition` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | S&P 500 identity, methodology and total-return ticker; annual rows reuse the cached USD TR convention | Current page 2026-07-17; annual cache as-of 2025-12-31 |

## FXI Verified Facts And As-of Register

- Entity resolution: `FXI` is `iShares China Large-Cap ETF`, primary listing `NYSE Arca:FXI`; listing currency USD; fund inception `2004-10-05`.
- Instrument: passive, index-tracking China large-cap equity ETF; issuer benchmark `FTSE China 50 Index (Net)`.
- Return basis: official USD `NAV Total Return`, with distributions reinvested and fund expenses deducted. Market-price return is kept separate.
- Expense ratio: `0.73%`; distribution frequency: semi-annual.
- Latest official NAV: `$34.19` as of `2026-07-17`; closing market price `$34.13`; premium/discount `-0.18%`; 1-day NAV change `-1.29%`.
- Latest official NAV Total Return YTD: `-9.28%` as of `2026-07-16`.
- Official standardized NAV performance as of `2026-06-30`: 1-year `-11.84%`, 3-year `7.95%` annualized, 5-year `-5.06%` annualized, 10-year `1.75%` annualized, and since-inception `4.94%` annualized. The same issuer table reports 10-year cumulative return `18.94%`; raw daily TR endpoints are not exposed.
- Portfolio snapshot: 50 holdings as of `2026-07-16`; 3-year standard deviation `21.41%`, P/E `11.16x`, P/B `1.38x`, and equity beta `0.34` as of the stated issuer dates. Sector mix: Financials `32.95%`, Consumer Discretionary `26.73%`, Communication `17.43%`.
- Latest verified distribution: `$0.263439` per share, ex-date `2026-06-15`, payable `2026-06-18`; trailing yield `2.14%` as of `2026-06-30`.

## FXI Official Annual NAV Total Return Inputs

| Year | FXI NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | -21.04% | 28.71% |
| 2022 | -20.40% | -18.11% |
| 2023 | -12.87% | 26.29% |
| 2024 | 30.10% | 25.02% |
| 2025 | 29.01% | 17.88% |

FXI rows are official complete-calendar-year NAV Total Return from the iShares
product page/factsheet; S&P 500 rows reuse the cached USD Total Return convention
with dividends reinvested and reference as-of `2025-12-31`.

## FXI Calculations And Gaps

- 2021-2025 FXI cumulative/CAGR: `-8.08%` / `-1.67%`; up/down `2 / 3`.
- S&P 500 TR 2021-2025 cumulative/CAGR: `96.17%` / `14.43%`; FXI lagged by `104.25 percentage points` cumulative.
- Rolling 10-year check: issuer cumulative `18.94%` normalized as `100.00 -> 118.94` over `10.00` years; `(118.94 / 100.00)^(1 / 10.00) - 1 = 1.75%`.
- Current S&P 500 TR YTD: `+9.64%` as of `2026-07-17` from Slickcharts; this is a secondary current snapshot and is one trading day later than FXI's official YTD.
- Secondary drawdown proxy: maximum drawdown `-72.68%` on `2008-10-27`, recovery `3,094` trading sessions through `2021-02`; current drawdown `-29.28%` as of `2026-07-08`. These are adjusted-total-return proxy values, not official NAV drawdown/recovery.
- Official daily NAV Total Return index levels for direct maximum drawdown/recovery calculation: `ไม่พบข้อมูลที่ยืนยันได้`.

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
