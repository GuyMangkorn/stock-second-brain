# 06: Deliver the Obsidian Intake and Monitor experience

**What to build:** Complete the Obsidian operating surface so humans can add and hold work easily while automation state remains authoritative in Research Card properties.

**Blocked by:** 02, 05

**Status:** ready-for-agent

- [ ] A Base Board presents Ready and Blocked cards as the primary intake/hold workspace.
- [ ] A native Bases monitor presents Ready, In Progress, Blocked, Done, and Cancelled cards with useful timestamps, workflow, instrument, owner, lease, and output links.
- [ ] Board and monitor views read status and metadata directly from Research Card properties; column placement is not a second source of truth.
- [ ] A human can move Ready to Blocked, Blocked to Ready, and non-terminal work to Cancelled through the documented operating flow.
- [ ] In Progress and Done transitions are documented and enforced as automation-owned.
- [ ] Done and Cancelled cards remain discoverable at stable durable locations rather than being deleted or moved into ephemeral storage.
- [ ] View counts reconcile with the cards on disk for every status.
- [ ] Classic Kanban is optional presentation only and is not required for state transitions or monitoring.
- [ ] A smoke test verifies view parsing, status coverage, stable links, and count reconciliation in a representative temporary vault.
