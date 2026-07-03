---
type: decision-refresh
date: 2026-07-03
scope: covered equities previously researched in vault
source_note: raw/imports/US_covered_equities_market_quote_2026-07-03.md
tags:
  - decision-refresh
  - covered-equities
---

# US Covered Equities Decision Refresh - 2026-07-03

## Action Read

**Bottom line: ยังไม่มีตัวไหนเป็น `CLEAR ADD` แบบ margin of safety ชัดตาม
vault discipline.** ถ้าใช้กติกา strict ว่าราคาต้องต่ำกว่า base-case DCF หรือ
มี source-backed evidence ใหม่ที่ยก fair value ขึ้นอย่างมีนัยสำคัญ คำตอบคือ
**ยังไม่มีหุ้นที่เหมาะจะลงทุนแบบเต็มไม้ทันที**.

แต่ถ้าแยกเป็น decision ที่ใช้งานได้จริง กลุ่มที่ “พอเหมาะสมในการพิจารณา
ลงทุนแบบ selective / staged entry” ตอนนี้คือ **BABA, META, PG, UL, IBM,
VZ** โดย BABA เป็น recovery/speculative candidate, VZ เป็น income-only
candidate, ส่วน META/PG/UL/IBM เป็น quality watchlist ที่ต้องการราคาดีขึ้น
หรือ proof เพิ่มก่อนจะเป็น ADD ที่ชัดกว่า.

| Bucket | Tickers | Read |
|---|---|---|
| Clear ADD today | None | ยังไม่มีราคาที่ให้ base-case margin of safety ชัดพอจาก valuation memos เดิม. |
| Best selective candidates | META, PG, UL, IBM | คุณภาพ/FCF support ดีกว่ากลุ่มส่วนใหญ่ แต่ราคายังสูงกว่า base DCF. เหมาะกับ staged entry เท่านั้น. |
| Speculative / recovery candidate | BABA | ราคาอยู่ใน fair/watch zone เดิม แต่ต้องเห็น FCF recovery ก่อนขยับเป็น ADD จริง. |
| Income-only candidate | VZ | ราคาอยู่ต่ำกว่า bull DCF เดิมและ dividend case อาจใช้ได้สำหรับ income mandate แต่ leverage ยังเป็นตัวล็อก. |
| Thematic watchlist | CEG, VST, UNH, MDT, ABT, CRWD | มีบางมุมที่น่าสนใจหลังเทียบราคาใหม่ แต่ยังไม่ผ่าน margin of safety หรือ source-quality threshold. |

## Current Price / Market Data Check

Market data source: Nasdaq quote API, fetched 2026-07-03 Asia/Bangkok. Nasdaq
reported `marketStatus: Closed`, `isRealTime: false`, and latest available
`lastTradeTimestamp: Jul 1, 2026`. See
`raw/imports/US_covered_equities_market_quote_2026-07-03.md`.

## Decision Ranking

