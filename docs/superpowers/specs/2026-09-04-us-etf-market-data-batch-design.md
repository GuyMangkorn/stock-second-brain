---
status: proposed
date: 2026-09-04
owner: US ETF Paper Portfolio Competition
---

# US ETF Market Data Batch and Screen Cache Design

## Goal

ปรับ market-data workflow ของ
`paper-portfolios/us-etf-competition` ให้การพิจารณาซื้อ ETF ใช้ข้อมูลย้อนหลัง
เพื่อคัดกรองได้เร็ว แล้วเปิด direct quote เฉพาะ ETF ที่มีโอกาสถูกเสนอซื้อจริง
โดยลดการสร้างไฟล์ evidence แบบหนึ่งไฟล์ต่อ ticker ต่อ run เหลือหนึ่ง evidence
batch ต่อ Portfolio Run และยังรักษา audit trail แบบ source-backed ไว้ครบ.

## Problem and Current Evidence

ปัจจุบัน direct quote, clock, calendar และ fund evidence ถูกเก็บไว้ใต้โฟลเดอร์
วันที่ใน `evidence/market-data/YYYY-MM-DD/` โดยทั่วไปหนึ่ง run มีไฟล์ JSON หลาย
ไฟล์แยกตาม ticker. จากการตรวจวันที่ 4 กันยายน 2026 มี JSON 44 ไฟล์และ market-data
รวมประมาณ 216 KB. พื้นที่ยังไม่ใช่ปัญหาใหญ่ แต่การสร้าง เปิด และอ้างอิงไฟล์จำนวนมาก
เพิ่ม latency และทำให้ agent มีแนวโน้มใช้เวลาสแกนหลักฐานก่อนเข้าสู่การตัดสินใจ.

`price-log.md` มี observation ของทุก ticker แบบ Markdown และเป็นประวัติที่ถูกต้อง
สำหรับ audit แต่มีทั้ง completed-session, intraday, duplicate observations และ
source freshness หลายสถานะ จึงไม่ควรใช้เป็น current-price cache หรือสแกนทั้งไฟล์
ทุก run.

## Invariants

- `ledger/events.jsonl` ยังคงเป็น Portfolio Ledger และ system of record ตาม
  `docs/adr/0002-local-paper-portfolio-ledger.md`.
- Direct browser evidence เป็น read-only input; ราคาที่ใช้ก่อน `BUY` ต้องมาจาก
  direct quote ที่ verify ได้ ไม่ใช่ราคาที่ต่ำกว่าเดิมใน cache เพียงอย่างเดียว.
- ทุก verified observation ยังคงเก็บ URL, page title, visible values/text,
  source as-of, retrieval time, discovery query และ SHA-256 content hash.
- `price-log.md` ยังคง append-only; ห้ามแก้ ลบ หรือ rewrite historical observation.
- Evidence batch เป็น immutable หลังเขียนเสร็จ; correction ต้องสร้าง evidence
  ใหม่หรือ `CORRECTION` event ตามชนิดของข้อมูล ไม่เขียนทับของเดิม.
- หลักฐานเก่าใต้ dated directories ต้องคง path เดิม เพื่อให้ run notes และ ledger
  เก่าย้อนกลับไปตรวจได้.
- Scheduled-inline ยังไม่ dispatch reviewer/sub-agent และยังไม่ส่งคำสั่งซื้อ.
- Candidate Score, admission, overlap, freshness, risk และ Proposal Phase rules
  ไม่เปลี่ยนจาก `PROMPT.md` และ `config.yaml`.

## Non-goals

- ไม่ลบหรือ migrate historical JSON files ที่มีอยู่แล้ว.
- ไม่ย้าย Portfolio Ledger ไปเป็น JSON batch หรือให้ market-data เป็นเจ้าของ
  accounting.
- ไม่ใช้ screen cache เพื่อข้าม direct quote หรือ admission gate ก่อน `BUY`.
- ไม่เพิ่ม data provider ใหม่และไม่เปลี่ยน source priority.
- ไม่ทำ portfolio construction, factor scoring หรือ automatic execution ให้
  เสร็จในงานเดียวกันโดยไม่มี evidence รองรับ.

## Proposed Architecture

แบ่ง market data เป็นสามชั้นที่มีเจ้าของชัดเจน:

