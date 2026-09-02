---
type: source-batch
workflow: check-etf-performance
scope: research-queue
updated: 2026-09-02
execution_profile: scheduled-inline
window: available complete calendar years plus current 2026 YTD
return_basis: NAV total return
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
---

# ETF Performance Sources — 2026-09-02 Run 5

This dated batch records the source-backed evidence, calculations and
scheduled-local pre-save review for cards processed sequentially under one
retained `research-queue-manager` project lease. No sub-agent or reviewer was
dispatched by design for this scheduled-inline run.

## TXUE evidence packet

- Input ticker: `TXUE`; canonical identity: `Nasdaq:TXUE`; fund: `Thornburg International Equity ETF`. Thornburg's official product page identifies the exchange as Nasdaq, benchmark as `MSCI EAFE Index`, inception as `2025-01-21`, asset category as International Equity, and total expense ratio as `0.65%`. SEC's 2025-12-30 summary prospectus also identifies ticker `TXUE` and Nasdaq listing.
- Official classification: `active-equity-long-only`, `fundamental-active`. SEC states the fund invests at least 80% in common stocks/depositary receipts of non-U.S. developed-market companies and uses bottom-up fundamental analysis; it may use currency forwards for hedging. No leverage, inverse, option-income, buffer, single-stock, bond, commodity or derivative-defined payoff was identified.
- Management benchmark: `MSCI EAFE Index`, selected before comparing performance at hierarchy step 2 because Thornburg designates it as the fund benchmark. No closer official performance-table comparator was disclosed in the reviewed capture. The S&P 500 remains a separate common USD reference.
- Official fund facts as of `2026-08-28`: net assets `US$557.96M`, NAV `US$36.42`, Nasdaq exchange, annual distribution frequency and `0.65%` total expense ratio. Pricing/trading as of `2026-08-27`: NAV `US$36.25`, market price `US$36.37`, premium `0.31%`, 30-day median bid-ask spread `0.28%`, average volume `34,340`, shares outstanding `15.32M`.
- Official current performance: Thornburg reports NAV TR YTD `16.36%` as of `2026-08-28`. The page's issuer performance table as of `2026-06-30` reports NAV YTD `9.81%`, 1-year `18.42%`, and inception `25.72%`; corresponding MSCI EAFE values are `9.44%`, `20.23%`, and `26.21%`. The issuer states total returns use the daily 4:00pm NAV and assume distributions are reinvested on the pay date at NAV.
- Return-only calculations from the identical 2026-06-30 table: YTD `9.81% - 9.44% = +0.37 pp`; 1-year `18.42% - 20.23% = -1.81 pp`; inception `25.72% - 26.21% = -0.49 pp`. These are not alpha. No Excess CAGR, cumulative relative wealth or hit rate is calculated because the fund has no three-year comparable history and no complete calendar-year return table.
- Distribution evidence: official page lists ex-date `2025-12-19`, payable date `2025-12-31`, total/income distribution `US$0.33847`; no future distribution is inferred.
- SEC calendar-history gap: the summary prospectus says the fund recently commenced operations and did not have a full calendar year as of `2025-12-30`, so no 2025 complete-year row is used. 2025 is inception-year partial and 2026 is ongoing; 10-year CAGR, 2021-2025 CAGR, up/down-year counts, best/worst year and calendar hit rate are not applicable/not disclosed.
- Current S&P reference: S&P DJI's current all-returns table labels `S&P 500 (TR)` and reports YTD `12.34%` as of `2026-09-01`. It is not compared directly with TXUE's `2026-08-28` YTD because the as-of dates differ. The full-calendar S&P cache is not used for a TXUE annual comparison because TXUE has no complete annual row.
- Risk/portfolio evidence: Thornburg reports 48 holdings and active share `80.4%` as of `2026-07-31`; top listed positions as of `2026-08-31` include Thornburg Capital Management Fund LIQUID `5.88%`, TSM `3.46%`, BNP Paribas `3.34%`, Mitsubishi UFJ `3.11%` and ING `2.98%`. Sector weights as of `2026-07-31` include Industrials `22.7%`, Financials `19.9%`, Utilities `9.5%`, Cash & Equivalents `6.4%`; top country weights are France `19.3%`, Japan `14.2%`, Germany `11.9%`, United States `6.8%` and Spain `6.3%`.
- Active evidence: `track_record: insufficient` because elapsed fund history remains below three comparable years. `management_evidence: insufficient` because no complete-year hit rate or three-year/longer comparable Excess CAGR is available. `risk_evidence: not-verified` because compatible daily NAV history for drawdown, recovery and risk-adjusted persistence was not captured. Lei Wang, CFA and Matt Burdett are the named portfolio managers; prior tenure is not substituted for fund track record.
- Source map: official product `https://www.thornburg.com/product/etfs/eie/TXUE/`; SEC summary prospectus `https://www.sec.gov/Archives/edgar/data/2038383/000199937125021310/txue-497k_123025.htm`; current S&P TR table `https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization`; S&P definition `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`.

