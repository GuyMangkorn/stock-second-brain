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

## IEMMF / IWMO evidence packet

- Identity: input `IEMMF` is a secondary OTC alias for the official USD London Stock Exchange listing `IWMO` of iShares Edge MSCI World Momentum Factor UCITS ETF U.S. Dollar (Accumulating), ISIN `IE00BP3QZ825`. Official listing date is 6 Oct 2014; share-class/fund launch is 3 Oct 2014.
- Official classification: passive physical optimised equity UCITS ETF tracking `MSCI World Momentum Index (Net)`. The selected share class is accumulating, USD, TER `0.25%`, and does not define its payoff through leverage, inverse exposure, or options.
- Current official product-page snapshot: NAV `US$114.55` as of 28 Aug 2026; NAV Total Return YTD `19.25%` as of 27 Aug 2026; net assets `US$6,022,456,334` as of 28 Aug 2026; holdings `353` as of 28 Aug 2026; 3-year beta `0.999` and standard deviation `17.79%` as of 31 Jul 2026.
- Official June 2026 factsheet observations: 2016–2025 annual NAV/index rows; 6-month/YTD `28.24%`, 1-year `36.71%`, 3-year annualised `29.88%`, 5-year annualised `14.55%`, and since-inception annualised `14.61%`, all as of 30 Jun 2026. The reviewed current capture did not expose a separate issuer rolling 10-year field.
- Official calendar NAV TR / issuer index TR rows, USD, complete years 2016–2025:

| Year | IWMO NAV TR | MSCI World Momentum Index TR |
|---|---:|---:|
| 2016 | 4.05% | 4.19% |
| 2017 | 31.91% | 32.09% |
| 2018 | -2.97% | -2.76% |
| 2019 | 27.44% | 27.68% |
| 2020 | 27.90% | 28.26% |
| 2021 | 14.31% | 14.64% |
| 2022 | -17.87% | -17.79% |
| 2023 | 11.56% | 11.75% |
| 2024 | 29.80% | 30.15% |
| 2025 | 21.23% | 21.33% |

- Cached S&P 500 TR rows for the same 2016–2025 USD total-return basis: 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; cached reference as of 31 Dec 2025.
- Calculation inputs and outputs: IWMO product `3.5775152551`, cumulative `257.75%`, rounded-input 10-year calendar CAGR `13.59%†`; issuer index product `3.6448173138`, cumulative `264.48%`, CAGR `13.81%`; S&P product `3.9832911148`, cumulative `298.33%`, CAGR `14.82%`. IWMO 2021–2025 product `1.6480840290`, cumulative `64.81%`, CAGR `10.51%`; issuer index `1.6631090524`, cumulative `66.31%`, CAGR `10.71%`; S&P `1.9616961801`, cumulative `96.17%`, CAGR `14.43%`.
- Annual NAV standard deviation, population: `15.49%` for 2016–2025 and `16.12%` for 2021–2025. Annual active differences versus issuer index: `-0.14`, `-0.18`, `-0.21`, `-0.24`, `-0.36`, `-0.33`, `-0.08`, `-0.19`, `-0.35`, `-0.10` percentage points; no alpha claim.
- Annual-path risk: maximum year-end drawdown `-17.87%` in 2022; cumulative year-end level exceeded the previous high by 2024; daily drawdown/recovery date is not disclosed in the reviewed official capture.
- Ranking review: `8 / 2` up/down years; best `2017 +31.91%`; least positive `2016 +4.05%`; worst `2022 -17.87%`; least bad down year `2018 -2.97%`.
- Source integrity review: PASS — OTC alias mapping is clearly secondary, official identity/listing and passive equity classification are separated, all return numbers use USD NAV Total Return or clearly labelled issuer-index/S&P comparison bases, and current/annual/as-of dates are visible.
- Calculation and format review: PASS — ten complete official calendar rows support a rounded-input calendar CAGR, issuer rolling 10-year is not invented, required sections/one annual table/Thai-first narrative/canonical `geography/International` tag/breadcrumb are present, and daily risk gaps are stated.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, and `log.md` were already dirty before this claim due to retained FNDF recovery state. They were not modified or included in this card’s scoped output; the IWMO row and workflow log bullet remain deferred to clean navigation reconciliation.
- Planned durable contents: create `wiki/analysis/performance/ETF_LSE_IWMO Performance.md` with the full IEMMF/IWMO performance page and update this source batch with the evidence, calculations, local review, and deferred shared-navigation note.
- Planned durable paths/change map: `wiki/analysis/performance/ETF_LSE_IWMO Performance.md` (create); `raw/imports/ETF_performance_sources_2026-09-01_run-3.md` (update). No other path is written by the downstream workflow for this card.
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

