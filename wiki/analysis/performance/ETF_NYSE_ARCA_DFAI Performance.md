---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DFAI
ticker: DFAI
exchange: NYSE Arca
updated: 2026-08-29
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return for official fields; secondary dividend-reinvested proxy for rows marked *
management_mode: active-systematic
active_process_subtype: broad core market with flexible daily implementation
management_benchmark: MSCI World ex USA IMI Index (net dividends)
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/DFAI
---

# DFAI Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DFAI เป็น active transparent/systematic ETF ของ Dimensional ที่ใช้ flexible daily
process และ broad developed-market ex-U.S. exposure ไม่ใช่ passive index fund.
กองทุนเริ่ม 17 พ.ย. 2020 จึงมี track record ต่ำกว่า 10 ปี. Official Quick Guide
ณ 2025-12-31 รายงาน NAV 5-year annualized `10.34%` เทียบกับ management benchmark
`9.03%` หรือ return-only excess `+1.31 pp`; official 1-year อยู่ที่ `33.92%`
เทียบ benchmark `32.18%` หรือ `+1.74 pp`. Calendar rows และ current YTD ในหน้านี้
เป็น secondary proxy* เพราะ reviewed current official capture ไม่แสดง annual/YTD
table ที่อ่านได้ครบ.

## Performance check

- `entity_key: NYSE Arca:DFAI`
- Fund: `Dimensional International Core Equity Market ETF`; inception/listing: 17 พ.ย. 2020 / 18 พ.ย. 2020; asset class: international equity
- Metric: NAV Total Return รวมเงินปันผลและ capital gains ที่ reinvested; official Quick Guide returns are annualized where stated
- Management mode: `active-systematic`; active-process subtype คือ broad core market exposure with flexible daily implementation, research-led portfolio design and trading
- Management benchmark: `MSCI World ex USA IMI Index (net dividends)`
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference ไม่ใช่ management benchmark ของ DFAI)
- Official rolling 10-year NAV TR: `ไม่พบข้อมูลที่ยืนยันได้` เพราะ inception ยังไม่ครบ 10 ปี
- Official 5-year NAV TR: `10.34%` annualized ณ `2025-12-31`; management benchmark `9.03%`; return-only excess `+1.31 pp`
- Official 1-year NAV TR: `33.92%` ณ `2025-12-31`; management benchmark `32.18%`; return-only excess `+1.74 pp`
- Available common window: `2021-2025` secondary proxy compound `63.57%*` / rounded-input CAGR `10.34%*`; S&P 500 cache compound `96.17%` / CAGR `14.43%`
- Current YTD: `15.19%*` secondary dividend-reinvested total-return proxy, captured through late August 2026; current official YTD not disclosed in reviewed Dimensional capture
- Coverage note: annual table เป็น secondary dividend-reinvested proxy จาก FinanceCharts และติด `*`; official Quick Guide 5-year/1-year figures remain separate. ไม่คำนวณ 2016-2020 เพราะ ETF ยังไม่เกิด

| ปี | DFAI total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2021 | 13.86%* | 28.71% |
| 2022 | -12.94%* | -18.11% |
| 2023 | 17.59%* | 26.29% |
| 2024 | 4.69%* | 25.02% |
| 2025 | 34.04%* | 17.88% |

**Up years / Down years — available 2021-2025 proxy window**

- Best proxy year: 2025, **+34.04%***
- Least positive proxy year: 2024, **+4.69%***
- Worst proxy year: 2022, **-12.94%***
- Least bad proxy down year: 2022, **-12.94%***
- Current YTD proxy: **+15.19%***; official current YTD is not disclosed in reviewed Dimensional capture
- DFAI proxy beat the S&P 500 common reference in 2022 and 2025 (`2 / 5` available years); this arithmetic comparison is not evidence of manager skill

## Risk read-through

DFAI ใช้ broad diversification across companies, sectors และ countries ใน
developed markets นอกสหรัฐฯ โดย Dimensional ระบุว่ากระบวนการ active ใช้ research,
portfolio design, portfolio management และ trading ที่ยืดหยุ่นรายวัน พร้อม
emphasis on size, relative price และ profitability drivers. Official summary
prospectus ระบุ objective เป็น long-term capital appreciation, exchange เป็น NYSE
Arca และ expense ratio `0.18%`; 2026 distribution schedule แสดง quarterly
record/ex-date pattern.

Official current AUM, holdings, valuation multiples และ standard-deviation series
ที่ตรวจสอบได้จาก current Dimensional capture ยัง `ไม่พบข้อมูลที่ยืนยันได้`.
Official daily NAV Total Return history ที่เพียงพอสำหรับ maximum drawdown,
recovery และ risk-adjusted skill evidence ก็ยังไม่พบ; จึงไม่แทนที่ด้วย price หรือ
secondary drawdown proxy. Track record maturity คือประมาณห้าปีเต็ม ณ สิ้นปี 2025;
return-only excess บวกใน Quick Guide ยังไม่ใช่ alpha และยังสรุป persistence หรือ
risk-adjusted manager skill ไม่ได้.

## Sources

- [Dimensional DFAI ETF page](https://www.dimensional.com/us-en/funds/dfai/international-core-equity-market-etf) — official product access point and fund identity
- [Dimensional ETF lineup](https://www.dimensional.com/us-en/etfs) — active ETF structure and flexible daily process context
- [Dimensional newsroom listing DFAI](https://www.dimensional.com/us-en/newsroom/dimensional-lists-etfs) — active transparent classification, NYSE Arca listing, inception/listing and 0.18% net expense ratio
- [Dimensional ETF Quick Guide](https://my.dimensional.com/chmedia/282748/source/dimensional-etf-quick-guide.pdf) — official 1-year/5-year NAV and management-benchmark returns as of 2025-12-31
- [SEC DFAI summary prospectus](https://www.sec.gov/Archives/edgar/data/1816125/000181612526000086/c497k.htm) — objective, NYSE Arca listing, strategy and risks
- [FinanceCharts DFAI performance](https://www.financecharts.com/etfs/DFAI/performance) — secondary dividend-reinvested annual/YTD proxy, marked `*`
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common USD total-return benchmark for 2021-2025
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
