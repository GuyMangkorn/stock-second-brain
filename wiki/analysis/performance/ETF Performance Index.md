---
type: etf-performance-index
scope: expanded
updated: 2026-07-14
canonical_window: 2021-2025
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - analysis/index
---

# ETF Performance Index

หน้ารวมสำหรับเลือก ETF และเทียบ behavior. อ่านหน้า ETF รายตัวเพื่อดู annual
table และ driver notes; อ่านหน้านี้เมื่อต้องการ cross-ETF analysis.

## Coverage

| ETF | History used | 10Y NAV CAGR | 2021-2025 CAGR | 2026 YTD | Best / Worst in window | Structural | Behavioral |
|---|---|---:|---:|---:|---|---|---|
| [[ETF_AMEX_DGRO]] | 2014* / official 2021-2025 | 13.38% | 11.69% | 10.22% | 2021 +26.56% / 2022 -7.85% | U.S. dividend growth | quality/large-cap, moderate downside |
| [[ETF_AMEX_VIG]] | 2006* / official 2011-2025 | 13.13% | 11.27% | 7.19% | 2021 +23.64% / 2022 -9.79% | U.S. dividend growth | quality/large-cap, relatively defensive |
| [[ETF_NASDAQ_VIGI]] | 2016† / official 2017-2025 | 8.13% | 5.46% | 4.64% | 2025 +16.89% / 2022 -16.71% | international dividend growth | FX/country-sensitive, higher downside |
| [[ETF_AMEX_DIVI Performance]] | official rolling as of 2026-06-30; calendar 2017-2025 | 11.24% | 13.59% | 11.38% | 2025 +34.51% / 2022 -1.74% | international value/dividend tilt | lower beta, value/financials/FX-sensitive |
| [[ETF_NYSE_ARCA_EWC Performance]] | official 1996 / official 2016-2025 | 11.25% | 14.11% | 8.78% | 2025 +36.03% / 2018 -17.20% | Canada single-country equity | financials/energy/materials concentrated, country/commodity/FX-sensitive |
| [[ETF_NYSE_ARCA_FLCA Performance]] | official 2017 / official 2018-2025 | not applicable (<10y history) | 14.70% | 8.17% | 2025 +34.90% / 2018 -15.80% | Canada single-country equity | financials/energy/materials concentrated, country/commodity/FX-sensitive |
| [[ETF_AMEX_DTD Performance]] | official 2006 / official 2016-2025 | 12.06% | 12.69% | 10.80% | 2021 +26.14% / 2022 -3.81% | U.S. all-cap dividend | broad dividend/value tilt, still equity-risk sensitive |
| [[ETF_AMEX_FVD Performance]] | official 2003 / official 2016-2025 | 8.40% | 7.95% | 5.76% | 2021 +24.86% / 2022 -5.24% | U.S. value/dividend income | utilities/financials tilt, equity-risk sensitive |
| [[ETF_NYSE_ARCA_VOO Performance]] | official 2010 / official 2016-2025 | 15.47% | 14.38% | 9.97% | 2019 +31.46% / 2022 -18.15% | U.S. large-cap broad equity | S&P 500 market beta, mega-cap sensitive |
| [[ETF_NASDAQ_OPPJ Performance]] | 2013 / official 2016-2024, secondary 2025* | 17.89% | 21.87%* | 24.67% | 2023 +36.69% / 2018 -17.82% | Japan opportunities, dynamic FX hedge | single-country/concentration; strategy break mid-2025 |

10Y NAV CAGR เป็น rolling average annual return จาก official issuer และแต่ละกองมี
as-of date ต่างกัน; DIVI ใช้ Franklin factsheet ณ 2026-06-30 และ raw TR endpoints
ไม่เปิดเผย. TDV และ FLCA ไม่มี 10-year CAGR เพราะประวัติกองยังไม่ครบ 10 ปี.
2026 YTD เป็น partial period และแต่ละกองมี performance as-of date ต่างกัน. `*`
คือ secondary proxy; `†` คือ official inception-year partial.

## Common Window

