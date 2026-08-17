---
type: source-batch
topic: ETF performance
accessed: 2026-08-17
input_source: Trello ETF child cards GSSC, XSMO, SSEUF, FNDA, ZPRVF, NUSC, IMWSF, DES, FNDC, RWJ, ISHOF, DISV, CPLCF, BSVO, FYX, IWMI, VB, SCHA, SPSM, VBR, VTWO, VSS, IJR, IWM, IWN, IWO, AVUV, DFAS, AVDV, SCZ, BBSC, ISCF, GWX, ISCV, EES, JPSE, XSVM, JHSC, SFLO, OSCV, SMDV, SMIN, EWX, AVSC, FESM, DFSV, PSC
input_count: 47
workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## IWMI unsupported ETF type

| Scope | Source | Role | Evidence |
|---|---|---|---|
| IWMI | https://www.sec.gov/Archives/edgar/data/1848758/000199937126009956/iwmi-497k_050126.htm | Official SEC summary prospectus for NEOS Russell 2000® High Income ETF | Dated 2026-05-01; principal strategy identifies the fund as actively managed, uses Russell 2000 exposure plus written/sold RUT call options, and states the fund is not an index fund |
| IWMI | https://www.cboe.com/us/equities/notices/new_listings/details/?etf=true&firm_name=NEOS+Investment+Management+LLC&first_trade_dt=2024-06-25&ipo=true&symbols=IWMI | Official exchange listing confirmation | Cboe BZX listing for NEOS Russell 2000 High Income ETF, first trading date 2024-06-25 |

## IWMI scheduled-inline local review

- Status: `PASS` for the type gate; `BLOCKED` for ETF v1 performance processing.
- Confirmed the canonical fund identity as NEOS Russell 2000® High Income ETF (IWMI), Cboe BZX listing, active management, and options overlay from the official SEC prospectus.
- Classification: unsupported ETF type because the fund is actively managed and derivative-heavy rather than a passive index-tracking equity ETF.
- No performance page, region row, performance-index row, or ETF performance calculations were written.
- Local pre-save result: `PASS` for the blocking decision.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## AGSCF / AVGS official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:AVGS (input alias AGSCF) | https://www.avantisinvestors.com/ucitsetf/avantis-global-small-cap-value-ucits-etf/ | Official Avantis product page: fund identity, active objective, current NAV and regulatory-document links | Page reviewed 2026-08-17; product-page NAV US$29.85 as of 2026-08-14 |
| LSE:AVGS (input alias AGSCF) | https://res.avantisinvestors.com/docs/avantis-global-small-cap-value-ucits-etf-fact-sheet.pdf | Official Avantis factsheet: active approach, inception, benchmark, OCF, NAV performance, holdings, country exposures and risk language | Marketing communication as of 2026-07-31; inception 2024-09-25; OCF 0.39%; NAV YTD 21.43%; benchmark YTD 13.80%; NAV 1-year 36.36%; benchmark 1-year 27.16% |
| LSE:AVGS (input alias AGSCF) | https://www.londonstockexchange.com/stock/AVGS/american-century-icav/company-page | Official exchange identity cross-check | USD ticker AVGS on London Stock Exchange; listing date 2024-12-04; ISIN IE0003R87OG3 |
| LSE:AVGS (input alias AGSCF) | https://registers.centralbank.ie/%28S%28atb1s1eysq1bdt45cyzep0nm%29%29/FundRegisterDataPage.aspx?fundReferenceNumber=C544701&register=28 | Official regulator fund-register cross-check | Avantis Global Small Cap Value UCITS ETF; UCITS ICAV sub-fund; approval 2024-08-16; page updated 2026-07-27 |

## AGSCF / AVGS raw observations and calculations

| Window | AVGS NAV TR | MSCI World Small Cap Value Index | Active difference |
|---|---:|---:|---:|
| 2026 YTD | 21.43% | 13.80% | +7.63 pp |
| Rolling 1-year | 36.36% | 27.16% | +9.20 pp |

- Metric basis: official factsheet NAV total returns; returns assume reinvestment of dividends and capital gains; currency USD; the fund is accumulating.
- Active difference calculations: `21.43% - 13.80% = +7.63 pp`; `36.36% - 27.16% = +9.20 pp`.
- No annual calendar rows, complete 2021-2025 window, 10-year window, ITD annualized return or compatible annual hit-rate series was disclosed in the reviewed official sources; no CAGR or hit rate is calculated.
- Current official product-page NAV snapshot: US$29.85 as of 2026-08-14. It is retained separately from the 2026-07-31 performance factsheet.

## AGSCF / AVGS gaps and scheduled-inline local review

- Canonical identity resolves input alias AGSCF to official USD listing `LSE:AVGS`, Avantis Global Small Cap Value UCITS ETF, on the London Stock Exchange; ISIN IE0003R87OG3 cross-checks the share class.
- AVGS is within supported ETF scope as an active, long-only equity UCITS ETF. The official materials state that it does not seek to replicate a specified index; the portfolio approach uses valuation and profitability tilts with broad developed-market small-cap equity exposure.
- Management benchmark is MSCI World Small Cap Value Index, the official strategy-aligned small-cap value comparator. S&P 500 TR remains common reference context only.
- Track record is developing-short-live-history because inception is 2024-09-25 and the reviewed performance factsheet has less than two years of live-history context.
- Only official 2026 YTD and rolling 1-year rows are saved. Calendar-year rows, CAGR, hit rate and a synchronized S&P 500 YTD comparison remain not disclosed.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; no numeric drawdown or recovery claim is saved.
- Planned durable paths: created `wiki/analysis/performance/ETF_LSE_AVGS Performance.md`; updated `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region International; breadcrumb `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`; canonical tags `geography/International`, `ticker/AVGS`, and `ticker/AGSCF`; all affected wikilinks resolve after the performance page is created.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## DFIS official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| Cboe BZX:DFIS | https://www.sec.gov/Archives/edgar/data/1816125/000181612526000070/c497k.htm | Official SEC summary prospectus: identity, exchange, active classification, strategy, fees, annual NAV rows, benchmark, quarterly extremes, turnover and manager continuity | Prospectus dated 2026-02-28; annual performance rows through 2025-12-31; expense ratio 0.39%; inception 2022-03-23 |
| Cboe BZX:DFIS | https://www.dimensional.com/us-en/funds/dfis/international-small-cap-etf | Official Dimensional product-page identity and strategy discovery | Page reviewed 2026-08-17; dynamic page retained as official discovery source |
| Cboe BZX:DFIS | https://my.dimensional.com/chmedia/282748/source/dimensional-etf-quick-guide.pdf | Official Dimensional ETF Quick Guide: inception, expense ratio, annualized performance and management benchmark cross-check | Fund facts as of 2025-12-31; DFIS 1-year NAV TR 37.49%, since-inception annualized 9.94%; benchmark 34.07% and 7.89% |
| Cboe BZX:DFIS | https://www.cboe.com/us/equities/listings/listed_products/symbols/DFIS/ | Official exchange listing cross-check | Listing page reviewed 2026-08-17 |
| Cboe BZX:DFIS | https://www.schwab.wallst.com/Prospect/Research/etfs/summary.asp?symbol=dfis | Secondary current price, NAV, premium/discount, distribution, assets, holdings and current rolling-performance cross-check | Price US$37.34 at 11:12am ET on 2026-08-13; previous close US$37.27; closing NAV US$37.18 on 2026-08-12; premium/discount +0.24% on 2026-08-12; cash distribution US$0.4222, ex-date 2026-06-23, pay date 2026-06-25; 3,461 holdings and 9% turnover |
| Cboe BZX:DFIS | https://chartexchange.com/symbol/bats-dfis/historical/ | Secondary historical closing-price cross-check used only for the current YTD proxy start price | 2025-12-31 close US$32.94; 2026-01-02 close US$33.18 |
| S&P 500 Total Return | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common-reference benchmark definition and cached annual convention | USD total return with dividends reinvested; annual rows 2023 26.29%, 2024 25.02%, 2025 17.88%, as of 2025-12-31 |

## DFIS raw observations and calculations

| Year / window | DFIS NAV TR | MSCI World ex USA Small Cap Index (net dividends) | S&P 500 TR | Annual active difference |
|---|---:|---:|---:|---:|
| 2023 | 15.04% | 12.62% | 26.29% | +2.42 pp |
| 2024 | 3.79% | 2.76% | 25.02% | +1.03 pp |
| 2025 | 37.49% | 34.07% | 17.88% | +3.42 pp |
| 2023-2025 cumulative | 64.16% | 55.16% | 86.12% | — |
| 2023-2025 CAGR | 17.97% | 15.77% | 23.01% | +2.20 pp Excess CAGR |

- Metric basis: official SEC NAV Total Return includes reinvested distributions and fund expenses; market-price return remains separate. Currency is USD.
- Cumulative calculation from displayed annual rows: `(1+15.04%) × (1+3.79%) × (1+37.49%) - 1 = 64.16%`; management benchmark `55.16%`; S&P 500 TR `86.12%`.
- Rounded-input CAGR calculation over three complete years: `64.16%` compound gives `17.97%`; management benchmark gives `15.77%`; S&P 500 TR gives `23.01%`.
- Relative wealth calculation: `1.64163082 / 1.55156948 - 1 = +5.80%`; annual hit rate `3 / 3 = 100%`.
- Annual population standard deviation of DFIS rows is `14.01%`; this is a three-observation short-window descriptor, not a long-run risk estimate.
- Current YTD proxy: `(2026-08-12 previous close 37.27 + 2026-06-25 cash distribution 0.4222) / 2025-12-31 close 32.94 - 1 = 14.18%`. It is explicitly a secondary market-price + cash-distribution proxy, not official NAV TR, and is not paired with a synchronized benchmark YTD.
- Current secondary fields retained separately: price US$37.34 at 11:12am ET on 2026-08-13, previous close US$37.27, closing NAV US$37.18 on 2026-08-12, premium/discount +0.24%, TTM distribution yield 1.99%.

## DFIS gaps and scheduled-inline local review

- Canonical identity is Cboe BZX:DFIS; the SEC summary prospectus, Dimensional product materials and Cboe listing confirm Dimensional International Small Cap ETF and the Cboe BZX venue.
- DFIS is within supported ETF scope as an active, long-only equity ETF. The official prospectus states that it is actively managed and does not seek to replicate a specific index; derivatives are described for exposure, cash management or settlement rather than a payoff-defining leveraged, inverse or option-income structure.
- The selected management benchmark is MSCI World ex USA Small Cap Index (net dividends), the official similar-universe additional index. S&P 500 TR is retained only as common reference context.
- Track record is provisional: inception 2022-03-23 and three complete comparable years through 2025-12-31; no 10-year or 2021-2025 strict window is claimed.
- Current YTD is not official NAV TR. The saved `14.18%*` is a clearly labelled secondary market-price + cash-distribution proxy using independently dated observations.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; no numeric drawdown or recovery claim is saved.
- Planned durable paths: created `wiki/analysis/performance/ETF_CBOE_BZX_DFIS Performance.md`; updated `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region International; breadcrumb `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`; canonical tag `geography/International`; all affected wikilinks resolve after the performance page is created.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## EWX official and secondary source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:EWX` | https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-emerging-markets-small-cap-etf-ewx | Official State Street product/performance page: identity, exchange, issuer benchmark, passive strategy, fee, NAV, market price, holdings, country weights and rolling performance | Product/listing/fund information reviewed 2026-08-17; NAV, market price and holdings as of 2026-08-14; distribution yield as of 2026-08-13; official performance through 2026-07-31 |
| `NYSE Arca:EWX` | https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-ewx.pdf | Official factsheet: standardized NAV, market-price and index returns, inception, fee, benchmark and risk fields | Factsheet as of 2026-06-30; NAV YTD 13.79%, 1-year 22.44%, 5-year annualized 6.83%, 10-year annualized 9.48% |
| `NYSE Arca:EWX` | https://www.sec.gov/Archives/edgar/data/1168164/000119312526031211/d87745d497k.htm | Official SEC summary prospectus: passive objective, index construction, fees, sampling, risks and annual-return extremes | Prospectus dated 2026-01-31; gross expense ratio 0.65%; best quarter +25.82% in Q2 2020; worst quarter -28.68% in Q1 2020 |
| `NYSE Arca:EWX` | https://www.etfreplay.com/etf/ewx | Secondary dividend-adjusted total-return observations for calendar-year proxy | Page reviewed 2026-08-17; annual table data as of 2026-07-08; not issuer-published NAV rows |
| `NYSE Arca:EWX` | https://www.financecharts.com/etfs/EWX/performance | Secondary cross-check for the calendar-year proxy | Page reviewed 2026-08-17; annual observations differ from ETFreplay by 0.01–0.03 percentage points and were not mixed |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | Cached USD total-return convention with dividends reinvested; annual window 2016-2025 as of 2025-12-31 |

## EWX raw observations and calculations

| Year / window | EWX secondary total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.94% | 11.96% |
| 2017 | 34.10% | 21.83% |
| 2018 | -18.74% | -4.38% |
| 2019 | 15.59% | 31.49% |
| 2020 | 14.86% | 18.40% |
| 2021 | 18.16% | 28.71% |
| 2022 | -15.00% | -18.11% |
| 2023 | 18.15% | 26.29% |
| 2024 | 6.84% | 25.02% |
| 2025 | 15.44% | 17.88% |
| 2016-2025 cumulative | 128.55% | 298.33% |
| 2016-2025 rounded-input CAGR | 8.62% | 14.82% |
| 2021-2025 cumulative | 46.36% | 96.17% |
| 2021-2025 rounded-input CAGR | 7.92% | 14.43% |

`*` EWX annual rows are ETFreplay dividend-adjusted total-return observations,
not issuer-published NAV rows. S&P 500 rows reuse the cached USD Total Return
convention as of 2025-12-31.

- Metric basis: official State Street NAV Total Return includes reinvested distributions and fund expenses; USD; market-price return remains separate.
- Identity and classification: State Street identifies EWX as the SPDR S&P Emerging Markets Small Cap ETF, listed on NYSE Arca, tracking the `S&P Emerging Under USD2 Billion Index`; the prospectus describes passive sampling and an at-least-80% index policy.
- Official rolling fields: issuer-reported 10-year NAV TR average annual `7.95%` and current NAV TR YTD `3.91%`, both as of 2026-07-31; raw rolling endpoints and exact elapsed years are not disclosed.
- Formula: cumulative return is `product(1 + annual return) - 1`; CAGR is `cumulative^(1/n) - 1`; displayed annual inputs are rounded, so the CAGR is labelled rounded-input.
- Proxy calculations: 2016-2025 cumulative `128.55%`, rounded-input CAGR `8.62%`; 2021-2025 cumulative `46.36%`, rounded-input CAGR `7.92%`; annual-return population standard deviation `15.04%`; up/down years `8 / 2`; best 2017 `+34.10%`; worst 2018 `-18.74%`.
- Current issuer fields: NAV `$72.25` and market price `$71.89` as of 2026-08-14; AUM `$700.81M` and 3,381 holdings as of 2026-08-14; fund distribution yield `2.55%` as of 2026-08-13; gross expense ratio `0.65%`.
- The cached S&P 500 convention remains a common reference benchmark, not the issuer tracking benchmark. Current-year S&P 500 data was not paired with EWX because the captured current observations are not synchronized.
- FinanceCharts differences were retained as a source conflict note; ETFreplay is the only secondary source used for the calendar proxy. No strict common-window NAV ranking row was added from these proxy observations.

## EWX gaps and scheduled-inline local review

- Canonical identity is `NYSE Arca:EWX`; the State Street product page and SEC prospectus confirm the exchange, fund name, passive strategy and `S&P Emerging Under USD2 Billion Index` benchmark.
- EWX is within supported ETF scope as a passive, index-tracking, long-only equity ETF. No leverage, inverse, bond, commodity, covered-call, option-income or derivative-heavy structure was found; incidental futures use is described only for index tracking and cash management.
- Official State Street performance capture provides rolling NAV fields but not a complete 2016-2025 calendar NAV table. The annual proxy is explicitly secondary and is not added to the strict common-window NAV comparison.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; no numeric NAV drawdown or recovery proxy is saved.
- Planned durable paths: created `wiki/analysis/performance/ETF_NYSE_ARCA_EWX Performance.md`; updated `wiki/analysis/comparisons/Emerging Markets ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region Emerging Markets; breadcrumb `[[ETF Region Index]] → [[Emerging Markets ETF]] → [[ETF Performance Index]]`; canonical tag `geography/Emerging-Markets`; all affected wikilinks resolve to existing targets.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## AVSC official and secondary source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:AVSC` | https://www.avantisinvestors.com/avantis-investments/avantis-us-small-cap-equity-etf/ | Official Avantis product page: identity, active strategy, current NAV/market price, current YTD and expense ratio | Product page reviewed 2026-08-17; NAV `$75.22` and market price `$75.25` as of 2026-08-14; NAV TR YTD `23.92%` and market-price YTD `23.71%` as of 2026-07-31; gross/net expense ratio `0.25%` as of 2026-01-01 |
| `NYSE Arca:AVSC` | https://res.avantisinvestors.com/docs/avantis-us-small-cap-equity-avsc-etf-fact-sheet.pdf | Official Avantis factsheet: rolling NAV, market-price and Russell 2000 benchmark returns, inception, fee, AUM, holdings and management team | Factsheet as of 2026-06-30; NAV 1Y `43.54%`, 3Y annualized `18.50%`, since-inception annualized `10.24%`; Russell 2000 `40.78%`, `18.60%`, `8.97%`; AUM `$3.0B`; holdings `1,516`; expense `0.25%` |
| `NYSE Arca:AVSC` | https://www.sec.gov/Archives/edgar/data/1710607/000171060725000415/acetftavsc497k.htm | Official SEC summary prospectus: inception, active investment process, fees, risks, turnover, official 2024 return and quarter extremes | Summary prospectus dated 2026-01-01; inception 2022-01-11; portfolio turnover `5%` for latest fiscal year; 2024 return before taxes `7.76%`; highest quarter `15.75%` in Q4 2023; lowest quarter `-4.21%` in Q2 2024 |
| `NYSE Arca:AVSC` | https://www.aaii.com/fund/ticker/AVSC | Secondary AAII/Morningstar annual NAV total-return observations used as a compact calendar proxy | Page reviewed 2026-08-17; annual rows 2023 `19.4%`, 2024 `7.8%`, 2025 `9.4%`; current YTD `23.9%` is retained only as a cross-check |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | Cached USD total-return convention with dividends reinvested; annual window 2023-2025 as of 2025-12-31 |

## AVSC raw observations and calculations

| Year / window | AVSC secondary NAV total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2023 | 19.40% | 26.29% |
| 2024 | 7.80% | 25.02% |
| 2025 | 9.40% | 17.88% |
| 2023-2025 cumulative | 40.81% | 86.12% |
| 2023-2025 rounded-input CAGR | 12.08% | 23.01% |

`*` AVSC annual rows are AAII/Morningstar secondary NAV total-return
observations, not a complete issuer-published calendar table. S&P 500 rows
reuse the cached USD Total Return convention as of 2025-12-31.

- Metric basis: official Avantis NAV Total Return includes reinvested distributions and fund expenses; USD; market-price return remains separate.
- Identity and classification: Avantis and SEC materials identify AVSC as Avantis U.S. Small Cap Equity ETF, listed on NYSE Arca, actively managed, and not seeking to replicate a specified index. The official factsheet names Russell 2000 as the benchmark.
- Active process: the SEC prospectus describes selection and weighting using company financials and market data, including book value, cash flows, profitability, market capitalization, liquidity and implementation costs; the portfolio managers make buy, sell and hold decisions.
- Official rolling fields: as of 2026-06-30 AVSC NAV TR was `43.54%` for 1Y, `18.50%` annualized for 3Y and `10.24%` annualized since inception; Russell 2000 was `40.78%`, `18.60%` and `8.97%` respectively. Reported return differences are `+2.76 pp`, `-0.10 pp` and `+1.27 pp`; these are not alpha.
- Formula: cumulative return is `product(1 + annual return) - 1`; CAGR is `cumulative^(1/n) - 1`; displayed annual inputs are rounded, so the CAGR is labelled rounded-input.
- Proxy calculations: 2023-2025 cumulative `40.81%`, rounded-input CAGR `12.08%`; annual-return population standard deviation `5.13%`; up/down years `3 / 0`; best 2023 `+19.40%`; least positive 2025 `+9.40%`.
- The fund began in 2022, so the strict 2021-2025 common window is not available. No 10-year NAV CAGR, 2021-2025 CAGR, or common-window ranking row is inferred.
- Source reconciliation: SEC 2024 official return before taxes is `7.76%`, while the secondary AAII/Morningstar row is `7.8%`; the difference is consistent with rounding and the sources are not mixed.
- Current issuer fields: NAV `$75.22` and market price `$75.25` as of 2026-08-14; current official NAV TR YTD `23.92%` as of 2026-07-31; gross/net expense ratio `0.25%` as of 2026-01-01.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; no numeric NAV drawdown or recovery proxy is saved.

## AVSC gaps and scheduled-inline local review

- Canonical identity is `NYSE Arca:AVSC`; Avantis product, factsheet and SEC prospectus confirm the exchange, fund name, active long-only structure and 2022-01-11 inception.
- AVSC is within supported ETF scope as an active long-only equity ETF. It is not a passive/index-tracking fund, but it has no leverage, inverse, bond, commodity, covered-call, option-income or derivative-heavy structure in the reviewed official materials.
- Management benchmark is `Russell 2000` from the official factsheet; S&P 500 remains only the common reference benchmark. One-year and since-inception reported excess returns are positive, while the three-year comparison is slightly negative; this is mixed, short-track-record evidence.
- Complete official calendar NAV rows beyond the SEC 2024 cross-check were not captured. The 2023-2025 annual table is a single secondary proxy and is excluded from strict active-skill scoring.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; risk evidence is therefore not-verified beyond the issuer's qualitative risk disclosures and quarter extremes.
- Planned durable paths: created `wiki/analysis/performance/ETF_NYSE_ARCA_AVSC Performance.md`; updated `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region USA; breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; canonical tag `geography/United-States`; all affected wikilinks resolve to existing targets.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## DFSV official and secondary source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:DFSV` | https://www.sec.gov/Archives/edgar/data/1816125/000174177325001189/c497k.htm | Official SEC summary prospectus: identity, exchange, active strategy, fee, turnover, risks, annual 2023-2024 returns and Russell 2000 Value comparison | Prospectus dated 2025-02-28; 2023 NAV TR `19.23%`, 2024 NAV TR `7.27%`, 2024 1-year Russell 2000 Value `8.05%`, since-inception NAV `9.50%` vs Russell 2000 Value `5.16%` through 2024-12-31 |
| `NYSE Arca:DFSV` | https://my.dimensional.com/chmedia/282748/source/dimensional-etf-quick-guide.pdf | Official Dimensional ETF quick guide: 2025 annual NAV return, since-inception return, fee, AUM, company count, inception and listing dates | Data as of 2025-12-31; NAV 1-year `8.51%`, since-inception annualized `9.25%`, gross/net expense `0.30%`/`0.30%`, AUM `$5,978M`, 1,008 companies, inception 2022-02-23, listing 2022-02-24 |
| `NYSE Arca:DFSV` | https://www.dimensional.com/us-en/funds/dfsv/us-small-cap-value-etf | Official Dimensional fund page: current fund identity and product context | Page reviewed 2026-08-17; dynamic performance fields were not exposed in the text capture, so no unsupported current official figure is inferred |
| `NYSE Arca:DFSV` | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=dfsv | Secondary fixed-date performance cross-check: NAV/market-price returns and current performance windows | Returns as of 2026-06-30; NAV YTD `18.7%`, 1-year `33.8%`, 3-year annualized `16.4%`, inception annualized `12.5%`; current fields are secondary, not issuer-published |
| `NYSE Arca:DFSV` | https://www.financecharts.com/etfs/DFSV/performance/total-return | Secondary total-return cross-check for calendar rows and later snapshot | Page reviewed 2026-08-13; secondary rows 2023 `19.25%`, 2024 `7.13%`, 2025 `8.60%`; these differ from official rows and are excluded from the official calculation |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | Cached USD total-return convention with dividends reinvested; annual window 2023-2025 as of 2025-12-31 |

## DFSV raw observations and calculations

| Year / window | DFSV NAV TR | Russell 2000 Value | S&P 500 TR |
|---|---:|---:|---:|
| 2023 | 19.23% | not disclosed | 26.29% |
| 2024 | 7.27% | 8.05% | 25.02% |
| 2025 | 8.51% | not disclosed | 17.88% |
| 2023-2025 cumulative | 38.78% | not disclosed | 86.12% |
| 2023-2025 rounded-input CAGR | 11.54% | not disclosed | 23.01% |

- Metric basis: official Dimensional NAV Total Return includes reinvestment of dividends and other earnings; USD; market-price return remains separate. The 2023 and 2024 rows come from the SEC summary prospectus and the 2025 row from the official Dimensional quick guide, all treated as official NAV return evidence.
- Identity and classification: Dimensional and SEC materials identify DFSV as the Dimensional US Small Cap Value ETF, listed on NYSE Arca, actively managed, and not seeking to replicate a specific index. The strategy uses a broad, market-cap-weighted portfolio of U.S. small-cap lower-relative-price stocks and may emphasize smaller companies and higher profitability.
- Management benchmark: the SEC performance table uses the `Russell 2000 Value Index`; S&P 500 Total Return is retained only as the common reference benchmark. The 2024 official comparison was DFSV `7.27%` versus Russell 2000 Value `8.05%`; since inception through 2024-12-31 it was `9.50%` versus `5.16%`. These are benchmark-relative observations, not alpha.
- Current official fields: the official quick guide as of 2025-12-31 reports NAV 1-year `8.51%`, since-inception annualized `9.25%`, gross/net expense `0.30%`/`0.30%`, AUM `$5,978M`, and `1,008` companies. The SEC summary prospectus reports portfolio turnover `8%` for the latest fiscal year.
- Current secondary fields: Schwab reports as of 2026-06-30 NAV YTD `18.7%`, 1-year `33.8%`, 3-year annualized `16.4%`, and inception annualized `12.5%`; these are retained as a secondary current snapshot because the dynamic Dimensional page did not expose a text-readable current table.
- Formula: cumulative return is `product(1 + annual return) - 1`; CAGR is `cumulative^(1/n) - 1`; displayed annual inputs are rounded, so the calculated 2023-2025 CAGR is labelled rounded-input.
- Calculations: official 2023-2025 cumulative `38.78%`, rounded-input CAGR `11.54%`, annual-return population standard deviation `5.37%`, up/down years `3 / 0`, best 2023 `+19.23%`, and least positive 2025 `+8.51%`. A 10-year or 2021-2025 CAGR is not calculated because the fund began in 2022.
- Source reconciliation: FinanceCharts secondary rows `19.25%`/`7.13%`/`8.60%` differ from the official `19.23%`/`7.27%`/`8.51%` rows; the secondary series is excluded from the saved official calculation rather than mixed with it.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; no numeric NAV drawdown or recovery proxy is saved.

## DFSV gaps and scheduled-inline local review

