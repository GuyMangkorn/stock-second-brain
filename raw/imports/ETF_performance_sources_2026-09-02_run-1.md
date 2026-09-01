---
type: source-batch
topic: ETF performance
accessed: 2026-09-02
workflow: check-etf-performance
execution_profile: scheduled-inline
caller: research-queue-manager
handoff: research_handoff
---

# ETF Performance Sources — 2026-09-02 Run 1

This is the card-scoped evidence packet for the `IMWSF` research card. The
input is an OTC alias; the durable page remains the existing canonical USD
London Stock Exchange page for `LSE:WSML`. Shared navigation files were dirty
before this claim and are deliberately excluded from the scoped write.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## IMWSF / WSML evidence packet

- Identity and exchange: iShares identifies the USD accumulating share class as
  `iShares MSCI World Small Cap UCITS ETF`, ISIN `IE00BF4RFH31`, listed on the
  London Stock Exchange as `WSML` in USD. `IMWSF` is retained as the input OTC
  alias and is not used as the displayed exchange key. Official source:
  https://www.ishares.com/uk/professionals/en/products/296576/ — reviewed for
  identity, listing, benchmark, and current fields through 2026-08-28.
- Eligibility: official iShares classifies the fund as `Equity`, `PASSIVE`, and
  physical/optimised; its objective is to track small-capitalisation companies
  across developed markets globally. Currency-hedged share classes use
  derivatives, but the selected USD accumulating class is not defined by
  leverage, inverse exposure, options, fixed income, commodities, or
  multi-asset exposure.
- Fund facts: share-class launch `2018-03-27`; Total Expense Ratio `0.35%`;
  income treatment `Accumulating`; current NAV `USD 10.62` and NAV Total Return
  YTD `17.53%` as of 2026-08-28; holdings `3,548` as of 2026-08-28; 3-year
  standard deviation `16.17%` and beta `1.000` as of 2026-07-31. These are
  separate as-of dates and are not treated as one synchronized snapshot.
- Return definition: official iShares performance is on a NAV basis with gross
  income reinvested where applicable. Annual rows are the share-class NAV total
  return in USD; market-price return is not mixed into the ranking.
- Annual official NAV TR rows for complete calendar years 2019-2025 are
  `25.73%, 15.83%, 15.81%, -18.64%, 16.02%, 7.93%, 19.84%`. The official issuer
  index rows are `26.19%, 15.96%, 15.75%, -18.75%, 15.76%, 8.15%, 19.88%`.
  Source: iShares factsheet
  https://www.ishares.com/gls-download/literature/fact-sheet/wsml-ishares-msci-world-small-cap-ucits-etf-fund-fact-sheet-en-gb.pdf
  with performance as of 2026-03-31 in the retrieved factsheet; the current
  product page is used for the newer current fields.
- Cached common benchmark: `S&P 500 Total Return`, USD, dividends reinvested,
  complete calendar years 2016-2025, as of 2025-12-31. The cached rows for
  2019-2025 are `31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`.
  Original references are the S&P DJI historical research PDF,
  https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true,
  the 2023 market-attributes PDF,
  https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf,
  the 2021 market-attributes page,
  https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/,
  and the 2025 market-attributes page,
  https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/.
- Calculations from the stated annual rows: WSML 2019-2025 product `2.0592`,
  cumulative `105.92%`, rounded-input CAGR `10.87%`; WSML 2021-2025 product
  `1.4139`, cumulative `41.39%`, rounded-input CAGR `7.17%`; S&P 500 2019-2025
  cumulative `205.41%`, CAGR `17.29%`; S&P 500 2021-2025 cumulative `96.17%`,
  CAGR `14.43%`. Complete-year count is `6` up / `1` down; best `2019
  +25.73%`, least positive `2024 +7.93%`, worst and least bad down year `2022
  -18.64%`.
- Ten-year treatment: not applicable because the official share-class launch is
  2018-03-27 and the verified annual history begins in 2019. No shorter period
  is relabelled as a 10-year NAV TR CAGR.
- Risk gap: the reviewed official capture does not provide a daily NAV series
  sufficient to verify maximum drawdown or recovery duration. The performance
  page records `ไม่พบข้อมูลที่ยืนยันได้` rather than substituting a market-price
  proxy.
- Primary region: `International`, because the underlying exposure is global
  developed-market small-cap equities. The existing breadcrumb
  `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]` and
  canonical `geography/International` tag are preserved. No shared region or
  index file is included because those paths were already dirty before claim.

