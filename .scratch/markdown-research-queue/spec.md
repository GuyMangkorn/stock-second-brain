# Project-Local Markdown Research Queue

Status: ready-for-agent

## Problem Statement

ผู้ใช้ต้องการเลิกใช้ Trello เป็น operational state owner ของงานวิจัยหุ้นและ
ETF เพราะสถานะการ์ดอยู่นอก Stock Second Brain, ต้องพึ่ง connector-specific
skills และตรวจสอบร่วมกับ research files ได้ยาก ผู้ใช้ต้องการโยน ticker list
พร้อมบอกว่าเป็น ETF หรือ Stock แล้วให้ระบบสร้างและติดตามงานใน Obsidian โดยไม่
ต้องกรอก schema ที่ซับซ้อนเอง การ์ดต้องมองเห็นง่ายใน Ready, In Progress,
Blocked, Done และ Cancelled แต่ automation ยังต้องรักษา claim safety,
verification gate, durable-write contract และ Git history เดิม

## Solution

สร้าง Research Queue กลางที่ใช้ Markdown Research Card หนึ่งไฟล์ต่อหนึ่ง
research job และใช้ frontmatter เป็น source of truth Obsidian Bases แสดง
Monitor view และ Base Board แสดง Intake view โดย plugin เป็นเพียง projection
ที่อ่านและเขียน properties ของไฟล์เดิม

ผู้ใช้ส่ง ticker list แบบธรรมดาให้ `research-card-intake`; skill ใช้
deterministic queue interface เพื่อสร้าง Research Batch และ Research Cards ที่
ครบ schema, ตรวจ duplicate และตั้ง Ready ให้โดยอัตโนมัติ Scheduled
`research-queue-manager` เลือก Ready cards ตามลำดับ, claim ภายใต้ renewable
two-hour lease, เรียก Research Workflow ที่ระบุชัด และยอมรับเฉพาะ structured
handoff ก่อน route ไป Done หรือ Blocked

V1 ประมวลผล `check-etf-performance` เท่านั้น แต่ vocabulary, card schema และ
queue interface รองรับการเพิ่ม Stock workflows ภายหลังโดยไม่แยก storage หรือ
state machine ใหม่ Trello tickers เดิมจะถูกนำเข้าเป็น one-time seed ผ่าน Intake
ปกติ จากนั้น automation เดิมจะเปลี่ยนมาอ่าน Research Queue และ Trello จะเหลือ
เป็น inert history โดยไม่มี sync หรือ migration protocol ถาวร

## User Stories