- Canonical identity is `NYSE Arca:DFSV`; the SEC prospectus and Dimensional materials confirm the exchange, fund name, active long-only equity structure, 2022-02-23 inception and 2022-02-24 listing.
- DFSV is within supported `check-etf-performance` scope as an active long-only equity ETF. The prospectus permits limited futures/options use for adjusting equity exposure around cash flows, but the fund is not derivative-heavy, leveraged, inverse, bond, commodity, covered-call or option-income.
- Management benchmark is `Russell 2000 Value`; official evidence is mixed and short-track-record: 2024 trailed the benchmark while since-inception through 2024-12-31 led it. No alpha claim is made.
- Official 2023-2025 rows are complete only through two official documents with different publication dates; the 2023-2025 calculation is retained as an official-row combination with source provenance, while secondary conflicting rows are excluded.
- Official current 2026 text-readable NAV fields and daily NAV history sufficient for maximum drawdown/recovery were not verified; current 2026 fields are explicitly secondary and the drawdown/recovery gap remains disclosed.
- Planned durable paths: created `wiki/analysis/performance/ETF_NYSE_ARCA_DFSV Performance.md`; updated `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region USA; breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; canonical tag `geography/United-States`; all affected wikilinks resolve to existing targets.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## PSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NASDAQ:PSC | https://www.principalam.com/us/fund/psc | Official Principal product page: identity, Nasdaq listing, active rules-based factor process, Russell 2000 benchmark, current performance, price/NAV and fund facts | Performance table as of 2026-07-31; current fund facts as of 2026-08-14; NAV YTD 18.52%, 1-year 29.43%, 3-year annualized 16.19%, 5-year annualized 9.54%, since-inception annualized 12.01%; NAV US$70.73, price US$70.76, assets US$2.4B, gross/net expense 0.38%/0.38% |
| NASDAQ:PSC | https://brandassets.principal.com/m/2b8aa0c162042812/original/Principal-U-S-Small-Cap-ETF-Quarterly-Commentary.pdf | Official quarterly commentary: calendar NAV rows, Russell 2000 rows, current Q2 cross-check and strategy-change caveat | Q2 2026 as of 2026-06-30; official NAV rows 2017-2025; PSC Q2 22.52% vs Russell 2000 21.49%; prior strategy differed before 2022-07-08 |
| NASDAQ:PSC | https://brandassets.principal.com/m/157c05db44e9d2ec/original/Principal-ETF-Reference-Sheet.pdf | Official ETF reference sheet: fund name, inception, exchange, benchmark and expense cross-check | PSC inception 2016-09-21; Nasdaq; Russell 2000; gross expense 0.38% |
| NASDAQ:PSC | https://www.sec.gov/Archives/edgar/data/1572661/000139834425017144/fp0095168-1_ncsrixbrl.htm | Official SEC annual shareholder report: objective, small-cap policy and expense disclosure | Principal U.S. Small-Cap ETF; long-term growth; normally at least 80% in small-cap equity; expense cost 0.38% |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | Cached USD total-return convention with dividends reinvested; annual window 2017-2025 as of 2025-12-31 |

## PSC raw observations and calculations

| Year / window | PSC NAV TR | Russell 2000 TR | S&P 500 TR |
|---|---:|---:|---:|
| 2017 | 13.41% | 14.65% | 21.83% |
| 2018 | -9.23% | -11.01% | -4.38% |
| 2019 | 18.87% | 25.52% | 31.49% |
| 2020 | 13.45% | 19.96% | 18.40% |
| 2021 | 32.32% | 14.82% | 28.71% |
| 2022 | -15.99% | -20.44% | -18.11% |
| 2023 | 18.53% | 16.93% | 26.29% |
| 2024 | 12.34% | 11.54% | 25.02% |
| 2025 | 13.39% | 12.81% | 17.88% |
| 2017-2025 cumulative | 133.00% | 106.48% | 255.78% |
| 2017-2025 rounded-input CAGR | 9.85% | 8.39% | 15.14% |
| 2021-2025 cumulative | 67.84% | 34.41% | 96.17% |
| 2021-2025 rounded-input CAGR | 10.91% | 6.09% | 14.43% |

- Metric basis: official Principal NAV Total Return includes reinvested distributions and fund expenses; USD; market-price return remains separate.
- Identity and classification: Principal identifies PSC as an active rules-based U.S. small-cap ETF using quality, momentum and value factors, normally at least 80% in the Russell 2000 market-cap range. It is within supported active-equity-long-only scope and is not derivative-heavy.
- Official current fields: as of 2026-07-31 NAV YTD 18.52%, 1-year 29.43%, 3-year annualized 16.19%, 5-year annualized 9.54%, since-inception annualized 12.01%; Russell 2000 18.85%, 34.18%, 15.08%, and 7.11% for the comparable windows. Product facts as of 2026-08-14 include NAV US$70.73, price US$70.76, assets US$2.4B, and SEC yield 0.56%.
- Calculations: official 2017-2025 cumulative 133.00%, rounded-input CAGR 9.85%, annual-return population standard deviation 13.86%, up/down years 7 / 2, best 2021 +32.32%, worst 2022 -15.99%; 2021-2025 CAGR 10.91%.
- Active comparison: annual hit rate 6 / 9, cumulative relative wealth +24.91% versus Russell 2000, and rounded-input Excess CAGR +1.47 pp. These are benchmark-relative observations, not alpha.
- Source reconciliation: the latest product-page performance table is as of 2026-07-31, while the calendar-year table is from the official Q2 commentary as of 2026-06-30. Principal states that the strategy before 2022-07-08 differed from the current strategy; the combined 2017-2025 history is retained with that caveat.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; no numeric NAV drawdown or recovery proxy is saved.

## PSC gaps and scheduled-inline local review

- Canonical identity is NASDAQ:PSC; official Principal materials confirm the fund name, exchange, inception, benchmark, active rules-based process and fee.
- PSC is within supported check-etf-performance scope as an active long-only equity ETF. The reviewed materials do not identify a leveraged, inverse, bond, commodity, covered-call, option-income or derivative-heavy structure.
- The annual window combines the pre-2022-07-08 strategy with the current active process; current-process attribution remains provisional.
- Daily NAV history sufficient for maximum drawdown and recovery was not verified; the gap is disclosed on the performance page.
- Planned durable paths were written: wiki/analysis/performance/ETF_NASDAQ_PSC Performance.md, wiki/analysis/comparisons/USA ETF.md, wiki/analysis/comparisons/ETF Region Index.md, wiki/analysis/performance/ETF Performance Index.md, this source batch, and log.md.
- Planned graph changes were applied: primary region USA; breadcrumb [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]; canonical tag geography/United-States.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## FESM official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:FESM` | https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F9911747.PDF | Official Fidelity factsheet: identity, active strategy, benchmark, NAV/market-price returns, annual rows, expense ratio and risk fields | Factsheet as of 2026-06-30; NAV TR YTD `28.42%`, 1-year `52.23%`, 3-year annualized `24.57%`, 5-year annualized `11.69%`, 10-year annualized `13.28%`; Russell 2000 `22.57%`, `40.78%`, `18.60%`, `6.98%`, `11.62%` |
| `NYSE Arca:FESM` | https://institutional.fidelity.com/app/proxy/content?literatureURL=%2FRD_QAA_7545.PDF | Official Fidelity Q&A: systematic multifactor process and quarterly performance comparison | Quarter ending 2026-06-30; confirms NAV 1-year/3-year/5-year/10-year returns and systematic, risk-aware process |
| `NYSE Arca:FESM` | https://www.sec.gov/Archives/edgar/data/945908/000094590826000151/filing12065.htm | Official SEC name-change supplement | Filed 2025-10-30; former `Fidelity Enhanced Small Cap ETF` changed to `Fidelity Enhanced Small Cap Core ETF` effective on/about 2026-05-11 |
| `NYSE Arca:FESM` | https://institutional.fidelity.com/advisors/investment-solutions/performance/fidelity-etfs | Official Fidelity ETF lineup: current identity, exchange, expense and fund metadata cross-check | Page reviewed 2026-08-17; current FESM Core identity and `0.28%` expense cross-check |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | Cached USD total-return convention with dividends reinvested; annual window 2016-2025 as of 2025-12-31 |

## FESM raw observations and calculations

| Year / window | FESM NAV TR | Russell 2000 TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 22.84% | 21.31% | 11.96% |
| 2017 | 7.22% | 14.65% | 21.83% |
| 2018 | -13.04% | -11.01% | -4.38% |
| 2019 | 23.65% | 25.52% | 31.49% |
| 2020 | 18.53% | 19.96% | 18.40% |
| 2021 | 20.54% | 14.82% | 28.71% |
| 2022 | -18.28% | -20.44% | -18.11% |
| 2023 | 21.04% | 16.93% | 26.29% |
| 2024 | 16.48% | 11.54% | 25.02% |
| 2025 | 17.70% | 12.81% | 17.88% |
| 2016-2025 cumulative | 174.39% | 150.48% | 298.33% |
| 2016-2025 rounded-input CAGR | 10.62% | 9.62% | 14.82% |
| 2021-2025 cumulative | 63.46% | 34.41% | 96.17% |
| 2021-2025 rounded-input CAGR | 10.33% | 6.09% | 14.43% |

- Metric basis: official Fidelity NAV Total Return includes reinvested dividends/capital gains and fund expenses; USD; market-price return remains separate. The annual NAV rows are official factsheet rows, while the S&P 500 rows reuse the cached USD Total Return convention.
- Identity and classification: Fidelity identifies FESM as the actively managed Fidelity Enhanced Small Cap Core ETF, listed on NYSE Arca, normally investing at least 80% in Russell 2000 securities and using quantitative analysis of valuation, growth and profitability factors. Before 2026-05-11 the fund was named Fidelity Enhanced Small Cap ETF.
- Structural caveat: the fund reorganized from a predecessor mutual fund effective 2023-11-17 and first listed as an ETF on 2023-11-20; rows before 2023-11-17 are predecessor history and should not be read as ETF-market-price history.
- Official rolling fields: as of 2026-06-30 FESM NAV TR was `28.42%` YTD, `52.23%` for 1-year, `24.57%` annualized for 3-year, `11.69%` annualized for 5-year and `13.28%` annualized for 10-year; the matching Russell 2000 figures were `22.57%`, `40.78%`, `18.60%`, `6.98%` and `11.62%`. Reported differences are `+5.85 pp`, `+11.45 pp`, `+5.97 pp`, `+4.71 pp` and `+1.66 pp`; these are excess-return comparisons, not alpha.
- Formula: cumulative return is `product(1 + annual return) - 1`; CAGR is `cumulative^(1/n) - 1`; displayed annual inputs are rounded, so calculated CAGRs are labelled rounded-input.
- Calculations: 2016-2025 cumulative `174.39%`, rounded-input CAGR `10.62%`; 2021-2025 cumulative `63.46%`, rounded-input CAGR `10.33%`; annual-return population standard deviation `14.38%` versus Russell 2000 `13.91%`; active annual difference was positive in `6 / 10` years; relative wealth versus Russell 2000 was `+9.55%` cumulative and excess CAGR was `+1.00 pp`.
- Return profile: FESM had `8` up years and `2` down years; best year was 2019 at `+23.65%`; worst year was 2018 at `-13.04%`.
- Current issuer fields: assets `$5,784.9M`, holdings `786`, turnover `41%` for 12/25, beta `1.02`, 3-year standard deviation `20.52%`, 30-day SEC yield `0.52%`, top 10 holdings `7.97%`, and gross/net expense ratio `0.28%`/`0.28%`.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; no numeric NAV drawdown or recovery proxy is saved.

## FESM gaps and scheduled-inline local review

- Canonical identity is `NYSE Arca:FESM`; Fidelity factsheet, Q&A, lineup and SEC supplement confirm the exchange, current fund name, active long-only equity structure and the 2026-05-11 name transition.
- FESM is within supported `check-etf-performance` scope as an active long-only equity ETF. The reviewed official materials do not identify a leveraged, inverse, bond, commodity, covered-call, option-income or derivative-heavy structure.
- The management benchmark is `Russell 2000`; S&P 500 remains only a common reference benchmark. The positive return comparisons and `6 / 10` annual hit rate are management evidence, not alpha.
- Official calendar rows are complete for 2016-2025 but mix predecessor mutual-fund history with the current ETF period; the predecessor and 2023-11-20 first-listing caveats remain attached to the page.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; this remains a disclosed gap.
- Planned durable paths: created `wiki/analysis/performance/ETF_NYSE_ARCA_FESM Performance.md`; updated `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region USA; breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; canonical tag `geography/United-States`; all affected wikilinks resolve to existing targets.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## SFLO official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:SFLO` | https://advisor.vcm.com/products/victoryshares-etfs/victoryshares-etfs-list/victoryshares-small-cap-free-cash-flow-etf | Official Victory product page: identity, passive/index objective, index strategy, risk context and current-performance navigation | Product page reviewed 2026-08-17; standardized performance is linked to the current factsheet; net-expense waiver through 2026-10-31 |
| `NASDAQ:SFLO` | https://www.vcm.com/assets/etf/factsheet-pdf/VS%20SFLO%20FS.pdf | Official Victory factsheet: current NAV/market-price/index returns, expense ratio, inception, listing, holdings, index method and risk fields | Factsheet as of 2026-06-30; NAV YTD `16.54%`, market-price YTD `16.47%`, issuer-index YTD `16.95%`, 1-year NAV `31.73%`, since-inception annualized NAV `14.48%`, gross/net expense `0.56%`/`0.49%`, holdings `202` |
| `NASDAQ:SFLO` | https://www.sec.gov/Archives/edgar/data/1547580/000119312525260722/f43139d1.htm | Official SEC summary prospectus: Nasdaq listing, passive objective, 80% index/small-cap policy, fee waiver, 2024 calendar return and inception date | Prospectus dated 2025-11-01; 2024 NAV total return before taxes `6.49%` for the year ended 2024-12-31; SEC inception date `2023-12-21` |
| `NASDAQ:SFLO` | https://ir.vcm.com/news/news-details/2023/Victory-Capital-Adds-VictoryShares-Small-Cap-Free-Cash-Flow-ETF-to-its-ETF-Lineup/default.aspx | Official Victory Capital launch announcement: fund launch, rules-based structure and tracked index | Published 2023-12-21; launch context and index objective |
| `Victory U.S. Small Cap Free Cash Flow Index` | https://www.vettafi.com/indexing/index/sflo | Official index provider page: index identity, equity classification, region, quarterly rebalance and linked SFLO product | Page reviewed 2026-08-17; index total-return/current fields are kept separate from fund NAV returns |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## SFLO raw observations and calculations

| Year / window | SFLO NAV TR | SFLO Market Price TR | Issuer index / S&P 500 TR |
|---|---:|---:|---:|
| 2024 calendar year | 6.49% | not disclosed | Victory index not disclosed in SEC calendar table; S&P 500 TR 25.02% |
| QTD 2026-06-30 | 14.24% | 14.22% | Victory index 14.45%; S&P 500 not synchronized |
| YTD 2026-06-30 | 16.54% | 16.47% | Victory index 16.95%; S&P 500 not synchronized |
| 1-year 2026-06-30 | 31.73% | 31.73% | Victory index 32.65%; S&P 500 not synchronized |
| Since inception annualized 2026-06-30 | 14.48% | 14.46% | not applicable |

- Metric basis: official Victory NAV Total Return includes reinvestment of dividends/capital gains and reflects fund expenses; market-price and issuer-index returns remain separate; currency USD.
- Issuer benchmark: `Victory U.S. Small Cap Free Cash Flow Index`; the rules-based index screens profitable U.S. small-cap companies for free-cash-flow yield and growth, selects 200 stocks, and rebalances/reconstitutes quarterly.
- Inception conflict: factsheet lists `2023-12-20`; SEC summary prospectus and Victory ETF lineup list `2023-12-21`. Both are retained; neither is used to fabricate a 10-year window.
- 2023 is an inception-year partial and is excluded. The reviewed SEC prospectus provides the complete 2024 NAV row `6.49%`; a complete official 2025 calendar NAV row was not found.
- 2021-2025 CAGR, up/down counts, best/worst year ranking, annual-return volatility and max drawdown/recovery are not calculated because only one complete official calendar-year NAV row is available and daily NAV history was not verified.
- S&P 500 cached rows are retained only as the common reference table; the issuer index is retained as fund metadata and not substituted for the S&P 500 comparison.

## SFLO gaps and scheduled-inline local review

- Canonical identity is `NASDAQ:SFLO`; the SEC prospectus and June 2026 factsheet agree on Nasdaq listing, passive/index objective, tracked index and fee structure. The one-day inception-date difference is recorded as a source conflict.
- SFLO is within ETF v1 scope: official materials describe a rules-based fund that seeks to track the Victory U.S. Small Cap Free Cash Flow Index, with at least 80% in index and small-cap equity securities; no active, leveraged, inverse, bond, commodity, multi-asset or derivative-heavy structure was found.
- The latest official factsheet provides NAV/market-price/index returns through 2026-06-30. The SEC prospectus provides a 2024 calendar NAV row but not a complete 2025 row; no secondary annual proxy is saved.
- Price/NAV, annual-return volatility, standard deviation, beta, max drawdown and recovery remain `ไม่พบข้อมูลที่ยืนยันได้` from the official source capture; the factsheet shows dashes for standard deviation, Sharpe ratio and beta, and no daily NAV history was verified.
- Planned durable paths: create `wiki/analysis/performance/ETF_NASDAQ_SFLO Performance.md`; update `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `USA`; add breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; preserve `geography/United-States`; link the new page from USA navigation and the performance index; keep numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## JHSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:JHSC` | https://www.jhinvestments.com/content/dam/jhi-investments/JHINV/public/ETFs/Documents/FactSheets/InvestorFactSheet/etf-multifactor-small-cap-investor-fact-sheet-jhi.pdf | Official John Hancock investor factsheet: fund identity, objective, index, exchange, inception, rolling NAV/market-price returns, fee, holdings and risk context | Factsheet data as of 2026-06-30; NAV YTD `16.34%`, market-price YTD `16.10%`, 1-year NAV `25.93%`, 3-year NAV `14.42%`, 5-year NAV `8.00%`, since-inception annualized NAV `9.14%`, gross/net expense `0.46%`/`0.42%`, holdings `496` |
| `NYSE Arca:JHSC` | https://www.sec.gov/Archives/edgar/data/1478482/000119312525191975/d942427d497k.htm | Official SEC summary prospectus: passive/index objective, listing, investment approach, advisor/subadvisor and risk disclosures | Prospectus dated 2025-09-01; fund seeks to track the John Hancock Dimensional Small Cap Index and normally invests at least 80% in index securities |
| `NYSE Arca:JHSC` | https://www.jhinvestments.com/content/dam/jhi-investments/JHINV/public/ETFs/Documents/Prospectuses/StatutoryProspectus/etf-multifactor-small-cap-statutory-prospectus-jhi.pdf | Official statutory prospectus: fund and index risk context, expense disclosure and historical financial-report ownership | Official issuer document reviewed 2026-08-17; no complete 2016-2025 calendar NAV table was found in the reviewed capture |
| `John Hancock ETFs` | https://www.jhinvestments.com/etf | Official issuer ETF lineup and product identity cross-check | Page reviewed 2026-08-17; JHSC is listed as Multifactor Small Cap ETF and Morningstar category Small Blend |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## JHSC raw observations and calculations

| Window | JHSC NAV TR | JHSC Market Price TR | S&P 500 TR |
|---|---:|---:|---:|
| QTD 2026-06-30 | 13.64% | 13.66% | not synchronized |
| YTD 2026-06-30 | 16.34% | 16.10% | not synchronized |
| 1-year 2026-06-30 | 25.93% | 25.72% | not synchronized |
| 3-year annualized 2026-06-30 | 14.42% | 14.40% | not synchronized |
| 5-year annualized 2026-06-30 | 8.00% | 7.99% | not synchronized |
| Since inception annualized 2026-06-30 | 9.14% | 9.14% | not applicable |

- Metric basis: official John Hancock NAV Total Return includes reinvested distributions and reflects fund expenses; market-price return remains separate; currency USD.
- Issuer benchmark: `John Hancock Dimensional Small Cap Index`; the index emphasizes smaller capitalization, lower relative price and higher profitability, with semiannual reconstitution/rebalance.
- JHSC inception is `2017-11-08`, so a 10-year NAV TR CAGR is not applicable as of the reviewed factsheet date.
- Complete official calendar-year NAV rows for 2016-2025 were not disclosed in the reviewed issuer materials. Therefore 2021-2025 CAGR, annual-return volatility, up/down counts, best/worst years, max drawdown and recovery are not calculated.
- S&P 500 cached annual rows are retained only as the common reference table in the performance page; no synchronized 2026 current-year comparison is asserted against JHSC's 2026-06-30 YTD.

## JHSC gaps and scheduled-inline local review

- Canonical identity is `NYSE Arca:JHSC`; the official factsheet and SEC prospectus agree on fund name, exchange, inception date and tracked index. No ticker/exchange alias conflict was found.
- JHSC is within ETF v1 scope: the SEC prospectus describes a passive/index-tracking approach to the John Hancock Dimensional Small Cap Index; no active, leveraged, inverse, bond, commodity, multi-asset or derivative-heavy structure was found.
- The issuer factsheet provides rolling/period performance through 2026-06-30 but not complete calendar-year NAV rows or daily NAV history. The performance page records these values as `not disclosed` rather than substituting fiscal-year returns from the annual report.
- Price/NAV, max drawdown, recovery, volatility and positive/negative-year counts remain `ไม่พบข้อมูลที่ยืนยันได้` from the official source capture; no secondary proxy is saved.
- Planned durable paths: create `wiki/analysis/performance/ETF_NYSE_ARCA_JHSC Performance.md`; update `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `USA`; add breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; preserve `geography/United-States`; link the new page from USA navigation and the performance index; keep numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## EES official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:EES` | https://www.wisdomtree.com/us/products/equity/ees | Official WisdomTree product page: fund identity, passive objective, WTSEI index, expense ratio, NAV/market price, annualized returns, current NAV TR YTD and distributions | Product and quote fields as of 2026-08-14; month-end performance through 2026-07-31 |
| `NYSE Arca:EES` | https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/us-equity/wisdomtree-factsheet-ees-1012.pdf | Official factsheet: exchange, inception, fee, NAV return definition, rolling performance and fund structure | Factsheet data as of 2026-06-30; stock exchange is NYSE Arca |
| `NYSE Arca:EES` | https://www.wisdomtree.com/us/media/ees-presentation | Official WisdomTree Q1-2026 presentation: complete 2016-2025 calendar NAV return rows | Presentation performance table as of 2026-03-31; annual rows cover 2016-2025 |
| `WTSEI` | https://www.wisdomtree.com/us/indexes/WTSEI?index=WTSEI | Official issuer benchmark page: index identity, earnings-positive eligibility and methodology context | Index page reviewed 2026-08-17; index facts through 2026-07-29 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current cross-check for S&P 500 (TR) | YTD `9.00%` as of 2026-07-28; not synchronized with EES 2026-07-31 YTD |

## EES raw observations and calculations

| Year | EES NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 29.96% | 11.96% |
| 2017 | 12.56% | 21.83% |
| 2018 | -9.96% | -4.38% |
| 2019 | 21.92% | 31.49% |
| 2020 | 2.79% | 18.40% |
| 2021 | 34.34% | 28.71% |
| 2022 | -16.16% | -18.11% |
| 2023 | 18.42% | 26.29% |
| 2024 | 9.89% | 25.02% |
| 2025 | 6.93% | 17.88% |
| 2026 YTD | 19.57% (official NAV TR, 2026-07-31) | 9.00% (official S&P 500 TR, 2026-07-28) |

- Metric basis: official WisdomTree NAV Total Return, calculated from the daily 4:00 p.m. NAV under the issuer performance convention; USD; fund expenses are reflected in NAV returns. Market-price return remains separate.
- Issuer benchmark: `WisdomTree U.S. SmallCap Index (WTSEI)`, formerly WisdomTree U.S. SmallCap Earnings Index; the fund seeks to track the index before fees and expenses.
- EES 2016-2025 compound: `158.70%` cumulative; rounded-input CAGR `9.97%`.
- EES 2021-2025 compound: `56.73%` cumulative; rounded-input CAGR `9.40%`.
- Issuer rolling 10-year NAV TR average annual: `10.85%` as of 2026-07-31; raw rolling endpoints are not disclosed and this is kept separate from the 2016-2025 calendar-window CAGR.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`; S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`; normalized 2016-2025 start TR value `100.00` and rounded-input end TR value `258.70`.
- Annual-return volatility: population standard deviation `15.31%` across the ten official rounded annual NAV observations.
- Up years / down years: `8 / 2`; best `2021 +34.34%`; least positive `2020 +2.79%`; worst `2022 -16.16%`; least bad down year `2018 -9.96%`.
- Current issuer fields: NAV `$69.712`, closing market price `$69.666`, expense ratio `0.38%`, and distribution yield `1.46%`, all as of 2026-08-14; current NAV TR YTD is as of 2026-07-31.

## EES gaps and scheduled-inline local review

- Canonical identity is `NYSE Arca:EES`; no ticker/exchange alias conflict was found. The input card ticker and title both resolve to `EES`.
- EES is within ETF v1 scope: WisdomTree describes it as tracking the earnings-generating U.S. small-cap index; no active, leveraged, inverse, bond, commodity, multi-asset or derivative-heavy structure was found.
- Annual rows are official issuer observations from the Q1-2026 presentation and are rounded; cumulative/CAGR calculations are therefore rounded-input approximations. No secondary annual proxy or partial year is used.
- The issuer rolling 10-year field `10.85%` is a separate average annual observation through 2026-07-31; raw endpoints are not disclosed, so the page does not relabel it as the calendar-window CAGR.
- The current S&P 500 TR cross-check is `9.00%` as of 2026-07-28, three calendar days before EES's 2026-07-31 current YTD field; no same-date current benchmark pair is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Planned durable paths: create `wiki/analysis/performance/ETF_NYSE_ARCA_EES Performance.md`; update `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `USA`; add breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; preserve `geography/United-States`; link the new page from USA navigation and the performance index; keep annual numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

annual_rows_as_of: "GSSC official 2018-2025; XSMO official 2016-2025; SSEUF canonical LSE:R2US official 2016-2025; FNDA secondary 2016-2025; ZPRVF canonical LSE:USSC official 2016-2025; NUSC official 2017-2025; IMWSF canonical LSE:WSML official 2019-2025; DES official 2016-2025; FNDC official 2016-2025; RWJ secondary 2016-2025; ISHOF canonical LSE:IDP6 official 2016-2025; DISV official 2023-2025 with 2022 inception partial excluded; CPLCF canonical LSE:CUSS official 2016-2025; BSVO unsupported active ETF; FYX official 2016-2025; IWMI unsupported active ETF; VB official 2016-2025; SCHA secondary 2016-2025; SPSM calendar rows not disclosed; VBR official 2016-2025; VTWO official 2016-2025; VSS official 2016-2025; IJR official 2016-2025; IWM official 2016-2025 at 0.1% precision; IWN official 2016-2025 at 0.1% precision; IWO official 2016-2025 at 0.1% precision; AVUV unsupported active ETF; DFAS unsupported active ETF; AVDV unsupported active ETF; SCZ official 2016-2025; BBSC official 2021-2025; ISCF official 2016-2024 SEC and 2025 factsheet; GWX calendar rows not disclosed; ISCV official 2016-2025; EES official 2016-2025; JHSC calendar rows not disclosed; SFLO official 2024 only; EWX secondary 2016-2025; AVSC secondary 2023-2025; FESM official 2016-2025 with predecessor history caveat; DFSV official 2023-2025; PSC official 2017-2025 with strategy-change caveat; current NAV/YTD fields through 2026-08-14; S&P current cross-check through 2026-08-10"
annual_rows_addendum: "JPSE official 2017-2025; 2016 inception-year partial excluded; XSVM official 2016-2025; JHSC calendar rows not disclosed; SFLO official 2024 only, 2023 inception-year partial excluded and 2025 row not disclosed; FESM official 2016-2025 with predecessor history; DFSV official 2023-2025, current 2026 fields secondary; PSC official 2017-2025, strategy change effective 2022-07-08"
tags:
  - source/etf
---

# ETF Performance Source Batch - 2026-08-17

## Scope and gate

Research-bearing lean source batch for GSSC, XSMO, SSEUF, FNDA, ZPRVF, NUSC, IMWSF, DES, FNDC, RWJ, ISHOF, DISV, CPLCF, BSVO, FYX, IWMI, VB, SCHA, SPSM, VBR, VTWO, VSS, IJR, IWM, IWN, IWO, AVUV, DFAS, AVDV, SCZ, BBSC, ISCF, GWX, ISCV, EES, JPSE, XSVM, JHSC, SFLO, OSCV, SMDV, SMIN, EWX, AVSC, FESM, DFSV, and PSC. Source discovery, reading, reconciliation,
calculation, synthesis, and the complete pre-save checklist were performed
inline under `scheduled-inline`. No research worker, reviewer,
`source_verifier`, or other sub-agent was dispatched.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## DISV retry refresh — active long-only support

- The earlier unsupported-type record is superseded by this retry because `check-etf-performance` now supports active long-only equity ETFs. The final type gate is `PASS` for `active-equity-long-only`.
- Input ticker: `DISV`; canonical identity: `Cboe BZX:DISV`; fund: Dimensional International Small Cap Value ETF; inception `2022-03-23`; listing date `2022-03-24`.
- Official SEC materials identify DISV as an actively managed ETF that does not seek to replicate a specific index. Long public equity is the principal return source; futures, options on futures, swaps and FX forwards are described for exposure, cash-flow and currency management and do not make the fund derivative-heavy for this scope.
- `active_process: systematic-active`; Dimensional describes an integrated research, portfolio-design, portfolio-management and trading process with flexible daily implementation.
- `management_benchmark: MSCI World ex USA Small Value Index (net dividends)`, selected because the official SEC performance table calls it an additional index with a similar investment universe. The broader MSCI World ex USA Index and the common S&P 500 reference were rejected as management comparators.
- Official annual chart rows: `2023 19.60%`, `2024 6.02%`, `2025 47.24%`; 2022 inception-year partial is not shown and is excluded. These rows compound to `86.70%` cumulative / rounded-input CAGR `23.14%`; population annual-return volatility is `17.15%`; up/down count is `3 / 0`.
- Official since-inception annualized return as of `2025-12-31`: DISV `14.78%` versus management benchmark `10.38%`, Excess CAGR `+4.40 pp`; compatible annual benchmark rows and hit rate are not disclosed, so management evidence is `positive return-only` and not alpha.
- Secondary Schwab current fields as of `2026-07-31`: NAV TR YTD `12.90%`, 1-year `31.90%`, 3-year annualized `22.40%`, since-inception annualized `15.90%`; market price `US$44.25` as of `2026-08-14`. These are kept separate from official issuer calendar rows.

