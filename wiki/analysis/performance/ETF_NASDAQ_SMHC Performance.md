---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:SMHC
ticker: SMHC
exchange: Nasdaq
fund: VanEck China Semiconductor ETF
tracked_index: MarketVector China Semiconductor 25 Index (MVSMHCTR)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-07-20
current_ytd_as_of: not disclosed
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/SMHC
  - geography/China
---

# SMHC Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

SMHC เป็น passive/index-tracking equity ETF ที่เพิ่งเริ่มกองทุนเมื่อ `2026-06-23` จึงไม่มี 10-year NAV Total Return. หน้า official ของ VanEck ที่ตรวจสอบยังแสดง fund NAV/market-price performance เป็น `--` และยังไม่เปิดเผย current NAV YTD; จึงไม่สร้าง proxy จากผลตอบแทนของ underlying index (`+20.18%` 1-month) และไม่คำนวณ CAGR เองจากข้อมูลที่ไม่มีจุดปลายทาง.

## Performance check

- entity_key: `Nasdaq:SMHC`
- Fund: VanEck China Semiconductor ETF
- Inception: `2026-06-23`
- Tracked index: MarketVector China Semiconductor 25 Index (`MVSMHCTR`)
- Metric: NAV Total Return including reinvested distributions and fund expenses
- 10-year NAV TR: unavailable; fund history is under 10 years
- Available-period window reviewed: `2026-06-23` to `2026-07-20`, `27 days / 0.073973 years`
- Start NAV TR value: not disclosed
- End NAV TR value: not disclosed
- Available-period cumulative return: not disclosed
- Available-period CAGR: not disclosed
- Current NAV TR YTD: not disclosed
- Official performance table: SMHC fund NAV and market-price rows are `--`; the underlying-index 1-month result is not an ETF NAV TR result

| Period | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016-2025 | not applicable; fund had not launched | 11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88% |
| 2026 YTD | not disclosed | not comparable; 2026 is outside the cached 2016-2025 benchmark window |

S&P 500 rows are the cached USD Total Return convention for complete calendar years `2016-2025`; they are shown only as a common reference and do not fill the missing SMHC NAV TR fields.

## Up years / Down years

- Up years / Down years: not disclosed; no complete SMHC calendar-year NAV TR table
- Best: not disclosed
- Least positive: not disclosed
- Worst: not disclosed
- Least bad down year: not disclosed

## Risk read-through

SMHC ให้ exposure แบบ concentrated ไปยังบริษัท semiconductor จีน 25 บริษัท. ความเสี่ยงหลักคือ China/semiconductor sector concentration, policy and export-control changes, geopolitics, FX, liquidity และความเสี่ยงของกองทุนใหม่ที่ยังไม่มีประวัติ NAV TR เพียงพอ. Expense ratio ตาม official fund profile คือ `0.65%`.

## Sources

- [VanEck SMHC official product/performance page](https://www.vaneck.com/us/en/investments/china-semiconductor-etf-smhc/)
- [VanEck SMHC launch release](https://www.vaneck.com/us/en/press-releases/vaneck-launches-smhc-offering-pure-play-access-to-chinas-semiconductor-build-out/)
- [VanEck SMHC Q&A](https://www.vaneck.com/us/en/blogs/thematic-investing/smhc-etf-question-answer/)
- [VanEck SMHC fund profile](https://www.vaneck.com/us/en/investments/china-semiconductor-etf-smhc/smhc-chinas-race-to-the-future-fund-profile.pdf)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
