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
