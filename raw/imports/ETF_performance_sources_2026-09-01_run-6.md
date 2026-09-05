---
type: source-batch
workflow: check-etf-performance
scope: research-queue
updated: 2026-09-01
execution_profile: scheduled-inline
window: available complete calendar years plus current 2026 YTD
return_basis: NAV total return
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
---

# ETF Performance Sources — 2026-09-01 Run 6

This dated batch records source-backed evidence and the scheduled-local pre-save review for cards processed under the retained `research-queue-manager` project lease. Shared navigation/index files and earlier recovery artifacts were already dirty before this run and remain outside each card's clean output scope.

## FIVA evidence packet

- Input ticker: `FIVA`; canonical identity: `NYSE Arca:FIVA`; fund: Fidelity International Value Factor ETF; inception `2018-01-16`.
- Official classification: `passive-index` / strategic-beta international equity ETF. Fidelity states that the fund normally invests at least 80% in securities in the Fidelity International Value Factor Index, a rules-based index of large- and mid-capitalization developed international companies with attractive valuations. No leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified.
- Official June 30, 2026 factsheet fields: NAV Total Return YTD `14.34%`, 1-year `35.42%`, 3-year annualized `22.28%`, 5-year annualized `13.72%`, life-of-fund annualized `8.91%`; net expense ratio `0.18%`; 3-year standard deviation `13.24%`, beta `1.00`, Sharpe `1.32`, and tracking error `0.10`; turnover rate `69%` as of 2026-04. Fidelity’s quote page crawled 2026-09-01 reports NAV `USD 39.837917`, market price `USD 39.74`, primary exchange `NYSE ARCA`.
- Official complete calendar NAV Total Return rows from the Fidelity factsheet dated `2026-06-30`: 2019 `19.70%`, 2020 `-1.68%`, 2021 `16.05%`, 2022 `-10.42%`, 2023 `20.26%`, 2024 `3.34%`, 2025 `44.65%`. The factsheet reports no 2018 calendar row; it is excluded rather than backfilled.
- Official issuer benchmark: Fidelity International Value Factor Index (Net). NAV returns include changes in share price and reinvestment of dividends and capital gains; market-price returns remain separate. Fidelity identifies Geode Capital Management as sub-adviser since 2018, but the fund is passive and the page does not turn benchmark spread into manager skill evidence.
- Latest secondary current-YTD cross-check: Schwab reports FIVA NAV YTD `+16.7%` as of `2026-07-31`; it is labelled secondary and kept separate from Fidelity’s official `+14.34%` June 30 YTD field. No same-date official August YTD field was established in the retrieved issuer sources.
- Common S&P 500 Total Return reference uses the cached USD dividend-reinvested rows for 2019-2025: `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`.
- Calculations from official FIVA rows: 2019-2025 product `2.1993802350`, cumulative `119.9380%`, rounded-input CAGR `11.9180%`; 2021-2025 product `1.8688063349`, cumulative `86.8806%`, rounded-input CAGR `13.3216%`; population standard deviation `16.7580%`; `5 / 2` up/down years. Best `2025 +44.65%`; least positive `2024 +3.34%`; worst `2022 -10.42%`; least-bad down year `2020 -1.68%`.
- S&P 500 cached calculations for the same windows: 2019-2025 product `3.0540502198`, cumulative `205.4050%`, rounded-input CAGR `17.2919%`; 2021-2025 CAGR `14.4264%`. FIVA spreads are `-5.3739` percentage points for 2019-2025 and `-1.1048` percentage points for 2021-2025; these are arithmetic comparisons, not alpha.
- Daily NAV maximum drawdown and recovery were not verified. The primary gap is the unavailable 2018 calendar row and the lack of an issuer current YTD field matching the secondary 2026-07-31 date.
- Source map: official factsheet `https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F9887716.PDF`; official quote `https://digital.fidelity.com/prgw/digital/research/quote/dashboard/summary?symbol=FIVA`; SEC prospectus `https://www.sec.gov/Archives/edgar/data/945908/000094590826000084/filing10958.htm`; secondary YTD `https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=fiva`; cached S&P references are defined in the `check-etf-performance` skill.
- Source integrity review: PASS — issuer identity, exchange, passive strategic-beta classification, index, NAV/market-price separation, annual rows, fees and risk fields reconcile; official and secondary YTD observations remain date-separated.
- Calculation review: PASS — cumulative returns, available-period CAGRs, standard deviation, S&P comparisons, year counts and best/worst subsets were recomputed from the stated rows; no partial or unavailable year was ranked.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required sections, canonical `geography/International` tag and breadcrumb resolve to existing navigation targets.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, the prior run-3 batch and retained recovery artifacts were dirty before the FIVA pre-write boundary; they were not modified or included in this scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NYSE_ARCA_FIVA Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-6.md`; no shared navigation file is in this card’s output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## FIVA research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive strategic-beta identity, current quote, annual NAV total-return rows, date-separated YTD cross-check, calculations and scheduled-local review passed with unavailable 2018 and daily drawdown gaps disclosed.
```

## KOKU evidence packet

- Input ticker: `KOKU`; canonical identity: `NYSE Arca:KOKU`; fund: Xtrackers MSCI Kokusai Equity ETF; inception `2020-04-07`.
- Official classification: `passive-index` developed-markets ex-Japan equity ETF. DWS states that the fund uses a passive/indexing approach and full replication where practicable to track the MSCI Kokusai Index, also known as MSCI World ex Japan. The fund does not hedge foreign-currency exposure; no leverage, inverse, option-income, bond, commodity, currency or derivative-defined payoff was identified.
- Official Q1 2026 factsheet fields as of `2026-03-31`: NAV 1-year `18.75%`, 3-year annualized `17.14%`, 5-year annualized `10.85%`, since-inception annualized `16.88%`; net expense ratio `0.09%`; beta `1.04`; 1,143 holdings and net assets `$805,182,756.00`. The factsheet defines the MSCI Kokusai Net Total Return Index as the tracked index and keeps market-price returns separate.
- Official calendar NAV Total Return rows from the DWS prospectus: 2021 `23.81%`, 2022 `-17.96%`, 2023 `24.38%`, and 2024 `19.64%`. The prospectus bar chart identifies 2020 as an inception-year partial and exposes no 2025 calendar row in the retrieved official filing.
- Secondary dividend-reinvested history from PortfoliosLab, last updated `2026-08-29`: current YTD `13.09%` and 2025 total return `21.45%`. The 2025 observation is marked `*` in the performance page and is not described as official issuer data. Official DWS calendar rows and secondary rows are not mixed without provenance.
- Common S&P 500 Total Return reference uses cached USD dividend-reinvested rows for 2021-2025: `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`.
- Calculations from the four official rows plus marked secondary 2025 proxy: 2021-2025 product `1.8357175134`, cumulative `83.5718%`, rounded-input CAGR `12.9175%`; population standard deviation `16.2011%`; `4 / 1` up/down years. Best `2023 +24.38%`; least positive `2024 +19.64%`; worst and least-bad down year `2022 -17.96%`.
- S&P cached calculations for 2021-2025: product `1.9616961801`, cumulative `96.1696%`, rounded-input CAGR `17.4115%`. KOKU’s arithmetic spread is `-4.4940` percentage points; this is not alpha.
- Daily NAV maximum drawdown and recovery were not verified. The principal data limitation is that official calendar rows for 2025 and a current issuer YTD field were not established; 2025 and current YTD remain clearly marked secondary observations.
- Source map: official factsheet `https://etf.dws.com/en-us/AssetDownload/Index/94ec1d01-afbe-4684-8d4a-497c224fb2e5/KOKU-Fact-Sheet.pdf`; official prospectus `https://etf.dws.com/en-us/AssetDownload/Index/cfabbe07-bfc5-49c6-9de2-15429c72ad99/KOKU-1.pdf`; SEC filing `https://www.sec.gov/Archives/edgar/data/1503123/000008805325001122/k121925koku.htm`; secondary history `https://portfolioslab.com/symbol/KOKU`; cached S&P references are defined in the `check-etf-performance` skill.
- Source integrity review: PASS — official identity, exchange, passive eligibility, index, inception, fees, official 2021-2024 rows and secondary 2025/YTD observations reconcile with explicit provenance and no mixed return basis.
- Calculation review: PASS — cumulative return, CAGR, standard deviation, S&P comparison, year counts and best/worst subsets were recomputed from the stated rows; 2020 inception partial was excluded from ranking.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required sections, canonical `geography/International` tag and breadcrumb resolve to existing navigation targets.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, the prior run-3 batch, and retained recovery artifacts were dirty before the KOKU pre-write boundary; they were not modified or included in this scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NYSE_ARCA_KOKU Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-6.md`; no shared navigation file is in this card’s output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## KOKU research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive developed-equity identity, current secondary YTD, official 2021-2024 NAV rows, marked 2025 proxy, calculations and scheduled-local review passed with inception and daily drawdown gaps disclosed.
```
## WSML evidence packet