```text
price-log.md (append-only history)
          │
          ├── normal run: current batch observations update cache incrementally
          │
          └── recovery/bootstrap: one-time rebuild when cache is missing or invalid
          ↓
latest-prices.md (screen-cache: compact per-ticker rolling summary)
          ↓
candidate shortlist from cache + research/fund facts
          ↓
direct quote for shortlisted candidates + SPY/current holdings
          ↓
one immutable evidence batch for the run
          ↓
price-log append + screen-cache update + decision/ledger/run note
```

### 1. `price-log.md`: historical index

คงไฟล์เดิมไว้เป็น compact append-only Markdown index. ทุก verified price
observation เพิ่มหนึ่งแถว โดยมี ticker, exchange-qualified identity, price,
price basis, source as-of, retrieval time, source URL, local evidence reference,
run ID และ status. แถวนี้ไม่ต้อง copy visible response เต็ม เพราะ response เต็ม
อยู่ใน evidence batch.

ใน normal run agent อ่านเฉพาะ tail ที่จำเป็นสำหรับ sanity check และ duplicate
check. ห้ามอ่านทั้งไฟล์เพื่อเลือก ETF. การ rebuild จาก price-log เป็น recovery
operation เท่านั้น.

### 2. `latest-prices.md`: screen cache

คง path เดิมเพื่อไม่ทำลาย links แต่เปลี่ยน frontmatter/คำอธิบายให้ชัดว่าเป็น
`etf-price-screen-cache` และใช้เพื่อ preliminary screening. ให้มีหนึ่ง summary row
ต่อ ticker โดยอย่างน้อยประกอบด้วย:

- latest verified price, currency, price basis และ source-as-of;
- retrieval time, freshness status และ evidence batch reference;
- recent completed-session close series ที่มีอยู่ใน rolling window เดียวกัน;
- 1-session, 5-session และ 20-session return เมื่อคำนวณได้;
- drawdown จาก recent high เมื่อมีข้อมูลเพียงพอ;
- five-session median dollar volume เมื่อมี volume ครบ;
- screening flags เช่น `REFRESH_REQUIRED`, `LIQUIDITY_FAIL`, `STALE` หรือ
  `PRELIMINARY`.

Cache row เป็น derived state จึง update ได้จาก current batch และแทนที่ด้วย
ผลลัพธ์ที่ validate แล้ว. หาก cache หาย เสียรูป หรือไม่สอดคล้อง ให้ rebuild จาก
`price-log.md` หนึ่งครั้ง; หาก rebuild ไม่สำเร็จให้ `BLOCKED / NO_TRADE` และห้าม
เติมค่าจากการคาดเดา.

ราคาหรือ return ใน cache ไม่ใช่ `decision_reference_price` โดยอัตโนมัติ. Cache
ทำหน้าที่จัดลำดับว่า ETF ใดควรเปิด direct page ต่อ.

### 3. Evidence batch: full source envelope per run

สร้างโฟลเดอร์ใหม่ `evidence/market-data/batches/` และให้แต่ละ Portfolio Run
สร้างไฟล์เดียวชื่อ `{run_id}.json`. Batch หนึ่งไฟล์รวม clock, calendar และทุก
direct observation ที่ถูก refresh ใน run นั้น เช่น quote ของ SPY และ finalists.

แต่ละ observation ต้องคง envelope fields เดิมไว้ ได้แก่ `evidence_id`, ticker,
exchange-qualified identity, provider, discovery method/query, direct URL, page
title, visible response text/values, source as-of, retrieved-at, content hash,
price basis, currency, session/volume calculations และ `post_period_data_used`.
Batch metadata ต้องมี `schema_version`, `competition_id`, `run_id`,
`information_cutoff_at`, `analysis_at`, `created_at` และ `evidence_status`.

`evidence_id` ต้อง stable ภายใน batch เช่น `{run_id}:quote:VOO` เพื่อให้ run note
และ ledger อ้างได้ว่า observation ใดอยู่ใน batch แม้ไม่มีไฟล์แยกต่อ ticker.
`source_evidence` ของ decision event จะชี้ batch path พร้อม evidence IDs.