## Planned durable paths/change map

- Update `wiki/analysis/performance/ETF_LSE_WSML Performance.md` for the
  `IMWSF / WSML` input mapping, current run date, and this source-batch link.
- Create this source batch.
- Do not update `International ETF.md`, `ETF Region Index.md`,
  `ETF Performance Index.md`, or `log.md` in this scoped card because they were
  pre-existing dirty paths at claim time; their navigation already resolves to
  the existing WSML page.

## Local pre-save review

- Source and data integrity: `PASS` — canonical exchange-qualified identity,
  alias separation, passive equity eligibility, NAV TR basis, annual rows,
  current YTD, fund facts, and separate as-of dates reconcile.
- Calculation and ranking review: `PASS` — annual compounding, CAGRs, year
  counts, best/worst selection, and the under-10-year treatment recompute from
  the stated inputs; no market-price return is mixed into the ranking.
- Format and graph review: `PASS` — Thai-first narrative, required sections,
  one annual table, source links, existing breadcrumb, and canonical geography
  tags resolve; the performance page remains the numeric source of truth.
- No critical or high finding remains. The daily-NAV drawdown/recovery gap and
  deferred shared-navigation updates remain explicit.

## research_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official WSML evidence passed the scheduled-local checklist and the canonical performance page plus source batch were updated.

## FNDC evidence packet

- Identity and eligibility: Schwab identifies `FNDC` as the `Schwab Fundamental
  International Small Equity ETF`, listed on NYSE Arca, with inception
  `2013-08-15`, management style `Passive`, and objective to track small
  non-U.S. developed-market companies weighted by fundamental size and weight.
  Official source: https://www.schwabassetmanagement.com/products/fndc —
  reviewed through 2026-08-28.
- Fund facts: Total Expense Ratio `0.390%`; NAV `$51.52`, market price
  `$51.34`, premium/discount `-0.35%`, net assets `$3,189,048,898.14`, and
  holdings `1,588` as of 2026-08-28; portfolio turnover `25.61%` as of
  2026-07-31. The current issuer YTD NAV field is `10.96%` as of 2026-07-31.
  These are separate as-of dates.
- Tracked index: current `RAFI Fundamental High Liquidity Developed ex US Small
  Index (Net)`; the issuer discloses that the prior `Russell RAFI Developed ex
  US Small Company Index (Net)` changed effective 2024-06-21. The benchmark
  change is disclosed rather than backfilled as one unchanged series.
- Return definition and annual rows: official SEC/Schwab material defines the
  annual figures as NAV total return with distributions reinvested, net of
  expenses, in USD. Complete 2016-2025 annual NAV TR rows are `8.87%, 29.04%,
  -18.77%, 20.02%, 7.11%, 9.83%, -14.82%, 15.21%, 1.57%, 35.79%`.
  Official sources: https://www.sec.gov/Archives/edgar/data/1454889/000088454626000301/c497k.htm
  and https://www.schwabassetmanagement.com/resource/etf-investment-performance-summary.
- Cached common benchmark: `S&P 500 Total Return`, USD, dividends reinvested,
  complete 2016-2025 calendar years, as of 2025-12-31. The rows are the static
  skill convention: `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%,
  26.29%, 25.02%, 17.88%`; original URLs are retained in the WSML section
  above and in the performance page.
- Calculations: FNDC annual product `2.1808`, cumulative `118.08%`, normalized
  endpoints `100.00 → 218.08`, and rounded-input calendar CAGR `8.11%` over
  `10.00` years; 2021-2025 product `1.4865`, cumulative `48.65%`, CAGR `8.25%`.
  S&P 500 2016-2025 cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative
  `96.17%`, CAGR `14.43%`. The FNDC complete-year count is `8 / 2` up/down;
  best `2025 +35.79%`, least positive `2024 +1.57%`, worst `2018 -18.77%`,
  least bad down year `2022 -14.82%`.
- Risk evidence: issuer 3-year standard deviation `15.14%` as of 2026-07-31;
  annual-row sample standard deviation `17.24%` is kept separate. The annual
  path shows a year-end drawdown approximation of `-18.77%` in 2018 and recovery
  above the prior year-end high by 2020; daily maximum drawdown and recovery
  duration are not verified.
- Primary region: `International` because the fund owns developed ex-U.S.
  small-cap equities. The existing breadcrumb and `geography/International`
  tag are preserved. Shared navigation and log paths were dirty before claim
  and are not in this card’s output scope.