## Scheduled-local review

- Source integrity review: PASS — ticker/exchange, fund identity, active equity eligibility, official management benchmark, return basis, currency, expenses, distributions, as-of dates and no-complete-year gap reconcile across official Thornburg, SEC and S&P sources.
- Calculation review: PASS — the three return-only differences were recomputed from identical issuer periods; no annual CAGR, best/worst ranking, hit rate or risk metric was inferred from partial history.
- Active-management review: PASS — `fundamental-active` is supported by the SEC strategy disclosure; `track_record: insufficient`, `management_evidence: insufficient` and `risk_evidence: not-verified` follow the deterministic rules; return-only differences are not called alpha.
- Format and graph review: PASS — Thai-first performance page, required active fields/sections, canonical `geography/International` tag, breadcrumb, one primary region, and resolving output/index links are present.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NASDAQ_TXUE Performance.md` and this source batch; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, and append one `log.md` workflow bullet.
- Planned graph/index changes: assign exactly one primary region, `International`, based on underlying developed international equity exposure; add TXUE to the International navigation table; increment the region count `69 → 70`; add the performance-index coverage row and the dated queue-coverage bullet; preserve the breadcrumb `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`.
- Local pre-save verdict: PASS; exact scheduled audit lines are `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design`; no critical, high or blocking finding remains.

## TXUE research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official active international-equity identity, Nasdaq listing, current NAV/YTD, comparable issuer performance fields, calculations and scheduled-local review passed with no-complete-year, insufficient-track-record and daily-NAV risk gaps disclosed.
```

## FYLD evidence packet

