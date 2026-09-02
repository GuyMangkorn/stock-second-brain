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
