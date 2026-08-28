---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:HEWJ
ticker: HEWJ
exchange: NYSE Arca
fund: iShares Currency Hedged MSCI Japan ETF
tracked_index: MSCI Japan 100% Hedged to USD Index (Net)
benchmark: S&P 500 Total Return
issuer: BlackRock / iShares
inception: 2014-01-31
expense_ratio: 1.02% gross; 0.49% net
updated: 2026-08-29
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-25
nav_as_of: 2026-08-26
market_price_as_of: 2026-08-26
fund_facts_as_of: 2026-08-26
risk_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/HEWJ
  - geography/Japan
---

# HEWJ Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

HEWJ เป็น passive/index-tracking equity ETF ของ iShares ที่ติดตาม MSCI Japan
100% Hedged to USD Index (Net) และจดทะเบียนบน NYSE Arca. Official rolling
10-year NAV Total Return ณ 2026-06-30 อยู่ที่ cumulative 391.99% และ CAGR
17.27%; latest current date-to-date NAV Total Return YTD อยู่ที่ 23.35% ณ
2026-08-25 และ current NAV อยู่ที่ USD 64.55 ณ 2026-08-26. ตัวเลขหลักเป็น
NAV Total Return ที่สะท้อนการ reinvest distributions และค่าใช้จ่ายของกองทุน
ตามข้อมูล performance ของ issuer.

## Performance check

- entity_key: NYSE Arca:HEWJ
- Inception: 2014-01-31; Asset Class: Equity
- Expense ratio: 1.02% gross; 0.49% net expense ratio (current prospectus;
  exact fee as-of date not disclosed)
- Metric: NAV Total Return รวม reinvested distributions และ fund expenses;
  issuer ระบุว่าผลตอบแทนบางช่วงสะท้อน fee waivers/reimbursements
- Tracked index (issuer benchmark): MSCI Japan 100% Hedged to USD Index (Net)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference
  benchmark)
- Current NAV: US$64.55 ณ 2026-08-26; closing market price US$64.63,
  premium/discount 0.13%, and 30-day median bid/ask spread 0.16% as of
  2026-08-25 or 2026-08-26 according to the respective issuer fields.
- Fund facts: net assets US$745.52M and 11.55M shares outstanding as of
  2026-08-26; current 30-day SEC yield 3.80% and trailing 12-month yield
  3.72% as of 2026-07-31.
- 10-year coverage: official rolling performance from 2016-06-30 to
  2026-06-30; actual years 10.00
- Start TR value: 100.00 normalized; End TR value: 491.99 normalized,
  derived from official cumulative return 391.99%; raw NAV endpoints are not
  disclosed
- 10-year NAV TR CAGR: 17.27% issuer-reported average annual NAV Total Return
- Formula: (End TR / Start TR)^(1 / Years) - 1 = (491.99 / 100.00)^(1 / 10.00) - 1 = approximately 17.27%
- Latest date-to-date NAV TR YTD: 23.35% as of 2026-08-25. This is kept
  separate from the standardized month-end table below.
- Coverage/source note: official page provides rolling 10-year
  cumulative/average annual returns as of 2026-06-30 and calendar rows
  2021-2025. The normalized endpoint is derived from the rounded official
  cumulative metric, not a proxy or market-price return.

| Year | HEWJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 12.79% | 28.71% |
| 2022 | -3.91% | -18.11% |
| 2023 | 36.20% | 26.29% |
| 2024 | 24.87% | 25.02% |
| 2025 | 30.08% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ HEWJ;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31. ช่วง annual
comparison ที่เปิดเผยตรงกันคือ 2021-2025.

## Up years / Down years

- Up years / Down years: 4 / 1 ใน complete rows ที่ issuer เปิดเผย
- Best: 2023, +36.20%
- Least positive: 2021, +12.79%
- Worst: 2022, -3.91%
- Least bad down year: 2022, -3.91%
- 2021-2025 cumulative / CAGR: 139.77% / 19.11%; S&P 500 TR: 96.17% / 14.43%
- Current date-to-date YTD: 23.35% NAV as of 2026-08-25
- Standardized month-end YTD: 22.41% NAV as of 2026-06-30; kept separate from the later date-to-date observation

## Risk read-through

HEWJ ให้ exposure ต่อ Japanese large- and mid-cap equities พร้อม currency
forwards เพื่อ hedge JPY/USD; hedge overlay นี้ไม่ใช่การจัดประเภท
derivative-heavy ใน ETF v1. Official 3-year standard deviation อยู่ที่ 11.98%
และ equity beta 0.43 ณ 2026-07-31; P/B 2.04 และ P/E 19.16 ณ 2026-08-25.
Sector weights ล่าสุด ณ 2026-08-25 คือ Industrials 24.63%, Financials
18.66%, Information Technology 17.84% และ Consumer Discretionary 15.30%.
ความเสี่ยงหลักคือ Japan country/sector concentration, hedge cost และ
tracking/basis risk. Daily NAV history สำหรับคำนวณ max drawdown และ
recovery: ไม่พบข้อมูลที่ยืนยันได้.

## Sources

- [Official iShares HEWJ product and performance page](https://www.ishares.com/us/products/259624/ishares-currency-hedged-msci-japan-etf) — identity, NYSE Arca listing, benchmark, current NAV/price, fund facts, sector snapshot, standardized returns and calendar rows; accessed 2026-08-29.
- [Official iShares HEWJ factsheet](https://www.ishares.com/us/literature/fact-sheet/hewj-ishares-currency-hedged-msci-japan-etf-fund-fact-sheet-en-us.pdf) — fund objective, fee framework and performance definition.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition.
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as of 2025-12-31.
- ETF source batch: [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