- Input ticker: `FYLD`; canonical identity: `Cboe BZX:FYLD`; fund: `Cambria Foreign Shareholder Yield ETF`. Cambria's official product page and fact sheet identify the Cboe BZX listing, inception `2013-12-03`, actively managed ETF status, equity-income objective and expense ratio `0.59%`. The SEC summary prospectus identifies the active foreign-equity mandate and principal risks.
- Official classification: `active-equity-long-only`, `systematic-active`. The SEC states that the fund invests at least 80% of total assets in equity securities of developed countries outside the United States and uses a shareholder-yield/value-oriented process. Cboe describes the quantitative selection of roughly 100 companies using dividend and net buyback ranks with value, quality and low-leverage filters. No bond, commodity, currency, leveraged, inverse, covered-call, defined-outcome or derivative-heavy payoff was identified.
- Management benchmark: `MSCI EAFE Index`, selected before comparing results because the official Cambria fact sheet names it as the strategy comparison for the developed foreign-equity mandate. Annual benchmark rows were not disclosed in the reviewed sources; they remain `not disclosed` rather than being inferred.
- Official 2026-06-30 fact sheet: NAV TR `13.49%` YTD, `29.81%` 1-year, `11.16%` 5-year annualized, `11.35%` 10-year annualized and `7.73%` since inception annualized. Matching MSCI EAFE fields are `9.84%`, `20.80%`, `9.60%`, `10.20%` and `7.44%`, giving return-only differences of `+3.65`, `+9.01`, `+1.56`, `+1.15` and `+0.29` percentage points. These are not alpha.
- Official annual NAV rows from Cambria's historical summary: 2016 `6.53%`, 2017 `28.46%`, 2018 `-13.66%`, 2019 `17.83%`, 2020 `4.35%`, 2021 `17.68%`, 2022 `-5.15%`, 2023 `12.95%`, 2024 `3.22%`. Secondary AAII annual row for 2025 is `34.20%*`; the asterisk marks the non-official provider. S&P 500 TR cache rows for 2016-2025 are `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`.
- Calculations from rounded annual inputs: FYLD 2016-2025 product `2.5371305857`, cumulative `153.7131%`, rounded-input CAGR `9.7575%` → display `153.71%*` / `9.76%*`; FYLD 2021-2025 product `1.7463954884`, cumulative `74.6395%`, rounded-input CAGR `11.7966%` → display `74.64%*` / `11.80%*`. S&P cache 2016-2025 cumulative `298.3291%` / CAGR `14.8218%` → display `298.33%` / `14.82%`; 2021-2025 cumulative `96.1696%` / CAGR `14.4264%` → display `96.17%` / `14.43%`.
- Calendar read-through: blended 2016-2025 window has `8 / 2` up/down years; best `2025 +34.20%*`, least positive `2024 +3.22%`, worst `2018 -13.66%`, least-bad down year `2022 -5.15%`. The 2025 row and blended CAGRs remain marked secondary.
- Strategy/history caveat: the SEC prospectus records a strategy/objective change on `2020-06-01`; before that date FYLD tracked the Cambria Foreign Shareholder Yield Index. The 2016-2019 rows are therefore historical context, not perfectly like-for-like evidence for the current systematic process.
- Official fund/risk facts as of `2026-06-30`: 30-day SEC yield `3.79%`, holdings `101`, quarterly distributions, Energy `25.0%`, Financials `23.2%`, Industrials `13.8%`, Japan `25.0%`, Britain `14.0%`, France `11.1%`, Canada `11.0%`. Compatible official daily NAV history for maximum drawdown, recovery, downside capture, tracking error or risk-adjusted persistence was not verified. Cambria's dynamic product page shows an undated holdings field of `112`, while the dated fact sheet shows `101`; the dated fact sheet is used and the conflict is retained.
- Current-period cross-check: AAII reports NAV total-return YTD `22.30%*` and 2025 `34.20%*` as of `2026-07-31`; these are kept separate from the official `2026-06-30` fields. Current S&P 500 TR is `12.34%` as of `2026-09-01`; no direct same-date comparison is made.
- Source map: official product `https://www.cambriafunds.com/fyld`; official fact sheet `https://www.cambriafunds.com/assets/docs/FYLD-FactSheet.pdf`; SEC summary prospectus `https://www.sec.gov/Archives/edgar/data/1529390/000121390025083085/ea0253992-03_497k.htm`; Cboe listing `https://www.cboe.com/us/equities/listings/listed_products/symbols/FYLD/`; official historical summary `https://cambriafunds.com/assets/docs/Cambria_FYLD_Summary.pdf`; secondary AAII `https://www.aaii.com/etf/ticker/FYLD`; current S&P TR table `https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization`.

## FYLD scheduled-local review

