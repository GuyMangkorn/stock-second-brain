---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:SCHF
ticker: SCHF
exchange: NYSE Arca
updated: 2026-08-29
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return for official fields; secondary dividend-reinvested proxy for rows marked *
management_mode: passive-index
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/SCHF
---

# SCHF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

SCHF เป็น passive developed-markets ex-U.S. ETF ที่มี official rolling 10-year NAV
Total Return `10.11%` annualized และ official NAV TR YTD `15.26%` ณ 2026-07-31.
สำหรับ complete annual comparison หน้านี้ใช้ secondary dividend-reinvested
total-return proxy* เนื่องจาก reviewed official annual rows ไม่ได้อยู่ใน capture
ที่อ่านและตรวจสอบได้แบบครบถ้วน: proxy CAGR ช่วง 2016-2025 คือ `8.81%*` และช่วง
2021-2025 คือ `9.31%*`. Proxy แยกจาก official NAV fields และไม่ใช้ตัดสิน
tracking difference.

## Performance check

- `entity_key: NYSE Arca:SCHF`
- Fund: `Schwab International Equity ETF`; inception: 3 พ.ย. 2009; asset class: developed international equity
- Metric: official fields เป็น `NAV Total Return` รวมเงินปันผลและ capital gains ที่ reinvested และหักค่าใช้จ่ายตาม issuer convention
- Management mode: `passive-index`; implementation ใช้ sampling เพื่อ track index
- Tracked index (issuer benchmark): `FTSE Developed ex US Index (Net)`
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference ไม่ใช่ tracked index ของ SCHF)
- Official rolling 10-year NAV TR: `10.11%` annualized ณ `2026-07-31`; official 2026-06-30 quarterly field คือ `10.63%`
- Official current NAV TR YTD: `15.26%` ณ `2026-07-31`; market-price YTD ในช่วงเดียวกันคือ `14.79%`, จึงไม่ปะปนกัน
- Complete calendar window: `2016-2025` secondary proxy compound `132.55%*` / rounded-input CAGR `8.81%*`; S&P 500 cache compound `298.33%` / CAGR `14.82%`
- Common window: `2021-2025` secondary proxy compound `56.09%*` / rounded-input CAGR `9.31%*`; S&P 500 cache compound `96.17%` / CAGR `14.43%`
- Coverage note: annual table ด้านล่างเป็น secondary dividend-reinvested total-return proxy จาก FinanceCharts; official Schwab page ให้ current/rolling NAV fields และมี NAV history download แต่ reviewed annual rows ไม่ readable เป็นชุดที่ใช้ยืนยันได้ใน capture นี้ จึงติด `*` ทุกค่า SCHF

| ปี | SCHF total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | 3.05%* | 11.96% |
| 2017 | 26.01%* | 21.83% |
| 2018 | -14.26%* | -4.38% |
| 2019 | 22.23%* | 31.49% |
| 2020 | 9.48%* | 18.40% |
| 2021 | 11.40%* | 28.71% |
| 2022 | -14.79%* | -18.11% |
| 2023 | 18.34%* | 26.29% |
| 2024 | 3.28%* | 25.02% |
| 2025 | 34.54%* | 17.88% |

**Up years / Down years**

- Best proxy year: 2025, **+34.54%***
- Least positive proxy year: 2016, **+3.05%***
- Worst proxy year: 2022, **-14.79%***
- Least bad proxy down year: 2018, **-14.26%***
- Official current YTD: **+15.26% NAV**, as of **2026-07-31**
- SCHF proxy beat the S&P 500 common reference in 2017, 2022, and 2025 (`3 / 10` complete years); this arithmetic comparison is not a manager-skill claim

## Risk read-through

SCHF ให้ large- และ mid-cap exposure ใน developed countries นอกสหรัฐฯ โดย
official Schwab snapshot ณ 2026-08-28 แสดง NAV `USD 28.40`, total net assets
`USD 69.68bn`, holdings `1,494`, turnover `3.90%` ณ 2026-07-31, P/E `16.70x`,
P/B `2.26x`, 3-year standard deviation `14.53%`, 30-day SEC yield `2.08%`, และ
distribution yield `3.05%`. Total expense ratio คือ `0.030%`; exchange คือ NYSE
Arca และ management style เป็น passive.

Schwab ระบุความเสี่ยงจาก foreign markets, currency fluctuations, accounting
standards, geopolitical risk, foreign taxes/regulation, illiquid markets และ
large-/mid-cap cycle. Official daily NAV Total Return series ที่เปิดเผยเพียงพอ
สำหรับคำนวณ maximum drawdown และ recovery ยัง `ไม่พบข้อมูลที่ยืนยันได้`; จึงไม่
แทนที่ด้วย market-price หรือ secondary drawdown proxy. ความต่างระหว่าง official
NAV YTD `15.26%` กับ market-price YTD `14.79%` ย้ำว่าต้องแยก investor price
experience ออกจาก NAV evaluation.

## Sources

- [Schwab SCHF product page](https://www.schwabassetmanagement.com/products/schf) — identity, exchange, inception, passive style, current NAV/assets/holdings, official rolling/YTD NAV and market-price returns, benchmark, expense, valuation and standard deviation
- [Schwab SCHF documents](https://www.schwabassetmanagement.com/products/schf/documents) — fund-document and NAV-history access point
- [SEC SCHF summary prospectus](https://www.sec.gov/Archives/edgar/data/1454889/000110465926020707/tm266454-7_497k.htm) — index objective, sampling, derivatives/cash handling and risks
- [FinanceCharts SCHF performance](https://www.financecharts.com/etfs/SCHF/performance) — secondary dividend-reinvested annual total-return proxy; not substituted for official NAV TR
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common USD total-return benchmark for 2016-2025
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
