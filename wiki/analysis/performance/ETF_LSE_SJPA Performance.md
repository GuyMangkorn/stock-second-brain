---
type: etf-performance
instrument_type: ETF
entity_key: LSE:SJPA
ticker: SJPA
exchange: LSE
input_alias: IHREF (OTC)
fund: iShares Core MSCI Japan IMI UCITS ETF
tracked_index: MSCI Japan Investable Market Net Index (USD)
benchmark: S&P 500 Total Return
updated: 2026-08-28
performance_as_of: 2026-07-31
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-26
fund_facts_as_of: 2026-08-26
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return (USD); gross income reinvested
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SJPA
  - ticker/IHREF
  - geography/Japan
---

# SJPA Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

Input `IHREF` เป็น OTC alias ของ iShares Core MSCI Japan IMI UCITS ETF; issuer
ยืนยัน primary listing `SJPA` บน London Stock Exchange สำหรับ ISIN
`IE00B4L5YX21`. Share class ที่ตรวจสอบเป็น USD (Accumulating) แต่ listing
`LSE:SJPA` ใช้ GBP; จึงแยก listing currency ออกจาก USD NAV return. กองทุนเป็น
passive physical equity ETF ที่ติดตาม `MSCI Japan Investable Market Net Index
(USD)`. Current official NAV TR YTD คือ `19.87%` ณ 2026-08-26; NAV ล่าสุดที่
ตรวจสอบได้คือ `USD 82.57` ณ 2026-08-26. Current capture ไม่เปิดเผยตัวเลข
rolling 10-year ที่ reconcile ได้; complete calendar 2016-2025 rows ให้
cumulative `104.57%` และ rounded-input CAGR `7.42%`.

## Performance check

- `entity_key`: `LSE:SJPA`
- Input alias: `IHREF` (OTC); canonical issuer/exchange listing: `SJPA` (LSE); ISIN `IE00B4L5YX21`
- Share class: USD (Accumulating); LSE:SJPA listing currency GBP; same share class also has an LSE USD listing under `IJPA`
- Inception: `2009-09-25`
- Total Expense Ratio: `0.12%`; use of income `accumulating`; product structure `physical`; methodology `optimised`; rebalance frequency `quarterly`
- Metric: NAV Total Return (USD); issuer states performance is on a NAV basis with gross income reinvested where applicable. Market price is kept separate from NAV performance.
- Tracked index (issuer benchmark): `MSCI Japan Investable Market Net Index (USD)`
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not issuer benchmark)
- 10-year calendar coverage: official `2016-2025` rows; actual years `10.00`
- 2016-2025 calendar NAV TR cumulative / rounded-input CAGR: `104.57%` / `7.42%`; normalized review endpoints are `100.00` and `204.57`; raw NAV endpoints are not disclosed
- Current snapshot: NAV `USD 82.57`, share-class net assets `USD 8,336,622,614`, fund net assets `USD 8,660,886,597`, and `955` holdings, all as of `2026-08-26`; current NAV TR YTD is `19.87%` as of `2026-08-26`.
- Current portfolio metrics: P/B `1.88` and P/E `18.73` as of `2026-08-26`; 3-year standard deviation `14.77%` and beta `0.993` as of `2026-07-31`.
- Rolling 10-year issuer field: `not disclosed` in the current July 2026 factsheet/product capture. A prior dated capture recorded `147.80%` cumulative / `9.50%` CAGR for 2016-06-30 to 2026-06-30, but it conflicts with the current official 2016-2025 series and is not carried into the current ranking.
- Coverage/source note: the July 2026 factsheet provides the two-decimal 2016-2025 calendar series; the current product page supplies the later NAV/current-YTD snapshot. Calendar calculations use displayed rounded inputs, not a market-price proxy.

| Year | SJPA NAV TR | MSCI Japan Investable Market Net Index (USD) TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 3.12% | 3.25% | 11.96% |
| 2017 | 25.09% | 25.25% | 21.83% |
| 2018 | -13.58% | -13.46% | -4.38% |
| 2019 | 19.43% | 19.56% | 31.49% |
| 2020 | 13.03% | 13.10% | 18.40% |
| 2021 | 0.92% | 0.98% | 28.71% |
| 2022 | -15.88% | -15.78% | -18.11% |
| 2023 | 18.86% | 18.96% | 26.29% |
| 2024 | 7.47% | 7.57% | 25.02% |
| 2025 | 25.36% | 25.45% | 17.88% |
| 2026 YTD (month-end) | 16.99% | 17.02% | not comparable; current year not cached |

MSCI Japan Investable Market Net Index (USD) เป็น issuer benchmark ของ SJPA;
S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark. ตาราง S&P ใช้
cached USD Total Return convention ณ 2025-12-31. Current product-page YTD เป็น
ข้อมูล ณ 2026-08-26; month-end row ใช้ July 2026 factsheet ณ 2026-07-31.

## Up years / Down years

- Up years / Down years: `8 / 2` in complete 2016-2025 rows
- Best: 2017, `+25.09%`
- Least positive: 2021, `+0.92%`
- Worst: 2022, `-15.88%`
- Least bad down year: 2018, `-13.58%`
- 2016-2025 cumulative / rounded-input CAGR: `104.57%` / `7.42%`; issuer benchmark cumulative / CAGR: `106.61%` / `7.53%`; SJPA trails by approximately `0.11 pp` CAGR.
- 2021-2025 cumulative / CAGR: `35.94%` / `6.33%`; issuer benchmark cumulative / CAGR: `36.53%` / `6.42%`; SJPA trails by approximately `0.09 pp` CAGR.
- S&P 500 TR 2016-2025 cumulative / CAGR: `298.33%` / `14.82%`; SJPA trails the common reference by approximately `7.40 pp` CAGR. In 2021-2025, S&P 500 is `96.17%` / `14.43%`, and the gap is approximately `8.09 pp` CAGR.
- Current date-to-date YTD: `19.87%` NAV as of `2026-08-26`
- Standardized month-end YTD: `16.99%` NAV and `17.02%` issuer benchmark as of `2026-07-31`; kept separate from the later date-to-date observation
- Index history note: issuer states the tracked index changed from MSCI Japan Index to MSCI Japan Investable Market Index (IMI) on `2014-05-30`.

## Risk read-through

SJPA ให้ broad Japan exposure ครอบคลุม large-, mid- และ small-cap companies;
issuerรายงาน `955` holdings ณ 2026-08-26. Current portfolio metrics คือ P/B
`1.88` และ P/E `18.73` ณ 2026-08-26; 3-year standard deviation `14.77%` และ
equity beta `0.993` ณ 2026-07-31. Sector exposure นำโดย Industrials `24.44%`,
Financials `17.55%`, Information Technology `16.95%`, Consumer Discretionary
`14.86%` และ Communication `5.82%` ณ 2026-08-26. กองทุนเป็น physical,
optimised, accumulating share class; ความเสี่ยงหลักคือ Japan country/sector,
small-cap liquidity, equity volatility และ FX sensitivity ของนักลงทุนที่ใช้
สกุลเงินอื่นนอก USD. Daily NAV history สำหรับคำนวณ max drawdown และ recovery:
`ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official iShares product/performance page: https://www.ishares.com/uk/professionals/en/products/251867/ishares-core-msci-japan-imi-ucits-etf?siteEntryPassthrough=true&switchLocale=y
- Official iShares SJPA factsheet: https://www.ishares.com/uk/individual/en/literature/fact-sheet/sjpa-ishares-core-msci-japan-imi-ucits-etf-fund-fact-sheet-en-gb.pdf
- Secondary OTC alias identity: https://stockanalysis.com/quote/otc/IHREF/ (used only to corroborate the input alias, not for performance numbers)
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-28]] | [[ETF Performance Index]]
