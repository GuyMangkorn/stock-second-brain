---
type: source-note
source_profile: etf-performance-delta
accessed: 2026-07-18
canonical_outputs:
  - wiki/analysis/performance/ETF_NYSE_ARCA_VSS Performance.md
  - wiki/analysis/performance/ETF_NASDAQ_VXUS Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_EWJ Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_EWG Performance.md
  - wiki/analysis/performance/ETF Performance Index.md
tags:
  - source/etf
  - source/performance
  - source/benchmark
---

# ETF Performance Source Batch - 2026-07-18

## VSS Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:VSS` | [Vanguard product page](https://investor.vanguard.com/investment-products/etfs/profile/vss) | Fund identity, official annual NAV TR, rolling returns, expense ratio, benchmark, price/NAV and distributions | Annual 2025-12-31; rolling 2026-06-30; price/NAV 2026-06-22; distribution 2026-06-23 |
| `NYSE Arca:VSS` | [Vanguard Advisors page](https://advisors.vanguard.com/investments/products/vss/vanguard-ftse-all-world-ex-us-small-cap-etf) | Fresh official YTD NAV Total Return | 2026-07-13 |
| `NYSE Arca:VSS` | [Official fact sheet](https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3184.pdf) | NYSE Arca listing, passive index-sampling approach, return definition, risk and fund facts | 2026-03-31 |
| `NYSE Arca:VSS` | [Official prospectus](https://fund-docs.vanguard.com/p3184.pdf) | Legal share-class name, policy, benchmark and fee effectiveness | 2026-02-27 |

## VSS Verified Fund Facts And As-Of Register

- Entity resolution: user alias `AMEX-VSS` resolves to official primary listing
  `NYSE Arca:VSS`; fund name `Vanguard FTSE All-World ex-US Small-Cap ETF`.
- Instrument: passive, index-tracking equity ETF using index sampling; issuer
  benchmark `FTSE Global Small Cap ex US Index`; inception `2009-04-02`.
- Return basis: official `NAV Total Return`, USD, pre-tax, net of fund expenses,
  with dividends and capital-gains distributions reinvested.
- Expense ratio: `0.06%` as of `2026-02-27` (effective `2026-02-02`).
- Current YTD NAV TR: `6.36%` as of `2026-07-13`; cumulative, not annualized.
- Rolling 10-year NAV TR: `8.26%` average annual return as of `2026-06-30`;
  implied window `2016-06-30` to `2026-06-30`.
- Latest official closing pair captured: market price `$157.89`, NAV `$157.53`
  as of `2026-06-22`; stale relative to access date and not presented as current.
- Latest captured distribution: `$0.858600` per share, ex/record date
  `2026-06-18`, payable `2026-06-23`.
- Holdings/portfolio characteristics snapshot: `2026-05-31`; fund facts and
  methodology description: `2026-03-31`.

## VSS Official Annual NAV Total Return Inputs

| Year | VSS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 4.37% | 11.96% |
| 2017 | 30.26% | 21.83% |
| 2018 | -18.43% | -4.38% |
| 2019 | 21.73% | 31.49% |
| 2020 | 11.95% | 18.40% |
| 2021 | 12.81% | 28.71% |
| 2022 | -21.22% | -18.11% |
| 2023 | 15.25% | 26.29% |
| 2024 | 2.67% | 25.02% |
| 2025 | 29.99% | 17.88% |

VSS rows are official complete-calendar-year NAV TR as of `2025-12-31`.
S&P 500 rows copy the skill's cached USD Total Return convention, dividends
reinvested, reference as of `2025-12-31`; no fresh benchmark web search was run.

## VSS Calculations

- VSS 2016-2025 cumulative: `106.58%`; CAGR: `7.53%`; up/down: `8 / 2`.
- S&P 500 TR 2016-2025 cumulative: `298.33%`; CAGR: `14.82%`.
- VSS 2021-2025 cumulative: `36.70%`; CAGR: `6.45%`.
- S&P 500 TR 2021-2025 cumulative: `96.17%`; CAGR: `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; CAGR
  `= product(1 + annual TR)^(1 / years) - 1`.
- Normalized rolling 10-year start `100.00`; calculated end `221.15` from the
  rounded official CAGR: `100 x (1 + 0.0826)^10`. This is a shown calculation,
  not a reported Vanguard endpoint.

## Benchmark Cache Sources

- [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true) — 2016-2019 reference rows
- [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf) — 2018-2022 rows
- [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/) — 2021 row
- [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — 2022-2025 rows
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index definition and methodology

## VSS Gaps And Reconciliation

- Official maximum drawdown and recovery series: `ไม่พบข้อมูลที่ยืนยันได้`.
- Vanguard did not expose raw rolling 10-year TR endpoints for `2026-06-30`;
  the normalized endpoint in the performance page is calculated from the rounded
  official CAGR and is labelled accordingly.
- No secondary return series was used. Market-price return is excluded from the
  annual table and ranking. The current YTD line uses the fresher `2026-07-13`
  official NAV figure rather than the month-end `8.18%` as of `2026-06-30`.

## VXUS Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `Nasdaq:VXUS` | [Vanguard product page](https://investor.vanguard.com/investment-products/etfs/profile/vxus) | Fund identity, official annual/rolling NAV Total Return, fee, price/NAV and distributions | Annual 2025-12-31; rolling 2026-06-30; price/NAV 2026-07-09; distribution 2026-06-23 |
| `Nasdaq:VXUS` | [Vanguard Advisors page](https://advisors.vanguard.com/investments/products/vxus/vanguard-total-international-stock-etf) | Fresh official YTD NAV Total Return | 2026-07-13 |
| `Nasdaq:VXUS` | [Vanguard fact sheet](https://institutional.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3369.pdf) | Nasdaq listing, passive replication, return definition, risk and fund facts | 2026-03-31 |
| `Nasdaq:VXUS` | [Vanguard prospectus](https://personal1.vanguard.com/pub/Pdf/p3369.pdf), [SEC-hosted summary prospectus](https://www.sec.gov/Archives/edgar/data/736054/000119312526077510/f44038d1.htm) | Legal share-class name, Nasdaq listing, expense breakdown and index strategy | 2026-02-27 |
| `Nasdaq:VXUS` trend | [Barchart performance](https://www.barchart.com/etfs-funds/quotes/VXUS/performance) | Secondary market-price trend only; not NAV Total Return | 2026-07-17 |

## Verified Fund Facts And As-Of Register

- Entity: `Nasdaq:VXUS`; fund name `Vanguard Total International Stock ETF`;
  inception `2011-01-26`; expense ratio `0.05%` as of `2026-02-27`.
- Instrument: passive, index-tracking international equity ETF using index
  replication; issuer benchmark `FTSE Global All Cap ex US Index`.
- Return basis: official pre-tax `NAV Total Return`, including reinvested
  dividends/capital-gains distributions and net of fund expenses. Currency is
  presented in USD, but Vanguard does not separately label return currency in
  the captured table; no FX-hedged return is inferred.
- Official rolling 10-year NAV TR as of `2026-06-30`: cumulative `158.55%`,
  CAGR `9.95%`; normalized window `2016-06-30` to `2026-06-30`, `100.00 -> 258.55`.
- Latest official NAV YTD: `11.55%` as of `2026-07-13`. Earlier official
  snapshots were `13.08%` at `2026-06-30`, `14.73%` at `2026-07-06`, and
  `13.05%` at `2026-07-09`; dates are kept separate rather than smoothed.
- Latest verified official market price/NAV pair: USD `84.90` / `84.74` as of
  `2026-07-09`. The captured premium/discount field was inconsistent with the
  displayed difference and is omitted.
- Latest distribution captured: USD `0.386100` per share, ex-date `2026-06-18`,
  payable `2026-06-23`. Distribution analysis was not requested.
- Fund facts as of `2026-03-31`: `8,794` stocks, P/E `16.9x`, 3-year standard
  deviation `12.60%`; financials `22.6%`, industrials `15.7%`, technology
  `14.6%`; Japan was the largest market allocation at `15.3%`.

## Official Annual NAV Total Return Inputs

| Year | VXUS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 4.72% | 11.96% |
| 2017 | 27.52% | 21.83% |
| 2018 | -14.42% | -4.38% |
| 2019 | 21.58% | 31.49% |
| 2020 | 11.32% | 18.40% |
| 2021 | 8.69% | 28.71% |
| 2022 | -15.99% | -18.11% |
| 2023 | 15.56% | 26.29% |
| 2024 | 5.20% | 25.02% |
| 2025 | 32.23% | 17.88% |

VXUS rows are official complete-calendar-year NAV TR as of `2025-12-31`.
S&P 500 rows use the cached USD Total Return convention with dividends
reinvested, reference as of `2025-12-31`; market-price returns are excluded.

## Calculations And Current Trend

- 2016-2025 cumulative/CAGR: `127.03%` / `8.54%`; up/down: `8 / 2`.
- S&P 500 TR 2016-2025 cumulative/CAGR: `298.33%` / `14.82%`; VXUS gap is
  `-171.30 percentage points` cumulative and `-6.28 percentage points` annualized.
- 2021-2025 cumulative/CAGR: VXUS `46.78%` / `7.98%`; S&P 500 TR
  `96.17%` / `14.43%`.
- NAV YTD moved from `14.73%` on `2026-07-06` to `11.55%` on `2026-07-13`;
  equivalent intervening return is `(1.1155 / 1.1473) - 1 = -2.77%`.
- Secondary market-price snapshot as of `2026-07-17`: USD `83.37`, 5-day
  `-2.23%`, 1-month `-3.15%`, YTD price return `+10.60%`, and `-5.85%` below
  the 52-week high. This supports `positive medium-term / correcting short-term`
  and is not mixed into official NAV TR metrics.

## Benchmark Cache Sources

- [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true) — 2016-2019 rows
- [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf) — 2018-2022 rows
- [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/) — 2021 row
- [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — 2022-2025 rows
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index definition

## Gaps And Reconciliation

- Official daily NAV total-return levels and maximum drawdown/recovery series:
  `ไม่พบข้อมูลที่ยืนยันได้`; no price proxy is relabelled as NAV drawdown.
- Official market price/NAV after `2026-07-09`: `ไม่พบข้อมูลที่ยืนยันได้`; the
  `2026-07-17` trend data are secondary and separately labelled.
- Same-date official S&P 500 TR YTD for `2026-07-13`:
  `ไม่พบข้อมูลที่ยืนยันได้`; no mismatched-date figure is presented as a strict
  current comparator.

## EWG Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:EWG` | [iShares product page](https://www.ishares.com/us/products/239650/ishares-msci-germany-etf) | Fund identity, exchange, objective, benchmark, NAV/price, YTD, fee, risk metrics and distributions | YTD 2026-07-13; NAV/price 2026-07-14; risk 2026-06-30; distribution 2026-06-18 |
| `NYSE Arca:EWG` | [iShares fact sheet](https://www.ishares.com/us/literature/fact-sheet/ewg-ishares-msci-germany-etf-fund-fact-sheet-en-us.pdf) | Official 2021-2025 NAV calendar returns, return definition and fund facts | 2026-03-31 |
| `NYSE Arca:EWG` | [BlackRock localized performance page](https://www.blackrock.com/fi/professionals/products/239650/ishares-msci-germany-etf) | Official USD NAV Total Return rows 2016-2025 | 2025-12-31 |
| `NYSE Arca:EWG` | [SEC-hosted summary prospectus](https://www.sec.gov/Archives/edgar/data/930667/000119312525336658/d175829d497k.htm) | Index-tracking policy, reinvestment convention, best/worst quarter | 2025-12-30 |
| Common benchmark | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Fresh `S&P 500 (TR)` YTD, USD Total Return | 2026-07-17 |

## EWG Verified Fund Facts And As-Of Register

- Entity: `NYSE Arca:EWG`; fund name `iShares MSCI Germany ETF`; passive,
  index-tracking equity ETF; inception `1996-03-12`.
- Issuer benchmark: `MSCI Germany Index (Net)`; expense ratio `0.49%` under the
  current prospectus.
- Return basis: official USD `NAV Total Return`; distributions reinvested and
  fund expenses deducted. Market-price returns remain separate.
- Latest official EWG NAV YTD: `-0.85%` as of `2026-07-13`. Latest official
  NAV/closing-price pair found: USD `41.34` / `41.39` as of `2026-07-14`.
- Official rolling 10-year NAV TR as of `2026-06-30`: cumulative `120.25%`,
  CAGR `8.22%`; normalized window `2016-06-30` to `2026-06-30`,
  `100.00 -> 220.25`.
- Official risk: 3-year standard deviation `16.00%` as of `2026-06-30`;
  prospectus worst quarter `-27.07%` in Q1 2020 and best quarter `+26.67%`
  in Q2 2020. Quarter returns are not relabelled as drawdown/recovery.
- Latest distribution: USD `0.831581` per share, record/ex-date `2026-06-15`,
  payable `2026-06-18`; distribution frequency is semi-annual.
- Current common benchmark: `S&P 500 (TR)` USD Total Return YTD `+9.64%` as of
  `2026-07-17`; this is later than EWG's `2026-07-13` YTD date and is not used
  as a strict same-date comparator.

## EWG Official Annual NAV Total Return Inputs

| Year | EWG NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 2.60% | 11.96% |
| 2017 | 27.40% | 21.83% |
| 2018 | -22.30% | -4.38% |
| 2019 | 20.60% | 31.49% |
| 2020 | 11.30% | 18.40% |
| 2021 | 4.85% | 28.71% |
| 2022 | -22.17% | -18.11% |
| 2023 | 22.90% | 26.29% |
| 2024 | 10.32% | 25.02% |
| 2025 | 35.15% | 17.88% |

EWG rows are official complete-calendar-year NAV TR. The localized issuer table
publishes 2016-2020 to one decimal; 2021-2025 use the two-decimal U.S. fact-sheet
values. S&P 500 rows reuse the skill's cached USD Total Return convention,
dividends reinvested, reference as of `2025-12-31`.

## EWG Calculations

- EWG 2016-2025 cumulative/CAGR: `103.85%` / `7.38%`; up/down: `8 / 2`.
- S&P 500 TR 2016-2025 cumulative/CAGR: `298.33%` / `14.82%`.
- EWG 2021-2025 cumulative/CAGR: `49.53%` / `8.38%`; S&P 500 TR
  `96.17%` / `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; CAGR
  `= product(1 + annual TR)^(1 / years) - 1`.
- Rolling normalized endpoint: `100 x (1 + 120.25%) = 220.25`; CAGR check
  `= (220.25 / 100)^(1 / 10) - 1 = 8.216%`, rounded to official `8.22%`.

## EWG Gaps And Reconciliation

- Official NAV Total Return maximum drawdown and recovery date:
  `ไม่พบข้อมูลที่ยืนยันได้`.
- Official EWG NAV/market close after `2026-07-14`: `ไม่พบข้อมูลที่ยืนยันได้`
  as of access date `2026-07-18`; the last captured values are not presented as
  current-day prices.
- No secondary return series was used. Market-price return is excluded from the
  annual table and ranking.

## EWJ Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:EWJ` | [iShares product page](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf) | Fund identity, exchange, objective, benchmark, NAV/price, current YTD, rolling returns, fee and risk metrics | YTD 2026-07-16; NAV/price 2026-07-17; rolling/risk 2026-06-30 |
| `NYSE Arca:EWJ` | [iShares Summary Prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-japan-etf-8-31.pdf) | Passive/index-sampling policy, return definition, official calendar returns 2016-2024 and fund risks | 2025-12-30 |
| `NYSE Arca:EWJ` | [iShares fact sheet](https://www.ishares.com/us/literature/fact-sheet/ewj-ishares-msci-japan-etf-fund-fact-sheet-en-us.pdf) | Official 2021-2025 NAV calendar returns and return-definition cross-check | 2026-03-31 |
| `NYSE Arca:EWJ` drawdown | [PortfoliosLab](https://portfolioslab.com/symbol/EWJ) | Secondary dividend-adjusted market-price drawdown/recovery proxy; not NAV TR | 2026-07-14 |

## EWJ Verified Fund Facts And As-Of Register

- Entity: `NYSE Arca:EWJ`; fund name `iShares MSCI Japan ETF`; inception
  `1996-03-12`; passive, representative-sampling equity ETF tracking
  `MSCI Japan Index (Net)`.
- Return basis: official before-tax `NAV Total Return`, USD, distributions
  reinvested and fund expenses deducted; market-price return is excluded from
  the annual table and rankings.
- Expense ratio: `0.49%` under the current prospectus. Official 3-year standard
  deviation: `13.32%` as of `2026-06-30`.
- Latest official NAV YTD: `14.28%` as of `2026-07-16`. Latest NAV/closing price:
  USD `90.53` / `90.49` as of `2026-07-17`.
- Official rolling 10-year NAV TR as of `2026-06-30`: CAGR `9.54%`, cumulative
  `148.81%`; normalized endpoints `100.00 -> 248.81`, window
  `2016-06-30` to `2026-06-30`.
- Source reconciliation: an earlier issuer search snapshot exposed YTD `16.32%`
  as of `2026-07-15`; the directly opened issuer page refreshed to `14.28%` as
  of `2026-07-16`, so the later official snapshot is retained.

## EWJ Official Annual NAV Total Return Inputs

| Year | EWJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 1.96% | 11.96% |
| 2017 | 23.56% | 21.83% |
| 2018 | -13.17% | -4.38% |
| 2019 | 19.19% | 31.49% |
| 2020 | 14.03% | 18.40% |
| 2021 | 1.56% | 28.71% |
| 2022 | -17.36% | -18.11% |
| 2023 | 19.78% | 26.29% |
| 2024 | 6.80% | 25.02% |
| 2025 | 25.92% | 17.88% |

EWJ rows are official complete-calendar-year fund returns. The Summary Prospectus
provides 2016-2024 and states that returns assume dividends/distributions are
reinvested; the issuer page provides 2025 and cross-checks 2021-2024. S&P 500
rows reuse the cached USD Total Return convention documented above.

## EWJ Calculations

- EWJ 2016-2025 cumulative/CAGR: `101.00%` / `7.23%`; up/down: `8 / 2`.
- S&P 500 TR 2016-2025 cumulative/CAGR: `298.33%` / `14.82%`.
- EWJ 2021-2025 cumulative/CAGR: `35.20%` / `6.22%`; S&P 500 TR
  `96.17%` / `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; CAGR
  `= product(1 + annual TR)^(1 / years) - 1`.

## EWJ Gaps And Reconciliation

- Same-date official S&P 500 TR YTD for `2026-07-16`:
  `ไม่พบข้อมูลที่ยืนยันได้`; no mismatched-date figure is presented as a strict
  current comparator.
- Official EWJ NAV maximum drawdown/recovery series: `ไม่พบข้อมูลที่ยืนยันได้`.
  PortfoliosLab reports a secondary 10-year dividend-adjusted market-price max
  drawdown of `-33.14%*`, trough October 2022, recovered March 2024; it is kept
  separate from official NAV TR.
