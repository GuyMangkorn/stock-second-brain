---
type: etf-performance
instrument_type: ETF
entity_key: LSE:MVOL
input_ticker: IEMXF
ticker: MVOL
exchange: London Stock Exchange
fund: iShares Edge MSCI World Minimum Volatility UCITS ETF U.S. Dollar (Accumulating)
tracked_index: MSCI World Minimum Volatility (USD)
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-09-01
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
rolling_performance_as_of: 2026-06-30
current_ytd_as_of: 2026-08-28
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-3.md
return_basis: NAV total return; gross income reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/MVOL
  - ticker/IEMXF
  - geography/International
---

# IEMXF / MVOL ETF Performance

> [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IEMXF เป็น OTC input alias ของ USD share class `LSE:MVOL` ของ iShares Edge
MSCI World Minimum Volatility UCITS ETF ซึ่งเป็น passive, physical,
accumulating global developed-market equity ETF. Official rolling 10-year NAV
Total Return CAGR อยู่ที่ `6.88%` สำหรับ 30 มิ.ย. 2016–30 มิ.ย. 2026 พร้อม
cumulative return `94.59%`; จาก official complete calendar rows 2016–2025
คำนวณได้ `111.71%` หรือ rounded-input CAGR `7.79%†`.

ช่วง 2021–2025 MVOL ทำ cumulative return `35.82%` หรือ CAGR `6.31%` เทียบกับ
issuer benchmark `35.70%` / `6.30%` และ S&P 500 Total Return `96.17%` /
`14.43%`. Current official NAV TR YTD คือ `7.25%` และ NAV `US$78.51` ณ
28 ส.ค. 2026.

## Performance check

- `entity_key: LSE:MVOL`; input card ticker: `IEMXF` (OTC alias); official USD listing: London Stock Exchange `MVOL`
- Fund: iShares Edge MSCI World Minimum Volatility UCITS ETF U.S. Dollar (Accumulating)
- ISIN `IE00B8FHGS14`; share-class launch and fund launch: 30 พ.ย. 2012
- Classification: supported passive/index-tracking developed-market equity UCITS ETF; physical, optimised replication
- Management mode: `passive-index`
- TER: `0.30%`; income treatment: accumulating; cash distributions are not used in the return table because income is reinvested in NAV
- Metric: `NAV Total Return` with gross income reinvested where applicable and fund expenses reflected; currency USD
- Tracked index / issuer benchmark: `MSCI World Minimum Volatility (USD)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark, not the issuer benchmark)
- 10-year window: `2016-06-30` to `2026-06-30`; official rolling 10-year NAV TR CAGR `6.88%`; normalized start/end TR values `100.00` / `194.59`; elapsed years `10.00`
- Calendar calculation: `2016-2025` official annual rows compound to `111.71%`; rounded-input CAGR `7.79%†`. The calendar CAGR is a calculation from rounded displayed annual returns, not the same endpoint window as the issuer rolling field.
- Current official NAV TR YTD: `7.25%` as of 28 ส.ค. 2026; NAV `US$78.51` as of 28 ส.ค. 2026
- Coverage/source note: official iShares annual NAV/index rows cover 2016–2025; 10-year rolling and current fields are kept at their separate as-of dates. The cached S&P 500 convention is reused for the identical 2016–2025 window.

| Year | MVOL NAV TR | MSCI World Minimum Volatility Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 7.40% | 7.47% | 11.96% |
| 2017 | 17.36% | 17.32% | 21.83% |
| 2018 | -2.15% | -2.03% | -4.38% |
| 2019 | 23.16% | 23.17% | 31.49% |
| 2020 | 2.62% | 2.61% | 18.40% |
| 2021 | 14.15% | 14.26% | 28.71% |
| 2022 | -9.86% | -9.79% | -18.11% |
| 2023 | 7.79% | 7.42% | 26.29% |
| 2024 | 10.80% | 10.87% | 25.02% |
| 2025 | 10.52% | 10.54% | 17.88% |

† Calendar CAGR is calculated from the issuer's rounded annual rows; it is not
the issuer's rolling 10-year field.

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016–2025
- Best: 2019, `+23.16%`; least positive: 2020, `+2.62%`
- Worst: 2022, `-9.86%`; least bad down year: 2018, `-2.15%`
- 2016–2025 cumulative / rounded-input CAGR: `111.71%` / `7.79%†`
- 2021–2025 cumulative / rounded-input CAGR: `35.82%` / `6.31%`
- Current official NAV TR YTD: `+7.25%` as of 28 ส.ค. 2026; the return basis is NAV total return and is not mixed with the OTC market price

## Risk read-through

MVOL เป็น developed-world equity factor ETF ที่ลด volatility ผ่านดัชนี
minimum-volatility แต่ไม่ได้รับประกันว่าราคาซื้อขายจะผันผวนน้อยกว่าตลาดเสมอไป.
Official 3-year standard deviation คือ `9.43%` และ beta `1.005` ณ 31 ก.ค.
2026; holdings `286` ณ 25 ส.ค. 2026. จาก annual NAV observations, maximum
year-end drawdown คือ `-9.86%` ใน 2022 และระดับ cumulative year-end กลับสูงกว่า
จุดสูงสุดเดิมใน 2024. Daily NAV drawdown และ exact recovery date
`ไม่พบข้อมูลที่ยืนยันได้` ใน source capture.

เมื่อเทียบกับ issuer benchmark ผลต่างรายปีใน 2016–2025 อยู่ระหว่าง `-0.12`
ถึง `+0.37` percentage points และ rounded-input calendar CAGR ต่างกันเพียง
`-0.01 pp`; นี่เป็น passive tracking observation หลังค่าใช้จ่ายและ rounding
ไม่ใช่ alpha หรือหลักฐาน manager skill. ความเสี่ยงหลักคือ factor concentration,
country/sector allocation, currency, equity-market, liquidity และ counterparty
risk.

## Sources

- [iShares official MVOL product page](https://www.ishares.com/uk/individual/en/products/251382/ishares-msci-world-minimum-volatility-ucits-etf?shortLocale=en_GB&siteEntryPassthrough=true&switchLocale=y) — official identity, LSE USD listing, ISIN, launch, NAV/YTD, benchmark, TER, structure, holdings and risk fields; current observations through 28 ส.ค. 2026
- [iShares official MVOL June 2026 factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/mvol-ishares-edge-msci-world-minimum-volatility-ucits-etf-fund-fact-sheet-en-gb.pdf) — official 2016–2025 annual NAV/index rows, rolling 10-year fields, USD return definition and fund facts as of 30 มิ.ย. 2026
- [IEMXF OTC profile](https://stockanalysis.com/quote/otc/IEMXF/) — secondary OTC alias/name cross-check; not used for NAV Total Return ranking
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 Total Return references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); cached reference as of 31 ธ.ค. 2025
- [[ETF_performance_sources_2026-09-01_run-3]] — source map, observations, calculations, reconciliation and scheduled-local verification record
