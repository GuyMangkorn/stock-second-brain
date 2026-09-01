---
type: etf-performance
instrument_type: ETF
entity_key: LSE:GGRA
ticker: GGRA
input_ticker: WGQDF
input_alias: WGQDF
exchange: London Stock Exchange
fund: WisdomTree Global Quality Dividend Growth UCITS ETF - USD Acc
tracked_index: WisdomTree Global Developed Quality Dividend Growth Index (TR)
benchmark: S&P 500 Total Return
updated: 2026-09-01
performance_as_of: 2026-07-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-6.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/GGRA
  - ticker/WGQDF
  - geography/International
  - geography/global-developed
---

# GGRA Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

`WGQDF` เป็น OTC input alias ที่ resolve ได้เป็น USD accumulating share class
ของ WisdomTree Global Quality Dividend Growth UCITS ETF ซึ่งมี official USD
listing เป็น `LSE:GGRA` และ ISIN `IE00BZ56SW52`. กองทุนเป็น passive,
physical, index-tracking global developed-market equity ETF ที่ track WisdomTree
Global Developed Quality Dividend Growth Index (TR) และใช้ dividend-weighted,
quality/momentum risk-screened methodology.

Official complete calendar-year NAV Total Return 2017-2025 compound เป็น
`178.34%` หรือ rounded-input CAGR `12.05%`; เทียบกับ S&P 500 TR ที่ `255.78%`
หรือ `15.14%` ต่อปี. ช่วง 2021-2025 GGRA ทำ CAGR `9.02%` เทียบกับ S&P 500
ที่ `14.43%`. Latest official NAV TR YTD ที่ยืนยันได้คือ `+7.28%` ณ 31 ก.ค.
2026; current same-date secondary exchange-price total-return cross-check คือ
`+9.45%` ณ 28 ส.ค. 2026 และไม่ถูกนำมาปนกับ NAV TR.

## Performance check

- `entity_key: LSE:GGRA`; input card ticker: `WGQDF` (OTC alias); official USD listing: London Stock Exchange `GGRA`
- Classification: supported passive/index-tracking global developed-markets quality/dividend-growth equity UCITS ETF
- ISIN `IE00BZ56SW52`; inception: 3 มิ.ย. 2016; total expense ratio `0.38%`; income treatment: accumulating; replication: physical/fully replicated
- Metric: `NAV Total Return` net of fees, USD; accumulating income remains in NAV. Market-price and exchange-price returns remain separate.
- Tracked index (issuer benchmark): `WisdomTree Global Developed Quality Dividend Growth Index (TR)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของกองทุน)
- 10-year NAV TR: `not applicable (<10y history)`; 2016 inception-year observation is partial and is excluded from calendar-year ranking
- 2017-2025 calendar NAV TR: cumulative `178.34%`; rounded-input CAGR `12.05%`
- 2021-2025 calendar NAV TR: cumulative `54.02%`; rounded-input CAGR `9.02%`
- Issuer index 2017-2025: cumulative `183.89%`; rounded-input CAGR `12.29%`; 2021-2025 CAGR `9.24%`
- Latest official current NAV TR YTD: `+7.28%` as of 31 ก.ค. 2026; the latest secondary LSE USD exchange-price return with payments is `+9.45%` as of 28 ส.ค. 2026 and is not a NAV substitute
- Latest official NAV: `US$50.525` as of 28 ส.ค. 2026; another WisdomTree locale page showed `US$50.542` for the same date, so the IE issuer page is retained as the canonical current-NAV source and the small locale discrepancy is disclosed
- Coverage/source note: official WisdomTree factsheet provides annual NAV/index rows and July YTD; the issuer product page provides current identity, NAV and structure. No official issuer NAV YTD field through 28 ส.ค. 2026 was established in this lean capture.

| Year | GGRA NAV TR | WisdomTree Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2017 | 27.99% | 28.42% | 21.83% |
| 2018 | -8.81% | -8.63% | -4.38% |
| 2019 | 33.18% | 33.51% | 31.49% |
| 2020 | 16.26% | 16.51% | 18.40% |
| 2021 | 19.29% | 19.72% | 28.71% |
| 2022 | -13.88% | -13.88% | -18.11% |
| 2023 | 18.26% | 18.49% | 26.29% |
| 2024 | 8.98% | 9.21% | 25.02% |
| 2025 | 16.33% | 16.58% | 17.88% |

## Up years / Down years

- Up years / Down years: `7 / 2` across complete calendar years 2017-2025
- Best: 2019, `+33.18%`; least positive: 2024, `+8.98%`
- Worst: 2018, `-8.81%`; least-bad down year: 2018, `-8.81%`
- 2017-2025 CAGR: `12.05%`; 2021-2025 CAGR: `9.02%`
- Issuer-index tracking spread calculated from rounded annual rows: `-0.25 pp` CAGR over 2017-2025 and `-0.21 pp` CAGR over 2021-2025; this is a tracking comparison, not alpha
- Latest official NAV TR YTD: `+7.28%` as of 31 ก.ค. 2026. The secondary `+9.45%` observation is exchange-price total return with payments through 28 ส.ค. 2026 and is kept separate.

## Risk read-through

GGRA กระจายหุ้น developed markets แต่มี factor และ dividend-weighting exposure
จึงอาจเบี่ยงจาก market-cap global index ได้มากกว่ากอง broad-market ทั่วไป. Official
issuer methodology ระบุ quality และ momentum composite risk screen, ESG exclusion
และการเลือกประมาณ 600 บริษัทก่อน dividend-based weighting. ความเสี่ยงหลักคือ
equity-market, country, currency, sector/style concentration และ tracking error.
Annual-return population dispersion ที่คำนวณจากแถวปัดเศษ 2017-2025 อยู่ที่
`14.66%`; ค่านี้ไม่ใช่ official daily volatility. Official daily NAV history
สำหรับคำนวณ maximum drawdown และ recovery ยังไม่ถูกยืนยันใน lean capture จึงบันทึก
เป็น `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [WisdomTree official GGRA product page](https://www.wisdomtree.com/ie/products/equities/wisdomtree-global-quality-dividend-growth-ucits-etf---usd-acc) — official identity, ISIN, LSE USD listing, inception, accumulating structure, index, TER, replication and current NAV/AUM; current observations through 28 ส.ค. 2026
- [WisdomTree official GGRA factsheet](https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BZ56SW52/) — official NAV/index annual rows 2017-2025, July 2026 YTD, benchmark methodology, risk disclosures and listing table; document date 31 ก.ค. 2026
- [StockAnalysis WGQDF OTC profile](https://stockanalysis.com/quote/otc/WGQDF/) — secondary input-alias and fund-name cross-check only; not used for NAV Total Return ranking
- [Cbonds GGRA profile](https://cbonds.fr/etf/6397/) — secondary LSE USD exchange-price total return with payments, YTD `+9.45%` through 28 ส.ค. 2026; not mixed with NAV TR
- [Borsa Italiana IE00BZ56SW52 profile](https://www.borsaitaliana.it/borsa/etf/scheda/IE00BZ56SW52-ETFP.html) — secondary exchange/listing and instrument metadata cross-check; not used for USD NAV TR ranking
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); cached USD Total Return convention as of 31 ธ.ค. 2025
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-6]] | [[ETF Performance Index]]

---
window: complete calendar years 2017-2025 plus current 2026 YTD
return_basis: NAV total return
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
---
