---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:DMXF
input_ticker: DMXF
ticker: DMXF
exchange: NASDAQ
fund: iShares ESG Advanced MSCI EAFE ETF
tracked_index: MSCI EAFE Choice ESG Screened Index (USD) (Net)
benchmark: MSCI EAFE Choice ESG Screened Index (USD) (Net)
management_mode: passive-index
updated: 2026-09-01
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
rolling_10y_as_of: not applicable (<10y history)
current_ytd_as_of: 2026-08-31
price_nav_as_of: 2026-08-31
fund_facts_as_of: 2026-08-31 / 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-6.md
return_basis: NAV total return; dividends and capital gains reinvested; net of fund expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/DMXF
  - geography/International
  - geography/global-developed
---

# DMXF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DMXF คือ iShares ESG Advanced MSCI EAFE ETF ที่จดทะเบียนบน `NASDAQ` และเป็น
passive, developed-market equity ETF ซึ่งติดตาม `MSCI EAFE Choice ESG Screened
Index (USD) (Net)`. กองทุนเริ่ม 16 มิ.ย. 2020, expense ratio `0.12%`, จ่าย
distribution แบบ semi-annual และมี `395` holdings ณ 31 ส.ค. 2026.

จาก official complete calendar-year NAV Total Return rows ช่วง 2021-2025
ผลตอบแทนสะสมคือ `37.84%` หรือ rounded-input CAGR `6.63%`, โดยมี positive /
negative years `4 / 1`. ปีดีที่สุดคือ 2025 ที่ `+23.04%` และแย่ที่สุดคือ 2022
ที่ `-19.18%`; current official NAV TR YTD อยู่ที่ `+16.02%` ณ 31 ส.ค. 2026
และ NAV อยู่ที่ `USD 86.46` ในวันเดียวกัน. S&P 500 Total Return เป็นเพียง
common USD reference ไม่ใช่ tracked index ของ DMXF.

## Performance check

- `entity_key: NASDAQ:DMXF`; official fund name, ticker, exchange and inception are confirmed by iShares and Nasdaq: `2020-06-16`.
- Classification: `passive-index`; the fund seeks to track the MSCI EAFE Choice ESG Screened Index, a free-float-adjusted, market-capitalization-weighted index of developed-market equities excluding the U.S. and Canada with ESG and controversy screens.
- Metric: issuer `Total Return` / NAV return, with dividends and capital gains reinvested and fund expenses deducted; market-price return is kept separate.
- Issuer benchmark: `MSCI EAFE Choice ESG Screened Index (USD) (Net)`. Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference only).
- Official current snapshot as of `2026-08-31`: NAV `USD 86.46`, closing price `USD 86.59`, net assets `USD 959.73m`, premium/discount `0.15%`, and exchange `NASDAQ`.
- Official current NAV TR YTD: `+16.02%` as of `2026-08-31`. Official rolling fields as of `2026-06-30`: 1-year `18.74%`, 3-year annualized `15.47%`, 5-year annualized `7.72%`, and since inception `11.48%`; a 10-year field is not applicable because the fund launched in 2020.
- Coverage/source note: official annual NAV rows are available for complete years 2021-2025; 2020 is an inception-year partial and is not backfilled or ranked. No secondary annual proxy is used.

| Year | DMXF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 10.92% | 28.71% |
| 2022 | -19.18% | -18.11% |
| 2023 | 20.75% | 26.29% |
| 2024 | 3.49% | 25.02% |
| 2025 | 23.04% | 17.88% |

The official DMXF 2021-2025 rows compound to `37.84%` / rounded-input CAGR
`6.63%`. The cached S&P 500 rows for the same window compound to `96.17%` /
rounded-input CAGR `14.43%`. Annual DMXF-minus-S&P observations are `-17.79`,
`-1.07`, `-5.54`, `-21.53` and `+5.16` percentage points; these are arithmetic
comparisons, not alpha. The cumulative relative wealth of DMXF versus the S&P
reference is `-29.74%` over 2021-2025.

**Up years / Down years**

- Best NAV TR year: 2025, `+23.04%`
- Least positive year: 2024, `+3.49%`
- Worst NAV TR year: 2022, `-19.18%`
- Least-bad down year: 2022, `-19.18%`
- 2021-2025 annual-return standard deviation, population: `15.21%`
- Current official NAV TR YTD: `+16.02%` as of `2026-08-31`

## Risk read-through

DMXF มี annual NAV TR volatility ที่ค่อนข้างสูงในช่วง 2021-2025 โดยมี downside
ในปี 2022 และ recovery ใน 2023-2025; 5-year rounded-input CAGR อยู่ที่ `6.63%`
สำหรับ common window นี้. Official 3-year standard deviation อยู่ที่ `14.23%`
และ equity beta `0.82` ณ 31 ก.ค. 2026. Portfolio มี Financials `33.71%`,
Information Technology `18.95%`, Industrials `15.16%` และ Health Care `10.18%`
ณ 31 ส.ค. 2026; geography หลักคือ Japan `30.04%`, Netherlands `10.54%`,
Switzerland `9.80%`, Germany `7.89%` และ France `7.80%`.

ความเสี่ยงหลักคือ developed-market country, currency, sector, ESG-screening และ
fair-value/timing risk จากหุ้นต่างประเทศ. Official daily NAV observations ที่
เพียงพอสำหรับคำนวณ maximum drawdown และ recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`;
จึงไม่แทนที่ด้วย market-price หรือ secondary proxy. Distribution ล่าสุดที่ issuer
แสดงคือ `USD 1.032946` ex-date 15 มิ.ย. 2026 และ `USD 2.504331` ex-date 16 ธ.ค.
2025; frequency คือ semi-annual.

## Sources

- [iShares DMXF product and performance page](https://www.ishares.com/us/products/314362/ishares-esg-advanced-msci-eafe-etf) — official identity, NASDAQ exchange, inception, current NAV/price/YTD, holdings, exposures, rolling fields and distributions; reviewed 2026-09-01.
- [iShares DMXF fact sheet](https://www.ishares.com/us/literature/fact-sheet/dmxf-ishares-esg-advanced-msci-eafe-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 calendar NAV/market-price/index rows, return definition, fee, benchmark and fund facts as of 2026-06-30.
- [Nasdaq DMXF information circular](https://www.nasdaqtrader.com/content/newsalerts/2020/infocircular/DMXF%20USXF%20ETF%20Circular.pdf) — listing, exchange and index objective confirmation.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and the cached `check-etf-performance` convention — common USD total-return benchmark for 2021-2025.
- [[ETF_performance_sources_2026-09-01_run-6]] | [[ETF Performance Index]]

## Follow-up

- Refresh the current NAV/YTD snapshot and retain the June factsheet as the annual-row source; do not claim a 10-year NAV TR CAGR before the fund has ten elapsed years.
- Keep DMXF under International exposure rather than NASDAQ/USA geography; reconcile the shared region/index/log navigation in a clean navigation pass.
- Verify official daily NAV history if iShares publishes a suitable series for maximum drawdown and recovery.