| Rank | Ticker | Current Price | Valuation Anchor | Refresh Decision | Why |
|---:|---|---:|---|---|---|
| 1 | BABA | 96.14 | Base about 88; fair/watch zone 85-110 | SPECULATIVE STAGED WATCHLIST | ราคาอยู่ใน fair/watch zone และ risk/reward ดีกว่าตอน USD 115.38 แต่ FY2026 FCF ยังติดลบ จึงเหมาะแค่ starter / staged entry สำหรับคนรับ China/recovery risk ได้. |
| 2 | META | 582.90 | Base DCF 529.40 / Bull 1,032.81 | SELECTIVE WATCHLIST / HOLD | ราคาเหนือ base ประมาณ 10%; FoA cash engine ยังแข็งแรง แต่ AI capex ต้องแปลงเป็น durable FCF ก่อนจะ justify stronger ADD. |
| 3 | PG | 151.41 | Base DCF 133.34 / Bull 179.70 | DEFENSIVE WATCHLIST / HOLD | ราคาเหนือ base ประมาณ 14%; คุณภาพ defensive ดี แต่ upside ไม่หนาพอสำหรับ clear new-capital ADD. |
| 4 | UL | 62.48 | Base DCF 53.28 / Bull 73.28 | DEFENSIVE WATCHLIST / HOLD | ราคาเหนือ base ประมาณ 17%; volume-led recovery และ Power Brands น่าสนใจ แต่ต้องเห็น FCF/leverage proof หลัง Q1/H1 2026. |
| 5 | IBM | 289.52 | Base DCF 240.27 / Bull 367.87 | WATCHLIST-HIGH / HOLD | ราคาเหนือ base ประมาณ 20%; story ยังดีขึ้นจาก Software/Red Hat/AI แต่ margin of safety ลดลงหลังราคาขึ้น. |
| 6 | VZ | 42.56 | Base DCF 34.96 / Bull 47.29 | INCOME WATCHLIST ONLY | ราคาอยู่ต่ำกว่า bull DCF และดีกว่า refresh ก่อน แต่ leverage ทำให้เหมาะเฉพาะ income mandate ไม่ใช่ broad ADD. |
| 7 | CEG | 239.25 | Base DCF 194.39 / Bull 349.31 | THEMATIC WATCHLIST | ราคาเหนือ base ประมาณ 23%; power/nuclear/data-center thesis ยังน่าสนใจ แต่ valuation ยังพึ่ง non-GAAP FCF conversion. |
| 8 | VST | 151.05 | Base DCF 120.01 / Bull 209.62 | THEMATIC WATCHLIST | ราคาเหนือ base ประมาณ 26%; power demand thesis ยังดี แต่ FCFbG/growth capex quality ต้องตามต่อ. |
| 9 | UNH | 425.36 | Base DCF 258.41 / Bull 458.83 | RECOVERY WATCHLIST | ราคาใกล้ bull มากกว่าฐาน; ต้องเห็น medical-cost / guidance recovery ชัดก่อน ADD. |
| 10 | CRWD | 193.98 | Base DCF 134.50 / Bull 157.11 | IMPROVED BUT WAIT | ราคาลดแรงจาก refresh ก่อน แต่ยังสูงกว่า bull DCF เดิมประมาณ 24%; ต้อง refresh valuation หลัง source ใหม่ก่อนยกระดับ. |

## Full Covered List

