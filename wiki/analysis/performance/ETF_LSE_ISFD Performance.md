---
type: etf-performance
instrument_type: ETF
entity_key: LSE:ISFD
input_ticker: IRESF
ticker: ISFD
exchange: London Stock Exchange
fund: iShares Core FTSE 100 UCITS ETF USD Hedged (Accumulating)
tracked_index: FTSE 100 Index
benchmark: FTSE 100 Index
management_mode: passive-index-tracking
updated: 2026-08-19
performance_as_of: 2025-12-31
rolling_10y_as_of: not-applicable-lt-10y
current_ytd_as_of: 2026-08-12
price_nav_as_of: 2026-08-12
fund_facts_as_of: 2026-08-12
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; gross income reinvested; net of expenses
return_currency: "USD share-class NAV; benchmark rows GBP"
tags:
  - analysis/etf-performance
  - ticker/ISFD
  - ticker/IRESF
  - geography/United-Kingdom
---

# IRESF / ISFD ETF Performance

> [[ETF Region Index]] → [[United Kingdom ETF]] → [[ETF Performance Index]]

## Bottom line

`IRESF` เป็น OTC input alias ของ share class เดียวกับ official London Stock
Exchange line `LSE:ISFD`, ยืนยันด้วย ISIN `IE00BYZ28W67`. กองทุนคือ iShares
Core FTSE 100 UCITS ETF USD Hedged (Accumulating): passive, physical,
replicated equity ETF, TER `0.20%`, share-class launch 19 ต.ค. 2017 และติดตาม
`FTSE 100 Index`. Share class ใช้ USD และ hedge GBP exposure ด้วย derivatives;
benchmark rows ใน factsheet แสดงเป็น GBP จึงต้องแยก currency basis.

Official complete calendar NAV Total Return rows มีเฉพาะ 2018-2025 เพราะ
share class ยังมี history ต่ำกว่า 10 ปี. ช่วง 2018-2025 compound ได้ `83.09%`
หรือ rounded-input CAGR `7.85%`; common window 2021-2025 ได้ `87.30%` หรือ
`13.37%` ต่อปี โดยเป็นบวกครบ 5 ปี. Latest official product-page NAV TR YTD
คือ `11.08%` ณ 12 ส.ค. 2026; July factsheet ให้ `11.18%` ณ 31 ก.ค. 2026
ซึ่งเป็นคนละ snapshot.

## Performance check

- `entity_key: LSE:ISFD`; `input_ticker: IRESF`; official iShares listing table maps ISIN `IE00BYZ28W67` to `ISFD` on the London Stock Exchange in USD. The OTC symbol is retained only as an input alias.
- Classification: `passive-index`; physical, replicated, Ireland-domiciled UCITS equity ETF. The fund seeks to track the 100 largest UK companies in the FTSE 100 Index.
- Metric: issuer `NAV Total Return` with gross income reinvested where applicable and fund expenses reflected in NAV; market-price return is not mixed into the annual table.
- Share-class launch: 19 ต.ค. 2017; TER `0.20%`; accumulating; quarterly rebalance; 100 holdings as of 12 ส.ค. 2026.
- Latest issuer product-page snapshot: NAV `USD 10.45` and NAV TR YTD `11.08%` as of 12 ส.ค. 2026; share-class net assets `USD 225.39m` and total fund net assets `GBP 16.67bn` as of the same date.
- Official July factsheet as of 31 ก.ค. 2026 reports 1-month `3.63%`, 3-month `5.30%`, 6-month `8.00%`, YTD `11.18%`, 1-year `22.44%`, 3-year annualised `16.17%`, 5-year annualised `13.43%`, and since-inception annualised `8.80%`.
- A 10-year NAV CAGR is `not applicable (<10y history)`; the 2018-2025 CAGR below is a calendar-derived result from eight complete displayed annual rows, not an issuer-labeled 10-year field.

| Year | ISFD Share Class NAV TR (USD) | FTSE 100 Index (GBP) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2018 | -7.49% | -14.11% | -4.38% |
| 2019 | 19.10% | 17.28% | 31.49% |
| 2020 | -11.28% | -11.58% | 18.40% |
| 2021 | 18.42% | 18.40% | 28.71% |
| 2022 | 5.69% | 4.67% | -18.11% |
| 2023 | 8.49% | 7.90% | 26.29% |
| 2024 | 9.66% | 9.63% | 25.02% |
| 2025 | 25.79% | 25.78% | 17.88% |

