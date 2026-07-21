---
type: source-note
source_profile: etf-performance-delta
accessed: 2026-07-13
canonical_outputs:
  - wiki/analysis/performance/ETF_AMEX_DGRO Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_EWC Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_FLCA Performance.md
  - wiki/analysis/performance/ETF_AMEX_VIG Performance.md
  - wiki/analysis/performance/ETF_NASDAQ_VIGI Performance.md
  - wiki/analysis/performance/ETF_AMEX_DIVI Performance.md
  - wiki/analysis/performance/ETF_AMEX_DTD Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_VOO Performance.md
  - wiki/analysis/performance/ETF Performance Index.md
tags:
  - source/etf
  - source/performance
  - source/benchmark
---

# ETF Performance Source Batch - 2026-07-13

## Cached Comparator Refresh

VIG, VIGI, DIVI และ DTD reuse S&P 500 Total Return cached convention โดยไม่ค้น
เว็บใหม่. Basis คือ USD gross total return รวม reinvested dividends; reference
as-of `2025-12-31`. ใช้เฉพาะ complete calendar years ที่ overlap กับแต่ละ ETF:

| ETF | Common window | ETF cumulative / CAGR | S&P 500 TR cumulative / CAGR |
|---|---|---:|---:|
| VIG | 2016-2025 | 242.14% / 13.09% | 298.33% / 14.82% |
| VIGI | 2017-2025 | 116.23% / 8.95% | 255.78% / 15.14% |
| DIVI | 2017-2025 | 149.29% / 10.68% | 255.78% / 15.14% |
| DTD | 2016-2025 | 206.16% / 11.84% | 298.33% / 14.82% |

Original cache URLs are recorded in the `S&P 500 TR cache` rows below. Issuer
tracked indexes and broad-based benchmarks remain metadata or in the prior
source batch; they are not substituted for the common-reference series.

## Source Map

