---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLSW
input_ticker: FLSW
ticker: FLSW
exchange: NYSE Arca
fund: Franklin FTSE Switzerland ETF
tracked_index: FTSE Switzerland Capped Index-NR
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-19
performance_as_of: 2025-12-31
rolling_5y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-07
price_nav_as_of: 2026-08-07
fund_facts_as_of: 2026-08-06
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; dividends and capital gains distributions reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FLSW
  - geography/Switzerland
---

# FLSW Performance

> Navigation: [[ETF Region Index]] → [[Switzerland ETF]] → [[ETF Performance Index]]

## Bottom line

`FLSW` คือ Franklin FTSE Switzerland ETF ที่จดทะเบียนบน NYSE Arca และเป็น
`passive-index` single-country equity ETF สำหรับหุ้น Swiss large- และ mid-cap
โดยติดตาม `FTSE Switzerland Capped Index`. กองทุนเริ่มเมื่อ 6 ก.พ. 2018 จึงยัง
ไม่มี 10-year window ที่ครบถ้วน. Official complete-calendar NAV rows ปี
2019-2025 compound ได้ `128.13%` หรือ rounded-input CAGR `12.50%`; ช่วงร่วม
2021-2025 ได้ `50.65%` หรือ `8.54%` ต่อปี. Latest official NAV TR YTD คือ
`+8.87%` ณ 7 ส.ค. 2026 ขณะที่ S&P 500 TR แบบ secondary อยู่ที่ `+13.38%`
ในวันเดียวกัน.

## Performance check

- `entity_key: NYSE Arca:FLSW`; Franklin ยืนยัน fund name, ticker, NYSE Arca listing และ inception `02/06/2018`.
- Classification: `passive-index`. Franklin อธิบายว่า FLSW มุ่งให้ผลตอบแทนสอดคล้องกับ FTSE Switzerland RIC Capped Index ซึ่งเป็น market-cap-weighted large-/mid-cap Swiss index.
- Metric: `NAV Total Return` รวม distributions ที่ reinvested และหัก fund expenses; return currency คือ USD. Market-price return แยกออกจาก NAV.
- Tracked index: `FTSE Switzerland Capped Index-NR`; ดัชนีมี security caps เพื่อลดการกระจุกตัวในหุ้นรายตัว. Index reconstitution เป็น semi-annual.
- Inception: `6 ก.พ. 2018`; expense ratio `0.09%` (gross/net as of 1 ส.ค. 2026); distribution frequency semi-annual.
- Latest official rolling NAV TR ณ 30 มิ.ย. 2026: `1Y 18.06%`, `3Y 13.53%`, `5Y 7.87%`, since inception `10.12%`; 10-year field ยังไม่ applicable.
- Official snapshot: NAV `$44.38` ณ 7 ส.ค. 2026; total net assets `$84.32M` ณ 9 ส.ค. 2026; 50 holdings, P/E `26.69x`, P/B `4.50x` ณ 6 ส.ค. 2026.

| Year | FLSW NAV TR (USD) | FTSE Switzerland Capped Index-NR (USD) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2019 | 32.66% | 32.19% | 31.49% |
| 2020 | 14.15% | 13.30% | 18.40% |
| 2021 | 20.40% | 19.98% | 28.71% |
| 2022 | -18.30% | -18.50% | -18.11% |
| 2023 | 16.71% | 16.27% | 26.29% |
| 2024 | -1.41% | -1.83% | 25.02% |
| 2025 | 33.10% | 32.80% | 17.88% |

Coverage/source note: Franklin's factsheet supplies official 2019-2025 calendar
NAV, market-price and index rows. The 2018 inception year is partial and omitted
from ranking. S&P 500 rows use the cached USD total-return convention, dividends
reinvested, as of 31 ธ.ค. 2025; the current YTD cross-check is a secondary
dividend-reinvested series as of 7 ส.ค. 2026.

Official FLSW 2019-2025 rows compound to `128.13%` / rounded-input CAGR `12.50%`;
the 2021-2025 subset compounds to `50.65%` / `8.54%`. The tracked-index rows
compound to `121.99%` / `12.07%` for 2019-2025 and `48.22%` / `8.19%` for
2021-2025. These fund-minus-index differences are passive tracking observations,
not alpha. Cached S&P 500 TR compounds to `205.41%` / `17.29%` for 2019-2025 and
`96.17%` / `14.43%` for 2021-2025.

**Up years / Down years**

- Complete 2019-2025 NAV TR up/down: `5 / 2`
- Best NAV TR year: 2025, `+33.10%`
- Least positive year: 2020, `+14.15%`
- Worst NAV TR year: 2022, `-18.30%`
- Least bad down year: 2024, `-1.41%`
- Population standard deviation of the seven complete annual NAV returns: `17.08%`; Franklin's separate 3-year NAV standard deviation is `15.88%` as of 31 มี.ค. 2026.
- Current YTD: `+8.87%` as of 7 ส.ค. 2026; secondary S&P 500 TR reference: `+13.38%` as of 7 ส.ค. 2026.

## Risk read-through

FLSW มี annual-return CAGR `12.50%` ใน complete 2019-2025 window แต่ยังไม่มี
10-year NAV TR history. Franklin's rolling 5-year NAV TR อยู่ที่ `7.87%` ณ
30 มิ.ย. 2026 และ 3-year NAV standard deviation `15.88%` ณ 31 มี.ค. 2026.
ความเสี่ยงหลักคือ single-country exposure, CHF/USD FX, Swiss market valuation
และ sector concentration: Health Care `38.85%`, Financials `18.10%`, Industrials
`13.67%`, Consumer Staples `13.42%`, Materials `8.52%` ณ 6 ส.ค. 2026. Expense
ratio `0.09%` ช่วยลด drag แต่ official daily NAV maximum drawdown และ recovery
date ยัง `ไม่พบข้อมูลที่ยืนยันได้`; จึงรายงาน `risk-adjusted evidence:
not-verified`.

## Sources

- [Franklin FLSW product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26352/SINGLCLASS/franklin-ftse-switzerland-etf/FLSW) — official identity, exchange, benchmark, inception, fee, rolling NAV returns, current NAV/YTD, assets, holdings, sectors and portfolio statistics.
- [Franklin FLSW factsheet](https://www.franklintempleton.com/forms-literature/download/FLSW-FF) — official 2019-2025 calendar NAV/index rows, return definitions, expense ratio and 3-year NAV risk statistics as of 31 มี.ค. 2026.
- [Franklin FLSW summary prospectus](https://www.franklintempleton.com/forms-literature/download-preview/FLSW-PSUM) — official fund objective, annual-return disclosure and passive/index context.
- [Slickcharts S&P 500 YTD](https://www.slickcharts.com/sp500/returns/ytd) — secondary current S&P 500 total-return YTD cross-check as of 7 ส.ค. 2026.
- S&P 500 Total Return 2019-2025 cached convention from the workflow; USD dividends reinvested, reference as of 31 ธ.ค. 2025.
- [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