| ETF | 2021 | 2022 | 2023 | 2024 | 2025 | Cumulative | Positive / Negative |
|---|---:|---:|---:|---:|---:|---:|---:|
| [[ETF_AMEX_DGRO Performance]] | 26.56% | -7.85% | 10.43% | 16.61% | 15.74% | 73.82% | 4 / 1 |
| [[ETF_AMEX_VIG Performance]] | 23.64% | -9.79% | 14.46% | 17.02% | 14.18% | 70.58% | 4 / 1 |
| [[ETF_NASDAQ_VIGI Performance]] | 12.42% | -16.71% | 16.16% | 2.62% | 16.89% | 30.47% | 4 / 1 |
| [[ETF_AMEX_DIVI Performance]] | 17.22% | -1.74% | 19.23% | 2.36% | 34.51% | 89.08% | 4 / 1 |
| [[ETF_NYSE_ARCA_EWC Performance]] | 26.74% | -12.77% | 14.62% | 12.25% | 36.03% | 93.49% | 4 / 1 |
| [[ETF_NYSE_ARCA_FLCA Performance]] | 29.10% | -11.95% | 15.23% | 12.36% | 34.90% | 98.54% | 4 / 1 |
| [[ETF_AMEX_DTD Performance]] | 26.14% | -3.81% | 10.44% | 18.75% | 14.22% | 81.75% | 4 / 1 |
| [[ETF_AMEX_FVD Performance]] | 24.86% | -5.24% | 4.10% | 10.00% | 8.19% | 46.58% | 4 / 1 |
| [[ETF_NYSE_ARCA_VOO Performance]] | 28.66% | -18.15% | 26.25% | 24.98% | 17.84% | 95.81% | 4 / 1 |
| [[ETF_NASDAQ_OPPJ Performance]] | 11.98% | 6.84% | 36.69% | 20.68% | 36.20%* | 168.80%* | 5 / 0 |
| S&P 500 Total Return | 28.71% | -18.11% | 26.29% | 25.02% | 17.88% | 96.17% | 4 / 1 |

S&P 500 row uses the cached USD Total Return convention with dividends
reinvested, reference as-of `2025-12-31`; it is a common reference benchmark,
not the tracked index of every ETF.

OPPJ `2025*` เป็น secondary standardized NAV return; common window ของ OPPJ
ยังคร่อมการเปลี่ยน objective/index เมื่อ 30 มิ.ย. 2025 จึงไม่ใช่ record ของ
current strategy แบบต่อเนื่องห้าปี.

## Regime read

| Regime / question | Read-through |
|---|---|
| 2022 rate-hike shock | VIGI แย่สุด; DGRO/VIG มี quality cushion; DIVI ใกล้ flat จาก value/financials/ex-North-America mix |
| 2020 COVID drawdown | Secondary drawdown: DGRO -35.10%, VIG -31.72%, VIGI -31.01%, DIVI -27.76%; ทุกกองยังมี equity risk |
| 2025 rebound | DIVI นำที่ +34.51%; VIGI +16.89%; DGRO +15.74%; VIG +14.18% สอดคล้องกับ international/value leadership แต่ยังเป็น hypothesis |
| OPPJ continuity | 2025 +36.20%* และ 2026 YTD +24.67% แข็งแรง แต่ปี 2025 ผสม predecessor/current strategy; ห้าม extrapolate rolling 10Y เป็น current-strategy history |
| Portfolio grouping | U.S. quality = DGRO/VIG; international growth = VIGI; international value/dividend = DIVI; Canada single-country = EWC/FLCA |

**สรุปสั้น:** DIVI ชนะใน common window แต่ไม่ควรถูกตีความว่า defensive อัตโนมัติ.
DGRO และ VIG เป็น U.S. quality core ที่ behavior ใกล้กัน. VIGI เพิ่ม geographic
diversification แต่แลกกับ FX/country sensitivity และผลตอบแทนช่วงนี้ต่ำกว่า. FVD
เพิ่ม U.S. value/dividend income exposure แต่มี utilities และ financials tilt.

## Sources

