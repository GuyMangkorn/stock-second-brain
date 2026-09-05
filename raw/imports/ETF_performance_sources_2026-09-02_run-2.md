---
type: source-batch
topic: ETF performance
accessed: 2026-09-02
workflow: check-etf-performance
execution_profile: scheduled-inline
caller: research-queue-manager
handoff: research_handoff
---

# ETF Performance Sources — 2026-09-02 Run 2

This card-scoped evidence packet covers `NUDM` only. Durable output scope:
`wiki/analysis/performance/ETF_CBOE_BZX_NUDM Performance.md` and this source
batch. Existing shared navigation and index pages are unchanged because the
common window, coverage, classification, and primary region did not change.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## NUDM evidence packet

- Identity and exchange: the official SEC summary prospectus identifies
  `Nuveen ESG International Developed Markets Equity ETF`, ticker `NUDM`, and
  listing exchange `Cboe BZX Exchange, Inc.`; inception is `2017-06-06`.
  Source: https://www.sec.gov/Archives/edgar/data/1635073/000119312526080207/d40382d497k.htm
- Eligibility and strategy: the SEC prospectus describes a fund seeking to
  track the Nuveen ESG International Developed Markets Equity Index, comprised
  solely of listed equity securities and depositary receipts from developed
  markets excluding the U.S. and Canada. The official Nuveen factsheet states
  that the fund uses a passive management/indexing approach and the index is
  rebalanced quarterly. Sources:
  https://www.nuveen.com/en-us/exchange-traded-funds/nudm-nuveen-esg-international-developed-markets-equity-etf
  and https://documents.nuveen.com/Documents/Nuveen/Viewer.aspx?download=1&uniqueId=02852fbf-974a-433c-9b45-56a6a1289a83
- Return basis and annual rows: the Nuveen factsheet is as of `2026-06-30`
  and defines NAV total returns as assuming reinvestment of distributions. The
  complete calendar-year NAV TR rows are `2018 -14.63%`, `2019 24.28%`,
  `2020 10.74%`, `2021 10.21%`, `2022 -15.08%`, `2023 17.89%`, `2024 5.55%`,
  and `2025 29.35%`. The index rows are `-14.47%`, `24.66%`, `11.14%`,
  `10.52%`, `-14.94%`, `18.19%`, `5.80%`, and `29.87%` respectively.
  Source: official Nuveen factsheet above.
- Current official fields: the same factsheet reports 2026 YTD NAV TR of
  `10.10%` as of `2026-06-30`, expense ratio `0.27%`, SEC 30-day yield
  `2.33%`, annual distribution frequency, total net assets `US$698.26M`,
  `76` positions, weighted average market cap `US$126.09B`, and forward P/E
  `17.39x`. Price/NAV was not disclosed in the reviewed official sources.
- Adviser continuity: the factsheet states that Teachers Advisors, LLC
  merged into Nuveen Asset Management, LLC effective `2026-08-01`, with no
  investment-strategy or portfolio-management change; Nuveen Asset Management
  became the fund's sub-adviser. The dated factsheet wording is preferred over
  older product-page wording when the roles differ.
- Common benchmark: cached `S&P 500 Total Return` in USD with dividends
  reinvested, as of `2025-12-31`, is used for the overlapping 2018-2025 rows.
  The cached rows are `2018 -4.38%`, `2019 31.49%`, `2020 18.40%`, `2021
  28.71%`, `2022 -18.11%`, `2023 26.29%`, `2024 25.02%`, and `2025 17.88%`.
  This is a common reference, not NUDM's issuer benchmark. The cached source
  references are retained in the performance page and the skill convention.
- Calculations from the official rounded annual rows: NUDM product
  `1.7698793878`, cumulative `76.99%`, normalized endpoints `100.00` at
  `2017-12-31` to `176.99` at `2025-12-31`, and rounded-input CAGR `7.40%`
  over eight complete years. For 2021-2025, product `1.5063734`, cumulative
  `50.64%`, CAGR `8.54%`. S&P 500 2018-2025 cumulative/CAGR are `192.03%`/
  `14.33%`; 2021-2025 are `96.17%`/`14.43%`. NUDM has `6` up years and `2`
  down years; best `2025 +29.35%`, least positive `2024 +5.55%`, worst `2022
  -15.08%`, and least bad down year `2018 -14.63%`. Annual-row population
  standard deviation is `15.33%` for 2018-2025 and `14.73%` for 2021-2025.
- Risk gap: compatible daily NAV history sufficient to verify maximum
  drawdown, recovery duration, downside capture, and risk-adjusted evidence
  was not found in the reviewed official materials. The performance page uses
  `ไม่พบข้อมูลที่ยืนยันได้` rather than a market-price proxy.
- Primary region: `International`, based on underlying developed-market
  ex-U.S./Canada equity exposure. The existing breadcrumb and canonical
  `geography/International` tag are preserved; no region/index change is
  required for this refresh.

## Planned durable paths and local pre-save review

- Update `wiki/analysis/performance/ETF_CBOE_BZX_NUDM Performance.md` only to
  point to this fresh source batch; its existing narrative, table, calculations,
  breadcrumb, and tags were rechecked against the evidence above.
- Create this source batch with the evidence, as-of dates, gaps, planned-path
  map, and the handoff below.
- Source/data integrity: `PASS` — canonical exchange, fund identity, passive
  equity eligibility, NAV TR basis, annual rows, current YTD, benchmark basis,
  and separate as-of dates reconcile.
- Calculation/ranking review: `PASS` — compounding, CAGRs, standard deviation,
  up/down counts, best/worst selection, and partial-year treatment recompute
  from the stated inputs; no market-price return is mixed into the ranking.
- Format/graph review: `PASS` — Thai-first narrative, required sections, one
  annual table, source links, existing breadcrumb, and canonical region tag
  resolve. No critical or high finding remains.

## Planned durable paths/change map

- Updated: `wiki/analysis/performance/ETF_CBOE_BZX_NUDM Performance.md`.
- Created: `raw/imports/ETF_performance_sources_2026-09-02_run-2.md`.
- No changes: `wiki/analysis/comparisons/International ETF.md`,
  `wiki/analysis/comparisons/ETF Region Index.md`,
  `wiki/analysis/performance/ETF Performance Index.md`, or `log.md`.

## research_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official NUDM evidence passed the scheduled-local checklist and the canonical performance page plus source batch were updated.