1. As an investor, I want to queue an ETF ticker list in plain language, so that I do not have to create cards manually.
2. As an investor, I want to identify a whole list as ETF or Stock once, so that repeated metadata entry is unnecessary.
3. As an investor, I want to submit comma-separated tickers, so that quick capture is frictionless.
4. As an investor, I want to submit Markdown bullets, so that lists copied from notes remain usable.
5. As an investor, I want to submit a Markdown table, so that structured watchlists can become research work.
6. As an investor, I want to reference a project-relative input file, so that a large existing list does not need to be pasted into chat.
7. As an investor, I want a mixed table with an explicit Type column to be accepted, so that deliberately mixed future inputs remain representable.
8. As an investor, I want ETF intake to choose the documented ETF-performance workflow by default, so that the common request stays short.
9. As an investor, I want to override the default Research Workflow explicitly, so that specialized work can be requested without changing the queue model.
10. As an investor, I want an explicit dry-run option, so that I can inspect normalization without creating files.
11. As an investor, I want an explicit create or queue request to write Ready cards without another confirmation, so that intake can be fast and predictable.
12. As an investor, I want one Research Batch to record each authorized list submission, so that I can see which cards were created together.
13. As an investor, I want a Research Batch to be Done when card creation is complete, so that batch creation is not confused with research completion.
14. As an investor, I want each Research Card to represent one instrument and one Research Workflow, so that independent jobs do not share blockers or outcomes.
15. As an investor, I want the same instrument to have separate results, valuation, and decision jobs, so that their lifecycle remains independent.
16. As an investor, I want an existing active instrument/workflow pair to be reused instead of duplicated, so that two workers cannot perform the same active job accidentally.
17. As an investor, I want a new refresh card after an earlier card is terminal, so that repeated research remains auditable.
18. As an investor, I want human-readable card titles with immutable card identities, so that renamed subjects do not break links or claims.
19. As an Obsidian user, I want an Intake board showing Ready and Blocked cards, so that I can add work, pause it, and unblock it visually.
20. As an Obsidian user, I want a Monitor view showing every status, so that I can observe automation without using Trello.
21. As an Obsidian user, I want dragging between Ready and Blocked to update the card property directly, so that the Markdown file remains authoritative.
22. As an Obsidian user, I want In Progress and Done to be automation-owned, so that a visual drag cannot bypass claim or durable-write checks.
23. As an Obsidian user, I want Done and Cancelled cards to retain stable paths, so that historical links and Git history remain valid.
24. As an Obsidian user, I want result files linked from a card instead of copied into it, so that analysis numbers have one durable owner.
25. As a queue operator, I want only Ready cards with supported explicit workflows selected, so that the manager never infers a route from a ticker or title.
26. As a queue operator, I want Ready cards processed oldest-first with a deterministic tie-break, so that batch order is predictable.
27. As a queue operator, I want each manager run bounded by a positive count, so that scheduled work has a clear capacity limit.
28. As a queue operator, I want cards processed sequentially, so that shared indexes, logs, and Git commits are not mutated concurrently.
29. As a queue operator, I want one project-scoped lease across queue operations, so that intake splitting and research processing cannot overlap unsafely.
30. As a queue operator, I want the lease renewed at safe phase boundaries and to expire after two idle hours, so that an abandoned run does not block future schedules forever.
31. As a queue operator, I want a fencing token checked before state changes and durable writes, so that an expired worker cannot resume and overwrite a newer owner.
32. As a queue operator, I want safe stale claims returned to Ready automatically, so that unfinished research can be retried without manual cleanup.
33. As a queue operator, I want stale claims with possible partial writes moved to Blocked, so that ambiguous output is inspected before retry.
34. As a queue operator, I want claim, lease expiry, phase, and result metadata visible on the Research Card, so that operational state is inspectable in Obsidian.
35. As a queue operator, I want business `updated_at` separate from `lease_expires_at`, so that human note edits cannot keep a dead worker alive.
36. As a queue operator, I want all queue workers to run in the same saved-project checkout, so that they observe the same lock and working-tree state.
37. As a queue operator, I want strict structured downstream results, so that prose or file presence cannot be mistaken for success.
38. As a queue operator, I want only a verified durable completion routed to Done, so that PASS without completed writes is not terminal success.
39. As a queue operator, I want warnings, unsupported instruments, hard data gaps, and item errors routed to Blocked with a reason, so that failures have a clear owner.
40. As a queue operator, I want an item-level block to allow the next Ready card to run, so that one ticker does not stop the whole batch.
41. As a queue operator, I want configuration, claim-state, contradictory-result, and unsafe recovery failures to stop the run, so that global faults do not spread mutations.
42. As a maintainer, I want one high-level deterministic queue interface, so that skills do not implement frontmatter and locking rules differently.
43. As a maintainer, I want queue state and scoped research outputs committed together per terminal card, so that Git shows a coherent job outcome.
44. As a maintainer, I want unrelated working-tree changes preserved and excluded from queue commits, so that scheduled work does not capture user edits.
45. As a maintainer, I want project-scoped intake and manager skills, so that the workflow contract is versioned with the vault.
46. As a maintainer, I want the existing ETF-performance skill to return a backward-compatible research handoff, so that the new manager can validate outcomes without breaking the old route during cutover.
47. As a maintainer, I want V1 to process ETF performance only, so that the Trello replacement can ship before adding Stock execution routes.
48. As a maintainer, I want the generic schema to reserve Stock as an instrument type, so that Stock processing can be added later without moving existing cards.
49. As a maintainer, I want Trello Ready and Blocked tickers seeded through normal Intake once, so that no permanent importer or provenance schema is introduced.
50. As a maintainer, I want the Trello board left unchanged after seeding, so that it remains a recoverable historical reference rather than a second live queue.
51. As a maintainer, I want the existing scheduled automation updated in place, so that two dispatchers never process the old and new queues concurrently.
52. As a maintainer, I want the existing three-hour schedule, count, model, and scheduled-inline profile preserved, so that cutover changes storage rather than workload policy.
53. As a maintainer, I want a manual single-card run before automation cutover, so that state, research, lease, and Git behavior are proven together.
54. As a maintainer, I want Base views to report the same counts as the files on disk, so that the UI can be trusted as a projection.
55. As a maintainer, I want the classic Kanban plugin excluded from this queue's state model, so that a board note cannot become a competing source of truth.