## DBEF / DBEF evidence packet

- Identity: `DBEF` is the NYSE Arca ticker for Xtrackers MSCI EAFE Hedged Equity ETF; issuer factsheet identifies the underlying index as `MSCI EAFE US Dollar Hedged Index` and the fund inception date as 8 Jun 2011.
- Official classification: passive/index-tracking developed ex-US equity ETF. The fund normally invests at least 80% in equity issuers in Europe, Australia and the Far East and uses non-deliverable/forward foreign-currency contracts to hedge non-US currencies. The hedge is implementation risk, not a leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff structure.
- Official Q2 factsheet snapshot as of 30 Jun 2026: NAV returns 3M `12.08%`, 1Y `27.58%`, 3Y annualized `18.49%`, 5Y annualized `13.76%`, 10Y annualized `12.66%`, since inception annualized `10.42%`; issuer benchmark respectively `12.08%`, `27.86%`, `18.74%`, `13.95%`, `12.90%`, `10.73%`; broad MSCI EAFE reference respectively `10.82%`, `20.23%`, `16.44%`, `9.05%`, `9.66%`, `6.99%`.
- Official Q2 fund facts as of 30 Jun 2026: `690` holdings, net assets `US$9,039,408,798.94`, gross/net expense ratio `0.35%`, SEC 30-day yield `2.05%`, beta `0.72`, ticker `DBEF`, NAV ticker `DBEF.NV`, CUSIP `233051200`.
- Current YTD evidence: issuer current YTD field was not exposed in the reviewed Q2/current product captures. AAII secondary profile reports NAV YTD `+14.1%` as of 31 Jul 2026; it is marked secondary and is not merged with the official 30 Jun rolling fields. AAII also reports standard deviation `9.6%`; this remains a secondary cross-check.
- Secondary annual NAV total-return observations as of 31 Jul 2026: 2016 `5.7%`, 2017 `16.6%`, 2018 `-9.3%`, 2019 `24.4%`, 2020 `2.3%`, 2021 `19.3%`, 2022 `-4.7%`, 2023 `19.7%`, 2024 `14.0%`, 2025 `22.9%`. The issuer Q2 factsheet exposes rolling annualized fields but not a numeric 2016–2025 calendar table; therefore all annual DBEF rows remain marked `*` as secondary and the issuer benchmark annual column is `not disclosed`.
- Cached S&P 500 TR rows for the same 2016–2025 USD total-return basis: 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; cached reference as of 31 Dec 2025.
- Calculations from the stated secondary annual rows: 2016–2025 product `2.7124457932`, cumulative `171.24%`, rounded-input CAGR `10.49%`, population standard deviation `11.26%`; 2021–2025 product `1.9067081765`, cumulative `90.67%`, rounded-input CAGR `13.78%`, population standard deviation `9.89%`; S&P 500 2016–2025 cumulative `298.33%` / CAGR `14.82%` and 2021–2025 cumulative `96.17%` / CAGR `14.43%`.
- Annual-path risk calculation: maximum year-end drawdown `-9.30%` in 2018; cumulative year-end level exceeded the previous high in 2019. Up/down count `8 / 2`; best `2019 +24.40%`; least positive `2020 +2.30%`; worst `2018 -9.30%`; least bad down year `2022 -4.70%`. Daily NAV drawdown and exact recovery timing were not verified.
- Source map: official factsheet `https://etf.dws.com/download/asset/0eb88b89-c04c-4170-b412-80462e8598e1`; SEC summary prospectus `https://www.sec.gov/Archives/edgar/data/1503123/000008805325000874/k100125dbef.htm`; DWS currency-hedged page `https://etf.dws.com/en-us/etf-knowledge/focus-topics-etf-investment-strategies/currency-hedged-etfs-mitigating-currency-risks-from-international-equities/`; secondary AAII profile `https://www.aaii.com/etf/ticker/DBEF`; S&P 500 source URLs are the cached references listed above.
- Source integrity review: PASS — official identity, exchange, strategy, hedge role, USD NAV return basis, rolling fields and fund facts are separated from secondary calendar/YTD/risk fields; missing issuer annual rows and current official YTD are explicitly disclosed; no market-price return is mixed with NAV return.
- Calculation review: PASS — cumulative return, rounded-input CAGRs, standard deviations, year counts, best/worst rows and annual-path drawdown were recomputed from the stated inputs; official rolling 10Y `12.66%` is kept separate from the secondary calendar proxy CAGR `10.49%` because windows and source methods differ.
- Format and graph review: PASS for the planned card-specific files — Thai-first narrative, one annual table, required risk/source sections, canonical `geography/International` tag and breadcrumb resolve to existing pages.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, and `log.md` were already dirty before this claim due to retained FNDF recovery state. They were not modified or included in this card's scoped output; the DBEF row and workflow log bullet remain deferred to clean navigation reconciliation.
- Planned durable contents: create `wiki/analysis/performance/ETF_NYSE_ARCA_DBEF Performance.md` with the complete DBEF performance page described above and update this source batch with the evidence, calculations, local review and deferred shared-navigation note.
- Planned durable paths/change map: `wiki/analysis/performance/ETF_NYSE_ARCA_DBEF Performance.md` (create); `raw/imports/ETF_performance_sources_2026-09-01_run-3.md` (update). No other path is written by the downstream workflow for this card.
- Local pre-save verdict: `PASS`; no critical, high or unresolved material finding remains within the renewed clean output scope.