- Input ticker: `WSML`; canonical identity: `LSE:WSML`; legacy OTC alias `IMWSF`; fund: iShares MSCI World Small Cap UCITS ETF; official USD listing is London Stock Exchange `WSML` for ISIN `IE00BF4RFH31`. Underlying exposure is global developed-market small-cap equity, primary region `International`, canonical tag `geography/global-developed`.
- Official classification: `passive-index`; the fund seeks to track the `MSCI World Small Cap Index (Net)`, uses a physical/optimised structure, has share-class launch `2018-03-27`, `0.35%` Total Expense Ratio, and accumulating income treatment.
- Official product source: https://www.ishares.com/uk/professionals/en/products/296576/ishares-msci-world-small-cap-ucits-etf-usd-%28acc%29-fund — product page reviewed for current observations through `2026-08-28`; NAV `USD 10.62`, NAV Total Return YTD `17.53%`, holdings `3,548`, P/B `2.11`, P/E `19.19`, and benchmark level `USD 996.55` as of `2026-08-28`; 3-year standard deviation `16.17%` and beta `1.000` as of `2026-07-31`.
- Official historical source: https://www.ishares.com/gls-download/literature/fact-sheet/wsml-ishares-msci-world-small-cap-ucits-etf-fund-fact-sheet-en-gb.pdf — official factsheet with complete annual NAV/index rows for `2019-2025`, July 2026 YTD `13.88%` as of `2026-07-31`, and the USD accumulating share-class identity. Annual rows: fund `25.73%, 15.83%, 15.81%, -18.64%, 16.02%, 7.93%, 19.84%`; issuer index `26.19%, 15.96%, 15.75%, -18.75%, 15.76%, 8.15%, 19.88%`.
- Return basis: USD `NAV Total Return` with gross income reinvested where applicable; accumulating income remains in NAV. Market-price return is not mixed. Complete 2018 inception-year annual data was not disclosed, so the 2019-2025 window is used for annual ranking and no 10-year NAV TR CAGR is claimed because the share class has less than ten elapsed years as of the run date.
- Performance calculations from official annual rows: 2019-2025 product compound `105.92%` and rounded-input CAGR `10.87%`; 2021-2025 compound `41.39%` and CAGR `7.17%`; issuer-index 2019-2025 CAGR `10.92%`; issuer-index 2021-2025 CAGR `7.14%`. Complete-year count is `6 / 1` up/down; best `2019 +25.73%`; least positive `2024 +7.93%`; worst and least-bad down year `2022 -18.64%`.
- Cached common benchmark: `S&P 500 Total Return` in USD with dividends reinvested, complete calendar years `2016-2025`, reference as of `2025-12-31`; annual rows `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`; 2019-2025 cumulative `205.41%` / CAGR `17.29%`; 2021-2025 cumulative `96.17%` / CAGR `14.43%`. The cached benchmark is not used as a synchronized 2026 YTD comparison.
- Risk limitation: official daily NAV observations sufficient to calculate maximum drawdown and recovery were not verified in this lean refresh; no numeric drawdown proxy is saved. The latest NAV and YTD are separate as-of fields and are not combined with the older July factsheet field as if they were contemporaneous.
- Source integrity review: PASS — issuer identity, exchange, passive equity eligibility, index, TER, NAV/market-price separation, annual rows, current fields, calculations, and date separation reconcile; no unsupported annual proxy or shorter-period 10-year claim is used.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required sections, existing breadcrumb targets resolve, and the canonical `geography/global-developed` tag is present.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, and retained recovery artifacts were dirty before the WSML pre-write boundary; they were not modified or included in this scoped commit. Existing navigation links already resolve to the canonical WSML performance page.
- Planned durable paths/change map: update `wiki/analysis/performance/ETF_LSE_WSML Performance.md`; update this source batch; no shared navigation file is in this card’s output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## WSML research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
@@
@@
@@
 reason: Official passive global small-cap identity, current NAV/YTD, annual NAV rows, calculations and scheduled-local review passed with daily drawdown gaps disclosed.