| Scope | Official source | Role | Data date |
|---|---|---|---|
| `AMEX:DGRO` | [iShares DGRO product page](https://www.ishares.com/us/products/264623/ishares-core-dividend-growth-etf), [DGRO factsheet](https://www.ishares.com/us/literature/fact-sheet/dgro-ishares-core-dividend-growth-etf-fund-fact-sheet-en-us.pdf) | Fund identity, NAV Total Return, and issuer benchmark metadata | 2026-06-30 for performance; see prior batch for full source map |
| `S&P 500 TR` | [iShares IVV factsheet](https://www.ishares.com/us/literature/fact-sheet/ivv-ishares-core-s-p-500-etf-fund-fact-sheet-en-us.pdf) | Official S&P 500 Index (USD) calendar-year benchmark returns | 2026-03-31 factsheet; calendar years 2021-2025 |
| `S&P 500 TR cache` | `check-etf-performance` cached convention; [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) | Reusable complete-year S&P 500 TR reference | 2025-12-31; calendar years 2016-2025 |
| `S&P 500` | [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Index definition and total-return series identity | accessed 2026-07-13 |

## Reporting Scope

- Cached comparator window: complete calendar years 2016-2025.
- Official DGRO NAV common window: complete calendar years 2021-2025.
- Currency: USD.
- Return basis: S&P 500 Total Return with dividends reinvested; not price
  return and not net total return.
- DGRO series: official `NAV Total Return`, including reinvested distributions
  and fund expenses, as captured in the prior 2026-07-12 batch.
- The issuer-tracked DGRO index remains `Morningstar US Dividend Growth Index`.
  `S&P 500 Total Return` is the common reference benchmark requested for the
  performance comparison, not a substitute description of DGRO's index.

## Extracted Facts

| Year | DGRO TR | S&P 500 TR |
|---|---:|---:|
| 2016* | 15.20% | 11.96% |
| 2017* | 23.00% | 21.83% |
| 2018* | -2.38% | -4.38% |
| 2019* | 29.87% | 31.49% |
| 2020* | 9.50% | 18.40% |
| 2021 | 26.56% | 28.71% |
| 2022 | -7.85% | -18.11% |
| 2023 | 10.43% | 26.29% |
| 2024 | 16.61% | 25.02% |
| 2025 | 15.74% | 17.88% |

The IVV factsheet identifies its benchmark as `S&P 500 Index (USD)` and reports
the 2021-2025 rows above. The 2016-2025 cache uses the source references listed
in the `check-etf-performance` convention. The annual DGRO rows and the
source-date details remain in `raw/imports/ETF_performance_sources_2026-07-12.md`.

## Calculations

- Official 2021-2025 S&P 500 common-window cumulative return:
  `Π(1 + annual TR) - 1 = 96.17%`.
- Official 2021-2025 S&P 500 common-window CAGR:
  `(1 + 96.17%)^(1 / 5) - 1 = 14.43%`.
- Cached S&P 500 2016-2025 cumulative return: `298.33%`.
- Cached S&P 500 2016-2025 CAGR: `14.82%` from rounded annual inputs.
- DGRO cumulative return and CAGR retained from the official common window:
  `73.82%` and `11.69%`.
- DGRO blended 2016-2025 `10-year TR CAGR*`: `13.08%`, cumulative `241.91%`;
  2016-2020 are secondary proxy rows and 2021-2025 are official NAV TR rows.
- Blended proxy gap versus S&P 500 cache: `-56.42 percentage points` cumulative
  and approximately `-1.74 percentage points` annualized.
- DGRO minus S&P 500: `-22.35 percentage points` cumulative and `-2.74
  percentage points` annualized CAGR.
- DGRO beat S&P 500 in 2022 by `10.26 percentage points`; it lagged in 2021,
  2023, 2024, and 2025.

## Missing / Unverified Data

- DGRO's 2016-2020 rows remain marked `*` as secondary dividend-reinvested
  market-price proxies rather than official NAV Total Return. The resulting
  2016-2025 DGRO figure is explicitly `10-year TR CAGR*`, not official NAV TR.
- A same-date current YTD S&P 500 comparator is not added to the annual table;
  the existing DGRO YTD snapshot remains as of 2026-06-30.

## Handoff For Ingest

Update only `wiki/analysis/performance/ETF_AMEX_DGRO Performance.md` with the
S&P 500 comparator and retain the issuer benchmark as metadata. Do not change
the DGRO entity's tracked-index description or create a corporate valuation.

## EWC Source Map

| Scope | Official source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:EWC` | [iShares EWC product page](https://www.ishares.com/us/products/239615/ishares-msci-canada-etf), [EWC fact sheet](https://www.ishares.com/us/literature/fact-sheet/ewc-ishares-msci-canada-etf-fund-fact-sheet-en-us.pdf) | Fund identity, exchange, inception, expense ratio, NAV Total Return, issuer benchmark, rolling 10-year return, standard deviation, and YTD | Performance 2026-06-30; NAV/price 2026-07-10; YTD 2026-07-09 |
| `NYSE Arca:EWC` | [BlackRock EWC calendar-year performance](https://www.blackrock.com/fi/professionals/products/239615/ishares-msci-canada-etf) | Official calendar-year NAV Total Return rows 2016-2025 | 2025-12-31 year-end rows; page accessed 2026-07-13 |
| `S&P 500 TR` | [S&P 500 DJI returns page](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization) | Same-date YTD comparator | 2026-07-09 |
| `S&P 500 TR cache` | [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) | Reusable complete-year S&P 500 TR reference | 2025-12-31; calendar years 2016-2025 |
| `NYSE Arca:EWC` risk context | [ETF Central EWC](https://www.etfcentral.com/fund/EWC) | Secondary maximum drawdown and drawdown duration | 2026-06-30 |

## EWC Extracted Facts

| Year | EWC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 24.30% | 11.96% |
| 2017 | 16.00% | 21.83% |
| 2018 | -17.20% | -4.38% |
| 2019 | 27.40% | 31.49% |
| 2020 | 5.60% | 18.40% |
| 2021 | 26.74% | 28.71% |
| 2022 | -12.77% | -18.11% |
| 2023 | 14.62% | 26.29% |
| 2024 | 12.25% | 25.02% |
| 2025 | 36.03% | 17.88% |

- Official rolling 10-year EWC NAV Total Return as of 2026-06-30: cumulative
  `190.39%`, CAGR `11.25%`; normalized shown calculation is `100.00 -> 290.39`
  over `10.00` years.
- Official EWC current YTD NAV Total Return: `8.78%` as of 2026-07-09.
- Official S&P 500 TR current YTD: `9.98%` as of 2026-07-09.
- EWC 2021-2025 cumulative/CAGR: `93.49%` / `14.11%`; S&P 500 TR: `96.17%` /
  `14.43%`.
- EWC 2016-2025 cumulative/CAGR calculated from the displayed annual rows:
  `210.78%` / `12.01%`; the 2016-2020 issuer rows are rounded to one decimal.
- Secondary 5-year maximum drawdown: `-24.75%`; duration `834` days, as of
  2026-06-30.

## FLCA Source Map

| Scope | Official source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:FLCA` | [Franklin Templeton FLCA product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26364/SINGLCLASS/franklin-ftse-canada-etf/FLCA) | Fund identity, exchange, inception, issuer benchmark, expense ratio, current NAV, YTD, distribution frequency, and indexed classification | Current NAV/YTD 2026-07-06; expense ratio as of 2025-08-01 |
| `NYSE Arca:FLCA` | [Franklin Templeton FLCA factsheet](https://www.franklintempleton.com/forms-literature/download/FLCA-FF) | Official NAV Total Return calendar-year rows, since-inception annualized return, sector exposure, and NAV risk statistics | 2026-06-30 |
| `S&P 500 TR cache` | [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) | Reusable complete-year S&P 500 Total Return common-reference rows | 2025-12-31; calendar years 2016-2025 |

## FLCA Reporting Scope

- Currency: USD; return basis: official `NAV Total Return`, including reinvested
  distributions and fund expenses.
- Official complete-year coverage: 2018-2025. The issuer factsheet does not show a
  2017 calendar-year partial return; no `†` value is invented.
- Common comparison window: 2018-2025. The issuer benchmark remains `FTSE Canada
  Capped Index-NR`; `S&P 500 Total Return` is a common reference only.
- Current FLCA YTD NAV Total Return: `8.17%` as of 2026-07-06; same-date S&P 500 TR
  YTD was not added because a directly verified official snapshot was not found.

## FLCA Extracted Facts

| Year | FLCA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -15.80% | -4.38% |
| 2019 | 28.67% | 31.49% |
| 2020 | 5.91% | 18.40% |
| 2021 | 29.10% | 28.71% |
| 2022 | -11.95% | -18.11% |
| 2023 | 15.23% | 26.29% |
| 2024 | 12.36% | 25.02% |
| 2025 | 34.90% | 17.88% |

## FLCA Calculations

- 2018-2025 cumulative NAV Total Return: `127.81%`.
- 2018-2025 annualized compound return: `(1 + 127.81%)^(1 / 8) - 1 = 10.84%`.
- 2021-2025 cumulative NAV Total Return: `98.54%`.
- 2021-2025 CAGR: `(1 + 98.54%)^(1 / 5) - 1 = 14.70%`.
- Since-inception NAV annualized return from the factsheet: `11.37%` as of
  2026-06-30; this is not a 10-year CAGR.

## FLCA Missing / Unverified Data

- Official 10-year NAV TR CAGR is not available because the fund launched on
  2017-11-02 and has not completed ten years.
- Max drawdown and recovery period are not disclosed in the captured issuer
  materials; annual returns are insufficient to calculate true intra-year values.
- Same-date S&P 500 TR YTD as of 2026-07-06 remains `ไม่พบข้อมูลที่ยืนยันได้` in the
  captured official snapshot; no price-return proxy is substituted.

## EWC Missing / Unverified Data

- Issuer does not provide a full all-time maximum drawdown and recovery statistic
  in the captured product-page performance table; record as `ไม่พบข้อมูลที่ยืนยันได้`.
- The complete-year table's 2016-2020 values are official displayed values but
  rounded to one decimal; cumulative and CAGR calculations using them are
  approximate. No `*` proxy marker is used because the rows come from the issuer.
- S&P 500 current YTD is a same-date common reference comparator, not EWC's
  tracked index; EWC's issuer benchmark remains MSCI Canada Custom Capped Index.

## VOO Source Map

| Scope | Official source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:VOO` | [Vanguard VOO product page](https://investor.vanguard.com/investment-products/etfs/profile/voo) | Fund identity, current NAV/price, NAV YTD, annual NAV Total Return, rolling 10-year return, expense ratio, and distributions | Annual rows 2025-12-31; rolling/YTD performance 2026-06-30 and 2026-07-09; NAV/price 2026-07-09; distribution 2026-06-30; expense ratio 2026-04-28 |
| `NYSE Arca:VOO` | [Vanguard VOO fact sheet](https://institutional.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F0968.pdf) | Exchange, inception, passive full-replication classification, S&P 500 issuer benchmark, return definition, and 3-year standard deviation | 2026-03-31 |
| `S&P 500 TR` | [S&P DJI index returns](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization) | Same-date current YTD common-reference comparator | 2026-07-09 |
| `S&P 500 TR cache` | [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) | Complete-year S&P 500 Total Return rows | 2016-2025; reference as-of 2025-12-31 |

## VOO Reporting Scope

- Currency: USD. Fund series: official pre-tax `NAV Total Return`, net of fund
  expenses and including reinvested dividends and capital-gains distributions.
- VOO is a supported passive, index-tracking U.S. large-cap equity ETF employing
  full replication; issuer benchmark is `S&P 500 Index`.
- Official annual coverage: complete calendar years 2016-2025. The cached S&P
  500 TR convention uses the same window and return basis.
- Latest NAV/market price: USD `690.90` / `690.69` as of 2026-07-09. This is a
  dated verification and is not presented as a current 2026-07-13 quote.
- Latest distribution: USD `1.9622` per share, payable 2026-06-30; distribution
  schedule is quarterly. Distribution analysis was not requested.

## VOO Extracted Facts

| Year | VOO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 11.93% | 11.96% |
| 2017 | 21.78% | 21.83% |
| 2018 | -4.42% | -4.38% |
| 2019 | 31.46% | 31.49% |
| 2020 | 18.35% | 18.40% |
| 2021 | 28.66% | 28.71% |
| 2022 | -18.15% | -18.11% |
| 2023 | 26.25% | 26.29% |
| 2024 | 24.98% | 25.02% |
| 2025 | 17.84% | 17.88% |

- Official rolling 10-year VOO NAV Total Return as of 2026-06-30: cumulative
  `321.27%`, CAGR `15.47%`; normalized shown calculation is `100.00 -> 421.27`
  for the `2016-06-30` to `2026-06-30` window.
- Official same-window S&P 500 benchmark: cumulative `322.71%`, CAGR `15.51%`.
- Current VOO NAV YTD: `9.97%` as of 2026-07-09; S&P 500 TR YTD: `9.98%` on
  the same date.
- VOO 2016-2025 cumulative/CAGR from rounded annual rows: `296.90%` / `14.78%`;
  cached S&P 500 TR: `298.33%` / `14.82%`.
- VOO 2021-2025 cumulative/CAGR: `95.81%` / `14.38%`; S&P 500 TR:
  `96.17%` / `14.43%`.

## VOO Missing / Unverified Data

- The Vanguard sources captured do not disclose a maximum drawdown or recovery
  series; record as `ไม่พบข้อมูลที่ยืนยันได้` rather than calculating from
  annual observations.
- Vanguard does not expose raw rolling total-return index levels; the displayed
  `100.00 -> 421.27` endpoints normalize the official cumulative return and are
  shown calculations, not source-published index levels.
- Do not mix Vanguard's quarterly table `Year-end` market-price returns with the
  annual table `Total return by NAV`; this page uses the latter exclusively.