Official iShares rows are complete calendar-year NAV returns from the July
2026 factsheet. The share-class rows compound to `83.09%` / rounded-input
calendar CAGR `7.85%` for 2018-2025 and `87.30%` / `13.37%` for 2021-2025.
The FTSE 100 benchmark rows compound to `64.23%` / `6.40%` and `84.39%` /
`13.02%`, respectively. The benchmark is displayed in GBP while the share
class is USD hedged, so the rounded differences are tracking observations with
currency/hedge effects, not alpha or manager-skill evidence.

The cached S&P 500 Total Return rows are a common USD reference only. They
compound to `192.03%` / rounded-input CAGR `14.33%` over 2018-2025 and
`96.17%` / `14.43%` over 2021-2025. The S&P 500 is not the strategy-appropriate
benchmark for a UK large-cap ETF.

## Up years / Down years

- Complete 2018-2025 NAV TR up/down: `6 / 2`
- Best NAV TR year: 2025, `+25.79%`
- Least positive year: 2022, `+5.69%`
- Worst NAV TR year: 2020, `-11.28%`
- Least bad down year: 2018, `-7.49%`
- 2018-2025 annual-return standard deviation, population: `12.07%`
- Common 2021-2025 annual-return standard deviation, population: `7.43%`; up/down `5 / 0`

## Current and rolling official fields

| Metric | Value | As of | Basis |
|---|---:|---|---|
| Current NAV TR YTD | 11.08% | 2026-08-12 | official product page |
| NAV | USD 10.45 | 2026-08-12 | official product page |
| Factsheet YTD | 11.18% | 2026-07-31 | official factsheet |
| 1-year NAV TR | 22.44% | 2026-07-31 | official factsheet |
| 3-year annualised NAV TR | 16.17% | 2026-07-31 | official factsheet |
| 5-year annualised NAV TR | 13.43% | 2026-07-31 | official factsheet |
| Since-inception annualised NAV TR | 8.80% | 2026-07-31 | official factsheet |
| 3-year standard deviation | 9.46% | 2026-07-31 | official product page |
| 3-year beta | 0.989 | 2026-07-31 | official product page |
| Price / book | 2.40x | 2026-08-12 | official product page |
| Price / earnings | 18.04x | 2026-08-12 | official product page |

## Risk read-through

ความเสี่ยงหลักคือ UK single-country/large-cap concentration, sector mix,
GBP/USD hedge implementation, hedge cost, equity volatility, liquidity,
counterparty และ securities lending. Official exposure snapshot ณ 12 ส.ค.
2026 มี Financials `28.48%`, Industrials `14.14%`, Consumer Staples `13.27%`,
Health Care `11.36%`, Energy `10.49%` และ Materials `8.15%`. กองทุนใช้
currency-hedged share class ซึ่งช่วยลดผลของ GBP/USD แต่ไม่ได้ลบ tracking,
forward/counterparty หรือ basis risk. Official daily NAV maximum drawdown และ
recovery date ไม่ได้เปิดเผยใน reviewed sources; `risk-adjusted evidence:
not-verified` สำหรับสองฟิลด์นี้.

## Sources

- [iShares professional product page](https://www.ishares.com/uk/professionals/en/products/291401/?siteEntryPassthrough=true&switchLocale=y) — official identity, LSE listing, ISIN, current NAV/YTD, assets, holdings, benchmark, structure, fee, beta, standard deviation and exposures.
- [iShares July 2026 factsheet](https://www.ishares.com/gls-download/literature/fact-sheet/isfd-ishares-core-ftse-100-ucits-etf-fund-fact-sheet-en-gb.pdf) — official 2018-2025 calendar NAV/benchmark rows, return definition, rolling performance and dated fund facts.
- [MarketScreener IRESF page](https://www.marketscreener.com/quote/etf/ISHARES-CORE-FTSE-100-UCI-66468693/) — secondary OTC alias and ISIN cross-check only; not primary NAV evidence.
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached S&P 500 Total Return references — common USD reference for the displayed calendar rows.
- [[ETF_performance_sources_2026-08-19]] — source map, raw observations, calculations, reconciliation and scheduled-local verification record.

## Follow-up

- Refresh the official product-page NAV/YTD together on the next run and retain the July factsheet snapshot as historical evidence.
- Keep the USD hedged share-class NAV, GBP benchmark rows and USD S&P common reference separate; do not infer alpha from arithmetic differences.
- Verify official daily NAV drawdown/recovery if iShares publishes a suitable dated series.