ไฟล์ batch เป็น full evidence ไม่ใช่ cache: ไม่ถูกอ่านทั้งก้อนในทุก run และไม่
ถูกใช้แทน `latest-prices.md` สำหรับการคัดกรองปกติ.

## Portfolio Run Flow

1. กำหนด `analysis_at` และ `information_cutoff_at`; ตรวจ execution phase และ
   calendar ตาม prompt.
2. รัน `rebuild_portfolio.py --check` และ reconcile state ก่อนตัดสินใจ.
3. อ่าน `latest-prices.md` ซึ่งเป็น screen cache และอ่านเฉพาะ tail ของ
   `price-log.md`; ไม่ glob หรือเปิด historical evidence ทั้งหมด.
4. ใช้ cache summary ร่วมกับ existing research/fund facts เพื่อคัด candidate
   shortlist. ตัด ETF ที่ติด eligibility, stale research, AUM, expense,
   liquidity หรือ known blocking condition ก่อนเปิดเว็บเมื่อราคาไม่สามารถ
   เปลี่ยนผลลัพธ์ได้.
5. เปิด direct pages เฉพาะ current holdings, SPY และ candidates ที่ผ่าน cheap
   screen แล้วมีโอกาสเปลี่ยน decision. นอก market hours ใช้ latest completed
   close และติด label ให้ชัด; ใน market hours ใช้ราคาที่เห็นพร้อม timestamp.
6. ตรวจ visible evidence และ hash ของแต่ละ page แล้วรวมผลไว้ในหนึ่ง batch JSON.
7. คำนวณ final admission, score, overlap, risk, turnover และ target weights.
   Cache observation ห้ามข้าม direct-quote freshness gate.
8. ถ้ามี data failure ให้บันทึก `BLOCKED / NO_TRADE`, preserve portfolio และ
   ยังคงเก็บ batch ที่อธิบาย failure ได้. ถ้าผ่านทุก gate ให้สร้าง `BUY` proposal
   ตาม Proposal Phase rules แต่ยังไม่ส่งคำสั่ง.
9. หลัง batch ผ่าน validation ให้ append compact observations ลง `price-log.md`,
   update `latest-prices.md` จาก cache state เดิม + observations ใน batch,
   append ledger events และเขียน dated run note.
10. รัน portfolio rebuild และ checks อีกครั้ง. หาก cache/log update ล้มเหลว
    ให้ run เป็น blocked หรือ recovery-required และห้ามอ้าง cache ที่อาจไม่
    สอดคล้องเป็นหลักฐาน final.

## Batch and Cache Update Contract

เพื่อให้ normal run ไม่ต้องอ่าน price-log ทั้งก้อน ให้มี deterministic helper
ตัวเดียวรับ validated batch แล้วทำงานดังนี้:

1. ตรวจ schema, required fields, duplicate `evidence_id`, source-as-of,
   `information_cutoff_at` และ hash.
2. สร้าง compact log rows จาก observations โดยไม่เปลี่ยนความหมายของ source.
3. Append rows ลง price log โดยรักษาลำดับและไม่แก้ history.
4. โหลด screen cache ปัจจุบัน, merge เฉพาะ observations ของ batch, คำนวณ rolling
   metrics จากข้อมูลใน cache และเขียน cache ใหม่แบบ atomic.
5. เขียน validation summary ที่ run note และ ledger ใช้อ้าง ไม่สร้าง duplicate
   evidence files ต่อ ticker.

Bootstrap/recovery mode จึงเป็น mode เดียวที่อ่าน price-log ทั้งไฟล์เพื่อสร้าง
cache ใหม่. หากต้องมีการ partition ในอนาคต ให้เป็นการเปลี่ยนแปลงแยกที่มี
manifest และไม่ทำลาย path เดิม.

## Failure Handling and Audit

- Batch ที่ขาด URL, page title, visible values, source-as-of, retrieval time,
  query หรือ hash: reject batch และ `BLOCKED / NO_TRADE`.
- Quote stale, conflicting หรือไม่สามารถเปิด direct page ได้: เก็บสถานะและ
  source gap ใน batch/run note แต่ไม่ promote เป็น decision reference.
- Cache stale แต่ batch/direct quote ใช้ได้: refresh จาก direct evidence; cache
  stale status ไม่ block การอ่านเพื่อ shortlist แต่ block `BUY` หากไม่มี final
  quote ตาม gate.