- Source integrity review: PASS — ticker/exchange, fund identity, supported active equity type, inception, strategy, management benchmark, return basis, USD currency, expenses, distribution treatment, official/secondary separation and all as-of dates reconcile across the reviewed sources; the 2020 strategy change and 101-versus-112 holdings conflict are disclosed.
- Calculation review: PASS — annual products, cumulative returns, CAGRs, up/down count, best/worst ranking and rolling return-only differences were recomputed from the stated rounded inputs; S&P rows use the permitted 2016-2025 USD TR cache; no annual MSCI EAFE rows, hit rate, daily drawdown or risk-adjusted metric was inferred.
- Active-management review: PASS — `active-equity-long-only` and `systematic-active` are supported; `track_record: established` follows the 2013 inception; `management_evidence: positive return-only` follows positive 10-year excess with unavailable hit rate; `risk_evidence: not-verified` follows the missing compatible daily NAV series; no return difference is called alpha.
- Format and graph review: PASS — Thai-first performance page, required active fields/sections, canonical `geography/International` tag, breadcrumb, one primary region, resolving page/index links and source-batch linkage are present.
- Complete proposed durable contents: create `wiki/analysis/performance/ETF_CBOE_BZX_FYLD Performance.md` with the frontmatter and sections above; append this FYLD evidence/review/handoff packet; add the exact International row `| FYLD | Cambria Foreign Shareholder Yield ETF | active systematic foreign developed shareholder-yield/value/quality equity | 11.35% | 11.80%* | 22.30%* | [[ETF_CBOE_BZX_FYLD Performance]] |`; change `International` region count `70 → 71`; add the exact FYLD coverage row to `ETF Performance Index`; append the dated queue-coverage bullet; append one `etf-performance` log bullet with the official/secondary as-of split and risk gap.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_CBOE_BZX_FYLD Performance.md`; update this batch, `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, and `log.md`.
- Local pre-save verdict: PASS; exact scheduled audit lines are `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design`; no critical, high or blocking finding remains.

## FYLD research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official active foreign-equity identity, Cboe BZX listing, dated official NAV/benchmark fields, separated secondary current data, calculations and scheduled-local review passed with strategy-break, unavailable-hit-rate and daily-NAV risk gaps disclosed.
```

## SEIS evidence packet

- Input ticker: `SEIS`; canonical identity: `Nasdaq:SEIS`; fund: `SEI Select Small Cap ETF`. SEI's official page and fact sheet identify the Nasdaq listing; SEC states operations began `2024-10-08`, while the Nasdaq listing notice records first listing/trading on `2024-10-10`. The operations date is used for track-record classification and the listing date is kept separately.
- Official classification: `active-equity-long-only`, `other-active`. The SEC states that the fund invests at least 80% in equity securities of small companies in the Russell 2000 market-cap universe and combines SEI's quantitative-based active portfolio with model portfolios from sub-advisers. The official fact sheet identifies allocations to SEI Investments Management Corporation, Easterly Investment Partners and Geneva Capital Management. No bond, commodity, currency, leveraged, inverse, covered-call, defined-outcome or derivative-heavy payoff was identified.
- Management benchmark: `Russell 2000 Index (USD)`, selected from the official SEI fact sheet as the strategy-aligned U.S. small-cap comparator. S&P 500 TR remains a common reference only.
- Official fact sheet fields: the current/YTD block is as of `2026-07-31` and reports NAV TR YTD `15.79%` versus Russell 2000 `18.85%`; the annualized block is as of `2026-06-30` and reports NAV TR 1-year `31.44%` versus `40.78%` and since-inception annualized `18.35%` versus `21.99%`. The official fact sheet also reports net assets `US$575.55M`, holdings `372`, weighted capitalization `US$6,065M`, P/B `2.40`, median forward P/E `14.37`, beta `0.95`, and expense ratio `0.55%`.
- Return-only calculations from identical official periods: YTD `15.79% - 18.85% = -3.06 pp`; 1-year `31.44% - 40.78% = -9.34 pp`; since inception annualized `18.35% - 21.99% = -3.64 pp`. These are not alpha. No Excess CAGR or hit rate is calculated because the fund has less than three years of operating history and annual benchmark rows are not disclosed.
- Calendar evidence: official SEI sources reviewed do not expose a complete calendar-year table. Secondary AAII reports 2025 annual NAV TR `9.80%*` and 2026 YTD `15.8%` as of `2026-07-31`; only the 2025 row is used as a secondary complete-year observation. The 2024 inception-year partial is not annualized or backfilled. S&P cache 2025 TR is `17.88%`.
- Calendar read-through: one available complete-year observation is positive (`2025 +9.80%*`), but a meaningful up/down count, best/worst year and 2021-2025 CAGR are `not applicable`. The 2025 observation remains marked secondary.
- Risk/portfolio evidence: official July factsheet reports beta `0.95`, no 3-year standard deviation and no 3-year tracking error, with 372 holdings. Prospectus risks include equity, small/medium capitalization, momentum, quality, value, low volatility, quantitative investing, market, liquidity, management, new-fund, authorized participant and premium/discount risks. Compatible official daily NAV history for maximum drawdown, recovery, downside capture or risk-adjusted persistence was not verified. The official reliable capture used for the page does not provide a dated NAV/market-price pair.
- Active evidence: `track_record: insufficient` because operations began 2024-10-08 and elapsed history is under three years. `management_evidence: insufficient` because the available one-year/YTD fields are below the minimum track-record threshold and no complete annual benchmark rows or compatible hit rate are available. `risk_evidence: not-verified`; no return difference is called alpha.
- Current S&P reference: S&P DJI's current all-returns table reports S&P 500 TR YTD `12.34%` as of `2026-09-01`; it is not directly compared with SEIS's `2026-07-31` YTD because the as-of dates differ. The permitted cached S&P 2016-2025 rows are retained only for the 2025 common-reference row.
- Source map: official product `https://seietfs.filepoint.live/seis`; official fact sheet `https://seietfs.filepoint.live/assets/pdfs/SEIS_FactSheet.pdf`; SEC summary prospectus `https://www.sec.gov/Archives/edgar/data/1888997/000110465925073552/tm258862d15_497k.htm`; Nasdaq listing `https://nasdaqtrader.com/TraderNews.aspx?id=ETP2024-93`; secondary AAII `https://www.aaii.com/etf/ticker/SEIS`; current S&P TR table `https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization`.