### DISV official and secondary source map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `Cboe BZX:DISV` | https://www.sec.gov/Archives/edgar/data/1816125/000181612526000069/c497k.htm | Official SEC summary prospectus: identity, exchange, active status, strategy, expense ratio, turnover, annual chart, management benchmark and since-inception returns | Prospectus dated 2026-02-28; performance periods ended 2025-12-31; 2023-2025 annual chart; 2022-03-23 inception |
| `Cboe BZX:DISV` | https://www.sec.gov/Archives/edgar/data/1816125/000181612526000046/c485bpos.htm | Official SEC prospectus: integrated active process, portfolio construction, flexible trading, portfolio manager continuity and derivative-use context | Prospectus dated 2026-02-28; latest fiscal-year turnover 8% |
| `Cboe BZX:DISV` | https://www.dimensional.com/us-en/funds/disv/international-small-cap-value | Official issuer fund identity and strategy page | Page reviewed 2026-08-17; numeric performance fields not exposed in the captured HTML |
| `Cboe BZX:DISV` | https://www.dimensional.com/us-en/etfs | Official issuer ETF lineup and active-ETF classification | Page reviewed 2026-08-17; Dimensional describes 44 active ETFs as of 2026-06-30 |
| `Cboe BZX:DISV` | https://my.dimensional.com/chmedia/282748/source/dimensional-etf-quick-guide.pdf | Official Dimensional Quick Guide: annualized NAV/market-price returns, benchmark and expense cross-check | Guide as of 2025-12-31; NAV 1-year `47.24%`, since inception `14.78%`; MSCI World ex USA Small Value Index `38.55%` / `10.38%`; net expense `0.42%` |
| `Cboe BZX:DISV` | https://www.cboe.com/us/equities/listings/listed_products/symbols/DISV | Official exchange listing and identity cross-check | Listing page reviewed 2026-08-17 |
| `Cboe BZX:DISV` | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=disv | Secondary current NAV/market-price performance and price cross-check | Performance as of 2026-07-31; price as of 2026-08-14 |
| `S&P 500 TR` | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

### DISV raw observations and calculations

| Year / window | DISV NAV TR | S&P 500 TR | Management benchmark |
|---|---:|---:|---:|
| 2023 | 19.60% | 26.29% | not disclosed as annual row |
| 2024 | 6.02% | 25.02% | not disclosed as annual row |
| 2025 | 47.24% | 17.88% | not disclosed as annual row |
| 2023-2025 cumulative | 86.70% | 86.12% | not comparable from annual rows |
| Since inception annualized, 2022-03-23 to 2025-12-31 | 14.78% | not paired | 10.38% |
| 2026 YTD | 12.90% (secondary NAV, 2026-07-31) | not synchronized | not synchronized |

- Metric basis: official DISV NAV Total Return includes reinvested distributions and fund expenses; market-price return remains separate. Currency is USD.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`; 2023-2025 normalized start TR value `100.00` and rounded-input end TR value `186.70`.
- 2023-2025 annual active returns versus S&P 500 common reference were `-6.69`, `-19.00`, and `+29.36 pp`; these are not management-benchmark evidence.
- Official SEC highest quarter was `+15.12%` in 2025 Q2; lowest quarter was `-7.54%` in 2024 Q4. Official daily NAV history sufficient for maximum drawdown and recovery was not verified.

### DISV scheduled-local review

- Complete pre-save checklist reviewed locally: canonical identity/exchange, official active long-only eligibility, active-process subtype, management-benchmark selection, complete-year markers, common S&P 500 comparison, secondary labels, current as-of dates, calculations, management-evidence label, risk-evidence status, output paths, graph links and card result metadata.
- Result: local `PASS`; performance page and source batch refresh were written. No research worker, reviewer, `source_verifier`, or other sub-agent was dispatched.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## ISHOF / IDP6 official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:IDP6 / input ISHOF | https://www.ishares.com/uk/individual/en/products/251920/ishares-s-p-smallcap-600-ucits-etf?siteEntryPassthrough=true | Official iShares product page: identity, listings, ISIN, index, structure, expense ratio, NAV, YTD, risk fields and calendar NAV TR rows | Product/current fields through 2026-07-31; NAV TR YTD through 2026-07-30; calendar rows 2016-2025 |
| LSE:IDP6 / input ISHOF | https://www.blackrock.com/uk/professional/en/literature/fact-sheet/isp6-ishares-s-p-smallcap-600-ucits-etf-fund-fact-sheet-en-gb.pdf | Official factsheet: USD distributing share class and calendar NAV performance | Calendar rows 2016-2025; factsheet capture dated 2026-03-31 / 2026-04-14 fields |
| LSE:IDP6 / input ISHOF | https://www.ishares.com/uk/professional/en/literature/kiid/ucits_kiid-ishares-sp-smallcap-600-ucits-etf-usd-dist-gb-ie00b2qwcy14-en.pdf | Official KIID: passive objective, benchmark, NAV return definition and small-cap/liquidity risk | KIID reviewed 2026-08-17 |
| S&P 500 TR current | https://www.slickcharts.com/sp500/returns/ytd | Secondary current benchmark cross-check | `10.14%` total return YTD through 2026-07-31; one day later than IDP6 current YTD |

## ISHOF / IDP6 raw observations and calculations

| Year | IDP6 NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 25.93% | 11.96% |
| 2017 | 12.62% | 21.83% |
| 2018 | -8.95% | -4.38% |
| 2019 | 22.04% | 31.49% |
| 2020 | 10.64% | 18.40% |
| 2021 | 26.25% | 28.71% |
| 2022 | -16.72% | -18.11% |
| 2023 | 15.43% | 26.29% |
| 2024 | 8.04% | 25.02% |
| 2025 | 5.55% | 17.88% |
| 2026 YTD | 21.36% | 10.14%† |

- Metric basis: official iShares NAV Total Return, with gross income reinvested where applicable and performance after ongoing charges; USD share-class values are used for the canonical USD line.
- `†` secondary S&P 500 current cross-check with a different as-of date; complete-year benchmark rows use the cached project convention.
- 2016-2025 IDP6 compound: `141.31%` cumulative; rounded-input CAGR `9.21%`.
- 2021-2025 IDP6 compound: `38.40%` cumulative; rounded-input CAGR `6.72%`.
- Annual-row positive/negative years: `8 / 2`; best 2016 `+25.93%`, worst 2022 `-16.72%`.
- Official current NAV TR YTD: `21.36%` as of 2026-07-30; NAV quote `US$117.48` as of 2026-07-31.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.

## ISHOF / IDP6 gaps, alias resolution, and scheduled-local gate

- ISHOF is an OTC input alias; official iShares listings for ISIN `IE00B2QWCY14` identify the USD London line as `IDP6`, while `ISP6` is the GBP London line of the same fund. Durable ownership uses `LSE:IDP6` and preserves ISHOF as `input_alias`.
- The latest official iShares current NAV TR field located is `21.36%` as of 2026-07-30. The latest displayed NAV quote is `US$117.48` as of 2026-07-31; these are separate as-of fields.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Complete pre-save checklist: identity/exchange/index, alias and ISIN, return basis, benchmark, candidate claims, periods, units/currencies, metric definitions, as-of dates, calculations, source URLs, unresolved gaps, exact planned page/batch/index/log contents, graph links, and ownership were reviewed locally before write.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## Complete evidence register

| Input ticker | Status | Canonical entity key | Primary region | Current NAV YTD / as-of | Primary source | Gap / resolution note |
|---|---|---|---|---|---|---|
| GSSC | supported | NYSE Arca:GSSC | USA | 21.33% (2026-06-30) | https://am.gs.com/public-assets/documents/574deb07-24d6-11ef-870d-c7a1cb19e681 | passive/index-tracking U.S. small-cap multi-factor equity; 10-year history not yet available; daily NAV drawdown/recovery not disclosed |
| XSMO | supported | NYSE Arca:XSMO | USA | 30.50% (2026-06-30, secondary NAV) | https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/xsmo-invesco-s-p-smallcap-momentum-etf-fact-sheet.pdf | passive/index-tracking U.S. small-cap momentum equity; official current YTD not located; daily NAV drawdown/recovery not disclosed |
| SSEUF | supported | LSE:R2US | USA | 18.69% (2026-07-31) | https://www.ssga.com/uk/en_gb/institutional/etfs/state-street-spdr-russell-2000-us-small-cap-ucits-etf-acc-zprr-gy | OTC alias for official USD LSE line; passive/index-tracking U.S. small-cap equity; daily NAV drawdown/recovery not disclosed |
| FNDA | supported | NYSE Arca:FNDA | USA | 21.18% (2026-06-30) | https://www.schwabassetmanagement.com/products/fnda | passive/index-tracking U.S. small-cap fundamental equity; annual calendar rows are secondary total-return proxy; daily NAV drawdown/recovery not disclosed |
| NUSC | supported | Cboe BZX:NUSC | USA | 16.76% (2026-06-30) | https://documents.nuveen.com/Documents/Nuveen/Viewer.aspx?uniqueId=8238272c-9326-4c32-93cb-40d80e4fc4a9 | passive/index-tracking U.S. small-cap ESG equity; history under 10 years; Nuveen HTML performance table rendered no records, official PDF factsheet used; daily NAV drawdown/recovery not disclosed |
| IMWSF | supported | LSE:WSML | International | 19.00% (2026-08-13) | https://www.ishares.com/uk/professionals/en/products/296576/ishares-msci-world-small-cap-ucits-etf-fund?siteEntryPassthrough=true&switchLocale=y | OTC alias resolved to official USD LSE line by ISIN `IE00BF4RFH31`; passive/global developed small-cap equity; history under 10 years; daily NAV drawdown/recovery not disclosed |
| DES | supported | NYSE Arca:DES | USA | 22.93% (2026-07-31) | https://www.wisdomtree.com/us/products/equity/des | passive/index-tracking U.S. small-cap dividend equity; official 2016-2025 annual NAV rows; current S&P cross-check is not same-date; daily NAV drawdown/recovery not disclosed |
| FNDC | supported | NYSE Arca:FNDC | International | 10.96% (2026-07-31) | https://www.schwabassetmanagement.com/products/fndc | passive/index-tracking developed ex-U.S. small-cap fundamental equity; benchmark changed effective 2024-06-21; daily NAV drawdown/recovery not disclosed |
| RWJ | supported | NYSE Arca:RWJ | USA | 28.61% (2026-08-14, secondary proxy) | https://www.sec.gov/Archives/edgar/data/1378872/000119312525325669/d54028d497k.htm | passive/index-tracking U.S. small-cap revenue-weighted equity; annual/current fields use secondary dividend-reinvested proxy; official SEC average annual return kept separate |
| ISHOF | supported | LSE:IDP6 | USA | 21.36% (2026-07-30) | https://www.ishares.com/uk/individual/en/products/251920/ishares-s-p-smallcap-600-ucits-etf?siteEntryPassthrough=true | OTC alias resolved to official USD LSE line by ISIN; passive U.S. small-cap equity; daily NAV drawdown/recovery not disclosed |
| DISV | unsupported | Cboe BZX:DISV | not assigned | not applicable | https://www.sec.gov/Archives/edgar/data/0001816125/000181612526000069/c497k.htm | actively managed/no passive index-tracking mandate; no performance artifact created |
| CPLCF | supported | LSE:CUSS | USA | 14.97% (2026-07-29) | https://www.ishares.com/uk/individual/en/products/253480/cuss?siteEntryPassthrough=true&switchLocale=y | OTC alias resolved to official USD LSE line by ISIN; passive U.S. small-cap ESG equity; benchmark changed 2022-06-01; daily NAV drawdown/recovery not disclosed |
| BSVO | unsupported | Nasdaq:BSVO | not assigned | not applicable | https://bridgewayetfs.com/bsvo/ | actively managed small-cap value ETF; no passive index-tracking mandate; no performance artifact created |
| FYX | supported | NASDAQ:FYX | USA | 28.10% (2026-06-30) | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FYX | passive/indexing U.S. small-cap rules-based equity; official 2016-2025 rows; index changed 2026-04-08; daily NAV drawdown/recovery not disclosed |
| IWMI | unsupported | Cboe BZX:IWMI | not assigned | not applicable | https://www.sec.gov/Archives/edgar/data/1848758/000199937126009956/iwmi-497k_050126.htm | actively managed and written-call options ETF; not a passive index-tracking equity ETF; no performance artifact created |
| VB | supported | NYSE Arca:VB | USA | 19.48% (2026-08-07) | https://investor.vanguard.com/investment-products/etfs/profile/vb | passive/index-tracking U.S. small-cap equity; official 2016-2025 rows and rolling 10-year field; daily NAV drawdown/recovery not disclosed |
| SCHA | supported | NYSE Arca:SCHA | USA | 18.27% (2026-07-31) | https://www.schwabassetmanagement.com/products/scha | passive/index-tracking U.S. small-cap equity; official current/rolling fields, secondary annual proxy; daily NAV drawdown/recovery not disclosed |
| SPSM | supported | NYSE Arca:SPSM | USA | 21.54% (2026-07-31) | https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-600-small-cap-etf-spsm | passive/index-tracking U.S. small-cap equity; issuer calendar rows and raw 10-year endpoints not disclosed; benchmark continuity is disclosed |
| IWN | supported | NYSE Arca:IWN | USA | 25.91% (2026-08-13) | https://www.ishares.com/us/products/239712/ishares-russell-2000-value-etf | passive/index-tracking U.S. small-cap value equity; official 2016-2025 rows at 0.1% precision; daily NAV drawdown/recovery not disclosed |
| IWO | supported | NYSE Arca:IWO | USA | 21.61% (2026-08-13) | https://www.ishares.com/us/products/239709/ishares-russell-2000-growth-etf | passive/index-tracking U.S. small-cap growth equity; official 2016-2025 rows at 0.1% precision; daily NAV drawdown/recovery not disclosed |
| AVUV | unsupported | NYSE Arca:AVUV | not assigned | not applicable | https://www.sec.gov/Archives/edgar/data/1710607/000171060725000416/acetftavuv497k.htm | actively managed and does not seek to replicate a specified index; outside passive index-tracking equity scope; no performance artifact created |
| DFAS | unsupported | NYSE Arca:DFAS | not assigned | not applicable | https://www.sec.gov/Archives/edgar/data/1816125/000181612526000081/c497k.htm | actively managed and does not seek to replicate a specific index; outside passive index-tracking equity scope; no performance artifact created |
| AVDV | unsupported | NYSE Arca:AVDV | not assigned | not applicable | https://www.sec.gov/Archives/edgar/data/1710607/000171060725000402/acetftavdv497k.htm | actively managed and does not seek to replicate a specified index; outside passive index-tracking equity scope; no performance artifact created |
| SCZ | supported | NASDAQ:SCZ | International | 13.83% (2026-08-13) | https://www.ishares.com/us/products/239627/ | passive/index-tracking developed ex-U.S./Canada small-cap equity; official 2016-2025 rows; daily NAV drawdown/recovery not disclosed |
| BBSC | supported | Cboe BZX:BBSC | USA | 23.96% (2026-06-30) | https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBSC.PDF | passive/index-tracking U.S. small-cap equity; history under 10 years; exchange transfer from NYSE Arca to Cboe BZX resolved; daily NAV drawdown/recovery not disclosed |
| ISCF | supported | NYSE Arca:ISCF | International | 12.52% (2026-08-13) | https://www.ishares.com/us/products/272823/ishares-international-small-cap-equity-factor-etf | passive/index-tracking international small-cap factor equity; benchmark changed from MSCI World ex USA Small Cap Diversified Multiple-Factor Index to STOXX International Small-Cap Equity Factor Index on 2023-03-01; daily NAV drawdown/recovery not disclosed |
| GWX | supported | NYSE Arca:GWX | International | 8.18% (2026-06-30) | https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-international-small-cap-etf-gwx | passive/index-tracking international small-cap equity; official calendar rows and daily NAV drawdown/recovery not disclosed; reviewed secondary annual table conflicts with official 2025 NAV result and is not saved |
| ISCV | supported | NYSE Arca:ISCV | USA | 20.34% (2026-08-13) | https://www.ishares.com/us/products/239588/ishares-morningstar-smallcap-value-etf | passive/index-tracking U.S. small-cap value equity; official 2016-2025 NAV rows displayed to one decimal; daily NAV drawdown/recovery not disclosed |
| EES | supported | NYSE Arca:EES | USA | 19.57% (2026-07-31) | https://www.wisdomtree.com/us/products/equity/ees | passive/index-tracking U.S. small-cap earnings-weighted equity; official 2016-2025 annual rows; annual-return volatility and daily NAV drawdown/recovery gaps disclosed |
| FESM | supported | NYSE Arca:FESM | USA | 28.42% (2026-06-30) | https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F9911747.PDF | active systematic U.S. small-cap equity; official 2016-2025 rows include predecessor history; daily NAV drawdown/recovery not disclosed |
| DFSV | supported | NYSE Arca:DFSV | USA | 18.7% (2026-06-30, secondary) | https://www.sec.gov/Archives/edgar/data/1816125/000174177325001189/c497k.htm | active systematic U.S. small-cap value equity; official 2023-2025 rows and secondary current fields; history under 10 years and daily NAV drawdown/recovery not disclosed |
| PSC | supported | NASDAQ:PSC | USA | 18.52% (2026-07-31) | https://www.principalam.com/us/fund/psc | active rules-based U.S. small-cap quality/momentum/value equity; official 2017-2025 rows; strategy changed from passive to active 2022-07-08; daily NAV drawdown/recovery not disclosed |
| JPSE | supported | NYSE Arca:JPSE | USA | 20.41% (2026-06-30) | https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-JPSE.PDF | passive/index-tracking U.S. small-cap multi-factor equity; official 2017-2025 annual rows; history under 10 years, annual-return volatility and daily NAV drawdown/recovery gaps disclosed |
| XSVM | supported | NYSE Arca:XSVM | USA | 23.00% (2026-06-30, secondary NAV) | https://www.invesco.com/us/en/financial-products/etfs/invesco-sp-smallcap-value-with-momentum-etf.html | passive/index-tracking U.S. small-cap value/momentum equity; official 2016-2025 annual rows; latest YTD is secondary Schwab NAV and official issuer snapshot is older; daily NAV drawdown/recovery not disclosed |

## GSSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:GSSC | https://am.gs.com/public-assets/documents/574deb07-24d6-11ef-870d-c7a1cb19e681 | Official Goldman Sachs product/fact card: fund identity, exchange, inception, expense ratio, NAV return definition, annual NAV rows, current NAV/YTD | Annual rows 2018-2025 and performance fields as of 2026-06-30 |
| NYSE Arca:GSSC | https://www.sec.gov/Archives/edgar/data/1479026/000119312525334837/d72082d497k.htm | SEC summary prospectus: passive objective, issuer benchmark, inception, NAV return definition, and risk quarters | Filed 2025-12-29; performance period through 2024-12-31; best/worst quarter disclosures |
| NYSE Arca:GSSC | https://www.sec.gov/Archives/edgar/data/1479026/000119312526206736/d120512dncsrs.htm | SEC semi-annual report: current fund classification and expense observation | Period ended 2026-02-28; annualized fund cost 0.20% |
| NYSE Arca:GSSC | https://www.etfcentral.com/fund/GSSC | Secondary current price/NAV and YTD context | Snapshot updated 2026-07-27; return basis not used for NAV TR ranking |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused for eligible 2018-2019 rows |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused for 2018-2022 rows |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused for 2022-2025 rows |

## GSSC raw observations and calculations

| Year | GSSC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -8.72% | -4.38% |
| 2019 | 23.43% | 31.49% |
| 2020 | 15.80% | 18.40% |
| 2021 | 24.05% | 28.71% |
| 2022 | -16.87% | -18.11% |
| 2023 | 17.37% | 26.29% |
| 2024 | 10.94% | 25.02% |
| 2025 | 10.71% | 17.88% |
| 2026 YTD | 21.33% | not available from cached current-year benchmark |

- Metric basis: official GSSC NAV Total Return in USD; distributions are reinvested and fund expenses are reflected in NAV.
- Issuer benchmark: Goldman Sachs ActiveBeta U.S. Small Cap Equity Index; retained as metadata and not substituted for the common S&P 500 reference.
- 2018-2025 GSSC compound: `93.95%` cumulative; rounded-input CAGR `8.63%`.
- 2021-2025 GSSC compound: `48.66%` cumulative; rounded-input CAGR `8.25%`.
- S&P 500 cached 2018-2025 compound: `192.03%` cumulative; rounded-input CAGR `14.33%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official fact card also reports 5-year annualized NAV TR `8.46%` and since-inception annualized NAV TR `10.86%` as of 2026-06-30; these are not relabelled as a 10-year CAGR.
- Official prospectus risk observations: best quarter `+29.24%` in 4Q2020; worst quarter `-30.94%` in 1Q2020.

## GSSC gaps and conflicts

- Inception is 2017-06-28, so the 2017 partial year is excluded from complete-year ranking and the official history is under 10 years as of 2026-06-30.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- The latest official NAV TR YTD field located is 21.33% as of 2026-06-30. A later secondary snapshot reports a different YTD figure with an unclear return basis, so it is not mixed into the NAV table.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## VBR official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:VBR` | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F0937.pdf | Official Vanguard factsheet: passive/full-replication structure, benchmark, expense ratio, exchange, inception, annualized NAV TR, current YTD, and standard deviation | Factsheet as of 2026-06-30; annual rows through 2025-12-31 |
| `NYSE Arca:VBR` | https://investor.vanguard.com/investment-products/etfs/profile/vbr | Official Vanguard performance/quote page: annual NAV TR rows and price/NAV inputs | Annual rows as of 2025-12-31; quote as of 2026-06-18 |
| `NYSE Arca:VBR` | https://advisors.vanguard.com/content/dam/fas/pdfs/MRSTR.pdf | Official Vanguard ticker/CUSIP name-change list | New name effective 2026-07-29; ticker VBR and CUSIP 922908611 |
| `NYSE Arca:VBR` | https://corporate.vanguard.com/content/corporatesite/us/en/corp/who-we-are/pressroom/press-release-vanguard-to-update-names-of-us-equity-index-funds-tracking-morningstar-indexes-042926.html | Official Vanguard rebrand release: effective date and unchanged objective/management | Published 2026-04-29; changes effective 2026-07-29 |
| `NYSE Arca:VBR` | https://www.sec.gov/Archives/edgar/data/36405/000003640526000204/f44857d1.htm | SEC summary prospectus: passive objective, full replication, benchmark context, and fee schedule | Filed 2026-04-28 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## VBR raw observations and calculations

| Year | VBR NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 24.80% | 11.96% |
| 2017 | 11.79% | 21.83% |
| 2018 | -12.22% | -4.38% |
| 2019 | 22.76% | 31.49% |
| 2020 | 5.82% | 18.40% |
| 2021 | 28.07% | 28.71% |
| 2022 | -9.29% | -18.11% |
| 2023 | 16.00% | 26.29% |
| 2024 | 12.39% | 25.02% |
| 2025 | 9.09% | 17.88% |
| 2026 YTD | 15.83% NAV / 15.92% market price | not available from cached current-year benchmark |

- Canonical identity: `NYSE Arca:VBR`; current fund name `Vanguard Morningstar Small-Cap Value ETF`; passive, full-replication U.S. small-cap value equity ETF; inception `2004-01-26`; USD.
- Current issuer benchmark: `Morningstar US Small Cap Value Index`, formerly `CRSP US Small Cap Value Index`; Bloomberg ticker `CRSPSCVT`. The rebrand is effective 2026-07-29 and Vanguard states it does not change the investment objective or management.
- Metric basis: official Vanguard NAV Total Return is pre-tax, net of expenses, with dividends and capital-gains distributions reinvested. The S&P 500 comparison is the cached USD Total Return convention with dividends reinvested.
- Official period-ended-2026-06-30 fields: NAV YTD `15.83%`, market-price YTD `15.92%`, issuer benchmark YTD `15.86%`, 1-year `27.01%`, 3-year annualized `16.08%`, 5-year annualized `9.23%`, 10-year annualized `10.99%`, since-inception annualized `9.51%`, and three-year standard deviation `16.43%`.
- Latest captured quote: market price `US$238.40`, NAV `US$238.46`, quote date 2026-06-18; price/NAV discount `= 238.40 / 238.46 - 1 = -0.025%`, displayed as `-0.03%`.
- Using published rounded annual NAV returns, VBR 2016-2025 cumulative `162.85%`, CAGR `10.15%`, and 2021-2025 cumulative `65.22%`, CAGR `10.56%`; up/down count `8 / 2`, best `2021 +28.07%`, worst `2018 -12.22%`.
- S&P 500 cached 2016-2025 cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative `96.17%`, CAGR `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## VBR gaps, reconciliation, and scheduled-local gate

- The official English 2026-06-30 factsheet and historical Vanguard page retain the former CRSP wording for the reviewed performance rows; the official 2026 name-change list and release establish the current Morningstar name/index and effective date. The durable page preserves both labels and does not infer a strategy change.
- The issuer 10-year annualized field `10.99%` is retained as an official average annual return for the period ended 2026-06-30. Raw TR endpoints and exact elapsed years were not disclosed, so no endpoint-derived cumulative value is asserted.
- No newer official price/NAV quote than 2026-06-18 was verified; current YTD performance is available through 2026-06-30. Dates remain separate in the performance page.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric drawdown proxy is saved.
- Complete pre-save checklist: canonical ticker/exchange, current and former fund/index names, passive-equity type, return basis, distributions, annual rows, cached S&P 500 window, 10-year field and gap, as-of dates, calculations, source URLs, candidate page/source-batch contents, USA navigation link, canonical tag, and single log bullet were reviewed locally. No critical/high finding remained.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS


## VTWO official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:VTWO` | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3351.pdf | Official Vanguard factsheet: passive/full-replication structure, Russell 2000 benchmark, expense ratio, exchange, inception, annualized NAV TR, current YTD, assets, and standard deviation | Factsheet as of 2026-06-30; annualized fields through 2026-06-30 |
| `NASDAQ:VTWO` | https://investor.vanguard.com/investment-products/etfs/profile/vtwo | Official Vanguard performance/quote page: complete annual NAV TR rows and price/NAV inputs | Annual rows as of 2025-12-31; quote as of 2026-06-22 |
| `NASDAQ:VTWO` | https://fund-docs.vanguard.com/FA3351_SPM.pdf | Official Vanguard factsheet mirror used to reconcile fund identity, exchange, return basis, and risk fields | Same 2026-06-30 data as the English factsheet |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## VTWO raw observations and calculations

| Year | VTWO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 21.33% | 11.96% |
| 2017 | 14.70% | 21.83% |
| 2018 | -10.98% | -4.38% |
| 2019 | 25.61% | 31.49% |
| 2020 | 20.10% | 18.40% |
| 2021 | 14.81% | 28.71% |
| 2022 | -20.40% | -18.11% |
| 2023 | 17.00% | 26.29% |
| 2024 | 11.57% | 25.02% |
| 2025 | 12.88% | 17.88% |
| 2026 YTD | 22.60% NAV TR | not available from cached current-year benchmark |