## FNDC planned paths and local review

- Update `wiki/analysis/performance/ETF_NYSE_ARCA_FNDC Performance.md` with the
  current issuer snapshot, separated as-of dates, and this source-batch link.
- Update this source batch with the complete FNDC evidence and audit record.
- Do not update `International ETF.md`, `ETF Region Index.md`,
  `ETF Performance Index.md`, or `log.md` in this scoped card because they were
  pre-existing dirty paths; current navigation targets already resolve.
- Source/data integrity: `PASS` — identity, passive equity classification, NAV
  TR basis, benchmark change, annual rows, current YTD and separate fund-fact
  dates reconcile.
- Calculation/ranking review: `PASS` — compounding, CAGRs, year counts,
  rankings, and risk distinction recompute from stated inputs; no price return
  is mixed with NAV TR.
- Format/graph review: `PASS` — Thai-first required sections, one annual table,
  source links, breadcrumb, and canonical region tag resolve.

## FNDC research_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official FNDC evidence passed the scheduled-local checklist and the canonical performance page plus source batch were updated.

## IVGAF / DFND evidence packet

- Identity resolution: the input `IVGAF` is a secondary OTC alias for the
  iShares Global Aerospace & Defence UCITS ETF U.S. Dollar (Accumulating),
  ISIN `IE000U9ODG19`. Official iShares listings show the USD line as `DFND` on
  SIX Swiss Exchange, listed 2024-04-30; London Stock Exchange `DFND` is a GBP
  line and is not used as the USD canonical key. Official source:
  https://www.ishares.com/uk/individual/en/products/334464/ishares-global-aerospace-defence-ucits-etf?siteEntryPassthrough=true&switchLocale=y.
- Eligibility: iShares classifies the fund as `Equity` and `PASSIVE`, with
  physical replicated exposure to developed-market aerospace and defence
  equities. The selected USD accumulating class is not leverage, inverse,
  option-income, fixed income, commodity, or multi-asset; incidental cash/
  derivatives are not the return-defining structure.
- Fund facts: share-class/fund launch `2024-02-01`; TER `0.35%`; accumulating;
  current NAV `$9.73`, NAV TR YTD `7.13%`, net assets `$1,878,123,633` as of
  2026-08-31; holdings `77` as of 2026-08-28; industrials `99.83%` and
  cash/derivatives `0.19%` as of 2026-08-31.
- Return definition and annual observation: the official July 2026 factsheet
  states performance is on NAV basis with gross income reinvested where
  applicable. Complete calendar performance reports 2025 share-class NAV TR
  `54.55%` and benchmark `54.93%`; the 2024 cell is blank. No partial 2024
  return is inferred.
- Cached common benchmark: `S&P 500 Total Return`, USD, dividends reinvested,
  as of 2025-12-31; 2025 row `17.88%`. It is a common reference, not DFND’s
  issuer benchmark.
- Calculations: only one complete annual observation is verified, so cumulative
  and CAGR are both `54.55%` for 2025 and the up/down count is `1 / 0`. The
  common-reference comparison is `54.55% - 17.88% = 36.67 pp`; it is a single-
  year return difference and not alpha. Ten-year CAGR, volatility, maximum
  drawdown, and recovery are not calculated because the history is insufficient.
- Primary region: `International`, because the underlying exposure is global
  developed-market aerospace and defence equities. The performance page uses
  the existing breadcrumb and canonical tags `geography/International` and
  `geography/global-developed`. Shared navigation and log files were dirty
  before claim and are not in this card’s output scope.

## IVGAF / DFND planned paths and local review

- Create `wiki/analysis/performance/ETF_SIX_DFND Performance.md` with the
  canonical USD listing, input-alias note, one complete annual row, current
  fields, and explicit history/risk gaps.
- Update this source batch with the evidence and audit record.
- Do not update `International ETF.md`, `ETF Region Index.md`,
  `ETF Performance Index.md`, or `log.md` because they were dirty before this
  claim; navigation reconciliation is deferred.
- Source/data integrity: `PASS` — alias/listing/currency, passive equity
  eligibility, benchmark, NAV TR basis, annual row, current YTD and separate
  as-of dates reconcile.
- Calculation/ranking review: `PASS` — one-year return, reference comparison,
  and inapplicable multi-year metrics follow the available history; no partial
  2024 return is ranked.