## DBEF research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official identity, strategy, rolling NAV fields, secondary annual/YTD fields, calculations and source dates passed the scheduled-local pre-save review with all source-quality gaps disclosed.
```

## HEFA evidence packet

- Identity: `HEFA` is currently listed by iShares on `Cboe BZX`; canonical entity key is `Cboe BZX:HEFA`. Fund launch date is 31 Jan 2014 and the official benchmark is `MSCI EAFE 100% Hedged to USD Index (Net)`.
- Official classification: passive/index-tracking international equity ETF. HEFA uses the iShares MSCI EAFE ETF as the underlying exposure and currency forwards to hedge FX; the structure is not leverage, inverse, option-income, bond, commodity, currency or derivative-defined payoff.
- Current official product snapshot: NAV `US$47.39` and NAV Total Return YTD `16.33%` as of 28 Aug 2026; closing price `US$47.28` and net assets `US$7,525,863,862` as of 28 Aug 2026. The NAV metric is used; closing price is retained only as a separate fact.
- Official fund facts as of 31 Jul 2026: gross expense ratio `0.70%`, fee waiver `0.35%`, net expense ratio `0.35%`, 30-day SEC yield `3.23%`, 12-month trailing yield `3.09%`, 3-year standard deviation `8.64%`, and 3-year beta `0.46`. The product page/factsheet reports one direct holding because the fund holds the underlying iShares MSCI EAFE ETF and currency-forward positions.
- Official rolling performance as of 30 Jun 2026: NAV 1Y `28.14%`, 3Y annualized `18.56%`, 5Y annualized `13.92%`, 10Y annualized `12.71%`, since inception annualized `10.81%`; cumulative NAV YTD `13.52%`, 1M `3.12%`, 3M `10.33%`, 6M `13.52%`, 1Y `28.14%`, 3Y `66.65%`, 5Y `91.85%`, 10Y `230.88%`, inception `257.49%`. Corresponding issuer benchmark fields are `27.86%`, `18.72%`, `13.95%`, `12.89%`, `10.85%` annualized and `13.03%`, `2.46%`, `12.08%`, `13.03%`, `27.86%`, `67.41%`, `92.15%`, `236.39%`, `259.50%` cumulative.
- Official calendar NAV rows for complete years 2016–2025: 2016 `6.57%`, 2017 `16.69%`, 2018 `-9.24%`, 2019 `24.73%`, 2020 `2.11%`, 2021 `19.38%`, 2022 `-4.73%`, 2023 `20.44%`, 2024 `13.71%`, 2025 `23.25%`. The 2016–2020 rows are from the official HEFA summary prospectus calendar bar chart; 2021–2025 rows are also exposed in the current official product page/factsheet.
- Official issuer benchmark rows exposed for 2021–2025: `19.43%`, `-4.60%`, `19.95%`, `14.14%`, `23.10%`. Earlier annual benchmark rows were not exposed in the reviewed capture and remain `not disclosed` in the performance table.
- Cached S&P 500 TR rows for the same 2016–2025 USD total-return basis: 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; cached reference as of 31 Dec 2025.
- Calculations from official HEFA annual rows: 2016–2025 product `2.7596014563`, cumulative `175.96%`, rounded-input CAGR `10.68%`, population standard deviation `11.37%`; 2021–2025 product `1.9197473382`, cumulative `91.97%`, rounded-input CAGR `13.93%`, population standard deviation `10.06%`. Issuer benchmark 2021–2025 product `1.9202509138`, cumulative `92.03%`, rounded-input CAGR `13.94%`.
- Annual-path risk calculation: maximum year-end drawdown `-9.24%` in 2018; cumulative year-end level exceeded the previous high in 2019. Up/down count `8 / 2`; best `2019 +24.73%`; least positive `2020 +2.11%`; worst `2018 -9.24%`; least bad down year `2022 -4.73%`. Daily NAV drawdown and exact recovery timing were not verified.
- Source map: official product page `https://www.ishares.com/us/products/259622/HEFA`; factsheet `https://www.ishares.com/us/literature/fact-sheet/hefa-ishares-currency-hedged-msci-eafe-etf-fund-fact-sheet-en-us.pdf`; summary prospectus `https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-currency-hedged-msci-eafe-etf-7-31.pdf`; S&P 500 source URLs are the cached references listed above.
- Source integrity review: PASS — official exchange-qualified identity, benchmark, NAV return basis, annual rows, rolling fields, current YTD/NAV, fees and risk fields reconcile; market price is kept separate; the underlying-fund/forward structure and fee waiver are disclosed.
- Calculation review: PASS — cumulative return, rounded-input CAGRs, standard deviations, year counts, best/worst rows, annual-path drawdown and recovery statement were recomputed from the stated inputs; official rolling 10Y is kept separate from the calendar CAGR because the windows differ.
- Format and graph review: PASS for the planned card-specific files — Thai-first narrative, one annual table, required risk/source sections, canonical `geography/International` tag and breadcrumb resolve to existing pages.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, and `log.md` were already dirty before this claim due to retained FNDF recovery state. They were not modified or included in this card's scoped output; the HEFA row and workflow log bullet remain deferred to clean navigation reconciliation.
- Planned durable contents: create `wiki/analysis/performance/ETF_CBOE_BZX_HEFA Performance.md` with the complete HEFA performance page described above and update this source batch with the evidence, calculations, local review and deferred shared-navigation note.
- Planned durable paths/change map: `wiki/analysis/performance/ETF_CBOE_BZX_HEFA Performance.md` (create); `raw/imports/ETF_performance_sources_2026-09-01_run-3.md` (update). No other path is written by the downstream workflow for this card.
- Local pre-save verdict: `PASS`; no critical, high or unresolved material finding remains within the renewed clean output scope.

## HEFA research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official exchange identity, NAV annual/rolling/current fields, hedge structure, calculations and source dates passed the scheduled-local pre-save review.
```

## DFIS correction notice

The appended DFIS draft in this mixed `IEMXF`/`LSE:MVOL` batch was not canonical:
it used `Cboe:DFIS`, an outdated SEC source, and a stale YTD proxy. It is
superseded by the scoped recheck [[ETF_performance_sources_2026-09-02_recheck]]
and the canonical page [[ETF_CBOE_BZX_DFIS Performance]]. Use the recheck for
all current DFIS evidence; no performance decision should be based on the
superseded draft.