- Canonical identity: `NASDAQ:VTWO`; Vanguard Russell 2000 ETF; passive, full-replication U.S. small-cap broad equity ETF; inception `2010-09-20`; USD; issuer benchmark `Russell 2000 Index`.
- Metric basis: official Vanguard NAV Total Return is pre-tax, net of expenses, with dividends and capital-gains distributions reinvested. The S&P 500 comparison is the cached USD Total Return convention with dividends reinvested.
- Official period-ended-2026-06-30 fields: NAV YTD `22.60%`, market-price YTD `22.63%`, issuer benchmark YTD `22.57%`, 1-year `40.87%`, 3-year annualized `18.65%`, 5-year annualized `7.03%`, 10-year annualized `11.68%`, since-inception annualized `11.55%`, and three-year standard deviation `19.99%`.
- Latest captured quote: market price `US$120.46`, NAV `US$120.52`, quote date 2026-06-22; price/NAV discount `= 120.46 / 120.52 - 1 = -0.050%`, displayed as `-0.05%`.
- Using published rounded annual NAV returns, VTWO 2016-2025 cumulative `151.67%`, CAGR `9.67%`, and 2021-2025 cumulative `34.66%`, CAGR `6.13%`; up/down count `8 / 2`, best `2019 +25.61%`, worst `2022 -20.40%`.
- S&P 500 cached 2016-2025 cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative `96.17%`, CAGR `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## VTWO gaps, reconciliation, and scheduled-local gate

- The Vanguard profile's complete annual table as of 2025-12-31 is used for the 2016-2025 calendar window. A later quarterly capture can show revised-looking historical rows; those observations are not mixed into this complete-calendar table.
- Separate Vanguard advisor/fund-list captures returned different YTD or inception metadata in the reviewed HTML context, including an inconsistent inception display and YTD values that did not match the direct 2026-06-30 factsheet. The direct factsheet and product-profile identity (`2010-09-20`) are retained; the conflicting captures are not used as performance inputs.
- The issuer 10-year annualized field `11.68%` is retained as an official average annual return for the period ended 2026-06-30. Raw TR endpoints and exact elapsed years were not disclosed, so no endpoint-derived cumulative value is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric drawdown proxy is saved. Quarterly distributions are disclosed, but the reviewed sources do not provide a complete distribution schedule in the performance table.
- Complete pre-save checklist: canonical ticker/exchange, fund/index identity, passive-equity type, return basis, distributions, annual rows, cached S&P 500 window, 10-year field and gap, current YTD, quote inputs, as-of dates, calculations, source URLs, candidate page/source-batch contents, USA navigation link, canonical tag, and single log bullet were reviewed locally. No critical/high finding remained.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## VSS official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:VSS` | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3184.pdf | Official Vanguard factsheet: passive/index-sampling structure, FTSE benchmark, expense ratio, exchange, inception, annualized NAV TR, current factsheet YTD, distributions, holdings, and standard deviation | Factsheet as of 2026-06-30; current factsheet YTD `8.18%`, rolling 10-year `8.26%`, standard deviation `14.43%` vs benchmark `15.27%` |
| `NYSE Arca:VSS` | https://advisors.vanguard.com/investments/products/vss/vanguard-ftse-all-world-ex-us-small-cap-etf | Official Vanguard product/quote page: complete annual NAV TR rows, rolling 10-year field, and later price/NAV/YTD capture | Annual rows as of 2025-12-31; rolling 10-year `7.42%` as of 2026-07-31; quote and current YTD as of 2026-08-11 |
| `NYSE Arca:VSS` | https://investor.vanguard.com/investment-products/etfs/profile/vss | Official Vanguard product-page identity and performance-page cross-check | Accessed 2026-08-17; dynamic page did not expose stable line-level data in the web capture |
| `NYSE Arca:VSS` | https://fund-docs.vanguard.com/p3184.pdf | Official Vanguard prospectus: legal fund identity, benchmark, and strategy context | Reviewed with the prior source batch; fee effective 2026-02-27 |
| VSS drawdown context | https://totalrealreturns.com/n/VSS | Secondary price total-return history | Data ending 2026-08-10; drawdown proxy only, not NAV Total Return |

## VSS raw observations and calculations

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
| 2026 current | 10.86% NAV / 11.40% market price | not available from cached current-year benchmark |

- Canonical identity: `NYSE Arca:VSS`; Vanguard FTSE All-World ex-US Small-Cap ETF; passive/index-tracking equity ETF using index sampling; inception `2009-04-02`; USD; issuer benchmark `FTSE Global Small Cap ex US Index` (`TGPVA09U`).
- Metric basis: official Vanguard NAV Total Return is pre-tax, net of expenses, with dividends and capital-gains distributions reinvested. The S&P 500 comparison is the cached USD Total Return convention with dividends reinvested.
- Latest product-page capture: market price `US$158.81`, NAV `US$158.05`, price/NAV premium `0.48%`, NAV YTD `10.86%`, and market-price YTD `11.40%`, all as of 2026-08-11.
- Official factsheet cross-check as of 2026-06-30: NAV YTD `8.18%`, market-price YTD `8.23%`, issuer benchmark YTD `7.53%`, 1-year `18.74%`, 3-year annualized `15.50%`, 5-year annualized `5.71%`, 10-year annualized `8.26%`, since-inception annualized `9.51%`, and standard deviation `14.43%` versus benchmark `15.27%`.
- Using published rounded annual NAV returns, VSS 2016-2025 cumulative `106.58%`, CAGR `7.53%`, and 2021-2025 cumulative `36.70%`, CAGR `6.45%`; up/down count `8 / 2`, best `2017 +30.26%`, worst `2022 -21.22%`.
- S&P 500 cached 2016-2025 cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative `96.17%`, CAGR `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## VSS gaps, reconciliation, and scheduled-local gate

- The latest product-page capture through 2026-08-11 is used for current YTD and quote fields. The 2026-06-30 factsheet is retained for the standardized current facts and risk cross-check; the two as-of windows are not mixed.
- The issuer rolling 10-year NAV TR field is `7.42%` as of 2026-07-31, while the factsheet's earlier 2026-06-30 field is `8.26%`; both are official issuer fields for different month-end windows and raw TR endpoints are not disclosed.
- Official complete-calendar-year NAV rows are available for 2016-2025. Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; the secondary `-43.51%` price total-return drawdown ending 2020-03-23 and current `-2.11%` price drawdown ending 2026-08-10 remain clearly marked as non-NAV context.
- Complete pre-save checklist: canonical ticker/exchange, international primary region, passive-equity type, return basis, distributions, annual rows, cached S&P 500 window, current/rolling fields, standard-deviation fields, quote inputs, separate as-of dates, calculations, source URLs, candidate page/source-batch contents, International navigation link, canonical tags, and single log bullet were reviewed locally. No critical/high finding remained.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## IJR official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:IJR` | https://www.ishares.com/us/products/239774/ishares-core-sp-smallcap-etf?fundSearch=true&qt=IJR | Official iShares product page: identity, exchange, benchmark, inception, expense ratio, current NAV/price, premium/discount, current YTD, rolling annualized return, standard deviation, and calendar rows | Current NAV/price as of 2026-08-14; NAV YTD as of 2026-08-13; rolling 10-year field as of 2026-06-30; standard deviation as of 2026-07-31; annual rows through 2025-12-31 |
| `NYSE Arca:IJR` | https://www.ishares.com/us/literature/fact-sheet/ijr-ishares-core-s-p-small-cap-etf-fund-fact-sheet-en-us.pdf | Official iShares factsheet: passive/index-tracking objective, S&P SmallCap 600 benchmark, calendar rows, fee, exchange, distributions, and risk fields | Factsheet as of 2026-06-30; standard deviation `19.42%` and annual rows 2021-2025 |
| `NYSE Arca:IJR` | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-core-s-and-p-small-cap-etf-3-31.pdf | Official iShares summary prospectus: fund identity, strategy, benchmark, and fee context | Current prospectus source reviewed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| IJR drawdown context | https://totalrealreturns.com/s/IJR | Secondary price total-return history | Drawdown context only; not authoritative NAV maximum drawdown/recovery |

## IJR raw observations and calculations

| Year | IJR NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 26.49% | 11.96% |
| 2017 | 13.20% | 21.83% |
| 2018 | -8.43% | -4.38% |
| 2019 | 22.79% | 31.49% |
| 2020 | 11.24% | 18.40% |
| 2021 | 26.69% | 28.71% |
| 2022 | -16.20% | -18.11% |
| 2023 | 16.03% | 26.29% |
| 2024 | 8.61% | 25.02% |
| 2025 | 5.95% | 17.88% |
| 2026 current | 25.09% NAV TR | not available from cached current-year benchmark |

- Canonical identity: `NYSE Arca:IJR`; iShares Core S&P Small-Cap ETF; passive/index-tracking U.S. small-cap equity ETF; inception `2000-05-22`; USD; issuer benchmark `S&P SmallCap 600 Index` (`SPTRSMCP`).
- Metric basis: official iShares NAV Total Return includes reinvested dividends/distributions after fund expenses. The S&P 500 comparison is the cached USD Total Return convention with dividends reinvested.
- Latest official product-page fields: NAV `US$150.41`, closing price `US$150.44`, premium/discount `0.02%`, all as of 2026-08-14; NAV Total Return YTD `25.09%` as of 2026-08-13; three-year standard deviation `19.36%` as of 2026-07-31; quarterly distributions.
- Official issuer 10-year NAV Total Return annualized field is `11.47%` as of 2026-06-30. This is retained separately from the rounded-input 2016-2025 calendar CAGR `9.76%`; raw endpoints are not used to derive a second cumulative value.
- Using published rounded annual NAV returns, IJR 2016-2025 cumulative `153.87%`, CAGR `9.76%`, and 2021-2025 cumulative `41.75%`, CAGR `7.23%`; up/down count `8 / 2`, best `2021 +26.69%`, worst `2022 -16.20%`.
- S&P 500 cached 2016-2025 cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative `96.17%`, CAGR `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## IJR gaps, reconciliation, and scheduled-local gate

- The direct iShares product page supplies current NAV/price/YTD fields through 2026-08-14/13, while annualized 10-year and standard-deviation fields have separate June/July month-end as-of dates; these dates remain explicit and are not combined.
- The factsheet's 2026-06-30 standard deviation is `19.42%`; the later product-page field is `19.36%` as of 2026-07-31 and is used for the current page risk snapshot.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified. Secondary price-total-return sources report materially different methodology outputs, so they remain context only and no authoritative NAV recovery date is asserted.
- Complete pre-save checklist: canonical ticker/exchange, passive-equity type, return basis, benchmark identity, annual rows, cached S&P 500 window, issuer 10-year field and calendar CAGR separation, current YTD/quote fields, standard deviation, distributions, units/currencies, as-of dates, calculations, source URLs, candidate page/source-batch contents, USA navigation link, canonical tag, and single log bullet were reviewed locally. No critical/high finding remained.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## IWM official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:IWM` | https://www.ishares.com/us/products/239710/ishares-russell-2000-etf | Official iShares U.S. product page: identity, exchange, Russell 2000 benchmark, inception, fee, current NAV/price, premium/discount, current YTD, rolling annualized return, standard deviation, and 2021-2025 calendar rows | Current NAV/price as of 2026-08-14; NAV YTD as of 2026-08-13; rolling 10-year field as of 2026-06-30; standard deviation as of 2026-07-31 |
| `NYSE Arca:IWM` | https://www.ishares.com/us/literature/fact-sheet/iwm-ishares-russell-2000-etf-fund-fact-sheet-en-us.pdf | Official iShares factsheet: passive/index-tracking objective, benchmark, fee, exchange, distribution frequency, 2021-2025 calendar rows, and risk fields | Factsheet as of 2026-06-30; standard deviation `19.98%`; annual rows 2021-2025 |
| `NYSE Arca:IWM` | https://www.ishares.com/uk/professionals/en/products/239710/ishares-russell-2000-etf?siteEntryPassthrough=true&switchLocale=y | Official BlackRock/iShares professional page used for the complete 2016-2025 calendar table | 2016-2020 rows are published at 0.1% precision; table capture accessed 2026-08-17 |
| `NYSE Arca:IWM` | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-russell-2000-etf-3-31.pdf | Official iShares summary prospectus: fund objective, passive index exposure, benchmark, and fee context | Current prospectus source reviewed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| IWM drawdown context | https://totalrealreturns.com/n/IWM | Secondary price total-return history | Context only; not authoritative NAV maximum drawdown/recovery |

## IWM raw observations and calculations

| Year | IWM NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 21.4% | 11.96% |
| 2017 | 14.7% | 21.83% |
| 2018 | -11.0% | -4.38% |
| 2019 | 25.4% | 31.49% |
| 2020 | 19.9% | 18.40% |
| 2021 | 14.6% | 28.71% |
| 2022 | -20.5% | -18.11% |
| 2023 | 16.8% | 26.29% |
| 2024 | 11.4% | 25.02% |
| 2025 | 12.7% | 17.88% |
| 2026 current | 23.73% NAV TR | not available from cached current-year benchmark |

- Canonical identity: `NYSE Arca:IWM`; iShares Russell 2000 ETF; passive/index-tracking U.S. small-cap equity ETF; inception `2000-05-22`; USD; issuer benchmark `Russell 2000 Index` (`RU20INTR`).
- Metric basis: official iShares NAV Total Return includes reinvested dividends/distributions after fund expenses. The S&P 500 comparison is the cached USD Total Return convention with dividends reinvested.
- Latest official product-page fields: NAV `US$304.98`, closing price `US$305.09`, premium/discount `0.04%`, all as of 2026-08-14; NAV Total Return YTD `23.73%` as of 2026-08-13; three-year standard deviation `19.97%` as of 2026-07-31; quarterly distributions.
- Official issuer 10-year NAV Total Return annualized field is `11.53%` as of 2026-06-30. This is retained separately from the rounded-input 2016-2025 calendar CAGR `9.55%`; raw endpoints are not used to derive a second cumulative value.
- The official BlackRock/iShares professional page publishes the complete 2016-2025 rows at 0.1% precision. Using those consistent rounded inputs, IWM 2016-2025 cumulative `148.94%`, CAGR `9.55%`, and 2021-2025 cumulative `33.60%`, CAGR `5.96%`; up/down count `8 / 2`, best `2019 +25.4%`, worst `2022 -20.5%`.
- The current U.S. factsheet gives a higher-precision 2021-2025 cross-check (`14.62%`, `-20.48%`, `16.80%`, `11.35%`, `12.69%`); those rows are not mixed into the complete 0.1%-precision calculation.
- S&P 500 cached 2016-2025 cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative `96.17%`, CAGR `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## IWM gaps, reconciliation, and scheduled-local gate

- The direct U.S. iShares page supplies current NAV/price/YTD fields through 2026-08-14/13, while the issuer 10-year field is as of 2026-06-30 and standard deviation is as of 2026-07-31; dates remain explicit.
- The complete official 2016-2025 table used for calculation is available at 0.1% precision in the professional iShares capture. The U.S. factsheet's exact 2021-2025 rows are retained as a reconciliation note, not silently substituted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; secondary price-total-return history remains context only and no authoritative NAV recovery date is asserted.
- Complete pre-save checklist: canonical ticker/exchange, passive-equity type, return basis, benchmark identity, annual rows and precision, cached S&P 500 window, issuer 10-year field and calendar CAGR separation, current YTD/quote fields, standard deviation, distributions, units/currencies, as-of dates, calculations, source URLs, candidate page/source-batch contents, USA navigation link, canonical tag, and single log bullet were reviewed locally. No critical/high finding remained.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## VB official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:VB | https://investor.vanguard.com/investment-products/etfs/profile/vb | Official Vanguard product page: identity, annual NAV/market-price returns, rolling return, current NAV/price, historical-price observations, and current-period fields | Latest numeric product-page capture retained through 2026-08-07; direct scheduled recheck on 2026-08-17 found no newer machine-readable current return field |
| NYSE Arca:VB | https://fund-docs.vanguard.com/F0969.pdf | Official Vanguard factsheet: passive/full-replication approach, benchmark, expense ratio, NAV return definition, current YTD, rolling returns, standard deviation, holdings and fund facts | Factsheet as of 2026-06-30 |
| NYSE Arca:VB | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/investment-profiles/0969.pdf | Official Vanguard investment profile: complete annual and quarterly NAV return rows, recent distributions, risk measures and fund facts | Profile as of 2026-06-30; annual rows through 2025-12-31 |
| NYSE Arca:VB | https://www.sec.gov/Archives/edgar/data/36405/000003640526000206/f44854d1.htm | SEC summary prospectus: structure, passive index exposure and expense-ratio evidence | Prospectus dated 2026-04-28 |
| NYSE Arca:VB | https://advisors.vanguard.com/content/dam/fas/pdfs/MRSTR.pdf | Official Vanguard name-change list | Morningstar fund/benchmark names effective 2026-07-29; VB CUSIP 922908751 |
| NYSE Arca:VB | https://www.vanguardmexico.com/es/inicio/noticias/name-changes-for-vanguard-equity-index-funds-and-crsp-morningstar-benchmarks | Official Vanguard transition notice | Name-only CRSP → Morningstar transition; objectives, strategy, index construction, ticker, CUSIP and expense ratios unchanged |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/; https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached project reference for complete calendar years | 2016-2025 USD total return, dividends reinvested, as of 2025-12-31 |

## VB raw observations and calculations

| Year | VB NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 18.31% | 11.96% |
| 2017 | 16.24% | 21.83% |
| 2018 | -9.30% | -4.38% |
| 2019 | 27.37% | 31.49% |
| 2020 | 19.08% | 18.40% |
| 2021 | 17.72% | 28.71% |
| 2022 | -17.60% | -18.11% |
| 2023 | 18.21% | 26.29% |
| 2024 | 14.23% | 25.02% |
| 2025 | 8.83% | 17.88% |
| 2026 YTD | 19.48% (official NAV) | 13.58% (official S&P 500 TR, as of 2026-08-05; not synchronized) |

- Metric basis: official VB NAV Total Return in USD, with dividends and capital-gains distributions reinvested and fund expenses reflected in NAV.
- Issuer benchmark: Morningstar US Small Cap Index, formerly CRSP US Small Cap Index; the 2026-07-29 change is a name transition and is not treated as a methodology change.
- VB 2016-2025 compound: `169.68%` cumulative; rounded-input CAGR `10.43%`.
- VB 2021-2025 compound: `42.55%` cumulative; rounded-input CAGR `7.35%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official rolling 10-year NAV TR: `10.90%` annualized as of 2026-07-31; raw rolling endpoints are not disclosed and this field is not relabelled as the 2016-2025 calendar CAGR.
- Official 36-month monthly standard deviation: `17.26%` as of 2026-06-30.
- Quarter-end NAV-TR drawdown calculation: high-water index `1.58849` at 2019-12-31 to trough `1.11067` at 2020-03-31 equals `-30.08%`; recovery index `1.89154` at 2020-12-31 confirms the prior peak was recovered. This is not a daily maximum-drawdown series.
- Official recent distributions visible in the investment profile: ex-dividend 2026-06-26 `US$0.89` and 2026-03-27 `US$0.98`; payment dates are not disclosed in the reviewed capture.

## VB gaps, conflicts, and scheduled-inline local review

- The current product-page return snapshot is as of 2026-08-07 while factsheet/risk fields are as of 2026-06-30 and rolling 10-year return is as of 2026-07-31; these are kept separate.
- The 2026-07-29 CRSP → Morningstar change is a name/benchmark-label transition; Vanguard states that objectives, strategies, index construction, rebalancing, securities, ticker, CUSIP and expense ratios are unchanged.
- Official daily NAV history sufficient for a daily maximum drawdown and recovery calculation was not verified; the quarter-end calculation and monthly NAV-price-only proxy remain clearly labelled and are not substituted for daily NAV TR.
- Local pre-save result: `PASS`. Confirmed canonical identity `NYSE Arca:VB`, passive/full-replication classification, current fund/benchmark naming, official 2016-2025 annual rows, current YTD, rolling 10-year field, S&P cache basis/window, calculations, distribution observations, USA region ownership, breadcrumb links, and disclosed gaps.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## SCHA official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:SCHA | https://www.schwabassetmanagement.com/products/scha | Official Schwab Asset Management product page: objective, index, passive style, expense ratio, current NAV/AUM/holdings, current returns, risk fields and distributions | Current quote/NAV through 2026-08-14; performance and risk fields through 2026-07-31; holdings through 2026-08-13 |
| NYSE Arca:SCHA | https://www.schwabassetmanagement.com/products/scha/documents | Official documents hub for the SCHA factsheet, ETF performance summary, monthly fund report and distribution schedule | Factsheet last updated 2026-06-30; ETF performance summary and monthly report last updated 2026-07-31 |
| NYSE Arca:SCHA | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=scha | Official Schwab ETF research capture: current NAV YTD, rolling performance, current quote and best/worst three-month observations | Performance through 2026-07-31; close/price through 2026-08-14 |
| NYSE Arca:SCHA | https://www.sec.gov/Archives/edgar/data/1454889/000110465925123320/tm2526338-13_497k.htm | SEC summary prospectus: objective, index construction, 90% policy, passive indexing strategy and risks | Prospectus dated 2025-12-22; current product page supersedes its older 0.04% expense ratio with 0.03% effective 2026-06-11 |
| NYSE Arca:SCHA annual proxy rows | https://www.etfreplay.com/etf/scha | Secondary dividend-reinvested annual total-return history; used only as a labelled proxy because the issuer annual table did not render in the reviewed capture | 2016-2025 annual rows; secondary proxy, not official issuer NAV rows |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/; https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached project reference for complete calendar years | 2016-2025 USD total return, dividends reinvested, as of 2025-12-31 |

## SCHA raw observations and calculations

| Year | SCHA total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | 19.97%* | 11.96% |
| 2017 | 14.93%* | 21.83% |
| 2018 | -11.77%* | -4.38% |
| 2019 | 26.50%* | 31.49% |
| 2020 | 19.34%* | 18.40% |
| 2021 | 16.45%* | 28.71% |
| 2022 | -19.81%* | -18.11% |
| 2023 | 18.46%* | 26.29% |
| 2024 | 11.16%* | 25.02% |
| 2025 | 11.60%* | 17.88% |
| 2026 YTD | 18.27% (official NAV) | not available from cached current-year benchmark |

- Metric basis: official SCHA NAV Total Return for current-period fields; annual rows are secondary dividend-reinvested proxy observations and are not relabelled as official issuer NAV rows.
- Issuer benchmark: Dow Jones U.S. Small-Cap Total Stock Market Index; retained as metadata and not substituted for the common S&P 500 reference.
- SCHA 2016-2025 proxy compound: `152.02%` cumulative; rounded-input CAGR `9.68%`.
- SCHA 2021-2025 proxy compound: `37.23%` cumulative; rounded-input CAGR `6.53%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official rolling 10-year NAV TR field: `10.48%` annualized as of 2026-07-31; raw rolling endpoints are not disclosed.
- Official risk fields as of 2026-07-31: beta `1.00` and standard deviation `19.78%`; holdings `1,711` as of 2026-08-13; turnover `13.99%` as of 2026-07-31.
- Official 2026 distributions visible: `US$0.1004` ex/pay 2026-06-24/2026-06-29 and `US$0.0384` ex/pay 2026-03-25/2026-03-30.

## SCHA gaps and scheduled-inline local review

- The issuer page supplied current NAV/rolling fields but the reviewed machine-readable issuer capture did not expose the complete 2016-2025 annual NAV table; secondary rows are therefore marked `*` and excluded from claims of official annual coverage.
- Official current fields are split across 2026-07-31 performance/risk, 2026-08-13 holdings, and 2026-08-14 quote snapshots; these dates are kept separate.
- Official daily NAV history sufficient for a numeric maximum drawdown and recovery calculation was not verified; no daily drawdown proxy is saved.
- Local pre-save result: `PASS`. Confirmed canonical identity `NYSE Arca:SCHA`, passive/index-tracking classification, index objective, expense ratio, current NAV/YTD, rolling field, proxy markers, S&P cache basis/window, risk/distribution observations, USA region ownership, graph breadcrumb, and disclosed gaps.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## SPSM official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:SPSM | https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-600-small-cap-etf-spsm | Official State Street product page: passive objective, index, exchange/listing, inception, NAV/AUM, expense ratio, holdings, characteristics, current performance and benchmark continuity | Product page accessed 2026-08-17; fund facts through 2026-08-15; NAV/AUM/characteristics as of 2026-08-13; performance as of 2026-07-31 |
| NYSE Arca:SPSM | https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-spsm.pdf | Official State Street factsheet: fund facts, passive index objective, standardized NAV/market-value/index performance and risk context | Factsheet as of 2026-06-30; accessed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/; https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached project reference for complete calendar years | 2016-2025 USD total return, dividends reinvested, as of 2025-12-31 |

## SPSM raw observations and calculations

| Period | SPSM NAV TR | Linked benchmark series |
|---|---:|---:|
| 1 month to 2026-07-31 | -1.90% | -1.90% |
| QTD to 2026-07-31 | -1.90% | -1.90% |
| 2026 YTD | 21.54% | 21.55% |
| 1 year to 2026-07-31 | 33.62% | 33.64% |
| 3 years annualized to 2026-07-31 | 13.24% | 13.26% |
| 5 years annualized to 2026-07-31 | 7.45% | 7.48% |
| 10 years annualized to 2026-07-31 | 10.75% | 10.79% |
| Since inception annualized to 2026-07-31 | 10.08% | 10.09% |

- Metric basis: official State Street fund NAV total return, net of fees, with dividends and capital gains reinvested. The linked benchmark series is gross of fund fees.
- Current quote/fund facts: NAV `US$58.20`, bid/ask midpoint `US$58.22`, premium/discount `+0.02%`, AUM `US$17,415.46M`, 606 holdings, gross expense ratio `0.03%`, 30-day SEC yield `1.44%`, and quarterly distributions as of 2026-08-13 or the applicable official fund-facts snapshot.
- Tracking differences, calculated as fund NAV minus linked benchmark from the same issuer table, are `-0.01 pp` YTD, `-0.02 pp` for 1 year, `-0.02 pp` for 3 years, `-0.03 pp` for 5 years, and `-0.04 pp` for 10 years.
- The issuer's benchmark history is linked across Russell 2000 from inception through 2017-11-16, SSGA Small Cap Index from 2017-11-16 through 2020-01-24, and S&P SmallCap 600 Index from 2020-01-24 onward.
- Official SPSM calendar-year NAV rows for 2016-2025 and raw rolling 10-year endpoints were not disclosed in the reviewed issuer capture; no annual-row CAGR or up/down-year count is calculated.
- S&P 500 annual rows reuse the cached USD total-return convention and are not mixed with the current SPSM YTD date window.

## SPSM gaps and scheduled-inline local review

- The latest official current-period performance located is through 2026-07-31; the latest official quote, AUM, holdings and characteristics are separate 2026-08-13/15 snapshots and remain separately labelled.
- Official calendar-year NAV rows for 2016-2025 and raw endpoints for the 10-year field remain `ไม่พบข้อมูลที่ยืนยันได้`; the issuer-labeled `10.75%` annualized field is retained as a source fact, not recomputed.
- Official daily NAV history sufficient for a numeric maximum drawdown and recovery calculation was not verified; no drawdown proxy is saved.
- Complete local pre-save checklist: confirmed canonical identity `NYSE Arca:SPSM`, passive/index-tracking classification, S&P SmallCap 600 objective, inception, fee, return basis, benchmark continuity, current/rolling fields, units/currencies, as-of dates, tracking calculations, cached S&P window/basis, graph breadcrumb, USA primary-region ownership, planned page/index/source-batch/log contents, and disclosed gaps.
- Local pre-save result: `PASS`.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## FYX official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NASDAQ:FYX | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FYX | Official First Trust product page: fund identity, Nasdaq listing, objective, index methodology, expense ratio, current NAV/market price, rolling NAV performance, risk fields, and distribution context | Product/current fields through 2026-08-03; performance fields through 2026-06-30 |
| NASDAQ:FYX | https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=b4ab133b-7d16-4b63-81f3-83640709b936 | Official First Trust factsheet: inception, Nasdaq listing, expense ratio, index identity, 2016-2025 calendar NAV total-return rows, 2026 YTD, and 3-year risk statistics | Factsheet as of 2026-06-30 |
| NASDAQ:FYX | https://www.ftportfolios.com/Funds/ETF/Prospectus/FYT | Official prospectus: indexing approach, at-least-90% index exposure, 2016-04-08 index change, annual return chart, and best/worst quarter observations | Prospectus dated 2025-12-01; annual chart through 2024 |
| NASDAQ:FYX | https://www.ftportfolios.com/Retail/Etf/EtfPriceHistory.aspx?Ticker=FYX | Official historical pricing: NAV/market price and net assets | Latest visible quote `2026-08-03` |
| NASDAQ:FYX | https://www.ftportfolios.com/Retail/Etf/EtfDividHistory.aspx?Ticker=FYX | Official cash distribution history | 2026 records visible through 2026-06-30 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/; https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached project reference for complete calendar years | 2016-2025 USD total return, dividends reinvested, as of 2025-12-31 |

## FYX raw observations and calculations

| Year | FYX NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 22.72% | 11.96% |
| 2017 | 14.45% | 21.83% |
| 2018 | -10.26% | -4.38% |
| 2019 | 21.04% | 31.49% |
| 2020 | 19.23% | 18.40% |
| 2021 | 27.48% | 28.71% |
| 2022 | -18.39% | -18.11% |
| 2023 | 18.12% | 26.29% |
| 2024 | 12.20% | 25.02% |
| 2025 | 12.90% | 17.88% |
| 2026 YTD | 28.10% (official NAV TR) | not available from cached current-year benchmark |

- Metric basis: official FYX NAV Total Return in USD; distributions are reinvested and fund expenses are reflected in NAV.
- Issuer benchmark: Nasdaq AlphaDEX Small Cap Core™ Index (`NQDXUSSCT`); retained as metadata and not substituted for the common S&P 500 reference.
- FYX 2016-2025 compound: `183.16%` cumulative; rounded-input CAGR `10.97%`.
- FYX 2021-2025 compound: `55.67%` cumulative; rounded-input CAGR `9.25%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official rolling 10-year NAV TR field: `13.26%` annualized as of 2026-06-30; raw rolling endpoints are not disclosed and the field is not relabelled as the 2016-2025 calendar CAGR.
- Official 3-year risk fields as of 2026-06-30: standard deviation `19.91%`, alpha `4.99`, beta `1.02`, Sharpe ratio `0.87`, correlation `0.99`.
- Official 2026 distributions visible in the reviewed archive: `US$0.4369` ex/pay 2026-06-25/2026-06-30 and `US$0.2029` ex/pay 2026-03-26/2026-03-31.

