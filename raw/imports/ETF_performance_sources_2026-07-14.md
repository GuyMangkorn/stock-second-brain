---
type: source-note
source_profile: etf-performance-delta
accessed: 2026-07-14
canonical_outputs:
  - wiki/analysis/performance/ETF_NASDAQ_OPPJ Performance.md
  - wiki/analysis/performance/ETF Performance Index.md
tags:
  - source/etf
  - source/performance
  - source/benchmark
---

# ETF Performance Source Batch - 2026-07-14

## OPPJ Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NASDAQ:OPPJ` | [WisdomTree product page](https://www.wisdomtree.com/us/products/equity/oppj), [factsheet](https://www.wisdomtree.com/us/media/wisdomtree-factsheet-oppj) | Fund identity, NAV return definition, expense ratio, current YTD, rolling returns, NAV/price, hedge ratio, distributions | Performance 2026-06-30; expense/NAV/hedge 2026-07-13; market price 2026-07-10 |
| `NASDAQ:OPPJ` | [SEC 2025 summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011309/oppj73125497k.htm), [annual-return chart](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011309/oppj_chart.jpg) | Exchange, passive classification, strategy change, 2015-2024 annual NAV Total Return, return basis | Prospectus 2025-08-01; annual returns through 2024-12-31 |
| OPPJ index | [WisdomTree index page](https://www.wisdomtree.com/us/indexes/WTJOP), [methodology](https://www.wisdomtree.com/us/media/core-equity-index-methodology) | Issuer benchmark and dynamic JPY/USD hedge methodology | accessed 2026-07-14 |
| `NASDAQ:OPPJ` 2025 | [Schwab standardized ETF report](https://www.schwab.wallst.com/schwab/Prospect/research/etfs/reports/reportRetrieve.asp?reportType=etfrc&symbol=OPPJ) | Secondary 2025 NAV total return, rounded; marked `*` | 2025-12-31 |
| `NASDAQ:OPPJ` risk | [PortfoliosLab](https://portfolioslab.com/symbol/OPPJ) | Secondary dividend-adjusted max drawdown and recovery | accessed 2026-07-14 |
| `S&P 500 TR cache` | [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) | Reusable complete-year S&P 500 Total Return common-reference rows | 2016-2025; reference as-of 2025-12-31 |

## Classification And Continuity

- OPPJ เป็น U.S.-domiciled passive, index-tracking Japan equity ETF; listing
  exchange คือ NASDAQ และ reporting/trading currency คือ USD.
- Fund inception คือ `2013-06-28`, แต่ current strategy/ticker เริ่ม
  `2025-07-01`. ก่อนหน้านั้นเป็น WisdomTree Japan Hedged SmallCap Equity Fund
  (`DXJS`); objective/index เปลี่ยน effective `2025-06-30`.
- Current issuer benchmark คือ WisdomTree Japan Opportunities Index. Index ใช้
  dynamic JPY/USD hedge 0-100%; latest fund aggregate hedge ratio `0.02%` ณ
  2026-07-13.
- Expense ratio: management `0.58%`, other expenses `0.00%`, total/net `0.58%`.
- Product page แสดง NAV USD `56.571` ณ 2026-07-13 และ closing market price USD
  `58.180` ณ 2026-07-10. Dates ไม่ตรงกัน จึงไม่คำนวณ premium/discount จากคู่นี้.

## Extracted Facts

Return basis ของ annual rows คือ pre-tax `NAV Total Return` รวม reinvested
distributions และหัก fund expenses. 2025* เป็น secondary standardized NAV total
return; S&P 500 TR เป็น common reference ไม่ใช่ issuer benchmark.

| Year | OPPJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 6.88% | 11.96% |
| 2017 | 29.46% | 21.83% |
| 2018 | -17.82% | -4.38% |
| 2019 | 18.33% | 31.49% |
| 2020 | -4.64% | 18.40% |
| 2021 | 11.98% | 28.71% |
| 2022 | 6.84% | -18.11% |
| 2023 | 36.69% | 26.29% |
| 2024 | 20.68% | 25.02% |
| 2025* | 36.20% | 17.88% |

- Official 2026 YTD NAV Total Return: `24.67%` ณ 2026-06-30.
- Official 1-/3-/5-/10-year NAV average annual returns: `58.06%`, `32.86%`,
  `24.84%`, `17.89%` ณ 2026-06-30.
- Official since-inception cumulative/CAGR: `541.90%` / `15.37%` ณ 2026-06-30.
- Latest four official distributions: USD `0.34000` (2026-06-25), `0.05500`
  (2026-03-26), `0.23981` (2025-12-26), `0.01000` (2025-09-25). Distribution
  analysis was not requested.

## Calculations

- 2016-2025 cumulative/CAGR: `244.89%` / `13.18%`; includes secondary 2025*.
- S&P 500 TR 2016-2025 cumulative/CAGR: `298.33%` / `14.82%` from cached annual
  rows. OPPJ gap is `-53.44 percentage points` cumulative and `-1.64 percentage
  points` annualized.
- OPPJ 2021-2025 cumulative/CAGR: `168.80%` / `21.87%*`; S&P 500 TR:
  `96.17%` / `14.43%`. This OPPJ window spans the mid-2025 strategy change.
- Issuer-reported rolling 10-year NAV TR CAGR `17.89%` implies a normalized
  `100.00 -> 518.52` over 10.00 years via `100 x (1 + 17.89%)^10`. This is a
  shown calculation, not disclosed issuer TR endpoints.
- Secondary adjusted-price max drawdown: `-39.30%`; peak 2018-01-09, trough
  2020-03-16, recovery 2021-03-15. This is not official NAV history.

## Source Conflicts And Gaps

- Official index symbols conflict: product page `WTJOPN`; index page `WTJOP` /
  `JOPN`; methodology `JPOP`; 2026 factsheet still shows predecessor symbol
  `WTJSEH`. ใช้ full index name เป็น canonical label และเก็บ conflict นี้ไว้.
- Official raw daily/monthly NAV total-return index levels and 10-year endpoints
  are `ไม่พบข้อมูลที่ยืนยันได้`; official max drawdown/recovery จึงคำนวณไม่ได้.
- No current issuer table with 2025 calendar-year NAV return was captured. The
  `36.20%*` row comes from a secondary standardized report and is not silently
  treated as an issuer row.
- Pre-2025-06-30 performance belongs to the predecessor objective. The 2025
  calendar year itself mixes about six months of each strategy.

## Handoff For Performance Page

Create `[[ETF_NASDAQ_OPPJ Performance]]`, add OPPJ to `[[ETF Performance Index]]`,
and retain the strategy-break warning beside all long-history interpretations.
Do not route this ETF through company financial ingest or DCF.