```

## JHMD evidence packet

- Input ticker/canonical identity: `JHMD`; `NYSE Arca:JHMD`; fund: John Hancock Multifactor Developed International ETF; inception `2016-12-15`.
- Official classification: `passive-index`; developed international multifactor equity ETF. John Hancock states that the fund seeks to track the John Hancock Dimensional Developed International Index and emphasizes smaller capitalization, lower relative price and higher profitability characteristics. No leverage, inverse, option-income, bond, commodity, currency or derivative-defined payoff was identified.
- Official Q1 2026 factsheet fields as of `2026-03-31`: NAV QTD/YTD `0.08%`, 1-year `23.26%`, 3-year annualized `14.40%`, 5-year annualized `8.36%`, since-inception annualized `8.53%`; 10-year is unavailable; gross expense ratio `0.43%`, net expense ratio `0.39%` through `2026-08-31`.
- Secondary rounded annual NAV rows from AAII, used only for the calendar-year table: `2017 25.2%`, `2018 -13.9%`, `2019 20.3%`, `2020 6.6%`, `2021 11.7%`, `2022 -13.9%`, `2023 19.1%`, `2024 2.5%`, `2025 32.8%`. The issuer factsheet exposes standardized periods but no text calendar-year table in this capture, so annual rows are explicitly marked secondary.
- Return basis: USD `NAV Total Return` with distributions reinvested. Secondary AAII current NAV YTD is `+11.6%` as of `2026-07-31`; the issuer’s retrieved YTD field is only `+0.08%` as of `2026-03-31`, so the two fields remain date-separated and no same-date issuer value is backfilled.
- Common S&P 500 Total Return reference uses cached USD dividend-reinvested rows for complete calendar years `2017-2025`: `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`.
- Calculations from secondary rounded annual rows: JHMD 2017-2025 product `2.1553625809`, cumulative `115.5363%`, rounded-input CAGR `8.9075%`; 2021-2025 product `1.5591576376`, cumulative `55.9158%`, CAGR `9.2894%`; population standard deviation `15.4664%`; `7 / 2` up/down years. Best `2025 +32.80%`; least positive `2024 +2.50%`; worst and least-bad down years tie in `2018` and `2022` at `-13.90%`.
- S&P cached calculations for 2017-2025: cumulative `255.7781%`, rounded-input CAGR `15.1442%`; 2021-2025 cumulative `96.1696%`, CAGR `14.4264%`. JHMD’s arithmetic CAGR comparison is `-6.2367 pp` for 2017-2025 and `-5.1370 pp` for 2021-2025; this is a reference comparison, not alpha.
- Daily NAV maximum drawdown and recovery were not verified. Secondary risk cross-check reports beta `0.90` and standard deviation `13.0%` as of `2026-07-31`; these are not treated as issuer-confirmed daily metrics.
- Source map: official factsheet `https://www.jhinvestments.com/content/dam/jhi-investments/JHINV/public/ETFs/Documents/FactSheets/InvestorFactSheet/etf-multifactor-developed-international-investor-fact-sheet-jhi.pdf`; SEC prospectus `https://www.sec.gov/Archives/edgar/data/1478482/000119312525191988/d911861d497k.htm`; secondary current YTD/annual table `https://www.aaii.com/etfs/summary?ticker=JHMD`; cached S&P references are defined in the `check-etf-performance` skill.
- Source integrity review: PASS — official passive index identity, exchange, factor strategy, fee fields and standardized returns reconcile; secondary July YTD and annual rows are clearly labelled and kept separate from official March observations.
- Calculation review: PASS — cumulative returns, available-period CAGRs, annual dispersion, S&P comparisons, year counts and best/worst subsets were recomputed from the stated rounded rows.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required sections, canonical `geography/International` and `geography/global-developed` tags, and existing breadcrumb targets resolve.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/run-5 batches and retained recovery artifacts were dirty before the JHMD pre-write boundary; they were not modified or included in this scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NYSE_ARCA_JHMD Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-6.md`; no shared navigation file is in this card’s output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## JHMD research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive multifactor identity and standardized returns, secondary complete calendar rows and current YTD, calculations and scheduled-local review passed with secondary annual/risk and daily drawdown gaps disclosed.
```

## IDHQ evidence packet

- Input ticker/canonical identity: `IDHQ`; `NYSE Arca:IDHQ`; fund: Invesco S&P International Developed Quality ETF; CUSIP `46138E214`; inception `2007-06-13`.
- Official classification: `passive-index`; international developed-market quality equity ETF. Invesco states that the fund is based on the S&P Quality Developed ex-U.S. LargeMidCap Index, normally invests at least 90% in index securities, and uses quality measures based on return on equity, accruals ratio and financial leverage. No leverage, inverse, option-income, bond, commodity, currency or derivative-defined payoff was identified.
- Official Q1 2026 factsheet fields as of `2026-03-31`: NAV YTD `0.84%`, 1-year `20.52%`, 3-year annualized `12.85%`, 5-year annualized `6.68%`, 10-year annualized `8.57%`, fund-inception annualized `4.13%`; management fee and total expense ratio `0.29%`; 193 holdings; P/E `23.81`, P/B `9.02`, ROE `32.01%`, and 30-day SEC yield `1.02%`.
- Official calendar NAV/index rows from the same factsheet: fund `2016 -1.96%`, `2017 26.73%`, `2018 -12.74%`, `2019 29.86%`, `2020 15.63%`, `2021 11.29%`, `2022 -20.20%`, `2023 18.99%`, `2024 1.90%`, `2025 26.80%`; issuer index `-1.24%`, `26.76%`, `-12.63%`, `30.21%`, `15.65%`, `11.60%`, `-20.07%`, `19.13%`, `2.07%`, `27.34%`.
- Return basis: USD `NAV Total Return`; the issuer index is net return and market-price returns remain separate. Secondary AAII reports current NAV YTD `+26.0%` as of `2026-07-31`; the issuer’s retrieved factsheet current YTD is only through `2026-03-31`, so the two observations remain date-separated and the secondary field is clearly labelled.
- Common S&P 500 Total Return reference uses cached USD dividend-reinvested rows for complete calendar years `2016-2025`: `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`.
- Calculations from official rows: IDHQ 2016-2025 product `2.2228328488`, cumulative `122.2833%`, rounded-input CAGR `8.3155%`; 2021-2025 product `1.3654095492`, cumulative `36.5410%`, CAGR `6.4272%`; population standard deviation `16.4535%`; `7 / 3` up/down years. Best `2019 +29.86%`; least positive `2024 +1.90%`; worst `2022 -20.20%`; least-bad down year `2016 -1.96%`.
- Issuer-index calculations: 2016-2025 cumulative `127.4960%`, rounded-input CAGR `8.5669%`; 2021-2025 cumulative `38.1205%`, CAGR `6.6723%`. Arithmetic fund/index spread is `-0.2514 pp` CAGR for 2016-2025 and `-0.2451 pp` for 2021-2025; this is tracking difference, not alpha.
- S&P cached calculations: 2016-2025 cumulative `298.3291%`, rounded-input CAGR `14.8218%`; 2021-2025 cumulative `96.1696%`, CAGR `14.4264%`. IDHQ’s arithmetic CAGR comparison is `-6.5062 pp` for 2016-2025 and `-7.9992 pp` for 2021-2025; these are reference comparisons, not manager-skill evidence.
- Daily NAV maximum drawdown and recovery were not verified. The current YTD field is secondary and date-separated from the official March factsheet; no unsupported issuer value was backfilled.
- Source map: official factsheet `https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/idhq-invesco-s-p-international-developed-quality-etf-fact-sheet.pdf`; SEC prospectus `https://www.sec.gov/Archives/edgar/data/1168164/000119312526031207/d72607d497k.htm`; secondary current YTD/annual table `https://www.aaii.com/etf/ticker/IDHQ`; cached S&P references are defined in the `check-etf-performance` skill.
- Source integrity review: PASS — official identity, exchange, passive quality methodology, index, fees, annual NAV/index rows and official standardized returns reconcile; secondary July YTD is explicitly separated from the official March observation.
- Calculation review: PASS — cumulative returns, available-period CAGRs, annual dispersion, S&P comparisons, tracking spreads, year counts and best/worst subsets were recomputed from the official rows.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required sections, canonical `geography/International` and `geography/global-developed` tags, and existing breadcrumb targets resolve.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/run-5 batches and retained recovery artifacts were dirty before the IDHQ pre-write boundary; they were not modified or included in this scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NYSE_ARCA_IDHQ Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-6.md`; no shared navigation file is in this card’s output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## IDHQ research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive quality ETF identity, standardized issuer returns, official annual NAV/index rows, date-separated secondary current YTD, calculations and scheduled-local review passed with daily drawdown gaps disclosed.
```

## TLTD evidence packet