## FYX gaps and conflicts

- The latest official performance fields located are as of 2026-06-30, while the latest visible official NAV/market-price quote is as of 2026-08-03; these are separate snapshots and are not presented as one same-date observation.
- The underlying index changed from the Defined Small Cap Core Index to the Nasdaq AlphaDEX Small Cap Core™ Index on 2026-04-08. The 2016 full-year fund return remains an official NAV observation, but pre-change performance is not necessarily indicative of the current index methodology.
- Official daily NAV history sufficient for a numeric maximum drawdown and recovery calculation was not verified; no secondary drawdown proxy is saved.
- The reviewed official distribution archive exposed only the two 2026 records above; older distributions are not inferred because they are not needed to calculate NAV Total Return.

## FYX scheduled-inline local review

- Status: `PASS`
- Confirmed canonical identity `NASDAQ:FYX`, Nasdaq listing, passive/indexing classification, inception, expense ratio, issuer benchmark, NAV Total Return definition, official 2016-2025 annual rows, official 2026 YTD, issuer rolling 10-year field, risk statistics, distributions, S&P cache window/basis, best/worst ranking, calculations, source links, USA primary-region ownership, graph breadcrumb, and no unsupported drawdown/recovery inference.
- All material durable values map to official First Trust sources or the cached S&P 500 convention; annual rows and YTD are clearly separated from the current quote snapshot.
- No proxy marker is used because the factsheet provides the complete official 2016-2025 annual row set.
- Local pre-save result: `PASS`.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## BSVO unsupported ETF record

- Input ticker: `BSVO`; canonical identity: `Nasdaq:BSVO`; fund: EA Bridgeway Omni Small-Cap Value ETF; inception `2010-12-31`.
- Type gate: `unsupported ETF type`. Bridgeway’s official fund page labels BSVO `Fund Type: Active`, and the SEC summary prospectus describes a broad small-cap value portfolio managed by an adviser/sub-adviser rather than a passive index-tracking mandate. ETF v1 excludes active ETFs even when the holdings are equity securities.
- No NAV performance page, annual equity-return table, S&P 500 comparison, region row, or ETF Performance Index row was created after the type gate. Current return observations were not used as performance evidence.

### BSVO Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `Nasdaq:BSVO` | https://bridgewayetfs.com/bsvo/ | Official issuer fund page: active classification, ticker, Nasdaq exchange, inception, expense, NAV and current month-end performance context | Page reviewed 2026-08-17; current facts shown as of 2026-07-29 / month-end performance through 2026-06-30 |
| `Nasdaq:BSVO` | https://www.sec.gov/Archives/edgar/data/1592900/000159290024002170/eabridgewayomnismall-capva.htm | SEC summary prospectus: fund objective, active portfolio management and formal listing | Prospectus dated 2024-10-31 |
| `Nasdaq:BSVO` | https://www.sec.gov/Archives/edgar/data/1592900/000159290025001783/bridgewaysaibbluandbsvo.htm | SEC SAI: exchange and adviser/sub-adviser context | SAI dated 2024-10-31, supplemented 2025-07-10 |

### BSVO scheduled-local review

- Complete pre-save checklist reviewed locally: canonical identity/exchange, issuer classification, active/passive type gate, index status, scope exclusion, source URLs/as-of dates, no-performance-artifact decision, card result metadata, and final-round sequencing.
- Result: local `PASS` for the unsupported-type classification; no performance artifact was written.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## BSVO active-equity refresh source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| Nasdaq:BSVO | https://bridgewayetfs.com/bsvo/ | Official Bridgeway product page: active classification, ticker, exchange, predecessor-inclusive inception, current expense, NAV/market price, current rolling performance, holdings and strategy | Page reviewed 2026-08-17; current month-end performance through 2026-07-31; current page snapshot as of 2026-08-17 |
| Nasdaq:BSVO | https://www.sec.gov/Archives/edgar/data/1592900/000159290024002170/eabridgewayomnismall-capva.htm | Official SEC summary prospectus: active objective, value/small-cap strategy, statistical/evidence-based process, fees, predecessor history and listing | Prospectus dated 2024-10-31; total annual fund operating expenses 0.47%; ETF listing Nasdaq; predecessor history carried from 2010-12-31 |
| Nasdaq:BSVO | https://www.sec.gov/Archives/edgar/data/1592900/000159290025002595/ck0001592900-20250630.htm | Official annual shareholder report: NAV returns, Russell 2000 Value benchmark comparisons, holdings, turnover and predecessor caveat | Fiscal period ended 2025-06-30; 1-year NAV 1.39% vs benchmark 5.54%; 5-year annualized NAV 17.45% vs 12.47%; 10-year annualized NAV 7.14% vs 6.72%; 613 holdings; turnover 17% |
| Nasdaq:BSVO | https://www.sec.gov/Archives/edgar/data/1592900/000159290025001783/bridgewaysaibbluandbsvo.htm | Official SEC SAI: exchange, adviser/sub-adviser and governance cross-check | SAI dated 2024-10-31, supplemented 2025-07-10 |

## BSVO active-equity refresh raw observations and calculations

| Window / source date | BSVO NAV TR | Russell 2000 Value TR | Excess return |
|---|---:|---:|---:|
| 2026 YTD, 2026-07-31 current page | 25.66% | not synchronized | not calculated |
| Rolling 1-year, 2026-07-31 current page | 44.04% | not synchronized | not calculated |
| Rolling 3-year annualized, 2026-07-31 current page | 16.32% | not synchronized | not calculated |
| Rolling 5-year annualized, 2026-07-31 current page | 11.89% | not synchronized | not calculated |
| Rolling 10-year annualized, 2026-07-31 current page | 11.04% | not synchronized | not calculated |
| Since predecessor inception annualized, 2026-07-31 current page | 10.45% | not synchronized | not calculated |
| 1-year fiscal, 2025-06-30 annual report | 1.39% | 5.54% | -4.15 pp |
| 5-year annualized, 2025-06-30 annual report | 17.45% | 12.47% | +4.98 pp |
| 10-year annualized, 2025-06-30 annual report | 7.14% | 6.72% | +0.42 pp |

- Metric basis: Bridgeway NAV total return; the current page states that returns are annualized except periods under one year, and that pre-2023-03-13 performance is predecessor-mutual-fund history. Currency is USD.
- Current product fields: NAV US$30.15, market price US$30.15 and premium/discount 0% on the page snapshot reviewed 2026-08-17; AUM US$2,499.55 million and bid/ask spread 0.07%.
- Active differences are direct calculations: `1.39% - 5.54% = -4.15 pp`; `17.45% - 12.47% = +4.98 pp`; `7.14% - 6.72% = +0.42 pp`.
- Current product page expense ratio 0.45% and 2024 SEC summary-prospectus expense ratio 0.47% are retained as a source-dated conflict; no value is smoothed or backfilled.
- No complete calendar-year row set or synchronized 2026 benchmark series was captured; no calendar CAGR or annual hit rate is calculated.

## BSVO active-equity refresh gaps and scheduled-inline local review

- Canonical identity is `Nasdaq:BSVO`; Bridgeway product, SEC prospectus and annual report confirm EA Bridgeway Omni Small-Cap Value ETF.
- The earlier type-gate record classified BSVO as unsupported when ETF v1 was passive-only. Under the current scheduled workflow’s active long-only support, the official active equity structure is supported; no leverage, inverse, covered-call, option-income or derivative-heavy payoff structure was found.
- The management benchmark is Russell 2000 Value Total Return Index, identified by the official annual report as the measure of the Fund’s investment strategy and universe. S&P 500 TR remains common reference context only.
- Track record is established-with-predecessor-history; live ETF listing began 2023-03-10/13 while official performance includes the predecessor mutual fund from 2010-12-31. The prospectus states that lower ETF expenses can make predecessor-era returns differ from the ETF.
- Current 2026 fields are official fund observations through 2026-07-31; benchmark-relative evidence is a separate official fiscal snapshot through 2025-06-30.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; no numeric drawdown or recovery claim is saved.
- Planned durable paths: created `wiki/analysis/performance/ETF_NASDAQ_BSVO Performance.md`; updated `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region USA; breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; canonical tag `geography/United-States`; all affected wikilinks resolve after the performance page is created.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## AVUV active-equity refresh source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:AVUV | https://www.avantisinvestors.com/avantis-investments/avantis-us-small-cap-value-etf/?aud=indiv | Official Avantis product page: identity, active classification, current NAV/market price, current YTD and strategy/risk language | Page reviewed 2026-08-17; NAV TR YTD 23.61% and market-price TR YTD 23.62% as of 2026-07-31; NAV US$128.69 and market price US$128.73 as of 2026-08-14; expense ratio 0.25% as of 2026-01-01 |
| NYSE Arca:AVUV | https://res.avantisinvestors.com/docs/avantis-us-small-cap-value-avuv-etf-fact-sheet.pdf | Official Avantis factsheet: benchmark, synchronized NAV/market/benchmark performance, inception, expense, holdings, portfolio characteristics, team and risks | Quarterly factsheet as of 2026-06-30; NAV YTD 23.09%, 1-year 39.00%, 3-year annualized 19.06%, 5-year annualized 12.29%, since-inception annualized 16.32%; Russell 2000 Value benchmark 22.99%, 43.01%, 18.73%, 8.23%, 11.85% |
| NYSE Arca:AVUV | https://www.sec.gov/Archives/edgar/data/1710607/000171060726000063/0001710607-26-000063-index.htm | Official SEC filing index cross-check: current Avantis ETF listing and NYSE Arca venue | Filing reviewed 2026-08-17; AVUV listed as NYSE Arca, Inc. |
| NYSE Arca:AVUV | https://www.sec.gov/Archives/edgar/data/1710607/000171060720000387/acetftavuv497k.htm | SEC prospectus/filing cross-check for the original listing and exchange | AVUV NYSE Arca listing; historical filing retained for exchange identity |

## AVUV active-equity refresh raw observations and calculations

| Window / source date | AVUV NAV TR | Russell 2000 Value TR | Excess return |
|---|---:|---:|---:|
| 2026 YTD, current product page 2026-07-31 | 23.61% | not synchronized | not calculated |
| 2026 YTD, factsheet 2026-06-30 | 23.09% | 22.99% | +0.10 pp |
| Rolling 1-year, 2026-06-30 | 39.00% | 43.01% | -4.01 pp |
| Rolling 3-year annualized, 2026-06-30 | 19.06% | 18.73% | +0.33 pp |
| Rolling 5-year annualized, 2026-06-30 | 12.29% | 8.23% | +4.06 pp |
| Since inception annualized, 2026-06-30 | 16.32% | 11.85% | +4.47 pp |

- Metric basis: official Avantis NAV Total Return and market-price return; the factsheet states that returns less than one year are not annualized and keeps benchmark performance separate. Currency is USD.
- Active differences are direct calculations: `23.09% - 22.99% = +0.10 pp`; `39.00% - 43.01% = -4.01 pp`; `19.06% - 18.73% = +0.33 pp`; `12.29% - 8.23% = +4.06 pp`; `16.32% - 11.85% = +4.47 pp`.
- Latest product-page current fields are retained separately: NAV TR YTD 23.61% and market-price TR YTD 23.62% as of 2026-07-31; NAV US$128.69 and market price US$128.73 as of 2026-08-14.
- The factsheet provides no complete calendar-year return table and no compatible annual hit-rate series; no calendar CAGR or hit rate is calculated.
- Risk descriptors from the factsheet as of 2026-06-30: 792 holdings, weighted average market cap $4.1B versus benchmark $3.5B, weighted average book/market 0.63x versus 0.56x, weighted average profits/book 0.31x versus 0.14x, top ten holdings 8.54%.

## AVUV active-equity refresh gaps and scheduled-inline local review

- Canonical identity is `NYSE Arca:AVUV`; official Avantis materials and SEC filings confirm Avantis U.S. Small Cap Value ETF and the NYSE Arca venue.
- AVUV is within supported ETF scope as an active, long-only equity ETF. The official factsheet states that it does not seek to replicate a specified index; no leverage, inverse, covered-call, option-income or derivative-heavy payoff structure was found, although derivatives are disclosed as a risk.
- Management benchmark is Russell 2000 Value Total Return Index, the official strategy-aligned comparator. S&P 500 TR remains common reference context only.
- Track record is developing-short-live-history because inception is 2019-09-24 and the reviewed materials do not yet provide a 10-year return field.
- Current YTD is the newer official product-page observation through 2026-07-31. Benchmark-relative evidence uses the latest synchronized official factsheet through 2026-06-30; the as-of mismatch is disclosed and not compounded.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; no numeric drawdown or recovery claim is saved.
- Planned durable paths: created `wiki/analysis/performance/ETF_NYSE_ARCA_AVUV Performance.md`; updated `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region USA; breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; canonical tag `geography/United-States`; all affected wikilinks resolve after the performance page is created.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## DFAS active-equity refresh source map

workflow: check-etf-performance
mode: lean
caller: trello-etf-processing
handoff: trello_handoff
execution_profile: scheduled-inline

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:DFAS | https://www.sec.gov/Archives/edgar/data/1816125/000181612526000081/c497k.htm | Official SEC summary prospectus: identity, exchange, objective, fee, active classification, process, predecessor-history treatment, risks, annual NAV returns and rolling Russell 2000/Russell 3000 comparisons | Summary prospectus dated 2026-02-28; annual rows 2016-2025 and rolling fields ended 2025-12-31 |
| NYSE Arca:DFAS | https://www.dimensional.com/us-en/funds/dfas/us-small-cap-etf | Official issuer fund-page identity and current fund entry point | Page reviewed 2026-08-17; numeric page fields were not available in the text capture |
| NYSE Arca:DFAS | https://www.dimensional.com/us-en/newsroom/dimensional-lists-four-new-etfs-following-the-industrys-largest-mutual-fund-to-etf-conversion | Official issuer listing announcement: active transparent ETF, NYSE Arca listing, conversion context and listing date | Published 2021-06-14; reviewed 2026-08-17 |
| NYSE Arca:DFAS | https://my.dimensional.com/chmedia/282748/source/dimensional-etf-quick-guide.pdf | Official Dimensional Quick Guide search capture: inception/listing and rolling performance cross-check | Search capture reviewed 2026-08-17; reported inception 1998-12-15, listing 2021-06-14, 1Y 8.18%, 5Y 9.42%, 10Y 9.78%; access redirected to issuer login during direct open |
| NYSE Arca:DFAS | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=dfas | Secondary current performance cross-check: NAV/market-price YTD and rolling fields | Performance page reviewed 2026-08-17; as of 2026-07-31: YTD 16.9%, 1Y 26.9%, 3Y 13.2%, 5Y 8.7%, inception 9.7% |
| NYSE Arca:DFAS | https://www.schwab.wallst.com/Prospect/Research/etfs/summary.asp?symbol=dfas | Secondary quote, NAV, premium/discount, holdings and expense cross-check | Page reviewed 2026-08-17; price 84.48 at 2026-08-14 close; NAV 83.78 and premium/discount +0.04% as of 2026-08-12; 2,059 holdings; total assets US$15.3B; 0.26% expense |

## DFAS active-equity refresh raw observations and calculations

| Window / source date | DFAS NAV TR | Management comparator | Difference |
|---|---:|---:|---:|
| 2026 YTD, Schwab secondary 2026-07-31 | 16.9% | not synchronized | not calculated |
| 1-year annualized, official 2025-12-31 | 8.18% | Russell 2000 Index 12.81% | -4.63 pp |
| 5-year annualized, official 2025-12-31 | 9.42% | Russell 2000 Index 6.09% | +3.33 pp |
| 10-year annualized, official 2025-12-31 | 9.78% | Russell 2000 Index 9.62% | +0.16 pp |
| 2016-2025 cumulative | 154.28% | not calculated | not calculated |
| 2016-2025 CAGR | 9.78% | not calculated | not calculated |
| 2021-2025 CAGR | 9.42% | not calculated | not calculated |

- Official annual NAV Total Return rows: 2016 23.99%, 2017 11.87%, 2018 -13.12%, 2019 21.89%, 2020 10.36%, 2021 29.70%, 2022 -13.80%, 2023 17.53%, 2024 10.35%, 2025 8.18%.
- S&P 500 rows use the cached USD Total Return convention for complete calendar years 2016-2025: 11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, and 17.88%; cumulative 298.33% and CAGR 14.82%.
- DFAS 2016-2025 cumulative and CAGR use `product(1 + annual_return) - 1` and the tenth root from rounded official annual inputs. 2021-2025 cumulative is 56.86% and CAGR 9.42%.
- Annual population standard deviation is 13.73% across the ten rounded DFAS observations; up/down years are 8/2.
- Annual Russell 2000 rows for each calendar year were not disclosed in the reviewed official source; no annual benchmark hit rate is calculated.
- Current YTD is explicitly secondary and uses Schwab's same one-decimal NAV/market-price observation, not an issuer current NAV table.

## DFAS active-equity refresh gaps and scheduled-inline local review

- Canonical identity is `NYSE Arca:DFAS`; SEC and Dimensional materials confirm Dimensional U.S. Small Cap ETF and NYSE Arca venue.
- DFAS is within supported scope as an active, long-only equity ETF. The SEC prospectus says it is actively managed and does not seek to replicate a specific index; no leverage, inverse, covered-call, option-income or derivative-heavy payoff structure was found, although futures/options and related risks are disclosed.
- Active process is `systematic-active`; official materials describe integrated research, portfolio design, portfolio management and trading, with market-cap weighting and possible emphasis on small size, lower relative price and higher profitability.
- Management comparator is Russell 2000 Index, the official additional index with a similar investment universe in the SEC performance table. S&P 500 TR remains common reference context only.
- Track record is `established-with-predecessor-history`; the SEC performance section adopts predecessor-fund results before the June 2021 reorganization, while the ETF listing date is 2021-06-14.
- The SEC summary prospectus reports total annual fund operating expenses of 0.26% as of 2026-02-28; the official Quick Guide search capture showed 0.27%, so the source-dated fee difference is preserved rather than smoothed.
- Current YTD is the secondary Schwab observation through 2026-07-31; price/NAV snapshot dates are separate and are not used to replace NAV total-return history.
- Official daily NAV history sufficient for reproducible maximum drawdown and recovery was not verified; no numeric drawdown or recovery claim is saved.
- Historical `DFAS unsupported ETF type` material from the earlier passive-only gate is retained for provenance; this refresh supersedes that classification under the current active-long-only support rule.
- Planned durable paths: created `wiki/analysis/performance/ETF_CBOE_BZX_DFAS Performance.md`; updated `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region USA; breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; canonical tag `geography/United-States`; all affected wikilinks resolve after the performance page is created.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## FNDC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:FNDC | https://www.schwabassetmanagement.com/products/fndc | Official product page: fund identity, passive management style, index, expense, NAV, rolling/YTD performance, risk fields, and portfolio snapshot | NAV/quote fields through 2026-08-14; performance and risk fields through 2026-07-31 |
| NYSE Arca:FNDC | https://www.schwabassetmanagement.com/products/fndc/documents?page=0 | Official document hub and performance/factsheet entry points | Hub reviewed 2026-08-17; performance summary entry updated 2026-07-31; factsheet entry updated 2026-06-30 |
| NYSE Arca:FNDC | https://www.sec.gov/Archives/edgar/data/1454889/000088454626000301/c497k.htm | SEC summary prospectus: annual total returns, index methodology, passive/index-fund treatment, benchmark change, and return definitions | Prospectus dated 2026-06-26; annual rows through 2025 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common benchmark definition | USD total return, dividends reinvested; page reviewed 2026-08-17 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current cross-check | `14.04%` YTD displayed on page dated 2026-08-10; not synchronized with FNDC YTD 2026-07-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-2021/; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached project convention for complete calendar years | 2016-2025 USD gross total return, dividends reinvested, as of 2025-12-31 |

## FNDC raw observations and calculations

| Year | FNDC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 8.87% | 11.96% |
| 2017 | 29.04% | 21.83% |
| 2018 | -18.77% | -4.38% |
| 2019 | 20.02% | 31.49% |
| 2020 | 7.11% | 18.40% |
| 2021 | 9.83% | 28.71% |
| 2022 | -14.82% | -18.11% |
| 2023 | 15.21% | 26.29% |
| 2024 | 1.57% (source precision 1.5698548%) | 25.02% |
| 2025 | 35.79% (source precision 35.7881285%) | 17.88% |
| 2026 YTD | 10.96% (official NAV, 2026-07-31) | 14.04% (official current page dated 2026-08-10; not same date) |

- FNDC 2016-2025 compound: `118.08%` cumulative; rounded-input CAGR `8.11%`.
- FNDC 2021-2025 compound: `48.65%` cumulative; rounded-input CAGR `8.25%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- The official rolling 10-year FNDC NAV TR field is `8.48%` as of 2026-07-31; raw rolling endpoints were not disclosed in the reviewed issuer capture. The `8.11%` figure is the separate 2016-2025 calendar-window calculation using the SEC annual rows.
- Annual-row sample standard deviation is `17.24%`; issuer-reported 3-year standard deviation is `15.14%` as of 2026-07-31. These are different windows and neither is daily maximum drawdown.
- Year-end cumulative-path drawdown approximation is `-18.77%` at the 2018 year-end observation, with recovery above the prior year-end high by 2020; no daily maximum drawdown is claimed.
- The 2024 and 2025 source rows retain additional precision in this batch, while page/index displays are rounded to two decimals.

## FNDC pre-save checklist

- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Entity and exchange reconciled as `NYSE Arca:FNDC`; passive/index-fund classification confirmed from Schwab and SEC sources.
- Return basis, USD currency, issuer benchmark, common benchmark, annual coverage, current-field as-of dates, rolling-vs-calendar distinction, and separate distribution-yield field were checked before write.
- Benchmark/index change effective 2024-06-21 is disclosed; the historical fund NAV return series is not spliced with an unverified proxy.
- Every durable number above maps to an official URL or the cached S&P convention; rounded-input calculations are labeled and no synchronized S&P current-YTD spread is asserted.
- Existing international-region navigation was updated with canonical `NYSE Arca:FNDC`; no duplicate performance page was found.
- Local pre-save result: `PASS`.

## FNDC gaps and conflicts

- The issuer changed the comparative index effective 2024-06-21; pre-change and post-change benchmark identities are preserved rather than treated as one unchanged index series.
- FNDC YTD is as of 2026-07-31 while the official S&P current cross-check is displayed for 2026-08-10; no same-date benchmark spread is claimed.
- Annual issuer rows are rounded in the page display; source precision for 2024 and 2025 is retained, and cumulative/CAGR/annual-row volatility calculations remain input-dependent.
- Official daily NAV history sufficient for a daily maximum-drawdown and recovery statistic was not verified; only the labeled year-end observation approximation is retained.

## DES official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:DES | https://www.wisdomtree.com/us/products/equity/des | Official product page: fund identity, passive/index-tracking description, NAV/market price, rolling and YTD performance, expense, and distributions | NAV/price and expense through 2026-08-14; rolling 10Y and YTD performance through 2026-07-31; distributions through 2026-07-28 |
| NYSE Arca:DES | https://www.wisdomtree.com/us/media/des-presentation | Official issuer presentation: calendar-year NAV total returns and methodology | 2016-2025 annual NAV rows; presentation data as of 2026-03-31 |
| NYSE Arca:DES | https://www.wisdomtree.com/us/media/wisdomtree-factsheet-des-1008 | Official quarterly factsheet: exchange, inception, index, expense, and return definition | Factsheet data as of 2026-03-31 |
| NYSE Arca:DES | https://www.sec.gov/Archives/edgar/data/1350487/000121465925011322/des73125497k.htm | SEC summary prospectus: passive indexing, listing, fees, and return treatment | Filing reviewed 2026-08-17 |
| WTSDI | https://www.wisdomtree.com/us/indexes/wtsdi | Official tracked-index methodology and identity | Index methodology page reviewed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common benchmark definition | USD total return convention; page reviewed 2026-08-17 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current cross-check | `14.04%` YTD displayed on page dated 2026-08-10; not synchronized with DES YTD 2026-07-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-2021/; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached project convention for complete calendar years | 2016-2025 USD gross total return, dividends reinvested, as of 2025-12-31 |

## DES raw observations and calculations

| Year | DES NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.06% | 11.96% |
| 2017 | 8.66% | 21.83% |
| 2018 | -12.74% | -4.38% |
| 2019 | 20.30% | 31.49% |
| 2020 | -4.41% | 18.40% |
| 2021 | 26.71% | 28.71% |
| 2022 | -10.94% | -18.11% |
| 2023 | 16.40% | 26.29% |
| 2024 | 9.79% | 25.02% |
| 2025 | 0.26% | 17.88% |
| 2026 YTD | 22.93% (official NAV, 2026-07-31) | 14.04% (official current page dated 2026-08-10; not same date) |

