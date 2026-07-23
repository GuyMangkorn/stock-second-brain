---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLIN
ticker: FLIN
exchange: NYSE Arca
fund: Franklin FTSE India ETF
tracked_index: FTSE India Capped Index-NR
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FLIN
  - geography/India
---

# FLIN Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

FLIN เป็น passive/index-tracking India equity ETF ของ Franklin ติดตาม `FTSE India Capped Index-NR` และเริ่มกองทุนเมื่อ 2018-02-06. Official 10-year NAV TR unavailable เพราะกองทุนยังมีประวัติไม่ครบ 10 ปี; official available-period NAV Total Return annualized คือ `5.91%` จาก 2018-02-06 ถึง 2026-06-30 (`8.39` ปี). เมื่อ normalize จาก 100.00 จะเท่ากับประมาณ 161.93 ที่ปลายช่วง. Current standardized NAV TR YTD คือ `-8.34%` ณ 2026-06-30.

## Performance check

- `entity_key`: `NYSE Arca:FLIN`
- Fund: Franklin FTSE India ETF; asset class `Equity`; ETF type `Indexed`; net expense ratio `0.19%`
- Inception: `2018-02-06`
- Metric: official NAV Total Return, รวม reinvested distributions และหัก fund expenses แล้ว
- Issuer benchmark: FTSE India Capped Index-NR; market-capitalization weighted Indian large- and mid-cap index with issuer-weight caps
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not issuer benchmark)

### Available-period NAV TR window

| Start date | End date | Actual years | Start TR value | End TR value | Annualized return | Disclosure |
|---|---|---:|---:|---:|---:|---|
| 2018-02-06 | 2026-06-30 | 8.39 | 100.00 (normalized) | approx. 161.93 (calculated from official CAGR) | 5.91% | Official 10-year field is `—`; raw start/end NAV TR values not disclosed |

สูตร normalized endpoint: `100.00 × (1 + 5.91%)^8.394 = 161.93`; ค่านี้เป็นการคำนวณจาก issuer-reported available-period annualized return ไม่ใช่ raw NAV และไม่ควรเรียกเป็น 10-year result.

### Annual NAV Total Return

| Year | FLIN NAV TR | FTSE India Capped Index-NR TR | S&P 500 TR |
|---|---:|---:|---:|
| 2018 | not applicable (partial inception year) | not applicable (partial inception year) | -4.38% |
| 2019 | 4.93% | 6.38% | 31.49% |
| 2020 | 15.16% | 16.53% | 18.40% |
| 2021 | 24.82% | 28.77% | 28.71% |
| 2022 | -8.19% | -8.36% | -18.11% |
| 2023 | 20.71% | 25.30% | 26.29% |
| 2024 | 10.47% | 12.99% | 25.02% |
| 2025 | 2.21% | 3.84% | 17.88% |
| 2026 YTD | -8.34% | -9.68% | not comparable; current year not cached |

Franklin factsheet as of 2026-06-30 provides complete calendar rows for `2019-2025`; 2018 is shown only as a partial inception-year marker. S&P 500 rows reuse the cached USD Total Return convention as of `2025-12-31`; 2026 YTD ไม่ใช้แทน complete calendar year.

### Window calculations and ranking

- Complete-calendar window `2019-2025`: FLIN NAV TR cumulative `88.74%`, CAGR `9.50%`; FTSE India Capped Index-NR cumulative `115.06%`, CAGR `11.56%`.
- Common complete-calendar window `2021-2025`: FLIN NAV TR cumulative `56.19%`, CAGR `9.33%`; S&P 500 TR cumulative `96.17%`, CAGR `14.43%`; FLIN trails by approximately `5.10 pp` CAGR.
- Up years / down years in `2021-2025`: `4 / 1`.
- Best complete year: `2021`, `24.82%`; worst complete year: `2022`, `-8.19%`.
- Current NAV TR YTD: `-8.34%` as of `2026-06-30`; this is a partial-year observation, not a calendar-year ranking.

## Risk read-through

FLIN เป็น single-country India equity exposure with `283` holdings as of `2026-06-30`; 3-year NAV-return standard deviation is `15.09%` versus `17.36%` for the benchmark. Portfolio P/E is `21.58x` and P/B `3.34x` as of the same factsheet date. Franklin notes that emerging-market, currency, country concentration and non-diversification risks can increase volatility; daily NAV history sufficient for fund-level max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

## Sources

- Official issuer product/performance page: https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26348/SINGLCLASS/franklin-ftse-india-etf/FLIN
- Official Franklin factsheet (performance through 2026-06-30): https://www.franklintempleton.com/forms-literature/download/FLIN-FF
- Official summary prospectus: https://www.franklintempleton.com/tools-and-resources/literature/info/FLIN-PSUM
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]]
- Navigation: [[India ETF]] | [[ETF Region Index]] | [[ETF Performance Index]]
