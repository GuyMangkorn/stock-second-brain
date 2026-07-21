---
type: decision-refresh
date: 2026-06-28
scope: covered equities previously researched in vault
source_note: raw/imports/US_covered_equities_market_quote_2026-06-28.md
tags:
  - decision-refresh
  - covered-equities
---

# US Covered Equities Decision Refresh - 2026-06-28
## Related Entities
[[AAPL]] · [[ABT]] · [[AMAT]] · [[ATLX]] · [[AXON]] · [[BABA]] · [[CEG]] · [[COST]] · [[CRWD]] · [[CRWV]] · [[CSCO]] · [[DELL]] · [[EW]] · [[GE]] · [[GEV]] · [[GOOGL]] · [[IBM]] · [[JNJ]] · [[MCD]] · [[MDT]] · [[META]] · [[MSFT]] · [[NVDA]] · [[PG]] · [[SHOP]] · [[UNH]] · [[V]] · [[VST]] · [[VZ]] · [[WMT]]

## Action Read

**Bottom line: ยังไม่มีตัวไหนเป็น `CLEAR ADD` แบบ margin of safety ชัดตาม vault
discipline.** ตัวที่เหมาะสุดสำหรับพิจารณาลงทุนตอนนี้ยังเป็นกลุ่ม
`selective / staged entry` ไม่ใช่ซื้อเต็มไม้ทันที: **META, IBM, PG, BABA,
VZ, V**.

ถ้า strict ว่าต้องต่ำกว่า base-case DCF และไม่มี thesis damage คำตอบคือ
**ยังไม่มี**. ถ้ายอมรับการทยอยสะสมหุ้นคุณภาพหรือหุ้น recovery ที่ยังมี
source gaps กลุ่มที่พอเหมาะสมสุดคือ:

| Bucket | Tickers | Read |
|---|---|---|
| Clear ADD today | None | ยังไม่มีราคาที่ให้ base-case margin of safety ชัดพอจาก valuation memos เดิม. |
| Best selective candidates | META, IBM, PG | คุณภาพ/FCF support ดีกว่ากลุ่มอื่น แต่ราคายังสูงกว่า base DCF. เหมาะกับ staged entry เท่านั้น. |
| Speculative / recovery candidate | BABA | ราคา USD 94.81 อยู่ใน fair/watch zone ของ BABA valuation range USD 75-110 แต่ยังต้องพิสูจน์ FCF recovery. |
| Income / defensive watchlist | VZ | ราคาใกล้ bull DCF และอาจเหมาะกับ income mandate แต่ leverage ทำให้ไม่ใช่ broad ADD. |
| Existing-position quality HOLD | META, IBM, MSFT, PG, V, ABT, NVDA | ถือได้ถ้า sizing ปกติและ horizon ยาว; ไม่ใช่สัญญาณ add new capital แบบเหมารวม. |

## Current Price / Market Data Check

Market data source: Nasdaq quote API, fetched 2026-06-28 Asia/Bangkok. Because
U.S. markets were closed, Nasdaq reported `marketStatus: Closed`,
`isRealTime: false`, and latest available `lastTradeTimestamp: Jun 25, 2026`.
See `raw/imports/US_covered_equities_market_quote_2026-06-28.md`.

## Decision Ranking

| Rank | Ticker | Current Price | Valuation Anchor | Refresh Decision | Why |
|---:|---|---:|---|---|---|
| 1 | META | 550.25 | Base DCF 529.40 / Bull 1,032.81 | SELECTIVE WATCHLIST / staged entry on weakness | ราคาอยู่เหนือ base เพียงประมาณ 4% และ FoA cash engine ยังแข็งแรง แต่ต้องพิสูจน์ว่า AI capex แปลงเป็น FCF ไม่ใช่แค่ narrative. |
| 2 | IBM | 271.63 | Base DCF 240.27 / Bull 367.87 | WATCHLIST-HIGH / HOLD | ราคายังสูงกว่า base ประมาณ 13% หลังดีดขึ้นจาก refresh ก่อน แต่ FCF yield และ dividend support ดีกว่าหลายตัวใน vault. |
| 3 | PG | 149.02 | Base DCF 133.34 / Bull 179.70 | DEFENSIVE WATCHLIST / HOLD | ราคาเหนือ base ประมาณ 12%; เหมาะเป็น defensive compounder มากกว่า high-upside add. |
| 4 | BABA | 94.81 | Base fair value about 88; fair/watch zone 85-110 | SPECULATIVE STAGED WATCHLIST | ราคาเข้าใกล้ base recovery value มากขึ้น แต่ FY2026 FCF ยังติดลบและต้องรอหลักฐานว่า recovery path เกิดจริง. |
| 5 | VZ | 46.54 | Base DCF 34.96 / Bull 47.29 | INCOME WATCHLIST ONLY | ราคาใกล้ bull DCF จึงไม่ถูกบน intrinsic view แต่ dividend/income case อาจรับได้ถ้า mandate ชัดและยอมรับ leverage. |
| 6 | V | 336.23 | Base DCF 233.21 / Bull 336.91 | QUALITY HOLD / WATCHLIST | ราคาเกือบเท่ากับ bull DCF แล้ว ทำให้เหมาะกับถือหุ้นคุณภาพเดิมมากกว่า add new capital. |

## Full Covered List

