# Source Verifier Sub-Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a read-only `source_verifier` sub-agent and make it a mandatory pre-save evidence gate for durable stock-second-brain work.

**Architecture:** Keep the main agent as the only durable-file writer. The main agent prepares an evidence packet, dispatches `.codex/agents/source-verifier.toml`, receives `PASS`, `CHANGES_REQUIRED`, or `WARNING`, then saves only after resolving High/Medium findings or receiving user confirmation for Low findings.

**Tech Stack:** Codex custom-agent TOML, Markdown project instructions, Obsidian vault conventions, Python `tomllib` validation, Git.

## Global Constraints

- Use `.codex/agents/source-verifier.toml` as the project-scoped custom agent file.
- The reviewer is read-only and must not write vault files.
- Every durable number needs a URL, local path, filing reference, or shown calculation from sourced inputs.
- High and Medium findings block saving until correction and another review.
- Low findings require explicit user confirmation before saving.
- Keep Thai-first narrative and existing source-priority / missing-data rules.
- Preserve unrelated worktree changes and stage only files in this prompt's scope.

---

### Task 1: Create the custom source verifier

**Files:**
- Create: `.codex/agents/source-verifier.toml`

**Interfaces:**
- Consumes: an evidence packet containing candidate files, claims, calculations, sources, and as-of dates.
- Produces: a read-only review report with `PASS`, `CHANGES_REQUIRED`, or `WARNING` and evidence for every finding.

- [x] **Step 1: Define the required TOML identity fields**

Set `name = "source_verifier"`, a description that says it is an independent
read-only source and data reviewer, and a multiline `developer_instructions`
value.

- [x] **Step 2: Set read-only behavior**

Set `sandbox_mode = "read-only"`; do not add write-capable tools or instructions.

- [x] **Step 3: Encode the comparison and verdict contract**

Require source hierarchy, independent comparison, period/unit/currency/definition
reconciliation, source-date checks, calculation checks, severity classification,
and the exact save verdict behavior defined in the design spec.

- [x] **Step 4: Validate TOML syntax**

Run:

```bash
python3.12 -c 'import tomllib; from pathlib import Path; p=Path(".codex/agents/source-verifier.toml"); d=tomllib.loads(p.read_text()); assert {"name", "description", "developer_instructions"} <= d.keys(); assert d["name"] == "source_verifier"; assert d["sandbox_mode"] == "read-only"; print("valid source verifier TOML")'
```

Expected: `valid source verifier TOML`.

### Task 2: Wire the pre-save gate into project instructions

**Files:**
- Modify: `AGENTS.md` after `## Source Integrity Rules`
- Modify: `README.MD` project structure block

**Interfaces:**
- Consumes: the custom agent from Task 1 and the existing source-integrity rules.
- Produces: an explicit project-wide trigger and a discoverable `.codex/agents/` directory.

- [x] **Step 1: Add the pre-save protocol**

Document candidate drafting, evidence-packet preparation, dispatch of
`source_verifier`, waiting for its result, and the rule that only the main agent
may write durable files.

- [x] **Step 2: Add verdict handling**

Document that `CHANGES_REQUIRED` for High/Medium blocks writing and requires
correction plus re-review; `WARNING` for Low pauses for user confirmation;
`PASS` permits saving.

- [x] **Step 3: Add fallback and chat boundary**

Document the local checklist fallback when the sub-agent is unavailable and keep
read-only `chat` responses outside the pre-save gate.

- [x] **Step 4: Update the README structure**

Add `.codex/agents/source-verifier.toml` beside `.codex/skills/` without
duplicating the full protocol.

### Task 3: Record the durable workflow documentation

**Files:**
- Create: `docs/superpowers/specs/2026-08-09-source-verifier-agent-design.md`
- Create: `docs/superpowers/plans/2026-08-09-source-verifier-agent.md`
- Modify: `log.md` under `## 2026-08-09`

**Interfaces:**
- Consumes: the approved design and completed implementation files.
- Produces: traceable project documentation and one workflow log bullet.

- [x] **Step 1: Keep the design and implementation plan aligned**

Confirm that the verdict names, severity behavior, single-writer rule, and
fallback language match across the spec, plan, `AGENTS.md`, and TOML.

- [x] **Step 2: Add one concise log entry**

Record the agent file, pre-save gate, and validation outcome in one dated bullet;
do not add one bullet per artifact.

### Task 4: Verify the implementation and commit scoped changes

**Files:**
- Validate: `.codex/agents/source-verifier.toml`, `AGENTS.md`, `README.MD`, `log.md`, and the two docs files

**Interfaces:**
- Consumes: all completed files from Tasks 1–3.
- Produces: verified diff and a concise commit.

- [x] **Step 1: Run structural checks**

Run the TOML parser command from Task 1 with `python3.12` and:

```bash
rg -n "source_verifier|source-verifier|Pre-Save|pre-save|CHANGES_REQUIRED|WARNING" AGENTS.md README.MD .codex/agents/source-verifier.toml docs/superpowers/specs/2026-08-09-source-verifier-agent-design.md
```

Expected: the agent identity, gate, verdicts, and design references are present.

- [x] **Step 2: Review the diff and status**

Run `git diff --check`, `git diff --stat`, and `git status --short`; confirm no
unrelated files are changed and no placeholders remain in the spec or plan.

- [x] **Step 3: Stage only scoped files**

Stage the agent, `AGENTS.md`, `README.MD`, `log.md`, and the two documentation
files, excluding unrelated changes.

- [x] **Step 4: Commit the implementation**

Run:

```bash
git commit -m "feat: add pre-save source verifier agent"
```

Expected: a non-empty commit containing only the scoped implementation and
documentation.

## Self-review

- Spec coverage: the agent contract, pre-save trigger, severity gate, fallback,
  documentation, validation, and commit scope are covered by Tasks 1–4.
- Placeholder scan: no `TODO`, `TBD`, or unspecified test step is required.
- Boundary consistency: the agent reviews and reports; `AGENTS.md` orchestrates;
  the main agent alone writes durable files.
