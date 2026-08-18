---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWG
ticker: EWG
exchange: NYSE Arca
fund: iShares MSCI Germany ETF
tracked_index: MSCI Germany Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-17
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; distributions reinvested; fund expenses reflected in NAV
tags:
  - analysis/etf-performance
  - ticker/EWG
  - geography/Germany
---

# EWG Performance

> Navigation: [[ETF Region Index]] → [[Germany ETF]] → [[ETF Performance Index]]

## Bottom line

EWG ให้ cumulative `NAV Total Return` ประมาณ `103.85%` ในปี 2016-2025 หรือ
rounded-input CAGR `7.38%`; บวก 8 ปีและลบ 2 ปี เทียบ S&P 500 TR CAGR `14.82%`.
ปีดีที่สุดคือ 2025 `+35.15%`; แย่ที่สุดคือ 2018 `-22.30%`. Latest official
NAV TR YTD ของ EWG คือ `+6.09%` ณ 14 ส.ค. 2026; NAV ล่าสุดที่ตรวจสอบได้คือ
`$43.90` ณ 17 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:EWG`
- Inception: 12 มี.ค. 1996; official exchange `NYSE Arca`
- Classification: `passive-index`; iShares ใช้ indexing/representative sampling เพื่อติดตาม German large- และ mid-cap equities; derivatives ใช้เพื่อ tracking/cash management ตาม prospectus ไม่ใช่ payoff หลัก
- Metric: `NAV Total Return` (USD), distributions reinvested หลังหัก fund expenses
- Tracked index (issuer benchmark): `MSCI Germany Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ EWG)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `8.22%`; Start TR value: `100.00`; End TR value:
  `220.25`; Years: `10.00`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`; End TR เป็น normalized
  calculation จาก official cumulative `120.25%`, ไม่ใช่ raw index level
- Annual coverage: official complete calendar years 2016-2025; ไม่มี `*` หรือ `†`.
  ปี 2016-2020 มาจาก issuer table ที่ปัดเศษหนึ่งตำแหน่ง; 2021-2025 ใช้ official
  U.S. fact sheet แบบสองตำแหน่ง
- S&P 500 cache 2016-2025: cumulative `298.33%`; CAGR `14.82%` จาก rounded annual inputs
- Latest official product-page snapshot: NAV `$43.90`, closing price `$43.96`, net assets `$1.712bn`, and 52 holdings as of 17 Aug / 14 Aug 2026; current NAV TR YTD `+6.09%` is as of 14 Aug 2026.

| ปี | EWG NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 2.60% | 11.96% |
| 2017 | 27.40% | 21.83% |
| 2018 | -22.30% | -4.38% |
| 2019 | 20.60% | 31.49% |
| 2020 | 11.30% | 18.40% |
| 2021 | 4.85% | 28.71% |
| 2022 | -22.17% | -18.11% |
| 2023 | 22.90% | 26.29% |
| 2024 | 10.32% | 25.02% |
| 2025 | 35.15% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2025, `+35.15%`
- Least positive: 2016, `+2.60%`
- Worst: 2018, `-22.30%`
- Least bad down year: 2022, `-22.17%`
- 2021-2025 common-window cumulative: EWG `49.53%`, CAGR `8.38%`; S&P 500 TR
  `96.17%`, CAGR `14.43%`
- Current official NAV TR YTD: EWG `+6.09%` as of 14 ส.ค. 2026.

## Risk read-through

**10-year NAV CAGR:** `8.22%` ณ 30 มิ.ย. 2026. EWG เป็น Germany single-country
equity ที่กระจุกใน Industrials `30.22%`, Financials `22.60%` และ Information
Technology `15.61%` ณ 14 ส.ค. 2026 พร้อม EUR/USD exposure จึงไวต่อ country
cycle, sector concentration และ FX. Official 3-year standard deviation คือ
`16.03%` ณ 31 ก.ค. 2026; beta `0.76` ณ วันเดียวกัน. Official NAV TR max
drawdown/recovery ยัง `ไม่พบข้อมูลที่ยืนยันได้`. Expense ratio `0.49%` เป็น
cost drag สำคัญ.

## Sources

- [iShares EWG product page](https://www.ishares.com/us/products/239650/ishares-msci-germany-etf) — official identity, exchange, current NAV/YTD, holdings, sectors, rolling fields and distributions
- [iShares EWG fact sheet](https://www.ishares.com/us/literature/fact-sheet/ewg-ishares-msci-germany-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 NAV/index returns, fee, benchmark, fund facts and risk as of 30 June 2026
- [BlackRock EWG calendar-year performance](https://www.blackrock.com/fi/professionals/products/239650/ishares-msci-germany-etf) — official 2016-2025 NAV returns and current international-locale cross-check
- [iShares EWG summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-germany-etf-8-31.pdf) — indexing strategy, 80% policy, representative sampling, derivatives role and Germany risks
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — USD Total Return definition
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
