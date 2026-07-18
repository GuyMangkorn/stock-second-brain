---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLJP
ticker: FLJP
exchange: NYSE Arca
fund: Franklin FTSE Japan ETF
tracked_index: FTSE Japan Capped Index-NR
benchmark: S&P 500 Total Return
updated: 2026-07-18
performance_as_of: 2026-06-30
rolling_10y_as_of: not_applicable
current_ytd_as_of: 2026-07-08
price_nav_as_of: 2026-07-08
source_batch: raw/imports/ETF_performance_sources_2026-07-18.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FLJP
  - geography/Japan
---

# FLJP Performance

## Bottom line

FLJP มี official `NAV Total Return` ครบปี 2018-2025 ให้ cumulative `62.92%` หรือ
CAGR `6.29%`; เป็นบวก 6 ปีและลบ 2 ปี. ปีดีที่สุดคือ 2025 ที่ `+25.30%` และแย่ที่สุด
คือ 2022 ที่ `-15.78%`. Current YTD ล่าสุดจาก issuer คือ `+14.82%` ณ 8 ก.ค. 2026;
S&P 500 TR อยู่ที่ `+9.64%` ณ 18 ก.ค. 2026 แต่คนละ as-of date จึงไม่ใช่การเทียบแบบ
same-date.

## Performance check

- `entity_key: NYSE Arca:FLJP`
- Fund: Franklin FTSE Japan ETF
- Inception: 2 พ.ย. 2017; expense ratio: `0.09%` (as of 1 ส.ค. 2025)
- Metric: `NAV Total Return` รวม distributions reinvested และหัก fund expenses
- Tracked index (issuer benchmark): `FTSE Japan Capped Index-NR`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ FLJP)
- 10-year NAV TR CAGR: `not applicable` เพราะ official history ยังไม่ครบ 10 ปี;
  official since-inception average annual NAV return คือ `7.83%` ณ 30 มิ.ย. 2026
- Current YTD: `+14.82%` NAV ณ 8 ก.ค. 2026; issuer page ที่ตรวจพบไม่มี snapshot
  NAV YTD ที่ใหม่กว่านี้
- Annual coverage: official complete calendar years 2018-2025; 2017 เป็น
  inception-year partial และ issuer factsheet แสดง `—` จึงไม่นำมาจัดอันดับ

| ปี | FLJP NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -13.10% | -4.38% |
| 2019 | 19.09% | 31.49% |
| 2020 | 14.35% | 18.40% |
| 2021 | 1.16% | 28.71% |
| 2022 | -15.78% | -18.11% |
| 2023 | 19.68% | 26.29% |
| 2024 | 7.76% | 25.02% |
| 2025 | 25.30% | 17.88% |

S&P 500 TR 2018-2025 cumulative คือ `192.03%` และ CAGR `14.33%`; rows ใช้ cached
USD Total Return convention, dividends reinvested, reference as-of `2025-12-31`.

## Up years / Down years

- Up years / Down years: `6 / 2` ใน 2018-2025
- Best: 2025, `+25.30%`
- Least positive: 2021, `+1.16%`
- Worst: 2022, `-15.78%`
- Least bad down year: 2018, `-13.10%`
- 2021-2025 cumulative / CAGR: FLJP `37.67%` / `6.60%`; S&P 500 TR
  `96.17%` / `14.43%`
- Current YTD: `+14.82%` NAV ณ 8 ก.ค. 2026; same-date S&P 500 TR
  `ไม่พบข้อมูลที่ยืนยันได้` (ตัวเลข `+9.64%` ณ 18 ก.ค. 2026 เป็นคนละวัน)

## Risk read-through

FLJP เป็น passive single-country Japan large/mid-cap equity ETF; official 3-year
standard deviation อยู่ที่ `14.67%` ณ 30 มิ.ย. 2026. ความเสี่ยงหลักคือ Japan
country, industrials/financials/technology concentration และ JPY/USD FX เพราะ
กองไม่ได้ hedge ค่าเงิน. Secondary dividend-adjusted market-price proxy ระบุ
maximum drawdown `-32.49%*` เมื่อ 14 ต.ค. 2022 และใช้ 348 trading sessions* ในการ
recover; ไม่ใช่ official NAV drawdown. ข้อมูลยังไม่ครบ 10 ปี จึงไม่ควร relabel
since-inception return เป็น 10-year CAGR.

## Sources

- [Franklin Templeton FLJP product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26357/SINGLCLASS/franklin-ftse-japan-etf/FLJP?role=fp) — identity, NYSE Arca listing, benchmark, inception, expense ratio, current official NAV YTD
- [Official FLJP factsheet](https://www.franklintempleton.com/forms-literature/download/FLJP-FF?role=fp) — annual NAV TR 2018-2025, return definition, since-inception return and risk statistics as of 2026-06-30
- [S&P 500 official returns page](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=76d0e321-60b6-4834-a4b7-68bbe72fd4ea&sourceIdentifier=index-family-specialization) — current S&P 500 TR YTD as of 2026-07-18
- [PortfoliosLab FLJP](https://portfolioslab.com/symbol/FLJP) — secondary dividend-adjusted market-price drawdown/recovery proxy, page updated 2026-07-03
- [[ETF_performance_sources_2026-07-18]] | [[ETF Performance Index]]
