---
type: etf-performance-source-batch
workflow: check-etf-performance
run_date: 2026-09-01
run_label: run-3
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
input_ticker: IEMXF
entity_key: LSE:MVOL
primary_region: International
performance_output: wiki/analysis/performance/ETF_LSE_MVOL Performance.md
---

# ETF Performance Sources — 2026-09-01 — run-3

## Scope and handoff

- Workflow: `check-etf-performance`; caller: `research-queue-manager`; handoff: `research_handoff`; mode: `lean`.
- Input: `IEMXF`; canonical identity: `LSE:MVOL`; primary region by underlying exposure: `International`.
- The input is an OTC alias. The official iShares USD listing is London Stock Exchange `MVOL`, share-class ISIN `IE00B8FHGS14`; the official product page lists other exchange lines for the same share class.
- Management mode: `passive-index`; supported asset class: physical developed-market equity ETF; no payoff-defining leverage, inverse, options, or non-equity structure identified.
- Return basis: USD NAV Total Return, with gross income reinvested where applicable and fund expenses reflected. The share class is accumulating, so no cash distribution series is used.
- Official issuer benchmark: `MSCI World Minimum Volatility (USD)`. Common comparison benchmark: cached `S&P 500 Total Return` in USD with dividends reinvested for the identical complete calendar window 2016–2025.

## Source map

| Source | Type | As-of / role |
|---|---|---|
| https://www.ishares.com/uk/individual/en/products/251382/ishares-msci-world-minimum-volatility-ucits-etf?shortLocale=en_GB&siteEntryPassthrough=true&switchLocale=y | Official issuer product page | Current NAV/YTD and fund facts through 28 Aug 2026; annual table and benchmark; rolling fields through 30 Jun 2026 |
| https://www.ishares.com/uk/professional/en/literature/fact-sheet/mvol-ishares-edge-msci-world-minimum-volatility-ucits-etf-fund-fact-sheet-en-gb.pdf | Official issuer factsheet | Performance, annual rows and rolling fields as of 30 Jun 2026; other facts as of 6 Jul 2026 |
| https://stockanalysis.com/quote/otc/IEMXF/ | Secondary OTC profile | Alias/name cross-check only; not used for NAV return calculations |
| https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official index page | S&P 500 definition; common-reference benchmark |
| https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Official S&P DJI research | Cached 2016–2019 S&P 500 TR rows; reference as of 31 Dec 2025 |
| https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Official S&P DJI commentary | Cached 2018–2022 S&P 500 TR rows; reference as of 31 Dec 2025 |
| https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Official S&P DJI commentary | Cached 2021 S&P 500 TR row; reference as of 31 Dec 2025 |
| https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Official S&P DJI commentary | Cached 2022–2025 S&P 500 TR rows; reference as of 31 Dec 2025 |

## Raw observations and definitions

- Identity: iShares Edge MSCI World Minimum Volatility UCITS ETF U.S. Dollar (Accumulating); iShares VI plc; Ireland UCITS; physical optimised replication; fund/share-class launch 30 Nov 2012; TER `0.30%`; share-class currency and base currency USD; benchmark `MSCI WORLD MINIMUM VOLATILITY (USD)`.
- Official listing: London Stock Exchange `MVOL`, USD, listing date 3 Dec 2012, Bloomberg `MVOL LN`, RIC `MVOL.L`. The same share class is also listed on Cboe Europe, Borsa Italiana, Xetra, SIX and other venues; the USD LSE line is used as canonical to match the return currency.
- Current official product-page snapshot: NAV `US$78.51` and NAV Total Return YTD `7.25%`, both as of 28 Aug 2026; holdings `286` and P/B `3.28` as of 25 Aug 2026; 3-year beta `1.005` and standard deviation `9.43%` as of 31 Jul 2026; net assets of share class `US$2,646,011,639` as of 26 Aug 2026.
- Official rolling performance page: 10-year annualised NAV TR `6.88%` and issuer benchmark `6.88%`; 10-year cumulative NAV TR `94.59%` and benchmark `94.55%`, with rolling window 30 Jun 2016–30 Jun 2026. These values are USD NAV-based with gross income reinvested where applicable.
- Official 30 Jun 2026 trailing annualised fields also show 1-year NAV TR `6.74%`, 3-year `9.43%`, 5-year `5.21%`, and since-inception `8.47%`; these are not substituted for the requested complete-calendar comparison.
- Official calendar NAV TR / issuer index TR rows, USD, complete years 2016–2025:

| Year | MVOL NAV TR | MSCI World Minimum Volatility Index TR |
|---|---:|---:|
| 2016 | 7.40% | 7.47% |
| 2017 | 17.36% | 17.32% |
| 2018 | -2.15% | -2.03% |
| 2019 | 23.16% | 23.17% |
| 2020 | 2.62% | 2.61% |
| 2021 | 14.15% | 14.26% |
| 2022 | -9.86% | -9.79% |
| 2023 | 7.79% | 7.42% |
| 2024 | 10.80% | 10.87% |
| 2025 | 10.52% | 10.54% |

