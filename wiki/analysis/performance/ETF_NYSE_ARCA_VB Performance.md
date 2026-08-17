---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VB
ticker: VB
exchange: NYSE Arca
fund: Vanguard Morningstar Small-Cap ETF
tracked_index: Morningstar US Small Cap Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-08-07
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-08-07
price_nav_as_of: 2026-08-07
distribution_as_of: not disclosed
benchmark_transition_effective: 2026-07-29
methodology_as_of: not disclosed
benchmark_source_accessed: 2026-08-17
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VB
  - geography/United-States
---

# VB Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

VB ให้ cumulative NAV Total Return 169.68% หรือ CAGR 10.43% ใน complete
calendar years 2016-2025 จาก official annual rows ที่ปัดเศษแล้ว; S&P 500 TR
อยู่ที่ 298.33% / CAGR 14.82% ในช่วงเดียวกัน. เป็นบวก 8 ปีและลบ 2 ปี โดยปีดี
ที่สุดคือ 2019 ที่ +27.37% และแย่ที่สุดคือ 2022 ที่ -17.60%. Current YTD
ของ VB คือ +19.48% ณ 7 ส.ค. 2026; S&P 500 TR ล่าสุดที่ยืนยันได้คือ +13.58%
ณ 5 ส.ค. 2026 จึงเป็นคนละ as-of date และไม่ควรตีความเป็น same-day spread.

## Performance check

- entity_key: NYSE Arca:VB
- Inception: 26 ม.ค. 2004
- Expense ratio: 0.03% ตาม SEC summary prospectus ลงวันที่ 28 เม.ย. 2026
- Metric: NAV Total Return แบบ pre-tax รวม dividends และ capital-gains distributions
  reinvested หลัง fund expenses; currency: USD
- Tracked index (issuer benchmark): Morningstar US Small Cap Index; ชื่อเดิม
  CRSP US Small Cap Index; benchmark transition effective 29 ก.ค. 2026. Older
  factsheet/report ยังใช้ชื่อ CRSP; หน้านี้ไม่ infer management continuity.
- Benchmark: S&P 500 Total Return (USD gross index TR, dividends reinvested; no
  fund-expense deduction; common reference benchmark ไม่ใช่ issuer benchmark ของ VB)
- Official rolling 10-year NAV TR: 10.90% average annual return ณ 31 ก.ค. 2026
  จาก issuer; raw TR endpoints ไม่ได้เปิดเผย จึงไม่คำนวณ endpoint-based CAGR ซ้ำ.
- Calendar-window formula: (Π(1 + annual NAV TR))^(1 / 10.00) - 1; cumulative/CAGR
  ข้างต้นใช้ annual rows ทางการที่ปัดเศษแล้ว.
- Annual coverage: official complete calendar years 2016-2025; ไม่มี proxy หรือ
  inception-year partial. S&P rows ใช้ cached USD gross index TR convention,
  dividends reinvested, reference as-of 31 ธ.ค. 2025.

| ปี | ETF TR | Benchmark |
|---|---:|---:|
| 2016 | 18.31% | 11.96% |
| 2017 | 16.24% | 21.83% |
| 2018 | -9.30% | -4.38% |
| 2019 | 27.37% | 31.49% |
| 2020 | 19.08% | 18.40% |
| 2021 | 17.72% | 28.71% |
| 2022 | -17.60% | -18.11% |
| 2023 | 18.21% | 26.29% |
| 2024 | 14.23% | 25.02% |
| 2025 | 8.83% | 17.88% |

## Up years / Down years

- Up years / Down years: 8 / 2 ใน 2016-2025
- Best: 2019, +27.37%
- Least positive: 2025, +8.83%
- Worst: 2022, -17.60%
- Least bad down year: 2018, -9.30%
- 2021-2025 cumulative: VB 42.55%, CAGR 7.35%; S&P 500 TR 96.17%, CAGR 14.43%
- Current YTD: VB +19.48% NAV ณ 7 ส.ค. 2026; S&P 500 TR +13.58% ณ 5 ส.ค. 2026
  จาก official S&P DJI dashboard; exact same-day Aug-7 benchmark field not disclosed.

## Risk read-through

