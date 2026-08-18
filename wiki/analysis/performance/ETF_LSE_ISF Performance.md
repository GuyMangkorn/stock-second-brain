---
type: etf-performance
instrument_type: ETF
entity_key: LSE:ISF
input_ticker: BCYIF
ticker: ISF
exchange: London Stock Exchange
fund: iShares Core FTSE 100 UCITS ETF GBP (Distributing)
tracked_index: FTSE 100 Index
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: not-issuer-disclosed
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; gross income reinvested where applicable; fund expenses reflected in NAV
return_currency: GBP share-class NAV; S&P 500 reference is USD
tags:
  - analysis/etf-performance
  - ticker/ISF
  - ticker/BCYIF
  - geography/United-Kingdom
---

# ISF Performance

> Navigation: [[ETF Region Index]] → [[United Kingdom ETF]] → [[ETF Performance Index]]

## Bottom line

`BCYIF` เป็น OTC input alias ของ official GBP distributing line `LSE:ISF` ของ
iShares Core FTSE 100 UCITS ETF โดย match ผ่าน ISIN `IE0005042456`. กองทุนเป็น
passive, physical, replicated equity ETF ที่ติดตาม `FTSE 100 Index`. Official
2016-2025 NAV TR rows ให้ cumulative `130.92%` และ rounded-input calendar CAGR
`8.73%`; common 2021-2025 ให้ `83.60%` / `12.92%`. ค่า 8.73% เป็น calendar
CAGR จาก annual rows ไม่ใช่ issuer-labeled rolling 10-year field. Latest official
NAV TR YTD คือ `11.05%` ณ 13 ส.ค. 2026.

## Performance check

- `entity_key: LSE:ISF`; `input_ticker: BCYIF`; the official iShares listing table maps ISIN `IE0005042456` to `ISF` on the London Stock Exchange in GBP. The OTC symbol is retained only as an input alias.
- Classification: `passive-index`; physically replicated, Ireland-domiciled UCITS equity ETF. The fund seeks to track the 100 largest UK companies in the FTSE 100 Index.
- Metric: issuer `NAV Total Return` with gross income reinvested where applicable; market-price return is not mixed. Share-class currency is GBP.
- Tracked index: `FTSE 100 Index`; `S&P 500 Total Return` is a separate common reference in USD and is not a currency-matched performance comparator.
- Share-class launch date: 27 เม.ย. 2000; total expense ratio `0.07%`; distribution frequency `quarterly`; methodology `replicated`; product structure `physical`.
- Official rolling fields from the July 2026 factsheet as of 31 ก.ค. 2026: NAV 1-month `3.61%`, 3-month `5.38%`, 6-month/YTD `8.20%`, 1-year `22.68%`, 3-year annualised `16.11%`, 5-year annualised `13.02%`, and since inception annualised `5.60%`. No issuer-labeled 10-year field is shown in the reviewed capture.
- Latest official product-page snapshot: NAV `£10.50` as of 14 ส.ค. 2026; NAV TR YTD `11.05%` as of 13 ส.ค. 2026; 100 holdings as of 13 ส.ค. 2026; share-class net assets `£16,485.15m` as of 14 ส.ค. 2026.
- The factsheet notes that the benchmark changed from a total-return series to a net-of-tax total-return series on 17 ก.ค. 2019; historic benchmark data was simulated to reflect the change.

| Year | ISF Share Class NAV TR (GBP) | FTSE 100 Index (GBP) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2016 | 19.03% | 19.04% | 11.96% |
| 2017 | 11.94% | 11.91% | 21.83% |
| 2018 | -8.83% | -8.77% | -4.38% |
| 2019 | 17.18% | 17.28% | 31.49% |
| 2020 | -11.64% | -11.58% | 18.40% |
| 2021 | 18.31% | 18.40% | 28.71% |
| 2022 | 4.62% | 4.67% | -18.11% |
| 2023 | 7.80% | 7.90% | 26.29% |
| 2024 | 9.50% | 9.63% | 25.02% |
| 2025 | 25.66% | 25.78% | 17.88% |

Official iShares rows are complete calendar-year GBP NAV returns from the July
2026 factsheet. ISF Share Class rows compound to `130.92%` / rounded-input
calendar CAGR `8.73%` for 2016-2025 and `83.60%` / `12.92%` for 2021-2025. The
FTSE 100 benchmark rows compound to `132.39%` / `8.80%` and `84.39%` / `13.02%`;
rounded-input fund-minus-index differences are approximately `-0.07 pp` and
`-0.10 pp`, not alpha. The S&P 500 rows are retained as a USD reference only;
no direct GBP/USD CAGR gap is asserted.

## Up years / Down years

- Complete 2016-2025 NAV TR up/down: `8 / 2`
- Best NAV TR year: 2025, `+25.66%`
- Least positive year: 2022, `+4.62%`
- Worst NAV TR year: 2020, `-11.64%`
- Least bad down year: 2018, `-8.83%`
- 2016-2025 cumulative/CAGR: `130.92%` / `8.73%`; this is compounded from rounded official annual inputs, not an issuer-labeled rolling-10-year field.
- Common 2021-2025 NAV TR cumulative/CAGR: `83.60%` / `12.92%`.
- Latest official NAV TR YTD: `+11.05%` as of 13 ส.ค. 2026; the July factsheet's earlier YTD observation was `+11.42%` as of 31 ก.ค. 2026.

## Risk read-through

The official 31 ก.ค. 2026 factsheet reports 3-year standard deviation of `9.57%`
and the product page reports 3-year beta of `1.00` as of the same date. The
portfolio had 100 holdings as of 13-14 ส.ค. 2026, with sector weights Financials
`28.65%`, Industrials `14.15%`, Consumer Staples `13.45%`, Health Care `11.21%`,
and Energy `10.59%`. UK/country, GBP share-class and sector concentration risks
remain relevant; a U.S. investor also has GBP/USD translation risk. Official
daily NAV maximum drawdown and recovery date were not disclosed in the reviewed
capture, so `risk-adjusted evidence: not-verified` for those fields. The 0.07%
TER and physical replication support low tracking friction but do not remove
country or currency risk.

## Sources

- [iShares Core FTSE 100 UCITS ETF product page](https://www.ishares.com/uk/individual/en/products/251795/ishares-core-ftse-100-ucits-etf) — official ISIN/listing map, NAV/YTD, fund facts, benchmark, risk and exposure snapshot
- [iShares Core FTSE 100 factsheet, July 2026](https://www.ishares.com/gls-download/literature/fact-sheet/isf-ishares-core-ftse-100-ucits-etf-fund-fact-sheet-en-gb.pdf) — official 2016-2025 NAV/index rows, rolling returns, structure and trading information
- [iShares Core FTSE 100 GBP distributing KIID](https://www.ishares.com/uk/individual/en/literature/kiid/ucits_kiid-ishares-core-ftse-100-ucits-etf-gbp-dist-gb-ie0005042456-en.pdf?siteEntryPassthrough=true&switchLocale=y) — official passive/replication, benchmark and share-class risk/charge disclosures
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
