---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IEUR
input_ticker: IEUR
ticker: IEUR
exchange: NYSE Arca
fund: iShares Core MSCI Europe ETF
tracked_index: MSCI Europe IMI Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-19
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-08-17
price_nav_as_of: 2026-08-17
fund_facts_as_of: 2026-08-17
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; dividends reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IEUR
  - geography/Europe
---

# IEUR Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`IEUR` คือ iShares Core MSCI Europe ETF ของ iShares/BlackRock, canonical
listing `NYSE Arca:IEUR`. Official complete-calendar NAV rows ปี 2021-2025
compound ได้ `60.39%` หรือ rounded-input CAGR `9.91%`; ผลตอบแทนเป็นบวก/ลบ
`4 / 1` ปี และ current official NAV TR YTD คือ `+12.03%` ณ 17 ส.ค. 2026.
Issuer rolling 10-year NAV TR คือ `10.02%` ณ 30 มิ.ย. 2026 ซึ่งแยกจาก
calendar-derived 2021-2025 CAGR.

## Performance check

- `entity_key: NYSE Arca:IEUR`; iShares ระบุ exchange `NYSE Arca`, CUSIP `46434V738`, fund inception `10 มิ.ย. 2014`, benchmark `MSCI Europe IMI Index (Net)` และ asset class `Equity`.
- Classification: `passive-index-tracking`; กองทุนมุ่งติดตามดัชนีหุ้น large-, mid- และ small-cap ใน developed Europe.
- Metric: `NAV Total Return` รวม dividends/capital gains ที่ reinvested และ fund expenses; คำนวณเป็น USD. Market-price return ถูกเก็บแยกจาก NAV TR.
- Common reference: `S&P 500 Total Return` (USD, dividends reinvested); issuer benchmark ยังคงเป็น `MSCI Europe IMI Index (Net)` และไม่ควรเรียก S&P 500 ว่า strategy benchmark.
- Expense ratio: `0.10%`; official NAV `US$77.83` และ closing price `US$78.05` ณ 17 ส.ค. 2026; net assets `US$9.402B` ณ วันเดียวกัน.
- Current official NAV TR YTD: `+12.03%` ณ 17 ส.ค. 2026. Official 1Y/3Y/5Y/10Y annualised NAV TR คือ `17.19% / 16.18% / 9.07% / 10.02%` ณ 30 มิ.ย. 2026.
- Distribution check: frequency `Semi-Annual`; latest displayed income distributions คือ `US$1.542483` จ่าย 18 มิ.ย. 2026 และ `US$0.849102` จ่าย 19 ธ.ค. 2025, รวม `US$2.391585` ต่อหน่วยในสองงวดล่าสุด. 30-day SEC yield `2.39%` และ 12m trailing yield `3.11%` ณ 31 ก.ค. 2026 เป็นคนละ metric กับ NAV TR.
- Coverage/source note: iShares factsheet ให้ complete official calendar rows ปี 2021-2025; 10-year value เป็น issuer rolling NAV TR field ไม่ใช่ CAGR ที่คำนวณจาก annual rows. S&P 500 rows เป็น cached USD total-return convention ปี 2021-2025 ณ 31 ธ.ค. 2025.

| Year | IEUR NAV TR (USD) | MSCI Europe IMI Index (Net) (USD) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|---:|
| 2021 | 16.21% | 16.13% | 28.71% |
| 2022 | -16.18% | -16.71% | -18.11% |
| 2023 | 19.83% | 19.52% | 26.29% |
| 2024 | 1.70% | 1.49% | 25.02% |
| 2025 | 35.11% | 35.08% | 17.88% |

Official IEUR rows compound to `60.39%` / rounded-input CAGR `9.91%` for
2021-2025. The corresponding MSCI index rows compound to `58.49%` / `9.65%`;
the approximately `+0.26 pp` fund-minus-index difference is a passive tracking
observation, not alpha. Cached S&P 500 TR compounds to `96.17%` / `14.43%` for
the same period; it is a common reference rather than the issuer benchmark.

**Up years / Down years**

- Complete 2021-2025 NAV TR up/down: `4 / 1`
- Best NAV TR year: 2025, `+35.11%`
- Least positive year: 2024, `+1.70%`
- Worst NAV TR year: 2022, `-16.18%`
- Least bad down year: 2022, `-16.18%`
- Population standard deviation of the five complete annual NAV returns: `17.38%`
- Official 3-year standard deviation: `13.67%` as of 31 ก.ค. 2026
- Current YTD: `+12.03%` as of 17 ส.ค. 2026

## Risk read-through

The issuer's rolling 10-year NAV TR is `10.02%` as of 30 มิ.ย. 2026, while the
available complete 2021-2025 annual rows produce `9.91%` CAGR. The fund held
1,009 positions ณ 17 ส.ค. 2026, with country exposure to the United Kingdom
`22.71%`, France `14.47%`, Switzerland `13.72%`, Germany `13.25%`, and the
Netherlands `8.76%`. Main risks are European country/sector/small-cap exposure,
non-USD underlying currency movements, equity volatility, NAV/market-price
timing and index-tracking risk. Official daily NAV maximum drawdown and
recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [iShares IEUR product page](https://www.ishares.com/us/products/264617/IEUR) — official identity, NYSE Arca listing, current NAV/YTD, holdings, exposures, price/NAV, distributions and performance tables.
- [iShares IEUR factsheet](https://www.ishares.com/us/literature/fact-sheet/ieur-ishares-core-msci-europe-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 calendar rows, rolling annualized fields, expense ratio, holdings, distributions and dated fund facts.
- [iShares IEUR summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-core-msci-europe-etf-7-31.pdf) — official investment objective, risks and fee disclosures.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 31 ธ.ค. 2025.
- [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
