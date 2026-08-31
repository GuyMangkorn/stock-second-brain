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
