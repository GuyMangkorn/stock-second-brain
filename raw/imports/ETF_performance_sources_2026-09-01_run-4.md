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

# ETF Performance Sources — 2026-09-01 Run 4

This dated batch records the source-backed evidence and local pre-save review for cards processed by the scheduled-inline `research-queue-manager` run. Shared navigation/index files were already dirty before this run and remain outside each card's clean output scope.

## DDWM evidence packet

- Input ticker: `DDWM`; canonical identity: `Cboe BZX:DDWM`; fund: WisdomTree Dynamic International Equity Fund; inception `2016-01-07`.
- Official classification: `passive-index` international equity fund. WisdomTree describes a rules-based process tracking dividend-paying developed-market companies outside the U.S. and Canada with a monthly dynamic currency hedge; the hedge is implementation risk, not a leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff structure.
- Official product snapshot: expense ratio `0.40%`, NAV `$47.511` as of `2026-08-31`, closing market price `$47.534` as of `2026-08-28`, and aggregate hedge ratio `83.67%` as of `2026-08-31`.
- Official month-end performance as of `2026-07-31`: NAV Total Return 1-month `1.91%`, 3-month `4.77%`, YTD `9.70%`, since inception cumulative `187.23%`; NAV annualized 1-year `21.49%`, 3-year `17.40%`, 5-year `13.19%`, 10-year `10.41%`, since-inception `10.50%`. Market-price returns remain separate.
- Official annual NAV Total Return rows for complete calendar years: 2016 `14.18%`, 2017 `18.52%`, 2018 `-11.05%`, 2019 `21.03%`, 2020 `-4.20%`, 2021 `14.33%`, 2022 `-1.27%`, 2023 `15.44%`, 2024 `10.65%`, 2025 `30.10%`. The issuer presentation states NAV total returns use daily 4:00 p.m. NAV and distributions are included; raw endpoints for the rolling 10-year field are not disclosed.
- Official issuer benchmark metadata: WisdomTree Dynamic International Equity Index (`WTDFAHD`), a fundamentally weighted dividend-paying developed ex-U.S./Canada index with a monthly 0%-100% rules-based currency hedge. The common comparison remains S&P 500 Total Return in USD with dividends reinvested.
- Cached S&P 500 TR rows for the same 2016-2025 USD total-return basis: 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; cached reference as of `2025-12-31`.
- Calculations from official DDWM rows: product `2.6180657529`, cumulative `161.8066%`, rounded-input 2016-2025 CAGR `10.1027%`, population standard deviation `11.9594%`; 2021-2025 product `1.8758338709`, cumulative `87.5834%`, rounded-input CAGR `13.4067%`, population standard deviation `10.0566%`; S&P 500 product `3.9832911148`, cumulative `298.33%`, CAGR `14.82%`.
- Annual-path risk: 8 up years / 2 down years; best `2025 +30.10%`; least positive `2024 +10.65%`; worst `2018 -11.05%`; least bad down year `2022 -1.27%`. The official presentation reports 10-year annualized NAV volatility `12.41%` as of `2026-03-31`; daily NAV drawdown and exact recovery date were not verified.
- Source map: official product/performance page `https://www.wisdomtree.com/us/products/equity/ddwm`; official presentation `https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/presentations/equity/ddwm_presentation.pdf`; official index page `https://www.wisdomtree.com/us/indexes/WTDFAHD`; Cboe listed-symbols cross-check `https://www.cboe.com/us/equities/market_statistics/listed_symbols/`; secondary AAII cross-check `https://www.aaii.com/etf/ticker/DDWM`; S&P cached source URLs are the standard references recorded in the skill.
- Source integrity review: PASS — current NAV, month-end NAV TR, official annual NAV rows, benchmark metadata, exchange identity and market-price separation reconcile; rolling 10-year raw endpoints and daily drawdown/recovery remain explicitly undisclosed.
- Calculation review: PASS — cumulative return, CAGRs, population standard deviation, year counts and best/worst subsets were recomputed from the stated official annual rows; no partial year was ranked.
- Format and graph review: PASS for the card-specific outputs — Thai-first narrative, one annual table, required sections, canonical `geography/International` tag and breadcrumb resolve to existing pages.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, the prior run-3 batch, and retained recovery artifacts were dirty before this card's pre-write boundary; they were not modified or included in the DDWM scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: update `wiki/analysis/performance/ETF_CBOE_DDWM Performance.md`; create/update `raw/imports/ETF_performance_sources_2026-09-01_run-4.md`; no shared navigation file is in this card's output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## DDWM research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official identity, NAV total-return history, current YTD/NAV fields, benchmark metadata, calculations and scheduled-local review passed with source gaps disclosed.
```

## TOUS evidence packet

- Input ticker: `TOUS`; canonical identity: `NYSE Arca:TOUS`; fund: T. Rowe Price International Equity ETF; inception `2023-06-14`.
- Official classification: `active-equity-long-only`, `fundamental-active`. The January 2026 summary prospectus states the fund normally invests at least 80% in equities and at least 65% in non-U.S. stocks, primarily in developed markets; adviser decision-making focuses on bottom-up stock selection. No payoff-defining leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-heavy structure was identified.
- Official factsheet as of `2026-06-30`: benchmark `MSCI EAFE Index Net`, expense ratio `0.50%`, total assets `USD 1,525,974,857`, portfolio turnover `29.2%` for the one-year period ending `2025-12-31`, and official NAV YTD `11.34%`, 1-year `20.64%`, 3-year annualized `17.53%`, since-inception annualized `17.03%`. The factsheet states total return reflects reinvested dividends and capital gains.
- Official complete calendar NAV/benchmark rows: 2024 fund `3.72%`, benchmark `3.82%`; 2025 fund `33.69%`, benchmark `31.22%`. 2023 is a June 14 inception-year partial and is excluded from complete-year rankings. Market-price rows remain separate.
- Latest current secondary cross-check: Schwab reports TOUS NAV YTD `+12.8%`, 1-month `+1.3%`, 3-month `+6.4%`, 6-month `+6.9%`, 1-year `+25.0%`, 3-year annualized `+17.0%`, and inception-period annualized `+17.0%`, all as of `2026-07-31`; the secondary closing price is `$39.75` as of `2026-08-28`.
- Active benchmark selection: `MSCI EAFE Index Net` is the official issuer-designated comparator and matches the fund's primarily developed non-U.S./non-Canadian international equity universe; no alternative official benchmark was preferred.
- Cached S&P 500 TR rows for 2024-2025: 2024 `25.02%`, 2025 `17.88%`; cached USD total-return convention as of `2025-12-31`.
- Calculations from official 2024-2025 rows: fund product `1.3866326800`, cumulative `38.6633%`, rounded-input CAGR `17.7554%`, population standard deviation `14.9850%`; management benchmark product `1.3623260400`, cumulative `36.2326%`, CAGR `16.7187%`; S&P product `1.4737357600`, cumulative `47.3736%`, CAGR `21.3975%`.
- Active evidence: Excess CAGR `+1.0366 pp`, complete-year hit rate `1/2 = 50.00%`, cumulative relative wealth `+1.7842%`. This is `provisional` / `positive` evidence only; it is not called alpha and does not establish persistent manager skill.
- Risk and continuity: two-year annual-path up/down count `2 / 0`; best `2025 +33.69%`; least positive `2024 +3.72%`; no complete-year down observation; daily NAV volatility, drawdown and recovery were not verified. June factsheet lists Jodi Love and Colin McQueen managed since 2023, Jordan Pryor and Richard Clattenburg since 2025; attribution remains at the adviser-process level.
- Source conflict: current January 2026 summary prospectus reports turnover `34.7%`, while June 2026 factsheet reports `29.2%` for a one-year period ending 2025-12-31. Both are preserved rather than silently reconciled.
- Source map: official factsheet `https://www.troweprice.com/literature/public/country/us/language/en/literature-type/quarterly-factsheet/sub-type/etf-single-class?productCode=INX`; official summary prospectus `https://www.troweprice.com/literature/public/country/us/language/en/literature-type/summary-prospectus/sub-type/etf?currency=USD&productCode=INX`; SEC exchange cross-check `https://www.sec.gov/Archives/edgar/data/1795351/000109926326000010/xslFormN-CEN_X05/primary_doc.xml`; secondary Schwab `https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=tous`; secondary AAII `https://www.aaii.com/etf/ticker/TOUS`.
- Source integrity review: PASS — official identity, exchange, active equity eligibility, management benchmark, return definition, complete-year rows, secondary current YTD, and turnover conflict are separated and dated.
- Calculation review: PASS — cumulative returns, CAGRs, annual standard deviation, active spread, hit rate, relative wealth and best/worst subset were recomputed from the stated compatible rows; 2023 partial year was excluded.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, active-management fields, risk/source sections, canonical `geography/International` tag and breadcrumb resolve to existing pages.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, the prior run-3 batch and retained recovery artifacts were dirty before this card's pre-write boundary; they were not modified or included in the TOUS scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NYSE_ARCA_TOUS Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-4.md`; no shared navigation file is in this card's output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## TOUS research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official active eligibility, issuer benchmark, compatible NAV rows, current secondary YTD, calculations and scheduled-local review passed with provisional evidence and source conflict disclosed.
```
