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

นี่คือ dashboard สำหรับ performance coverage ของ ETF ใน vault. ตัวเลขใน
`Common Window` ใช้ official NAV total return และไม่รวม 2026 YTD เพราะยังเป็น
partial period. Monthly behavior และ drawdown ใช้ secondary context ตามที่ระบุ
ในแต่ละ normalized file.

## Pilot Coverage

| ETF | Performance note | Normalized data | Official calendar coverage | 2021-2025 CAGR | 2026 YTD (partial) | Best year in common window | Worst year in common window | Structural group | Behavioral read |
|---|---|---|---|---:|---:|---:|---:|---|---|
| [[ETF_AMEX_DGRO]] | [[ETF_AMEX_DGRO Performance]] | [[ETF_AMEX_DGRO_performance]] | 2021-2025; secondary extension 2014-2020 | 11.69% | 10.22% | 2021 +26.56% | 2022 -7.85% | U.S. dividend growth | quality/large-cap, moderate downside |
| [[ETF_AMEX_VIG]] | [[ETF_AMEX_VIG Performance]] | [[ETF_AMEX_VIG_performance]] | 2011-2025; secondary extension 2007-2010 | 11.27% | 7.19% | 2021 +23.64% | 2022 -9.79% | U.S. dividend growth | quality/large-cap, defensive relative to broad equity |
| [[ETF_NASDAQ_VIGI]] | [[ETF_NASDAQ_VIGI Performance]] | [[ETF_NASDAQ_VIGI_performance]] | 2017-2025; 2016 partial | 5.46% | 4.12% | 2025 +16.89% | 2022 -16.71% | international dividend growth | FX/country-sensitive, higher downside |
| [[ETF_AMEX_DIVI]] | [[ETF_AMEX_DIVI Performance]] | [[ETF_AMEX_DIVI_performance]] | 2017-2025; 2016 partial | 13.59% | 11.38% | 2025 +34.51% | 2022 -1.74% | international dividend/value tilt | lower beta, value/financials/FX-sensitive |

## Fast Read

- ใน common window `DIVI` มี CAGR สูงสุดและ 2025 เป็นผู้นำ แต่ไม่ได้แปลว่าเป็น
  defensive ทุก regime เพราะ international, FX และ financial-sector exposure ยัง
  เป็นความเสี่ยงหลัก
- `DGRO` และ `VIG` ให้ผลตอบแทนสะสมใกล้กันใน 2021-2025 โดย `DGRO` เสียหายน้อยกว่า
  ใน 2022 แต่ต้องใช้ข้อมูล holdings/methodology ที่เทียบวันเดียวกันก่อนสรุปว่า
  ต่างกันจาก factor ใด
- `VIGI` เป็น international dividend-growth sleeve ที่ผลตอบแทนต่ำกว่าและ
  drawdown สูงกว่าใน common window จึงควรวิเคราะห์เป็น regional diversifier ไม่ใช่
  substitute แบบหนึ่งต่อหนึ่งกับ U.S. dividend-growth ETF

## Navigation

- [[ETF Performance Regime Matrix]]
- [[ETF_AMEX_DGRO Performance]]
- [[ETF_AMEX_VIG Performance]]
- [[ETF_NASDAQ_VIGI Performance]]
- [[ETF_AMEX_DIVI Performance]]
- [[ETF Index]]

## Data Quality

- Canonical annual tables come from official issuer pages/factsheets.
- Monthly behavior and drawdown metrics are secondary dividend-adjusted context.
- A normalized monthly observation series is not yet captured for the pilot.
- 2026 figures are partial and have separate as-of dates across issuers.
