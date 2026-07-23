---
type: source-batch
topic: ETF performance
accessed: 2026-07-24
input_source: raw/imports/tradingview_etf_list_filtered_2026-07-22.md
input_count: 125
review_gate: local_fallback_pass
tags:
  - source/etf
---

# ETF Performance Source Batch - 2026-07-24

## Scope and gate

ใช้ `check-etf-performance` sequential queue ต่อเนื่องตามลำดับทีละ ticker. รอบนี้รวมผลถึง row `30/125`, ทำ mandatory 10-year coverage audit จาก official product page/factsheet/prospectus และใช้ local pre-save fallback เนื่องจากไม่มี independent reviewer.

## Complete evidence register

| Input ticker | Status | Canonical entity key | Primary region | Current NAV YTD / as-of | Source URL | Gap / resolution note |
|---|---|---|---|---|---|---|
| FLKR | supported | NYSE Arca:FLKR | South Korea | 86.35% (2026-07-07) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26353/SINGLCLASS/franklin-ftse-south-korea-etf/FLKR | official inception 2017-11-02; issuer 10-year NAV return `—`; available official annual rows 2018-2025 |
| VPL | supported | NYSE Arca:VPL | Asia-Pacific | 19.62% (2026-07-17) | https://investor.vanguard.com/investment-products/etfs/profile/vpl | official rolling 10Y NAV TR 177.37% / CAGR 10.74% as of 2026-05-31; annual NAV TR rows 2016-2025 |
| ISSSF | supported | LSE:SAUS | Australia | 10.27% (2026-07-21) | https://www.ishares.com/uk/professional/en/products/251851/ishares-msci-australia-ucits-etf | OTC alias; official rolling 10Y NAV TR 121.17% / CAGR 8.26% as of 2026-06-30; annual NAV TR rows 2016-2025 |
| SCJ | supported | NYSE Arca:SCJ | Japan | 16.10% (2026-07-21) | https://www.ishares.com/us/products/239666/ishares-msci-japan-smallcap-etf | official rolling 10Y NAV TR 119.60% / CAGR 8.18% as of 2026-06-30; annual NAV TR rows 2016-2025 |
| EEMA | supported | NASDAQ:EEMA | Emerging Markets | 20.51% (2026-07-22) | https://www.ishares.com/us/products/239629/ishares-msci-emerging-markets-asia-etf | official rolling 10Y NAV TR 172.29% / CAGR 10.54% as of 2026-06-30; official NAV rows 2016-2025; index change on 2018-06-01 |
| VNFGF | supported | LSE:VDJP | Japan | 16.30% (2026-05-31) | https://www.vanguard.co.uk/professional/product/etf/equity/9504/ftse-japan-ucits-etf-usd-distributing | OTC alias resolved to USD LSE ticker VDJP by ISIN IE00B95PGT31; official rolling 10Y NAV TR CAGR 9.45% as of 2026-05-31; official rolling 12-month rows; current-page NAV US$50.23 as of 2026-07-22 |
| CSKRF | supported | LSE:CSKR | South Korea | 70.53% (2026-07-21) | https://www.ishares.com/uk/professional/en/products/253733/cskr | OTC alias; official rolling 10Y NAV TR cumulative 369.63% / CAGR 16.73% as of 2026-06-30; official calendar NAV rows 2016-2025; benchmark change 2020-02-11 |
| GSJY | supported | NYSE Arca:GSJY | Japan | 12.86% (2026-06-30) | https://am.gs.com/public-assets/documents/5747f795-24d6-11ef-870d-ed3a247c783e | official rolling 10Y NAV TR CAGR 9.29% as of 2026-06-30; official calendar NAV/ActiveBeta index rows 2017-2025; 2016 inception partial; rules-based index and not actively managed |
| IHSEF | supported | LSE:IAPD | Asia-Pacific | 14.55% (2026-07-21) | https://www.ishares.com/uk/professional/en/products/251567/iapd?siteEntryPassthrough=true&switchLocale=y | OTC alias resolved to official LSE:IAPD listing; official rolling 10Y NAV TR CAGR 6.75% as of 2026-06-30; official calendar NAV/benchmark rows 2016-2025; physical/replicated passive equity; TER 0.59% |
| MINV | unsupported ETF type | NYSE Arca:MINV | Asia | not applicable | https://us.matthewsasia.com/funds/etfs/asia-innovators-active-etf/ | Matthews identifies MINV as an active, high-conviction, all-cap fundamental equity ETF; active share 74.8% as of 2026-06-30; passive ETF scope excludes active funds |

## CSKRF Sequential Queue Record

