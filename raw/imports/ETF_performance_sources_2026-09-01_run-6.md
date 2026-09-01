---
type: etf-performance-source-batch
workflow: check-etf-performance
run_date: 2026-09-01
run_label: run-6
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
---

# ETF Performance Sources — 2026-09-01 — run-6

## WSML — iShares MSCI World Small Cap UCITS ETF

- `entity_key`: `LSE:WSML`; input ticker `WSML`; legacy OTC alias `IMWSF`; official USD listing is London Stock Exchange `WSML` for ISIN `IE00BF4RFH31`. The underlying exposure is global developed-market small-cap equity, so primary region is `International` and canonical tag is `geography/global-developed`.
- Management mode: `passive-index`; the fund seeks to track the `MSCI World Small Cap Index (Net)`, uses a physical/optimised structure, has share-class launch `2018-03-27`, `0.35%` Total Expense Ratio, and accumulating income treatment.
- Official product source: https://www.ishares.com/uk/professionals/en/products/296576/ishares-msci-world-small-cap-ucits-etf-usd-%28acc%29-fund — product page reviewed for current observations through `2026-08-28`; NAV `USD 10.62`, NAV Total Return YTD `17.53%`, holdings `3,548`, P/B `2.11`, P/E `19.19`, and benchmark level `USD 996.55` as of `2026-08-28`; 3-year standard deviation `16.17%` and beta `1.000` as of `2026-07-31`.
- Official historical source: https://www.ishares.com/gls-download/literature/fact-sheet/wsml-ishares-msci-world-small-cap-ucits-etf-fund-fact-sheet-en-gb.pdf — official factsheet with complete annual NAV/index rows for `2019-2025`, July 2026 YTD `13.88%` as of `2026-07-31`, and the USD accumulating share-class identity. Annual rows are retained from the verified factsheet capture: fund `25.73%, 15.83%, 15.81%, -18.64%, 16.02%, 7.93%, 19.84%`; issuer index `26.19%, 15.96%, 15.75%, -18.75%, 15.76%, 8.15%, 19.88%`.
- Return basis: USD `NAV Total Return` with gross income reinvested where applicable; accumulating income remains in NAV. Market-price return is not mixed. Complete 2018 inception-year annual data was not disclosed, so the 2019-2025 window is used for annual ranking and no 10-year NAV TR CAGR is claimed because the share class has less than ten elapsed years as of the run date.
- Performance calculations from official annual rows: 2019-2025 product compound `105.92%` and rounded-input CAGR `10.87%`; 2021-2025 compound `41.39%` and CAGR `7.17%`; issuer-index 2019-2025 CAGR `10.92%`; issuer-index 2021-2025 CAGR `7.14%`. Complete-year count is `6 / 1` up/down; best `2019 +25.73%`; least positive `2024 +7.93%`; worst and least-bad down year `2022 -18.64%`.
- Cached common benchmark: `S&P 500 Total Return` in USD with dividends reinvested, complete calendar years `2016-2025`, reference as of `2025-12-31`; annual rows `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`; 2019-2025 cumulative `205.41%` / CAGR `17.29%`; 2021-2025 cumulative `96.17%` / CAGR `14.43%`. The cached benchmark is not used as a synchronized 2026 YTD comparison.
- Risk limitation: official daily NAV observations sufficient to calculate maximum drawdown and recovery were not verified in this lean refresh; no numeric drawdown proxy is saved. The latest NAV and YTD are separate as-of fields and are not combined with the older July factsheet field as if they were contemporaneous.
- Planned durable paths: update `wiki/analysis/performance/ETF_LSE_WSML Performance.md`; create this source batch. Existing `International ETF.md`, `ETF Region Index.md`, `ETF Performance Index.md`, and `log.md` were already dirty before the claim and are intentionally outside this scoped commit; the existing navigation links resolve, and the performance page retains the breadcrumb plus adds the canonical `geography/global-developed` tag.

## Scheduled-inline local review

- Review packet checked canonical exchange/ticker, legacy alias handling, passive equity eligibility, fund identity, inception, benchmark, TER, accumulating NAV TR basis, current and historical as-of dates, official source links, complete-year markers, 10-year eligibility, cached S&P 500 convention, calculations, not-disclosed handling, one annual table, breadcrumb, and canonical tag.
- Pre-save verdict: `PASS`. No market-price return, unsupported annual proxy, or shorter-period 10-year claim is used. Daily-NAV max-drawdown/recovery remains explicitly unresolved, and the current 2026 YTD is not presented as a same-date benchmark comparison.

### research_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official WSML performance evidence passed scheduled-local review and the scoped performance page and source batch were written.