- Cached S&P 500 TR rows for the same 2016–2025 USD total-return basis: 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; cached reference as of 31 Dec 2025.
- Secondary source use is limited to resolving the OTC alias/name. It does not supply any annual NAV TR, current NAV, YTD, benchmark, or risk number.

## Calculations and reconciliation

- Formula for cumulative return: `Π(1 + annual return) - 1`.
- Formula for calendar CAGR: `(1 + cumulative return)^(1 / number of complete years) - 1`.
- MVOL 2016–2025: product `2.1170907804`; cumulative `111.71%`; rounded-input CAGR `7.79%†`.
- Issuer benchmark 2016–2025: product `2.1184323443`; cumulative `111.84%`; rounded-input CAGR `7.80%`.
- S&P 500 TR 2016–2025: product `3.9832911148`; cumulative `298.33%`; rounded-input CAGR `14.82%`.
- MVOL 2021–2025: product `1.3581651365`; cumulative `35.82%`; rounded-input CAGR `6.31%`.
- Issuer benchmark 2021–2025: product `1.3569616013`; cumulative `35.70%`; rounded-input CAGR `6.30%`.
- S&P 500 TR 2021–2025: product `1.9616961801`; cumulative `96.17%`; rounded-input CAGR `14.43%`.
- MVOL annual return standard deviation, population, 2016–2025: `9.06%`; 2021–2025: `8.51%`. These are calculations from compatible annual NAV TR observations and are not issuer-disclosed volatility fields.
- MVOL annual active differences versus issuer index in percentage points, 2016–2025: `-0.07`, `+0.04`, `-0.12`, `-0.01`, `+0.01`, `-0.11`, `-0.07`, `+0.37`, `-0.07`, `-0.02`; no alpha claim is made.
- 10-year rolling field: issuer-reported `94.59%` cumulative and `6.88%` annualised for 30 Jun 2016–30 Jun 2026. A normalized illustration uses start TR `100.00` and end TR `194.59`; exact raw index/NAV endpoints were not exposed in the reviewed page capture.
- Year-end drawdown calculation from a normalized cumulative NAV path: 2018 `-2.15%`, 2022 `-9.86%`, 2023 `-2.84%`; maximum year-end drawdown `-9.86%` in 2022. The cumulative year-end level exceeded the prior 2021 high by 2024; exact daily recovery date is not disclosed.
- Up/down count on complete calendar rows: `8 / 2`; best `2019 +23.16%`; least positive `2020 +2.62%`; worst `2022 -9.86%`; least bad down year `2018 -2.15%`.

## Evidence packet and local pre-save review

- Active eligibility review: not applicable; official issuer classifies the product as a passive physical equity ETF tracking a minimum-volatility equity index. Currency-hedged share classes use derivatives, but the selected USD accumulating share class is not currency hedged and the product is not leverage, inverse, option-income, bond, commodity, currency, or multi-asset.
- Source and data integrity: PASS — canonical exchange-qualified identity, fund/share-class identity, return basis, currency, issuer benchmark, official annual rows, rolling field, current YTD/NAV and separate as-of dates reconcile.
- Calculation and ranking review: PASS — cumulative returns, calendar CAGRs, annual standard deviation, year counts, best/worst rows, year-end drawdown and recovery statement recomputed from the stated inputs; the issuer rolling 10-year field is kept separate from the rounded calendar CAGR.
- Format and graph review: PASS for the planned card-specific files — Thai-first narrative, required sections, one annual table, source links, canonical `geography/International` tag, and breadcrumb `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]` resolve to existing pages.
- Shared navigation note: the pre-existing `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, and `log.md` paths were already dirty before this claim due to the retained FNDF recovery state. They were not modified or included in this card’s scoped output, so the new MVOL row and workflow log bullet are deferred to a clean navigation reconciliation.
- Planned durable contents: create `wiki/analysis/performance/ETF_LSE_MVOL Performance.md` with the complete performance page described above and create this source batch with the complete evidence, calculations, local review record, and deferred shared-navigation note.
- Planned durable paths/change map: `wiki/analysis/performance/ETF_LSE_MVOL Performance.md` (create); `raw/imports/ETF_performance_sources_2026-09-01_run-3.md` (create). No other path is written by the downstream workflow for this card.
- Local pre-save verdict: `PASS`; no critical, high, or unresolved material finding remains within the renewed clean output scope.

## Research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official identity, NAV total-return history, rolling field, current YTD, calculations and source dates passed the scheduled-local pre-save review.
```
