---
type: etf-performance-source-batch
workflow: check-etf-performance
batch_date: 2026-08-31
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
pre_save_review: PASS
---

# ETF Performance Sources — 2026-08-31

## ISQWF / IWQU — iShares Edge MSCI World Quality Factor UCITS ETF

- `entity_key`: `LSE:IWQU`; card input `ISQWF` is an OTC alias. The official BlackRock/iShares page and factsheet identify the USD share class as `IWQU` on the London Stock Exchange, ISIN `IE00BP3QZ601`, launched 2014-10-03, Ireland-domiciled and accumulating.
- Official product source: https://www.ishares.com/uk/professionals/en/products/270054/?siteEntryPassthrough=true&switchLocale=y — NAV `USD 90.42` as of 2026-08-24; NAV Total Return YTD `13.26%` as of 2026-08-21; net assets `USD 6,203,035,895` as of 2026-08-24; TER `0.25%`; benchmark `MSCI World Sector Neutral Quality Index (Net)`; physical optimized methodology; 301 holdings and P/E/P/B `27.16x`/`7.07x` as of 2026-08-21; 3-year standard deviation `12.05%` as of 2026-07-31.
- Official factsheet: https://www.blackrock.com/no/intermediaries/literature/fact-sheet/iwqu-ishares-edge-msci-world-quality-factor-ucits-etf-fund-fact-sheet-en-no.pdf — performance/fund facts as of 2026-07-31 and other data as of 2026-08-06; USD share-class NAV TR calendar rows for 2016-2025 are `5.03%, 23.09%, -7.31%, 30.53%, 14.91%, 23.20%, -19.20%, 25.72%, 16.62%, 15.39%`; issuer benchmark rows are `5.05%, 23.21%, -7.20%, 30.65%, 14.98%, 23.42%, -19.16%, 25.83%, 16.81%, 15.49%`.
- Return basis: iShares states performance is shown on an NAV basis with gross income reinvested where applicable; the share class is accumulating and TER is 0.25%. Market price is not mixed with NAV TR.
- Classification: supported `passive-index` equity UCITS ETF; the official factsheet labels it PASSIVE and the product objective is to track a subset of MSCI World stocks with strong and stable earnings. Derivatives are not the defining payoff; any hedged-share-class derivative disclosure does not change the USD accumulating share-class classification.
- Common benchmark: cached `S&P 500 Total Return` convention for complete calendar years 2016-2025, USD, dividends reinvested, as of 2025-12-31. The cached rows are `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`; original references and index definition are retained in the `check-etf-performance` skill.
- Calculations from rounded official annual rows: IWQU product `3.0269471`, cumulative `202.69%`, normalized endpoints `100.00 → 302.69`, rounded-input 10-year calendar CAGR `(3.0269471)^(1/10)-1 = 11.71%†`; 2021-2025 product `1.6840991`, cumulative `68.41%`, CAGR `10.99%`; S&P 500 2021-2025 product `1.9616962`, cumulative `96.17%`, CAGR `14.43%`; relative terminal wealth versus S&P common reference `1.6840991/1.9616962-1 = -14.15%`.
- Calendar ranking: 9 positive and 1 negative complete years; best 2019 `+30.53%`; least positive 2016 `+5.03%`; worst and least-bad down year 2022 `-19.20%`. No partial year is ranked.
- Distribution treatment: `Use of Income: Accumulating`; no cash distribution dates or per-round cash yield are inferred.
- Scheduled-local pre-save checklist: PASS — canonical exchange-qualified identity and OTC alias, passive eligibility, NAV TR definition, accumulating treatment, official complete-year rows, cached benchmark basis/window, as-of dates, calculations, source links, region breadcrumb, and unresolved daily-NAV risk gap reconciled. `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`.
- Evidence gap: official daily NAV TR observations sufficient to calculate maximum drawdown, recovery, downside capture, or compatible risk-adjusted evidence were not verified; no market-price or secondary proxy is substituted.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official IWQU performance evidence passed scheduled-local review and durable outputs were committed.
