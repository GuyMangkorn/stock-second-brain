---
type: source-batch
workflow: check-etf-performance
scope: research-queue
updated: 2026-09-01
execution_profile: scheduled-inline
window: 2016-2025 plus current 2026 YTD
return_basis: NAV total return
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
---

# ETF Performance Sources — 2026-09-01 Run 5

This dated batch records the source-backed evidence and scheduled-local pre-save review for cards processed by the retained `research-queue-manager` lease. Shared navigation/index files were already dirty before this run and remain outside each card's clean output scope.

## DLS evidence packet

- Input ticker: `DLS`; canonical identity: `NYSE Arca:DLS`; fund: WisdomTree International SmallCap Dividend Fund; inception `2006-06-16`.
- Official classification: `passive-index` international small-cap dividend equity ETF. WisdomTree describes tracking the WisdomTree International SmallCap Dividend Index; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified.
- Official product snapshot as of `2026-08-31`: NAV `$89.743`, total assets `$1,090,377.49k`, shares outstanding `12,150,000`, net expense ratio `0.58%`, distribution yield `6.39%`, and 30-day SEC yield `3.12%`. The latest market price was `$89.450` as of `2026-08-28`, with premium/discount `-0.433%`; NAV and market-price dates are kept separate.
- Official month-end performance as of `2026-07-31`: index YTD `8.77%`; NAV Total Return YTD `8.54%`, 1-year `18.29%`, 3-year `16.16%`, 5-year `7.25%`, 10-year average annual `7.69%`, and since inception `6.47%`. NAV total return reflects distributions reinvested and fund expenses; USD.
- Official complete calendar NAV Total Return rows from the WisdomTree presentation dated `2026-03-31`: 2016 `7.00%`, 2017 `30.95%`, 2018 `-18.69%`, 2019 `22.11%`, 2020 `-1.23%`, 2021 `11.66%`, 2022 `-17.36%`, 2023 `15.40%`, 2024 `3.24%`, 2025 `33.49%`. The SEC prospectus independently corroborates the 2022 row at `-17.36%`; no conflict is established.
- Official issuer benchmark metadata: WisdomTree International SmallCap Dividend Index (`WTISDI`). The common reference remains S&P 500 Total Return in USD with dividends reinvested; cached rows for 2016-2025 are `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`.
- Calculations from official DLS rows: 2016-2025 product `2.0165049887`, cumulative `101.6505%`, rounded-input CAGR `7.2680%`; 2021-2025 product `1.4674966327`, cumulative `46.7497%`, rounded-input CAGR `7.9738%`; 2016-2025 population standard deviation `17.5065%`; S&P 500 2016-2025 product `3.9832911148`, cumulative `298.3291%`, CAGR `14.8218%`; 2021-2025 S&P CAGR `14.4264%`.
- Annual-path risk: `7 / 3` up/down years; best `2025 +33.49%`; least positive `2024 +3.24%`; worst `2018 -18.69%`; least-bad down year `2020 -1.23%`. The official presentation reports since-inception standard deviation `17.67%`, Sharpe `0.24`, information ratio `0.08`, down capture `95.51%`, and beta `0.95` as of `2026-03-31`. Daily NAV maximum drawdown and recovery were not verified.
- Source map: official product/performance page `https://www.wisdomtree.com/us/products/equity/dls`; official presentation `https://www.wisdomtree.com/us/media/dls-presentation`; official index page `https://www.wisdomtree.com/us/indexes/wtisdi`; official factsheet `https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-dls-1050.ashx?la=en`; SEC summary prospectus `https://www.sec.gov/Archives/edgar/data/1350487/000121465923010467/dls497k.htm`; S&P cached source URLs are the standard references recorded in the skill.
- Source integrity review: PASS — official identity, exchange, passive-equity eligibility, current NAV/price and yield fields, month-end NAV total return, annual rows, benchmark metadata and market-price separation reconcile; issuer-reported 10-year average annual return has no disclosed raw endpoints and is not relabeled as independently calculated CAGR.
- Calculation review: PASS — cumulative returns, CAGRs, standard deviation, benchmark comparisons, year counts and best/worst subsets were recomputed from the stated official rows; no partial year was ranked.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required sections, canonical `geography/International` tag and breadcrumb resolve to existing pages.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/run-4 batches, and retained recovery artifacts were dirty before this card's pre-write boundary; they were not modified or included in the DLS scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: update `wiki/analysis/performance/ETF_NYSE_ARCA_DLS Performance.md`; create/update `raw/imports/ETF_performance_sources_2026-09-01_run-5.md`; no shared navigation file is in this card's output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## DLS research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official identity, current NAV and performance fields, annual NAV total-return rows, benchmark convention, calculations and scheduled-local review passed with drawdown endpoint gaps disclosed.
```

## IHDG evidence packet

- Input ticker: `IHDG`; canonical identity: `NYSE Arca:IHDG`; fund: WisdomTree International Hedged Quality Dividend Growth Fund; inception `2014-05-07`.
- Official classification: `passive-index` international equity ETF with a systematic currency hedge. WisdomTree describes the fund as tracking the WisdomTree International Hedged Quality Dividend Growth Index; the hedge is implementation risk, not a leveraged, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff.
- Official product snapshot as of `2026-08-28`: NAV `$53.716`, market price `$53.540`, premium/discount `-0.329%`, distribution yield `5.14%`, 30-day SEC yield `1.89%`, assets `$2,191,614.64k`, and aggregate hedge ratio `98.65%`. Net expense ratio is `0.58%` as of `2026-08-31`.
- Official month-end performance as of `2026-07-31`: index YTD `10.09%`; NAV Total Return YTD `9.84%`, 1-year `20.00%`, 3-year `11.71%`, 5-year `7.82%`, 10-year average annual `10.34%`, and since inception `9.69%`. NAV total return includes reinvested distributions and fund expenses; USD.
- The official IHDG factsheet dated `2026-06-30` independently reports NAV average annual returns of `18.05%`, `11.63%`, `8.14%`, `10.66%`, and `9.65%` for 1/3/5/10-year and since-inception periods respectively; the date difference explains the non-conflict with the newer product-page values. Raw endpoints for the issuer-reported 10-year average annual values are not disclosed.
- Official complete calendar NAV Total Return rows from the WisdomTree presentation dated `2026-03-31`: 2016 `1.66%`, 2017 `21.47%`, 2018 `-11.71%`, 2019 `32.74%`, 2020 `10.78%`, 2021 `19.72%`, 2022 `-11.36%`, 2023 `19.55%`, 2024 `6.42%`, 2025 `14.32%`.
- Official issuer benchmark metadata: WisdomTree International Hedged Quality Dividend Growth Index. The common reference remains S&P 500 Total Return in USD with dividends reinvested; cached rows for 2016-2025 are `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`.
- Calculations from official IHDG rows: 2016-2025 product `2.4744878981`, cumulative `147.4488%`, rounded-input CAGR `9.4835%`, population standard deviation `13.6465%`; 2021-2025 product `1.5434462374`, cumulative `54.3446%`, rounded-input CAGR `9.0682%`; S&P 500 2016-2025 product `3.9832911148`, cumulative `298.3291%`, CAGR `14.8218%`; S&P 2021-2025 CAGR `14.4264%`; relative wealth versus S&P `-37.8783%` for 2016-2025 and `-21.3208%` for 2021-2025.
- Annual-path risk: `8 / 2` up/down years; best `2019 +32.74%`; least positive `2024 +6.42%`; worst `2018 -11.71%`; least-bad down year `2022 -11.36%`. Daily NAV maximum drawdown and recovery were not verified; the currency hedge does not remove equity, country, liquidity, dividend or tracking risk.
- Source map: official product/performance page `https://www.wisdomtree.com/us/products/equity/ihdg`; official factsheet `https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-ihdg-1748.pdf`; official presentation `https://www.wisdomtree.com/us/media/ihdg-presentation`; official index page `https://www.wisdomtree.com/us/indexes/wtidhg`; S&P cached source URLs are the standard references recorded in the skill.
- Source integrity review: PASS — official identity, exchange, passive-equity eligibility, current NAV/price/yield and hedge fields, date-separated rolling returns, annual rows, benchmark metadata and market-price separation reconcile; the 10-year reported average annual figures are not relabeled as independently calculated CAGRs.
- Calculation review: PASS — cumulative returns, CAGRs, annual-path standard deviation, benchmark comparisons, year counts and best/worst subsets were recomputed from the stated official rows; no partial year was ranked.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required passive/index sections, canonical `geography/International` tag and breadcrumb resolve to existing pages.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/run-4 batches, and retained recovery artifacts were dirty before this card's pre-write boundary; they were not modified or included in the IHDG scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NYSE_ARCA_IHDG Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-5.md`; no shared navigation file is in this card's output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## IHDG research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-equity identity, current NAV and hedge fields, annual NAV total-return rows, benchmark convention, calculations and scheduled-local review passed with date-separated rolling metrics and drawdown gaps disclosed.
```

## GCOW evidence packet

- Input ticker: `GCOW`; canonical identity: `Cboe BZX:GCOW`; fund: Pacer Global Cash Cows Dividend ETF; inception `2016-02-22`.
- Official classification: `passive-index` global equity ETF tracking the Pacer Global Cash Cows Dividend Index. The strategy screens global large-cap stocks using free-cash-flow yield and dividend characteristics; the SEC summary prospectus identifies GCOW as listed on Cboe BZX and passively tracking the index. No leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified.
- Official product/factsheet fields as of `2026-03-31`: NAV `USD 45.98`, total expense ratio `0.60%`, strategy benchmark `MSCI World Value Index`, official NAV annualised returns YTD `12.46%`, 1-year `30.59%`, 5-year `13.72%`, 10-year `10.15%`, and since inception `10.75%`. The factsheet's corresponding MSCI World Value figures are `1.18%`, `16.60%`, `9.59%`, `9.35%`, and `9.87%`.
- Current secondary cross-check as of `2026-07-31`: AAII reports NAV YTD `14.7%`, 1-year `28.3%`, 3-year annualised `15.6%`, 5-year annualised `13.4%`, and 10-year annualised `9.8%`. This is used for current context only; the official Pacer factsheet remains the source for issuer strategy and dated benchmark fields.
- Official Pacer GCOW summary/prospectus rows through complete calendar year `2024`: 2017 `20.63%`, 2018 `-7.56%`, 2019 `17.53%`, 2020 `-4.07%`, 2021 `13.86%`, 2022 `6.09%`, 2023 `13.69%`, and 2024 `3.56%`. A 2016 row is excluded because inception was during the year.
- Secondary AAII calendar-year NAV row for `2025` is `27.60%`; it is explicitly marked in the durable page and calculations because a current official Pacer calendar row was not found in the retrieved official packet.
- The common S&P 500 Total Return reference remains the cached USD dividend-reinvested series for 2017-2025: `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`.
- Calculations from eight official rows plus the explicitly marked rounded secondary 2025 row: 2017-2025 product `2.2815450934`, cumulative `128.1545%`, rounded-input CAGR `9.5982%`, population standard deviation `10.9080%`, 7 up/2 down years; 2021-2025 product `1.8147241197`, cumulative `81.4724%`, rounded-input CAGR `12.6580%`. S&P 500 reference CAGRs are `15.1442%` for 2017-2025 and `14.4264%` for 2021-2025. Best `2025 +27.60%`; least positive `2024 +3.56%`; worst `2018 -7.56%`; least-bad down year `2020 -4.07%`.
- Source integrity review: PASS — official identity, passive-equity classification, issuer benchmark, expense/inception fields and official annual rows reconcile. The missing official 2025 annual row is disclosed and the secondary replacement is marked; no source conflict is hidden or treated as issuer data.
- Calculation review: PASS — cumulative returns, CAGRs, standard deviation, S&P reference comparisons, year counts and best/worst subsets were recomputed from the stated inputs; partial 2016 inception and 2026 YTD were excluded from annual ranking.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required sections, canonical `geography/International` tag and breadcrumb resolve to existing pages; secondary 2025 provenance is visible in the table and footnote.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/run-4 batches, and retained recovery artifacts were dirty before this card's pre-write boundary; they were not modified or included in the GCOW scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_CBOE_BZX_GCOW Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-5.md`; no shared navigation file is in this card's output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## GCOW research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive global-equity identity and index fields, official annual rows through 2024, explicitly marked secondary 2025 cross-check, current context, calculations and scheduled-local review passed with provenance and drawdown gaps disclosed.
```

## ISPFF evidence packet

- Input ticker: `ISPFF`; canonical identity: `LSE:IDWP`; fund: iShares Developed Markets Property Yield UCITS ETF USD (Dist), ISIN `IE00B1FZS350`, inception `2006-10-20`. The official iShares listing table identifies the USD listing as London Stock Exchange ticker `IDWP`; `ISPFF` is retained only as the incoming OTC alias.
- Official classification: `passive-index` equity ETF focused on listed real estate companies and REITs in developed markets. The official product page identifies the asset class as Real Estate and the KIID describes passive management; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified for this USD share class.
- Official product snapshot as of `2026-08-28`: NAV `USD 25.65`, share-class net assets `USD 1,180,449,055`, fund net assets `USD 1,652,942,689`, total expense ratio `0.59%`, quarterly distribution, physical/optimised structure, and `46,013,444` shares outstanding. Official NAV Total Return YTD is `10.11%` as of `2026-08-27`; NAV and performance dates are kept separate.
- Official benchmark metadata: `FTSE EPRA Nareit Developed Dividend+ Net Index in USD`; the product page reports `312` holdings as of `2026-08-27`, standard deviation `16.05%` and beta `0.998` as of `2026-07-31`.
- Official iShares factsheet calendar-year NAV Total Return rows dated `2026-03-31`: 2016 `5.50%`, 2017 `10.59%`, 2018 `-5.80%`, 2019 `21.95%`, 2020 `-9.47%`, 2021 `25.18%`, 2022 `-24.33%`, 2023 `8.92%`, 2024 `1.00%`, 2025 `8.24%`. The same table reports benchmark rows `5.52%`, `10.53%`, `-5.75%`, `21.97%`, `-9.56%`, `25.28%`, `-24.17%`, `8.87%`, `1.06%`, `8.28%` respectively.
- Official rolling NAV TR as of `2026-06-30`: 1-year `16.30%`, 3-year annualised `8.75%`, 5-year annualised `1.03%`, 10-year annualised `2.81%`, and since inception annualised `3.62%`. These are issuer-reported rolling metrics; raw endpoints are not disclosed, so the 10-year figure is not relabeled as an independently calculated CAGR.
- The common S&P 500 Total Return reference remains the cached USD dividend-reinvested series for complete calendar years 2016-2025: `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`.
- Calculations from the rounded official IDWP rows: 2016-2025 product `1.3676894500`, cumulative `36.7689%`, rounded-input CAGR `3.1808%`; 2021-2025 product `1.1279126597`, cumulative `12.7913%`, rounded-input CAGR `2.4366%`; population standard deviation `13.9470%`; 7 up/3 down years; best `2021 +25.18%`; least positive `2024 +1.00%`; worst `2022 -24.33%`; least-bad down year `2018 -5.80%`. S&P 500 reference CAGRs are `14.8218%` for 2016-2025 and `14.4264%` for 2021-2025.
- Source integrity review: PASS — the OTC alias was resolved to the official USD LSE listing by the official listing table and ISIN; passive real-estate equity eligibility, NAV/performance date separation, calendar-year rows, FTSE benchmark rows, current YTD, rolling metrics and risk fields reconcile. The issuer-reported rolling figures are not used as independently calculated endpoint CAGRs.
- Calculation review: PASS — cumulative returns, CAGRs, standard deviation, benchmark comparisons, year counts and best/worst subsets were recomputed from the stated rounded rows; no partial year was ranked.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required sections, canonical `geography/International` tag and breadcrumb resolve to existing pages; `LSE:IDWP` is used throughout the durable page.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/run-4 batches, and retained recovery artifacts were dirty before this card's pre-write boundary; they were not modified or included in the ISPFF scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_LSE_IDWP Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-5.md`; no shared navigation file is in this card's output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## ISPFF research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive real-estate equity identity, canonical USD LSE listing, current NAV and YTD, calendar NAV total-return rows, benchmark data, calculations and scheduled-local review passed with rolling-endpoint and drawdown gaps disclosed.
```
