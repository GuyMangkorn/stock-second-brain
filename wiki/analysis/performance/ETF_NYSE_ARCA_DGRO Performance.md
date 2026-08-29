---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DGRO
ticker: DGRO
exchange: NYSE Arca
updated: 2026-08-29
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
management_mode: passive-index
tags:
  - analysis/etf-performance
  - geography/United-States
  - ticker/DGRO
---

# DGRO Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]
> Entity: [[ETF_AMEX_DGRO]]

## Bottom line

DGRO ให้ผลตอบแทนเป็นบวก `8 / 10` complete calendar years ในช่วง 2016-2025 โดยปีดีที่สุดคือ 2019 ที่ `+30.00%` และแย่ที่สุดคือ 2022 ที่ `-7.85%`. Official rolling 10-year NAV Total Return อยู่ที่ cumulative `251.19%` หรือ CAGR `13.38%` สำหรับ 2016-06-30 ถึง 2026-06-30. ใน common window 2021-2025 DGRO ให้ cumulative `73.82%` หรือ CAGR `11.69%` เทียบกับ S&P 500 Total Return ที่ `96.17%` หรือ `14.43%`; lagged ราว `22.35 percentage points` แบบ cumulative และ `2.74 pp` ต่อปี. Latest NAV TR YTD คือ `+15.25%` ณ 2026-08-27; NAV `USD 79.27` และ closing price `USD 79.28` ณ วันเดียวกัน.

## Performance check

- `entity_key: NYSE Arca:DGRO`
- Exchange: `NYSE Arca`; inception: 10 มิ.ย. 2014; asset class: `Equity`
- Metric: `NAV Total Return` รวมเงินปันผลและ capital gains ที่ reinvested และหัก fund expenses ตาม issuer convention
- Management mode: `passive-index`
- Tracked index (issuer benchmark): `Morningstar US Dividend Growth Index`
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference ไม่ใช่ tracked index ของ DGRO)
- Official rolling 10-year window: `2016-06-30` ถึง `2026-06-30`; normalized NAV TR index `100.00 → 351.19`; cumulative `251.19%`; CAGR `13.38%`; elapsed years `10.00`
- Complete calendar window: `2016-2025` DGRO compound `242.63%` / rounded-input CAGR `13.11%`; S&P 500 cache compound `298.33%` / CAGR `14.82%`
- Common window: `2021-2025` DGRO compound `73.82%` / rounded-input CAGR `11.69%`; S&P 500 cache compound `96.17%` / CAGR `14.43%`
- Coverage note: 2016-2020 annual NAV TR มาจาก official iShares regional performance page ที่แสดงหนึ่งทศนิยม; 2021-2025 มาจาก official U.S. product page ที่แสดงสองทศนิยม. ไม่มี secondary proxy ในตารางนี้.

| ปี | DGRO TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 15.30% | 11.96% |
| 2017 | 22.80% | 21.83% |
| 2018 | -2.20% | -4.38% |
| 2019 | 30.00% | 31.49% |
| 2020 | 9.50% | 18.40% |
| 2021 | 26.56% | 28.71% |
| 2022 | -7.85% | -18.11% |
| 2023 | 10.43% | 26.29% |
| 2024 | 16.61% | 25.02% |
| 2025 | 15.74% | 17.88% |

**Up years / Down years**

- Best: 2019, **+30.00%**
- Least positive: 2020, **+9.50%**
- Worst: 2022, **-7.85%**
- Least bad down year: 2018, **-2.20%**
- Current YTD: **+15.25% NAV**, as of 2026-08-27
- DGRO beat the S&P 500 common reference in 2016, 2017, 2018, and 2022 (`4 / 10` complete years); this is not a manager-skill claim.

## Risk read-through

Official 3-year standard deviation is `10.65%` and equity beta `0.68` as of 2026-07-31. Current official characteristics as of 2026-08-27 include `390` holdings, net assets `USD 43.60bn`, P/B `4.04`, P/E `24.68`, and premium/discount `0.02%`; 30-day SEC yield is `1.97%` and trailing 12-month yield `1.89%` as of 2026-07-31. Expense ratio is `0.08%` and distributions are quarterly.

Secondary price-and-distribution history reports maximum drawdown of approximately `-35.10%` on 23 มี.ค. 2020 with `161` trading sessions to recovery. This is secondary evidence, not an official NAV drawdown calculation; an official daily NAV TR series sufficient to reproduce max drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`. Structurally DGRO is U.S. dividend growth / quality large-cap exposure. Behaviorally it showed a relative cushion in 2022, but it remains exposed to broad equity, valuation, and rate repricing risk.

## Driver notes

- **2022, observed:** DGRO fell `-7.85%` versus S&P 500 TR `-18.11%`, a `+10.26 pp` relative cushion without capital protection.
- **2020, observed:** official calendar NAV TR was `+9.50%`, while the secondary series still records a sharp COVID-era drawdown; the return bases are not interchangeable.
- **2025, observed:** DGRO returned `+15.74%`; one positive year does not establish persistent outperformance.

## Sources

- [iShares U.S. product page](https://www.ishares.com/us/products/264623/DGRO) — identity, NYSE Arca listing, current NAV/YTD, holdings, characteristics, distributions, annual 2021-2025 returns, and benchmark
- [iShares regional performance page](https://www.ishares.com/ch/professionals/en/products/264623/ishares-core-dividend-growth-etf?switchLocale=Y) — official 2016-2025 calendar rows and 10-year rolling performance as of 2026-06-30
- [iShares DGRO factsheet](https://www.ishares.com/us/literature/fact-sheet/dgro-ishares-core-dividend-growth-etf-fund-fact-sheet-en-us.pdf)
- [PortfoliosLab](https://portfolioslab.com/symbol/DGRO) — secondary drawdown and recovery evidence
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common reference benchmark
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
