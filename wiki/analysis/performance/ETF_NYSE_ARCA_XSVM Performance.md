---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:XSVM
ticker: XSVM
exchange: NYSE Arca
fund: Invesco S&P SmallCap Value with Momentum ETF
tracked_index: S&P SmallCap 600 High Momentum Value Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-08-05
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/XSVM
  - geography/United-States
---

# XSVM Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

XSVM เป็น passive/index-tracking U.S. small-cap value-and-momentum ETF ที่
ติดตาม S&P SmallCap 600 High Momentum Value Index. Official Invesco NAV Total
Return ช่วง 2016-2025 ให้ cumulative `200.51%` และ rounded-input CAGR `11.63%`;
ใน common 2021-2025 windowให้ CAGR `12.30%` ต่ำกว่า S&P 500 Total Return `14.43%`.
Latest NAV TR YTD ที่พบเป็น secondary Schwab observation `23.00%*` ณ
2026-06-30; official Invesco Q1-2026 snapshot รายงาน NAV YTD `4.49%` ณ
2026-03-31 จึงไม่ผสมสอง as-of dates.

## Performance check

- entity_key: `NYSE Arca:XSVM`
- Inception: 2005-03-03
- Expense ratio: 0.37% total/net; management fee 0.29% (official Invesco product page)
- Metric: `NAV Total Return` รวม distributions ตาม issuer convention และ fund expenses; USD
- Tracked index (issuer benchmark): S&P SmallCap 600 High Momentum Value Index (`SPSVMOUT`)
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year window: 2016-01-01 to 2025-12-31 (ten complete calendar years)
- 10-year NAV TR CAGR: `11.63%` rounded-input approximation; normalized start TR value `100.00`, end TR value `300.51`, years `10.00`
- Common calendar window: 2016-2025 cumulative `200.51%`; 2021-2025 cumulative `78.58%` / CAGR `12.30%`; S&P 500 cached 2021-2025 cumulative `96.17%` / CAGR `14.43%`
- Latest secondary NAV TR YTD: `23.00%*` as of 2026-06-30; secondary market-price YTD is `22.90%*` on the same Schwab page
- Official issuer cross-check: NAV YTD `4.49%` as of 2026-03-31; this earlier official snapshot is retained separately

| Year | XSVM NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 35.52% | 11.96% |
| 2017 | 3.17% | 21.83% |
| 2018 | -11.82% | -4.38% |
| 2019 | 29.95% | 31.49% |
| 2020 | 5.03% | 18.40% |
| 2021 | 56.38% | 28.71% |
| 2022 | -13.55% | -18.11% |
| 2023 | 20.23% | 26.29% |
| 2024 | 2.12% | 25.02% |
| 2025 | 7.59% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ XSVM;
annual rows ใช้ cached USD Total Return convention ณ 2025-12-31. Invesco
เปิดเผย historical underlying-index changes (Dynamic Small Cap Value Intellidex,
RAFI Fundamental Small Value, Russell 2000 Pure Value และ S&P 600 High Momentum
Value ตามช่วงเวลา) จึงไม่ควรอ่าน index-relative history เป็น series เดียวแบบไร้
รอยต่อ. Cumulative returns และ CAGRs เป็น rounded-input calculations จาก official
fund NAV rows.

## Up years / Down years

- Up years / Down years: 8 / 2 in the complete 2016-2025 window
- Best: 2021, +56.38%
- Least positive: 2024, +2.12%
- Worst: 2022, -13.55%
- Least bad down year: 2018, -11.82%
- Latest secondary XSVM NAV TR YTD: +23.00% as of 2026-06-30
- Current price: US$71.88 as of 2026-08-05 (secondary quote; not used in NAV return calculations)

## Risk read-through

XSVM มี annual-return volatility แบบ population standard deviation `20.87%`
จาก official 2016-2025 rows. Value และ momentum tilts เพิ่ม factor-regime,
turnover, valuation และ reversal risk เหนือ broad small-cap beta; portfolio
มีประมาณ 120 หุ้นและ Invesco ระบุว่า rebalanced/reconstituted semi-annually.
Official daily NAV history สำหรับคำนวณ max drawdown และ recovery ยังไม่พบข้อมูล
ที่ยืนยันได้ จึงไม่สร้างตัวเลข proxy เพิ่ม.

## Sources

- [Official Invesco XSVM product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-sp-smallcap-value-with-momentum-etf.html)
- [Official Invesco Q1 2026 performance material](https://www.invesco.com/us-rest/contentdetail?contentId=118407c649400410VgnVCM10000046f1bf0aRCRD&dnsName=us)
- [Official S&P SmallCap 600 High Momentum Value Index page](https://www.spglobal.com/spdji/en/indices/dividends-factors/sp-smallcap-600-high-momentum-value-index/)
- [Secondary Schwab XSVM performance page](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=xsvm)
- [S&P 500 index definition and cached historical reference](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
