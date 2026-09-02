# Stock Second Brain

คลังความรู้และ workflow วิจัย public equity ที่แยกหน่วยงานวิจัยออกจาก
หลักทรัพย์และผลลัพธ์ถาวร เพื่อให้ทั้งมนุษย์และ automation ใช้ภาษาเดียวกัน

## Research Workflow Language

**Research Card**:
งานวิจัยหนึ่งงานสำหรับ instrument หนึ่งตัวและ Research Workflow หนึ่ง route; card ไม่ใช่ entity หรือผลวิเคราะห์ของ instrument นั้น
_Avoid_: ETF card, Stock card, Trello card, instrument card

**Research Batch**:
คำขอสร้าง Research Cards ตั้งแต่หนึ่งใบขึ้นไปจาก ticker input ชุดเดียว; batch เสร็จเมื่อสร้าง cards ครบ ไม่ใช่เมื่อ research ทุก card เสร็จ
_Avoid_: Master card, research result batch

**Research Queue**:
ชุด Research Cards กลางของโปรเจกต์ที่ Obsidian แสดงเป็น views และ automation เลือกไปประมวลผล
_Avoid_: Trello board, ETF queue

**Research Workflow**:
route ที่ระบุชัดบน Research Card และเป็นเจ้าของการสร้าง durable research outputs ของงานนั้น
_Avoid_: Card type, inferred route

**Intake**:
ขั้นที่แปลง ticker input ซึ่งผู้ใช้อนุญาตแล้วเป็น Research Batch และ Research Cards โดยยังไม่เริ่ม research
_Avoid_: Processing, research run

**Ready**:
สถานะของ Research Card ที่พร้อมให้ Research Queue เลือกไปทำงาน
_Avoid_: Ready for AI, queued

**In Progress**:
สถานะของ Research Card ที่มี automation claim อยู่ภายใต้ lease ที่ยังใช้ได้
_Avoid_: Running without a claim

**Blocked**:
สถานะของ Research Card ที่ต้องรอการแก้ปัญหา การยืนยัน หรือการปลดกลับเป็น Ready
_Avoid_: Failed, Done with warning

**Done**:
สถานะ terminal ของ Research Card ที่ Research Workflow ยืนยัน durable completion แล้ว
_Avoid_: PASS without durable write, research attempted

**Cancelled**:
สถานะ terminal ของ Research Card ที่ผู้ใช้ยุติก่อน durable completion โดยยังเก็บ audit trail ไว้
_Avoid_: Deleted, Done

**One-time Seed**:
การนำ ticker ชุดเดิมจาก Trello เข้า Intake เพียงครั้งเดียวโดยไม่มี provenance, synchronization หรือ migration protocol ถาวร
_Avoid_: Trello migration, Trello sync

## Paper Portfolio Language

**Paper Portfolio Competition**:
การจำลองพอร์ตที่มีเงินตั้งต้น ช่วงเวลา benchmark และข้อจำกัดตายตัว โดยไม่มีเงินจริงหรือคำแนะนำส่วนบุคคลเกี่ยวข้อง
_Avoid_: Backtest, live portfolio, personal portfolio

**Research Universe**:
ชุด ETF ทุกตลาดที่ vault มีหรืออาจสร้างงานวิจัยให้ โดยยังไม่ได้หมายความว่า ETF ทุกตัวซื้อขายได้ในการแข่งขัน
_Avoid_: Tradable list, approved portfolio

**Tradable Universe**:
ส่วนของ Research Universe ที่เป็น US-listed, unleveraged, long-only equity ETF และผ่าน identity, eligibility และ source-integrity checks แล้ว
_Avoid_: All researched ETFs, watchlist

**Tradable Admission Gate**:
เงื่อนไขที่ ETF ต้องผ่านก่อนรับสถานะซื้อได้ โดยผล `WARNING`, `CHANGES_REQUIRED`, `BLOCKED` หรือข้อมูลราคาที่ stale ไม่ถือว่าผ่าน
_Avoid_: Research completed, page exists

