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
updated: 2026-08-29
performance_as_of: 2026-08-27
rolling_10y_as_of: 2026-08-27
rolling_10y_date_status: issuer current capture; selected return date not exposed
standardized_performance_as_of: 2026-07-31
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-27
fund_facts_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV Total Return
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
Return YTD `+28.91%` ณ 2026-08-26 และ NAV `US$41.43` ณ 2026-08-27. Issuer
rolling table ใน capture ล่าสุดรายงาน 10-year NAV TR แบบ annualised `10.24%`
และ cumulative `164.99%` เทียบ benchmark `10.43%` และ `169.59%`; table ไม่แสดง
selected as-of date แยกใน HTML จึงเก็บเป็น issuer-current capture ไม่ใช่การ
คำนวณจาก annual endpoints.

## Performance check

- `entity_key: LSE:IPOL`; `input_ticker: IPLCF`; official USD line on London Stock Exchange; LSE listing date `2011-01-24`; ISIN `IE00B4M7GH52`.
- Fund launch `2011-01-21`; benchmark/tracked index `MSCI Emerging - Poland in Net USD`; return metric `NAV Total Return` in USD with gross income reinvested where applicable.
- Total Expense Ratio `0.74%`; accumulating; Ireland-domiciled UCITS; physical and replicated; quarterly rebalance.
- Official current snapshot: NAV `US$41.43` as of 2026-08-27; NAV TR YTD `28.91%` as of 2026-08-26; net assets `US$1,114,481,096` as of 2026-08-27; 16 holdings as of 2026-08-26; P/E `17.26` and P/B `2.13` as of 2026-08-26; 3-year beta `0.993` and standard deviation `22.01%` as of 2026-07-31.
- Official 25 Aug sector snapshot: Financials `46.28%`, Energy `16.71%`, Consumer Discretionary `12.42%`, Materials `9.67%`, Consumer Staples `5.72%`, Communication `2.98%`, Information Technology `2.42%`, Utilities `1.79%`, Industrials `1.71%` and Cash/Derivatives `0.31%`.
- July 2026 factsheet standardized NAV/benchmark fields as of 2026-07-31: 1M `10.12%`/`10.19%`, 3M `11.83%`/`11.53%`, 6M `12.94%`/`12.82%`, YTD `21.20%`/`21.13%`, 1Y `38.59%`/`38.12%`, 3Y `30.08%`/`29.89%`, 5Y `15.80%`/`15.81%` and since inception `3.06%`/`3.14%`.
- 2021-2025 factsheet rows give NAV TR cumulative `90.51%` and rounded-input CAGR `13.76%`; the tracked benchmark cumulative `91.15%` and CAGR `13.83%`, a return-only tracking gap of about `-0.08 pp` CAGR. S&P 500 TR is shown only as a common reference, not as the management benchmark.
- The latest July 2026 USD accumulating factsheet and current live product-page table align on 2020 `-11.91%`; an earlier March 2026 factsheet snapshot in the prior batch reported `+1.91%`. The version conflict is retained, but the latest aligned July/live annual series is used for the 2016-2025 calculation.

| Year | IPOL NAV TR (factsheet) | MSCI Emerging - Poland in Net USD | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 0.02% | 0.13% | 11.96% |
| 2017 | 54.33% | 54.72% | 21.83% |
| 2018 | -13.14% | -12.87% | -4.38% |
| 2019 | -6.03% | -5.87% | 31.49% |
| 2020 | -11.91% | -11.39% | 18.40% |
| 2021 | 8.16% | 8.46% | 28.71% |
| 2022 | -27.36% | -27.24% | -18.11% |
| 2023 | 48.25% | 48.60% | 26.29% |
| 2024 | -6.47% | -6.65% | 25.02% |
| 2025 | 74.88% | 74.61% | 17.88% |

`*` The prior March 2026 factsheet snapshot recorded 2020 fund/benchmark returns
of `+1.91%` / `+1.39%`; the latest July 2026 factsheet and live page record
`-11.91%` / `-11.39%`. The latest aligned official pair is used, and the
version conflict remains disclosed in the source batch.

