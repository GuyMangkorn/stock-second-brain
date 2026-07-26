---
type: etf-performance
instrument_type: ETF
entity_key: LSE:FLXI
ticker: FLIBF
listing_ticker: FLXI
exchange: LSE
fund: Franklin FTSE India UCITS ETF
tracked_index: FTSE India 30/18 Capped Index-NR
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FLIBF
  - geography/India
---

# FLIBF / FLXI Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

Input ticker `FLIBF` เป็น OTC alias ของ USD line `LSE:FLXI` สำหรับ Franklin FTSE India UCITS ETF. กองทุนเป็น indexed, physical, full-replication India equity ETF ที่ติดตาม `FTSE India 30/18 Capped Index-NR` และเริ่มเมื่อ `2019-06-25`; จึงยังไม่มี 10-year NAV Total Return. Official Franklin factsheet ณ `2026-06-30` ระบุ available-period NAV TR cumulative `64.43%` และ annualized `7.35%`; current official NAV TR YTD คือ `-8.42%`.

## Performance check

- `entity_key: LSE:FLXI` (canonical USD London Stock Exchange line; input alias `FLIBF` is not used as the durable exchange key)
- Fund: Franklin FTSE India UCITS ETF
- Inception: `2019-06-25`; official share-class/fund history is shorter than 10 years.
- Metric: `NAV Total Return` in USD, based on the ETF NAV; the accumulating share class reinvests income in the NAV. Market-price return is kept separate.
- Tracked index (issuer benchmark): `FTSE India 30/18 Capped Index-NR`
- Expense ratio: `0.19%` total expense ratio.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR: `unavailable`; the latest official history ends at `2026-06-30`, about `7.014374` elapsed years from inception.
- Available-period official observation: cumulative NAV TR `64.43%` and issuer-reported annualized NAV TR `7.35%` from `2019-06-25` to `2026-06-30`. Raw start/end NAV TR values are not disclosed. Using the rounded cumulative figure, `(1 + 64.43%)^(1 / 7.014374) - 1` gives an approximate `7.35%`, consistent with the issuer's annualized field.
- Latest official current-YTD field: `-8.42%` as of `2026-06-30`; latest displayed NAV `US$41.63` as of `2026-07-07` is a price/NAV observation, not a return.
- Coverage/source note: official complete calendar NAV rows are available for `2020-2025`; `2019` is an incomplete inception year. The S&P 500 rows reuse the cached USD Total Return convention as of `2025-12-31`.

| Year | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2019† | not disclosed; partial inception year | 31.49% |
| 2020 | 12.48% | 18.40% |
| 2021 | 24.89% | 28.71% |
| 2022 | -7.89% | -18.11% |
| 2023 | 22.37% | 26.29% |
| 2024 | 10.61% | 25.02% |
| 2025 | 2.63% | 17.88% |
| 2026 YTD | -8.42% as of 2026-06-30 | not comparable; current year not cached |

**Up years / Down years**

- Up years / Down years: `5 / 1` across complete calendar years `2020-2025`.
- Best: `2021`, `24.89%`
- Least positive: `2025`, `2.63%`
- Worst: `2022`, `-7.89%`
- Least bad down year: `2022`, `-7.89%`
- 2020-2025 compound / CAGR from rounded official rows: `79.74% / 10.27%`; S&P 500 TR: `132.26% / 15.08%`.
- 2021-2025 compound / CAGR: `59.80% / 9.83%`; S&P 500 TR: `96.17% / 14.43%`.

## Risk read-through

The available-period official NAV TR annualized return is `7.35%`, not a 10-year CAGR. FLXI is a single-country India large-/mid-cap equity ETF with `277` holdings; Franklin's June factsheet reports 5-year standard deviation `15.08%` as of `2026-05-31`, financials exposure `28.29%`, and top issuer Reliance Industries at `5.72%`. India country, INR/USD currency, emerging-market liquidity, political/regulatory, sector-concentration, and valuation risks remain material. The official factsheet also notes that the Fund is physical and full replication; NAV return and market-price return are not mixed.

## Sources

- [Franklin Templeton official product/performance page](https://www.franklintempleton.co.uk/our-funds/etf/price-and-performance/products/27853/SINGLCLASS/franklin-ftse-india-ucits-etf/IE00BHZRQZ17) — identity, indexed equity classification, benchmark, inception, TER, current NAV and month-end performance fields.
- [Franklin Templeton June 2026 factsheet](https://www.franklintempletonoffshore.com/download/en-os/factsheet/eb953849-e3ab-40a6-b777-15a7ba704486/Factsheet-FranklinFTSEIndiaUCITSETF-27853-FF-NRC-en-OS.PDF) — USD/LSE ticker mapping, available-period cumulative/annualized NAV TR, annual rows, YTD and risk/holdings data.
- [Franklin Templeton KIID](https://www.franklintempleton.co.uk/download/en-gb/KIID/36ada32a-c060-4f7d-87ad-83346b67d733/KIID_IE00BHZRQZ17_en_GB.pdf) — fund objective, accumulating share class and index-tracking policy.
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — benchmark definition; annual rows reuse the cached convention.
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