- DES 2016-2025 compound: `106.62%` cumulative; rounded-input CAGR `7.53%`.
- DES 2021-2025 compound: `44.59%` cumulative; rounded-input CAGR `7.65%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- The official rolling 10-year DES NAV TR field is `8.04%` as of 2026-07-31; raw rolling endpoints were not disclosed in the reviewed issuer capture. The `7.53%` figure is the separate 2016-2025 calendar-window calculation from rounded annual rows.
- DES annual-row sample standard deviation is `15.30%`; this is calculated from the ten rounded annual NAV TR observations and is not a daily risk measure.
- Year-end cumulative-path drawdown approximation is `-12.74%` at the 2018 year-end observation, with recovery above the prior year-end high by 2019; no daily maximum drawdown is claimed.
- Latest four official cash distributions reviewed sum to `$0.305`; latest listed distribution is `$0.045` ex/pay 2026-07-28/30, and the product page shows distribution yield `1.30%` as of 2026-08-14. These are separate from total return.

## DES pre-save checklist

- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Entity and exchange reconciled as `NYSE Arca:DES`; passive/index-tracking classification confirmed from issuer and SEC sources.
- Return basis, USD currency, issuer benchmark, common benchmark, annual coverage, current-field as-of dates, and separate NAV/price/distribution fields were checked before write.
- Every durable number above maps to an official URL or the cached S&P convention; rounded-input calculations are labeled and no synchronized S&P current-YTD spread is asserted.
- Existing DES performance path and USA-region navigation were updated in place; no duplicate canonical page was created.
- Local pre-save result: `PASS`.

## DES gaps and conflicts

- DES official rolling 10-year performance is available, but raw endpoint values were not disclosed in the reviewed issuer capture; it is not substituted with the calendar-window CAGR.
- DES YTD is as of 2026-07-31 while the official S&P current cross-check is displayed for 2026-08-10; no same-date benchmark spread is claimed.
- Annual issuer rows are rounded; cumulative, CAGR, and annual-row volatility are rounded-input calculations.
- Official daily NAV history sufficient for a daily maximum-drawdown and recovery statistic was not verified; only the labeled year-end observation approximation is retained.

## SSEUF / R2US official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:R2US / SSEUF | https://www.ssga.com/uk/en_gb/institutional/etfs/state-street-spdr-russell-2000-us-small-cap-ucits-etf-acc-zprr-gy | Official State Street product page: fund identity, listing table, benchmark, official Fund Net/NAV performance, current NAV/YTD, standard deviation and tracking error | Annual rows 2016-2025 and rolling/current fields as of 2026-07-31; NAV quote as of 2026-07-17 |
| LSE:R2US / SSEUF | https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-zprr-gy.pdf | Official State Street factsheet: ISIN, USD LSE ticker R2US, inception, TER, accumulating share class, optimized replication, benchmark and performance | Factsheet dated 30 Jun 2026; performance table through 31 Jul 2026 |
| LSE:R2US / SSEUF | https://www.ssga.com/library-content/kids?country=ie&documentType=kid&isin=IE00BJ38QD84&language=en_gb&ticker=zprr-gy | Official KID: index-tracking/passive objective, optimization policy, accumulating income treatment and risk disclosures | Accurate as of 2026-02-19 |
| SSEUF alias | https://www.google.com/finance/beta/quote/SSEUF%3AOTCMKTS | Secondary OTC alias and USD quote cross-check; canonical exchange key remains LSE:R2US | Search snapshot accessed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused without a new search |

## SSEUF / R2US raw observations and calculations

| Year | R2US Fund Net / NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 20.97% | 11.96% |
| 2017 | 13.98% | 21.83% |
| 2018 | -11.34% | -4.38% |
| 2019 | 24.98% | 31.49% |
| 2020 | 19.36% | 18.40% |
| 2021 | 14.70% | 28.71% |
| 2022 | -20.78% | -18.11% |
| 2023 | 16.27% | 26.29% |
| 2024 | 11.19% | 25.02% |
| 2025 | 12.32% | 17.88% |
| 2026 YTD | 18.69% | not available from cached current-year benchmark |

- Input ticker `SSEUF` is an OTC alias; official State Street listing data maps the same ISIN/share class to USD `LSE:R2US`. The primary listing is Deutsche Börse `ZPRR`, but the durable key uses the USD London line matching the input currency.
- Metric basis: official R2US Fund Net performance is NAV-based and net of fees; the accumulating share class retains income in NAV.
- Issuer benchmark: Russell 2000 Index Net Total Return (`RU20N30U`); retained as metadata and not substituted for the common S&P 500 reference.
- Official 10-year rolling NAV TR: `163.53%` cumulative / `10.18%` annualized as of 2026-07-31; since-inception: `177.36%` cumulative / `8.81%` annualized.
- 2016-2025 R2US compound: `140.61%` cumulative; rounded-input CAGR `9.18%`.
- 2021-2025 R2US compound: `31.94%` cumulative; rounded-input CAGR `5.70%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk observations: 3-year standard deviation `19.67%` and tracking error `0.08%` as of 2026-07-31.

## SSEUF / R2US gaps and conflicts

- The input is an OTC alias (`SSEUF`) rather than the official USD London ticker; the canonical exchange-qualified key is `LSE:R2US` and the official primary listing is Deutsche Börse `ZPRR`. The alias, ISIN, share-class currency and index identity were reconciled before save.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## SCZ official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:SCZ` | https://www.ishares.com/us/products/239627/ | Official iShares product page: identity, NASDAQ listing, inception, benchmark, current NAV/YTD, expense ratio, holdings and risk fields | Current NAV/price 2026-08-14; NAV TR YTD 2026-08-13; holdings 2026-08-13; risk fields through 2026-07-31 |
| `NASDAQ:SCZ` | https://www.ishares.com/ch/professionals/en/products/239627/ishares-msci-eafe-smallcap-etf?switchLocale=Y | Official iShares performance table with complete 2016-2025 calendar rows | Table reviewed 2026-08-17; rows displayed at one decimal |
| `NASDAQ:SCZ` | https://www.ishares.com/us/literature/fact-sheet/scz-ishares-msci-eafe-small-cap-etf-fund-fact-sheet-en-us.pdf | Official factsheet: NAV return basis, 2021-2025 rows, benchmark, inception and expense ratio | Factsheet as of 2026-06-30 |
| `NASDAQ:SCZ` | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-eafe-small-cap-etf-7-31.pdf | Official summary prospectus: objective, index-tracking scope and fee/risk context | Dated 2025-11-28 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | Cached USD total-return convention; annual rows as of 2025-12-31 |

## SCZ raw observations and calculations

| Year | SCZ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 2.40% | 11.96% |
| 2017 | 32.50% | 21.83% |
| 2018 | -17.80% | -4.38% |
| 2019 | 24.70% | 31.49% |
| 2020 | 12.10% | 18.40% |
| 2021 | 10.02% | 28.71% |
| 2022 | -21.22% | -18.11% |
| 2023 | 12.90% | 26.29% |
| 2024 | 1.35% | 25.02% |
| 2025 | 32.10% | 17.88% |

- Metric basis: official iShares NAV total return with dividends/capital gains reinvested and fund expenses deducted; USD.
- Issuer benchmark: `MSCI EAFE Small Cap Index (Net)`; retained as metadata and not substituted for the common S&P 500 reference.
- SCZ 2016-2025 compound from displayed annual rows: `104.25%` cumulative; rounded-input CAGR `7.40%`.
- SCZ 2021-2025 compound from displayed annual rows: `31.01%` cumulative; rounded-input CAGR `5.55%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Current NAV TR YTD: `13.83%` as of 2026-08-13; current NAV `US$87.17` and closing price `US$87.14` as of 2026-08-14.
- Issuer rolling 10-year NAV TR average annual: `8.60%` as of 2026-06-30; raw endpoints are not disclosed and this is not substituted for the calendar-window CAGR.
- Official risk fields: 3-year standard deviation `14.97%` and beta `0.78` as of 2026-07-31; holdings `2,056` as of 2026-08-13.

## SCZ gaps and local review

- The annual rows are official but rounded at different displayed precision: 2016-2020 one decimal in the product performance table and 2021-2025 two decimals in the June 2026 factsheet. Calculations preserve the displayed inputs and are labelled rounded-input.
- The current S&P 500 TR field reviewed is not synchronized to the SCZ current YTD observation, so no current-year cross-asset comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no secondary proxy is used.
- Planned durable paths: create `wiki/analysis/performance/ETF_NASDAQ_SCZ Performance.md`; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `International`; add breadcrumb `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`; add `geography/International` and `geography/international-ex-US`; preserve numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## AVUV unsupported ETF type

- Input ticker: `AVUV`; canonical identity: `NYSE Arca:AVUV`; fund: Avantis U.S. Small Cap Value ETF.
- Type gate: `unsupported ETF type`. The official Avantis product page says the fund is actively managed and does not seek to replicate the performance of a specified index. The current SEC summary prospectus states the same and describes portfolio-manager security selection using profitability/value characteristics plus possible derivatives. This fails ETF v1's passive, index-tracking equity scope.

### AVUV Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:AVUV` | https://www.avantisinvestors.com/avantis-investments/avantis-us-small-cap-value-etf/?aud=indiv | Official issuer product page: identity, exchange, active-management classification, and index-replication exclusion | Page reviewed 2026-08-17; current issuer page |
| `NYSE Arca:AVUV` | https://www.sec.gov/Archives/edgar/data/1710607/000171060725000416/acetftavuv497k.htm | Official SEC summary prospectus: identity, exchange, expense ratio, active security-selection strategy, derivatives context, and no-specified-index statement | Summary Prospectus dated 2026-01-01; reviewed 2026-08-17 |

### AVUV scheduled-local review

- Complete pre-save checklist reviewed locally: canonical identity/exchange, official issuer and SEC classification, active/passive type gate, index status, ETF v1 scope exclusion, source URLs/as-of dates, no-performance-artifact decision, Trello result metadata, and next-card sequencing.
- Result: local `PASS` for the unsupported-type classification; no performance page, annual equity-return table, S&P 500 comparison, region row, or ETF Performance Index row was written.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## DFAS unsupported ETF type

- Input ticker: `DFAS`; canonical identity: `NYSE Arca:DFAS`; fund: Dimensional U.S. Small Cap ETF.
- Type gate: `unsupported ETF type`. The current SEC summary prospectus identifies DFAS as an actively managed ETF that does not seek to replicate the performance of a specific index, and describes flexible portfolio-management decisions plus possible futures/options use. Dimensional's official materials also describe DFAS within its active ETF lineup. This fails ETF v1's passive, index-tracking equity scope.

### DFAS Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:DFAS` | https://www.sec.gov/Archives/edgar/data/1816125/000181612526000081/c497k.htm | Official SEC summary prospectus: identity, exchange, objective, active-management classification, index-replication exclusion, flexible process and derivative context | Summary Prospectus dated 2026-02-28; reviewed 2026-08-17 |
| `NYSE Arca:DFAS` | https://www.dimensional.com/us-en/our-approach/dimensional-equity-solutions | Official issuer equity-solutions page: DFAS identity and placement in Dimensional's component/small-cap active ETF lineup | Issuer page reviewed 2026-08-17 |
| `NYSE Arca:DFAS` | https://www.dimensional.com/us-en/newsroom/dimensional-lists-four-new-etfs-following-the-industrys-largest-mutual-fund-to-etf-conversion | Official issuer listing announcement: NYSE Arca listing and explicit active transparent ETF description | Published 2021-06-14; reviewed 2026-08-17 |

### DFAS scheduled-local review

- Complete pre-save checklist reviewed locally: canonical identity/exchange, official issuer and SEC classification, active/passive type gate, index status, ETF v1 scope exclusion, source URLs/as-of dates, no-performance-artifact decision, Trello result metadata, and next-card sequencing.
- Result: local `PASS` for the unsupported-type classification; no performance page, annual equity-return table, S&P 500 comparison, region row, or ETF Performance Index row was written.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## AVDV unsupported ETF type

- Input ticker: `AVDV`; canonical identity: `NYSE Arca:AVDV`; fund: Avantis International Small Cap Value ETF.
- Type gate: `unsupported ETF type`. The official Avantis product page says the fund is actively managed and does not seek to replicate the performance of a specified index. The current SEC summary prospectus states the same and describes portfolio-manager buy/sell/hold decisions using profitability and value characteristics, with possible derivative use. This fails ETF v1's passive, index-tracking equity scope.

### AVDV Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:AVDV` | https://www.avantisinvestors.com/avantis-investments/avantis-international-small-cap-value-etf/ | Official issuer product page: identity, exchange, active-management classification, index-replication exclusion and portfolio-manager decision context | Page reviewed 2026-08-17; current issuer page |
| `NYSE Arca:AVDV` | https://www.sec.gov/Archives/edgar/data/1710607/000171060725000402/acetftavdv497k.htm | Official SEC summary prospectus: identity, exchange, objective, fee, active security-selection strategy, derivatives context, and no-specified-index statement | Summary Prospectus dated 2026-01-01; reviewed 2026-08-17 |

### AVDV scheduled-local review

- Complete pre-save checklist reviewed locally: canonical identity/exchange, official issuer and SEC classification, active/passive type gate, index status, ETF v1 scope exclusion, source URLs/as-of dates, no-performance-artifact decision, Trello result metadata, and final-card sequencing.
- Result: local `PASS` for the unsupported-type classification; no performance page, annual equity-return table, S&P 500 comparison, region row, or ETF Performance Index row was written.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## IWN official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:IWN | https://www.ishares.com/us/products/239712/ishares-russell-2000-value-etf | Official iShares product page: identity, exchange, inception, benchmark, fee, current NAV/price, NAV YTD, standard deviation, beta, holdings, and fund facts | Current NAV/price and key facts through 2026-08-14; NAV TR YTD through 2026-08-13; risk fields through 2026-07-31 |
| NYSE Arca:IWN | https://www.ishares.com/us/literature/fact-sheet/iwn-ishares-russell-2000-value-etf-fund-fact-sheet-en-us.pdf | Official factsheet: NAV total-return definition, 2021-2025 calendar rows, annualized returns, fee and risk cross-check | Factsheet as of 2026-06-30 |
| NYSE Arca:IWN | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-russell-2000-value-etf-3-31.pdf | Official summary prospectus: passive objective, benchmark, complete 2016-2025 calendar-year table, YTD, and best/worst quarter | Prospectus performance table through 2025-12-31; YTD field through 2026-06-30 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached annual reference rows | 2022-2025; reused without new search |

## IWN raw observations and calculations

| Year | IWN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.64% | 11.96% |
| 2017 | 7.73% | 21.83% |
| 2018 | -12.94% | -4.38% |
| 2019 | 22.17% | 31.49% |
| 2020 | 4.50% | 18.40% |
| 2021 | 27.96% | 28.71% |
| 2022 | -14.67% | -18.11% |
| 2023 | 14.42% | 26.29% |
| 2024 | 7.74% | 25.02% |
| 2025 | 12.41% | 17.88% |
| 2026 YTD | 25.91% | not available from cached current-year benchmark |

- Metric basis: official iShares IWN NAV Total Return in USD; dividends and capital-gains distributions are reinvested and fund expenses are reflected in NAV. The complete 2016-2025 annual rows are published at 0.1% precision.
- Issuer benchmark: `Russell 2000 Value Index`; it is retained as metadata and is not substituted for the common S&P 500 reference.
- 2016-2025 IWN compound: `138.50%` cumulative; rounded-input CAGR `9.08%`.
- 2021-2025 IWN compound: `51.31%` cumulative; rounded-input CAGR `8.64%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Annual-row positive/negative years: `8 / 2`; best 2016 `+31.64%`, least positive 2024 `+7.74%`, worst 2022 `-14.67%`, least bad down year 2018 `-12.94%`.
- Official issuer rolling 10-year NAV TR annualized: `10.69%` as of 2026-06-30; raw endpoints were not disclosed and this field is kept separate from the annual-row CAGR.
- Official current NAV TR YTD: `25.91%` as of 2026-08-13; market price `US$227.43` and NAV `US$227.41` as of 2026-08-14; calculated premium `0.01%`.
- Official three-year standard deviation `19.10%` and equity beta `1.08` as of 2026-07-31; holdings `1,389` as of 2026-08-11; best quarter `+33.29%` and worst quarter `-35.70%` from the official prospectus.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## IWN gaps and scheduled-inline local review

- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- The issuer rolling 10-year field is a separate annualized observation as of 2026-06-30; raw endpoints and exact elapsed years were not disclosed.
- The complete annual table is official but rounded to 0.1%, so cumulative and CAGR outputs are explicitly rounded-input calculations.
- Complete pre-save checklist reviewed locally: canonical ticker/exchange, passive/index-tracking type, issuer benchmark, NAV return definition, distributions, annual rows, cached S&P 500 window, current YTD and price/NAV as-of dates, calculations, source URLs, unresolved gaps, exact planned page/source-batch/index/region/log contents, graph links, canonical geography tag, and single primary region.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## CPLCF / CUSS official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:CUSS / input CPLCF | https://www.ishares.com/uk/individual/en/products/253480/cuss?siteEntryPassthrough=true&switchLocale=y | Official iShares product page: identity, USD listing, ISIN, current index, name/benchmark change, NAV, YTD and calendar NAV TR rows | Product/current fields through 2026-07-29; calendar rows 2016-2025 |
| LSE:CUSS / input CPLCF | https://www.ishares.com/uk/professional/en/products/253480/csuss | Official professional page: USD share-class facts, expense, holdings and risk fields | Holdings/current fields through 2026-07-30; risk fields through 2026-06-30 |
| LSE:CUSS / input CPLCF | https://www.ishares.com/ch/privatkunden/de/literature/fact-sheet/csuss-ishares-msci-usa-small-cap-ctb-enhanced-esg-ucits-etf-fund-fact-sheet-de-ch.pdf | Official factsheet: calendar NAV performance and return definition | Calendar rows 2016-2025; factsheet capture reviewed 2026-08-17 |
| LSE:CUSS / input CPLCF | https://www.londonstockexchange.com/stock/CUSS/ishares/company-page | Official exchange listing cross-check | USD CUSS line reviewed 2026-08-17 |
| S&P 500 TR current | https://www.slickcharts.com/sp500/returns/ytd | Secondary current benchmark cross-check | `10.14%` total return YTD through 2026-07-31; later than CUSS current YTD |

## CPLCF / CUSS raw observations and calculations

| Year | CUSS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 19.13% | 11.96% |
| 2017 | 16.49% | 21.83% |
| 2018 | -10.49% | -4.38% |
| 2019 | 26.56% | 31.49% |
| 2020 | 18.15% | 18.40% |
| 2021 | 18.86% | 28.71% |
| 2022 | -16.94% | -18.11% |
| 2023 | 15.63% | 26.29% |
| 2024 | 10.71% | 25.02% |
| 2025 | 9.60% | 17.88% |
| 2026 YTD | 14.97% | 10.14%† |

- Metric basis: official iShares NAV Total Return, with gross income reinvested where applicable and performance after ongoing charges; USD accumulating share class values are used for the canonical USD line.
- `†` secondary S&P 500 current cross-check with a different as-of date; complete-year benchmark rows use the cached project convention.
- 2016-2025 CUSS compound: `157.28%` cumulative; rounded-input CAGR `9.91%`.
- 2021-2025 CUSS compound: `38.51%` cumulative; rounded-input CAGR `6.73%`.
- Annual-row positive/negative years: `8 / 2`; best 2019 `+26.56%`, worst 2022 `-16.94%`.
- Official current NAV TR YTD: `14.97%` as of 2026-07-29; NAV quote `US$675.97` as of 2026-07-29.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.

## CPLCF / CUSS gaps, benchmark change, and scheduled-local gate

- CPLCF is an OTC input alias; official iShares listings identify the USD London line as `CUSS` for ISIN `IE00B3VWM098`. The fund changed name/objective and benchmark on 2022-06-01; the pre-change benchmark was MSCI USA Small Cap Index and the current benchmark is MSCI USA Small Cap ESG Enhanced Focus CTB Index.
- The latest official iShares current NAV TR field located is `14.97%` as of 2026-07-29. The latest displayed NAV quote in the same capture is `US$675.97`; these are separate as-of fields.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Complete pre-save checklist: identity/exchange/index, alias and ISIN, benchmark-history change, return basis, candidate claims, periods, units/currencies, metric definitions, as-of dates, calculations, source URLs, unresolved gaps, exact planned page/batch/index/log contents, graph links, and ownership were reviewed locally before write.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## RWJ official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:RWJ | https://www.sec.gov/Archives/edgar/data/1378872/000119312525325669/d54028d497k.htm | Official SEC summary prospectus: fund identity, exchange, passive objective, index, expense ratio, risks, inception, annualized performance and official benchmark context | Prospectus filed 2025-12-18; performance period ended 2024-12-31 |
| NYSE Arca:RWJ | https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/rwj-invesco-s-p-smallcap-600-revenue-etf-fact-sheet.pdf | Official Invesco factsheet entry point and product identity | Link reviewed 2026-08-17; current PDF capture did not expose a synchronized annual table |
| NYSE Arca:RWJ | https://www.etfrc.com/RWJ | Secondary standardized performance and expense snapshot | Total returns through 2026-07-31; expense/AUM snapshot as displayed on page |
| NYSE Arca:RWJ | https://totalrealreturns.com/n/AVUV%2CRWJ%2CXSVM | Secondary dividend-reinvested annual rows, YTD, rolling returns and drawdown proxy | Daily/annual observations through 2026-08-14 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR current | https://www.slickcharts.com/sp500/returns/ytd | Secondary current benchmark cross-check | `10.14%` total return YTD through 2026-07-31; not synchronized with RWJ 2026-08-14 |

## RWJ raw observations and calculations

| Year | RWJ total-return proxy | S&P 500 TR |
|---|---:|---:|
| 2016 | 30.72%* | 11.96% |
| 2017 | 5.09%* | 21.83% |
| 2018 | -16.95%* | -4.38% |
| 2019 | 20.29%* | 31.49% |
| 2020 | 20.83%* | 18.40% |
| 2021 | 52.83%* | 28.71% |
| 2022 | -10.97%* | -18.11% |
| 2023 | 16.22%* | 26.29% |
| 2024 | 11.81%* | 25.02% |
| 2025 | 7.75%* | 17.88% |
| 2026 YTD | 28.61%* | 10.14%† |

- Metric basis: RWJ rows are a secondary dividend-reinvested total-return proxy; official SEC average annual returns are net of expenses but do not provide the same 2016-2025 calendar series in the reviewed capture. S&P rows are USD total return with dividends reinvested.
- `*` secondary TotalRealReturns observations; `†` secondary Slickcharts current cross-check with a different as-of date.
- 2016-2025 RWJ compound: `215.92%` cumulative; rounded-input CAGR `12.19%`.
- 2021-2025 RWJ compound: `90.51%` cumulative; rounded-input CAGR `13.76%`.
- Annual-row sample standard deviation from rounded observations: `19.95%`; this is not daily NAV volatility.
- Official SEC average annual total return: `10.33%` for the 10-year period ended 2024-12-31; kept separate from the calendar-row proxy.
- Secondary drawdown proxy: maximum drawdown `-45.04%` on 2020-03-18 from 2019-12-26 peak; recovery date not disclosed. Current drawdown was `-0.83%` on 2026-08-14 from 2026-08-04 peak.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.

## RWJ gaps, conflicts, and scheduled-local gate

- Official annual NAV rows and a synchronized official current NAV YTD field were not verified in the reviewed capture. The page labels all annual/current proxy values explicitly and does not mix them with the official SEC rolling figure.
- ETFRC standardized return was `25.7%` YTD as of 2026-07-31, versus TotalRealReturns `28.61%` through 2026-08-14; the later source was used for the current proxy, with the conflict/as-of difference preserved.
- Official daily NAV history was not verified; the `-45.04%` drawdown is a secondary total-return proxy and recovery timing is not disclosed.
- Complete pre-save checklist: identity/exchange/index, return basis, benchmark, candidate claims, periods, units/currencies, metric definitions, as-of dates, calculations, source URLs, unresolved gaps, exact planned page/batch/index/log contents, graph links, and ownership were reviewed locally before write.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## XSMO official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:XSMO | https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/xsmo-invesco-s-p-smallcap-momentum-etf-fact-sheet.pdf | Official Invesco fact sheet: fund identity, exchange, inception, expense ratio, index, annual NAV rows, issuer average annual returns, and benchmark continuity note | Annual rows 2016-2025 and standard performance as of 2025-12-31 |
| NYSE Arca:XSMO | https://www.invesco.com/us/en/financial-products/etfs/invesco-sp-smallcap-momentum-etf.html | Official Invesco product page and product identity cross-check | Current product page accessed 2026-08-17; current numeric YTD field not extractable |
| NYSE Arca:XSMO | https://www.sec.gov/Archives/edgar/data/1209466/000119312525190429/d56632d497k.htm | SEC summary prospectus: passive objective, ticker/exchange, fee breakdown, index exposure, inception, and risk quarters | Filed 2025; risk/performance table through 2024-12-31 |
| NYSE Arca:XSMO | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=xsmo | Secondary NAV performance snapshot used only for current YTD context | NAV YTD +30.5% as of 2026-06-30 |
| NYSE Arca:XSMO | https://totalrealreturns.com/n/XSMO | Secondary total-return cross-check | Snapshot +18.10% YTD as of 2026-07-29; return basis/as-of conflict, not mixed into NAV ranking |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused without a new search |

## XSMO raw observations and calculations

| Year | XSMO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.17% | 11.96% |
| 2017 | 23.42% | 21.83% |
| 2018 | -2.88% | -4.38% |
| 2019 | 28.35% | 31.49% |
| 2020 | 21.84% | 18.40% |
| 2021 | 19.28% | 28.71% |
| 2022 | -15.48% | -18.11% |
| 2023 | 21.43% | 26.29% |
| 2024 | 17.57% | 25.02% |
| 2025 | 9.81% | 17.88% |
| 2026 YTD | 30.50% (secondary NAV) | not available from cached current-year benchmark |

- Metric basis: official XSMO NAV Total Return in USD; distributions are reinvested and fund expenses are reflected in NAV.
- Issuer benchmark: S&P SmallCap 600 Momentum Index; retained as metadata and not substituted for the common S&P 500 reference.
- 2016-2025 XSMO compound: `217.50%` cumulative; rounded-input CAGR `12.25%`.
- 2021-2025 XSMO compound: `58.05%` cumulative; rounded-input CAGR `9.59%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official fact sheet reports 10-year average annual NAV TR `12.25%` and inception average annual NAV TR `8.38%` as of 2025-12-31; the 10-year issuer field is not relabelled as a raw cumulative endpoint.
- SEC prospectus risk observations: best quarter `+23.72%` in 2Q2020; worst quarter `-25.15%` in 1Q2020.

## XSMO gaps and conflicts

- Official current XSMO NAV TR YTD was not located in the issuer materials read on 2026-08-17. The latest usable current snapshot is a secondary NAV return of `30.50%` as of 2026-06-30.
- Another secondary source reports `18.10%` YTD as of 2026-07-29, but its return basis and date convention are not reconciled with the Schwab NAV snapshot; it is retained as a conflict and excluded from the ranking table.
- The tracked-index history includes predecessor methodologies before 2019-06-21; calendar rows remain issuer fund NAV observations, not a synthetic backfilled index series.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## FNDA official and secondary source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:FNDA | https://www.schwabassetmanagement.com/products/fnda | Official Schwab product page: objective, index, passive style, fee, current NAV/YTD, holdings, turnover, beta and standard deviation | Official NAV/YTD and risk fields as of 2026-06-30; quote/NAV profile as of 2026-07-30 |
| NYSE Arca:FNDA | https://www.schwabassetmanagement.com/resource/fnda-fact-sheet | Official Schwab factsheet entry | Last updated 2026-06-30; PDF viewer download was not text-extractable in the web session |
| NYSE Arca:FNDA | https://www.sec.gov/Archives/edgar/data/1454889/000110465925063127/tm2513735-8_497k.htm | SEC summary prospectus: passive objective, fee, index methodology, 2024 index change, risk quarters and official 2024 performance table | Filed 2025-06-27; performance table through 2024-12-31 |
| NYSE Arca:FNDA | https://www.etfreplay.com/etf/fnda | Secondary dividend-adjusted total-return annual rows used for 2016-2025 common-window calculations | Data as of 2026-08-03; complete annual rows through 2025 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused without a new search |

## FNDA raw observations and calculations

| Year | FNDA secondary total-return proxy | S&P 500 TR |
|---|---:|---:|
| 2016 | 23.54% | 11.96% |
| 2017 | 12.66% | 21.83% |
| 2018 | -12.10% | -4.38% |
| 2019 | 24.33% | 31.49% |
| 2020 | 8.46% | 18.40% |
| 2021 | 31.11% | 28.71% |
| 2022 | -14.82% | -18.11% |
| 2023 | 20.31% | 26.29% |
| 2024 | 8.99% | 25.02% |
| 2025 | 7.44% | 17.88% |
| 2026 YTD | 21.18% (official NAV) | not available from cached current-year benchmark |

