# US ETF Paper Portfolio Competition

ระบบจำลองพอร์ต ETF สหรัฐฯ แบบ forward-only และ open-ended ด้วยเงินตั้งต้น
`$100,000` เพื่อดูผลลัพธ์ระยะ 1 ปีหรือนานกว่านั้น โดยใช้
[[ETF Performance Index]] และหน้าใน
`wiki/analysis/performance/` เป็น research context ไม่ใช่แหล่งราคาปัจจุบัน

## Open first

- [[dashboard]] — current derived portfolio state
- [PROMPT.md](PROMPT.md) — English instructions for each portfolio run
- [config.yaml](config.yaml) — competition policy and risk limits
- [ledger/events.jsonl](ledger/events.jsonl) — append-only system of record
- [state/portfolio.json](state/portfolio.json) — derived state; safe to rebuild

## Operating boundary

ใช้ local `simulation` ตามคำอนุมัติวันที่ 2026-09-05: กำหนด DECISION ก่อน
แล้วบันทึก `SIMULATED_FILL` ด้วยราคาเปิด session ถัดไปพร้อม slippage ตาม config.
ไม่ต้องมี broker และไม่รอ Proposal Phase. คำตัดสินที่ยังรอราคาไม่เปลี่ยน holdings.
ประวัติเก่ายังคงเดิม; ไม่ซื้อย้อนหลังจากคำตัดสินเก่า.

ลำดับ review: พอร์ต/ความเสี่ยง/pending → performance และ thesis ใน vault →
shortlist ตามบทบาท → เติมข้อมูลที่เปลี่ยนคำตัดสิน → ราคาของกองที่เกี่ยวข้อง →
คะแนน/น้ำหนัก/DECISION → settle เมื่อมีราคาเปิดที่กำหนดไว้ยืนยันแล้ว.
Forum/X เป็นบริบทเสริมเฉพาะคำถาม ไม่ใช่ขั้นบังคับหรือแหล่งยืนยันตัวเลข.

เริ่มลงทุนทีละกองได้ตาม risk/turnover limits; จำนวนกองเป้าหมายไม่ขวาง entry.
Hard gaps ตัดสิทธิ์เฉพาะกอง; noncritical research gaps เป็น warning พร้อมลดขนาด.
รายละเอียด gate และ run status อยู่ใน [PROMPT.md](PROMPT.md).

## Commands

Validate and rebuild the derived state and dashboard:

```bash
python3 paper-portfolios/us-etf-competition/scripts/rebuild_portfolio.py --check
python3 paper-portfolios/us-etf-competition/scripts/rebuild_portfolio.py
```

Record one captured market-data batch and update both compact projections:

```bash
python3 paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py \
  --root paper-portfolios/us-etf-competition --batch /path/to/captured-batch.json
```

If the screen cache is missing or invalid, rebuild it once from the complete
price log in recovery mode:

```bash
python3 paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py \
  --root paper-portfolios/us-etf-competition --bootstrap-cache
```

For a review, collect quotes with the Python API collector first, then use
ETF.com product pages and existing direct-web sources for fallback or missing fields.
Capture the clock, calendar, and relevant
market-data pages in one immutable batch under `evidence/market-data/batches/`.
Record the query, direct URL, page title, visible values/text, source as-of time,
retrieval time, and SHA-256 content hash. Search snippets alone are never
sufficient. Do not enter credentials or upload portfolio files into a website.
The dated directories under `evidence/market-data/YYYY-MM-DD/` are legacy
evidence and remain read-only; do not create new per-ticker JSON files there.

Before searching, read the screen cache in
[`latest-prices.md`](evidence/market-data/latest-prices.md) and the tail of
[`price-log.md`](evidence/market-data/price-log.md). Use those observations for
initial screening, then refresh only holdings, SPY, and decision-relevant
candidates. The recorder writes one append-only log row per verified
observation and one updated cache row per ticker; stale cache values are not
final quotes.

## Price and market-data sources

Quote source priority:

1. ETF.com delayedquotes API via `scripts/fetch_etf_quotes.py`.
2. ETF.com product page, for example https://www.etf.com/VOO.
3. Existing reputable direct market-data pages.

```bash
python3 paper-portfolios/us-etf-competition/scripts/fetch_etf_quotes.py --symbols VOO,SPY --output /tmp/unique-run-quotes.json
```

Python ใช้ curl เป็น HTTP client ตามการทดสอบ endpoint; เว้น request 10 วินาที,
ใช้ retrieval cache 15 นาที และ shared lock/cooldown ใต้ `.runtime/`.
เจอ 403/429 หยุดเรียก API ชั่วคราวอย่างน้อย 15 นาที เคารพ Retry-After ที่นานกว่า
และใช้ fallback. ค่าความถี่เป็นนโยบายของเรา ไม่ใช่ quota ที่ผู้ให้บริการรับรอง.
Output เป็น staging packet ให้ตรวจแล้วรวมลง batch เดิม พร้อม clock/calendar
และ unique evidence IDs; ไม่ได้บันทึก ledger หรือ settle อัตโนมัติ.
ดูรายละเอียด verification ใน PROMPT: snapshot ไม่ยืนยัน adjusted/unadjusted basis,
final close หรือ regular-session Open โดยตัวมันเอง; history และ SPY adjusted prices
ยังต้องเติมจากแหล่งที่ยืนยันได้. cache อายุสั้นไม่รับประกันว่าราคาต้นทางสด.

For calendar and fund facts retain these source rules:

- Official NYSE/Nasdaq or regulator pages for US trading dates, holidays, and
  early closes.
- ETF issuer product pages, fact sheets, holdings, NAV/performance pages, and
  SEC filings for fund identity, methodology, holdings, costs, and distributions.
- Direct reputable market-data pages for current quotes, bid/ask, volume, and
  historical prices when the page shows a timestamp or session date.

Keep current price, NAV, holdings, methodology, fund facts, and performance
dates separate in each evidence record. If a direct page cannot be verified or sources conflict, skip the affected
candidate and record the exact gap; portfolio-wide failures use BLOCKED.

## Disclaimer

This is an educational paper-trading simulation, not personalized investment
advice. It does not guarantee returns and must not invent unavailable evidence.

## Simulated settlement

หลัง record batch ที่มีราคาเปิดของ pending decision แล้ว:

```bash
python3 paper-portfolios/us-etf-competition/scripts/settle_simulation.py --batch paper-portfolios/us-etf-competition/evidence/market-data/batches/RUN.json
python3 paper-portfolios/us-etf-competition/scripts/settle_simulation.py --batch paper-portfolios/us-etf-competition/evidence/market-data/batches/RUN.json --write
```

คำสั่งแรกตรวจโดยไม่บันทึก; คำสั่งที่สอง append ledger และ rebuild projections.
ดู DECISION schema ใน PROMPT. รันซ้ำไม่เกิด fill ซ้ำ; ข้อมูลราคาเปิดที่ยังขาด
คง pending และคำสั่งที่เกิน notional cap จะถูกยกเลิกให้ทบทวนใหม่.
