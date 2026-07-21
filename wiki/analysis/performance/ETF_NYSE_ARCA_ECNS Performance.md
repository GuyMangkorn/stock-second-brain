---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:ECNS
ticker: ECNS
exchange: NYSE Arca
fund: iShares MSCI China Small-Cap ETF
tracked_index: MSCI China Small Cap Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-18
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-16
price_nav_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-18.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/ECNS
  - geography/China
  - style/small-cap
---

# ECNS Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

ECNS ไม่ได้ลงทุกปี: ปี 2025 NAV Total Return เด้ง `+36.42%`; แต่ช่วง official
2021-2025 ยังสะสม `-13.19%` หรือ CAGR `-2.79%` และ current YTD 2026 อยู่ที่
`-10.26%` ณ 16 ก.ค. 2026. ล่าสุด NAV อยู่ที่ `$28.18` และลด `-3.45%` ในวันที่
17 ก.ค.; ราคาปิด `$28.20` ต่ำกว่าจุดสูงสุด 52 สัปดาห์ `$39.84` ราว `-29.22%`
(คำนวณจากข้อมูล issuer). สาเหตุหลักคือ China small-cap risk ไม่ใช่ความผิดพลาดของ
ETF: หุ้นจีนทั้งตลาดถูกขาย และ small-cap มี volatility/liquidity risk สูงกว่า.

## Performance check

- `entity_key: NYSE Arca:ECNS`
- Fund: iShares MSCI China Small-Cap ETF; inception `28 ก.ย. 2010`; expense ratio
  `0.59%`