## Implementation Decisions

- The Research Queue is project-local and Markdown-backed. Research Card files
  retain stable paths; status is a frontmatter property and is the sole
  operational source of truth.
- A Research Card is one Research Workflow invocation for one instrument. It
  has an immutable, time-sortable card identity and a human-readable title.
- Required card properties are the card kind, immutable ID, title, status,
  explicit workflow, instrument type, input ticker, creation time, and business
  update time. Canonical entity identity, exchange, parent batch, claim, result,
  commit, and output links are populated only when their lifecycle stage needs
  them.
- Card statuses are Ready, In Progress, Blocked, Done, and Cancelled. Done and
  Cancelled are terminal. Humans may create Ready cards and move Ready to or
  from Blocked for manual holds. Automation owns In Progress and Done.
- A Research Batch records one authorized Intake submission. Its completion
  means every valid, non-duplicate child card was materialized; it does not
  summarize downstream research completion.
- Intake is a project-scoped, model-invoked skill whose trigger requires clear
  create, add, or queue intent. It accepts inline ticker lists, Markdown lists,
  Markdown tables, and project-relative files. A mixed request requires an
  explicit Type column.
- Intake supports a dry-run mode. A mutating request creates a Research Batch
  and Ready cards immediately without a second confirmation.
- Intake applies documented defaults and writes the selected route explicitly
  onto every card. V1 defaults ETF to `check-etf-performance`. The future Stock
  default is `official-source-stock-research` in deep-dive mode, but Stock
  creation remains disabled until a Stock processor is delivered.
- An active duplicate is an existing Ready, In Progress, or Blocked card for
  the same resolved-or-normalized instrument and Research Workflow. Intake
  returns the existing card instead of creating another. Terminal cards do not
  prevent a new refresh job.
- The manager is a separate project-scoped skill. It validates one positive
  count and one supported execution profile before selection, selects only
  supported Ready cards, preserves Intake order, and processes sequentially.
- V1 supports only ETF performance execution. Unknown and future workflow
  routes are not selected or inferred.
- One deterministic queue command surface owns Intake, validation, duplicate
  checks, claim, recovery, result routing, and lease operations. Skills
  orchestrate that interface instead of rewriting the file protocol in prose.
- One project-scoped runtime lease serializes the queue in the saved checkout.
  Runtime lock material is ignored by Git. The lease has a unique owner and
  fencing token, is renewed at safe phase boundaries, and expires two hours
  after its last renewal.
- A claim records its identity, acquisition time, current phase, and explicit
  lease expiry on the card. Business `updated_at` remains separate from lease
  liveness.
- The manager confirms a claim by rereading the same card. Every later queue
  mutation and the downstream pre-save boundary revalidate the fencing token.
- An expired claim in a pre-write phase returns to Ready only when scoped
  recovery confirms no durable output write began. A claim in a writing or
  finalizing phase, or one with ambiguous uncommitted scoped output, becomes
  Blocked with a stable partial-write recovery code.
- All scheduled queue work runs in the same local saved-project checkout.
  Queue execution from independent worktrees and overlapping managers is not
  supported.
- `check-etf-performance` remains the existing external skill dependency. It
  gains a backward-compatible `research_handoff` caller contract while keeping
  the old contract available through cutover.
- The research handoff retains the seven-field status, scope, durable-write,
  exhausted, confirmation, code, and reason envelope. The manager treats a
  missing or contradictory envelope as a global-stop result and never infers
  success from prose, links, or file existence.
- Done requires strict item-scoped success, completed durable writes, no
  exhaustion, no pending confirmation, an accepted success code, at least one
  existing `raw/`, `wiki/`, `index.md`, or `log.md` output path declared before
  downstream writes and changed after that baseline, and a successful scoped
  Git commit.
  Other valid item results become Blocked. Known-card invalid results are
  persisted safely before the manager stops globally.
- Result metadata stays compact on the card. Analysis content remains in its
  owning vault artifacts; the card stores wikilinks, completion time, and the
  scoped commit identifier.
- One completed card and its scoped downstream artifacts are staged and
  committed together. Unrelated user changes remain unstaged and untouched.