- Metric basis for the current field: official Schwab NAV Total Return in USD; distributions are reinvested and fund expenses are reflected in NAV.
- Annual-row basis: ETFreplay dividend-adjusted total-return proxy; it is not relabelled as official issuer NAV return.
- Issuer benchmark: current RAFI Fundamental High Liquidity US Small Index; the fund changed from Russell RAFI US Small Company Index effective 2024-06-21.
- Official rolling 10-year NAV TR: annualized `11.53%` as of 2026-06-30; raw endpoints are not disclosed.
- 2016-2025 secondary proxy compound: `159.56%` cumulative; rounded-input CAGR `10.01%`.
- 2021-2025 secondary proxy compound: `57.34%` cumulative; rounded-input CAGR `9.49%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk observations: best quarter `+30.46%` in 4Q2020; worst quarter `-35.49%` in 1Q2020; 3-year standard deviation `18.38%` and beta `1.00` as of 2026-06-30.

## FNDA gaps and conflicts

- Official current NAV/YTD and rolling 10-year fields are available only through 2026-06-30 in the product-page extract; the profile quote/NAV is newer at 2026-07-30 but is not a return metric.
- Schwab's SEC table reports 2024 before-tax return `8.96%`; the secondary annual proxy reports `8.99%`. The values are retained as a source conflict and not silently merged.
- Official annual NAV rows for 2016-2025 were not text-extractable from the issuer bar-chart/factsheet materials, so the common-window annual table remains explicitly secondary.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual proxy observations are rounded values; cumulative and CAGR outputs are rounded-input calculations.

## Scheduled-inline local review

- Status: `PASS`
- Confirmed GSSC, XSMO, SSEUF, and FNDA ticker/exchange, passive classification, inception, expense ratio, issuer benchmark, NAV TR definition, official annual/current fields, secondary annual proxy basis, S&P cache window/basis, best/worst ranking, formulas, source links, graph breadcrumb, region ownership, and unresolved gaps.
- XSMO-specific local checklist: verified the official 2016-2025 annual rows, issuer 10-year average annual field, secondary current NAV snapshot, separate return-basis treatment, predecessor-index continuity note, 8/2 up/down count, and no unsupported drawdown/recovery inference.
- SSEUF-specific local checklist: verified OTC-to-`LSE:R2US` alias mapping, ISIN/share-class currency, passive classification, official 2016-2025 rows, official 10-year/current NAV fields, S&P cache convention, 8/2 up/down count, risk metrics, graph breadcrumb, primary-region ownership, and no unsupported drawdown/recovery inference.
- FNDA-specific local checklist: verified passive/index classification, exchange, inception, fee, current tracked index, official NAV 10Y/YTD fields, secondary annual-row basis, 2024 benchmark splice, 8/2 up/down count, risk metrics, source conflict, graph breadcrumb, primary-region ownership, and no unsupported drawdown/recovery inference.
- ZPRVF-specific local checklist: resolved the OTC input alias to official USD `LSE:USSC` by ISIN `IE00BSPLC413`, verified passive/index-tracking equity classification, inception, TER, accumulation, issuer benchmark, official 2016-2025 Fund Net rows, rolling 10-year NAV TR, current YTD, S&P cache window/basis, current benchmark date mismatch, 8/2 up/down count, risk metrics, graph breadcrumb, USA primary-region ownership, and no unsupported drawdown/recovery inference.
- NUSC-specific local checklist: verified Cboe BZX identity, passive/index classification, inception, 0.31% fee, Nuveen ESG USA Small-Cap Index, official 2017-2025 NAV/index rows, official 2026 YTD NAV/index fields, under-10-year history, SEC best/worst-quarter corroboration, S&P cache window/basis, 7/2 up/down count, HTML/PDF performance-rendering conflict, graph breadcrumb, USA primary-region ownership, and no unsupported drawdown/recovery inference.
- IMWSF-specific local checklist: resolved OTC `IMWSF` to USD `LSE:WSML` by ISIN `IE00BF4RFH31`, verified passive/physical/optimised UCITS structure, inception, TER, accumulating treatment, official 2019-2025 NAV/index rows, current product-page NAV/YTD, factsheet July YTD, S&P cache/current date mismatch, 6/1 up/down count, 3-year standard deviation and beta, graph breadcrumb, International primary-region ownership, and no unsupported drawdown/recovery inference.
- Planned durable files reviewed before save: `wiki/analysis/performance/ETF_NYSE_ARCA_GSSC Performance.md`, `wiki/analysis/performance/ETF_NYSE_ARCA_XSMO Performance.md`, `wiki/analysis/performance/ETF_LSE_R2US Performance.md`, `wiki/analysis/performance/ETF_LSE_USSC Performance.md`, `wiki/analysis/performance/ETF_NYSE_ARCA_FNDA Performance.md`, `wiki/analysis/performance/ETF_CBOE_BZX_NUSC Performance.md`, `wiki/analysis/performance/ETF_LSE_WSML Performance.md`, this source batch, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `wiki/analysis/comparisons/ETF Region Index.md`, and `log.md`.

## ZPRVF / USSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:USSC / input ZPRVF | https://www.ssga.com/ie/en_gb/institutional/etfs/state-street-spdr-msci-usa-small-cap-value-weighted-ucits-etf-zprv-gy | Official State Street product page: fund identity, listings, inception, TER context, official NAV, Fund Net/NAV performance, annual rows, standard deviation and tracking error | Fund performance through 2026-07-31; NAV 2026-08-14; characteristics 2026-08-13 |
| LSE:USSC / input ZPRVF | https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-zprv-gy.pdf | Official State Street factsheet: ISIN, USD LSE ticker, index, inception, TER, accumulation, optimized replication and performance | Factsheet dated 2026-06-30; performance table through 2026-07-31 |
| Input ZPRVF alias | https://stockanalysis.com/quote/otc/ZPRVF/ | Secondary OTC identity/exchange cross-check; not used for NAV TR ranking | OTC ticker identity checked 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current S&P 500 (TR) YTD cross-check | 14.04% as of 2026-08-16; not synchronized with ETF 2026-07-31 YTD and not used in annual table |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached annual reference rows | 2022-2025; reused without a new search |

## ZPRVF / USSC raw observations and calculations

| Year | USSC Fund Net / NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 25.83% | 11.96% |
| 2017 | 9.37% | 21.83% |
| 2018 | -14.31% | -4.38% |
| 2019 | 23.80% | 31.49% |
| 2020 | 8.46% | 18.40% |
| 2021 | 35.40% | 28.71% |
| 2022 | -10.23% | -18.11% |
| 2023 | 21.18% | 26.29% |
| 2024 | 9.67% | 25.02% |
| 2025 | 13.89% | 17.88% |
| 2026 YTD | 20.29% (official Fund Net/NAV) | 14.04% (official current page, as of 2026-08-16; not same date) |

- Metric basis: official State Street Fund Net performance is NAV-based and net of fees; the accumulating USD share class retains income in NAV.
- Issuer benchmark: `MSCI USA Small Cap Value Weighted Index` (Net Total Return); retained as metadata and not substituted for the common S&P 500 reference.
- Official rolling 10-year NAV TR: `213.35%` cumulative / `12.10%` annualized as of 2026-07-31. Because raw NAV endpoints are not disclosed, the performance page uses a normalized index calculation `100.00 → 313.35` over `10.00` years; this is not presented as a raw provider index level.
- 2016-2025 USSC compound: `191.31%` cumulative; rounded-input CAGR `11.28%`.
- 2021-2025 USSC compound: `83.97%` cumulative; rounded-input CAGR `12.97%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk fields: 3-year standard deviation `18.28%` and annualized tracking error `0.07%` as of 2026-07-31; official NAV `US$96.48` as of 2026-08-14.

## ZPRVF / USSC gaps and conflicts

- The input ticker `ZPRVF` is an OTC alias. State Street's official listings for ISIN `IE00BSPLC413` identify the USD line as `LSE:USSC` and the primary EUR line as `Deutsche Börse:ZPRV`; the durable key uses `LSE:USSC` to match the USD share class while preserving the input alias in metadata.
- The latest official ETF YTD field is `20.29%` as of 2026-07-31. The latest official S&P 500 TR page reviewed shows `14.04%` as of 2026-08-16; the as-of dates differ, so the current benchmark figure is disclosed but not used as a same-date annual-table comparator.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations. Market-price observations from different currency listings are not mixed into the NAV Total Return ranking.

## NUSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| Cboe BZX:NUSC | https://documents.nuveen.com/Documents/Nuveen/Viewer.aspx?uniqueId=8238272c-9326-4c32-93cb-40d80e4fc4a9 | Official Nuveen factsheet: identity, passive/indexing approach, exchange, fee, NAV/index calendar returns, current YTD, holdings and risk context | Factsheet as of 2026-06-30; calendar rows 2017-2025; current NAV/index YTD 2026-06-30 |
| Cboe BZX:NUSC | https://www.nuveen.com/en-us/exchange-traded-funds/nusc-nuveen-esg-small-cap-etf | Official product page: identity, methodology, primary exchange, fee, inception, quote/NAV snapshot and current page-rendering check | Product-page quote/NAV as of 2026-06-26; performance component rendered no records in the reviewed capture |
| Cboe BZX:NUSC | https://www.sec.gov/Archives/edgar/data/1635073/000119312526080215/d91437d497k.htm | SEC summary prospectus: listing, objective, fees, index strategy, annual return chart and best/worst quarters | Filed 2026-02-27; annual rows through 2025; best/worst quarter history through 2025-12-31 |
| MSCI Nuveen ESG USA Small-Cap Index | https://www.msci.com/indexes/index/711741/nuveen-esg-usa-small-cap-index | Issuer benchmark identity and index-provider cross-check | Index identity checked 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## NUSC raw observations and calculations

| Year | NUSC NAV TR | Nuveen ESG USA Small-Cap Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2017 | 16.62% | 17.13% | 21.83% |
| 2018 | -9.28% | -8.88% | -4.38% |
| 2019 | 26.82% | 27.37% | 31.49% |
| 2020 | 23.48% | 23.97% | 18.40% |
| 2021 | 17.83% | 18.26% | 28.71% |
| 2022 | -17.68% | -17.55% | -18.11% |
| 2023 | 15.50% | 15.80% | 26.29% |
| 2024 | 8.48% | 8.79% | 25.02% |
| 2025 | 7.60% | 7.85% | 17.88% |
| 2026 YTD | 16.76% (official NAV) | 16.94% (official issuer index) | not available from cached current-year benchmark |

- Metric basis: official Nuveen NAV total return includes reinvested distributions and fund expenses; the issuer index excludes fund expenses.
- Issuer benchmark: `Nuveen ESG USA Small-Cap Index`, calculated by MSCI; retained as metadata and not substituted for the common S&P 500 reference.
- NUSC 2017-2025 compound: `116.65%` cumulative; rounded-input CAGR `8.97%`.
- NUSC 2021-2025 compound: `30.77%` cumulative; rounded-input CAGR `5.51%`.
- Issuer index 2017-2025 compound: `123.26%` cumulative; rounded-input CAGR `9.33%`; 2021-2025 CAGR `5.79%`.
- S&P 500 cached 2017-2025 compound: `255.78%` cumulative; rounded-input CAGR `15.14%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk observations: best quarter `+29.98%` in 4Q2020 and worst quarter `-30.76%` in 1Q2020 from the SEC summary prospectus; official daily NAV history for maximum drawdown/recovery was not verified.

## NUSC gaps and conflicts

- Inception was 13 Dec 2016, so 2016 is a partial inception period and the fund has not reached a full 10-year history as of 2026-06-30; no 10-year NAV CAGR is claimed.
- Nuveen's HTML product page rendered `No Records Available` for the performance component in the reviewed capture, while the official PDF factsheet dated 2026-06-30 supplied numeric calendar/YTD fields; the factsheet is used for performance and the rendering conflict is preserved here.
- The latest official NUSC performance field reviewed is `16.76%` NAV TR YTD as of 2026-06-30; the common S&P cache has no synchronized 2026 current-year row, so no current S&P YTD comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## IMWSF / WSML official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:WSML / input IMWSF | https://www.ishares.com/uk/professionals/en/products/296576/ishares-msci-world-small-cap-ucits-etf-fund?siteEntryPassthrough=true&switchLocale=y | Official iShares product page: USD share-class identity, listings, benchmark, TER, structure, current NAV/YTD, holdings and risk metrics | Current page observations: NAV 2026-08-14; NAV TR YTD 2026-08-13; portfolio/risk fields through 2026-07-31 |
| LSE:WSML / input IMWSF | https://www.ishares.com/gls-download/literature/fact-sheet/wsml-ishares-msci-world-small-cap-ucits-etf-fund-fact-sheet-en-gb.pdf | Official iShares factsheet: ISIN, launch, USD accumulating share class, physical/optimised structure, annual NAV/index rows, July YTD and listings | Factsheet dated July 2026; performance and NAV data as of 2026-07-31; other data as of 2026-08-07 |
| Input IMWSF alias | https://digital.fidelity.com/prgw/digital/research/quote/dashboard/summary?symbol=IMWSF | Secondary OTC alias / ISIN cross-check; not used for NAV Total Return ranking | OTC identity checked 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current S&P 500 TR YTD cross-check | 14.04% as of 2026-08-16; not synchronized with WSML 2026-08-13 YTD |

## IMWSF / WSML raw observations and calculations

| Year | WSML NAV TR | MSCI World Small Cap Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2019 | 25.73% | 26.19% | 31.49% |
| 2020 | 15.83% | 15.96% | 18.40% |
| 2021 | 15.81% | 15.75% | 28.71% |
| 2022 | -18.64% | -18.75% | -18.11% |
| 2023 | 16.02% | 15.76% | 26.29% |
| 2024 | 7.93% | 8.15% | 25.02% |
| 2025 | 19.84% | 19.88% | 17.88% |
| 2026 YTD | 19.00% (official NAV) | not available from same-date official product-page field | 14.04% (official current page, as of 2026-08-16; not same date) |

- Metric basis: official iShares NAV total return is shown on NAV basis with gross income reinvested where applicable; the accumulating USD share class retains income in NAV.
- Issuer benchmark: `MSCI World Small Cap Index (Net)`; retained as metadata and not substituted for the common S&P 500 reference.
- WSML 2019-2025 compound: `105.92%` cumulative; rounded-input CAGR `10.87%`.
- WSML 2021-2025 compound: `41.39%` cumulative; rounded-input CAGR `7.17%`.
- Issuer index 2019-2025 compound: `106.54%` cumulative; rounded-input CAGR `10.92%`; 2021-2025 CAGR `7.14%`.
- S&P 500 cached 2019-2025 compound: `205.41%` cumulative; rounded-input CAGR `17.29%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk fields: 3-year standard deviation `16.16%` and beta `1.000` as of 2026-06-30; holdings `3,558` as of 2026-07-30; official daily NAV history for maximum drawdown/recovery was not verified.

## IMWSF / WSML gaps and conflicts

- The OTC input `IMWSF` is not the canonical issuer listing. Official iShares listings for ISIN `IE00BF4RFH31` identify the USD line as `LSE:WSML`, with additional GBP/CHF/EUR listings; the durable key uses `LSE:WSML` while preserving the input alias.
- Inception was 27 Mar 2018; 2018 is a partial/inception period whose annual return is not disclosed in the reviewed official materials, and no 10-year NAV CAGR is claimed.
- The July factsheet reports NAV YTD `13.88%` as of 2026-07-31 while the newer product page reports `19.00%` as of 2026-08-13; these are separate as-of dates, so the newer product-page field is used as current and both observations are preserved.
- The current official S&P 500 TR page reports `14.04%` as of 2026-08-16, one date after the ETF current YTD; no synchronized current benchmark comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## BBSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Cboe BZX:BBSC` | https://am.jpmorgan.com/us/en/asset-management/adv/products/jpmorgan-betabuilders-us-small-cap-equity-etf-etf-shares-46641q290 | Official JPMorgan product page: identity, objective, tracked index and product context | Page reviewed 2026-08-17; current exchange context cross-checked against SEC materials |
| `Cboe BZX:BBSC` | https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBSC.PDF | Official factsheet: passive approach, benchmark, inception, fee, annual NAV returns, current NAV/market-price/benchmark fields and return basis | Factsheet dated 2026-06-30; annual rows 2021-2025 and current fields as of 2026-06-30 |
| `Cboe BZX:BBSC` | https://www.sec.gov/Archives/edgar/data/1485894/000119312526071799/d46741d497k.htm | SEC summary prospectus: objective, index strategy, fees and passive structure | Filed 2026-03-01; listing and strategy context reviewed 2026-08-17 |
| `Cboe BZX:BBSC` | https://www.sec.gov/Archives/edgar/data/1485894/000119312526128970/d123344d497k.htm | SEC supplement: exchange-transfer notice | Dated 2026-03-27; transfer from NYSE Arca to Cboe BZX effective 2026-04-16 |
| `Cboe BZX:BBSC` | https://www.sec.gov/Archives/edgar/data/1485894/000119312526152486/d134932d8a12b.htm | SEC Form 8-A: current Cboe BZX registration cross-check | Filed 2026-04-16; BBSC registered on Cboe BZX |
| `Cboe BZX:BBSC` | https://am.jpmorgan.com/us/en/asset-management/per/about-us/media/press-releases/jp-morgan-transfer-14-etfs-from-current-exchanges/ | JPMorgan exchange-transfer announcement | Reviewed 2026-08-17 |
| Parent input identity | `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md` | Exact parent backlog row used to disambiguate U.S. BBSC from the Ireland UCITS ticker | Line 16: JPMorgan BetaBuilders U.S. Small Cap Equity ETF, parent input snapshot |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## BBSC raw observations and calculations

| Year | BBSC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 15.55% | 28.71% |
| 2022 | -19.71% | -18.11% |
| 2023 | 20.03% | 26.29% |
| 2024 | 12.37% | 25.02% |
| 2025 | 10.56% | 17.88% |

- Metric basis: official JPMorgan NAV total return assumes dividends and capital gains are reinvested; NAV return reflects fund fees and expenses; currency USD.
- Issuer benchmark: `Morningstar US Small Cap Target Market Exposure Extended Index`; retained as metadata and not substituted for the common S&P 500 reference.
- BBSC 2021-2025 compound: `38.35%` cumulative; rounded-input CAGR `6.71%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Up years / down years: `4 / 1`; best `2021 +15.55%`; least positive `2025 +10.56%`; worst and least bad down year `2022 -19.71%`.
- Current official fields as of 2026-06-30: NAV TR YTD `23.96%`, market-price return `24.13%`, issuer benchmark `24.11%`.

## BBSC gaps and scheduled-inline local review

- The exact parent input row at `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md:16` identifies the intended U.S. fund. This resolves the ticker ambiguity with the Ireland UCITS BBSC listing before saving.
- Current canonical exchange is `Cboe BZX`; the prior NYSE Arca listing and 2026-04-16 transfer are preserved in the SEC source map. No old exchange slug is used for the durable page.
- Inception was 2020-11-16; 2020 is an inception-year partial period and no 10-year NAV CAGR is claimed. Complete annual calculations use official 2021-2025 rows only.
- The latest official current performance fields reviewed are as of 2026-06-30; no synchronized 2026-08-17 official NAV/price snapshot is asserted.
- The common S&P 500 annual cache ends 2025-12-31; no current-year S&P comparison is asserted against BBSC's 2026-06-30 fields.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.
- Planned durable paths: create `wiki/analysis/performance/ETF_CBOE_BZX_BBSC Performance.md`; update `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `USA`; add breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; add `geography/United-States`; link the new page from USA navigation and the performance index; keep annual numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS
## ISCF official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:ISCF` | https://www.ishares.com/us/products/272823/ishares-international-small-cap-equity-factor-etf | Official iShares product page: identity, exchange, benchmark, inception, current NAV/price/YTD, holdings and risk fields | Current NAV/price 2026-08-14; NAV TR YTD 2026-08-13; holdings 2026-08-13; risk fields through 2026-07-31 |
| `NYSE Arca:ISCF` | https://www.ishares.com/us/literature/fact-sheet/iscf-ishares-international-small-cap-equity-factor-etf-fund-fact-sheet-en-us.pdf | Official factsheet: NAV/market-price/benchmark rows 2021-2025, return basis, current benchmark metadata and fund characteristics | Factsheet as of 2026-06-30; 2025 row and annual benchmark rows through 2025 |
| `NYSE Arca:ISCF` | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-edge-msci-multifactor-intl-small-cap-etf-7-31.pdf | Official summary prospectus: passive objective, fees, 2016-2024 calendar NAV rows, best/worst quarters and benchmark splice | Dated 2025-11-28; annual chart through 2024; calendar YTD field in prospectus is stale and not used for current YTD |
| Parent input identity | `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md` | Exact parent backlog row used to confirm the intended iShares fund and current quote snapshot | Line 17: iShares International Small-Cap Equity Factor ETF, input price `46.04` |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## ISCF raw observations and calculations

| Year | ISCF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 0.01% | 11.96% |
| 2017 | 36.24% | 21.83% |
| 2018 | -18.18% | -4.38% |
| 2019 | 25.94% | 31.49% |
| 2020 | 7.89% | 18.40% |
| 2021 | 13.22% | 28.71% |
| 2022 | -15.06% | -18.11% |
| 2023 | 11.52% | 26.29% |
| 2024 | 4.33% | 25.02% |
| 2025 | 34.07% | 17.88% |

- Metric basis: official iShares NAV total return assumes reinvestment of dividends/capital gains and deducts fund expenses; currency USD.
- Issuer benchmark annual rows in the June 2026 factsheet for 2021-2025 are `13.43%`, `-15.01%`, `11.75%`, `4.67%`, and `33.75%`; they are retained as issuer metadata and not substituted for the common S&P 500 reference.
- Benchmark splice: historical index data before 2023-03-01 is `MSCI World ex USA Small Cap Diversified Multiple-Factor Index (Net)`; data from 2023-03-01 is `STOXX International Small-Cap Equity Factor Index (Net)`.
- ISCF 2016-2025 compound: `127.24%` cumulative; rounded-input CAGR `8.55%`.
- ISCF 2021-2025 compound: `50.01%` cumulative; rounded-input CAGR `8.45%`.
- Issuer rolling 10-year NAV TR average annual: `9.69%` as of 2026-06-30; raw rolling endpoints are not disclosed and this is not substituted for the calendar-window CAGR.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Up years / down years: `8 / 2`; best `2017 +36.24%`; least positive `2016 +0.01%`; worst `2018 -18.18%`; least bad down year `2022 -15.06%`.
- Current official fields: NAV TR YTD `12.52%` as of 2026-08-13; NAV `US$45.93` and closing price `US$46.04` as of 2026-08-14; 3-year standard deviation `14.21%` and beta `0.73` as of 2026-07-31; holdings `1,161` as of 2026-08-13.

## ISCF gaps, benchmark splice, and scheduled-inline local review

- The exact parent input row at `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md:17` identifies the intended iShares International Small-Cap Equity Factor ETF; no ticker alias conflict was found.
- The annual evidence is intentionally spliced by source date: SEC summary prospectus rows for 2016-2024 and the June 2026 official factsheet row for 2025. The overlapping 2021-2024 NAV rows reconcile exactly.
- The issuer benchmark changed on 2023-03-01 from the MSCI World ex USA Small Cap Diversified Multiple-Factor Index (Net) to the STOXX International Small-Cap Equity Factor Index (Net); this is preserved and not treated as a homogeneous single-index history.
- The latest official current NAV TR field reviewed is `12.52%` as of 2026-08-13; the common S&P cache has no synchronized 2026 current-year row, so no current S&P comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.
- Planned durable paths: create `wiki/analysis/performance/ETF_NYSE_ARCA_ISCF Performance.md`; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `International`; add breadcrumb `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`; add `geography/International` and `geography/international-ex-US`; link the new page from International navigation and the performance index; keep annual numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## ISCV official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:ISCV` | https://www.ishares.com/us/products/239588/ishares-morningstar-smallcap-value-etf | Official iShares product page: identity, passive objective, exchange, benchmark, current NAV/YTD, price/NAV, holdings, AUM and risk fields | NAV TR YTD 2026-08-13; NAV/price, holdings and AUM 2026-08-14; risk fields through 2026-07-31 |
| `NYSE Arca:ISCV` | https://www.ishares.com/ch/professionals/en/products/239588/ishares-morningstar-smallcap-value-etf?switchLocale=Y | Official iShares calendar-performance page: 2016-2025 NAV and issuer-benchmark rows, return-basis context and listing metadata | Page reviewed 2026-08-17; annual rows displayed to one decimal; listing date 2004-06-28 |
| `NYSE Arca:ISCV` | https://www.ishares.com/us/literature/fact-sheet/iscv-ishares-morningstar-small-cap-value-etf-fund-fact-sheet-en-us.pdf | Official factsheet: 2021-2025 NAV/market-price/benchmark rows, rolling annualized performance, fee, holdings and risk cross-check | Factsheet as of 2026-06-30; 10-year NAV TR average annual `9.22%`; 3-year standard deviation `18.27%` and beta `1.03` on that factsheet date |
| `NYSE Arca:ISCV` | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-morningstar-small-cap-value-etf-4-30.pdf | Official summary prospectus: passive investment objective, exchange, fees and risk context | Dated 2025-08-29; reviewed 2026-08-17 |
| Parent input identity | `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md` | Exact parent backlog row used to confirm the intended iShares fund and input quote | Line 19: iShares Morningstar Small-Cap Value ETF, input price `81.79` |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## ISCV raw observations and calculations

| Year | ISCV NAV TR | ISCV issuer benchmark | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 27.80% | 28.00% | 11.96% |
| 2017 | 8.10% | 8.40% | 21.83% |
| 2018 | -16.80% | -16.60% | -4.38% |
| 2019 | 19.50% | 20.00% | 31.49% |
| 2020 | 0.70% | 1.00% | 18.40% |
| 2021 | 29.20% | 29.20% | 28.71% |
| 2022 | -10.50% | -10.40% | -18.11% |
| 2023 | 16.40% | 16.30% | 26.29% |
| 2024 | 9.20% | 9.30% | 25.02% |
| 2025 | 10.50% | 10.50% | 17.88% |

- Metric basis: official iShares NAV total return is shown with gross income reinvested where applicable and fund expenses deducted; currency USD. Market-price return and issuer-benchmark return remain separate.
- Issuer benchmark: `Morningstar US Small Cap Broad Value Extended Index`; it is retained as metadata and not substituted for the common S&P 500 reference.
- ISCV 2016-2025 compound from official one-decimal NAV rows: `124.65%` cumulative; rounded-input CAGR `8.43%`.
- ISCV 2021-2025 compound from the same official NAV rows: `62.41%` cumulative; rounded-input CAGR `10.19%`.
- Issuer rolling 10-year NAV TR average annual: `9.22%` as of 2026-06-30; raw endpoints are not disclosed and this is not substituted for the calendar-window CAGR.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Up years / down years: `8 / 2`; best `2021 +29.20%`; least positive `2020 +0.70%`; worst `2018 -16.80%`; least bad down year `2022 -10.50%`.
- Current official fields: NAV TR YTD `20.34%` as of 2026-08-13; NAV `US$81.86`, closing price `US$81.78`, premium/discount `-0.10%`, holdings `1,049`, and AUM `US$712.17M` as of 2026-08-14; 3-year standard deviation `17.95%` and beta `1.01` as of 2026-07-31.

## ISCV gaps and scheduled-inline local review

- The exact parent input row at `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md:19` identifies the intended iShares Morningstar Small-Cap Value ETF; canonical listing is `NYSE Arca:ISCV`.
- The official iShares page displays 2016-2025 calendar NAV rows to one decimal; the June 2026 factsheet overlaps 2021-2025 and reconciles to those rows. Cumulative returns and CAGRs are rounded-input calculations.
- The issuer 10-year annualized field `9.22%` is a separate official average annual observation for the period ended 2026-06-30; raw endpoints are not disclosed, so it is not relabeled as the 2016-2025 calendar CAGR.
- The current NAV TR field is as of 2026-08-13 while price/NAV and holdings are as of 2026-08-14; dates remain separate. The common S&P cache ends 2025-12-31, so no current-year S&P comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Planned durable paths: create `wiki/analysis/performance/ETF_NYSE_ARCA_ISCV Performance.md`; update `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `USA`; add breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; add `geography/United-States`; link the new page from USA navigation and the performance index; keep annual numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## GWX official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:GWX` | https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-international-small-cap-etf-gwx | Official State Street product page: identity, passive objective, exchange, inception, tracked index and performance context | Page reviewed 2026-08-17; current product-page quote snapshot was not used as a current price claim |
| `NYSE Arca:GWX` | https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-gwx.pdf | Official factsheet: NAV/market-value/index standardized performance, return basis, expense ratio and holdings | Factsheet as of 2026-06-30; YTD NAV TR `8.18%`, market-value return `8.52%`, issuer-index return `6.77%`, holdings `2,083` |
| `NYSE Arca:GWX` | https://www.sec.gov/Archives/edgar/data/1168164/000119312526031217/d833468d497k.htm | SEC summary prospectus: passive sampling strategy, risks, 2025 year-end average annual returns and best/worst quarters | Filed 2026-01-30; 10-year NAV TR `7.00%` through 2025-12-31; best quarter `+20.78%` Q2 2020; worst quarter `-28.37%` Q1 2020 |
| Parent input identity | `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md` | Exact parent backlog row used to confirm the intended State Street fund and input quote | Line 18: State Street SPDR S&P International Small Cap ETF, input price `46.53` |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| Secondary annual history | https://assetsanalyzer.com/etf/GWX/performance | Secondary total-return proxy reviewed only to test issuer coverage; not saved because it conflicts with official source data | Annual table displayed 2016-2025; 2025 secondary `35.86%` versus official prospectus NAV `35.00%` through 2025-12-31 |

## GWX raw observations and calculations

| Year | GWX NAV TR | S&P 500 TR |
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