| Ticker | Current Price | Latest Vault Valuation Read | 2026-06-28 Refresh |
|---|---:|---|---|
| AAPL | 283.78 | Base DCF 153.37 / Bull 228.65 | Avoid new capital; hold existing only if tax/sizing context matters. |
| ABT | 94.12 | Base DCF 63.17 / Bull 95.22 | Hold/watchlist; current price is near bull case, not base-case cheap. |
| AMAT | 626.84 | Base DCF 120.50 / Bull 181.22 | Avoid new capital; valuation remains far above source-backed DCF. |
| ATLX | 3.68 | DCF stopped; no fair value | Speculative watchlist only; not decision-grade investment yet. |
| AXON | 464.83 | Base DCF 136.30 | Watchlist; quality platform but price still requires much larger FCF base. |
| BABA | 94.81 | Base about 88; fair/watch zone 85-110 | Speculative staged watchlist; wait for FCF recovery evidence before strong add. |
| CEG | 264.02 | Base DCF 194.39 / Bull 349.31 | Watchlist; power thesis strong but valuation still depends on non-GAAP FCF conversion. |
| COST | 952.54 | Base DCF 530.67 / Bull 746.41 | Avoid new capital; excellent business, still too expensive versus DCF. |
| CRWD | 701.09 | Base DCF 134.50 / Bull 157.11 | Avoid/wait; valuation gap remains extreme. |
| CRWV | 96.58 | DCF stopped; negative normalized FCF | Avoid new capital; growth is real but FCF support is not yet source-backed. |
| CSCO | 113.77 | Base DCF 47.02 / Bull 68.09 | Avoid/wait; price remains far above cash-flow valuation. |
| DELL | 399.49 | Base DCF 209.07 / Bull 308.48 | Avoid/wait; AI server momentum still priced above source-backed valuation. |
| EW | 90.78 | Base DCF about 40.15 | Avoid/wait; price is close to 52-week high and far above DCF. |
| GE | 369.00 | Base DCF 146.40 / Bull 227.49 | Avoid new capital; quality is strong but valuation is demanding. |
| GEV | 1,045.17 | Base DCF 587.37 / Bull 930.06 | Avoid/wait; electrification thesis does not offset current price enough. |
| GOOGL | 337.39 | Base DCF 112.92 / Bull 259.00 | Wait; price remains above bull DCF. |
| IBM | 271.63 | Base DCF 240.27 / Bull 367.87 | Watchlist-high / hold; not clear add after latest bounce. |
| JNJ | 254.66 | Base DCF 150.38 / Bull 197.63 | Avoid/wait; price is above bull DCF and near high zone. |
| MCD | 269.76 | Base DCF 125.32 / Bull 203.22 | Watchlist only; valuation still does not offer margin of safety. |
| MDT | 80.98 | Base DCF 59.41 / Bull 89.84 | Watchlist; below bull but still above base, with execution/FCF conversion risk. |
| META | 550.25 | Base DCF 529.40 / Bull 1,032.81 | Best selective candidate; still prefer weakness or better FCF proof before full ADD. |
| MSFT | 372.97 | Base DCF 205.70 / Bull 309.10 | Hold existing quality; still above bull DCF, no new-capital ADD. |
| NVDA | 192.53 | Base DCF 117.96 | Hold existing quality / wait; exceptional quality but price still above base value. |
| PG | 149.02 | Base DCF 133.34 / Bull 179.70 | Defensive watchlist / hold; possible staged entry, not high-conviction add. |
| SHOP | 116.86 | Base DCF 51.45 / Bull 85.33 | Wait; quality/growth not enough to clear valuation. |
| UNH | 427.89 | Base DCF 258.41 / Bull 458.83 | Wait; below bull but recovery/medical-cost proof still needed. |
| V | 336.23 | Base DCF 233.21 / Bull 336.91 | Quality hold / watchlist; current price is effectively bull-case valuation. |
| VST | 163.49 | Base DCF 120.01 / Bull 209.62 | Watchlist; power thesis attractive but current price still above base. |
| VZ | 46.54 | Base DCF 34.96 / Bull 47.29 | Income watchlist only; leverage blocks broad ADD. |
| WMT | 115.69 | Base DCF 37.41 / Bull 59.65 | Avoid/wait; valuation remains far above DCF. |

## What Would Change The Decision

- Upgrade to `ADD` if price falls to or below base-case fair value without
  thesis damage, or if official filings prove a materially higher sustainable
  FCF base.
- For AI/platform names, require evidence that capex and product adoption are
  converting into durable FCF rather than only revenue growth or multiple
  expansion.
- For recovery names such as BABA, require positive FCF evidence and cleaner
  segment profit recovery before moving from staged watchlist to stronger add.
- For income names such as VZ, require leverage/debt-service comfort and a
  portfolio mandate that values dividend income over capital-growth optionality.

## Missing / Unverified Data

- This refresh does not ingest new quarterly filings after each ticker's latest
  memo. It is a market-price and decision triage update.
- Market cap, shares, enterprise value, and valuation multiples were not
  refreshed for every ticker in this batch.
- Investor-specific constraints such as existing cost basis, target allocation,
  tax status, mandate, and cash level are unknown.

## Source Map

| Source | Use |
|---|---|
| `raw/imports/US_covered_equities_market_quote_2026-06-28.md` | Fresh closed-market quote table from Nasdaq quote API. |
| `wiki/analysis/decisions/` latest ticker memos | Prior action read, thesis framing, and action triggers. |
| `wiki/analysis/valuations/` latest ticker valuation memos | DCF anchors, valuation-stop memos, fair value ranges, and source gaps. |
| `raw/financials/` and `wiki/entities/` | Existing source-backed facts supporting each prior memo. |
