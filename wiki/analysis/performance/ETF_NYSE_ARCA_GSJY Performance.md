---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:GSJY
ticker: GSJY
exchange: NYSE Arca
fund: Goldman Sachs ActiveBeta Japan Equity ETF
tracked_index: Goldman Sachs ActiveBeta Japan Equity Index
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/GSJY
  - geography/Japan
---

# GSJY Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

GSJY เป็น rules-based smart-beta, passive/index-tracking Japan equity ETF ที่ติดตาม
Goldman Sachs ActiveBeta Japan Equity Index. แม้ชื่อมีคำว่า ActiveBeta แต่ official
prospectus ระบุว่า fund `is not actively managed`; จึงผ่าน passive equity gate. Official
Goldman Sachs factsheet ณ 2026-07-31 รายงาน rolling 10-year NAV Total Return CAGR
`9.01%` และ NAV TR YTD `15.60%`. Raw NAV TR endpoints ไม่ได้เปิดเผย; normalized end
`236.95` จาก start `100.00` เป็นเพียงค่าคำนวณจาก CAGR ที่ issuer ปัดเศษ. Calendar-year
NAV rows ที่ยืนยันได้เริ่ม 2017 เพราะ inception คือ 2016-03-02; 2016 จึงไม่ถูกเรียกว่า
complete calendar year. ช่วง 2017-2025 เป็นบวก `6 จาก 9` ปี โดย 2025 ดีที่สุดและ 2022
แย่ที่สุด.

## Performance check

- `entity_key`: `NYSE Arca:GSJY`
- Inception: `2016-03-02`; CUSIP `381430404`
- Metric: official `NAV Total Return`, รวมการ reinvest distributions และหัก fund expenses
- Tracked index (issuer benchmark): `Goldman Sachs ActiveBeta Japan Equity Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference only)
- Official 10-year NAV TR window: 2016-07-31 to 2026-07-31; actual years `10.00`
- Official rolling NAV TR as of `2026-07-31`: 1-month `2.42%`, YTD `15.60%`, 1-year `31.15%`, 3-year `17.33%`, 5-year `9.83%`, 10-year `9.01%`, since inception `9.50%`
- The ActiveBeta Japan Index fields for the same window are 1-month `2.46%`, YTD `15.65%`, 1-year `31.23%`, 3-year `17.37%`, 5-year `9.81%`, 10-year `8.90%`, and since inception `9.38%`. MSCI Japan - USD (Net) is a separate reference-universe series, not the issuer benchmark.
- Goldman Sachs' return convention reflects reinvested distributions; NAV calculation assumes management fees and operating expenses. The index is quarterly reconstituted across value, momentum, quality and low-volatility factors.

### Official July 2026 standardized returns

| Return basis | 1M | YTD | 1Y | 3Y annualized | 5Y annualized | 10Y annualized | Since inception |
|---|---:|---:|---:|---:|---:|---:|---:|
| NAV | 2.42% | 15.60% | 31.15% | 17.33% | 9.83% | 9.01% | 9.50% |
| Market price | 1.03% | 14.27% | 30.33% | 16.95% | 9.50% | 9.20% | 9.41% |
| ActiveBeta Japan Index | 2.46% | 15.65% | 31.23% | 17.37% | 9.81% | 8.90% | 9.38% |
| MSCI Japan - USD (Net) | 1.03% | 16.96% | 32.28% | 17.70% | 9.99% | 9.26% | 9.79% |

### Annual NAV Total Return

| Year | GSJY NAV TR | ActiveBeta Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed (partial inception year) | not disclosed | 11.96% |
| 2017 | 24.52% | 23.99% | 21.83% |
| 2018 | -10.52% | -12.88% | -4.38% |
| 2019 | 18.28% | 19.61% | 31.49% |
| 2020 | 12.52% | 14.44% | 18.40% |
| 2021 | 0.60% | 1.71% | 28.71% |
| 2022 | -15.60% | -16.65% | -18.11% |
| 2023 | 18.92% | 20.32% | 26.29% |
| 2024 | 9.09% | 8.28% | 25.02% |
| 2025 | 25.07% | 24.60% | 17.88% |

Goldman Sachs' official factsheet publishes the calendar rows for 2017-2025; 2016 is
an inception-year partial and is shown as unavailable rather than ranked. The S&P 500
rows reuse the cached USD Total Return convention for the same complete calendar years,
as of 2025-12-31.

## Window calculations and ranking

- Common `2021-2025`: GSJY NAV compound `37.76%`, rounded-input CAGR `6.62%`; positive / negative `3 / 2`.
- `2017-2025`: GSJY NAV compound `104.29%`, rounded-input CAGR `8.26%`; positive / negative `6 / 3`.
- Best complete calendar year: 2017, `+24.52%`; least positive: 2021, `+0.60%`.
- Worst complete calendar year: 2022, `-15.60%`; least bad down year: 2018, `-10.52%`.
- Cached S&P 500 TR common reference is cumulative `96.17%` / CAGR `14.43%` for 2021-2025 and `255.78%` / CAGR `15.14%` for 2017-2025. These are USD reference comparisons, not manager skill or alpha.
- Rolling 10-year issuer CAGR `9.01%` implies normalized growth `100.00 → 236.95`, or `136.95%` cumulative implied growth, via `100 × ((1 + 0.0901)^10 - 1)`. Raw NAV endpoints are not disclosed, so this is not an observed cumulative return.
- Same-window tracking context: NAV trails the ActiveBeta index by `-0.05 pp` YTD, `-0.08 pp` over 1 year, and `+0.11 pp` over 10 years; these small differences are consistent with expenses, transaction costs and implementation effects and are not called alpha.

## Risk read-through

The latest official snapshot reports `155` holdings, net assets `USD 85.21M`, weighted
average market cap `USD 83.95B`, P/E `17.70x`, P/B `1.86x`, ROE `12.00%`, dividend yield
`2.00%`, and 30-Day SEC Yield `1.42%`, all as of 2026-07-31. Sector weights are
Industrials `24.6%`, Financials `20.5%`, Information Technology `17.1%`, Consumer
Discretionary `15.2%`, Health Care `4.7%`, Communication Services `4.5%`, Materials
`4.1%`, Energy `3.2%`, Consumer Staples `3.2%`, Utilities `1.5%`, Real Estate `1.2%`,
and Cash `0.2%`. Total expense ratio is `0.25%`; distributions are normally paid
quarterly.

ความเสี่ยงหลักคือ Japan/country/sector/FX และ factor/smart-beta concentration. Official
prospectus notes that the index methodology may rely on assumptions and estimates, and
that tracking difference may arise from transaction costs, expenses and other factors.
The fund is not actively managed, so it generally does not dispose of securities unless
they leave the index. Official daily NAV history sufficient for an independently
reproducible max drawdown, recovery, or volatility measure is `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official Goldman Sachs factsheet/performance: https://am.gs.com/public-assets/documents/5747f795-24d6-11ef-870d-ed3a247c783e
- Official Goldman Sachs current fund page: https://am.gs.com/en-us/individual/funds/detail/PV102393/381430404/goldman-sachs-active-beta-japan-equity-etf
- Official Goldman Sachs summary prospectus: https://am.gs.com/public-assets/documents/179d857b-24e3-11ef-ad18-377468fbef87?view=true
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