- Input ticker and canonical identity: `TLTD`; `NYSE Arca:TLTD`; fund currently named Northern Trust Morningstar Developed Markets ex-US Factor Tilt ETF, formerly FlexShares Morningstar Developed Markets ex-US Factor Tilt Index Fund; CUSIP `33939L803`.
- Official classification: `passive-index`; developed-markets ex-US factor equity ETF. Northern Trust states that the fund seeks to track the Morningstar Developed Markets ex-US Factor Tilt Index, uses a passive/indexing approach and representative sampling, and targets increased small-cap and value exposure relative to the parent index. No leveraged, inverse, option-income, bond, commodity, currency or derivative-defined payoff was identified, although the prospectus permits limited futures/options/forwards for tracking and portfolio management.
- Official product page observations through `2026-08-28`: NAV `US$105.33`, market price `US$104.51`, net assets `US$695.16m`, net expense ratio `0.39%`, primary exchange `NYSE Arca`. Official factsheet dated `2026-06-30` reports inception `2012-09-25`, 2,307 holdings, gross expense ratio `0.41%`, net expense ratio `0.39%`, weighted average beta `1.03`, and quarterly distributions.
- Official current NAV Total Return performance from Northern Trust as of `2026-07-31`: YTD `11.45%`, 1-year cumulative `27.05%`, 3-year annualized `18.72%`, 5-year annualized `10.65%`, 7-year annualized `11.33%`, 10-year annualized `9.71%`, and since inception annualized `8.38%`. All fund figures assume reinvestment of dividends and capital gains at NAV; market-price returns remain separate.
- Secondary rounded annual NAV rows from AAII, used only for the calendar-year table: `2016 5.4%`, `2017 25.9%`, `2018 -17.2%`, `2019 21.5%`, `2020 4.4%`, `2021 12.3%`, `2022 -13.7%`, `2023 17.5%`, `2024 5.1%`, `2025 38.6%`. The retrieved issuer pages expose standardized/trailing returns and a prospectus 2025/5-year cross-check but no text calendar-year table, so these rows are explicitly marked secondary.
- Return basis: USD NAV Total Return with dividends and capital gains reinvested at NAV. The official current YTD field `+11.45%` as of `2026-07-31` is kept separate from the secondary calendar table and the `2026-08-28` NAV level.
- Common S&P 500 Total Return reference uses cached USD dividend-reinvested rows for complete calendar years `2016-2025`: `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`.
- Calculations from secondary rounded annual rows: TLTD 2016-2025 product `2.3118934751`, cumulative `131.1893%`, rounded-input CAGR `8.7419%`; 2021-2025 product `1.6588012918`, cumulative `65.8801%`, CAGR `10.6519%`; population standard deviation `16.2561%`; `8 / 2` up/down years. Best `2025 +38.60%`; least positive `2020 +4.40%`; worst `2018 -17.20%`; least-bad down year `2022 -13.70%`.
- S&P cached calculations for 2016-2025: cumulative `298.3291%`, rounded-input CAGR `14.8218%`; 2021-2025 cumulative `96.1696%`, CAGR `14.4264%`. TLTD’s arithmetic CAGR comparison is `-6.0799 pp` for 2016-2025 and `-3.7745 pp` for 2021-2025; this is a reference comparison, not alpha.
- Daily NAV maximum drawdown and recovery were not verified. The exact calendar table remains secondary, while official standardized NAV/YTD fields are retained as the primary current evidence.
- Source map: official product `https://etfs.ntam.northerntrust.com/us/en/individual/funds/tltd`; official factsheet `https://www.flexshares.com/content/dam/ntflexshares/fund-documents/tltd/tltd-factsheet.pdf.coredownload.pdf`; SEC prospectus `https://www.sec.gov/Archives/edgar/data/1491978/000119312526352175/d272956d497k.htm`; secondary annual rows `https://www.aaii.com/etf/ticker/TLTD`; cached S&P references are defined in the `check-etf-performance` skill.
- Source integrity review: PASS — official exchange/identity, passive factor classification, index, current NAV/price, fees, inception, official standardized returns and secondary calendar rows are reconciled with explicit provenance.
- Calculation review: PASS — secondary annual compound returns, available-period CAGRs, annual dispersion, S&P comparisons, year counts and best/worst subsets were recomputed from the stated rounded rows; no partial year was ranked.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required sections, canonical `geography/International` and `geography/global-developed` tags, and existing breadcrumb targets resolve.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/run-5 batches and retained recovery artifacts were dirty before the TLTD pre-write boundary; they were not modified or included in this scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NYSE_ARCA_TLTD Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-6.md`; no shared navigation file is in this card’s output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## TLTD research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive factor ETF identity, current NAV/YTD and trailing returns, secondary complete calendar rows, calculations and scheduled-local review passed with secondary annual-row and daily drawdown gaps disclosed.
```

## WGQDF evidence packet

