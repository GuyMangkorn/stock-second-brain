---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:SMHC
ticker: SMHC
exchange: Nasdaq
fund: VanEck China Semiconductor ETF
tracked_index: MarketVector China Semiconductor 25 Index (MVSMHCTR)
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2026-08-27
current_ytd_as_of: not disclosed
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/SMHC
  - geography/China
---

# SMHC Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

SMHC เป็น passive/index-tracking equity ETF ที่เพิ่งเริ่มกองทุนเมื่อ `2026-06-23`
จึงไม่มี 10-year NAV Total Return. Official VanEck summary ณ `2026-08-27`
แสดง NAV `US$47.82` และ performance since inception `-18.83%` แบบ cumulative
สำหรับช่วงที่ยังไม่ครบหนึ่งปี; current YTD ยังเป็น `--`. Detailed performance
table มี duplicate blocks ที่ให้ค่าขัดแย้งและไม่ระบุ as-of ชัดเจน จึงเลือกใช้
summary field ที่มีวันที่กำกับและเก็บ conflict ไว้; ไม่ annualize และไม่ใช้
underlying-index return หรือ secondary proxy แทน NAV TR.

## Performance check

- entity_key: `Nasdaq:SMHC`
- Fund: VanEck China Semiconductor ETF
- Inception: `2026-06-23`
- Tracked index: MarketVector China Semiconductor 25 Index (`MVSMHCTR`)
- Metric: NAV Total Return including reinvested distributions and fund expenses
- 10-year NAV TR: unavailable; fund history is under 10 years
- Available-period window reviewed: `2026-06-23` to `2026-08-27`, `65 days / 0.17796 years`
- Start NAV TR value: not disclosed
- End NAV TR value: not disclosed
- Available-period cumulative return: `-18.83%` (official VanEck summary field; not annualized)
- Available-period CAGR: not applicable; period is under one year
- Current NAV: `US$47.82` as of `2026-08-27`
- Total net assets: `US$26.30M` as of `2026-08-27`
- Holdings: `27` as of `2026-08-27`
- Current NAV TR YTD: not disclosed
- Official performance table: YTD and most detailed NAV/market-price rows are `--`; a duplicate table block contains conflicting/unlabeled values and is not used for the current metric

| Period | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016-2025 | not applicable; fund had not launched | 11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88% |
| 2026 YTD | not disclosed | not comparable; 2026 is outside the cached 2016-2025 benchmark window |

S&P 500 rows are the cached USD Total Return convention for complete calendar years `2016-2025`; they are shown only as a common reference and do not fill the missing SMHC NAV TR fields.

The official available-period summary field is `-18.83%` from `2026-06-23` to
`2026-08-27`; it is not a calendar-year or current-YTD figure and is not
annualized. The detailed page capture also shows a conflicting duplicate block
with values such as `-23.14%` and `15.61%` for life performance without a clear
matching as-of label; those values are excluded from the owner metric.

## Up years / Down years

- Up years / Down years: not disclosed; no complete SMHC calendar-year NAV TR table
- Best: not disclosed
- Least positive: not disclosed
- Worst: not disclosed
- Least bad down year: not disclosed

## Risk read-through

SMHC ให้ exposure แบบ concentrated ไปยังบริษัท semiconductor จีน 25 บริษัท;
official current holdings page แสดง `27` holdings ณ 2026-08-27 และ currency
exposure เป็น Chinese Renminbi `64.58%` / Other-Cash `35.42%` ณ 2026-07-31.
ความเสี่ยงหลักคือ China/semiconductor sector concentration, policy and
export-control changes, geopolitics, FX, Stock Connect, liquidity และความเสี่ยง
ของกองทุนใหม่. SEC ระบุว่า fund ใช้ passive approach, normally ลงทุนอย่างน้อย
80% ใน benchmark securities และเป็น non-diversified fund. Expense ratio ตาม
current official profile คือ `0.65%`.

## Sources

- [VanEck SMHC official product/performance page](https://www.vaneck.com/us/en/investments/china-semiconductor-etf-smhc/overview/)
- [VanEck SMHC launch release](https://www.vaneck.com/us/en/press-releases/vaneck-launches-smhc-offering-pure-play-access-to-chinas-semiconductor-build-out/)
- [VanEck SMHC Q&A](https://www.vaneck.com/us/en/blogs/thematic-investing/smhc-etf-question-answer/)
- [VanEck SMHC fund profile](https://www.vaneck.com/us/en/investments/china-semiconductor-etf-smhc/smhc-chinas-race-to-the-future-fund-profile.pdf)
- [SEC SMHC summary prospectus](https://www.sec.gov/Archives/edgar/data/1137360/000113736026000629/vaneckchinasemiconductoret.htm)
- [SEC SMHC statement of additional information](https://www.sec.gov/Archives/edgar/data/1137360/000113736026000630/veconsolsai485b062026.htm)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