**Portfolio Review**:
รอบตรวจพอร์ตตามตารางที่อาจจบด้วย `HOLD` โดยไม่ต้องเปลี่ยน target weights
_Avoid_: Mandatory trade, rebalance

**Rebalance**:
การเปลี่ยน target weights หรือเงินสดผ่านคำสั่งซื้อขายตาม cadence ปกติของการแข่งขัน
_Avoid_: Portfolio Review, mark-to-market

**Risk Override**:
คำสั่งลดหรือขายที่อนุญาตนอก cadence ของ Rebalance เมื่อ exit condition หรือ hard risk limit ถูกกระตุ้น
_Avoid_: Discretionary extra rebalance

**Decision Reference Price**:
ราคาพร้อม timestamp ที่มีอยู่จริงขณะตัดสินใจและใช้เป็นหลักฐานของข้อมูลที่ agent เห็นในรอบนั้น
_Avoid_: Fill Price, later close

**Submitted Price**:
ราคาอ้างอิงหรือ limit ที่แนบกับคำสั่งเมื่อส่งเข้า paper broker
_Avoid_: Decision Reference Price, Fill Price

**Fill Price**:
ราคาที่ paper broker ยืนยันว่าคำสั่งจำลองถูกจับคู่แล้วและเป็นเจ้าของ cost basis กับ realized P&L
_Avoid_: Estimated fill, Reference Price

**Operational Benchmark**:
SPY adjusted total-return proxy ที่ใช้กับ daily equity curve และ drawdown ของการแข่งขัน
_Avoid_: Official S&P 500 Total Return Index

**Reference Benchmark**:
Official S&P 500 Total Return Index ที่ใช้ใน periodic comparison เมื่อมีข้อมูลช่วงเวลาเดียวกันที่ตรวจสอบได้
_Avoid_: SPY price return, Operational Benchmark

**Proposal Phase**:
ระยะเริ่มต้นที่ automation สร้าง decision และ order sheet แต่ยังไม่ส่งคำสั่งให้ paper broker
_Avoid_: Automatic execution, live trading

**Automatic Execution Phase**:
ระยะที่ automation ส่งคำสั่งเข้า paper broker ได้หลัง Proposal Phase ผ่าน reconciliation และได้รับการเปิดใช้โดยชัดแจ้ง
_Avoid_: Live-money trading, assumed authorization

**Candidate Score**:
คะแนน 0–100 สำหรับจัดลำดับ ETF จาก regime fit, underlying earnings, valuation, strategy quality, momentum และ risk/liquidity/cost โดยไม่ใช่คำสั่งซื้อขายอัตโนมัติ
_Avoid_: Buy signal, deterministic rank

**Liquidity Gate**:
ข้อกำหนดขั้นต่ำด้าน AUM, trading volume, bid/ask spread, expense ratio และ usable history ที่ ETF ต้องผ่านก่อนเข้าสู่การพิจารณาซื้อ
_Avoid_: Tradable Admission Gate, Candidate Score

**Seasoning Rule**:
ข้อจำกัดน้ำหนักของ ETF ที่มี realized history ตั้งแต่หนึ่งปีแต่ยังไม่ถึงสามปี; ETF อายุต่ำกว่าหนึ่งปีเป็น watchlist เท่านั้น
_Avoid_: New-fund ban, seasoned ETF

**No-trade Band**:
ช่วงความต่างระหว่าง actual weight กับ target weight ที่เล็กเกินกว่าจะสร้างคำสั่ง Rebalance
_Avoid_: HOLD thesis, blocked order

**Normal Turnover**:
มูลค่าซื้อและขายรวมจาก Rebalance ปกติในหนึ่งรอบเทียบกับมูลค่าพอร์ต โดยไม่รวม Risk Override
_Avoid_: Trading volume, broker volume