- รายละเอียดรายกอง: [[ETF_AMEX_DGRO Performance]], [[ETF_AMEX_VIG Performance]],
  [[ETF_NASDAQ_VIGI Performance]], [[ETF_AMEX_DIVI Performance]],
  [[ETF_NYSE_ARCA_EWC Performance]], [[ETF_AMEX_DTD Performance]],
  [[ETF_AMEX_FVD Performance]], [[ETF_NYSE_ARCA_VOO Performance]],
  [[ETF_NASDAQ_OPPJ Performance]]
- Source batch: [[ETF_performance_sources_2026-07-14]] | [[ETF_performance_sources_2026-07-13]] | [[ETF_performance_sources_2026-07-12]]
- [Federal Reserve 2022 FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20221214a.htm)
- [Federal Reserve 2020 FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20200315a.htm)

## Preliminary Holdings Groups Batch

เพิ่ม `check-etf-performance` สำหรับ 37 passive equity ETFs ที่ยังไม่เคยตรวจใน
[[Dividend ETF Top 10 Holdings Tracker 2026-07-01]]. `QDPL` และ `MDIV` ถูกตัดออก
ตาม guardrail เพราะ derivative-heavy และ multi-asset ตามลำดับ.

| ETF | 10Y NAV CAGR | 2021-2025 CAGR | Worst year | Avg positive year | 2026 YTD | Coverage |
|---|---:|---:|---:|---:|---:|---|
| [[ETF_AMEX_DEM Performance]] | 9.78% | 8.97% | -10.32% | 14.60% | 15.75% | official 2021-2025 |
| [[ETF_AMEX_DES Performance]] | 8.55% | 7.65% | -10.94% | 13.29% | 22.71% | official 2021-2025 |
| [[ETF_AMEX_DFJ Performance]] | 9.13% | 8.57% | -8.65% | 14.06% | 10.98% | official 2021-2025 |
| [[ETF_AMEX_DGS Performance]] | 9.57% | 8.23% | -12.15% | 14.26% | 14.19% | official 2021-2025 |
| [[ETF_AMEX_DHS Performance]] | 9.44% | 12.05% | -0.19% | 15.47% | 13.44% | official 2021-2025 |
| [[ETF_AMEX_DLN Performance]] | 12.53% | 12.92% | -3.79% | 17.67% | 10.41% | official 2021-2025 |
| [[ETF_AMEX_DLS Performance]] | 8.11% | 7.97% | -17.36% | 15.95% | 5.23% | official 2021-2025 |
| [[ETF_AMEX_DON Performance]] | 9.36% | 10.88% | -4.76% | 15.55% | 10.79% | official 2021-2025 |
| [[ETF_AMEX_DTH Performance]] | 9.06% | 12.22% | -2.12% | 17.06% | 8.21% | official 2021-2025 |
| [[ETF_AMEX_DWM Performance]] | 8.94% | 10.46% | -9.11% | 16.49% | 8.10% | official 2021-2025 |
| [[ETF_CBOE_DDWM Performance]] | 10.72% | 13.41% | -1.27% | 17.63% | 7.65% | official 2021-2025 |
| [[ETF_CBOE_DDLS Performance]] | 10.18% | 11.33% | -9.79% | 17.55% | 4.48% | 2025 secondary*; other years official |
| [[ETF_AMEX_DJD Performance]] | 11.89% | 11.83% | -0.61% | 15.28% | ไม่พบข้อมูลที่ยืนยันได้ | official 2021-2025 |
| [[ETF_NASDAQ_PEY Performance]] | 8.83% | 7.96% | ไม่พบข้อมูลที่ยืนยันได้ | 8.33% | 13.25% | official 2021-2025 |
| [[ETF_NASDAQ_PFM Performance]] | 11.83% | 11.36% | -6.23% | 16.34% | 7.99% | official 2021-2025 |
| [[ETF_NASDAQ_PID Performance]] | 8.81% | 11.28% | -6.36% | 16.54% | 2.05% | official 2021-2025 |
| [[ETF_AMEX_VYM Performance]] | 11.61% | 12.68% | -0.42% | 16.42% | 11.49% | official 2021-2025 |
| [[ETF_NASDAQ_VYMI Performance]] | 10.73% | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | 38.06% | 12.31% | official rolling; calendar gap |
| [[ETF_CBOE_NOBL Performance]] | 9.62% | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | 3.62% | official rolling; calendar gap |
| [[ETF_CBOE_REGL Performance]] | 9.58% | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | 5.13% | official rolling; calendar gap |
| [[ETF_CBOE_SMDV Performance]] | 7.15% | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | 10.38% | official rolling; calendar gap |
| [[ETF_CBOE_TDV Performance]] | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | 20.77% | official rolling; calendar gap |
| [[ETF_AMEX_SPYD Performance]] | 8.81% | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | 10.99% | official rolling; calendar gap |
| [[ETF_AMEX_SDY Performance]] | 9.37% | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | 10.77% | official rolling; calendar gap |
| [[ETF_AMEX_WDIV Performance]] | 7.47% | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | 8.09% | official rolling; calendar gap |
| [[ETF_AMEX_DWX Performance]] | 7.44% | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | 6.97% | official rolling; calendar gap |
| [[ETF_AMEX_AMLP Performance]] | 8.22% | 22.43% | ไม่พบข้อมูลที่ยืนยันได้ | 22.90% | 14.86% | official 2021-2025 |
| [[ETF_AMEX_ENFR Performance]] | 13.40% | 23.39% | ไม่พบข้อมูลที่ยืนยันได้ | 24.19% | 23.50% | official 2021-2025 |
| [[ETF_AMEX_IDOG Performance]] | 10.38% | 13.18% | -4.23% | 18.84% | 10.58% | official 2021-2025 |
| [[ETF_AMEX_SDOG Performance]] | 9.38% | 10.52% | -0.13% | 13.60% | 13.99% | official 2021-2025 |
| [[ETF_AMEX_SDIV Performance]] | 0.13% | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | ไม่พบข้อมูลที่ยืนยันได้ | 5.50% | official rolling; calendar gap |
| [[ETF_NASDAQ_KBWD Performance]] | 5.92% | 7.14% | -18.99% | 15.44% | ไม่พบข้อมูลที่ยืนยันได้ | official 2021-2025 |
| [[ETF_NASDAQ_KBWY Performance]] | 0.99% | 1.85% | -18.90% | 21.94% | 1.51% | official 2021-2025 |
| [[ETF_AMEX_FDD Performance]] | 9.11% | 13.02% | -2.64% | 19.61% | ไม่พบข้อมูลที่ยืนยันได้ | official 2021-2025 |
| [[ETF_NASDAQ_TDIV Performance]] | 18.22% | 16.55% | -22.14% | 29.01% | 19.52% | official 2021-2025 |
| [[ETF_NASDAQ_DVY Performance]] | 10.11% | 11.96% | ไม่พบข้อมูลที่ยืนยันได้ | 12.49% | 12.48% | official 2021-2025 |
| [[ETF_CBOE_IDV Performance]] | 10.01% | 12.77% | -6.75% | 19.60% | 4.25% | official 2021-2025 |