- Metric: `NAV Total Return` รวม distributions reinvested และหัก fund expenses
- Tracked index (issuer benchmark): `MSCI China Small Cap Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ ECNS)
- 10-year NAV TR CAGR: `1.05%` ณ 30 มิ.ย. 2026; issuer ไม่เปิดเผย raw start/end
  TR values จึงแสดงได้เฉพาะ annualized result ของกอง ไม่คำนวณ endpoint ซ้ำ
- Current NAV: `$28.18` ณ 17 ก.ค. 2026; 1-day NAV change `-3.45%`
- Annual coverage: official complete calendar years 2021-2025; ไม่มี partial-year
  marker ในตาราง

| ปี | ECNS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 3.10% | 28.71% |
| 2022 | -24.77% | -18.11% |
| 2023 | -23.28% | 26.29% |
| 2024 | 6.94% | 25.02% |
| 2025 | 36.42% | 17.88% |

S&P 500 rows ใช้ cached USD Total Return convention, dividends reinvested,
reference as-of `2025-12-31`. ECNS 2021-2025 cumulative/CAGR คือ `-13.19%` /
`-2.79%`; S&P 500 TR คือ `96.17%` / `14.43%`.

## Up years / Down years

- Up years / Down years: `3 / 2` ใน 2021-2025
- Best: 2025, `+36.42%`
- Least positive: 2021, `+3.10%`
- Worst: 2022, `-24.77%`
- Least bad down year: 2023, `-23.28%`
- Current YTD: `-10.26%` NAV ณ 16 ก.ค. 2026; issuer's 1-day NAV snapshot ณ
  17 ก.ค. 2026 คือ `-3.45%`

## Risk read-through

ECNS เป็น passive China small-cap equity ETF ไม่ใช่ China internet ETF โดยตรง.
ความผันผวน 3 ปีอยู่ที่ `26.43%` เทียบกับ broad China ETF อย่าง MCHI ที่ `21.99%`
(ทั้งคู่ ณ 30 มิ.ย. 2026); portfolio มี 266 holdings, P/E `11.31x`, P/B `0.88x`
และ sector ใหญ่คือ Health Care `22.98%`, Industrials `14.12%`, Information
Technology `11.41%`, Consumer Discretionary `10.93%`, Real Estate `8.54%` และ
Materials `8.49%` ณ 16 ก.ค. 2026. จึงรับแรงจาก domestic demand, property และ
financing conditions มากกว่าการมองว่าเป็น pure technology bet.

## Why recent weakness persists

- `confirmed event` / high confidence: วันที่ 17 ก.ค. 2026 เป็น China/Hong Kong
  risk-off session; Hang Seng ลด `2.0%`, Hang Seng China Enterprises `2.4%` และ
  Hang Seng TECH `4.0%`. ECNS NAV ลด `3.45%` ในวันเดียวกัน จึงเป็นการเคลื่อนไหว
  ตามตลาด ไม่ใช่หลักฐานของ fund-specific event.
- `probable driver` / medium-high confidence: ข้อมูลเศรษฐกิจจีน Q2 โต `4.3%`,
  ต่ำสุดนับจาก Q4 2022; domestic spending/investment ยังอ่อน, fixed-asset
  investment ครึ่งปีแรกลด `5.7%`, retail sales โตเพียง `1.3%` และราคาบ้านยังลดลง.
  นี่เป็นแรงกดต่อ small-cap ที่พึ่งพาเศรษฐกิจในประเทศมากกว่า mega-cap; เป็น
  inference จาก macro data + portfolio exposure ไม่ใช่การพิสูจน์เหตุของทุกวันลง.
- `probable driver` / medium confidence: small-cap มี volatility และ liquidity
  risk สูงกว่า. อย่างไรก็ดี price `$28.20` เทียบ NAV `$28.18` และ premium/discount
  เพียง `0.08%` ณ 17 ก.ค. จึงไม่มีหลักฐานว่า ETF discount เป็นตัวขับหลัก.
- Distribution note: ECNS จ่าย `$0.453779` ต่อหุ้นใน ex-date 15 มิ.ย. 2026;
  ราคาอาจปรับลงเชิงกลราว `1.61%` จากการตัดเงินปันผล แต่ NAV Total Return รวมเงิน
  ปันผลแล้ว จึงไม่ควรนับเป็นขาดทุนซ้ำ.

สิ่งที่ต้องติดตามคือการฟื้นของ retail/property และการหยุดทำจุดต่ำใหม่ของ MSCI China
Small Cap; ถ้า broad China และ small-cap ยัง underperform ต่อ คำอธิบายเรื่อง
China risk-premium จะยังแข็งแรง. Official daily NAV TR series สำหรับคำนวณ maximum
drawdown/recovery โดยตรง: `ไม่พบข้อมูลที่ยืนยันได้`; ตัวเลข `-29.22%` ด้านบนเป็น
การเทียบราคาปัจจุบันกับ 52-week high ไม่ใช่ official maximum drawdown.

## Sources

- [iShares ECNS product page](https://www.ishares.com/us/products/239620/ishares-msci-china-smallcap-etf) — current NAV/price, YTD NAV TR, exchange, benchmark, inception, holdings, sector exposure, premium/discount, distributions and fees
- [Official ECNS factsheet](https://www.ishares.com/us/literature/fact-sheet/ecns-ishares-msci-china-small-cap-etf-fund-fact-sheet-en-us.pdf) — official annual NAV TR 2021-2025, return definition, standardized performance and risk facts as of 2026-03-31
- [AP: China economy slows to 4.3% in Q2 2026](https://apnews.com/article/china-economy-trade-exports-ai-95136222f87d5a1e62918f41efab00be) — latest macro data and domestic-demand/property context
- [ET Net: Hong Kong market close 17 Jul 2026](https://www.etnet.com.hk/www/eng/futures/futures_news_detail.php?newsid=20260717190) — same-session Hang Seng, China Enterprises and Hang Seng TECH moves
- [S&P 500 official returns page](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=76d0e321-60b6-4834-a4b7-68bbe72fd4ea&sourceIdentifier=index-family-specialization) — current S&P 500 TR YTD cross-check as of 2026-07-18
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index identity and methodology; annual 2021-2025 rows reuse cached skill convention
- [[ETF_performance_sources_2026-07-18]] | [[ETF Performance Index]]
