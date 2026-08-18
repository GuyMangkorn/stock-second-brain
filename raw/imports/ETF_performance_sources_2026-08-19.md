---
type: etf-performance-source-batch
date: 2026-08-19
workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS
---

# ETF Performance Source Batch — 2026-08-19

ชุดข้อมูลนี้เป็น evidence packet และ source ledger ของ workflow
`check-etf-performance` แบบ `scheduled-inline`. การตรวจ pre-save ทำใน
top-level context เดิมครบทุกข้อ และไม่มีการ dispatch worker, reviewer หรือ
`source_verifier`.

## VWCG — Vanguard FTSE Developed Europe UCITS ETF (EUR) Accumulating / VNGLF alias

### Identity and classification

- `entity_key: Euronext Amsterdam:VWCG`; input ticker `VNGLF`; canonical exchange `Euronext Amsterdam`; fund `Vanguard FTSE Developed Europe UCITS ETF (EUR) Accumulating`; ISIN `IE00BK5BQX27`; share-class inception `2019-07-23`; listing `2019-07-25`.
- `management_mode: passive-index`; tracked index `FTSE Developed Europe Index`; official EUR share class; physical acquisition with sampling where full replication is not practicable.
- `return_basis: NAV total return` with income reinvested, net of expenses, EUR; accumulation share class has no cash distribution schedule.
- Primary region: `Europe`; region page `[[Europe ETF]]` and canonical geography tag `geography/Europe`.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Vanguard product page | https://www.vanguard.co.uk/professional/product/etf/equity/9681/vanguard-ftse-developed-europe-ucits-etf-eur-accumulating | official identity, canonical exchange/ticker mapping, inception, benchmark, current NAV, assets, holdings and exposures |
| Vanguard factsheet | https://fund-docs.vanguard.com/FTSE_Developed_Europe_UCITS_ETF_EUR_Accumulating_9681_EU_INT_UK_EN.pdf | official fee, performance summary, current YTD, rolling returns, tracking error and dated fund facts as of 2026-07-31 |
| Vanguard KID | https://fund-docs.vanguard.com/ie00bk5bqx27-en.pdf | official EUR calendar rows 2020-2025, index rows and accumulation disclosure; accurate 2026-02-17 |
| Cached S&P 500 Total Return convention | workflow cache and original URLs in `check-etf-performance/SKILL.md` | USD calendar rows 2020-2025, dividends reinvested, as of 2025-12-31; no new search because the window is within cached 2016-2025 |

### Raw observations

- Vanguard identifies the EUR accumulating share class as `VWCG` on NYSE Euronext - Amsterdam, with the same ISIN across listed currencies/exchanges; the input OTC label `VNGLF` is retained as an alias and not used as the displayed entity key.
- Official KID calendar NAV/index rows in EUR: 2020 `-2.6% / -2.7%`, 2021 `25.2% / 24.9%`, 2022 `-10.0% / -10.2%`, 2023 `16.5% / 16.2%`, 2024 `9.4% / 9.1%`, 2025 `19.9% / 19.5%`. The 2019 launch-year partial is not used because no verified partial return was retained.
- Official factsheet as of 2026-07-31: fund NAV TR YTD `12.06%`, 1Y `22.47%`, 3Y `14.60%`, 5Y `10.39%`, since inception `10.44%`; benchmark YTD `11.78%`, 1Y `22.12%`, 3Y `14.28%`, 5Y `10.05%`, since inception `10.14%`. The factsheet states NAV-to-NAV, gross income invested and net of fund expenses for the fund.
- Official product-page NAV snapshot: `€60.9809` at closure on 2026-08-17. Fund total assets are `€7.678B` and share-class assets `€2.902B` as of 2026-07-31; 513 stocks and country weights include UK `23.21%`, France `14.67%`, Switzerland `14.44%`, Germany `13.33%`, and Netherlands `8.14%`.
- Official OCF is `0.10%`; accumulation shares reinvest income and show no cash distribution frequency. Official annualized tracking error is `0.14%` for 1, 3 and 5 years as of 2026-07-31. Official daily NAV maximum drawdown and recovery date were not disclosed in the reviewed sources.
- Cached S&P 500 TR rows used for the common reference are USD: 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; the EUR/USD basis mismatch is explicitly preserved.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`: VWCG 2020-2025 `67.71%`, rounded-input CAGR `9.00%`, population annual-return standard deviation `12.45%`, up/down `5/1`, best `2021 +25.20%`, least positive `2024 +9.40%`, worst/least-bad down year `2020 -2.60%`.
- VWCG 2021-2025 compounds to `72.19%` / rounded-input CAGR `11.48%`; the FTSE index compounds to `69.92%` / `11.19%`. Approximate fund-minus-index differences are `+0.30 pp` over 2021-2025 and `+0.26 pp` over 2020-2025; these are passive tracking observations, not alpha.
- Cached S&P 500 TR compounds to `132.26%` / `15.08%` over 2020-2025 and `96.17%` / `14.43%` over 2021-2025. No direct excess return is calculated because the ETF return is EUR and the common reference is USD.
- 10-year NAV TR CAGR is not applicable: the share class inception is 2019-07-23 and the official history is shorter than 10 years.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_EURONEXT_AMSTERDAM_VWCG Performance.md` with the canonical `Euronext Amsterdam:VWCG` identity, `input_ticker: VNGLF`, EUR NAV/index/S&P annual table, under-10-year rule, current YTD/NAV dates, tracking-risk evidence, source links, `geography/Europe` tag and breadcrumb.
- Update `wiki/analysis/comparisons/Europe ETF.md` with the VWCG row and current-date/under-10-year note.
- Update `wiki/analysis/comparisons/ETF Region Index.md` Europe count from `17` to `18` and preserve the existing navigation graph.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the VWCG coverage row, 2021-2025 Common Window row and 2026-08-19 coverage bullet.
- Append one `log.md` workflow bullet; no entity hub or `raw/funds/` file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical ticker/exchange mapping, fund name, ISIN, inception/listing dates, passive eligibility, FTSE benchmark, OCF, accumulation/distribution treatment, NAV TR definition, EUR currency, annual rows, current YTD/NAV and all as-of dates are source-backed.
- PASS: official calendar rows are separated from rolling/current fields and from the cached S&P USD reference; no cross-currency excess return is claimed; passive tracking differences are not called alpha.
- PASS: the 2019 partial and daily NAV drawdown/recovery remain explicitly disclosed as gaps; best/worst and up/down counts use only the six complete official years.
- PASS: complete proposed performance page, source batch section, Europe row/count, performance-index row/Common Window/bullet and log bullet are specified; canonical breadcrumb, `geography/Europe` tag and planned wikilinks resolve.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains. Required scheduled audit lines are present: `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design`.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Vanguard identity, passive classification, EUR annual NAV/index rows, current YTD evidence and the scheduled-local pre-save checklist passed; VWCG artifacts were written with the VNGLF alias and currency separation disclosed.