- Obsidian Base Board is the operational Intake projection for Ready and
  Blocked. Native Bases provides the all-status Monitor and historical views.
  Classic Kanban is not used for Research Queue state.
- The one-time seed reads only ticker values from the then-current Trello Ready
  and Blocked lanes and passes them to normal ETF Intake. It creates no
  migration-only properties, rules, synchronization, or Trello mutations.
- Cutover pauses selection long enough to seed the current ticker set and run
  one manual card. The existing automation is then updated in place, preserving
  its three-hour cadence, count of ten, model, reasoning effort, project target,
  local execution, and scheduled-inline boundary.
- Scheduled-inline continues to forbid research and reviewer delegation. The
  ETF workflow performs source work and the complete pre-save verification
  locally and records the required scheduled-local audit lines.

## Testing Decisions

- The primary test seam is the high-level deterministic queue command surface
  operating against a temporary vault. Tests assert resulting files, statuses,
  exit codes, and reported identities rather than internal functions.
- Intake tests cover every accepted input shape, ticker normalization, mixed
  Type requirements, invalid input, dry-run behavior, deterministic ordering,
  batch completion, immutable IDs, active duplicate reuse, and refresh creation
  after terminal work.
- State-machine tests cover the allowed human and automation transitions,
  claim reread, unsupported status changes, cancellation, terminal immutability,
  and stable paths.
- Lease tests use a controllable clock to cover acquisition, renewal, overlap,
  two-hour expiry, atomic takeover, fencing rejection of the stale owner, and
  same-checkout assumptions.
- Recovery tests cover pre-write stale claims with no output, writing-phase
  expiry, unknown-phase claims, ambiguous scoped working-tree changes, safe
  return to Ready, partial-write routing to Blocked, and reconciliation of a
  terminal card whose scoped commit completed just before a process crash.
- Result tests feed complete and malformed seven-field handoffs through the
  public seam. They cover strict success, accepted item blocks, confirmation
  warnings, unsupported instruments, data gaps, item errors, invalid-envelope
  persistence, and global-stop behavior.
- Git integration tests use a temporary repository to prove that one terminal
  job commits its card and scoped outputs together while unrelated dirty files
  remain untracked or unstaged by the queue operation.
- Obsidian view smoke tests verify that the view definitions load, filter the
  Research Card kind, expose the intended statuses, and do not introduce a
  second board-owned state field.
- Skill validation checks both project skills with the standard skill
  validator and exercises realistic natural-language Intake requests. Tests
  target produced artifacts and behavior rather than matching instruction text.
- Existing Trello workflow contract tests are prior art for result-envelope and
  execution-boundary invariants, but new tests replace prompt-string assertions
  with behavioral temporary-vault tests.
- Rollout includes a read-only queue count check, one manual scheduled-inline
  card with count one, inspection of its durable outputs and Git commit, and a
  post-update view of the existing automation configuration.

## Out of Scope

- Executing Stock Research Workflows in V1.
- Separate Stock and ETF queues or status machines.
- Priority scheduling, parallel card processing, multi-checkout coordination,
  and cross-host distributed locks.
- General card dependencies; multi-stage work continues to use an owning
  pipeline Research Workflow.
- Automatic retry when a stale claim may have begun durable writes.
- A permanent Trello importer, Trello provenance fields, two-way sync, card
  archival, board mutation, or continued Trello selection.
- Importing Trello Done cards.
- Using classic Kanban, TaskNotes, Project Tracker, due dates, reminders,
  calendars, time tracking, or other task-suite behavior for the Research Queue.
- Moving or duplicating the existing global ETF-performance skill into the
  project during this cutover.
- Changing ETF research methodology, source priority, return calculations,
  verification gates, region navigation, or durable output ownership.

## Further Notes

- The design-time Trello snapshot contained 69 Ready tickers, 3 Blocked
  tickers, no Backlog or In Progress cards, and 69 Done cards. The one-time seed
  should reread Ready and Blocked immediately before cutover because the active
  automation may change the snapshot.
- The existing ETF automation runs every three hours with a count of ten in the
  saved project using local scheduled-inline execution. Updating that automation
  is a cutover step, not a reason to create a second scheduled task.
- The two-hour rule is a renewable lease timeout, not a calculation from the
  card's generic update timestamp.
- Done and Cancelled cards remain queryable history. Intake and active Monitor
  views may hide them without moving or deleting their files.
