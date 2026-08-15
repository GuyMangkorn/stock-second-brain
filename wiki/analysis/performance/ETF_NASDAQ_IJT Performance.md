---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:IJT
ticker: IJT
exchange: NASDAQ
fund: iShares S&P Small-Cap 600 Growth ETF
tracked_index: S&P SmallCap 600 Growth Index
benchmark: S&P 500 Total Return
updated: 2026-08-15
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-15.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IJT
  - geography/United-States
---

# IJT Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

IJT เป็น iShares S&P Small-Cap 600 Growth ETF, passive/index-tracking U.S.
small-cap growth equity ETF บน NASDAQ ที่ติดตาม S&P SmallCap 600 Growth Index.
Official 2016-2025 NAV Total Return cumulative อยู่ที่ 150.04% และ rounded-input
CAGR 9.60%; official rolling 10-year NAV TR ณ 2026-06-30 อยู่ที่ 205.63%
cumulative / 11.82% annualized. Current official NAV TR YTD อยู่ที่ 26.03% ณ
2026-08-13 เทียบกับ secondary S&P 500 TR YTD 14.54% ณ 2026-08-14.

## Performance check

- entity_key: NASDAQ:IJT
- Inception: 2000-07-24
- Expense ratio: 0.18%
- Metric: NAV Total Return รวม reinvested dividends/capital-gain distributions และ fund expenses; USD
- Tracked index (issuer benchmark): S&P SmallCap 600 Growth Index (SPTRSG)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR: issuer-reported cumulative 205.63% / annualized 11.82% as of 2026-06-30; raw unrounded endpoints are not disclosed
- Common calendar window: official 2016-2025 cumulative 150.04% / rounded-input CAGR 9.60%
- 2021-2025 cumulative 29.80% / CAGR 5.35%; S&P 500 cached 2021-2025 cumulative 96.17% / CAGR 14.43%
- Coverage/source note: verified official complete rows cover 2013-2025; 2016-2025 is the common comparison window. Current IJT NAV/YTD is as of 2026-08-13; current S&P fallback is secondary as of 2026-08-14.

| Year | IJT NAV TR | S&P SmallCap 600 Growth Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 22.00% | not disclosed | 11.96% |
| 2017 | 14.57% | not disclosed | 21.83% |
| 2018 | -4.28% | not disclosed | -4.38% |
| 2019 | 20.82% | not disclosed | 31.49% |
| 2020 | 19.17% | not disclosed | 18.40% |
| 2021 | 22.40% | 22.62% | 28.71% |
| 2022 | -21.24% | -21.08% | -18.11% |
| 2023 | 16.97% | 17.10% | 26.29% |
| 2024 | 9.42% | 9.63% | 25.02% |
| 2025 | 5.20% | 5.37% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ IJT;
annual rows ใช้ cached USD Total Return convention ณ 2025-12-31. Benchmark rows
2016-2020 ไม่ได้ถูกเติมเมื่อ official packet ไม่เปิดเผย.

Historical SEC material references NYSE Arca, while current issuer, index-provider
and recent SEC material identify NASDAQ. This page uses current NASDAQ:IJT as the
canonical display key and preserves the discrepancy as a source gap.

## Up years / Down years

- Up years / Down years: 8 / 2 in the complete 2016-2025 window
- Best: 2021, +22.40%
- Least positive: 2025, +5.20%
- Worst: 2022, -21.24%
- Least bad down year: 2018, -4.28%
- Current IJT NAV TR YTD: +26.03% as of 2026-08-13
- S&P 500 TR YTD: +14.54% as of 2026-08-14, secondary fallback; exact official current TR was not extractable

## Risk read-through

IJT มี small-cap growth exposure จึงมี volatility, liquidity และ growth-style risk.
Official issuer metrics ระบุ 3-year standard deviation 19.48% และ beta 1.09 ณ
2026-07-31; worst quarter คือ -28.21% ใน quarter ended 2020-03-31 และ best
quarter +29.74% ใน quarter ended 2020-12-31. Secondary price-based analysis
รายงาน maximum decline ประมาณ 32.7% แต่ methodology และ exact NAV high-water
mark ไม่ยืนยันได้ จึงไม่ใช้เป็น official NAV drawdown/recovery.

## Sources

- [Official iShares IJT product page](https://www.ishares.com/us/products/239773/ishares-sp-smallcap-600-growth-etf)
- [Official iShares IJT factsheet](https://www.ishares.com/us/literature/fact-sheet/ijt-ishares-s-p-small-cap-600-growth-etf-fund-fact-sheet-en-us.pdf)
- [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1100663/000119312525171574/d921702d497k.htm)
- [SEC performance table](https://www.sec.gov/Archives/edgar/data/1100663/000119312523190469/R67.htm)
- [S&P SmallCap 600 Growth Index](https://www.spglobal.com/spdji/en/indices/equity/sp-smallcap-600-growth/)
- [Slickcharts S&P 500 returns](https://www.slickcharts.com/sp500/returns) (secondary current-YTD fallback)
- [KoalaGains IJT risk analysis](https://koalagains.com/etfs/NASDAQ/IJT/risk-analysis) (secondary price-based risk context only)
- ETF source batch: [[ETF_performance_sources_2026-08-15]] | [[ETF Performance Index]]
