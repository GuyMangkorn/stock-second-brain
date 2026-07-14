---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:OPPJ
ticker: OPPJ
updated: 2026-07-14
source_batch: raw/imports/ETF_performance_sources_2026-07-14.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/OPPJ
---

# OPPJ Performance

## Bottom line

OPPJ มีผลตอบแทนเป็นบวก 8 จาก 10 ปีเต็มช่วง 2016-2025; ปีดีที่สุดคือ 2023
ที่ `+36.69%` และแย่ที่สุดคือ 2018 ที่ `-17.82%`. 2026 YTD official NAV Total
Return อยู่ที่ `+24.67%` ณ 30 มิ.ย. 2026. อย่างไรก็ดี กองเปลี่ยนจาก DXJS / Japan
Hedged SmallCap เป็น OPPJ / Japan Opportunities เมื่อ 30 มิ.ย.-1 ก.ค. 2025;
ประวัติระยะยาวจึงเป็น spliced strategy record ไม่ใช่ track record ของกลยุทธ์
ปัจจุบันล้วน ๆ.

## Performance check

- `entity_key: NASDAQ:OPPJ`
- Inception: 28 มิ.ย. 2013; current strategy/ticker effective 1 ก.ค. 2025
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Tracked index (issuer benchmark): WisdomTree Japan Opportunities Index พร้อม
  dynamic JPY/USD hedge 0-100%
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference,
  not OPPJ's tracked index)
- 10-year window: 30 มิ.ย. 2016 ถึง 30 มิ.ย. 2026
- 10-year NAV TR CAGR: `17.89%` (issuer-reported). Issuer ไม่เปิดเผย raw TR
  endpoints; normalized implication คือ `100.00 -> 518.52` จาก
  `100 x (1 + 17.89%)^10`, ไม่ใช่ sourced NAV/TR index levels
- Coverage/source note: 2016-2024 เป็น official SEC annual NAV TR; `2025*` เป็น
  secondary standardized NAV total return, rounded to one decimal. ทุกปีถึง
  2024 และครึ่งแรกของ 2025 สะท้อน predecessor strategy
- `*` คือ secondary dividend-reinvested NAV return ไม่ใช่ annual row จาก issuer

Annual OPPJ rows ปี 2016-2024 มาจาก [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011309/oppj73125497k.htm);
ปี 2025 มาจาก [Schwab standardized ETF report](https://www.schwab.wallst.com/schwab/Prospect/research/etfs/reports/reportRetrieve.asp?reportType=etfrc&symbol=OPPJ):

- Annual NAV TR coverage: 2016-2024 official NAV TR; 2025 secondary proxy*
| ปี | OPPJ TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 6.88% | 11.96% |
| 2017 | 29.46% | 21.83% |
| 2018 | -17.82% | -4.38% |
| 2019 | 18.33% | 31.49% |
| 2020 | -4.64% | 18.40% |
| 2021 | 11.98% | 28.71% |
| 2022 | 6.84% | -18.11% |
| 2023 | 36.69% | 26.29% |
| 2024 | 20.68% | 25.02% |
| 2025* | 36.20% | 17.88% |

**Up years / Down years**

- Best: 2023, **+36.69%**
- Least positive: 2022, **+6.84%**
- Worst: 2018, **-17.82%**
- Least bad down year: 2020, **-4.64%**
- 2026 YTD: **+24.67% NAV**, as of 30 มิ.ย. 2026

## Risk read-through

Official rolling 10-year NAV TR CAGR อยู่ที่ `17.89%`, แต่ช่วงดังกล่าวรวมอดีต
DXJS เกือบทั้งหมด. Annual rows 2016-2025 (รวม secondary 2025*) compound เป็น
`13.18%` CAGR และ cumulative `244.89%`, เทียบ S&P 500 TR cache ที่ `14.82%`
และ `298.33%`. ใน common window 2021-2025 OPPJ ได้ `21.87%*` CAGR แต่กลยุทธ์
เปลี่ยนกลางปีสุดท้าย จึงไม่ใช่ apples-to-apples record ของ OPPJ ปัจจุบัน.

Secondary dividend-adjusted series ระบุ max drawdown `-39.30%` จากจุดสูงสุด
9 ม.ค. 2018 ถึงจุดต่ำสุด 16 มี.ค. 2020 และฟื้น 15 มี.ค. 2021; เป็น adjusted
market-price proxy ไม่ใช่ official NAV. Expense ratio `0.58%` ณ 13 ก.ค. 2026.
กองเป็น passive Japan equity ETF ที่มี single-country, sector/concentration และ
JPY/USD hedge risk; hedge ratio ล่าสุด `0.02%` ณ 13 ก.ค. 2026.

## Sources

- [WisdomTree OPPJ product page](https://www.wisdomtree.com/us/products/equity/oppj)
- [WisdomTree OPPJ factsheet](https://www.wisdomtree.com/us/media/wisdomtree-factsheet-oppj)
- [SEC OPPJ summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011309/oppj73125497k.htm)
- [WisdomTree Japan Opportunities Index](https://www.wisdomtree.com/us/indexes/WTJOP)
- [Schwab OPPJ report](https://www.schwab.wallst.com/schwab/Prospect/research/etfs/reports/reportRetrieve.asp?reportType=etfrc&symbol=OPPJ) — secondary 2025 NAV TR
- [PortfoliosLab OPPJ](https://portfolioslab.com/symbol/OPPJ) — secondary adjusted-price drawdown/recovery
- [[ETF_performance_sources_2026-07-14]] | [[ETF Performance Index]]
