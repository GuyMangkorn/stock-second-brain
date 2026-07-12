---
type: etf-performance-index
scope: pilot
updated: 2026-07-12
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

| ETF | History used | 2021-2025 CAGR | 2026 YTD | Best / Worst in window | Structural | Behavioral |
|---|---|---:|---:|---|---|---|
| [[ETF_AMEX_DGRO]] | 2014* / official 2021-2025 | 11.69% | 10.22% | 2021 +26.56% / 2022 -7.85% | U.S. dividend growth | quality/large-cap, moderate downside |
| [[ETF_AMEX_VIG]] | 2006* / official 2011-2025 | 11.27% | 7.19% | 2021 +23.64% / 2022 -9.79% | U.S. dividend growth | quality/large-cap, relatively defensive |
| [[ETF_NASDAQ_VIGI]] | 2016† / official 2017-2025 | 5.46% | 4.12% | 2025 +16.89% / 2022 -16.71% | international dividend growth | FX/country-sensitive, higher downside |
| [[ETF_AMEX_DIVI]] | official 2017-2025 | 13.59% | 11.38% | 2025 +34.51% / 2022 -1.74% | international value/dividend tilt | lower beta, value/financials/FX-sensitive |
| [[ETF_AMEX_DTD Performance]] | official 2006 / official 2016-2025 | 12.69% | 10.80% | 2021 +26.14% / 2022 -3.81% | U.S. all-cap dividend | broad dividend/value tilt, still equity-risk sensitive |
| [[ETF_AMEX_FVD Performance]] | official 2003 / official 2016-2025 | 7.95% | 5.76% | 2021 +24.86% / 2022 -5.24% | U.S. value/dividend income | utilities/financials tilt, equity-risk sensitive |

2026 YTD เป็น partial period และแต่ละกองมี performance as-of date ต่างกัน. `*`
คือ secondary proxy; `†` คือ official inception-year partial.

## Common Window

| ETF | 2021 | 2022 | 2023 | 2024 | 2025 | Cumulative | Positive / Negative |
|---|---:|---:|---:|---:|---:|---:|---:|
| [[ETF_AMEX_DGRO Performance]] | 26.56% | -7.85% | 10.43% | 16.61% | 15.74% | 73.82% | 4 / 1 |
| [[ETF_AMEX_VIG Performance]] | 23.64% | -9.79% | 14.46% | 17.02% | 14.18% | 70.58% | 4 / 1 |
| [[ETF_NASDAQ_VIGI Performance]] | 12.42% | -16.71% | 16.16% | 2.62% | 16.89% | 30.47% | 4 / 1 |
| [[ETF_AMEX_DIVI Performance]] | 17.22% | -1.74% | 19.23% | 2.36% | 34.51% | 89.08% | 4 / 1 |
| [[ETF_AMEX_DTD Performance]] | 26.14% | -3.81% | 10.44% | 18.75% | 14.22% | 81.75% | 4 / 1 |
| [[ETF_AMEX_FVD Performance]] | 24.86% | -5.24% | 4.10% | 10.00% | 8.19% | 46.58% | 4 / 1 |

## Regime read

| Regime / question | Read-through |
|---|---|
| 2022 rate-hike shock | VIGI แย่สุด; DGRO/VIG มี quality cushion; DIVI ใกล้ flat จาก value/financials/ex-North-America mix |
| 2020 COVID drawdown | Secondary drawdown: DGRO -35.10%, VIG -31.72%, VIGI -31.01%, DIVI -27.76%; ทุกกองยังมี equity risk |
| 2025 rebound | DIVI นำที่ +34.51%; VIGI +16.89%; DGRO +15.74%; VIG +14.18% สอดคล้องกับ international/value leadership แต่ยังเป็น hypothesis |
| Portfolio grouping | U.S. quality = DGRO/VIG; international growth = VIGI; international value/dividend = DIVI |

**สรุปสั้น:** DIVI ชนะใน common window แต่ไม่ควรถูกตีความว่า defensive อัตโนมัติ.
DGRO และ VIG เป็น U.S. quality core ที่ behavior ใกล้กัน. VIGI เพิ่ม geographic
diversification แต่แลกกับ FX/country sensitivity และผลตอบแทนช่วงนี้ต่ำกว่า. FVD
เพิ่ม U.S. value/dividend income exposure แต่มี utilities และ financials tilt.

## Sources

- รายละเอียดรายกอง: [[ETF_AMEX_DGRO Performance]], [[ETF_AMEX_VIG Performance]],
  [[ETF_NASDAQ_VIGI Performance]], [[ETF_AMEX_DIVI Performance]],
  [[ETF_AMEX_DTD Performance]], [[ETF_AMEX_FVD Performance]]
- Source batch: [[ETF_performance_sources_2026-07-12]]
- [Federal Reserve 2022 FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20221214a.htm)
- [Federal Reserve 2020 FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20200315a.htm)
