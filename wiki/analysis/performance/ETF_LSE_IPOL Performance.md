---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IPOL
ticker: IPOL
input_ticker: IPLCF
exchange: London Stock Exchange
fund: iShares MSCI Poland UCITS ETF USD (Acc)
tracked_index: MSCI Emerging - Poland in Net USD
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-08-14
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IPOL
  - ticker/IPLCF
  - geography/Poland
---

# IPOL Performance

> Navigation: [[ETF Region Index]] → [[Poland ETF]] → [[ETF Performance Index]]

## Bottom line

`IPLCF` เป็น OTC input alias ของ official USD listing `LSE:IPOL` ของ iShares
MSCI Poland UCITS ETF USD (Acc). กองทุนเป็น passive, physical, replicated และ
ใช้ income แบบ accumulating. Current official page capture รายงาน NAV Total
Return YTD `+27.44%` และ NAV `US$42.02` ณ 2026-08-14. Issuer rolling table ใน
capture เดียวกันรายงาน 10-year NAV TR แบบ annualised `10.24%` และ cumulative
`164.99%` เทียบ benchmark `10.43%` และ `169.59%`; table ไม่แสดง selected as-of
date แยกใน HTML จึงเก็บเป็น issuer-current capture ไม่ใช่การคำนวณจาก annual rows.

## Performance check

- `entity_key: LSE:IPOL`; `input_ticker: IPLCF`; official USD line on London Stock Exchange; LSE listing date `2011-01-24`; ISIN `IE00B4M7GH52`.
- Fund launch `2011-01-21`; benchmark/tracked index `MSCI Emerging - Poland in Net USD`; return metric `NAV Total Return` in USD with gross income reinvested where applicable.
- Total Expense Ratio `0.74%`; accumulating; Ireland-domiciled UCITS; physical and replicated; quarterly rebalance.
- Official current snapshot: net assets `US$1.126B` and 16 holdings as of 2026-08-14; 3-year beta `0.993` and standard deviation `22.01%` as of 2026-07-31; P/E `17.22` and P/B `2.11` as of 2026-08-14.
- 2021-2025 factsheet rows give NAV TR cumulative `90.51%` and rounded-input CAGR `13.76%`; the tracked benchmark cumulative `91.15%` and CAGR `13.83%`, a return-only tracking gap of about `-0.08 pp` CAGR. S&P 500 TR is shown only as a common reference, not as the management benchmark.
- The 2016-2025 annual table has a source conflict for 2020: the official March 2026 USD accumulating factsheet reports `+1.91%`, while the current live product-page table reports `-11.9%`. The conflict is preserved and no 2016-2025 cumulative/CAGR is calculated from the conflicting annual series.

| Year | IPOL NAV TR (factsheet) | MSCI Emerging - Poland in Net USD | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 0.02% | 0.13% | 11.96% |
| 2017 | 54.33% | 54.72% | 21.83% |
| 2018 | -13.14% | -12.87% | -4.38% |
| 2019 | -6.03% | -5.87% | 31.49% |
| 2020 | 1.91%† | 1.39%† | 18.40% |
| 2021 | 8.16% | 8.46% | 28.71% |
| 2022 | -27.36% | -27.24% | -18.11% |
| 2023 | 48.25% | 48.60% | 26.29% |
| 2024 | -6.47% | -6.65% | 25.02% |
| 2025 | 74.88% | 74.61% | 17.88% |

`†` Official March 2026 factsheet values for the USD accumulating share class;
BlackRock's current live product page shows 2020 fund/benchmark returns of
`-11.9%` / `-11.4%`. This unresolved source conflict is the reason the
2016-2025 annual CAGR is not presented as verified.

## Up years / Down years

- Factsheet annual rows: `6 / 4` up/down years across 2016-2025.
- Best complete calendar year: 2025, `+74.88%`; worst: 2022, `-27.36%`.
- Common 2021-2025 window: `3 / 2` up/down years; cumulative `90.51%`; rounded-input CAGR `13.76%`. The tracked benchmark cumulative is `91.15%` / CAGR `13.83%`.
- S&P 500 TR cached common-window cumulative is `96.17%` / CAGR `14.43%`; this is a common-reference comparison only and is not alpha or manager-skill evidence.
- Current YTD: IPOL NAV TR `+27.44%` as of 2026-08-14. A same-date S&P 500 TR pairing was not used; the separately captured S&P current YTD is dated 2026-08-17.

## Risk read-through

IPOL เป็น single-country Poland equity exposure ใน emerging market และมี
concentration สูง: Financials `45.80%`, Energy `16.68%`, Consumer Discretionary
`12.86%` ณ 2026-08-06. Official risk text เน้น emerging-market, country,
currency, equity, counterparty และ liquidity risk. แม้ 3-year beta `0.993` และ
standard deviation `22.01%` จะให้ risk snapshot ที่ตรวจสอบได้ แต่ official daily
NAV series สำหรับ maximum drawdown และ recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.
ไม่มี cash distributions เพราะ share class เป็น accumulating.

## Sources

- [BlackRock/iShares IPOL product page](https://www.blackrock.com/uk/individual/products/251875/ishares-msci-poland-ucits-etf_1) — current NAV/YTD, rolling table, fund facts, risk and listings.
- [iShares MSCI Poland UCITS ETF factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/spol-ishares-msci-poland-ucits-etf-fund-fact-sheet-en-gb.pdf) — USD accumulating share-class annual rows and benchmark.
- [iShares professional product page](https://www.ishares.com/uk/professionals/en/products/251875/ishares-msci-poland-ucits-etf?shortLocale=en_GB&siteEntryPassthrough=true&switchLocale=y) — listing map, holdings, exposures and risk fields.
- [S&P 500 Total Return report](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=df8ec300-24ad-4c70-81d3-a3dcce0200e2&sourceIdentifier=index-family-specialization) — current cross-check only; dates do not match IPOL YTD.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
