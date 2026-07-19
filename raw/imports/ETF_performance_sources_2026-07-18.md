---
type: source-note
source_profile: etf-performance-delta
accessed: 2026-07-18
canonical_outputs:
  - wiki/analysis/performance/ETF_NYSE_ARCA_VSS Performance.md
  - wiki/analysis/performance/ETF_NASDAQ_VXUS Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_EWG Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_EWJ Performance.md
  - wiki/analysis/performance/ETF_CBOE_EFAV Performance.md
  - wiki/analysis/performance/ETF_CBOE_BBJP Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_KWEB Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_FLJP Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_ECNS Performance.md
  - wiki/analysis/performance/ETF Performance Index.md
tags:
  - source/etf
  - source/performance
  - source/benchmark
---

# ETF Performance Source Batch - 2026-07-18

## ECNS Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:ECNS` | [iShares ECNS product page](https://www.ishares.com/us/products/239620/ishares-msci-china-smallcap-etf) | Fund identity, exchange, benchmark, inception, current NAV/price, YTD NAV TR, fees, holdings, sector exposure, premium/discount and distributions | Current NAV/price 2026-07-17; YTD NAV TR 2026-07-16; holdings/sectors 2026-07-16; performance 2026-06-30 |
| `NYSE Arca:ECNS` | [Official ECNS factsheet](https://www.ishares.com/us/literature/fact-sheet/ecns-ishares-msci-china-small-cap-etf-fund-fact-sheet-en-us.pdf) | Official NAV total-return definition, annual NAV TR 2021-2025, standardized 10-year NAV CAGR, expense ratio and risk facts | Fact sheet 2026-03-31; annual rows through 2025-12-31 |
| `NYSE Arca:ECNS` | [iShares summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-china-small-cap-etf-8-31.pdf) | Passive/index-tracking policy and China/small-cap risk disclosures | 2025-08-31 |
| `China macro` | [AP Q2 2026 China economy report](https://apnews.com/article/china-economy-trade-exports-ai-95136222f87d5a1e62918f41efab00be) | GDP, domestic demand, fixed-asset investment, retail sales and property context | Published 2026-07-15 |
| `China/Hong Kong market move` | [ET Net 17 Jul 2026 close](https://www.etnet.com.hk/www/eng/futures/futures_news_detail.php?newsid=20260717190) | Same-session Hang Seng, Hang Seng China Enterprises and Hang Seng TECH move | 2026-07-17 |
| `Common benchmark` | [S&P 500 official returns page](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=76d0e321-60b6-4834-a4b7-68bbe72fd4ea&sourceIdentifier=index-family-specialization) | Current S&P 500 Total Return YTD cross-check | 2026-07-18 |

## ECNS Verified Fund Facts And As-of Register

- Entity resolution: user alias `AMEX-ECNS` resolves to official primary listing
  `NYSE Arca:ECNS`; fund name `iShares MSCI China Small-Cap ETF`; listing currency
  USD; fund inception `2010-09-28`.
- Instrument: passive, index-tracking equity ETF; issuer benchmark `MSCI China
  Small Cap Index (Net)`; the fund targets smaller Chinese equities available to
  international investors.
- Return basis: official USD `NAV Total Return`, with distributions reinvested and
  fund expenses deducted. Market-price return is kept separate.
- Expense ratio: `0.59%`.
- Latest official NAV: `$28.18` as of `2026-07-17`; closing market price `$28.20`,
  52-week range `$28.08-$39.84`, and premium/discount `0.08%` on the issuer page.
- Latest official NAV Total Return YTD: `-10.26%` as of `2026-07-16`.
- Standardized official NAV performance as of `2026-06-30`: 1-year `-4.90%`,
  3-year `4.94%` annualized, 5-year `-8.85%` annualized, 10-year `1.05%`
  annualized, and since-inception `0.17%` annualized. Raw 10-year TR endpoints
  are not exposed by the issuer; no endpoint values are inferred.
- Downside-relevant portfolio snapshot as of `2026-07-16`: 266 holdings; Health
  Care `22.98%`, Industrials `14.12%`, Information Technology `11.41%`, Consumer
  Discretionary `10.93%`, Real Estate `8.54%`, Materials `8.49%`; 3-year standard
  deviation `26.43%`, P/E `11.31x`, P/B `0.88x`.
- Comparable broad-China context: iShares MCHI NAV YTD `-9.50%` as of `2026-07-16`
  and 3-year standard deviation `21.99%` as of `2026-06-30`; this is context only,
  not ECNS's issuer benchmark.

## ECNS Official Annual NAV Total Return Inputs

| Year | ECNS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 3.10% | 28.71% |
| 2022 | -24.77% | -18.11% |
| 2023 | -23.28% | 26.29% |
| 2024 | 6.94% | 25.02% |
| 2025 | 36.42% | 17.88% |

ECNS rows are official complete-calendar-year NAV Total Return from the iShares
factsheet as of `2026-03-31`; S&P 500 rows reuse the cached USD Total Return
convention documented below, with dividends reinvested and reference as-of
`2025-12-31`.

## ECNS Calculations And Recent Move

- 2021-2025 ECNS cumulative/CAGR: `-13.19%` / `-2.79%`; up/down `3 / 2`.
- S&P 500 TR 2021-2025 cumulative/CAGR: `96.17%` / `14.43%`.
- Current official ECNS NAV YTD is `-10.26%` as of `2026-07-16`; latest NAV one-day
  change is `-3.45%` as of `2026-07-17`.
- Current price is `29.22%` below the issuer's 52-week high: `(28.20 / 39.84) - 1`.
  This is a price-vs-52-week-high calculation, not official maximum drawdown.
- ECNS NAV was down `3.45%` on 17 Jul 2026 while the Hang Seng, Hang Seng China
  Enterprises and Hang Seng TECH fell about `2.0%`, `2.4%` and `4.0%`; this supports
  a market/China risk-off explanation for the latest session.
- Distribution: `$0.453779` per share, ex-date `2026-06-15`, payable `2026-06-18`.
  The distribution is about `1.61%` of the 17 Jul NAV and can create a mechanical
  price-chart drop; it is already included in NAV Total Return.

## ECNS Drivers And Gaps

- `confirmed event`: the 17 Jul China/Hong Kong risk-off session and ECNS's matching
  NAV decline; causality is attributed to market-wide movement, not a fund-specific
  announcement.
- `probable driver`: China Q2 2026 GDP growth slowed to `4.3%`, the slowest since
  late 2022; H1 fixed-asset investment fell `5.7%`, retail sales rose `1.3%`, and
  housing prices continued to fall. The link to ECNS is an inference from these
  macro facts and the fund's domestic small-cap sector mix.
- `probable driver`: small-cap liquidity and volatility risk; issuer 3-year standard
  deviation is `26.43%`, versus MCHI `21.99%`. The near-zero issuer premium/discount
  means ETF trading mechanics are not the primary confirmed cause.
- Official daily NAV Total Return index levels, maximum drawdown and recovery date:
  `ไม่พบข้อมูลที่ยืนยันได้`. No secondary price proxy is used in NAV rankings.

## Benchmark Cache Sources

- [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true) — 2016-2019 reference rows
- [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf) — 2018-2022 rows
- [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/) — 2021 row
- [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — 2022-2025 rows
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index definition and methodology

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

## VXUS Verified Fund Facts And As-Of Register

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

## VXUS Official Annual NAV Total Return Inputs

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
S&P 500 rows reuse the benchmark cache documented above; market-price returns
are excluded from the table and ranking.

## VXUS Calculations And Current Trend

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

## VXUS Gaps And Reconciliation

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

## EFAV Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `Cboe BZX:EFAV` | [iShares product page](https://www.ishares.com/us/products/239626/ishares-msci-eafe-minimum-volatility-etf) | Fund identity, exchange, official annual/rolling/current NAV TR, fee, NAV, market price, distributions and risk metrics | Annual 2025-12-31; rolling/risk 2026-06-30; YTD/price 2026-07-16; NAV 2026-07-17; distribution paid 2026-06-18 |
| `Cboe BZX:EFAV` | [Official fact sheet](https://www.ishares.com/us/literature/fact-sheet/efav-ishares-msci-eafe-min-vol-factor-etf-fund-fact-sheet-en-us.pdf) | Return definition, 2021-2025 NAV TR, benchmark, expense ratio and fund facts | 2026-03-31 |
| `Cboe BZX:EFAV` | [Summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-edge-msci-min-vol-eafe-etf-7-31.pdf) | Legal exchange/benchmark, passive representative-sampling strategy, return basis and official 2016-2024 annual returns | 2025-11-28 |
| `Cboe BZX:EFAV` | [Cboe listing](https://www.cboe.com/us/equities/listings/listed_products/symbols/EFAV) | Exchange and listing-date cross-check | Accessed 2026-07-18 |

## EFAV Verified Fund Facts And As-Of Register

- Entity: `Cboe BZX:EFAV`; fund name `iShares MSCI EAFE Min Vol Factor ETF`;
  inception `2011-10-18`; Cboe listing date `2011-10-20`.
- Instrument: passive, index-tracking developed-market equity ETF using
  representative sampling; supported by ETF v1. Issuer benchmark is
  `MSCI EAFE Minimum Volatility (USD) Index (Net)`.
- Return basis: official USD `NAV Total Return`, before investor taxes, with
  dividends/distributions reinvested and fund expenses reflected. Market-price
  returns are excluded from the table and ranking.
- Expense ratio: `0.20%`; management fee `0.20%`, other expenses `0.00%`.
- Current YTD NAV TR: `6.50%` as of `2026-07-16`; cumulative, not annualized.
- Rolling 10-year NAV TR: CAGR `6.02%`, cumulative `79.38%`, as of
  `2026-06-30`; normalized window `2016-06-30` to `2026-06-30`,
  `100.00 -> 179.38`.
- Latest official NAV: USD `90.81` as of `2026-07-17`; latest displayed closing
  price: USD `90.26` as of `2026-07-16`. Because dates differ, no current
  premium/discount is calculated.
- Latest distribution captured: USD `1.684140` per share, ex/record date
  `2026-06-15`, payable `2026-06-18`. Distribution analysis was not requested.
- Risk snapshot as of `2026-06-30`: 3-year standard deviation `10.46%`, equity
  beta versus S&P 500 `0.28`. Holdings were reported separately as of
  `2026-07-16`; no holdings analysis was requested.

## EFAV Official Annual NAV Total Return Inputs

| Year | EFAV NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -1.86% | 11.96% |
| 2017 | 21.57% | 21.83% |
| 2018 | -5.80% | -4.38% |
| 2019 | 16.78% | 31.49% |
| 2020 | 0.19% | 18.40% |
| 2021 | 7.02% | 28.71% |
| 2022 | -14.76% | -18.11% |
| 2023 | 11.98% | 26.29% |
| 2024 | 5.28% | 25.02% |
| 2025 | 26.16% | 17.88% |

EFAV 2016-2024 rows are official calendar-year returns before taxes in the
`2025-11-28` summary prospectus; 2025 is official NAV TR from the current
product page/fact sheet. S&P 500 rows reuse the benchmark cache documented
above; both series cover complete calendar years and no `*`/`†` is required.

## EFAV Calculations

- 2016-2025 cumulative/CAGR: EFAV `78.42%` / `5.96%`; up/down: `7 / 3`.
- S&P 500 TR 2016-2025 cumulative/CAGR: `298.33%` / `14.82%`.
- 2021-2025 cumulative/CAGR: EFAV `35.68%` / `6.29%`; S&P 500 TR
  `96.17%` / `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; CAGR
  `= product(1 + annual TR)^(1 / years) - 1`.
- Rolling 10-year check: `(179.38 / 100)^(1 / 10) - 1 = 6.0175%`, which rounds
  to the reported `6.02%`.

## EFAV Gaps And Reconciliation

- Official daily NAV TR index levels, maximum drawdown and recovery date:
  `ไม่พบข้อมูลที่ยืนยันได้`; no secondary price proxy is relabelled as NAV TR.
- Latest official price and NAV have different dates; synchronized
  `2026-07-17` price/NAV pair is `ไม่พบข้อมูลที่ยืนยันได้`.
- The `2026-07-16` current YTD value replaces the older month-end `3.47%` as of
  `2026-06-30`. Dates remain separate and no smoothing or backfill is used.

## BBJP Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `Cboe BZX:BBJP` | [JPMorgan BBJP fact sheet](https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBJP.PDF) | Fund identity, passive approach, issuer benchmark, official annual NAV TR, YTD, since-inception return, expense ratio and holdings | Annual 2025-12-31; YTD/fund facts 2026-06-30 |
| `Cboe BZX:BBJP` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1485894/000119312526071745/d800751d497k.htm) | Fund objective, indexed/passive mandate and legal disclosures | 2026-03-01 |
| `Cboe BZX:BBJP` | [Cboe new listing notice](https://www.cboe.com/us/equities/notices/new_listings/details/?etf=true&firm_name=J.P.+Morgan+Asset+Management&first_trade_dt=2018-06-18&ipo=true&symbols=BBEU%2CBBJP%2CBBRE) | Primary exchange and first-trading-date cross-check | 2018-06-18; accessed 2026-07-18 |
| `BBJP` risk | [ETF Central](https://www.etfcentral.com/fund/BBJP) | Secondary volatility, max drawdown and recovery proxy; not official NAV TR | Page updated 2026-06-22; risk table as-of not separately disclosed |
| `BBJP` distribution | [StockAnalysis dividend history](https://stockanalysis.com/etf/bbjp/dividend/) | Secondary latest distribution record: $3.53701, ex-date 2025-12-23, pay date 2025-12-26 | Last checked 2026-06-27 |

## BBJP Verified Fund Facts And As-Of Register

- Entity resolution: `BBJP` resolves to official primary listing `Cboe BZX:BBJP`;
  fund name `JPMorgan BetaBuilders Japan ETF`; Cboe first trade was 2018-06-18.
- Instrument: passive, index-tracking Japan equity ETF; issuer benchmark is
  `Morningstar Japan Target Market Exposure Index (net total return)`.
- Fund performance inception: 2018-06-15; calendar year 2018 is partial and is
  excluded from complete-year ranking.
- Return basis: official NAV Total Return with dividends and capital-gains
  distributions reinvested; NAV total return reflects management fees and
  operating expenses. Currency shown by the issuer is USD.
- Expense ratio: gross `0.190%`; net `0.190%`, as of 2026-06-30.
- Current official YTD NAV TR: `14.75%` as of 2026-06-30; cumulative, not annualized.
  JPMorgan states that YTD is measured through the last business day of the month.
- Since-inception official NAV annualized return: `7.95%` as of 2026-06-30. A
  10-year NAV TR CAGR is not applicable because the fund has less than 10 years of
  performance history.
- Latest captured distribution: `$3.53701` per share, annual, ex-date 2025-12-23
  and pay date 2025-12-26; secondary S&P Global Market Intelligence record via
  StockAnalysis. Distribution amount was not used in the annual table because
  official NAV TR already includes reinvested distributions.
- Latest issuer factsheet holdings snapshot: 173 holdings; Industrials `23.8%`,
  Information Technology `21.7%`, Financials `17.3%`, Consumer Discretionary
  `14.2%`; all as of 2026-06-30.

## BBJP Official Annual NAV Total Return Inputs

| Year | BBJP NAV TR | S&P 500 TR |
|---|---:|---:|
| 2019 | 18.62% | 31.49% |
| 2020 | 15.05% | 18.40% |
| 2021 | 1.39% | 28.71% |
| 2022 | -16.78% | -18.11% |
| 2023 | 20.02% | 26.29% |
| 2024 | 7.19% | 25.02% |
| 2025 | 26.56% | 17.88% |

BBJP rows are official complete-calendar-year NAV Total Return from the June 30,
2026 JPMorgan factsheet. S&P 500 rows reuse the cached USD Total Return convention
documented earlier in this source batch; dividends are reinvested and the reference
date is 2025-12-31. No market-price return is mixed into the table.

## BBJP Calculations

- 2019-2025 cumulative/CAGR: BBJP `87.49%` / `9.39%`; up/down: `6 / 1`.
- S&P 500 TR 2019-2025 cumulative/CAGR: `205.41%` / `17.29%`.
- 2021-2025 cumulative/CAGR: BBJP `37.38%` / `6.56%`; S&P 500 TR `96.17%` /
  `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; CAGR
  `= product(1 + annual TR)^(1 / years) - 1`.

## BBJP Gaps And Reconciliation

- Official rolling 10-year NAV TR endpoints, daily NAV TR levels, maximum drawdown,
  and recovery date: `ไม่พบข้อมูลที่ยืนยันได้`; the fund history is also shorter
  than 10 years.
- Official current YTD is only available through 2026-06-30 month-end in the
  captured JPMorgan factsheet. ETF Central shows a conflicting secondary YTD figure
  of `18.71%` as of 2026-06-18 with unclear return basis; it was excluded in favor of
  the official NAV figure.
- Secondary ETF Central 5-year risk figures (`18.44%` volatility, `-32.66%` max
  drawdown, `504 days` recovery) are displayed on a page last updated 2026-06-22;
  the risk table's separate as-of date is not disclosed. They are kept as a
  labelled proxy and are not used as official NAV performance or cross-ETF ranking
  inputs.

## KWEB Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:KWEB` | [KraneShares KWEB product page](https://kraneshares.com/etf/kweb/) | Official identity, benchmark, expense ratio, inception, daily NAV/market price, premium/discount, rolling NAV TR, holdings and listed-location exposure | NAV/market price/holdings 2026-07-17; rolling performance 2026-06-30 |
| `NYSE Arca:KWEB` | [KraneShares KWEB factsheet](https://kraneshares.com/resources/factsheet/kweb_factsheet.pdf) | Official return definition, fund facts, expense ratio, benchmark and rolling 10-year NAV TR CAGR | 2026-06-30 |
| `NYSE Arca:KWEB` | [Total Real Returns KWEB](https://totalrealreturns.com/n/KWEB) | Secondary dividend-reinvested market-price total-return proxy, annual rows and drawdown proxy | ending 2026-07-17 |
| `NYSE Arca:KWEB` | [Stock Analysis KWEB history](https://stockanalysis.com/etf/kweb/history/) | Secondary closing-price history and latest close cross-check | close 2026-07-17 |
| `NYSE Arca:KWEB` | [KraneShares 2025 China Outlook](https://kraneshares.com/2025-china-outlook-a-recipe-for-re-rating/) | Issuer commentary cross-check for the conflicting 2024 annual-return figure | published 2025-01-08; accessed 2026-07-18 |
| Common benchmark | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Common-reference index definition; 2016-2025 annual rows reuse cached skill convention | reference 2025-12-31 |
| Market move | [Reuters report via Investing.com](https://au.investing.com/news/stock-market-news/sp-500-and-nasdaq-slip-as-chip-rout-extends-netflix-slides-4539385) | Global AI/chip risk-off context and U.S. index comparison | 2026-07-17 |
| Market move | [ET Net Hong Kong market report](https://www.etnet.com.hk/www/eng/futures/futures_news_detail.php?newsid=20260717190) | Hang Seng / Hang Seng Tech session comparison | 2026-07-17 |
| China macro | [China NBS Q2/H1 GDP release](https://www.stats.gov.cn/english/PressRelease/202607/t20260717_1964160.html) and [AP summary](https://apnews.com/article/china-economy-trade-exports-ai-95136222f87d5a1e62918f41efab00be) | Current China growth and domestic-demand context | released 2026-07-15 to 2026-07-17 |

## KWEB Verified Fund Facts And As-Of Register

- Entity resolution: user alias `AMEX-KWEB` resolves to `NYSE Arca:KWEB`; the
  issuer page uses a generic `NYSE` label in places while the official factsheet
  and market-data page identify `NYSE Arca`. The vault uses `NYSE Arca` as the
  exchange-qualified key.
- Fund: `KraneShares CSI China Internet ETF`; passive equity ETF tracking the
  `CSI Overseas China Internet Index`; inception `2013-07-31`; expense ratio
  `0.70%`; annual distribution frequency.
- Return basis: official NAV Total Return includes reinvested distributions and
  deducts fund expenses. Official rolling 10-year NAV TR CAGR is `-0.85%` as of
  2026-06-30; issuer does not expose raw endpoint TR values in the captured page.
- Latest official daily pair: NAV `$26.72` and market price `$26.81`, both as of
  2026-07-17; NAV daily change `-3.15%`, market-price daily change `-2.44%`, and
  premium `$0.09` (approximately `0.34%`).
- Official NAV TR YTD is `-28.96%` as of 2026-06-30. A fresher secondary
  market-price total-return proxy is `-21.26%` YTD as of 2026-07-17; the two are
  not mixed because they have different return bases and as-of dates.
- Holdings snapshot as of 2026-07-17: top five are Tencent `10.22%`, Alibaba
  `8.51%`, PDD `7.96%`, Meituan `7.60%`, and NetEase `6.36%`, totaling `40.65%`.
  Listed-location breakdown: Hong Kong `72.1%`, U.S. ADRs with secondary Hong
  Kong listings `14.4%`, and U.S. ADRs with no secondary Hong Kong listing `13.5%`.
- Sector snapshot as of 2026-06-30: Communication Services `42.92%` and
  Consumer Discretionary `36.91%`; combined `79.83%`.

## KWEB Annual Proxy Inputs

| Year | KWEB total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | -8.54% | 11.96% |
| 2017 | 69.73% | 21.83% |
| 2018 | -33.80% | -4.38% |
| 2019 | 29.92% | 31.49% |
| 2020 | 58.23% | 18.40% |
| 2021 | -49.01% | 28.71% |
| 2022 | -17.24% | -18.11% |
| 2023 | -9.06% | 26.29% |
| 2024 | 12.01% | 25.02% |
| 2025 | 23.55% | 17.88% |

The annual rows are a secondary dividend-reinvested market-price total-return
proxy, not official NAV TR. KraneShares publishes official rolling NAV TR and
quarter/month-end figures, but the captured issuer pages do not provide a
complete calendar-year NAV TR table. An issuer commentary reports KWEB 2024 at
`13.25%`, which conflicts with the proxy's `12.01%`; the proxy is retained for
consistent year-by-year coverage and the conflict is not smoothed.

## KWEB Calculations

- 2016-2025 proxy cumulative/CAGR: `12.19%` / `1.16%`; up/down: `5 / 5`.
- 2021-2025 proxy cumulative/CAGR: `-46.89%` / `-11.89%`.
- S&P 500 TR 2016-2025 cumulative/CAGR: `298.33%` / `14.82%`.
- Secondary total-return proxy since 2013-08-01: `+31.22%`, annualized `+2.12%`,
  ending 2026-07-17.
- Secondary drawdown proxy: current `-68.99%` from 2021-02-17 high; worst
  `-80.92%` on 2022-10-24. Official NAV drawdown/recovery series:
  `ไม่พบข้อมูลที่ยืนยันได้`.
- Formula: cumulative `= product(1 + annual TR) - 1`; CAGR
  `= product(1 + annual TR)^(1 / years) - 1`.

## KWEB Current Move Read-through

- `confirmed event`: KWEB's latest NAV fell `3.15%` and market price fell
  `2.44%` on 2026-07-17. This was consistent with Hang Seng Tech falling about
  `4%` and Hang Seng falling about `2%`; KWEB was not an isolated ETF dislocation.
- `probable driver` / high confidence: global AI/chip risk-off. Reuters reported
  the S&P 500 fell `1.01%` and Nasdaq `1.40%` as investors questioned the pace and
  payoff of AI spending; this is a close timing match for the session.
- `probable driver` / medium-high confidence: weaker China domestic-growth
  narrative. Q2 growth slowed to `4.3%`, while AP reported H1 retail sales growth
  of only `1.3%`, fixed-asset investment down `5.7%`, and continued housing-price
  pressure; this matters for KWEB's e-commerce and consumer exposure but is a
  broader medium-term driver, not proof of a single-day cause.
- Fund-specific flow/discount cause: not confirmed. The latest market price was
  only about `0.34%` above NAV, so premium/discount mechanics do not explain the
  main move. Recovery confirmation requires Hang Seng Tech to stabilize and
  China's consumer/earnings data to improve; a renewed selloff in global AI/chip
  shares would weaken the market-wide explanation's short-term relevance.

## KWEB Gaps And Reconciliation

- Official complete-calendar-year NAV TR rows, official daily NAV TR index levels,
  volatility, maximum drawdown and recovery date: `ไม่พบข้อมูลที่ยืนยันได้`.
- Annual proxy rows are not relabelled as NAV TR and are excluded from strict
  official cross-ETF ranking. The official 10-year NAV CAGR and latest official
  NAV YTD remain separately reported.
- The issuer's generic `NYSE` label and factsheet's `NYSE Arca` label are kept as
  a source-label conflict; `NYSE Arca:KWEB` is the normalized vault key.

## FLJP Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:FLJP` | [Franklin Templeton FLJP product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26357/SINGLCLASS/franklin-ftse-japan-etf/FLJP?role=fp) | Fund identity, exchange, issuer benchmark, inception, expense ratio, official NAV YTD and pricing snapshot | YTD/NAV 2026-07-08; expense ratio 2025-08-01 |
| `NYSE Arca:FLJP` | [Official FLJP factsheet](https://www.franklintempleton.com/forms-literature/download/FLJP-FF?role=fp) | Official NAV total-return definition, annual 2018-2025 returns, since-inception return, benchmark and risk statistics | 2026-06-30 |
| `NYSE Arca:FLJP` drawdown | [PortfoliosLab FLJP](https://portfolioslab.com/symbol/FLJP) | Secondary dividend-adjusted market-price drawdown and recovery proxy; not official NAV TR | Page updated 2026-07-03; accessed 2026-07-18 |
| Common benchmark | [S&P 500 official returns page](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=76d0e321-60b6-4834-a4b7-68bbe72fd4ea&sourceIdentifier=index-family-specialization) | Fresh S&P 500 Total Return YTD cross-check | 2026-07-18 |
| Common benchmark | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Index identity and methodology; annual 2018-2025 rows reuse cached skill convention | Reference 2025-12-31 |

## FLJP Verified Fund Facts And As-Of Register

- Entity resolution: user alias `AMEX-FLJP` resolves to official primary listing
  `NYSE Arca:FLJP`; fund name `Franklin FTSE Japan ETF`.
- Instrument: passive, index-tracking equity ETF with large- and mid-cap Japanese
  exposure; issuer benchmark `FTSE Japan Capped Index-NR`; inception `2017-11-02`;
  dividend frequency `Semi-Annual`; net expense ratio `0.09%` as of `2025-08-01`.
- Return basis: official USD `NAV Total Return`, assuming reinvestment of all
  distributions and deduction of all fund expenses. Annual rows are complete
  calendar-year observations for 2018-2025; 2017 partial is omitted.
- Official since-inception average annual NAV return: `7.83%` as of `2026-06-30`;
  official 10-year field is `—` because the fund history is shorter than 10 years.
- Latest official NAV YTD captured: `14.82%` as of `2026-07-08`; the captured issuer
  page did not expose a later official NAV-YTD snapshot. Official factsheet month-end
  YTD was `15.32%` as of `2026-06-30`; the fresher issuer value is used in the page.
- Official 3-year standard deviation: `14.67%` as of `2026-06-30`; market price is
  not mixed into annual NAV rankings.

## FLJP Official Annual NAV Total Return Inputs

| Year | FLJP NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -13.10% | -4.38% |
| 2019 | 19.09% | 31.49% |
| 2020 | 14.35% | 18.40% |
| 2021 | 1.16% | 28.71% |
| 2022 | -15.78% | -18.11% |
| 2023 | 19.68% | 26.29% |
| 2024 | 7.76% | 25.02% |
| 2025 | 25.30% | 17.88% |

FLJP rows are official complete-calendar-year NAV Total Return from the June 30,
2026 factsheet. S&P 500 rows for 2018-2025 reuse the cached USD Total Return
convention documented in the skill and earlier source batch; dividends are
reinvested and the reference date is 2025-12-31.

## FLJP Calculations

- 2018-2025 cumulative/CAGR: FLJP `62.92%` / `6.29%`; up/down: `6 / 2`.
- S&P 500 TR 2018-2025 cumulative/CAGR: `192.03%` / `14.33%`.
- 2021-2025 cumulative/CAGR: FLJP `37.67%` / `6.60%`; S&P 500 TR `96.17%` /
  `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; CAGR
  `= product(1 + annual TR)^(1 / years) - 1`.

## FLJP Gaps And Reconciliation

- Official rolling 10-year NAV TR endpoints, 10-year NAV CAGR, daily NAV TR levels,
  maximum drawdown and recovery series: `ไม่พบข้อมูลที่ยืนยันได้`; the fund history
  is shorter than 10 years.
- Secondary PortfoliosLab drawdown proxy reports `-32.49%` on 2022-10-14 and
  recovery in `348 trading sessions`; it uses dividend-adjusted market-price data
  and is excluded from NAV TR rankings.
- Current FLJP NAV YTD `14.82%` is as of 2026-07-08, while the freshest official
  S&P 500 TR YTD captured is `9.64%` as of 2026-07-18; no same-date comparison is
  claimed.
