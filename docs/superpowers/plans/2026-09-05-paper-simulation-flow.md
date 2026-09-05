# Paper Simulation Flow Implementation Plan

**Goal:** เปิด local simulation ตามคำอนุมัติผู้ใช้วันที่ 2026-09-05 และให้แต่ละ run ปิดงานวิเคราะห์ก่อนค้นราคาเฉพาะ shortlist.

**Architecture:** คง ledger เดิม เพิ่ม phase `simulation` และ `SIMULATED_FILL` ที่อ้าง DECISION ที่บันทึกไว้ก่อนราคาเปิด session ถัดไป. CLI รับ batch ที่ตรวจแล้วและสร้าง fill แบบ deterministic; pending decision ไม่เปลี่ยนเงินสด.

**Spec:** ข้อเสนอใน task นี้ที่ผู้ใช้อนุมัติ: local simulation, forward prices, progressive entry, candidate-local blockers, warnings with reduced sizing, finish analysis and distinguish NO_TRADE from BLOCKED.

**Tech Stack:** Python standard library, existing batch validator, Markdown, YAML.

## Tasks

- [x] เพิ่ม simulation event validation และ settlement CLI; test buy/sell accounting, phase authorization, future-open enforcement, evidence mismatch, repeated settlement, cash rejection.
- [x] ปรับ PROMPT/config/README/glossary/ADR ให้ตรงกัน: thesis-first shortlist, optional forum, local admission, staged entry, next-session-open fill.
- [x] บันทึก PHASE_CHANGED จากคำอนุมัตินี้โดยไม่เปลี่ยน historical events; rebuild state/dashboard.
- [x] ทดสอบ ledger และ market-data suite, ตรวจ diff และ update automation prompt โดยคง schedule/model/status เดิม.
- [x] เพิ่ม workflow log และ commit เฉพาะ scope.

## Acceptance

`python3 -m unittest discover -s tests -p 'test_paper*.py'` และ market-data suite ต้องผ่าน; ledger จริงยังไม่มีการซื้อย้อนหลัง. Future run สามารถสร้าง decision และ settle ผ่าน CLI โดยไม่ใช้ broker. กองที่ blocked ไม่ขวางกองที่ผ่าน; จำนวนกองเป้าหมายไม่ใช่ prerequisite.