## SEIS scheduled-local review

- Source integrity review: PASS — ticker/exchange, operations-versus-listing dates, fund identity, supported active equity classification, benchmark, return basis, currency, expenses, current/YTD and annualized as-of dates, and official/secondary separation reconcile across SEI, SEC, Nasdaq and AAII sources.
- Calculation review: PASS — the three official return-only differences were recomputed from the stated periods; the 2025 secondary row was not used to manufacture a long-window CAGR; no annual benchmark, hit rate, drawdown, recovery or risk-adjusted metric was inferred.
- Active-management review: PASS — `active-equity-long-only` and `other-active` are supported by the integrated quantitative/fundamental multi-manager strategy; `track_record: insufficient`, `management_evidence: insufficient` and `risk_evidence: not-verified` follow the deterministic rules; return-only differences are not called alpha.
- Format and graph review: PASS — Thai-first performance page, required active fields/sections, canonical `geography/United-States` tag, breadcrumb, one primary region, resolving output/index links and source-batch linkage are present.
- Complete proposed durable contents: create `wiki/analysis/performance/ETF_NASDAQ_SEIS Performance.md` with the frontmatter, official/secondary tables, risk and active-management sections above; append this SEIS evidence/review/handoff packet; add the exact USA row `| SEIS | SEI Select Small Cap ETF | active integrated U.S. small-cap quantitative/fundamental | not applicable (<10y) | not applicable (2024 inception) | 15.79% | [[ETF_NASDAQ_SEIS Performance]] |`; change `USA` region count `67 → 68`; add the exact SEIS coverage row to `ETF Performance Index`; append the dated queue-coverage bullet; append one `etf-performance` log bullet with the official/secondary split and risk gap.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NASDAQ_SEIS Performance.md`; update this batch, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, and `log.md`.
- Local pre-save verdict: PASS; exact scheduled audit lines are `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design`; no critical, high or blocking finding remains.

## SEIS research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official active U.S. small-cap identity, Nasdaq listing, dated official NAV/benchmark fields, separated secondary 2025 row, calculations and scheduled-local review passed with insufficient-track-record and daily-NAV risk gaps disclosed.
```
