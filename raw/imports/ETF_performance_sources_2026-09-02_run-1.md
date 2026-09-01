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