## Up years / Down years

- Latest July/live annual rows: `6 / 4` up/down years across 2016-2025.
- Best complete calendar year: 2025, `+74.88%`; worst: 2022, `-27.36%`.
- Latest July/live 2016-2025 window: cumulative `111.45%`; rounded-input CAGR
  `7.78%`. This calculation uses the latest aligned official annual series,
  including 2020 `-11.91%`.
- Common 2021-2025 window: `3 / 2` up/down years; cumulative `90.51%`; rounded-input CAGR `13.76%`. The tracked benchmark cumulative is `91.15%` / CAGR `13.83%`.
- Current issuer rolling fund-minus-index difference is `-4.60 pp` cumulative
  and `-0.19 pp` annualized over 10 years; the 2021-2025 difference is about
  `-0.08 pp` CAGR. These are tracking observations, not alpha.
- S&P 500 TR cached common-window cumulative is `96.17%` / CAGR `14.43%`; this is a common-reference comparison only and is not alpha or manager-skill evidence.
- Common S&P 500 TR comparison: IPOL 2016-2025 CAGR `7.78%` versus S&P 500 TR `14.82%` (`-7.04 pp`); 2021-2025 `13.76%` versus `14.43%` (`-0.67 pp`).
- Current YTD: IPOL NAV TR `+28.91%` as of 2026-08-26. July standardized YTD `+21.20%` and the separately captured S&P current YTD are different windows; no same-date S&P pairing is inferred.

## Risk read-through

IPOL เป็น single-country Poland equity exposure ใน emerging market และมี
concentration สูง: Financials `46.28%`, Energy `16.71%`, Consumer Discretionary
`12.42%` ณ 2026-08-25; Materials `9.67%` และ Consumer Staples `5.72%` เป็น
น้ำหนักถัดมา. Official risk text เน้น emerging-market, country,
currency, equity, counterparty และ liquidity risk. แม้ 3-year beta `0.993` และ
standard deviation `22.01%` จะให้ risk snapshot ที่ตรวจสอบได้ แต่ official daily
NAV series สำหรับ maximum drawdown และ recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.
ไม่มี cash distributions เพราะ share class เป็น accumulating.

## Source-quality notes

- BlackRock/iShares current page and the latest July USD accumulating factsheet
  are used as the canonical pair. The earlier March factsheet snapshot's 2020
  `+1.91%` conflicts with the latest July/live `-11.91%`; the latest aligned
  official series is used for the annual calculation and the version conflict is
  not hidden.
- The rolling `10.24%` / `164.99%` field is an issuer current-page capture; its
  selected return date is not exposed in the HTML, so it is kept separate from
  the independently compounded annual rows.
- Official daily NAV history sufficient for maximum drawdown and recovery is
  `ไม่พบข้อมูลที่ยืนยันได้`; no numeric secondary proxy is saved. Point-in-time
  NAV, YTD return, AUM, holdings, characteristics, sectors and rolling fields
  retain separate as-of dates.

## Sources

- [BlackRock/iShares IPOL product page](https://www.blackrock.com/uk/individual/products/251875/ishares-msci-poland-ucits-etf_1) — current NAV/YTD, rolling table, fund facts, risk and listings through 27 Aug 2026.
- [iShares MSCI Poland UCITS ETF July factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/spol-ishares-msci-poland-ucits-etf-fund-fact-sheet-en-gb.pdf) — latest USD accumulating share-class annual, July standardized and benchmark rows.
- [iShares professional product page](https://www.ishares.com/uk/professionals/en/products/251875/ishares-msci-poland-ucits-etf?shortLocale=en_GB&siteEntryPassthrough=true&switchLocale=y) — listing map, holdings, exposures and risk fields.
- [BlackRock Denmark product page](https://www.blackrock.com/dk/individual/products/251875/ishares-msci-poland-ucits-etf) — adjacent-locale current NAV/YTD and sector cross-check.
- [S&P 500 Total Return report](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=df8ec300-24ad-4c70-81d3-a3dcce0200e2&sourceIdentifier=index-family-specialization) — current cross-check only; dates do not match IPOL YTD.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