- Format/graph review: `PASS` — Thai-first required sections, one annual table,
  visible as-of dates, source links, breadcrumb, and canonical region tags
  resolve.

## IVGAF / DFND research_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official DFND evidence passed the scheduled-local checklist and the canonical performance page plus source batch were written.

## LVHI evidence packet

- Identity and eligibility: Franklin identifies `LVHI` as the `Franklin
  International Low Volatility High Dividend Index ETF`, listed on `Cboe BZX`,
  with inception `2016-07-27`. The official factsheet classifies it as
  `Indexed` and `Equity`, tracking the `Franklin International Low Volatility
  High Dividend Hedged Index-NR`.
  Sources: https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/91481/SINGLCLASS/franklin-international-low-volatility-high-dividend-index-etf/LVHI
  and https://www.franklintempleton.com/forms-literature/download/91481-FF.
- Strategy classification: `passive-index`; the fund selects developed-market
  ex-U.S. equities with relatively high yield and low price/earnings volatility.
  Currency-related derivatives hedge currency exposure but do not define a
  leveraged, inverse, option-income, bond, commodity, or multi-asset payoff.
- Fund facts: expense ratio `0.40%`; NAV `$42.72`, NAV TR YTD `18.27%`, net
  assets `$5.57B`, and distribution rate at NAV `5.86%` as of 2026-08-06;
  holdings `194`, 30-day SEC yield `2.85%`, and net assets `$5.00B` in the
  June 30, 2026 factsheet snapshot. The latter is an older fund-facts field and
  is not mixed with the August snapshot.
- Return definition: Franklin states that NAV returns assume reinvestment of all
  distributions and deduction of fund expenses. Official complete annual NAV
  rows are 2017 `11.66%`, 2018 `-5.44%`, 2019 `18.81%`, 2020 `-8.79%`, 2021
  `18.42%`, 2022 `3.80%`, 2023 `17.22%`, 2024 `15.55%`, and 2025 `27.77%`.
  The 2016 inception-year cell is blank and is excluded from annual ranking.
- Cached common benchmark: `S&P 500 Total Return`, USD, dividends reinvested,
  complete calendar years 2016-2025, as of 2025-12-31. The 2017-2025 subset is
  `21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`.
- Calculations: LVHI 2017-2025 product `2.4340164586`, cumulative `143.40%`,
  rounded-input CAGR `10.39%`; S&P product `3.5577805598`, cumulative `255.78%`,
  CAGR `15.14%`; LVHI 2021-2025 product `2.1272717460`, cumulative `112.73%`,
  CAGR `16.30%`; S&P 2021-2025 cumulative `96.17%`, CAGR `14.43%`. Population
  standard deviation of the nine LVHI annual rows is `11.41%`. Complete-year
  ranking is `7 / 2` up/down; best `2025 +27.77%`, least positive `2022 +3.80%`,
  worst `2020 -8.79%`, least bad down year `2018 -5.44%`.
- Risk limitation: annual-path maximum drawdown approximation is `-8.79%` in
  2020, with year-end recovery by 2021. Daily NAV drawdown/recovery and
  compatible risk-adjusted evidence are not verified.
- Primary region: `International`, because the underlying exposure is developed
  markets outside the United States. The performance page uses the existing
  breadcrumb and canonical `geography/International` tag. Shared navigation
  and `log.md` were dirty before claim and are not in this card’s output scope.

## LVHI planned paths and local review

- Create `wiki/analysis/performance/ETF_CBOE_BZX_LVHI Performance.md` with the
  complete performance page, one annual table, current fields, and source links.
- Update this source batch with the LVHI evidence and local review.
- Do not update `International ETF.md`, `ETF Region Index.md`,
  `ETF Performance Index.md`, or `log.md` because those paths were dirty before
  this queue claim; navigation reconciliation is deferred.
- Source/data integrity: `PASS` — exchange/ticker, passive equity eligibility,
  hedge role, NAV TR definition, annual rows, current YTD, and separated as-of
  dates reconcile.
- Calculation/ranking review: `PASS` — annual compounding, CAGRs, volatility,
  year counts, best/worst rows, and annual-path drawdown recompute from the
  factsheet rows; 2016 blank inception year is not ranked.
- Format/graph review: `PASS` — Thai-first required sections, one annual table,
  visible as-of dates, source links, existing breadcrumb, and canonical region
  tag resolve.

## LVHI research_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official LVHI evidence passed the scheduled-local checklist and the performance page plus source batch were written.