10-year NAV CAGR: issuer-reported 10.90% ณ 31 ก.ค. 2026; calendar 2016-2025
CAGR 10.43% เป็นคนละ window. VB เป็น passive U.S. small-cap broad equity แบบ
full replication จึงมี small-cap/cyclicality และ equity drawdown sensitivity ชัด.
Official 36-month monthly standard deviation คือ 17.26% ณ 30 มิ.ย. 2026 และ
expense ratio อยู่ที่ 0.03%.

Quarter-end NAV-TR calculation จาก Vanguard official quarter-end observations:
high-water index 1.58849 ณ 31 ธ.ค. 2019, trough index 1.11067 ณ 31 มี.ค. 2020,
ดังนั้น drawdown = 1.11067 / 1.58849 - 1 = -30.08%. Index 1.89154 ณ 31 ธ.ค.
2020 ยืนยันว่ากลับผ่าน prior peak แล้ว. นี่เป็น quarter-end calculation ไม่ใช่
daily maximum drawdown series. Monthly NAV-price-only proxy จาก Vanguard historical
price table อยู่ที่ -30.34% (peak 165.69, trough 115.42, recovery 181.97) และ
ไม่รวม distributions จึงแยกจาก NAV Total Return.

Classification: Structural = U.S. small-cap broad equity tracking the Morningstar/
legacy CRSP small-cap index. Behavioral = higher-beta small-cap cyclicality, with
8 / 2 positive/negative calendar years in 2016-2025; ไม่ใช่ downside hedge.

## Driver notes

- Observed data pattern: 2019 เป็นปีบวกสูงสุดและ 2022 เป็นปีลบสูงสุดจาก complete
  official calendar rows; ไม่ตีความเป็น event attribution.
- Methodology transition: issuer benchmark เปลี่ยนชื่อ CRSP → Morningstar effective
  29 ก.ค. 2026; page นี้ไม่ claim management continuity.
- Scheduled-inline refresh on 17 ส.ค. 2026 rechecked Vanguard's official factsheet,
  product page and name-change notice. The latest numeric current-period capture
  retained is the official product-page observation through 7 ส.ค. 2026; no later
  machine-readable current return field was verified, so the separate as-of dates
  above remain explicit.

## Sources

- [Vanguard VB product page](https://investor.vanguard.com/investment-products/etfs/profile/vb) — official annual NAV/market-price/benchmark table, latest YTD, rolling return, historical-price table, and fund identity
- [Vanguard VB factsheet](https://fund-docs.vanguard.com/F0969.pdf) — official NAV return definition, passive/full-replication approach, volatility, fund facts as of 30 มิ.ย. 2026
- [Vanguard annual shareholder report](https://fund-docs.vanguard.com/AR969.pdf) — official 2016-2025 return path and 2025-12-31 cumulative/CAGR cross-check
- [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/36405/000003640526000206/f44854d1.htm) — official 28 เม.ย. 2026 expense ratio, structure and strategy
- [Vanguard name-change list](https://advisors.vanguard.com/content/dam/fas/pdfs/MRSTR.pdf) and [benchmark transition notice](https://www.vanguardmexico.com/es/inicio/noticias/name-changes-for-vanguard-equity-index-funds-and-crsp-morningstar-benchmarks) — effective 29 ก.ค. 2026 name/index transition
- [Morningstar US Small Cap Index](https://indexes.morningstar.com/indexes/details/morningstar-us-small-cap-FS00009VTW?currency=USD&tab=overview&variant=TR) — benchmark identity only; methodology/performance data not used
- [S&P DJI dashboard](https://www.spglobal.com/spdji/en/documents/performance-reports/dashboard-daily-global-markets.pdf) and [S&P methodology](https://www.spglobal.com/spdji/en/methodology/article/index-mathematics-methodology/) — current 2026 YTD gross TR through 5 ส.ค. 2026 and dividends-reinvested definition
- [S&P 500 TR cache source 1](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [source 2](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [source 3](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [source 4](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — cached 2016-2025 USD gross S&P 500 TR convention, reference as-of 31 ธ.ค. 2025
- [[ETF_performance_sources_2026-08-10]] | [[ETF Performance Index]]