- Input ticker: `WGQDF`; canonical identity: `LSE:GGRA`; legacy OTC alias `WGQDF`; fund: WisdomTree Global Quality Dividend Growth UCITS ETF - USD Acc; ISIN `IE00BZ56SW52`. The issuer listing table maps the USD London Stock Exchange line to `GGRA`; GBx line `GGRG` is the same ISIN but a different trading currency.
- Official classification: `passive-index`; global developed-market quality/dividend-growth equity UCITS ETF. WisdomTree describes the fund as tracking the WisdomTree Global Developed Quality Dividend Growth Index, with a rules-based fundamentally weighted universe, quality/momentum risk screen, ESG exclusions and dividend-based weighting. Physical fully replicated; accumulating; no leverage, inverse, option-income, bond, commodity, currency or derivative-defined payoff was identified.
- Official product page observations through `2026-08-28`: NAV `US$50.525`, fund AUM `US$1,705,874,426`, TER `0.38%`, inception `2016-06-03`, base currency USD, accumulating income, physical fully replicated. A second WisdomTree locale page displayed NAV `US$50.542` for the same date; this locale discrepancy is disclosed and the IE issuer page is retained as the canonical current-NAV source.
- Official WisdomTree factsheet, document date `2026-07-31`, reports NAV/index performance in USD net of fees: fund YTD `7.28%`, QTR `5.03%`, 1-year `16.52%`, 3-year annualized `11.98%`, inception annualized `11.70%`; index YTD `7.38%`, QTR `5.10%`, 1-year `16.84%`, 3-year annualized `12.22%`, inception annualized `11.95%`. Performance below one year is cumulative.
- Official complete calendar NAV/index rows from the same factsheet: fund `2017 27.99%`, `2018 -8.81%`, `2019 33.18%`, `2020 16.26%`, `2021 19.29%`, `2022 -13.88%`, `2023 18.26%`, `2024 8.98%`, `2025 16.33%`; index `28.42%`, `-8.63%`, `33.51%`, `16.51%`, `19.72%`, `-13.88%`, `18.49%`, `9.21%`, `16.58%`. The 2016 launch year is partial and excluded from ranking.
- Return basis: USD `NAV Total Return` net of fees; accumulating income remains in NAV. The official issuer product page did not expose a newer NAV YTD field through `2026-08-28` in this capture. Secondary Cbonds reports LSE USD exchange-price return with payments YTD `+9.45%` through `2026-08-28`; it is retained as a date-stamped price-based cross-check and never merged into the NAV series. Borsa Italiana’s EUR trading-line YTD is a separate exchange observation and is not used for USD NAV TR.
- Common S&P 500 Total Return reference uses cached USD dividend-reinvested rows for complete calendar years `2017-2025`: `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`.
- Calculations from official rounded annual rows: GGRA 2017-2025 product `2.7834091464`, cumulative `178.3409%`, rounded-input CAGR `12.0463%`; 2021-2025 product `1.5402260560`, cumulative `54.0226%`, CAGR `9.0227%`; population standard deviation `14.6637%`; `7 / 2` up/down years. Best `2019 +33.18%`; least positive `2024 +8.98%`; worst `2018 -8.81%`; least-bad down year `2018 -8.81%`.
- Issuer-index calculations for the same rows: 2017-2025 cumulative `183.8914%`, rounded-input CAGR `12.2924%`; 2021-2025 cumulative `55.5389%`, CAGR `9.2365%`. The fund/index arithmetic tracking spread is `-0.2461 pp` CAGR over 2017-2025 and `-0.2138 pp` over 2021-2025; it is not called alpha.
- S&P cached calculations: 2017-2025 cumulative `255.7781%`, rounded-input CAGR `15.1442%`; 2021-2025 cumulative `96.1696%`, CAGR `14.4264%`. GGRA’s arithmetic CAGR comparison is `-3.0979 pp` for 2017-2025 and `-5.4037 pp` for 2021-2025; these are reference comparisons, not manager-skill evidence.
- Daily NAV maximum drawdown and recovery were not verified. The current NAV locale discrepancy and lack of a same-date issuer NAV YTD field are disclosed; no unsupported proxy is substituted for those gaps.
- Source map: official product `https://www.wisdomtree.com/ie/products/equities/wisdomtree-global-quality-dividend-growth-ucits-etf---usd-acc`; official factsheet `https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BZ56SW52/`; OTC cross-check `https://stockanalysis.com/quote/otc/WGQDF/`; secondary current YTD `https://cbonds.fr/etf/6397/`; exchange metadata `https://www.borsaitaliana.it/borsa/etf/scheda/IE00BZ56SW52-ETFP.html`; cached S&P references are defined in the `check-etf-performance` skill.
- Source integrity review: PASS — issuer identity, LSE USD canonical mapping, passive eligibility, index, inception, fees, physical/accumulating structure, annual NAV/index rows, current NAV and date-separated secondary YTD reconcile; the official locale NAV discrepancy is preserved as a disclosed conflict.
- Calculation review: PASS — cumulative returns, available-period CAGRs, annual dispersion, S&P comparisons, tracking spreads, year counts and best/worst subsets were recomputed from the stated rounded rows; partial 2016 was excluded.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required sections, canonical `geography/International` and `geography/global-developed` tags, and existing breadcrumb targets resolve.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, the prior run-3/run-5 batches, and retained recovery artifacts were dirty before the WGQDF pre-write boundary; they were not modified or included in this scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_LSE_GGRA Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-6.md`; no shared navigation file is in this card’s output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## WGQDF research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive global developed equity identity, canonical LSE USD mapping, annual NAV/index rows, official July YTD, date-separated current secondary cross-check, calculations and scheduled-local review passed with NAV locale and daily drawdown gaps disclosed.

## TILC evidence packet

- Input ticker: `TILC`; canonical identity: `Nasdaq:TILC`; fund: Thrivent International Large Cap ETF; CUSIP `88588G604`; inception `2017-11-14`; Nasdaq listing date `2026-06-15`.
- Official classification: `active-equity-long-only`; Thrivent describes a diversified portfolio of non-U.S. developed-market large-cap international securities across growth, value and core styles, seeking long-term capital appreciation. The issuer says the process is driven primarily by quantitative techniques. No leveraged, inverse, option-income, bond, commodity, currency or derivative-defined payoff was identified.
- Official current product-page fields as of `2026-07-31`: NAV Total Return YTD `13.89%`, 1-year `26.76%`, net annual fund operating expenses `0.52%`, and `327` holdings. The page currently states that trading in ETF shares has been halted; current NAV and market price are therefore `not disclosed` in this run.
- Official month-end rolling performance as of `2026-07-31`: NAV / market price / MSCI EAFE were YTD `13.89% / 14.20% / 11.59%`, 1-year `26.76% / 27.11% / 24.33%`, 3-year annualized `17.28% / 17.38% / 15.96%`, and 5-year annualized `9.60% / 9.66% / 9.31%`; since inception annualized NAV / market price `7.85% / 7.88%`, with no issuer MSCI EAFE since-inception value. Separate quarter-end values as of `2026-06-30` were not merged.
- Official predecessor disclosure: before close of business `2026-06-12`, the ETF operated as an open-end mutual-fund predecessor with the same objective, strategy and adviser; predecessor NAVs represent pre-listing NAV and market-price return history. The predecessor did not charge a management fee, so its history is not perfectly comparable with the current ETF expense ratio.
- Official portfolio/risk fields as of `2026-07-31`: developed international `97.68%`, United States `2.32%`; Japan `22.97%`, United Kingdom `14.59%`, France `9.79%`, Switzerland `8.80%`, Germany `6.58%`; 3-year standard deviation `12.76%`, 5-year `15.90%`, beta `0.64`, R-squared `43%` versus S&P 500. Issuer cautions that S&P 500 may not represent this international strategy. Sector weights as of `2026-06-30` were Financials `27.83%`, Industrials `19.52%` and Information Technology `12.83%` among the largest exposures.
- Secondary complete-calendar NAV rows from AAII, used only for the calendar-year table and marked `*`: `2018 -12.5%`, `2019 18.5%`, `2020 2.9%`, `2021 16.5%`, `2022 -17.9%`, `2023 20.0%`, `2024 4.6%`, `2025 30.7%`. AAII provides no 2017 row; the partial 2017 inception year is excluded from ranking. AAII’s current YTD `13.9%` agrees with the official issuer field but remains secondary.
- Official strategy-aligned management benchmark: `MSCI EAFE Index (Net) (USD)`, selected because Thrivent explicitly includes MSCI EAFE in its performance table for developed-economy stocks in Europe, Australasia and the Far East. AAII’s MSCI ACWI Ex USA label is rejected as the management comparator because it is secondary and broader than the issuer-selected table comparator.
- Official MSCI EAFE USD net-return annual rows from the July 31, 2026 factsheet: `2018 -13.79%`, `2019 22.01%`, `2020 7.82%`, `2021 11.26%`, `2022 -14.45%`, `2023 18.24%`, `2024 3.82%`, `2025 31.22%`; the same factsheet reports YTD `11.59%`, 1-year `24.33%`, 3-year annualized `15.96%` and 5-year annualized `9.31%`.
- Common S&P 500 Total Return reference uses cached USD dividend-reinvested rows for complete calendar years `2018-2025`: `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`.
- Calculations from secondary rounded TILC rows: 2018-2025 product `1.6741693191`, cumulative `67.4169%`, rounded-input CAGR `6.6535%`, population standard deviation `15.6933%`, and `6 / 2` up/down years. Best `2025 +30.70%`; least positive `2024 +4.60%`; worst `2022 -17.90%`; least-bad down year `2018 -12.50%`.
- Calculations from official MSCI EAFE rows: 2018-2025 product `1.7388292943`, cumulative `73.8829%`, rounded-input CAGR `7.1599%`; 2021-2025 cumulative `53.3220%`, CAGR `8.9233%`. S&P cached calculations for 2018-2025 are product `2.9202828202`, cumulative `192.0283%`, CAGR `14.3347%`; 2021-2025 cumulative `96.1696%`, CAGR `14.4264%`.
- Common 2021-2025 TILC calculation: product `1.569125`, cumulative `56.9125%`, rounded-input CAGR `9.4288%`. Active benchmark comparison: 2018-2025 TILC excess CAGR versus MSCI EAFE `-0.5064 pp`, cumulative relative wealth `-3.7186%`, and annual hit rate `4 / 8`; 2021-2025 excess CAGR `+0.5054 pp`, cumulative relative wealth `+2.3418%`, and annual hit rate `3 / 5`. These arithmetic comparisons are not called alpha.
- Track-record and management evidence: use `track_record: established` under the skill’s elapsed comparable-year rule because eight complete predecessor/ETF rows are available, while the durable page exposes limited live ETF trading history. Use `management_evidence: mixed` because the full 2018-2025 excess CAGR is non-positive but hit rate is exactly 50%, with a positive 2021-2025 subwindow. Use `risk_evidence: mixed` because issuer risk fields are available but compare against an explicitly non-representative S&P 500 reference and daily-NAV drawdown/recovery are not verified.
- Daily NAV maximum drawdown and recovery were not verified. Current price/NAV are not backfilled from the stale AAII last-trade field because Thrivent’s current page reports a trading halt.
- Source map: official product `https://fp.thriventfunds.com/etfs/international-large-cap-etf.html`; SEC prospectus `https://www.sec.gov/Archives/edgar/data/1896670/000119312526200277/d108541d497k.htm`; official MSCI factsheet `https://www.msci.com/documents/10199/255599/msci-eafe-index-usd-net.pdf`; secondary annual/YTD cross-check `https://www.aaii.com/etf/ticker/TILC`; cached S&P references and definition are recorded in the `check-etf-performance` skill and official index page `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`.
- Source integrity review: PASS — official issuer identity, Nasdaq listing, active long-only eligibility, quantitative process, predecessor-history caveat, official current/rolling fields, MSCI EAFE benchmark, official benchmark annual rows, secondary fund annual rows, and trading-halt gap reconcile without mixing return bases or dates.
- Calculation review: PASS — cumulative returns, available-period CAGRs, annual dispersion, S&P comparisons, active benchmark spreads, cumulative relative wealth, hit rates and best/worst subsets were recomputed from the stated rounded rows.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one rolling table, one annual table, required active-management fields, canonical `geography/International` and `geography/global-developed` tags, and existing breadcrumb targets resolve.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/run-5 batches and retained recovery artifacts were dirty before the TILC pre-write boundary; they were not modified or included in this scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NASDAQ_TILC Performance.md`; append this TILC evidence packet and handoff to `raw/imports/ETF_performance_sources_2026-09-01_run-6.md`; no shared navigation file is in this card’s output scope.
- Proposed durable page contents: frontmatter identifies `Nasdaq:TILC`, `active-equity-long-only`, `systematic-active`, quantitative developed-international subtype, `MSCI EAFE Index (Net) (USD)` management benchmark, `track_record: established`, `management_evidence: mixed`, `risk_evidence: mixed`, source batch and International/global-developed tags. Body contains the navigation breadcrumb; Thai-first bottom line with official YTD, halted current quote and predecessor caveat; performance-check identity/metric/benchmark bullets; official 2026-07-31 NAV/market-price/MSCI EAFE rolling table; secondary `*` TILC annual rows for 2018-2025 alongside official MSCI EAFE and cached S&P rows; CAGR, volatility, up/down, best/worst calculations; active-management read-through with benchmark selection, excess CAGR, hit rates, relative wealth, process, tenure and risk status; risk read-through with expense, holdings, exposure, sector and trading-halt gap; and source links.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## TILC research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official active long-only identity and quantitative process, predecessor-history caveat, official current and rolling returns, secondary complete calendar rows, official MSCI EAFE benchmark rows, calculations and scheduled-local review passed with trading-halt and daily drawdown gaps disclosed.
```