**Daily Equity Curve**:
ลำดับมูลค่าพอร์ต ณ ราคาปิดของทุก US Trading Session ซึ่งเป็นเจ้าของ cumulative return และ Maximum Drawdown
_Avoid_: Intraday portfolio value, broker chart

**Intraday Portfolio Value**:
มูลค่า mark-to-market ระหว่าง session ที่ใช้ประกอบ Portfolio Review แต่ไม่เขียนทับ Daily Equity Curve
_Avoid_: Daily close, final NAV

**Data Failure**:
ภาวะที่ข้อมูลบังคับหาย stale ขัดแย้ง หรือเรียกไม่ได้ ซึ่งจบด้วย `NO TRADE` และ audit entry โดยไม่ backfill จากข้อมูลหลัง cutoff
_Avoid_: Zero value, implicit HOLD

**Portfolio Ledger**:
event history แบบ append-only ที่เป็น system of record ของ positions, cash, orders, fills, distributions, corrections และ portfolio performance
_Avoid_: Broker account, mutable holdings file

**Execution Mirror**:
paper-broker account ที่ส่งคำสั่งและยืนยัน fills แต่ไม่เป็นเจ้าของ total-return accounting หรือ canonical portfolio state
_Avoid_: Portfolio Ledger, live brokerage account

**Candidate Discovery Budget**:
จำนวน ETF ใหม่นอก verified universe ที่หนึ่ง Rebalance เปิด research ได้ โดย ETF ดังกล่าวยังซื้อไม่ได้ในรอบเดียวกัน
_Avoid_: Position limit, research batch size

**Soft Drawdown Trigger**:
ระดับ Maximum Drawdown ที่หยุดการเปิด position ใหม่และบังคับให้เพิ่ม cash พร้อมลด weakest positions
_Avoid_: Hard Drawdown Trigger, position stop

**Hard Drawdown Trigger**:
ระดับ Maximum Drawdown ที่หยุด `BUY` และบังคับให้ลด portfolio exposure อย่างมีนัยสำคัญจนกว่าจะผ่าน Portfolio Review ใหม่
_Avoid_: Soft Drawdown Trigger, liquidation

**Re-underwrite**:
การทบทวน thesis, Candidate Score, sources และ exit conditions ใหม่เมื่อ position-level loss trigger ถูกกระตุ้น
_Avoid_: Automatic SELL, routine Portfolio Review

**Source Freshness Gate**:
อายุสูงสุดที่ยอมรับได้ของข้อมูลแต่ละประเภทสำหรับคำสั่ง `BUY`; ข้อมูล stale ยังอนุญาต risk-driven `REDUCE` หรือ `SELL`
_Avoid_: Tradable Admission Gate, Data Failure

**Correction Event**:
รายการ append-only ที่อ้างอิง record เดิมและแก้ผลคำนวณโดยไม่ลบหรือเขียนทับ audit history
_Avoid_: File rewrite, silent backfill

**Final Reconciliation**:
การปิดผลการแข่งขันด้วยราคาปิดของวันสิ้นสุดและตรวจ ledger, benchmark, cash, distributions และ corrections โดยไม่บังคับขาย holdings
_Avoid_: Forced liquidation, post-period reinterpretation

**Market Data Evidence**:
immutable record ของ documented market-data request และ response พร้อม parameters, timestamps และ content hash ที่รองรับ Decision Reference Price หรือ Daily Equity Curve
_Avoid_: Search snippet, dashboard value, private endpoint scrape

**Mirror Sync**:
คำสั่งที่ทำให้ holdings ใน Execution Mirror ตรงกับ Portfolio Ledger เมื่อเริ่ม Automatic Execution Phase โดยไม่สร้าง competition trade หรือ P&L event
_Avoid_: Rebalance, opening trade

**Scheduled Portfolio Run**:
Portfolio Review ที่ heartbeat เรียกตาม US market calendar และอาจจบด้วย Rebalance, Risk Override, `HOLD` หรือ `BLOCKED/NO TRADE`
_Avoid_: Guaranteed trade, background live trading
