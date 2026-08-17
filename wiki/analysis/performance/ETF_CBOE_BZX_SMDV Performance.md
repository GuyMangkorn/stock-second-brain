---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:SMDV
ticker: SMDV
exchange: Cboe BZX
fund: ProShares Russell 2000 Dividend Growers ETF
tracked_index: Russell 2000 Dividend Growth Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SMDV
  - geography/United-States
---

# SMDV Performance
> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

SMDV เป็น passive/index-tracking U.S. small-cap dividend-growth ETF ที่ติดตาม
Russell 2000 Dividend Growth Index. Official NAV Total Return ช่วง complete
calendar window 2016-2025 ให้ cumulative 106.36% และ rounded-input CAGR 7.51%;
common 2021-2025 CAGR อยู่ที่ 10.66% เทียบกับ S&P 500 Total Return 14.43%.
Current NAV TR YTD อยู่ที่ 18.13% ณ 2026-07-31. ProShares ประกาศล่วงหน้าว่า
ประมาณ 2026-09-28 กองจะเปลี่ยนชื่อเป็น ProShares S&P SmallCap 600 Dividend
Aristocrats ETF และเปลี่ยน underlying index; ผลตอบแทนก่อน effective date นี้
ยังเป็นของ Russell 2000 Dividend Growth Index.

## Performance check

- entity_key: Cboe BZX:SMDV
- Inception: 2015-02-03
- Expense ratio: 0.40% ณ 2026-07-31
- Metric: NAV Total Return รวม distributions ที่ reinvested และ fund expenses ตาม issuer convention; USD
- Tracked index (issuer benchmark): Russell 2000 Dividend Growth Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- Management mode: passive-index
- Active process: not applicable
- 10-year window: 2016-01-01 to 2025-12-31; ten complete calendar years because the fund launched in February 2015
- 10-year NAV TR CAGR: 7.51% rounded-input approximation; normalized start TR value 100.00 and end TR value 206.36
- Common 2021-2025 window: cumulative 65.98%; rounded-input CAGR 10.66%; S&P 500 TR CAGR 14.43%
- Issuer rolling 10-year NAV TR: 7.41% as of 2026-07-31; this is a separate rolling metric from the rounded calendar-row CAGR
- Current NAV TR YTD: 18.13% as of 2026-07-31; 1-year 22.23%, 3-year annualized 10.42%, 5-year annualized 7.01%, and since-inception annualized 8.29% on the same issuer page
- Current NAV / market price: US$78.71 / US$78.76 as of 2026-08-14
- Distribution fields: quarterly frequency; 30-day SEC yield 2.56% as of 2026-06-30 and 12-month yield 2.28% as of 2026-07-31
- Coverage/source note: official ProShares summary prospectus supplies 2016-2024 annual NAV rows; the official ProShares attribution report supplies the 2025 calendar NAV total return of 0.34%. No secondary annual return is used.

| Year | SMDV NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.03% | 11.96% |
| 2017 | 8.89% | 21.83% |
| 2018 | -5.79% | -4.38% |
| 2019 | 19.11% | 31.49% |
| 2020 | -4.93% | 18.40% |
| 2021 | 17.37% | 28.71% |
| 2022 | -0.71% | -18.11% |
| 2023 | 4.70% | 26.29% |
| 2024 | 35.57% | 25.02% |
| 2025 | 0.34% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ SMDV;
annual rows ใช้ cached USD Total Return convention ณ 2025-12-31. Cumulative
returns และ CAGRs เป็น rounded-input calculations จาก annual observations.

## Up years / Down years

- Up years / Down years: 7 / 3 in the complete 2016-2025 window
- Best: 2024, +35.57%
- Least positive: 2025, +0.34%
- Worst: 2018, -5.79%
- Least bad down year: 2022, -0.71%
- Current SMDV NAV TR YTD: +18.13% as of 2026-07-31

## Risk read-through

Annual-return volatility แบบ population standard deviation อยู่ที่ 12.15% จาก
complete 2016-2025 rows. The fund has small-cap, dividend-screen, equal-weight,
sector-concentration, reconstitution, liquidity and tracking-error risks.
Official daily NAV history sufficient for maximum drawdown and recovery ยังไม่พบ
ข้อมูลที่ยืนยันได้; ProShares NAV History link returned an unsupported CSV
content type during source access, so no numeric drawdown proxy is saved.

## Tracking / implementation read-through

- ProShares annual shareholder report for the fiscal year ended 2026-05-31 reports fund total return 15.71% versus Russell 2000 Dividend Growth Index 16.17%; five-year annualized returns were 4.31% versus 4.71%, and ten-year annualized returns were 7.39% versus 7.84%.
- ProShares attribution report as of 2025-12-31 reports calendar-year 2025 NAV total return 0.34% versus index 0.72%; three-year annualized 5.36% versus 5.75%, five-year annualized 5.59% versus 5.99%, and ten-year annualized 7.51% versus 7.97%.
- The observed gap is consistent with ordinary fund expenses and implementation drag; it is not described as alpha or discretionary manager skill.
- The index selects U.S. small-cap companies with at least ten consecutive years of dividend growth, holds at least 40 companies, caps any sector at 30%, and uses equal weighting with quarterly resets under the current Russell methodology.

## Scheduled index transition

As of the 2026-07-13 ProShares supplement, the Board approved a change expected
around 2026-09-28: the fund name is scheduled to become ProShares S&P SmallCap
600 Dividend Aristocrats ETF and the underlying index is scheduled to change to
the S&P SmallCap 600 Dividend Aristocrats Index. This is future-dated as of the
2026-08-17 review; current identity, current performance rows and current
benchmark metadata remain Russell 2000 Dividend Growth Index.

## Sources

- [ProShares SMDV product page](https://www.proshares.com/our-etfs/strategic/smdv) — official identity, current index, exchange, rolling performance, NAV/market price, expense, yield and future index/name notice; reviewed 2026-08-17.
- [SMDV Fact Sheet](https://www.proshares.com/globalassets/proshares/fact-sheet/prosharesfactsheetsmdv.pdf) — official fund facts and rolling NAV/market-price/index returns as of 2026-06-30.
- [SMDV Summary Prospectus](https://www.proshares.com/globalassets/proshares/prospectuses/smdv_summary_prospectus.pdf) — official passive objective, index methodology, risks, inception and 2016-2024 annual return chart.
- [SMDV Attribution Report](https://www.proshares.com/globalassets/proshares/attribution-reports/smdv_review.pdf) — official 2025 calendar NAV/index returns and rolling tracking comparison as of 2025-12-31.
- [SMDV Annual Shareholder Report](https://www.proshares.com/globalassets/proshares/documents/annual-reports/annual_smdv.pdf) — official fiscal-year 2026 fund/index returns, volatility and fund statistics.
