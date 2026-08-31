---
name: research-queue-manager
description: Process Ready ETF Research Cards sequentially through the project Markdown Research Queue.
---

# Research Queue Manager

ใช้ skill นี้เพื่อรันคิวแบบมีขอบเขตทั้งจาก schedule และการสั่งงานโดยตรง โดย
การ์ด Markdown และ frontmatter เป็น operational state เดียว

Use this project-scoped skill for a scheduled or explicit bounded processing
run. The manager owns selection, claim confirmation, handoff validation, result
routing, and the scoped Git commit. It does not infer a workflow from a ticker
or title. V1 selects only Ready cards whose explicit workflow is
`check-etf-performance`.

## Execution contract

Require exactly one positive base-10 `count` and an execution profile of
`interactive-delegated` or `scheduled-inline`. Select oldest-first with a
stable timestamp/card-ID tie-break and process sequentially in the same saved
project checkout. Acquire the project lease before selection. Under
`scheduled-inline`, all ETF research and the pre-save verification checklist
remain inline in the top-level context; no worker or reviewer is dispatched.
Each bounded run first recovers expired In Progress claims, returning safe
pre-write claims to Ready and blocking ambiguous partial writes before selecting
new cards. It also materializes a committed terminal card from `HEAD` if a
process crashed after the scoped commit but before the final filesystem sync.

คำสั่งด้านล่างเป็น boundary เดียวสำหรับ claim, renew และ route ส่วน caller
ต้องเรียก downstream workflow ให้เสร็จก่อนส่งผลกลับเข้า queue:

```text
python3 scripts/research_queue.py claim-next --count 1 --owner research-queue-manager --keep-lease
python3 scripts/research_queue.py renew --card-id <ID> --owner <OWNER> --lease-token <LEASE_TOKEN> --fencing-token <TOKEN> --phase pre-write --output <OUTPUT_PATH>
python3 scripts/research_queue.py route --card-id <ID> --owner <OWNER> --lease-token <LEASE_TOKEN> --fencing-token <TOKEN> --handoff-json '<SEVEN-FIELD JSON>' --output <OUTPUT_PATH> --commit
python3 scripts/research_queue.py lease-release --owner <OWNER> --lease-token <LEASE_TOKEN>
```

สำหรับ integration test แบบ deterministic คำสั่ง `process` รับ fixture เดียว
หรือ executable adapter (`--handoff-command`) และใช้ claim/route/commit path
เดียวกัน ส่วน production caller ต้อง reread การ์ดและ renew เป็น `pre-write`
พร้อม fencing token ล่าสุดทันที ก่อนเรียก `check-etf-performance` ด้วย
`mode: lean`, execution profile ที่ระบุ, queue caller boundary และส่ง output
paths ที่เขียนจริงอย่างน้อยหนึ่งไฟล์ให้ `route` พร้อม `--commit` เท่านั้น
ถ้ารันหลายการ์ดผ่าน `process` ให้ใช้ `--output-map` แยก output scope ต่อ card
adapter ถูกจำกัดด้วย timeout ที่ต่ำกว่า lease สองชั่วโมง (`--handoff-timeout-seconds`)
เพื่อไม่ให้ subprocess ค้างจนหมดอายุ project lease และได้รับ
`RESEARCH_PROJECT_LEASE_TOKEN`, `RESEARCH_CARD_FENCING_TOKEN`,
`RESEARCH_EXECUTION_PROFILE` และ `RESEARCH_OUTPUT_PATHS` สำหรับตรวจ scope
ก่อนเขียน หาก adapter จบด้วย exit code ที่ไม่ใช่ศูนย์โดยไม่ส่ง handoff ครบเจ็ด
ฟิลด์ ให้ถือเป็น `unknown-result` ระดับ global เสมอ

`commit_id` บนการ์ดเป็น deterministic scope label (`queue/<card_id>`); ผลลัพธ์
คำสั่ง route จะคืน `commit_sha` ของ Git commit จริงและ `commit_sha_verified`; ถ้า
ตรวจ SHA หลัง commit ไม่ได้ ให้ถือเป็น evidence gap ที่ต้อง reconcile ผ่าน
`recover` จาก `HEAD` แต่ห้าม demote terminal commit ที่สำเร็จแล้ว

## Lease and fencing

Each manager run keeps one project lease from selection through the downstream
write; `claim-next --keep-lease` returns its lease token and `lease-release`
releases it after the bounded run. Each claim records owner, acquisition time, execution phase, fencing token, and
a renewable two-hour `lease_expires_at`. `updated_at` is business activity and
does not keep a dead worker alive. Renew the project lease and card at safe
phase boundaries and before the two-hour lease expires. Every mutation and
downstream pre-save boundary revalidates the token. Run recovery
when a claim is expired:

```text
python3 scripts/research_queue.py recover
```

An expired pre-write claim with no scoped output returns to Ready. A writing or
finalizing claim, or ambiguous partial output, becomes Blocked with
`partial-write-recovery`. Never retry that case automatically.

Ready cards with another workflow are not claimed; `claim-next`/`process`
returns them under `skipped` with `unsupported-workflow` so the disposition is
visible and can be handled when a future processor is shipped.

## Result boundary

Accept exactly these seven handoff fields:

```text
status, scope, durable_write, exhausted, confirmation, code, reason
```

Only `PASS + item + completed + false + none + success|durable-write-complete`
with at least one existing `raw/`, `wiki/`, `index.md`, or `log.md` output that
was declared at the pre-write renew boundary, changed after that baseline, and
a successful scoped Git commit routes to Done. Accepted item-scoped warnings, unsupported types, data
gaps, and downstream errors route to Blocked and allow the next card. Missing,
malformed, contradictory, or global results persist `unknown-result` on the
known card, report a global stop, and leave unstarted cards unchanged. Never
infer success from prose, exit status, links, or file presence.

## Git boundary and human controls

On successful completion, commit the card and explicitly supplied scoped
outputs together; unrelated user changes remain unstaged. Done and Cancelled
cards retain stable paths. Humans may use `hold`, `unblock`, and `cancel` for
manual control; In Progress and Done are automation-owned.