- Input row: `27/125`; input ticker: `CSKRF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:CSKR`; iShares' official product page maps ISIN `IE00B5W4TY14` to London Stock Exchange USD ticker `CSKR`, identifies the share class as iShares MSCI Korea UCITS ETF USD (Acc), issuing company iShares VII plc, physical/replicated, benchmark MSCI Korea 20/35 Index, and launch `2010-08-24`. `CSKRF` is retained as the input OTC alias; no provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page had stale YTD and no benchmark, inception, rolling 10-year result, or annual table. Rechecking the current official product page, March 2026 factsheet and official annual-report/document links confirms a genuine `10.00` elapsed-year NAV TR window; this was a page gap, not a history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `369.63%` and average annual `16.73%` for `2016-06-30` to `2026-06-30`. Normalized TR is `100.00` to `469.63`; raw NAV endpoints are not disclosed.
- Official calendar observations: iShares publishes NAV and benchmark rows for `2016-2025`. NAV rows compound to `141.88%` / CAGR `9.23%`; common `2021-2025` rows compound to `21.32%` / CAGR `3.94%`; positive / negative years are `2 / 3`. S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`.
- Benchmark caveat: iShares states that the benchmark changed from MSCI Korea Index to MSCI Korea 20/35 Index on `2020-02-11`; benchmark rows are kept separate from the fund NAV TR metric.
- Official current observation: iShares reports NAV `US$462.74` and NAV Total Return YTD `70.53%` as of `2026-07-21`; total expense ratio `0.65%`, 77 holdings as of `2026-07-20`, and 3-year standard deviation `44.57%` as of `2026-06-30`. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### CSKRF / CSKR Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:CSKR` | [iShares CSKR product and performance page](https://www.ishares.com/uk/professional/en/products/253733/cskr) | Canonical listing, ISIN/share class, fund identity, physical/replicated classification, benchmark, inception, annual NAV/benchmark rows, rolling 10Y NAV TR, current NAV/YTD, fees and risks | Page accessed `2026-07-24`; rolling summary `2026-06-30`; current NAV/YTD `2026-07-21`; holdings `2026-07-20` |
| `LSE:CSKR` | [iShares CSKR factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/cskr-ishares-msci-korea-ucits-etf-usd-acc-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) | Corroborates passive/physical/replicated structure, benchmark change, launch date, fee, NAV basis and risk disclosures | Factsheet March 2026; performance data through `2026-03-31` |
| `iShares VII plc` | Official annual report/document links on the CSKR product page | Legal structure and document cross-check | Page accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### CSKRF / CSKR Raw Observations And Calculations

| Year | CSKR NAV TR | MSCI Korea benchmark TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 8.0% | 8.7% | 11.96% |
| 2017 | 46.4% | 47.3% | 21.83% |
| 2018 | -21.4% | -20.9% | -4.38% |
| 2019 | 11.8% | 12.5% | 31.49% |
| 2020 | 43.5% | 44.7% | 18.40% |
| 2021 | -8.4% | -8.0% | 28.71% |
| 2022 | -29.2% | -29.0% | -18.11% |
| 2023 | 21.8% | 22.9% | 26.29% |
| 2024 | -22.9% | -22.5% | 25.02% |
| 2025 | 99.2% | 99.8% | 17.88% |

- Official rolling 10-year NAV TR is `+369.63%` with CAGR `16.73%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `469.63`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+141.88%` and annualize to `9.23%` over 10 complete calendar years. Common rows `2021-2025` compound to `+21.32%` and annualize to `3.94%`; positive / negative years are `2 / 3`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; CSKR trails by approximately `10.49 pp` CAGR in that common window.
- Official current NAV TR YTD is `+70.53%` as of `2026-07-21`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### CSKRF / CSKR Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, ISIN/share-class match, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, benchmark change, as-of dates, rankings, filenames, South Korea region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## GSJY Sequential Queue Record

- Input row: `28/125`; input ticker: `GSJY`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:GSJY`; Goldman Sachs' official factsheet identifies ticker GSJY, NYSE Arca, inception `2016-03-02`, and the Goldman Sachs ActiveBeta Japan Equity Index. The official summary prospectus states the Fund is not actively managed; this is a rules-based smart-beta/index-tracking equity ETF.
- Mandatory coverage audit: the existing page lacked the benchmark, inception, rolling 10-year result and annual rows. Rechecking the official June 2026 factsheet and summary prospectus confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; 2016 calendar year remains partial and is not labeled complete.
- Official rolling performance: Goldman Sachs reports NAV 10-year annualized total return `9.29%` as of `2026-06-30`. Raw endpoints/cumulative are not disclosed; normalized TR `100.00` to `243.11` is calculated from the rounded CAGR.
- Official calendar observations: NAV rows are 2017 `24.52%`, 2018 `-10.52%`, 2019 `18.28%`, 2020 `12.52%`, 2021 `0.60%`, 2022 `-15.60%`, 2023 `18.92%`, 2024 `9.09%`, and 2025 `25.07%`; the corresponding ActiveBeta index rows are `23.99%`, `-12.88%`, `19.61%`, `14.44%`, `1.71%`, `-16.65%`, `20.32%`, `8.28%`, and `24.60%`. NAV 2017-2025 cumulative is `104.29%` / CAGR `8.26%`; common 2021-2025 cumulative is `37.76%` / CAGR `6.62%`; positive/negative years are `3/2` in the common window.
- S&P 500 rows use the cached USD TR convention as of `2025-12-31`; common 2021-2025 CAGR is `14.43%`, so GSJY trails by `7.81 pp` CAGR.
- Official current observation: NAV YTD is `12.86%` as of `2026-06-30`; latest NAV price is `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed capture; total expense ratio is `0.25%` and holdings are `155`.

### GSJY Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:GSJY` | [Goldman Sachs GSJY factsheet](https://am.gs.com/public-assets/documents/5747f795-24d6-11ef-870d-ed3a247c783e) | identity, exchange, inception, passive/not actively managed classification, index, NAV TR, annual rows, fees and risk | Factsheet as of `2026-06-30` |
| `NYSE Arca:GSJY` | [Goldman Sachs summary prospectus](https://am.gs.com/public-assets/documents/179d857b-24e3-11ef-ad18-377468fbef87?view=true) | objective, not-actively-managed classification, fund structure and risk | Prospectus accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | cached USD TR rows as of `2025-12-31` |

### GSJY Raw Observations And Calculations

| Year | GSJY NAV TR | ActiveBeta Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed (partial inception year) | not disclosed | 11.96% |
| 2017 | 24.52% | 23.99% | 21.83% |
| 2018 | -10.52% | -12.88% | -4.38% |
| 2019 | 18.28% | 19.61% | 31.49% |
| 2020 | 12.52% | 14.44% | 18.40% |
| 2021 | 0.60% | 1.71% | 28.71% |
| 2022 | -15.60% | -16.65% | -18.11% |
| 2023 | 18.92% | 20.32% | 26.29% |
| 2024 | 9.09% | 8.28% | 25.02% |
| 2025 | 25.07% | 24.60% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `9.29%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `243.11`, actual years `10.00`. The normalized end is calculated from the rounded issuer CAGR; raw endpoints are not disclosed.
- Official calendar rows `2017-2025` compound to `104.29%` / CAGR `8.26%`; common rows `2021-2025` compound to `37.76%` / CAGR `6.62%`.

### GSJY Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## IHSEF Sequential Queue Record

- Input row: `29/125`; input ticker: `IHSEF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:IAPD`; the input OTC alias is resolved by iShares' official listing table to the iShares Asia Pacific Dividend UCITS ETF, ISIN `IE00B14X4T88`, with London Stock Exchange ticker `IAPD` in GBP and the same fund's USD line `IDAP`. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page already had calendar rows but lacked verified benchmark, inception, rolling 10-year calculation, fee and current-source details. Rechecking the current official iShares product page and factsheet confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this was a page-data gap, not a history gap.
- Type gate: official iShares identifies the asset class as Equity, the product as physical/replicated, and the objective as tracking an index of 50 high-dividend Asia-Pacific stocks. It is a passive/index-tracking equity ETF, not a bond, commodity, currency trust, active, leveraged, inverse, option-income or derivative-heavy fund.
- Official rolling performance: iShares reports NAV Total Return annualised `6.75%` for the 10-year window as of `2026-06-30`. Raw NAV endpoints are not disclosed; normalized TR `100.00` to `192.17` is calculated from the rounded CAGR.
- Official calendar observations: NAV rows 2016-2025 are `20.5%`, `16.6%`, `-15.1%`, `14.4%`, `-10.2%`, `4.0%`, `-2.3%`, `13.8%`, `5.9%`, and `29.7%`; the official benchmark rows are `21.0%`, `16.8%`, `-14.8%`, `14.9%`, `-9.6%`, `4.4%`, `-1.9%`, `14.3%`, `6.5%`, and `30.4%`. NAV 2016-2025 rows compound to approximately `94.63%` / CAGR `6.89%`; common 2021-2025 rows compound to `58.82%` / CAGR `9.69%`; positive/negative years are `4/1` in the common window.
- Benchmark caveat: iShares notes that the Fund used a different benchmark before `2020-06-22`; the official benchmark rows are retained separately from the fund NAV TR metric.
- S&P 500 rows use the cached USD TR convention as of `2025-12-31`; common 2021-2025 CAGR is `14.43%`, so IHSEF trails by approximately `4.74 pp` CAGR.
- Official current observations: NAV TR YTD is `14.55%` and NAV is `US$31.26`, both as of `2026-07-21`; TER is `0.59%`, holdings are `50` as of `2026-07-16`, and 3-year standard deviation is `14.36%` as of `2026-06-30`. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### IHSEF / IAPD Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:IAPD` | [iShares IAPD official product and performance page](https://www.ishares.com/uk/professional/en/products/251567/iapd?siteEntryPassthrough=true&switchLocale=y) | canonical listing, ISIN, fund identity, equity/passive physical-replicated classification, benchmark, inception, NAV TR, annual rows, current NAV/YTD, fee and risk data | Page accessed `2026-07-24`; rolling summary `2026-06-30`; NAV/YTD `2026-07-21`; holdings `2026-07-16` |
| `LSE:IAPD` | [iShares IAPD official factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/iapd-ishares-asia-pacific-dividend-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) | corroborates share class, passive objective, ISIN, fee, distribution policy, benchmark and fund structure | Factsheet March 2026; performance/portfolio data through `2026-03-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | cached USD TR rows as of `2025-12-31` |

### IHSEF / IAPD Raw Observations And Calculations

| Year | IAPD NAV TR | Dow Jones Asia/Pacific Select Dividend 50 Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 20.5% | 21.0% | 11.96% |
| 2017 | 16.6% | 16.8% | 21.83% |
| 2018 | -15.1% | -14.8% | -4.38% |
| 2019 | 14.4% | 14.9% | 31.49% |
| 2020 | -10.2% | -9.6% | 18.40% |
| 2021 | 4.0% | 4.4% | 28.71% |
| 2022 | -2.3% | -1.9% | -18.11% |
| 2023 | 13.8% | 14.3% | 26.29% |
| 2024 | 5.9% | 6.5% | 25.02% |
| 2025 | 29.7% | 30.4% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `6.75%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `192.17`, actual years `10.00`. The normalized end is calculated from the rounded issuer CAGR; raw endpoints are not disclosed.
- Calendar rows `2016-2025` compound to approximately `94.63%` / CAGR `6.89%`; common rows `2021-2025` compound to `58.82%` / CAGR `9.69%`.

### IHSEF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, ISIN/share-class match, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, benchmark-change caveat, as-of dates, rankings, filenames, Asia-Pacific region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## MINV Sequential Queue Record

- Input row: `30/125`; input ticker: `MINV`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:MINV`; Matthews' official fund page identifies the ticker, primary exchange, inception `2022-07-13`, benchmark `MSCI All Country Asia ex Japan Index`, and the Matthews Asia Innovators Active ETF. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. The official strategy is an active, high-conviction, all-cap fundamental approach investing at least 80% of net assets in companies Matthews believes are innovators. Official portfolio characteristics report active share `74.8%` as of `2026-06-30`; the page explicitly labels the product `Active ETF`. This is outside the required passive/index-tracking equity ETF scope.
- Per the type gate, no 10-year historical performance calculation, annual table, performance page, region performance row or S&P 500 comparison was created. Official current observations are not used as a performance deliverable.

### MINV Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:MINV` | [Matthews Asia Innovators Active ETF official page](https://us.matthewsasia.com/funds/etfs/asia-innovators-active-etf/) | canonical ticker/exchange, active classification, strategy, inception, benchmark and active share | Page accessed `2026-07-24`; portfolio characteristics `2026-06-30` |
| `NYSE Arca:MINV` | [Matthews MINV factsheet](https://us.matthewsasia.com/siteassets/resources/fund-documents/factsheets/etfs/fact_sheet_minv.pdf) | corroborates active strategy, inception, exchange, benchmark and fee | Factsheet March 2026 |

### MINV Pre-save Review Note

- No performance page save was required after the unsupported type gate. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-versus-active classification, terminal-status selection, source URL, filename decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## VNFGF Sequential Queue Record

- Input row: `26/125`; input ticker: `VNFGF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:VDJP`; Vanguard's official product page and May 2026 factsheet identify Vanguard FTSE Japan UCITS ETF (USD) Distributing, ISIN `IE00B95PGT31`, USD London Stock Exchange ticker `VDJP`, benchmark `FTSE Japan Index`, inception `2013-05-21`, passive physical/index strategy, and Vanguard Funds PLC as legal entity. `VNFGF` is retained as the input OTC alias; no provider slug or guessed exchange is used.
- Mandatory coverage audit: the previous source register left VNFGF unresolved because the primary listing code was not verified. Rechecking Vanguard's product page, factsheet, current prospectus and annual-report links resolves the share class to LSE:VDJP and confirms a genuine `10.00` elapsed-year NAV TR window. This was an alias/listing-resolution gap, not a history gap.
- Official rolling performance: Vanguard reports NAV-to-NAV total returns with gross income invested and all dividends/capital-gains distributions reinvested. The factsheet as of `2026-05-31` reports 10-year NAV annualized performance `9.45%` for `2016-06-01` to `2026-05-31`; normalized TR is `100.00` to `246.69`, calculated as `100 × (1 + 9.45%)^10` from the rounded issuer CAGR, not an official raw endpoint.
- Official annual observations: Vanguard publishes rolling 12-month NAV rows `2016-06-01 to 2026-05-31`, which compound to approximately `146.61%` and annualize to `9.45%` using the displayed rounded rows. These are not calendar-year rows; calendar 2021-2025 CAGR remains `not disclosed`. The official FTSE Japan benchmark rows are kept beside them.
- S&P 500 comparison: cached complete-calendar-year USD Total Return rows 2016-2025 are shown separately; they compound to `298.33%` / CAGR `14.82%`. This is directional only because the S&P window is calendar-year and the VDJP window is June-May.
- Official current observations: Vanguard's product page reports NAV `US$50.23` at closure `2026-07-22`; the latest standardized YTD disclosed in the official factsheet is `16.30%` as of `2026-05-31`. Ongoing charges figure is `0.10%`, Japan exposure `100.0%`, and holdings `476` as of `2026-06-30`. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### VNFGF / VDJP Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:VDJP` | [Vanguard FTSE Japan UCITS ETF USD Distributing product page](https://www.vanguard.co.uk/professional/product/etf/equity/9504/ftse-japan-ucits-etf-usd-distributing) | Canonical share-class mapping, exchange tickers, ISIN, fund identity, passive/physical classification, benchmark, inception, current NAV and holdings | Page accessed `2026-07-24`; current NAV `2026-07-22`; portfolio data `2026-06-30` |
| `LSE:VDJP` | [Vanguard VDJP factsheet](https://fund-docs.vanguard.com/FTSE_Japan_UCITS_ETF_USD_Distributing_9504_EU_INT_UK_EN.pdf) | Rolling 12-month NAV TR rows, 10-year NAV CAGR, reinvestment/NAV basis, fees, benchmark, exchange tickers and ISIN | Factsheet as of `2026-05-31` |
| `Vanguard Funds PLC` | [Vanguard ETF prospectus](https://fund-docs.vanguard.com/etf-prospectus-en.pdf) and annual-report link | Legal structure and official document cross-check | Prospectus dated `2026-06-02`; annual-report link accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### VNFGF / VDJP Raw Observations And Calculations

| Official rolling 12-month period | VDJP NAV TR | FTSE Japan Index TR |
|---|---:|---:|
| 2016-06-01 to 2017-05-31 | 15.56% | 15.76% |
| 2017-06-01 to 2018-05-31 | 14.79% | 14.94% |
| 2018-06-01 to 2019-05-31 | -10.92% | -10.74% |
| 2019-06-01 to 2020-05-31 | 6.92% | 7.06% |
| 2020-06-01 to 2021-05-31 | 24.81% | 24.97% |
| 2021-06-01 to 2022-05-31 | -13.73% | -13.64% |
| 2022-06-01 to 2023-05-31 | 4.48% | 4.57% |
| 2023-06-01 to 2024-05-31 | 17.73% | 17.85% |
| 2024-06-01 to 2025-05-31 | 11.48% | 11.59% |
| 2025-06-01 to 2026-05-31 | 32.20% | 32.31% |

- Official rolling 10-year NAV TR CAGR is `9.45%` for `2016-06-01` to `2026-05-31`; actual years `10.00`; normalized end `246.69` is derived from the rounded CAGR.
- Official displayed rolling rows compound to approximately `+146.61%` and annualize to `9.45%`; calendar-year 2021-2025 CAGR is `not disclosed`.
- S&P 500 TR calendar rows 2016-2025 compound to `+298.33%` / CAGR `14.82%`; this comparison is not date-aligned.
- Latest standardized NAV TR YTD is `+16.30%` as of `2026-05-31`; current-page NAV is `US$50.23` as of `2026-07-22`. Market-price return is kept separate.

### VNFGF / VDJP Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, ISIN/share-class match, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, rolling annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## EEMA Sequential Queue Record

- Input row: `25/125`; input ticker: `EEMA`; terminal status: `completed_10Y`.
- Canonical entity key: `NASDAQ:EEMA`; iShares' official product page and factsheet identify ticker `EEMA` on NASDAQ, fund inception `2012-02-08`, asset class `Equity`, passive/index-tracking exposure, and benchmark `MSCI EM Asia Custom Capped Index (Net)`. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page had only 2021-2025 annual rows, stale YTD, and no benchmark, inception, or rolling 10-year calculation. Rechecking the current official product page, official factsheet, summary prospectus, and official document links confirms a genuine `10.00` elapsed-year NAV TR window; this was a page gap, not a history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `172.29%` and average annual `10.54%` for `2016-06-30` to `2026-06-30`. Normalized TR is `100.00` to `272.29`; raw NAV endpoints are not disclosed.
- Official calendar observations: NAV rows `2016-2020` were recovered from the official summary prospectus, while `2021-2025` rows were confirmed in the current official product page and March 2026 factsheet. Calendar rows compound to `121.24%` / CAGR `8.26%`; common `2021-2025` rows compound to `17.94%` / CAGR `3.36%`. S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`.
- Index/source caveat: the official factsheet and prospectus state that on `2018-06-01` EEMA began tracking MSCI EM Asia Custom Capped Index (Net); historical index data before that date is MSCI Emerging Markets Asia Index (Net). The rolling 10-year fund NAV TR remains the primary metric; benchmark rows are kept separate.
- Official current observation: iShares reports NAV `US$112.84` and NAV Total Return YTD `20.51%` as of `2026-07-22`; expense ratio `0.49%`, 879 holdings, and key geography exposures China `31.53%`, Taiwan `31.06%`, South Korea `16.82%`, India `16.09%` as of the same date. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### EEMA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:EEMA` | [iShares EEMA product and performance page](https://www.ishares.com/us/products/239629/ishares-msci-emerging-markets-asia-etf) | Canonical listing, fund identity, passive/index classification, benchmark, inception, rolling NAV TR, current NAV/YTD, annual 2021-2025 rows, fees and exposures | Page accessed `2026-07-24`; rolling/annual performance `2026-06-30` / `2025-12-31`; current NAV/YTD `2026-07-22` |
| `NASDAQ:EEMA` | [iShares EEMA factsheet](https://www.ishares.com/us/literature/fact-sheet/eema-ishares-msci-emerging-markets-asia-etf-fund-fact-sheet-en-us.pdf) | Corroborates passive structure, benchmark, launch date, 2021-2025 NAV rows, index change, fee and risk basis | Factsheet as of `2026-03-31`; its 10-year field is older and not used instead of the current product-page figure |
| `NASDAQ:EEMA` | [iShares EEMA summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-emerging-markets-asia-etf-8-31.pdf) | Historical calendar rows 2016-2020, fund performance basis, index splice and inception confirmation | Prospectus accessed `2026-07-24`; performance table through `2024-12-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### EEMA Raw Observations And Calculations

| Year | EEMA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 5.59% | 11.96% |
| 2017 | 41.94% | 21.83% |
| 2018 | -15.54% | -4.38% |
| 2019 | 18.36% | 31.49% |
| 2020 | 25.20% | 18.40% |
| 2021 | -4.19% | 28.71% |
| 2022 | -21.45% | -18.11% |
| 2023 | 6.98% | 26.29% |
| 2024 | 10.71% | 25.02% |
| 2025 | 32.32% | 17.88% |

- Official rolling 10-year NAV TR is `+172.29%` with CAGR `10.54%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `272.29`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+121.24%` and annualize to `8.26%` over 10 complete calendar years. Common rows `2021-2025` compound to `+17.94%` and annualize to `3.36%`; positive / negative years are `3 / 2`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; EEMA trails by approximately `11.07 pp` CAGR in that common window.
- Official current NAV TR YTD is `+20.51%` as of `2026-07-22`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### EEMA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows from official documents, S&P 500 basis/window, index splice, as-of dates, rankings, filenames, Emerging Markets region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.
| CQQQ | supported | NYSE Arca:CQQQ | China | not disclosed (not disclosed) | https://www.invesco.com/us/en/financial-products/etfs/invesco-china-technology-etf.html | official complete calendar NAV TR rows 2016-2025; 10Y calendar CAGR 4.44%; predecessor/index methodology breaks disclosed; current NAV/YTD not disclosed |
| ISMJF | supported | LSE:CPXJ | Asia-Pacific | 8.15% (2026-07-08) | https://www.ishares.com/uk/professional/en/products/253735/ishares-core-msci-pacific-ex-japan-ucits-etf?siteEntryPassthrough=true&switchLocale=y | OTC alias; official rolling 10Y NAV TR 108.94% / CAGR 7.65% as of 2026-06-30; annual NAV TR rows 2016-2025 |

## FLKR Sequential Queue Record

- Input row: `18/125`; input ticker: `FLKR`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:FLKR`; Franklin's official page identifies ticker `FLKR`, listing exchange `NYSE Arca`, fund inception `2017-11-02`, asset class `Equity`, and indexed/passive exposure to the FTSE South Korea Capped Index-NR. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page contained 2018-2025 annual rows only. Rechecking the official product page and factsheet confirms inception `2017-11-02`, official 10-year NAV return `—`, and no official 10.00-year NAV/TR window as of 2026-07-24. The 2017 partial inception year is excluded; 2018-2025 gives eight complete calendar years.
- Official current observations: NAV `US$59.71`, NAV TR YTD `86.35%`, and 157 holdings as of `2026-07-07`; gross/net expense ratio `0.09%` as of `2025-08-01`; 3-year NAV standard deviation `34.71%` in the factsheet as of `2026-03-31`.

### FLKR Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:FLKR` | [Franklin FLKR product and performance page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26353/SINGLCLASS/franklin-ftse-south-korea-etf/FLKR) | Fund identity, exchange, benchmark, inception, passive classification, fee, current NAV/YTD, annual NAV returns, and official 10-year availability field | Page accessed `2026-07-24`; current NAV/YTD/holdings `2026-07-07`; average annual performance `2026-05-31` |
| `NYSE Arca:FLKR` | [Franklin FLKR factsheet](https://www.franklintempleton.com/forms-literature/download/FLKR-FF) | Corroborates NAV-return basis, distribution reinvestment, fee, inception, indexed category, 2018-2025 history, and 10-year unavailable field | Factsheet as of `2026-03-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### FLKR Raw Observations And Calculations

| Year | FLKR NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -20.34% | -4.38% |
| 2019 | 8.05% | 31.49% |
| 2020 | 42.82% | 18.40% |
| 2021 | -6.59% | 28.71% |
| 2022 | -28.31% | -18.11% |
| 2023 | 20.99% | 26.29% |
| 2024 | -19.46% | 25.02% |
| 2025 | 91.79% | 17.88% |

- Official available-period rows `2018-2025` compound to `+53.85%` and annualize to `5.53%` over `8.00 complete calendar years`. Normalized TR is `100.00` to `153.85`; raw NAV endpoint levels are `ไม่พบข้อมูลที่ยืนยันได้`.
- Complete common rows `2021-2025` compound to `+25.15%` and annualize to `4.59%`. S&P 500 TR compounds to `+96.17%` and annualizes to `14.43%`; FLKR trails by approximately `9.84 pp` CAGR.
- Official 10-year NAV TR is `unavailable`: issuer shows `—`, and inception `2017-11-02` to access date `2026-07-24` is `8.72 years` / `3,186 days`, below the required `10.00 elapsed years`.
- Official current NAV TR YTD is `+86.35%` as of `2026-07-07`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### FLKR Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, South Korea region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## CNXT Sequential Queue Record

- Input row: `24/125`; input ticker: `CNXT`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:CNXT`; VanEck's official product page and factsheet identify `CNXT` on NYSE Arca, inception `2014-07-23`, passive/index-tracking equity exposure, and the `ChiNext Index (SZ988107)`. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page had stale YTD data and no benchmark, inception, rolling 10-year result, or annual table. Rechecking the current official product page and factsheet confirms a genuine `10.00` elapsed-year NAV TR window; this was a page gap, not a history gap. The issuer also discloses a methodology/index change: before market close `2021-12-10`, the table reflects SME-ChiNext 100 Index (CNI6109); thereafter it reflects ChiNext Index (SZ988107).
- Official rolling performance: VanEck reports CNXT NAV average annual total return `7.37%` for the month ended `2026-06-30`, used as the 10-year CAGR for `2016-06-30` to `2026-06-30`. Raw start/end NAV TR values are not disclosed. Normalized TR is `100.00` to `203.62`, calculated as `100 × (1 + 7.37%)^10` from the rounded issuer CAGR and explicitly not treated as an official endpoint.
- Official calendar-year NAV rows: not disclosed in the reviewed issuer capture, so 2016-2025 CNXT rows, 2021-2025 CAGR, best/worst years, and common-window cumulative return remain `not disclosed`. S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`.
- Official current observation: VanEck reports NAV `US$51.14` and NAV YTD `16.05%` as of `2026-07-22`; net expense ratio `0.65%`, gross `1.00%`, and 99 holdings as of the same date. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### CNXT Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:CNXT` | [VanEck CNXT product and performance page](https://www.vaneck.com/us/en/investments/chinext-innovators-etf-cnxt/) | Fund identity, exchange, passive/index classification, benchmark, inception, rolling NAV TR CAGR, current NAV/YTD, fees, holdings and methodology break | Page accessed `2026-07-24`; rolling/annual performance `2026-06-30`; current NAV/YTD and holdings `2026-07-22` |
| `NYSE Arca:CNXT` | [VanEck CNXT factsheet](https://www.vaneck.com/us/en/investments/chinext-innovators-etf-cnxt-fact-sheet.pdf/) | Corroborates index, inception, NAV return basis, fees, holdings and issuer performance table | Factsheet as of `2026-06-30` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### CNXT Raw Observations And Calculations

| Year | CNXT NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | 11.96% |
| 2017 | not disclosed | 21.83% |
| 2018 | not disclosed | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | not disclosed | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |

- Official rolling 10-year NAV TR CAGR is `7.37%` for `2016-06-30` to `2026-06-30`; actual years `10.00`; normalized end `203.62` is derived from the rounded CAGR, not an official raw endpoint.
- 2021-2025 common-window CAGR and cumulative return: `not disclosed` because annual CNXT NAV TR rows are not disclosed.
- Current NAV TR YTD is `16.05%` as of `2026-07-22`; market-price return is kept separate. Daily NAV history for max drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### CNXT Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, calendar-row gap, S&P 500 basis/window, methodology/index break, as-of dates, rankings, filenames, China region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## ISMJF Sequential Queue Record

- Input row: `23/125`; input ticker: `ISMJF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:CPXJ`; iShares' official listing table maps the input OTC alias to London Stock Exchange ticker `CPXJ`, ISIN `IE00B52MJY50`. The official product page identifies the share class as iShares Core MSCI Pacific ex-Japan UCITS ETF, issued by iShares VII plc. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page lacked annual rows, inception, benchmark and rolling performance. Rechecking the official iShares product/performance view and factsheet confirms physical/replicated passive equity structure, inception `2010-01-12`, and official 10.00-year NAV TR coverage; this was a page gap, not a history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `108.94%` and annualised `7.65%` for `2016-06-30` to `2026-06-30`. Normalized TR is `100.00` to `208.94`; actual years `10.00`.
- Official annual observations: iShares calendar NAV rows `2016-2025` and issuer benchmark rows were captured from the official performance view. The source states performance is NAV-based with gross income reinvested where applicable.
- Official current observation: iShares reports NAV `US$237.50` and NAV Total Return YTD `8.15%` as of `2026-07-08`; market-price return is kept separate.

### ISMJF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:CPXJ` | [iShares CPXJ product and performance page](https://www.ishares.com/uk/professional/en/products/253735/ishares-core-msci-pacific-ex-japan-ucits-etf?siteEntryPassthrough=true&switchLocale=y) | Canonical identity/listing, passive physical/replicated classification, benchmark, inception, fee, holdings, annual NAV TR, rolling 10Y and current NAV/YTD | Page accessed `2026-07-24`; rolling summary `2026-06-30`; current NAV/YTD `2026-07-08` |
| `LSE:CPXJ` | [iShares CPXJ factsheet](https://www.ishares.com/nl/professionele-belegger/nl/literature/fact-sheet/cspxj-ishares-core-msci-pacific-ex-japan-ucits-etf-fund-fact-sheet-en-nl.pdf?siteEntryPassthrough=true&switchLocale=y) | Corroborates passive structure, benchmark, launch/fee and NAV-return basis | Issuer factsheet 2026-Q1/2026-03-31 |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### ISMJF Raw Observations And Calculations

| Year | ISMJF / CPXJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.70% | 11.96% |
| 2017 | 25.80% | 21.83% |
| 2018 | -10.40% | -4.38% |
| 2019 | 18.20% | 31.49% |
| 2020 | 6.40% | 18.40% |
| 2021 | 4.70% | 28.71% |
| 2022 | -6.10% | -18.11% |
| 2023 | 6.30% | 26.29% |
| 2024 | 4.50% | 25.02% |
| 2025 | 20.40% | 17.88% |

- Official rolling 10-year NAV TR is `+108.94%` with CAGR `7.65%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `208.94`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+100.75%` and annualize to `7.22%` over 10 complete calendar years. Common rows `2021-2025` compound to `+31.49%` and annualize to `5.63%`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; ISMJF/CPXJ trails by approximately `8.80 pp` CAGR.
- Official current NAV TR YTD is `+8.15%` as of `2026-07-08`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### ISMJF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Asia-Pacific region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## CQQQ Sequential Queue Record

- Input row: `22/125`; input ticker: `CQQQ`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:CQQQ`; Invesco's SEC summary prospectus identifies CQQQ on NYSE Arca, inception `2009-12-08`, asset class equity exposure, full-replication implementation and the `FTSE China Incl A 25% Technology Capped Index`. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page already contained 2016-2025 annual rows but lacked the official benchmark, inception, rolling/complete-window calculation and continuity caveat. Rechecking the Invesco product link, official factsheet link and SEC prospectus confirms 10 complete calendar years of NAV performance; this is a data/documentation gap, not a history-length gap.
- Strategy continuity audit: the SEC prospectus states CQQQ succeeded the Guggenheim China Technology ETF after the `2018-05-18` reorganization and that performance before that date belongs to the predecessor. It also states the current FTSE index began `2019-06-22`, with a blended AlphaShares/FTSE series before then. The 10-year result is therefore accepted as historical calendar coverage with an explicit strategy/index break, not as a continuous current-methodology series.
- Official annual observations: calendar NAV TR rows `2016-2025` were retained from the verified Invesco performance capture. Official annual rows compound to `+54.48%`; normalized TR is `100.00` to `154.48`; actual coverage is `10.00` complete calendar years and CAGR `4.44%`.
- Official current observation: current NAV/YTD was `ไม่พบข้อมูลที่ยืนยันได้` in the Invesco capture as of `2026-07-24`; no value is backfilled from a secondary provider.

### CQQQ Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:CQQQ` | [Invesco CQQQ product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-china-technology-etf.html) | Issuer product identity and official performance-document entry point | Page accessed `2026-07-24`; current NAV/YTD not disclosed in capture |
| `NYSE Arca:CQQQ` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1378872/000119312525040714/d834062d497k.htm) | Exchange, inception, index, full-replication/passive structure, fee, predecessor and methodology continuity | Prospectus dated `2025-02-28`; performance periods through `2024-12-31` |
| `NYSE Arca:CQQQ` | [Invesco CQQQ factsheet](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/cqqq-invesco-china-technology-etf-fact-sheet.pdf) | Official issuer performance document link for calendar and standardized NAV returns | Latest indexed issuer factsheet capture `2026-Q1`; current extraction did not expose current NAV/YTD |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### CQQQ Raw Observations And Calculations

| Year | CQQQ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -0.07% | 11.96% |
| 2017 | 72.54% | 21.83% |
| 2018 | -34.21% | -4.38% |
| 2019 | 32.46% | 31.49% |
| 2020 | 58.33% | 18.40% |
| 2021 | -25.13% | 28.71% |
| 2022 | -29.74% | -18.11% |
| 2023 | -16.97% | 26.29% |
| 2024 | 11.24% | 25.02% |
| 2025 | 33.65% | 17.88% |

- Official complete calendar rows `2016-2025` compound to `+54.48%` and annualize to `4.44%` over `10.00` complete calendar years. Normalized TR is `100.00` to `154.48`.
- Common rows `2021-2025` compound to `-35.06%` and annualize to `-8.27%`. S&P 500 TR compounds to `+96.17%` and annualizes to `14.43%`; CQQQ trails by approximately `22.70 pp` CAGR.
- Current NAV/YTD: `ไม่พบข้อมูลที่ยืนยันได้`; daily NAV history sufficient for max drawdown and recovery is also `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### CQQQ Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, issuer identity, passive-equity classification, inception and 10-calendar-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, predecessor/index breaks, as-of dates, rankings, filenames, China region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## SCJ Sequential Queue Record

- Input row: `21/125`; input ticker: `SCJ`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:SCJ`; iShares' official U.S. page identifies the product, exchange, fund launch `2007-12-20`, asset class `Equity`, benchmark `MSCI Japan Small Cap Index (Net)`, expense ratio `0.50%`, and ticker `SCJ`. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page contained only 2021-2025 rows and no inception, benchmark or rolling calculation. Rechecking the official U.S./international performance views and factsheet confirms official 10.00-year NAV TR coverage; the existing page gap was repaired rather than treated as a history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `119.60%` and average annual return `8.18%` for `2016-06-30` to `2026-06-30`. Normalized TR is `100.00` to `219.60`; actual years `10.00`.
- Official annual observations: the international iShares performance view supplies NAV and issuer benchmark rows for `2016-2025`; the U.S. factsheet corroborates precise NAV rows for `2021-2025`. The source states growth-of-hypothetical-investment performance assumes reinvestment of dividends/capital gains and deducts fund expenses.
- Official current observation: the iShares international performance view reports NAV `US$105.49` and NAV Total Return YTD `16.10%` as of `2026-07-21`; the U.S. page's earlier observation was `14.73%` as of `2026-07-17`, so the later official date is used.

### SCJ Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:SCJ` | [iShares SCJ U.S. product page](https://www.ishares.com/us/products/239666/ishares-msci-japan-smallcap-etf) | Canonical exchange, fund identity, benchmark, inception, fees, current NAV/YTD and rolling standardized NAV TR | Page accessed `2026-07-24`; rolling summary `2026-06-30`; current NAV/YTD `2026-07-17` |
| `NYSE Arca:SCJ` | [iShares SCJ international performance view](https://www.ishares.com/uk/professional/en/products/239666/ishares-msci-japan-smallcap-etf?siteEntryPassthrough=true&switchLocale=y) | 2016-2025 NAV/issuer benchmark rows and fresher current observation | Annual rows `2025-12-31`; current NAV/YTD `2026-07-21` |
| `NYSE Arca:SCJ` | [iShares SCJ factsheet](https://www.ishares.com/us/literature/fact-sheet/scj-ishares-msci-japan-small-cap-etf-fund-fact-sheet-en-us.pdf) | Corroborates passive equity objective, benchmark, launch, fee, 2021-2025 NAV rows and reinvestment/expense basis | Factsheet as of `2026-03-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### SCJ Raw Observations And Calculations

| Year | SCJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.60% | 11.96% |
| 2017 | 30.90% | 21.83% |
| 2018 | -16.40% | -4.38% |
| 2019 | 19.00% | 31.49% |
| 2020 | 6.30% | 18.40% |
| 2021 | -2.40% | 28.71% |
| 2022 | -12.70% | -18.11% |
| 2023 | 12.95% | 26.29% |
| 2024 | 3.26% | 25.02% |
| 2025 | 29.66% | 17.88% |

- Official rolling 10-year NAV TR is `+119.60%` with CAGR `8.18%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `219.60`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+92.14%` and annualize to `6.75%` over 10 complete calendar years. Precise common rows `2021-2025` compound to `+28.85%` and annualize to `5.20%`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; SCJ trails by approximately `9.23 pp` CAGR in that common window.
- Official current NAV TR YTD is `+16.10%` as of `2026-07-21`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### SCJ Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## ISSSF Sequential Queue Record

- Input row: `20/125`; input ticker: `ISSSF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:SAUS`; the iShares official product page and factsheet identify the product as `iShares MSCI Australia UCITS ETF`, ticker `SAUS` on the London Stock Exchange, issued by `iShares III plc`, ISIN `IE00B5377D42`. `ISSSF` is retained as the input OTC alias; no provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page already had calendar rows but lacked issuer benchmark, inception and rolling 10-year calculation. Rechecking the official product page, current factsheet and listing table confirms share-class launch `2010-01-22`, passive/replicated physical equity structure, and official 10.00-year NAV TR coverage; this was a page gap, not a history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `121.17%` and annualised `8.26%` for `2016-06-30` to `2026-06-30`. Normalized TR is `100.00` to `221.17`; actual years `10.00`.
- Official annual observations: iShares calendar-year NAV rows 2016-2025 and the issuer benchmark rows were captured from the official performance table. The source states performance is NAV-based with gross income reinvested where applicable.
- Official current observation: iShares reports NAV `US$62.24` and NAV Total Return YTD `10.27%` as of `2026-07-21`; market-price return is kept separate.

### ISSSF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:SAUS` | [iShares SAUS product and performance page](https://www.ishares.com/uk/professional/en/products/251851/ishares-msci-australia-ucits-etf) | Canonical listing, fund identity, passive/physical/replicated classification, benchmark, inception, annual NAV TR, rolling 10Y return, current NAV/YTD and risk facts | Page accessed `2026-07-24`; rolling summary `2026-06-30`; current NAV/YTD `2026-07-21` |
| `LSE:SAUS` | [iShares SAUS factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/saus-ishares-msci-australia-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) | Corroborates passive structure, benchmark, launch date, fee, NAV return basis and calendar rows | Factsheet February 2026; calendar performance through 2025-12-31 |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### ISSSF Raw Observations And Calculations

| Year | ISSSF / SAUS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 11.00% | 11.96% |
| 2017 | 19.60% | 21.83% |
| 2018 | -12.30% | -4.38% |
| 2019 | 22.50% | 31.49% |
| 2020 | 8.40% | 18.40% |
| 2021 | 9.00% | 28.71% |
| 2022 | -5.70% | -18.11% |
| 2023 | 14.30% | 26.29% |
| 2024 | 0.80% | 25.02% |
| 2025 | 14.30% | 17.88% |

- Official rolling 10-year NAV TR is `+121.17%` with CAGR `8.26%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `221.17`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+109.27%` and annualize to `7.66%` over 10 complete calendar years. Common rows `2021-2025` compound to `+35.36%` and annualize to `6.24%`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; ISSSF/SAUS trails by approximately `8.19 pp` CAGR in that common window.
- Official current NAV TR YTD is `+10.27%` as of `2026-07-21`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### ISSSF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Australia region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## VPL Sequential Queue Record

- Input row: `19/125`; input ticker: `VPL`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:VPL`; Vanguard's official factsheet identifies ticker `VPL`, exchange `NYSE Arca`, fund inception `2005-03-04`, and passive full-replication exposure to the FTSE Developed Asia Pacific All Cap Index. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page had current YTD but no annual rows, inception, benchmark, or 10-year calculation. Rechecking Vanguard's product page and June 2026 factsheet confirms a genuine 10.00-year NAV TR window and a 10-year field; the page gap was repaired rather than treated as a history gap.
- Official rolling performance: Vanguard reports 10-year NAV TR cumulative `177.37%` and average annual return `10.74%` for `2016-05-31` to `2026-05-31`. Normalized TR is `100.00` to `277.37`; actual years `10.00`.
- Official annual observations: NAV total returns and benchmark rows for calendar years `2016-2025` were captured from Vanguard's annual performance table as of `2025-12-31`. Official factsheet as of `2026-06-30` separately reports 10-year NAV return `10.68%`, YTD `28.00%`, expense ratio `0.07%`, and 3-year standard deviation `16.27%`.
- Official current observation: Vanguard Advisors' official product page reports NAV YTD `19.62%` as of `2026-07-17`; this later date is kept separate from the month-end rolling/annual observations.

### VPL Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:VPL` | [Vanguard VPL product and performance page](https://investor.vanguard.com/investment-products/etfs/profile/vpl) | Fund identity, exchange, benchmark, passive/index classification, inception, annual NAV TR rows, rolling 10Y cumulative/CAGR, and distribution/expense basis | Page accessed `2026-07-24`; annual table `2025-12-31`; rolling summary `2026-05-31` |
| `NYSE Arca:VPL` | [Vanguard VPL factsheet](https://fund-docs.vanguard.com/F0962.pdf) | Corroborates index, inception, 10-year NAV TR, YTD, expense ratio, holdings/exposure and standard deviation | Factsheet as of `2026-06-30` |
| `NYSE Arca:VPL` | [Vanguard Advisors VPL page](https://advisors.vanguard.com/investments/products/vpl/vanguard-ftse-pacific-etf) | Fresher official current YTD observation | NAV YTD `19.62%` as of `2026-07-17` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### VPL Raw Observations And Calculations

| Year | VPL NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 5.31% | 11.96% |
| 2017 | 28.60% | 21.83% |
| 2018 | -13.85% | -4.38% |
| 2019 | 17.61% | 31.49% |
| 2020 | 16.58% | 18.40% |
| 2021 | 1.51% | 28.71% |
| 2022 | -15.21% | -18.11% |
| 2023 | 15.58% | 26.29% |
| 2024 | 1.27% | 25.02% |
| 2025 | 33.16% | 17.88% |

- Official rolling 10-year NAV TR is `+177.37%` with CAGR `10.74%` for `2016-05-31` to `2026-05-31`; normalized TR is `100.00` to `277.37`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+114.60%` and annualize to `7.94%` over 10 complete calendar years. Common rows `2021-2025` compound to `+34.15%` and annualize to `6.05%`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; VPL trails by approximately `8.38 pp` CAGR in that common window.
- Official current NAV TR YTD is `+19.62%` as of `2026-07-17`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### VPL Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Asia-Pacific region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.