- Cache invalid และ recovery จาก price-log ล้มเหลว: preserve portfolio, no trade,
  report recovery blocker.
- Batch validate ผ่านแต่ cache update เขียนไม่สำเร็จ: ห้ามบอกว่ารอบสมบูรณ์;
  เก็บ batch ไว้เป็น evidence, mark run `BLOCKED` และซ่อม cache ใน recovery run.
- Existing dated JSON evidence: mark as legacy in documentation only; ห้ามย้าย
  หรือลบเพื่อรักษา historical links.
- Ledger correction: ใช้ `CORRECTION` event เท่านั้น ไม่ rewrite event เก่า.

## Migration and Compatibility

- ไม่แก้ historical dated evidence และไม่แก้ run notes เก่า.
- ปรับ `PROMPT.md`, `config.yaml` และ market-data README ให้บอกว่า new runs ใช้
  `batches/{run_id}.json`, cache เป็น screen summary และ price-log เป็น history.
- Run notes ใหม่ชี้ไปที่ batch เดียวและระบุ evidence IDs; links เก่ายังคงใช้
  dated files เดิมได้.
- เพิ่ม schema/version discriminator เพื่อให้ validator แยก legacy envelope
  กับ batch envelope ได้.
- Existing `latest-prices.md` rows ต้องถูก convert ใน place เป็น schema ของ
  screen-cache โดย preserve ราคาที่ verify แล้วและ source links เดิม.
- Rollout ครั้งแรกต้องสร้าง batch ใหม่จาก observations ที่ fetch ใน run นั้น
  เท่านั้น; ห้ามรวม historical files ย้อนหลังโดยไม่มี provenance.

## Files Expected to Change During Implementation

- `paper-portfolios/us-etf-competition/PROMPT.md`
- `paper-portfolios/us-etf-competition/config.yaml`
- `paper-portfolios/us-etf-competition/README.md`
- `paper-portfolios/us-etf-competition/evidence/market-data/README.md`
- `paper-portfolios/us-etf-competition/evidence/market-data/latest-prices.md`
- `paper-portfolios/us-etf-competition/evidence/market-data/price-log.md`
- new `paper-portfolios/us-etf-competition/evidence/market-data/batches/`
- new deterministic batch/cache validation helper under
  `paper-portfolios/us-etf-competition/scripts/`
- focused tests under `tests/` for schema, cache merge, hash validation and
  legacy compatibility.

ไม่รวมการแก้ historical JSON, existing run notes, Portfolio Ledger semantics,
หรือ unrelated research-queue/ETF-performance files.

## Validation and Acceptance Criteria

Implementation is complete only when all conditions below hold:

- A simulated run that refreshes SPY plus three candidates creates one batch JSON,
  not four new per-ticker JSON files.
- Batch validation rejects missing metadata, duplicate evidence IDs, mismatched
  hashes, post-cutoff values and unsupported price basis.
- `latest-prices.md` contains one compact current/rolling summary per ticker and
  can select finalists without reading the full price log.
- Every verified observation produces exactly one price-log row and one cache
  merge; rerunning the same batch does not duplicate rows or change history.
- Final `BUY` proposals cite direct batch evidence, not cache-only observations.
- A stale/conflicting direct quote produces `BLOCKED / NO_TRADE` and preserves the
  prior portfolio.
- Historical dated evidence and old run-note links remain readable.
- `python3 paper-portfolios/us-etf-competition/scripts/rebuild_portfolio.py --check`
  passes before and after a sample run.
- Focused tests, `git diff --check`, JSON parsing, hash checks and link checks pass.
- Scheduled-inline still makes no reviewer/sub-agent dispatch and no order call.

## Recommendation

ใช้ hybrid design นี้: `price-log` เป็น historical source, `latest-prices.md` เป็น
screen cache ที่มี rolling context มากกว่า latest row เดียว และหนึ่ง run ใช้ full
evidence batch เดียว. วิธีนี้แก้ทั้ง latency ของการคัด ETF และ file explosion โดย
ไม่ใช้ข้อมูลย้อนหลังแทนราคาจริงก่อนตัดสินใจ และไม่ทำลาย audit trail เดิม.