| Ticker | Current Price | Latest Vault Valuation Read | 2026-07-03 Refresh |
|---|---:|---|---|
| AAPL | 308.63 | Base DCF 153.37 / Quality Bull 290.33 / Aggressive Bull 429.89 | Avoid new capital; price is above quality-bull scenario and needs aggressive assumptions. |
| ABT | 95.40 | Base DCF 63.17 / Bull 95.22 | Hold/watchlist only; price is essentially bull-case valuation. |
| AMAT | 603.04 | Base DCF 120.50 / Bull 181.22 | Avoid new capital; valuation remains far above source-backed DCF. |
| ATLX | 3.64 | DCF stopped; no fair value | Speculative watchlist only; not decision-grade investment yet. |
| AXON | 597.04 | Base DCF 136.30 | Watchlist only; quality platform but price requires much larger FCF base than source-backed guidance verifies. |
| BABA | 96.14 | Base about 88; fair/watch zone 85-110 | Best speculative staged candidate; require FCF recovery proof before stronger ADD. |
| CEG | 239.25 | Base DCF 194.39 / Bull 349.31 | Thematic watchlist; not cheap enough for clear ADD. |
| COST | 951.67 | Base DCF 530.67 / Bull 746.41 | Avoid new capital; excellent business, still too expensive versus DCF. |
| CRWD | 193.98 | Base DCF 134.50 / Bull 157.11 | Improved but still wait; price remains above bull DCF. |
| CRWV | 81.745 | DCF stopped; negative normalized FCF | Avoid new capital; FCF support is not yet source-backed. |
| CSCO | 112.69 | Base DCF 47.02 / Bull 68.09 | Avoid/wait; price remains far above cash-flow valuation. |
| DELL | 394.32 | Base DCF 209.07 / Bull 308.48 | Avoid/wait; AI server momentum still priced above source-backed valuation. |
| EW | 94.37 | Base DCF about 40.15 | Avoid/wait; price remains far above DCF. |
| GE | 377.52 | Base DCF 146.40 / Bull 227.49 | Avoid new capital; quality is strong but valuation is demanding. |
| GEV | 1,113.11 | Base DCF 587.37 / Bull 930.06 | Avoid/wait; price is above bull DCF. |
| GOOGL | 359.91 | Base DCF 112.92 / Bull 259.00 | Wait; price remains above bull DCF. |
| IBM | 289.52 | Base DCF 240.27 / Bull 367.87 | Watchlist-high / hold; no clear margin of safety after latest rise. |
| JNJ | 263.04 | Base DCF 150.38 / Bull 197.63 | Avoid/wait; price is above bull DCF. |
| KO | 84.14 | Base DCF 51.53 / Bull 80.57 | Avoid/wait; defensive quality is fully priced versus DCF. |
| MCD | 280.63 | Base DCF 125.32 / Bull 203.22 | Watchlist only; valuation still does not offer margin of safety. |
| MDT | 83.19 | Base DCF 59.41 / Bull 89.84 | Watchlist; below bull but still above base, with execution/FCF conversion risk. |
| META | 582.90 | Base DCF 529.40 / Bull 1,032.81 | Best quality selective candidate; prefer weakness or stronger FCF proof before full ADD. |
| MSFT | 390.49 | Base DCF 205.70 / Bull 309.10 | Hold existing quality; still above bull DCF, no new-capital ADD. |
| NVDA | 194.83 | Base DCF 117.96 | Hold existing quality / wait; exceptional quality but price remains above base value. |
| PG | 151.41 | Base DCF 133.34 / Bull 179.70 | Defensive watchlist / hold; possible staged entry, not high-conviction add. |
| SHOP | 119.46 | Base DCF 51.45 / Bull 85.33 | Wait; quality/growth not enough to clear valuation. |
| UL | 62.48 | Base DCF 53.28 / Bull 73.28 | Defensive watchlist / hold; staged entry only if investor accepts transition and leverage risk. |
| UNH | 425.36 | Base DCF 258.41 / Bull 458.83 | Recovery watchlist; below bull but still needs medical-cost/guidance proof. |
| V | 362.13 | Base DCF 233.21 / Bull 336.91 | Quality hold / watchlist; price is above bull-case valuation. |
| VST | 151.05 | Base DCF 120.01 / Bull 209.62 | Thematic watchlist; current price still above base. |
| VZ | 42.56 | Base DCF 34.96 / Bull 47.29 | Income watchlist only; leverage blocks broad ADD. |
| WMT | 111.84 | Base DCF 37.41 / Bull 59.65 | Avoid/wait; valuation remains far above DCF. |

## What Would Change The Decision

- Upgrade to `ADD` if price falls to or below base-case fair value without
  thesis damage, or if official filings prove a materially higher sustainable
  FCF base.
- For BABA, require positive FCF recovery, cleaner cloud/AI profitability, and
  less evidence of quick-commerce losses consuming the thesis.
- For META/MSFT/NVDA/GOOGL and other AI/platform names, require evidence that
  capex and product adoption convert into durable FCF, not only revenue growth
  or multiple expansion.
- For PG/UL/KO and other defensive staples, require better FCF yield or proof
  that volume/margin improvement offsets premium valuation.
- For CEG/VST, require cleaner cash-flow conversion after growth capex and
  less dependence on non-GAAP FCF definitions.
- For VZ, require a mandate that explicitly prioritizes dividend income and a
  comfort level on leverage/debt service.

## Missing / Unverified Data

- This refresh does not ingest new quarterly filings after each ticker's latest
  memo. It is a market-price and decision triage update.
- Market cap, shares, enterprise value, and valuation multiples were not
  refreshed for every ticker in this batch.
- Nasdaq returned latest available closed-market prices from Jul 1, 2026, not
  real-time Jul 3, 2026 quotes.
- Investor-specific constraints such as existing cost basis, target allocation,
  tax status, mandate, and cash level are unknown.

## Source Map

| Source | Use |
|---|---|
| `raw/imports/US_covered_equities_market_quote_2026-07-03.md` | Fresh closed-market quote table from Nasdaq quote API. |
| `wiki/analysis/decisions/` latest ticker memos | Prior action read, thesis framing, and action triggers. |
| `wiki/analysis/valuations/` latest ticker valuation memos | DCF anchors, valuation-stop memos, fair value ranges, and source gaps. |
| `raw/financials/` and `wiki/entities/` | Existing source-backed facts supporting each prior memo. |