- Metric basis: official State Street NAV total return includes reinvested distributions and is net of fund expenses; market-value and index fields remain separate; currency USD.
- Issuer benchmark: `S&P Developed Ex-U.S. Under USD2 Billion Index`; it is retained as metadata and not substituted for the common S&P 500 reference.
- Official factsheet period returns as of 2026-06-30: QTD NAV `7.26%`, YTD NAV `8.18%`, 1-year NAV `21.24%`, 3-year NAV `15.84%`, 5-year NAV `5.32%`, and 10-year NAV `7.58%`.
- GWX 10-year NAV TR average annual: `7.58%` from the official factsheet as of 2026-06-30; raw endpoints and exact elapsed years are not disclosed, so no independent endpoint CAGR is calculated.
- The SEC prospectus reports a separate 10-year NAV TR average annual `7.00%` through 2025-12-31; the two observations have different as-of dates and are not combined.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`; it is shown only as the common reference table because GWX annual NAV rows are not disclosed.
- 2021-2025 CAGR, up/down counts, best/least-positive/worst/least-bad years, maximum drawdown and recovery: not disclosed; no secondary proxy is saved.
- Formula retained for any eligible calendar window: `CAGR = product(1 + annual return)^(1 / number of years)`; no GWX calendar CAGR is produced from the conflicting secondary table.

## GWX gaps, conflict, and scheduled-inline local review

- The exact parent input row at `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md:18` identifies the intended State Street fund; canonical listing is `NYSE Arca:GWX`.
- The official issuer materials reviewed provide rolling/period NAV returns but do not expose complete 2016-2025 calendar NAV rows or raw 10-year endpoints. The official 10-year factsheet field is retained as an issuer average annual fact, not relabeled as a recomputed CAGR.
- The reviewed secondary annual table is explicitly excluded because its 2025 result `35.86%` conflicts with the official SEC prospectus NAV result `35.00%` through the same year-end. No mixed-basis cumulative return, 2021-2025 CAGR, or year ranking is asserted.
- The latest synchronized official GWX performance fields reviewed are as of 2026-06-30; the common S&P cache ends 2025-12-31 and no current-year S&P comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Planned durable paths: create `wiki/analysis/performance/ETF_NYSE_ARCA_GWX Performance.md`; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `International`; add breadcrumb `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`; add `geography/International` and `geography/international-ex-US`; link the new page from International navigation and the performance index; keep annual numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## JPSE official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:JPSE` | https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-JPSE.PDF | Official JPMorgan factsheet: identity, passive/index objective, inception, expense ratio, NAV/market-price performance, annual rows and risk statistics | Factsheet dated 2026-06-30; NAV YTD `20.41%`, market-price YTD `20.71%`, annual rows 2017-2025, 3-year standard deviation `17.63%` |
| `NYSE Arca:JPSE` | https://www.sec.gov/Archives/edgar/data/1485894/000119312526071849/d58277d497k.htm | Official SEC summary prospectus: passive indexing approach, index construction, expenses, listing and risks | Prospectus dated 2026-03-01; management/total annual expenses `0.29%`; listing exchange NYSE Arca; fund uses at least 80% of assets in underlying index securities |
| `NYSE Arca:JPSE` | https://www.sec.gov/Archives/edgar/data/1485894/000119312525336832/d43117dncsr.htm | Official SEC annual shareholder report cross-check | Report period ended 2025-10-31; expense ratio `0.29%`; confirms ticker/exchange and annual report identity |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## JPSE raw observations and calculations

| Year | JPSE NAV TR | S&P 500 TR |
|---|---:|---:|
| 2017 | 14.38% | 21.83% |
| 2018 | -8.14% | -4.38% |
| 2019 | 22.67% | 31.49% |
| 2020 | 12.62% | 18.40% |
| 2021 | 29.14% | 28.71% |
| 2022 | -14.42% | -18.11% |
| 2023 | 15.77% | 26.29% |
| 2024 | 8.13% | 25.02% |
| 2025 | 8.95% | 17.88% |
| 2026 YTD | 20.41% (official NAV TR, 2026-06-30) | not synchronized; common cached annual series only |

- Metric basis: official JPMorgan NAV Total Return with dividends and capital gains reinvested; NAV total return assumes fund management fees and operating expenses.
- Issuer benchmark: `JP Morgan Diversified Factor US Small Cap Equity Index`; the fund uses a rules-based value, momentum and quality selection process with risk allocation across sectors and securities. Russell 3000 is the regulatory index and Russell 2000 is an additional comparison index.
- JPSE 2017-2025 compound: `118.79%` cumulative; rounded-input CAGR `9.09%`.
- JPSE 2021-2025 compound: `50.73%` cumulative; rounded-input CAGR `8.55%`.
- Issuer launch-to-date average annual NAV TR: `11.09%` as of 2026-06-30; this is not a 10-year rolling field because the fund history is under ten years at the factsheet date.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`; normalized available-window start TR value `100.00` and rounded-input end TR value `218.79` over nine complete calendar years.
- Annual-return volatility: population standard deviation `12.98%` across the nine official rounded annual NAV observations.
- Up years / down years: `7 / 2`; best `2021 +29.14%`; least positive `2024 +8.13%`; worst `2022 -14.42%`; least bad down year `2018 -8.14%`.
- Current official fields: NAV TR YTD `20.41%`, market-price return YTD `20.71%`, 3-month NAV TR `15.08%`, 1-year NAV TR `34.08%`, launch annualized NAV TR `11.09%`, and 3-year standard deviation `17.63%`, all as of 2026-06-30; gross/net expenses `0.29%` and value of investments `$593.73M` are also as of 2026-06-30.

## JPSE gaps and scheduled-inline local review

- Canonical identity is `NYSE Arca:JPSE`; the input card title and ticker resolve to the JPMorgan Diversified Return U.S. Small Cap Equity ETF.
- JPSE is within ETF v1 scope: the SEC prospectus describes a passive/indexing approach targeting the JP Morgan Diversified Factor US Small Cap Equity Index; no active, leveraged, inverse, bond, commodity, multi-asset or derivative-heavy structure was found. Futures use is capped at 10% of assets and does not change the passive classification.
- Official calendar rows begin in 2017 because the fund launched on 2016-11-15; no partial 2016 row is mixed into a complete-year CAGR. The available 2017-2025 result is explicitly marked history under ten years.
- The issuer launch annualized field `11.09%` is retained separately from the 2017-2025 calendar CAGR; no 10-year issuer average is asserted.
- The common S&P 500 comparison uses the cached annual convention for 2017-2025 and 2021-2025; no same-date 2026 current benchmark pair is asserted against the JPSE 2026-06-30 YTD value.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Planned durable paths: create `wiki/analysis/performance/ETF_NYSE_ARCA_JPSE Performance.md`; update `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `USA`; add breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; add `geography/United-States`; link the new page from USA navigation and the performance index; keep annual numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## XSVM official and secondary source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:XSVM` | https://www.invesco.com/us/en/financial-products/etfs/invesco-sp-smallcap-value-with-momentum-etf.html | Official Invesco product page: fund identity, passive/index objective, exchange, inception, fee, 90% index-investment policy, portfolio size and historical underlying-index transitions | Product page reviewed 2026-08-17; inception 2005-03-03; total/net expense ratio `0.37%`; management fee `0.29%` |
| `NYSE Arca:XSVM` | https://www.invesco.com/us-rest/contentdetail?contentId=118407c649400410VgnVCM10000046f1bf0aRCRD&dnsName=us | Official Invesco Q1-2026 performance material: complete 2016-2025 calendar NAV rows and issuer current snapshot | As of 2026-03-31; official NAV YTD `4.49%`; official NAV annual rows cover 2016-2025 |
| `S&P SmallCap 600 High Momentum Value Index` | https://www.spglobal.com/spdji/en/indices/dividends-factors/sp-smallcap-600-high-momentum-value-index/ | Official S&P index identity and linked-product confirmation | Index page reviewed 2026-08-17; index measures 120 S&P SmallCap 600 stocks with attractive valuations and momentum overlay |
| `NYSE Arca:XSVM` | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=xsvm | Secondary performance cross-check for the latest month-end NAV/market-price YTD and current quote | As of 2026-06-30: NAV YTD `23.00%`, market-price YTD `22.90%`; quote `US$71.88` as of 2026-08-05; used with secondary marker only |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## XSVM raw observations and calculations

| Year | XSVM NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 35.52% | 11.96% |
| 2017 | 3.17% | 21.83% |
| 2018 | -11.82% | -4.38% |
| 2019 | 29.95% | 31.49% |
| 2020 | 5.03% | 18.40% |
| 2021 | 56.38% | 28.71% |
| 2022 | -13.55% | -18.11% |
| 2023 | 20.23% | 26.29% |
| 2024 | 2.12% | 25.02% |
| 2025 | 7.59% | 17.88% |
| 2026 YTD | 23.00% (secondary NAV, 2026-06-30) | not synchronized; common cached annual series only |

- Metric basis: official Invesco NAV Total Return with distributions reinvested and fund expenses reflected; secondary current YTD is explicitly kept separate from the official 2026-03-31 issuer snapshot.
- Issuer benchmark: `S&P SmallCap 600 High Momentum Value Index`; the product page says the fund generally invests at least 90% of assets in index constituents and rebalances/reconstitutes semi-annually.
- XSVM 2016-2025 compound: `200.51%` cumulative; rounded-input CAGR `11.63%`.
- XSVM 2021-2025 compound: `78.58%` cumulative; rounded-input CAGR `12.30%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`; cached 2021-2025 compound `96.17%` / CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`; normalized start TR value `100.00` and rounded-input end TR value `300.51` over ten complete calendar years.
- Annual-return volatility: population standard deviation `20.87%` across the ten official rounded annual NAV observations.
- Up years / down years: `8 / 2`; best `2021 +56.38%`; least positive `2024 +2.12%`; worst `2022 -13.55%`; least bad down year `2018 -11.82%`.
- Current fields: secondary NAV TR YTD `23.00%`, secondary market-price YTD `22.90%`, 1-year NAV `36.70%`, 3-year NAV `16.70%`, 5-year NAV `8.50%`, and since-inception NAV `9.30%`, all from the 2026-06-30 secondary page; official issuer NAV YTD was `4.49%` as of 2026-03-31.

## XSVM gaps, benchmark history, and scheduled-inline local review

- Canonical identity is `NYSE Arca:XSVM`; the input card title and ticker resolve to the Invesco S&P SmallCap Value with Momentum ETF.
- XSVM is within ETF v1 scope: Invesco describes it as an index-based fund tracking the S&P SmallCap 600 High Momentum Value Index and investing at least 90% in index constituents; no active, leveraged, inverse, bond, commodity, multi-asset or derivative-heavy structure was found.
- The issuer reports historical underlying-index changes: Dynamic Small Cap Value Intellidex before 2011-06-16, RAFI Fundamental Small Value through 2015-05-22, Russell 2000 Pure Value through 2019-06-21, and S&P SmallCap 600 High Momentum Value thereafter. Fund NAV annual rows remain the numeric source of truth; index-relative comparisons are not treated as a single uninterrupted benchmark history.
- Latest 2026-06-30 YTD is a secondary Schwab NAV observation because the latest official Invesco performance material located is as of 2026-03-31. The page preserves both as-of dates and does not present the secondary number as an issuer disclosure.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Planned durable paths: create `wiki/analysis/performance/ETF_NYSE_ARCA_XSVM Performance.md`; update `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `USA`; add breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; add `geography/United-States`; link the new page from USA navigation and the performance index; keep annual numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## OSCV official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| Cboe BZX:OSCV | https://aptusetfs.com/oscv/ | Official Aptus product page: fund identity, active objective, exchange, current NAV/market price, expense ratio, distributions and rolling performance | Page reviewed 2026-08-17; fund details and price/NAV as of 2026-08-14; monthly performance and YTD through 2026-07-31 |
| Cboe BZX:OSCV | https://f.hubspotusercontent20.net/hubfs/4896827/Content%20Hub/Fact%20Sheets%20and%20Performance/ETF%20Fact%20Sheets/OSCV%20Fact%20Sheet.pdf | Official Aptus factsheet: calendar NAV returns, S&P 600 Value comparison, expense, inception, capture and risk fields | Factsheet as of 2026-06-30; NAV calendar rows 2018-2025; 3-year standard deviation OSCV 18.67% vs S&P 600 Value 24.00% |
| Cboe BZX:OSCV | https://www.sec.gov/Archives/edgar/data/1540305/000089418925006694/opussmallcapvalueetfsummary.htm | Official SEC summary prospectus: listing, active long-only eligibility, strategy, adviser/team, management benchmark, turnover and risks | Prospectus dated 2025-08-31; inception 2018-07-17; portfolio turnover 25% for fiscal year ended 2025-04-30; managers since 2019/2020 |
| Cboe BZX:OSCV | https://aptusetfs.com/wp-content/uploads/2025/06/OSCV-4.30.25-TSR-Final-Web-Ready-Public.pdf | Official annual shareholder report: turnover and standardized performance cross-check | Fiscal year ended 2025-04-30; portfolio turnover 25%; 30-day SEC yield 1.47% as of 2025-04-30 |
| S&P SmallCap 600 Value TR | https://www.spglobal.com/spdji/en/indices/equity/sp-smallcap-600-value/ | Official index identity and value methodology; management-benchmark context | Page reviewed 2026-08-17; index classifies S&P SmallCap 600 constituents using book value, earnings and sales to price |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## OSCV raw observations and calculations

| Year / window | OSCV NAV TR | S&P 500 TR | S&P SmallCap 600 Value TR | Active return vs management benchmark |
|---|---:|---:|---:|---:|
| 2018 inception partial† | -12.66% | -4.38% | -20.60% | not comparable; excluded |
| 2019 | 27.45% | 31.49% | 24.50% | +2.95 pp |
| 2020 | 4.88% | 18.40% | 2.48% | +2.40 pp |
| 2021 | 27.89% | 28.71% | 30.85% | -2.96 pp |
| 2022 | -11.36% | -18.11% | -11.09% | -0.27 pp |
| 2023 | 10.13% | 26.29% | 14.88% | -4.75 pp |
| 2024 | 11.44% | 25.02% | 7.55% | +3.89 pp |
| 2025 | 1.42% | 17.88% | 6.71% | -5.29 pp |
| 2021-2025 cumulative | 41.10% | 96.17% | 53.39% | — |
| 2026 YTD | 15.53% (official NAV, 2026-07-31) | not synchronized | not synchronized | — |

- Metric basis: official Aptus NAV Total Return includes reinvested distributions and fund expenses; market-price return remains separate. Currency is USD.
- Complete 2019-2025 compound: OSCV cumulative 88.61%, rounded-input CAGR 9.49%; S&P SmallCap 600 Value TR cumulative 95.70%, CAGR 10.07%; Excess CAGR -0.58 pp.
- Complete 2019-2025 cumulative relative wealth: (1 + 88.61%) / (1 + 95.70%) - 1 = -3.62%.
- Complete-year hit rate: 3 / 7 = 42.86%; zero active return would not count as outperformance.
- Common 2021-2025 compound: OSCV 41.10% / CAGR 7.13%; S&P 500 TR 96.17% / CAGR 14.43%.
- Annual-return volatility: population standard deviation 13.00% across complete 2019-2025 OSCV rows.
- Current issuer fields: NAV YTD 15.53%, 1-year NAV 17.99%, 3-year annualized NAV 10.20%, 5-year annualized NAV 6.81%, since-inception cumulative 90.35%, since-inception annualized 8.34%, all as of 2026-07-31; NAV US$43.25 and market price US$43.24 as of 2026-08-14.
- Latest four cash distributions shown by Aptus: $0.1171 (2026-06-29), $0.0582 (2026-03-30), $0.1547 (2025-12-30), $0.1161 (2025-09-29); average $0.1115 per round and approximate per-round yield 0.26% using the 2026-08-14 market price. The issuer 30-day SEC yield was 1.24% as of 2026-06-30.
- Management-benchmark selection: the SEC prospectus explicitly calls S&P SmallCap 600 Value TR a more applicable comparison; S&P 500 is retained as the common reference benchmark. No alternative was selected after observing performance.

## OSCV gaps and scheduled-inline local review

- Canonical identity is Cboe BZX:OSCV; SEC materials confirm Cboe BZX listing and the Aptus page confirms Cboe as primary exchange. The factsheet one-day inception date 2018-07-18 conflicts with the product page/SEC 2018-07-17 and is retained rather than silently normalized.
- OSCV is within supported ETF scope as an actively managed, long-only equity ETF: the official prospectus requires at least 80% in U.S. small-cap equity securities and describes common stocks, REITs and ADRs; no payoff-defining options, leverage, inverse, bond, commodity or derivative-heavy structure was found.
- active_process: fundamental-active reflects the disclosed combination of factor-based analysis and rigorous fundamental research; the official sell discipline and named adviser/team are retained.
- The official annual table exposes 2018-2025, but 2018 is an inception-year partial and excluded from rankings, CAGR and active evidence. Complete comparable years are 2019-2025.
- Daily NAV history sufficient for maximum drawdown and recovery was not verified. Current S&P 500 YTD was not paired with OSCV 2026-07-31 YTD because a same-date official benchmark observation was not captured.
- Planned durable paths: created wiki/analysis/performance/ETF_CBOE_BZX_OSCV Performance.md; updated wiki/analysis/comparisons/USA ETF.md, wiki/analysis/comparisons/ETF Region Index.md, wiki/analysis/performance/ETF Performance Index.md, this source batch, and log.md.
- Planned graph changes: primary region USA; breadcrumb [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]; canonical tag geography/United-States; all affected wikilinks resolve to existing/planned targets.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## SMIN official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| Cboe BZX:SMIN | https://www.ishares.com/us/products/239660/ishares-msci-india-smallcap-etf?fundSearch=true&qt=SMIN | Official iShares product and performance page: fund identity, exchange, tracked index, current NAV/market price, holdings, yield, risk fields and rolling performance | Page reviewed 2026-08-17; NAV TR YTD through 2026-08-13; NAV US$71.42 and closing price US$71.43 as of 2026-08-14; 461 holdings as of 2026-08-13; 3-year standard deviation 18.82% as of 2026-07-31 |
| Cboe BZX:SMIN | https://www.ishares.com/us/literature/fact-sheet/smin-ishares-msci-india-small-cap-etf-fund-fact-sheet-en-us.pdf | Official iShares factsheet: NAV calendar returns, benchmark comparison, rolling returns, expense ratio and risk fields | Factsheet as of 2026-06-30; NAV calendar rows 2021-2025; benchmark calendar rows 2021-2025; rolling 10-year NAV TR CAGR 9.71%; current YTD field -0.02% as of 2026-06-30 |
| Cboe BZX:SMIN | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-india-small-cap-etf-8-31.pdf | Official iShares summary prospectus: strategy, index, listing, inception, expenses and annual performance chart | Prospectus dated 2025-08-31; inception 2012-02-08; annual NAV rows 2015-2024; expense ratio 0.74%; fund is non-diversified and index-tracking |
| MSCI India Small Cap Index (Net) | https://www.msci.com/documents/10199/255599/msci-india-small-cap-index.pdf | Official index factsheet and benchmark identity | Index factsheet reviewed 2026-08-17; issuer benchmark retained as MSCI India Small Cap Index (Net) |
| Cboe BZX:SMIN | https://www.cboe.com/us/equities/listings/listed_products/symbols/SMIN/ | Exchange listing cross-check | Listing page reviewed 2026-08-17; Cboe BZX:SMIN |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return with dividends reinvested; cached annual convention as of 2025-12-31 |

## SMIN raw observations and calculations

| Year / window | SMIN NAV TR | S&P 500 TR | MSCI India Small Cap Index (Net) | SMIN active return vs issuer benchmark |
|---|---:|---:|---:|---:|
| 2015 | 2.02% | not captured in cached window | not disclosed in captured source | not disclosed |
| 2016 | -0.42% | 11.96% | not disclosed in captured source | not disclosed |
| 2017 | 61.78% | 21.83% | not disclosed in captured source | not disclosed |
| 2018 | -25.43% | -4.38% | not disclosed in captured source | not disclosed |
| 2019 | -5.17% | 31.49% | not disclosed in captured source | not disclosed |
| 2020 | 19.07% | 18.40% | not disclosed in captured source | not disclosed |
| 2021 | 44.69% | 28.71% | 51.13% | -6.44 pp |
| 2022 | -13.98% | -18.11% | -13.43% | -0.55 pp |
| 2023 | 34.80% | 26.29% | 42.63% | -7.83 pp |
| 2024 | 17.34% | 25.02% | 22.63% | -5.29 pp |
| 2025 | -6.82% | 17.88% | -7.92% | +1.10 pp |
| 2021-2025 cumulative | 83.44% | 96.17% | 110.71% | — |
| 2026 YTD | 2.50% (official NAV, 2026-08-13) | not synchronized | not synchronized | — |

- Metric basis: official iShares NAV Total Return includes reinvested distributions and fund expenses; market-price return remains separate. Currency is USD.
- Complete 2015-2025 compound from the displayed official annual rows: SMIN cumulative 153.86%, rounded-input CAGR 8.84%; population standard deviation 25.45%; up years / down years 6 / 5.
- Common 2021-2025 compound: SMIN 83.44% / CAGR 12.90%; S&P 500 TR 96.17% / CAGR 14.43%; MSCI India Small Cap Index (Net) 110.71% / CAGR 16.07%.
- Five-year benchmark-relative evidence: annual excess returns -6.44, -0.55, -7.83, -5.29 and +1.10 percentage points; excess CAGR -3.17 pp; hit rate 1 / 5 = 20%. This is tracking evidence, not alpha.
- Current issuer fields: NAV TR YTD 2.50% as of 2026-08-13; NAV US$71.42 and closing price US$71.43 as of 2026-08-14; 30-day SEC yield -0.07% as of 2026-07-31; 12-month yield 0.00%; 461 holdings as of 2026-08-13; 3-year standard deviation 18.82% as of 2026-07-31; beta 0.46 as of 2026-07-31.
- Standardized June 2026 page fields remain separate: 2026 YTD NAV -0.02% and MSCI India Small Cap Index (Net) +1.08% as of 2026-06-30; no same-date benchmark pairing was captured for the later 2026-08-13 YTD observation.

## SMIN gaps and scheduled-inline local review

- Canonical identity is Cboe BZX:SMIN; the iShares page and Cboe listing confirm the exchange, while the iShares prospectus confirms the 2012-02-08 inception and MSCI India Small Cap Index (Net) strategy.
- SMIN is within supported ETF scope as a passive, index-tracking, long-only equity ETF. No leverage, inverse, bond, commodity, covered-call, option-income or derivative-heavy structure was found in the official materials.
- The official annual table exposes 2015-2024 in the summary prospectus and 2025 in the June 2026 factsheet; no secondary annual return was substituted. The strict common issuer comparison remains 2021-2025.
- Current 2026-08-13 NAV YTD has no same-date official benchmark pair in the captured sources; the standardized 2026-06-30 page is retained separately.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; no numeric drawdown proxy is saved.
- Planned durable paths: refreshed wiki/analysis/performance/ETF_CBOE_BZX_SMIN Performance.md; updated wiki/analysis/comparisons/India ETF.md, wiki/analysis/performance/ETF Performance Index.md, this source batch, and log.md.
- Planned graph changes: primary region India; breadcrumb [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]; canonical tag geography/India; all affected wikilinks resolve to existing targets.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## SMDV official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| Cboe BZX:SMDV | https://www.proshares.com/our-etfs/strategic/smdv | Official ProShares product page: identity, current index, exchange, rolling performance, NAV/market price, expense, yield and future index/name notice | Page reviewed 2026-08-17; rolling returns as of 2026-07-31; NAV/market price as of 2026-08-14; scheduled transition notice dated 2026-07-13 |
| Cboe BZX:SMDV | https://www.proshares.com/globalassets/proshares/fact-sheet/prosharesfactsheetsmdv.pdf | Official factsheet: fund identity, index, current rolling NAV/market-price/index returns and fund risk language | Factsheet as of 2026-06-30; NAV YTD 17.74%, 1-year 21.31%, 3-year annualized 12.21%, 5-year annualized 6.68%, 10-year annualized 7.54%, since-inception 8.33% |
| Cboe BZX:SMDV | https://www.proshares.com/globalassets/proshares/prospectuses/smdv_summary_prospectus.pdf | Official summary prospectus: passive objective, index construction, fees, inception, risks and annual NAV chart | Supplement dated 2026-07-13; summary prospectus dated 2025-09-26; official annual NAV rows 2016-2024; expense ratio 0.40%; inception 2015-02-03 |
| Cboe BZX:SMDV | https://www.proshares.com/globalassets/proshares/attribution-reports/smdv_review.pdf | Official ProShares attribution report: 2025 calendar NAV/index return and rolling tracking comparison | As of 2025-12-31; 2025 NAV 0.34% vs index 0.72%; 3-year 5.36% vs 5.75%; 5-year 5.59% vs 5.99%; 10-year 7.51% vs 7.97%; since inception 7.11% vs 7.56% |
| Cboe BZX:SMDV | https://www.proshares.com/globalassets/proshares/documents/annual-reports/annual_smdv.pdf | Official annual shareholder report: fiscal-year return, index comparison, volatility and fund statistics | Period ended 2026-05-31; fund total return 15.71% vs index 16.17%; index volatility 15.76%; turnover 36% |
| S&P SmallCap 600 Dividend Aristocrats Index | https://www.proshares.com/globalassets/proshares/prospectuses/smdv_summary_prospectus.pdf | Official future-transition notice: scheduled replacement index and new fund name | Expected effective date around 2026-09-28; current Russell 2000 Dividend Growth Index remains the active benchmark as of 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## SMDV raw observations and calculations

| Year / window | SMDV NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.03% | 11.96% |
| 2017 | 8.89% | 21.83% |
| 2018 | -5.79% | -4.38% |
| 2019 | 19.11% | 31.49% |
| 2020 | -4.93% | 18.40% |
| 2021 | 17.37% | 28.71% |
| 2022 | -0.71% | -18.11% |
| 2023 | 4.70% | 26.29% |
| 2024 | 35.57% | 25.02% |
| 2025 | 0.34% | 17.88% |
| 2021-2025 cumulative | 65.98% | 96.17% |
| 2026 YTD | 18.13% (official NAV, 2026-07-31) | not synchronized |

- Metric basis: official ProShares NAV Total Return includes reinvested distributions and fund expenses; market-price return remains separate. Currency is USD.
- Complete 2016-2025 compound: SMDV cumulative 106.36%, rounded-input CAGR 7.51%; normalized start TR value 100.00 and end TR value 206.36.
- Common 2021-2025 compound: SMDV cumulative 65.98%, rounded-input CAGR 10.66%; S&P 500 TR cumulative 96.17%, CAGR 14.43%.
- Annual-return volatility: population standard deviation 12.15% across the ten official annual NAV observations.
- Up years / down years: 7 / 3; best 2024 +35.57%; least positive 2025 +0.34%; worst 2018 -5.79%; least bad down year 2022 -0.71%.
- Current issuer fields as of 2026-07-31: NAV TR YTD 18.13%, 1-year 22.23%, 3-year annualized 10.42%, 5-year annualized 7.01%, rolling 10-year annualized 7.41%, and since-inception annualized 8.29%; NAV 78.71 and market price 78.76 as of 2026-08-14.
- Yield fields: 30-day SEC yield 2.56% as of 2026-06-30 and 12-month yield 2.28% as of 2026-07-31; quarterly distributions.
- Tracking cross-check: the fiscal-year 2026 report gives fund 15.71% versus index 16.17%, five-year 4.31% versus 4.71%, and ten-year 7.39% versus 7.84%; the 2025 attribution report gives the calendar comparison above.

## SMDV gaps and scheduled-inline local review

- Canonical identity is Cboe BZX:SMDV; ProShares product and summary-prospectus materials confirm the Cboe BZX listing and current Russell 2000 Dividend Growth Index objective.
- SMDV is within supported ETF scope as a passive, index-tracking, long-only equity ETF. The prospectus describes an index of U.S. small-cap companies with at least ten consecutive years of dividend growth, equal weighting, a 30% sector cap and quarterly resets; no leverage, inverse, bond, commodity or derivative-heavy structure was found.
- The 2025 annual NAV row comes from the official ProShares attribution report as of 2025-12-31; 2016-2024 rows come from the official summary-prospectus annual chart. No secondary annual return was substituted.
- The Board-approved name/index transition is future-dated around 2026-09-28. Current performance and current benchmark metadata are not backfilled to the future S&P SmallCap 600 Dividend Aristocrats Index.
- Current S&P 500 YTD was not paired with SMDV 2026-07-31 YTD because a same-date official benchmark observation was not captured.
- Official daily NAV history sufficient for maximum drawdown and recovery was not verified; the issuer NAV History link returned an unsupported CSV content type during source access, so no numeric secondary drawdown proxy is saved.
- Planned durable paths: created wiki/analysis/performance/ETF_CBOE_BZX_SMDV Performance.md; updated wiki/analysis/comparisons/USA ETF.md, wiki/analysis/comparisons/ETF Region Index.md, wiki/analysis/performance/ETF Performance Index.md, this source batch, and log.md.
- Planned graph changes: primary region USA; breadcrumb [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]; canonical tag geography/United-States; all affected wikilinks resolve to existing/planned targets.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS
