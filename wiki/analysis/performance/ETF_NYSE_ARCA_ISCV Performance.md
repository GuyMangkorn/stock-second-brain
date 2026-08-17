---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:ISCV
ticker: ISCV
exchange: NYSE Arca
fund: iShares Morningstar Small-Cap Value ETF
tracked_index: Morningstar US Small Cap Broad Value Extended Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-08-13
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/ISCV
  - geography/United-States
---

# ISCV Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

ISCV เป็น passive/index-tracking U.S. small-cap value equity ETF ที่ติดตาม Morningstar US Small Cap Broad Value Extended Index. Official issuer รายงาน rolling 10-year NAV Total Return average annual `9.22%` ณ 2026-06-30 และ current NAV YTD `20.34%` ณ 2026-08-13. Annual NAV rows ทางการครบ 2016-2025 ให้ rounded-input CAGR `8.43%` และ 2021-2025 CAGR `10.19%`.

## Performance check

- entity_key: NYSE Arca:ISCV
- Inception: 2004-06-28
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index (issuer benchmark): Morningstar US Small Cap Broad Value Extended Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: issuer-labeled 10-year average annual field as of 2026-06-30; raw endpoints and exact elapsed years are not disclosed in the reviewed capture
- 10-year NAV TR CAGR: `9.22%` (official issuer average annual total return; retained as a source fact, not recomputed from undisclosed endpoints)
- 2016-2025 NAV TR CAGR: `8.43%` from official rounded annual rows; cumulative return `124.65%`
- 2021-2025 NAV TR CAGR: `10.19%` from official rounded annual rows; cumulative return `62.41%`
- Coverage/source note: ISCV calendar rows are official iShares NAV Total Return observations displayed to one decimal; the 2021-2025 factsheet rows reconcile with the official product-page history. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed.

| Year | ISCV NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 27.80% | 11.96% |
| 2017 | 8.10% | 21.83% |
| 2018 | -16.80% | -4.38% |
| 2019 | 19.50% | 31.49% |
| 2020 | 0.70% | 18.40% |
| 2021 | 29.20% | 28.71% |
| 2022 | -10.50% | -18.11% |
| 2023 | 16.40% | 26.29% |
| 2024 | 9.20% | 25.02% |
| 2025 | 10.50% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2`
- Best: `2021 +29.20%`
- Least positive: `2020 +0.70%`
- Worst: `2018 -16.80%`
- Least bad down year: `2022 -10.50%`
- Current YTD: `20.34%` NAV TR as of 2026-08-13; latest NAV `US$81.86` and closing price `US$81.78` as of 2026-08-14; official premium/discount `-0.10%`

## Risk read-through

ISCV ให้ U.S. small-cap value exposure ผ่าน Morningstar US Small Cap Broad Value Extended Index. Expense ratio คือ `0.06%`; holdings `1,049` ณ 2026-08-14; 3-year standard deviation `17.95%` และ beta `1.01` ณ 2026-07-31. Current product page ยังรายงาน 30-day SEC yield `2.00%` ณ 2026-07-31 และ AUM `US$712.17M` ณ 2026-08-14.

Rolling 10-year issuer average annual `9.22%` ใช้ period ended 2026-06-30 ขณะที่ 2016-2025 calendar CAGR `8.43%` ใช้ annual rows ที่ปัดเศษและสิ้นสุด 2025-12-31 จึงไม่ใช่ตัวเลขเดียวกัน. Max drawdown และ recovery ยังเป็น `ไม่พบข้อมูลที่ยืนยันได้` เพราะ reviewed issuer capture ไม่ได้ให้ daily NAV history; market-price figures ด้านบนคงแยกจาก NAV Total Return.

## Driver notes

- Confirmed structure: passive objective to track the Morningstar US Small Cap Broad Value Extended Index; the index selects U.S. small-cap companies with value characteristics using metrics including forward earnings, book value, sales, cash flow and dividend yield.
- Current refresh: the official iShares product page provides NAV TR YTD through 2026-08-13, price/NAV and holdings through 2026-08-14, and risk fields through 2026-07-31.
- Annual observations are official iShares values displayed to one decimal; cumulative returns and CAGRs are rounded-input calculations. The common S&P 500 cache ends 2025-12-31, so no current-year S&P comparison is asserted.

## Sources

- [Official ISCV issuer product page](https://www.ishares.com/us/products/239588/ishares-morningstar-smallcap-value-etf) — identity, passive objective, exchange, benchmark, current NAV/YTD, price/NAV, holdings and risk fields; accessed 2026-08-17
- [Official ISCV calendar-performance page](https://www.ishares.com/ch/professionals/en/products/239588/ishares-morningstar-smallcap-value-etf?switchLocale=Y) — official 2016-2025 calendar NAV/benchmark rows and NAV return-basis context; accessed 2026-08-17
- [Official ISCV factsheet](https://www.ishares.com/us/literature/fact-sheet/iscv-ishares-morningstar-small-cap-value-etf-fund-fact-sheet-en-us.pdf) — 2021-2025 NAV rows, annualized performance, fees, benchmark and fund characteristics; as of 2026-06-30; accessed 2026-08-17
- [Official ISCV summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-morningstar-small-cap-value-etf-4-30.pdf) — passive investment objective, NYSE Arca listing, fees and risk context; dated 2025-08-29; accessed 2026-08-17
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as-of 2025-12-31
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
