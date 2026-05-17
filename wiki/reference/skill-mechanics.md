# Skill Mechanics

This project uses the Dexter SKILL model conceptually, without copying the
Dexter runtime.

## What A Skill Is

A skill is a folder containing `SKILL.md`.

Each `SKILL.md` begins with YAML frontmatter:

```yaml
---
name: skill-name
description: When this skill should be used.
---
```

The body is the operating manual for the agent:

- when to use the skill
- source priority
- workflow checklist
- output files
- stop conditions
- audit rules

## How The Agent Should Use Skills

1. Match the user's task to available skill descriptions.
2. Invoke the relevant skill early.
3. Follow the skill's checklist before writing durable output.
4. Read referenced files in `wiki/reference/` when the skill requires them.
5. Save durable output into `raw/` and `wiki/`.
6. Update `log.md`.
7. Answer briefly with paths, caveats, and next best step.

## Available Local Skills

| Skill | Use When | Main Output |
|---|---|---|
| `latest-results-web` | Need latest official source discovery | `raw/imports/TICKER_latest_results_source.md` |
| `financial-facts-ingest` | Need to normalize filings, tables, transcripts, Markdown, or CSV | `raw/financials/TICKER_fundamentals.md`, `wiki/entities/TICKER.md` |
| `official-source-stock-research` | Need deep dive, thesis refresh, earnings review, or comparison | entity updates and analysis memos |

## Why This Matters

The SKILL model keeps research repeatable:

- the agent does not improvise a new process every time
- source hierarchy remains consistent
- outputs land in predictable Obsidian paths
- missing data is preserved instead of hidden
- prompt examples become reliable operating commands

## No Runtime Dependency

Dexter's original implementation scans skill folders and exposes metadata to an
LLM tool. This vault does not include that code. The useful part for this
project is the workflow contract: a skill is a Markdown playbook that the agent
must follow.

