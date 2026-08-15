---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IJS
ticker: IJS
exchange: NYSE Arca
fund: iShares S&P Small-Cap 600 Value ETF
tracked_index: S&P SmallCap 600 Value Index
benchmark: S&P 500 Total Return
updated: 2026-08-15
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-15.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IJS
  - geography/United-States
---

# IJS Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

IJS เป็น iShares S&P Small-Cap 600 Value ETF, passive/index-tracking U.S.
small-cap value equity ETF บน NYSE Arca ที่ติดตาม S&P SmallCap 600 Value Index.
Official 2016-2025 NAV Total Return cumulative อยู่ที่ 146.41% และ rounded-input
approximation CAGR 9.44%; official rolling 10-year NAV TR ณ 2026-06-30 อยู่ที่
173.99% cumulative / 10.60% annualized. Current official NAV TR YTD อยู่ที่
23.99% ณ 2026-08-13 เทียบกับ S&P 500 TR reference 14.54% ณ 2026-08-15;
dates ไม่ synchronized.

## Performance check

- entity_key: NYSE Arca:IJS
- Inception: 2000-07-24
- Expense ratio: 0.18%
- Metric: NAV Total Return รวม reinvested distributions และ fund expenses; USD
- Tracked index (issuer benchmark): S&P SmallCap 600 Value Index (SPTRSV)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- Rolling window: 2016-06-30 → 2026-06-30; 10.00 years; issuer-reported cumulative 173.99% / annualized 10.60%; normalized 100.00 → 273.99; raw endpoints are not disclosed
- Common calendar window: official 2016-2025 rows; rounded-input approximation cumulative 146.41% / CAGR 9.44%
- 2021-2025: rounded-input approximation cumulative 51.81% / CAGR 8.71%; S&P 500 cached 2021-2025 rounded-input approximation cumulative 96.17% / CAGR 14.43%
- Coverage: official complete NAV rows 2016-2025; IJS current NAV/YTD as of 2026-08-13/14; S&P current reference as of 2026-08-15 and not synchronized.

| Year | IJS NAV TR | S&P SmallCap 600 Value Index TR | Market-price TR | S&P 500 TR |
|---|---:|---:|---:|---:|
| 2016 | 31.17% | not disclosed | not disclosed | 11.96% |
| 2017 | 11.36% | not disclosed | not disclosed | 21.83% |
| 2018 | -12.80% | not disclosed | not disclosed | -4.38% |
| 2019 | 24.25% | not disclosed | not disclosed | 31.49% |
| 2020 | 2.56% | not disclosed | not disclosed | 18.40% |
| 2021 | 30.47% | 30.95% | 30.53% | 28.71% |
| 2022 | -11.32% | -11.04% | -11.33% | -18.11% |
| 2023 | 14.64% | 14.89% | 14.69% | 26.29% |
| 2024 | 7.42% | 7.56% | 7.35% | 25.02% |
| 2025 | 6.55% | 6.70% | 6.54% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ IJS;
annual rows ใช้ cached USD Total Return convention ณ 2025-12-31.
2026 YTD values มีคนละ as-of date และไม่ควรถูกใช้เป็น synchronized spread.

## Up years / Down years

- Up years / Down years: 8 / 2 in the complete 2016-2025 window
- Best: 2016, +31.17%
- Least positive: 2025, +6.55%
- Worst: 2018, -12.80%
- Least bad down year: 2022, -11.32%
- 2021-2025 rounded-input approximation: cumulative +51.81%; CAGR 8.71%
- Current IJS NAV TR YTD: +23.99% as of 2026-08-13
- S&P 500 TR reference: +14.54% as of 2026-08-15; current comparison is not synchronized

## Risk read-through

IJS มี small-cap value exposure จึงมี volatility, liquidity, value-cycle และ
market-risk sensitivity. Official issuer metrics ระบุ 3-year standard deviation
19.74% และ beta 1.07 ณ 2026-07-31; best quarter +32.92% ใน quarter ended
2020-12-31 และ worst quarter -37.36% ใน quarter ended 2020-03-31. ไม่มี official
daily NAV TR series สำหรับคำนวณ maximum drawdown/recovery date จึงระบุเป็น
not disclosed / unresolved.

## Distributions

| Ex-date | Payable date | Total distribution |
|---|---|---:|
| 2026-06-15 | 2026-06-18 | $0.539899 |
| 2026-03-17 | 2026-03-20 | $0.204616 |
| 2025-12-16 | 2025-12-19 | $0.544229 |
| 2025-09-16 | 2025-09-19 | $0.511064 |

รวมสี่รายการ $1.799808/share; all are income distributions with zero capital
gains and zero return of capital. Issuer trailing yield 1.32% ณ 2026-07-31;
price-based four-payment approximation 1.28% ณ price $140.68, with different
denominator/as-of convention.

## Sources

- [Official iShares IJS product page](https://www.ishares.com/us/products/239775/ishares-sp-smallcap-600-value-etf)
- [Official iShares IJS summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-s-and-p-small-cap-600-value-etf-3-31.pdf)
- [Official iShares IJS factsheet](https://www.ishares.com/us/literature/fact-sheet/ijs-ishares-s-p-small-cap-600-value-etf-fund-fact-sheet-en-us.pdf)
- [Official iShares IJS annual report](https://www.ishares.com/us/literature/annual-report/ar-ijs-en.pdf)
- [S&P SmallCap 600 Value Index](https://www.spglobal.com/spdji/en/indices/equity/sp-smallcap-600-value/)
- [S&P DJI current returns](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization)
- ETF source batch: [[ETF_performance_sources_2026-08-15]] | [[ETF Performance Index]]
