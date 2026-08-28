---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IEV
input_ticker: IEV
ticker: IEV
exchange: NYSE Arca
fund: iShares Europe ETF
tracked_index: S&P Europe 350 Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-29
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-27
fund_facts_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return; dividends reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IEV
  - geography/Europe
---

# IEV Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`IEV` คือ iShares Europe ETF ของ iShares/BlackRock, canonical listing
`NYSE Arca:IEV`. Official complete-calendar NAV rows ปี 2021-2025 compound ได้
`64.33%` หรือ rounded-input CAGR `10.44%`; ผลตอบแทนเป็นบวก/ลบ `4 / 1` ปี และ
current official NAV TR YTD คือ `+12.71%` ณ 26 ส.ค. 2026. Issuer rolling
10-year NAV TR คือ `9.87%` ณ 30 มิ.ย. 2026.

## Performance check

- `entity_key: NYSE Arca:IEV`; iShares ระบุ exchange `NYSE Arca`, CUSIP `464287861`, fund inception `25 ก.ค. 2000`, benchmark `S&P Europe 350 Index (Net)` และ asset class `Equity`.
- Classification: `passive-index-tracking`; กองทุนมุ่งติดตามดัชนีหุ้นยุโรป developed Europe และใช้ regional exposure เพื่อ diversification.
- Metric: `NAV Total Return` รวม dividends/capital gains ที่ reinvested และ fund expenses; คำนวณเป็น USD. Market-price return ถูกเก็บแยกจาก NAV TR.
- Common reference: `S&P 500 Total Return` (USD, dividends reinvested); issuer benchmark ยังคงเป็น `S&P Europe 350 Index (Net)` และไม่ควรใช้ S&P 500 เป็น strategy benchmark.
- Expense ratio: `0.60%`; official NAV `US$75.45` และ closing price `US$75.58` ณ 27 ส.ค. 2026; net assets `US$1.694B` ณ วันเดียวกัน.
- Current official NAV TR YTD: `+12.71%` ณ 26 ส.ค. 2026. Official 1Y/3Y/5Y/10Y annualised NAV TR คือ `18.26% / 16.07% / 9.64% / 9.87%` ณ 30 มิ.ย. 2026.
- Distribution check: frequency `Semi-Annual`; latest displayed income distributions คือ `US$1.280576` จ่าย 18 มิ.ย. 2026 และ `US$0.751330` จ่าย 19 ธ.ค. 2025, รวม `US$2.031906` ต่อหน่วยในสองงวดล่าสุด. 30-day SEC yield `1.94%` และ 12m trailing yield `2.72%` ณ 31 ก.ค. 2026 เป็นคนละ metric กับ NAV TR.
- Coverage/source note: iShares factsheet/product page ให้ complete official calendar rows ปี 2021-2025; rolling 10-year field เป็น issuer annualized NAV TR ณ 30 มิ.ย. 2026. S&P 500 rows เป็น cached USD total-return convention ปี 2021-2025 ณ 31 ธ.ค. 2025.

| Year | IEV NAV TR (USD) | S&P Europe 350 Index (Net) (USD) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|---:|
| 2021 | 16.34% | 16.62% | 28.71% |
| 2022 | -14.16% | -14.75% | -18.11% |
| 2023 | 19.82% | 20.20% | 26.29% |
| 2024 | 1.71% | 2.10% | 25.02% |
| 2025 | 35.02% | 35.78% | 17.88% |

Official IEV rows compound to `64.33%` / rounded-input CAGR `10.44%` for
2021-2025. The corresponding S&P Europe 350 rows compound to `65.67%` /
`10.62%`; the approximately `-0.18 pp` fund-minus-index difference is a
passive tracking observation, not alpha. Cached S&P 500 TR compounds to
`96.17%` / `14.43%` for the same period and remains a common reference only.

**Up years / Down years**

- Complete 2021-2025 NAV TR up/down: `4 / 1`
- Best NAV TR year: 2025, `+35.02%`
- Least positive year: 2024, `+1.71%`
- Worst NAV TR year: 2022, `-14.16%`
- Least bad down year: 2022, `-14.16%`
- Population standard deviation of the five complete annual NAV returns: `16.73%`
- Official 3-year standard deviation: `13.38%` as of 31 ก.ค. 2026
- Current YTD: `+12.71%` as of 26 ส.ค. 2026

## Risk read-through

Official 2021-2025 NAV TR CAGR is `10.44%`, while issuer rolling 10-year NAV TR
is `9.87%` as of 30 มิ.ย. 2026; the two windows are kept separate. The fund
held 360 positions ณ 27 ส.ค. 2026, with country exposure to the United Kingdom
`23.15%`, France `14.96%`, Switzerland `14.32%`, Germany `13.72%`, and the
Netherlands `8.36%`. Main risks are European country/sector concentration,
non-USD underlying currency movements, equity volatility, NAV/market-price
timing and index-tracking risk. Official daily NAV maximum drawdown and
recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [iShares IEV product page](https://www.ishares.com/us/products/239736/IEV) — official identity, NYSE Arca listing, current NAV/YTD, holdings, exposures, price/NAV, distributions and performance tables.
- [iShares IEV factsheet](https://www.ishares.com/us/literature/fact-sheet/iev-ishares-europe-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 calendar rows, rolling annualized fields, expense ratio, holdings and country/sector facts as of 30 มิ.ย. 2026.
- [iShares IEV prospectus](https://www.ishares.com/us/literature/prospectus/p-ishares-europe-etf-3-31.pdf) — official investment objective, fee and risk disclosures.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 31 ธ.ค. 2025.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
