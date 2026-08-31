---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IWMO
input_ticker: IEMMF
ticker: IWMO
exchange: London Stock Exchange
fund: iShares Edge MSCI World Momentum Factor UCITS ETF U.S. Dollar (Accumulating)
tracked_index: MSCI World Momentum Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-09-01
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
rolling_performance_as_of: 2026-06-30
current_ytd_as_of: 2026-08-27
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-3.md
return_basis: NAV total return; gross income reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IWMO
  - ticker/IEMMF
  - geography/International
---

# IEMMF / IWMO ETF Performance

> [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IEMMF เป็น OTC input alias ของ USD share class `LSE:IWMO` ของ iShares Edge
MSCI World Momentum Factor UCITS ETF ซึ่งเป็น passive, physical, accumulating
global developed-market equity factor ETF. Official complete calendar rows
2016–2025 ให้ cumulative NAV Total Return `257.75%` และ rounded-input CAGR
`13.59%†`; ช่วง 2021–2025 ให้ cumulative `64.81%` และ CAGR `10.51%`.

ผลตอบแทน 2016–2025 ต่ำกว่า issuer benchmark เล็กน้อย (`13.59%` เทียบกับ
`13.81%`) และต่ำกว่า S&P 500 Total Return (`14.82%`). Current official NAV TR
YTD คือ `19.25%` ณ 27 ส.ค. 2026 และ NAV `US$114.55` ณ 28 ส.ค. 2026.

## Performance check

- `entity_key: LSE:IWMO`; input card ticker: `IEMMF` (OTC alias); official USD listing: London Stock Exchange `IWMO`
- Fund: iShares Edge MSCI World Momentum Factor UCITS ETF U.S. Dollar (Accumulating)
- ISIN `IE00BP3QZ825`; share-class launch and fund launch: 3 ต.ค. 2014
- Classification: supported passive/index-tracking global developed-markets equity factor UCITS ETF; physical, optimised replication
- Management mode: `passive-index`
- TER: `0.25%`; income treatment: accumulating; cash distributions are not used in the return table because income is reinvested in NAV
- Metric: `NAV Total Return` with gross income reinvested where applicable and fund expenses reflected; currency USD
- Tracked index / issuer benchmark: `MSCI World Momentum Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark, not the issuer benchmark)
- 10-year window: `2016-01-01` to `2025-12-31` complete calendar years; normalized start/end TR values `100.00` / `357.75`; elapsed year count `10`; rounded-input calendar CAGR `13.59%†`
- Calendar calculation: official iShares rows cover all ten complete years 2016–2025. No separate issuer rolling 10-year field was exposed in the reviewed current capture, so `13.59%†` is not relabelled as an issuer-reported rolling field.
- Current official NAV TR YTD: `19.25%` as of 27 ส.ค. 2026; NAV `US$114.55` as of 28 ส.ค. 2026
- Coverage/source note: official iShares factsheet provides 2016–2025 NAV/index rows and June 2026 trailing fields; the current product page provides the newer NAV/YTD fields. The cached S&P 500 convention is reused for the identical 2016–2025 window.

| Year | IWMO NAV TR | MSCI World Momentum Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 4.05% | 4.19% | 11.96% |
| 2017 | 31.91% | 32.09% | 21.83% |
| 2018 | -2.97% | -2.76% | -4.38% |
| 2019 | 27.44% | 27.68% | 31.49% |
| 2020 | 27.90% | 28.26% | 18.40% |
| 2021 | 14.31% | 14.64% | 28.71% |
| 2022 | -17.87% | -17.79% | -18.11% |
| 2023 | 11.56% | 11.75% | 26.29% |
| 2024 | 29.80% | 30.15% | 25.02% |
| 2025 | 21.23% | 21.33% | 17.88% |

† CAGR is calculated from official issuer rows rounded to two decimals; it is
not an issuer-reported rolling 10-year field.

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016–2025
- Best: 2017, `+31.91%`; least positive: 2016, `+4.05%`
- Worst: 2022, `-17.87%`; least bad down year: 2018, `-2.97%`
- 2016–2025 cumulative / rounded-input CAGR: `257.75%` / `13.59%†`
- 2021–2025 cumulative / rounded-input CAGR: `64.81%` / `10.51%`
- Current official NAV TR YTD: `+19.25%` as of 27 ส.ค. 2026; the return basis is NAV total return and is not mixed with the OTC market price

## Risk read-through

IWMO เป็น momentum-factor ETF จึงมี factor rotation, concentration,
country/sector, currency, equity-market, liquidity และ counterparty risk. Official
3-year standard deviation คือ `17.79%` และ beta `0.999` ณ 31 ก.ค. 2026;
holdings `353` ณ 28 ส.ค. 2026. จาก annual NAV observations, maximum year-end
drawdown คือ `-17.87%` ใน 2022 และ cumulative year-end กลับสูงกว่าจุดสูงสุดเดิม
ใน 2024. Daily NAV drawdown และ exact recovery date `ไม่พบข้อมูลที่ยืนยันได้`.

ผลต่างระหว่างกองทุนกับ issuer benchmark อยู่ที่ `-0.36` ถึง `-0.08`
percentage points ทุกปีใน 2016–2025; rounded-input CAGR ต่างกันประมาณ
`-0.21 pp`. นี่เป็น passive tracking observation หลังค่าใช้จ่ายและ rounding
ไม่ใช่ alpha หรือหลักฐาน manager skill. Momentum อาจ lag ตลาดเมื่อ leadership
กลับทิศอย่างรวดเร็ว แม้ long-run return profile จะเด่นกว่ากองทุน minimum-volatility
ในชุดข้อมูลนี้.

## Sources

- [iShares official IWMO product page](https://www.ishares.com/uk/individual/en/products/270051/ishares-msci-world-momentum-factor-ucits-etf?locale=en_GB&siteEntryPassthrough=true&userType=individual) — official identity, LSE USD listing, ISIN, launch, NAV/YTD, benchmark, TER, structure, holdings and risk fields; current observations through 28 ส.ค. 2026
- [iShares official IWMO June 2026 factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/iwmo-ishares-edge-msci-world-momentum-factor-ucits-etf-fund-fact-sheet-en-gb.pdf) — official 2016–2025 annual NAV/index rows, USD return definition and fund facts as of 30 มิ.ย. 2026
- [IEMMF OTC profile](https://stockanalysis.com/quote/otc/IEMMF/) — secondary OTC alias/name cross-check; not used for NAV Total Return ranking
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 Total Return references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); cached reference as of 31 ธ.ค. 2025
- [[ETF_performance_sources_2026-09-01_run-3]] — source map, raw observations, calculations, reconciliation and scheduled-local verification record
