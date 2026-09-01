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

## DISV evidence packet

- Input ticker: `DISV`; canonical identity: `Cboe BZX:DISV`; fund: Dimensional International Small Cap Value ETF; inception `2022-03-23`; listing `2022-03-24`.
- Official classification: `active-equity-long-only`, `systematic-active`. The February 28, 2026 SEC summary prospectus identifies an actively managed ETF investing primarily in small non-U.S. developed-market equities. Swaps, futures, options on futures and FX forwards are described for exposure, cash-flow or currency management; they do not define a leveraged, inverse, option-income, bond, commodity, currency, multi-asset or derivative-heavy payoff.
- Official SEC expense/turnover fields: total annual fund operating expenses `0.42%` (`0.39%` management fee plus `0.03%` other expenses) and latest fiscal-year portfolio turnover `8%`; official Dimensional quick-guide cross-check reports gross `0.43%` / net `0.42%` as of `2025-12-31`.
- Official annual NAV Total Return chart rows for complete years: 2023 `19.60%`, 2024 `6.02%`, 2025 `47.24%`; the 2022 launch year is partial and excluded. Official return definition includes reinvested distributions and fund expenses; market-price return remains separate.
- Official management benchmark: `MSCI World ex USA Small Value Index (net dividends)`, selected because the SEC performance table explicitly identifies it as an additional index with a similar investment universe. The broader MSCI World ex USA Index and S&P 500 remain rejected as management comparators; S&P is only the common reference benchmark.
- Official annualized performance as of `2025-12-31`: 1-year DISV NAV `47.24%` versus selected management benchmark `38.55%`; since-inception annualized DISV `14.78%` versus benchmark `10.38%`. Compatible annual benchmark rows and a complete-year hit rate are not disclosed.
- Latest secondary current fields as of `2026-07-31`: NAV YTD `12.90%`, 1-year `31.90%`, 3-year annualized `22.40%`, since-inception annualized `15.90%`; secondary closing price `$44.63` as of `2026-08-31`.
- Cached S&P 500 TR rows for the same years: 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; cached USD total-return convention as of `2025-12-31`.
- Calculations from official DISV rows: product `1.8669664000`, cumulative `86.6966%`, rounded-input CAGR `23.1420%`, population standard deviation `17.1513%`; S&P product `1.8611808913`, cumulative `86.1181%`, CAGR `23.0066%`.
- Active evidence: official since-inception Excess CAGR `+4.40 pp` over 2022-03-23 to 2025-12-31; `management_evidence: positive return-only` because compatible annual benchmark rows/hit rate are unavailable; `track_record: provisional` at the latest evidence date. This is not called alpha.
- Annual-path risk: up/down count `3 / 0`; best `2025 +47.24%`; least positive `2024 +6.02%`; no complete down year; official highest quarter `+15.12%` in 2025 Q2 and lowest quarter `-7.54%` in 2024 Q4. Daily NAV max drawdown and exact recovery were not verified, so `risk_evidence: not-verified`.
- Adviser/team continuity: Dimensional describes an integrated research, portfolio-design, portfolio-management and trading process; the SEC prospectus names Jed S. Fogdall, Joseph F. Hohn and Joel P. Schneider as portfolio managers since inception and Brendan J. McAndrews since 2025. Attribute evidence to the disclosed strategy/adviser process rather than individual skill.
- Source map: official SEC summary prospectus `https://www.sec.gov/Archives/edgar/data/1816125/000181612526000069/c497k.htm`; official Dimensional fund page `https://www.dimensional.com/us-en/funds/disv/international-small-cap-value`; official ETF quick guide `https://my.dimensional.com/chmedia/282748/source/dimensional-etf-quick-guide.pdf`; official Cboe listing `https://www.cboe.com/us/equities/listings/listed_products/symbols/DISV`; secondary Schwab `https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=disv`; official S&P index page `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`.
- Source integrity review: PASS — active equity eligibility, process subtype, strategy-aligned benchmark, official annual rows, secondary current fields, return bases, dates and derivative-use context reconcile; no predecessor mutual-fund history is merged.
- Calculation review: PASS — annual cumulative return, CAGR, standard deviation, S&P comparison, year counts and best/worst subsets were recomputed from the stated official rows; the official since-inception benchmark spread is kept separate from annual hit-rate evidence.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, active-management fields, risk/source sections, canonical `geography/International` tag and breadcrumb resolve to existing pages.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, the prior run-3 batch and retained recovery artifacts were dirty before this card's pre-write boundary; they were not modified or included in the DISV scoped commit. Region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: update `wiki/analysis/performance/ETF_CBOE_BZX_DISV Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-4.md`; no shared navigation file is in this card's output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## DISV research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official active classification, strategy benchmark, annual NAV rows, current secondary YTD, calculations and scheduled-local review passed with return-only evidence and risk gaps disclosed.
```

## IIREF evidence packet

- Card reread: operational frontmatter identifies input ticker `IIREF`, workflow `check-etf-performance`, and an In Progress claim with fencing token `f260551088974e45b236b30799080e63`; the body contains stale URTH template text and was not treated as evidence because queue operational state is frontmatter-controlled.
- Input alias and canonical identity: `IIREF` is an OTC USD quote for the named iShares MSCI World UCITS ETF; official iShares identifies ISIN `IE00B0M62Q58` and maps the USD London Stock Exchange listing to `IDWR`. Canonical identity is `LSE:IDWR`; the issuer's `IWRD` page name and GBP line are preserved as the same share class's alternate listing metadata.
- Official classification: `passive-index`, physical/optimised developed-market equity UCITS ETF. The official KIID says the USD distributing share class seeks to reflect the MSCI World Index and may use optimising techniques; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified.
- Official product-page snapshot as of `2026-08-28`: NAV `USD 106.25`, NAV Total Return YTD `13.27%`, net assets `USD 9,563,943,154`, holdings `1,282`, total expense ratio `0.50%`, benchmark `MSCI World Index (Net)`, quarterly distribution and USD share-class currency.
- Official risk/portfolio fields: standard deviation `12.44%` and beta `1.000` as of `2026-07-31`; P/E `26.46`, P/B `4.15`, trailing distribution yield `0.85%`, and sector weights Information Technology `29.55%`, Financials `16.52%`, Industrials `11.21%` as of `2026-08-28`. Securities lending return was `0.02%` for the period ending `2026-06-30`.
- Official factsheet rolling snapshot as of `2026-05-31`: fund/benchmark YTD `10.06% / 10.26%`, 1-year `20.03% / 20.41%`, 3-year annualized `17.84% / 18.14%`, 5-year annualized `10.93% / 11.19%`, since-inception annualized `8.83% / 9.04%`. These are kept separate from the newer August YTD field.
- Official complete calendar NAV rows: 2016 `7.51%`, 2017 `22.26%`, 2018 `-8.89%`, 2019 `27.35%`, 2020 `15.59%`, 2021 `21.49%`, 2022 `-18.31%`, 2023 `23.55%`, 2024 `18.39%`, 2025 `20.75%`; official MSCI World Net rows: `7.51%`, `22.40%`, `-8.71%`, `27.67%`, `15.90%`, `21.82%`, `-18.14%`, `23.79%`, `18.67%`, `21.09%`.
- Latest secondary market-price cross-check for canonical USD line: `USD 106.16` at 10:32 BST on `2026-08-31`; historical 28 Aug close `USD 106.79`. The price is marked secondary and is not mixed into NAV performance.
- Cached S&P 500 TR rows for 2016-2025: 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; cached USD total-return convention as of `2025-12-31`.
- Calculations from official rows: 2016-2025 fund product `3.0901022540`, cumulative `209.0102%`, rounded-input CAGR `11.9431%`, population standard deviation `14.3544%`; benchmark product `3.1531955215`, cumulative `215.3196%`, CAGR `12.1696%`; 2021-2025 fund product `1.7528886858`, cumulative `75.2889%`, CAGR `11.8796%`; benchmark product `1.7738836057`, cumulative `77.3884%`, CAGR `12.1463%`; cached S&P product `3.9832911148`, cumulative `298.3291%`, CAGR `14.8218%`.
- Annual-path risk: fund up/down `8 / 2`; best `2019 +27.35%`; least positive `2016 +7.51%`; worst `2022 -18.31%`; least bad down year `2018 -8.89%`; 2021-2025 up/down `4 / 1`. Daily NAV drawdown and recovery series were not verified.
- Source map: official iShares product page `https://www.ishares.com/uk/individual/en/products/251881/ishares-msci-world-ucits-etf`; official factsheet `https://www.ishares.com/uk/individual/en/literature/fact-sheet/iwrd-ishares-msci-world-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true`; official KIID `https://www.ishares.com/uk/individual/en/literature/kiid/ucits_kiid-ishares-msci-world-ucits-etf-usd-dist-gb-ie00b0m62q58-en.pdf?siteEntryPassthrough=true&switchLocale=y`; OTC alias cross-check `https://stockanalysis.com/quote/otc/IIREF/history/`; secondary IDWR quote `https://markets.investorschronicle.markitdigital.com/data/etfs/tearsheet/historical?s=IDWR%3ALSE%3AUSD`; S&P official index page `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`.
- Source integrity review: PASS — official ISIN, USD share-class/listing mapping, passive equity eligibility, benchmark, return definition, current YTD/NAV, complete calendar rows, risk fields and secondary price separation reconcile; stale URTH body text is excluded from evidence.
- Calculation review: PASS — cumulative returns, CAGRs, population standard deviation, benchmark spread, year counts and best/worst subsets were recomputed from the stated rounded official rows; rolling factsheet fields remain date-separated from the current product-page YTD.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, canonical `geography/International` tag and breadcrumb resolve to existing pages; no shared navigation file was changed.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/recovery artifacts and pre-existing dirty outputs remain outside this card's scope; region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_LSE_IDWR Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-4.md`; no shared navigation file is in this card's output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## IIREF research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official USD share-class identity, NAV total-return history, current YTD/NAV fields, benchmark metadata, calculations and scheduled-local review passed with alias and risk gaps disclosed.
```

## SEIE evidence packet

- Input ticker and identity: `SEIE`; official SEI ETF page and SEC annual shareholder report identify `SEI Select International Equity ETF`, primary exchange `Nasdaq`, CUSIP `81589A700`. The July 31, 2026 summary prospectus states commencement of operations `2024-10-08`; the issuer ETF page displays `2024-10-10`, so the date discrepancy is preserved and the prospectus date is used for maturity assessment.
- Official classification: `active-equity-long-only`, integrated quantitative plus multi-manager model-portfolio process. SEI combines its own quantitative active stock portfolio with Brown Advisory and Pzena model portfolios; latest factsheet allocation is SEI `70%`, Pzena `20%`, Brown Advisory `10%`.
- Strategy/benchmark: at least 80% equity, at least 40% outside the U.S., primarily developed markets with possible emerging-market exposure; official management benchmark `MSCI EAFE Index (Net) (USD)`. S&P 500 is only a common USD reference.
- Official fees and turnover: total annual fund operating expenses `0.50%`; most recent fiscal-year portfolio turnover `70%` in the July 31, 2026 summary prospectus.
- Official current factsheet performance: NAV YTD `13.46%` versus benchmark `11.59%` and since-inception cumulative `25.69%` versus `20.12%`, cumulative column as of `2026-07-31`; NAV 1-year `23.57%` versus `20.23%` and since-inception annualized `24.66%` versus `19.21%`, annualized column as of `2026-06-30`.
- Official complete calendar row: 2025 SEIE NAV Total Return `38.96%` versus MSCI EAFE net `31.89%`; 2024 is a partial inception year and excluded. Cached S&P 500 TR reference for 2025 is `17.88%`.
- Active evidence: return-only spread `+7.07 pp` for 2025, `+1.87 pp` current YTD, and `+5.45 pp` since-inception annualized at their respective as-of dates. Evidence is `positive return-only` but `provisional` because only one complete calendar year is available; it is not called alpha.
- Risk/portfolio snapshot: issuer page as of `2026-08-27` reports NAV `$37.03`, closing price `$37.18`, net assets `$1.31bn`, shares outstanding `35,375,000`, holdings `357`, and 30-day SEC yield `2.12%`; July factsheet reports 346 holdings, P/B `1.90x`, median forward P/E `14.02x`, beta `0.94`, and standard deviation `N/A`. Full daily drawdown/recovery and risk-adjusted evidence were not verified.
- Annual-path risk: one complete-year observation, up/down `1 / 0`, best and least positive `2025 +38.96%`; no complete down year is ranked. The official prospectus reports best quarter `13.56%` (2025 Q2) and worst quarter `5.09%` (2025 Q3), both positive and not a drawdown series.
- Source map: official SEI strategy page `https://www.seic.com/financial-advisors/flexible-investment-solutions/etfs/select-etfs/sei-select-international-equity-etf-seie`; official ETF page `https://seietfs.filepoint.live/seie`; official fact sheet `https://seietfs.filepoint.live/assets/pdfs/SEIE_FactSheet.pdf`; official summary prospectus `https://seidocs.filepoint.live/assets/pdfs/Summary_Prospectuses/SEIE_Summary-Prospectus.pdf`; SEC annual report `https://www.sec.gov/Archives/edgar/data/1888997/000139834426010415/fp0099233-1_ncsrixbrl.htm`; secondary price history `https://stockanalysis.com/etf/seie/history/`; S&P official index page `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`.
- Source integrity review: PASS — official Nasdaq identity, active equity eligibility, process subtype, official strategy benchmark, date-separated current fields, one complete calendar row, current risk snapshot and secondary price separation reconcile; inception-date discrepancy is disclosed.
- Calculation review: PASS — 2025 benchmark spread and date-specific YTD/since-inception spreads were recomputed from the stated official fields; no partial 2024 year was ranked and no unsupported CAGR or volatility was inferred.
- Format and graph review: PASS for card-specific outputs — Thai-first narrative, one annual table, required active-management fields, canonical `geography/International` tag and breadcrumb resolve to existing pages; no shared navigation file was changed.
- Shared navigation note: `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, `log.md`, prior run-3/recovery artifacts and pre-existing dirty outputs remain outside this card's scope; region/index/log reconciliation is deferred to a clean navigation pass.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NASDAQ_SEIE Performance.md`; update `raw/imports/ETF_performance_sources_2026-09-01_run-4.md`; no shared navigation file is in this card's output scope.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## SEIE research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official active equity eligibility, strategy-aligned benchmark, date-separated current fields, one compatible calendar row, calculations and scheduled-local review passed with provisional evidence disclosed.
```