### Cross-fund read

- `TDIV` มี official 2016-2025 NAV TR CAGR `16.87%` สูงกว่า S&P 500 TR `14.82%`,
  แต่ 2022 ลด `-22.14%` แย่กว่า S&P 500 `-18.11%` จึงไม่ใช่ downside winner.
- `DJD` ให้ balance เด่นสุด: 2016-2025 CAGR `11.89%`, worst calendar yearเพียง
  `-0.61%`, และ 2021-2025 CAGR `11.82%`; upside ต่ำกว่า S&P แต่ downside control เด่น.
- `ENFR` นำช่วง 2021-2025 ที่ CAGR `23.39%` และไม่มีปีติดลบ แต่เป็น concentrated
  midstream-energy regime result; rolling 10Y `13.40%` ยังต่ำกว่า S&P 500 TR `14.16%`
  ใน issuer comparison as of 2026-03-31.
- `DLN` เด่นสุดใน broad U.S. dividend subset: official rolling 10Y `12.53%`,
  common-window 2021-2025 CAGR `12.92%`, worst year `-3.79%`.

การสรุป “บริหารกองทุนดี” ต้องตีความเป็น index methodology + tracking + cost control
เพราะกองทั้งหมดใน ranking นี้เป็น passive ไม่ใช่ discretionary active management.