## GWX evidence packet

- Input ticker and canonical identity: `GWX`; `NYSE Arca:GWX`; fund: State Street SPDR S&P International Small Cap ETF; inception `2007-04-20`; listing currency USD; semi-annual distributions.
- Official classification: `passive-index`; State Street says GWX seeks to track the `S&P Developed Ex-U.S. Under USD2 Billion Index` before fees and expenses through index sampling. The fund targets developed-market companies outside the United States with market capitalization under USD 2 billion. No leveraged, inverse, option-income, bond, commodity, currency or derivative-defined payoff was identified.
- Later dated official fund/market snapshot retained from the State Street product page: NAV `USD 46.56`, closing price `USD 46.71`, bid/ask midpoint `USD 46.58`, premium/discount `0.05%`, shares outstanding `20.20M` and AUM `USD 940.44M`, all as of `2026-08-26`.
- Official current characteristics retained from the same later dated capture as of `2026-08-26`: `2,081` holdings, P/B `1.36`, forward P/E `14.21`, weighted average market cap `USD 1,639.23M`, 30-day SEC yield `1.87%`, fund distribution yield `2.57%`, and index dividend yield `2.41%`. Sector weights as of `2026-08-25` were Industrials `22.35%`, Materials `15.62%`, Information Technology `13.94%`, Consumer Discretionary `10.87%`, and Financials `8.78%`.
- Official standardized NAV Total Return from the later State Street capture as of `2026-07-31`: YTD `7.28%`, 1-year `19.13%`, 3-year annualized `13.82%`, 5-year annualized `5.15%`, 10-year annualized `6.86%`, since-inception annualized `4.49%`; issuer-index YTD `5.91%` and 10-year `6.64%`. Returns assume reinvestment of dividends/capital gains and are net of fund fees. Market-value return remains separate.
- Fresh source recheck on `2026-09-01` reopened the same official product URL and the official June 2026 factsheet. The dynamic text capture exposed an older page snapshot with NAV `USD 43.22`, AUM `USD 860.02M`, holdings `2,083` and performance only through `2026-06-30`; those values are earlier than the retained 2026-08-26 / 2026-07-31 observations. The later dated official capture is kept, and the stale dynamic snapshot is recorded as a source-timing conflict rather than used to overwrite newer evidence.
- Official factsheet as of `2026-06-30` separately reports NAV YTD `8.18%`, market-value return `8.52%`, issuer-index return `6.77%`, 1-year NAV `21.24%`, 3-year `15.84%`, 5-year `5.32%`, 10-year `7.58%`, and holdings `2,083`; these are not mixed with the later July/August fields. The SEC prospectus separately reports 10-year NAV TR `7.00%` through `2025-12-31`; it is a different as-of observation.
- Complete calendar-year NAV rows, raw 10-year endpoints, volatility/beta and daily NAV history sufficient for maximum drawdown/recovery were not disclosed in the reviewed official sources. A secondary annual-return table was reviewed previously but excluded because its 2025 `35.86%` conflicted with the official SEC prospectus NAV result `35.00%` through 2025-12-31. No secondary annual proxy, calendar CAGR, up/down count or best/worst ranking is saved.
- Common S&P 500 Total Return reference remains the cached USD dividend-reinvested convention for 2016-2025, as of `2025-12-31`; it is shown only as a common reference and is not used to fill GWX annual gaps. Cached 2021-2025 S&P rows are `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`.
- Source map: official product `https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-international-small-cap-etf-gwx`; official factsheet `https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-gwx.pdf`; SEC prospectus `https://www.sec.gov/Archives/edgar/data/1168164/000119312526031217/d833468d497k.htm`; prior secondary conflict source `https://assetsanalyzer.com/etf/GWX/performance`; cached S&P definition `https://www.spglobal.com/spdji/en/indices/equity/sp-500/` and workflow cache.
- Source integrity review: PASS with disclosed source-timing conflict — issuer identity, exchange, passive structure, benchmark, later dated NAV/price/fund facts, July standardized returns and earlier June factsheet are date-separated; the stale dynamic recheck is not substituted for later official observations.
- Calculation review: PASS — only the official rolling fields and cached S&P reference claims are retained; no unsupported annual CAGR, risk statistic, drawdown, recovery or mixed-date calculation is produced.
- Format and graph review: PASS for card-specific output — Thai-first narrative, one annual table with undisclosed GWX rows rather than a conflicted proxy, canonical `geography/International` and `geography/global-developed` tags, and existing breadcrumb targets resolve.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/run-5 batches and retained recovery artifacts were dirty before the GWX pre-write boundary; they were not modified or included in this scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: refresh `wiki/analysis/performance/ETF_NYSE_ARCA_GWX Performance.md`; append this GWX evidence packet and handoff to `raw/imports/ETF_performance_sources_2026-09-01_run-6.md`; no shared navigation file is in this card’s output scope.
- Proposed durable page contents: retain the canonical `NYSE Arca:GWX` identity, passive/index-tracking classification, S&P Developed Ex-U.S. Under USD2 Billion Index, 10-year issuer average annual `6.86%`, official July YTD `7.28%`, later August NAV/price/fund facts, a single annual table with `not disclosed` GWX cells and cached S&P references, explicit no-proxy/no-drawdown gaps, the fresh stale-snapshot conflict note, risk/sector notes, canonical breadcrumb/tags and source links; update only `updated`, `source_batch`, `return_basis`, `primary_region`, tags and refresh/source-note text.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## GWX research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive international small-cap identity, later dated current fund facts and July standardized returns, explicit annual-data conflict/gaps, calculations limited to verified fields and scheduled-local review passed.
```

## IDOG evidence packet

- Input ticker and canonical identity: `IDOG`; official issuer and prospectus identify `NYSE Arca:IDOG`; fund: ALPS International Sector Dividend Dogs ETF; CUSIP `00162Q718`; inception `2013-06-27`; existing vault filename `ETF_AMEX_IDOG Performance.md` is retained as a legacy alias while the entity key and exchange are canonical NYSE Arca.
- Official classification: `passive-index`; ALPS states that IDOG seeks to replicate the S-Network International Sector Dividend Dogs Index (`IDOGX`) before fees and expenses and explicitly says the fund employs a passive/indexing approach. The index starts from developed international markets outside the Americas, selects the five highest-yielding stocks in each of ten GICS sectors and equally weights the selected portfolio. No leveraged, inverse, option-income, bond, commodity, currency or derivative-defined payoff was identified.
- Official July performance update: the ALPS source reports cumulative NAV / market-price / IDOGX index NTR of 1-month `6.14% / 6.12% / 6.20%`, YTD `16.08% / 16.38% / 16.09%`, and 1-year `34.75% / 35.03% / 35.11%` as of `2026-07-31`; it reports annualized NAV / market price / index of 3-year `27.34% / 27.17% / 27.69%`, 5-year `13.05% / 13.11% / 13.43%`, 10-year `10.66% / 10.60% / 11.06%`, and since inception `8.41% / 8.44% / 8.82%`, with the source note stating cumulative fields are as of 2026-07-31 and annualized fields as of 2026-06-30.
- Official June 30, 2026 factsheet separately reports NAV / market-price / IDOGX NTR YTD `9.40% / 9.85% / 9.32%`, 1-year `27.38% / 27.53% / 27.69%`, 3-year annualized `19.06% / 19.06% / 19.47%`, 5-year `13.07% / 13.19% / 13.44%`, 10-year `10.65% / 10.58% / 11.06%`, and since inception `8.42% / 8.47% / 8.82%`. The June values remain a separate dated official observation and are not merged with the July update.
- Official fund facts: total operating expenses `0.50%`, net assets `USD 516.45M`, quarterly distributions, and the June factsheet’s sector allocations Financials `10.61%`, Health Care `10.35%`, Industrials `10.31%`, Consumer Staples `10.27%`, Utilities `10.21%`, Consumer Discretionary `10.05%`, Materials `9.84%`, Information Technology `9.67%`, Communication Services `9.48%`, and Energy `9.20%`, all as of `2026-06-30`. The March 31, 2026 summary prospectus reports portfolio turnover `53%` for the fiscal year ended 2025-11-30.
- Official annual NAV Total Return rows captured from the ALPS issuer performance table on `2026-07-02`: `2016 3.97%`, `2017 25.81%`, `2018 -13.09%`, `2019 20.86%`, `2020 -1.34%`, `2021 11.36%`, `2022 -4.23%`, `2023 22.64%`, `2024 1.53%`, `2025 39.83%`. The source states performance includes reinvested distributions and capital gains; market-price and index returns remain separate.
- Rounded-input annual calculations from the official rows: 2016-2025 product `2.5171103340`, cumulative `151.7110%`, CAGR `9.6706%`, population standard deviation `15.4476%`, and `7 / 3` up/down years. Best `2025 +39.83%`; least positive `2024 +1.53%`; worst `2018 -13.09%`; least-bad down year `2020 -1.34%`. 2021-2025 product `1.8568875114`, cumulative `85.6888%`, CAGR `13.1767%`.
- Common S&P 500 Total Return reference uses cached USD dividend-reinvested rows for complete calendar years `2016-2025`: `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, cached as of `2025-12-31`. Calculations are cumulative `298.3291%` / CAGR `14.8218%` for 2016-2025 and cumulative `96.1696%` / CAGR `14.4264%` for 2021-2025; S&P is a common reference, not IDOGX’s issuer benchmark.
- Official ALPS page’s dynamic pricing/performance fields were blank in the current text capture. Secondary observations retained only as a dated cross-check are market price `USD 44.30` as of `2026-08-28` from FinanceCharts and closing NAV `USD 44.79` as of `2026-08-25` from Schwab. They are not used in NAV Total Return calculations; current official daily NAV, standard deviation, max drawdown and recovery remain `ไม่พบข้อมูลที่ยืนยันได้`.
- Source map: official product `https://www.alpsfunds.com/exchange-traded-funds/idog`; official July performance update `https://www.alpsfunds.com/perspectives/etf-spotlights/idog-cyclical-strength-pays-international-dividends-20260806?hs_amp=true`; official factsheet `https://www.alpsfunds.com/hubfs/alps-docs/lit/fs/alps-international-sector-dividend-dogs-etf-idog-fs.pdf`; official summary prospectus `https://www.alpsfunds.com/hubfs/alps-docs/reg/sum-pro/alps-international-sector-dividend-dogs-etf-idog-sum-pro.pdf`; secondary price `https://www.financecharts.com/etfs/IDOG/summary/price`; secondary NAV `https://www.schwab.wallst.com/Prospect/Research/etfs/summary.asp?symbol=IDOG`; cached S&P definition `https://www.spglobal.com/spdji/en/indices/equity/sp-500/` and workflow cache.
- Source integrity review: PASS — official NYSE Arca identity, passive eligibility, index construction, fees, official July rolling update, June factsheet and official calendar rows reconcile; older/current fields are separated by as-of date, and secondary price/NAV are clearly marked and excluded from NAV TR.
- Calculation review: PASS — 2016-2025 and 2021-2025 cumulative returns, CAGRs, population dispersion, up/down count and best/worst subsets were recomputed from the stated official rounded annual rows; no market-price or cross-date series was mixed into the calculations.
- Format and graph review: PASS for card-specific output — Thai-first narrative, one official rolling table, one annual table, canonical `NYSE Arca:IDOG` identity, `geography/International` and `geography/global-developed` tags, and existing breadcrumb targets resolve.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/run-5 batches and retained recovery artifacts were dirty before the IDOG pre-write boundary; they were not modified or included in this scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: refresh `wiki/analysis/performance/ETF_AMEX_IDOG Performance.md`; append this IDOG evidence packet and handoff to `raw/imports/ETF_performance_sources_2026-09-01_run-6.md`; no shared navigation file is in this card’s output scope.
- Proposed durable page contents: expand the existing legacy-filename page frontmatter with canonical exchange, ticker, fund, tracked index, benchmark, as-of dates, return basis, source batch, primary region and tags; update bottom line to official July YTD/rolling fields and corrected annual ranking; add official rolling NAV/market-price/index table; retain the official 2016-2025 annual NAV table with cached S&P reference; add corrected CAGR/volatility/up-down/best-worst calculations; add passive risk read-through with sector/value/dividend, currency, concentration, liquidity and data-gap notes; separate secondary August price/NAV observations; and link all official/secondary sources.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## IDOG research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive international dividend ETF identity, July rolling performance update, official annual NAV rows, corrected up/down ranking, dated secondary price/NAV cross-check and scheduled-local review passed with daily risk-data gaps disclosed.
```

## DMXF evidence packet

- Input ticker: `DMXF`; canonical identity: `NASDAQ:DMXF`; fund: iShares ESG Advanced MSCI EAFE ETF; official inception `2020-06-16`; exchange `NASDAQ`; return currency `USD`.
- Official classification: `passive-index`. iShares describes DMXF as tracking the `MSCI EAFE Choice ESG Screened Index (USD) (Net)`, a free-float-adjusted, market-capitalization-weighted index of developed-market equities excluding the U.S. and Canada with ESG and controversy screens. The reviewed objective does not define a leveraged, inverse, option-income, bond, commodity, currency, multi-asset or derivative-heavy payoff.
- Official current product-page fields as of `2026-08-31`: NAV `USD 86.46`, closing price `USD 86.59`, net assets `USD 959.73m`, premium/discount `0.15%`, holdings `395`, expense ratio `0.12%`, and current NAV Total Return YTD `+16.02%`. The page also reports 3-year standard deviation `14.23%` and equity beta `0.82` as of `2026-07-31`, 12-month trailing yield `4.19%` as of `2026-07-31`, and semi-annual distributions.
- Official rolling performance fields from the product page as of `2026-06-30`: NAV Total Return 1-year `18.74%`, 3-year annualized `15.47%`, 5-year annualized `7.72%`, since inception `11.48%`; 10-year field is not applicable because the fund launched in 2020. These rolling fields are kept date-separated from the August current snapshot.
- Official June 30, 2026 factsheet calendar NAV rows: 2021 `10.92%`, 2022 `-19.18%`, 2023 `20.75%`, 2024 `3.49%`, 2025 `23.04%`. Market-price rows (`10.90%`, `-19.23%`, `20.56%`, `4.02%`, `22.08%`) and issuer benchmark rows (`10.98%`, `-19.40%`, `20.79%`, `3.81%`, `22.63%`) remain separate and are not substituted into the NAV ranking. The factsheet states that growth-of-hypothetical-$10,000 performance assumes reinvestment of dividends and capital gains and deducts fund expenses.
- Common S&P 500 Total Return reference uses the cached USD dividend-reinvested rows for 2021-2025: `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`, reference as of `2025-12-31`.
- Calculations from official DMXF NAV rows: 2021-2025 product `1.3783533174`, cumulative `37.8353%`, rounded-input CAGR `6.6282%`; population standard deviation `15.2065%`; `4 / 1` up/down years. Best `2025 +23.04%`; least positive `2024 +3.49%`; worst and least-bad down year `2022 -19.18%`.
- S&P cached calculation for 2021-2025: product `1.9616961801`, cumulative `96.1696%`, rounded-input CAGR `14.4264%`. Annual DMXF-minus-S&P differences are `-17.79`, `-1.07`, `-5.54`, `-21.53` and `+5.16` percentage points; cumulative relative wealth `(1+DMXF)/(1+S&P)-1` is `-29.7367%`. These are arithmetic comparisons, not alpha.
- Official distributions shown on the current page: ex-date/payable date `2026-06-15/2026-06-18`, total distribution `USD 1.032946`; `2025-12-16/2025-12-19`, `USD 2.504331`; `2025-06-16/2025-06-20`, `USD 1.140518`; `2024-12-17/2024-12-20`, `USD 0.884233`. No distribution forecast is inferred.
- Official daily NAV observations sufficient for maximum drawdown and recovery were not verified; `risk-adjusted evidence: not-verified` for those fields. The 2020 inception partial is excluded from annual ranking. No secondary annual proxy or shorter-period 10-year CAGR is used.
- Source map: official product/performance `https://www.ishares.com/us/products/314362/ishares-esg-advanced-msci-eafe-etf`; official factsheet `https://www.ishares.com/us/literature/fact-sheet/dmxf-ishares-esg-advanced-msci-eafe-etf-fund-fact-sheet-en-us.pdf`; Nasdaq listing circular `https://www.nasdaqtrader.com/content/newsalerts/2020/infocircular/DMXF%20USXF%20ETF%20Circular.pdf`; cached S&P convention and official definition `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`.
- Source integrity review: PASS — official identity, NASDAQ exchange, passive equity classification, benchmark, inception, expense ratio, NAV/market-price separation, annual rows, current fields, distribution records and dated rolling fields reconcile without mixed return bases.
- Calculation review: PASS — annual compounding, CAGR, standard deviation, S&P comparison, relative wealth, year counts and best/worst subsets were recomputed from the stated rounded rows; partial 2020 was excluded.
- Format and graph review: PASS for card-specific output — Thai-first narrative, one annual table, required sections, canonical `geography/International` and `geography/global-developed` tags, and the existing International breadcrumb targets resolve. Shared navigation/index/log files were already dirty before this card's pre-write boundary and remain outside this scoped output.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NASDAQ_DMXF Performance.md`; update this source batch; no shared navigation/index/log file is in this card's output scope because those files were dirty before the retained lease.
- Proposed durable page contents: complete DMXF performance page with official identity, passive classification, current August snapshot, 2021-2025 NAV/S&P table, calculations, distribution dates, risk gaps, breadcrumb, canonical tags and source links.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## DMXF research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive developed-equity identity, current August NAV/YTD, official 2021-2025 NAV rows, cached S&P comparison, calculations and scheduled-local review passed with daily drawdown and recovery data gaps disclosed.
```

## DMXF queue route outcome

- The downstream `research_handoff` was complete and passed the scheduled-local research gate, but queue routing stopped globally before commit with `durable-output-scope-mismatch`: the card's intake-planned path was `wiki/analysis/performance/ETF_NYSE_ARCA_DMXF Performance.md`, while the official exchange verification required and the written page used `wiki/analysis/performance/ETF_NASDAQ_DMXF Performance.md`.
- The retained project lease was released by the global-block route. No other card was researched or mutated; the nine unstarted cards were restored to their exact pre-run `Ready` snapshots. The DMXF page and this source-batch append remain uncommitted for controlled path reconciliation.
```
