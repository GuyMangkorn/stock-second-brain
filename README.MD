# Stock Second Brain

Obsidian-native stock research project for building a durable equity research
second brain. This folder intentionally does **not** copy the Bun CLI from
`dexter-clone`; it borrows the agent workflow and SKILL style: source-first
planning, explicit checklists, tool/source selection, self-audit, and durable
notes.

## Design Choices

This project follows the requirements:

- Goal: full research OS, combining agent workflow, second-brain storage,
  source ingest, and report-ready notes.
- Primary output: Obsidian Markdown notes.
- MVP scope: ingest data into a Markdown vault.
- Source priority: SEC filings, earnings transcripts, financial statements /
  metrics, then news and web research.
- Architecture source: use `dexter-clone` workflow/SKILL behavior as the model,
  not its Bun runtime or CLI code.
- Folder name: `stock-second-brain`.

## What Comes From Dexter

The important Dexter ideas copied conceptually are:

- A skill is a Markdown instruction file with YAML frontmatter:
  `name` and `description`.
- The agent should invoke the relevant skill early when the user task matches
  the skill description.
- Each skill returns workflow instructions, source priority, output shape, and
  stop conditions.
- Complex research is done as an iterative loop: plan, gather sources, extract
  facts, write to a scratch/durable artifact, audit gaps, then answer.
- The final answer should be short; the durable knowledge should live in files.

See `wiki/reference/skill-mechanics.md` for the exact SKILL operating model used
by this project.

What is intentionally **not** copied:

- Bun runtime
- CLI UI
- TypeScript agent loop
- provider/tool registry implementation
- package files

## Project Structure

```text
stock-second-brain/
  README.MD
  AGENTS.md
  index.md
  log.md
  raw/
    imports/
    financials/
    assets/
  wiki/
    entities/
    analysis/
    overview/
    reference/
  .codex/
    skills/
      official-source-stock-research/
      latest-results-web/
      financial-facts-ingest/
```

## Source Priority

Use this default order unless a task explicitly says otherwise:

1. SEC filings and official company filings: 10-K, 10-Q, 8-K, 20-F, annual
   reports, quarterly reports, proxy statements, official IR-hosted filings.
2. Earnings transcripts and call materials: official webcast transcript,
   company transcript, earnings call, prepared remarks, Q&A, shareholder letter.
3. Financial statements and metrics: official financial tables, company data
   books, investor presentations, structured statement data, market ratios.
4. News and web research: reputable news, sell-side summaries, market context,
   and recent events not yet covered in official sources.

If sources conflict, record the conflict instead of forcing a clean answer.
Every durable number should trace back to a URL, local path, filing, or explicit
calculation from sourced inputs.

## Core Workflows

### 1. Discover Latest Official Sources

Use `.codex/skills/latest-results-web/SKILL.md`.

Goal: find official SEC/IR/transcript/financial sources, then save a traceable
raw source note in `raw/imports/`.

Expected output:

- `raw/imports/TICKER_latest_results_source.md`
- source URLs
- periods found
- currency and units
- missing/unverified fields
- handoff note for ingest

### 2. Ingest Financial Facts

Use `.codex/skills/financial-facts-ingest/SKILL.md`.

Goal: normalize facts from a source note, filing excerpt, transcript, financial
table, Markdown file, or CSV into Obsidian-readable company facts.

Expected output:

- `raw/financials/TICKER_fundamentals.md`
- optional `raw/financials/TICKER_fundamentals.json` if structured arrays are useful
- `wiki/entities/TICKER.md`
- `log.md` entry

### 3. Official-Source Stock Research

Use `.codex/skills/official-source-stock-research/SKILL.md`.

Goal: produce a durable company note or research memo using the official source
stack first, then secondary context.

Expected output:

- entity page update in `wiki/entities/TICKER.md`
- optional analysis memo in `wiki/analysis/`
- source-backed thesis, risks, catalysts, and watch items

## Prompt Examples

### Prompt Dependency Guide

The prompt examples below are entry points, not a single required wizard. Some
prompts can start from zero because they include source discovery. Others assume
the vault already contains source notes, normalized facts, or entity pages.

#### Can Start From Zero

Use these as standalone prompts when the ticker is known and the agent has web
or filing access:

| Prompt | Why it can run alone | Expected first output |
|---|---|---|
| Latest Results Ingest | It asks the agent to find official latest sources first. | `raw/imports/TICKER_latest_results_source.md` |
| SEC Filing First | It starts from SEC/official filings before writing notes. | source note plus entity update |
| Earnings Transcript Digest | It asks the agent to find or verify a transcript source. | `wiki/analysis/TICKER Earnings Transcript Digest YYYY-MM-DD.md` |
| News / Catalyst Update | It can search current news, but must label news as lower-priority context. | catalyst memo |
| Company Deep Dive | It includes official-source research and can build the first entity page. | `wiki/entities/TICKER.md` |
| Batch Screener | It starts from a ticker list supplied in the prompt. | screener triage memo |

#### Needs Existing Vault Data Or Source Files

Use these after at least one source note, entity page, or normalized financial
file exists:

| Prompt | Required input | Run this first if missing |
|---|---|---|
| Financial Statements Normalize | `raw/imports/TICKER_latest_results_source.md` or another source file | Latest Results Ingest or SEC Filing First |
| Thesis Refresh | `wiki/entities/TICKER.md` and ideally `raw/financials/TICKER_fundamentals.md` | Company Deep Dive or Financial Statements Normalize |
| Compare Companies | entity/fundamentals files for the compared tickers | Company Deep Dive for each ticker |
| Query The Vault | enough notes in `index.md`, `wiki/entities/`, or `wiki/analysis/` | ingest one or more tickers first |
| Source Integrity Audit | a non-empty vault with multiple notes | create or ingest source/entity notes first |
| Decision Memo | entity thesis plus current price/valuation if action depends on market data | Company Deep Dive, then refresh current market data |

#### Recommended Flow For A New Ticker

```text
1. ใช้ skill latest-results-web สำหรับ TICKER
2. ใช้ financial-facts-ingest กับ raw/imports/TICKER_latest_results_source.md
3. ใช้ official-source-stock-research ทำ thesis/entity update
4. สร้าง decision memo หรือ comparison หลังมีข้อมูลใน vault แล้ว
```

#### Recommended Flow For An Existing Ticker

```text
1. refresh thesis ของ TICKER จากข้อมูลล่าสุดใน vault
2. ถ้าข้อมูลเก่า ให้ใช้ latest-results-web เพื่อหา official source ใหม่
3. ingest source ใหม่ด้วย financial-facts-ingest
4. update entity page, thesis history, follow-up, และ log.md
```

### Latest Results Ingest

```text
ใช้ skill latest-results-web สำหรับ MSFT
หา source ทางการล่าสุดตามลำดับ SEC filings, earnings transcript, financial statements, news
แล้วสร้าง raw/imports/MSFT_latest_results_source.md
จากนั้นใช้ skill financial-facts-ingest เพื่ออัปเดต wiki/entities/MSFT.md
```

### SEC Filing First

```text
ใช้ official-source-stock-research สำหรับ AAPL
เริ่มจาก 10-Q/10-K ล่าสุดและ 8-K earnings release ก่อน
ดึง revenue, gross margin, operating income, EPS, cash flow, capex, share count
บันทึกเป็น raw/imports/AAPL_sec_filing_source.md แล้ว ingest เข้า entity note
```

### Earnings Transcript Digest

```text
อ่าน earnings transcript ล่าสุดของ NVDA จากแหล่งทางการหรือ transcript ที่ trace กลับได้
สรุป management commentary, demand signals, supply constraints, guidance tone,
และ Q&A ที่กระทบ thesis
บันทึกเป็น wiki/analysis/NVDA Earnings Transcript Digest YYYY-MM-DD.md
และ update follow-up ใน wiki/entities/NVDA.md
```

### Financial Statements Normalize

```text
ใช้ financial-facts-ingest กับ raw/imports/MSFT_latest_results_source.md
normalize periods ตาม source labels เท่านั้น
สร้าง financial table, key ratios ที่ input ครบ, quarterly/YTD/annual charts,
missing data registry และ update wiki/entities/MSFT.md
ถ้าข้อมูลยืนยันไม่ได้ให้เขียนว่า ไม่พบข้อมูลที่ยืนยันได้
```

### News / Catalyst Update

```text
อัปเดต catalyst note ของ PANW จากข่าวล่าสุด
ใช้ news เป็น source ชั้นที่ 4 เท่านั้น และแยกชัดว่าอะไรเป็น official filing,
อะไรเป็น transcript, อะไรเป็น financial metric, และอะไรเป็น news context
ถ้า insight durable ให้บันทึกใน wiki/analysis/PANW Catalyst Update YYYY-MM-DD.md
```

### Company Deep Dive

```text
ใช้ official-source-stock-research ทำ company deep dive ของ ASML
ต้องมี business model, segments, revenue mix, moat, risks, catalysts,
valuation watch items, source map, และ unanswered questions
output หลักเป็น wiki/entities/ASML.md และถ้าจำเป็นให้สร้าง memo ใน wiki/analysis/
```

### Thesis Refresh

```text
refresh thesis ของ MSFT จากข้อมูลล่าสุดใน vault
อ่าน index.md ก่อน แล้วอ่าน wiki/entities/MSFT.md, raw/financials/MSFT_fundamentals.md,
และ analysis notes ที่เกี่ยวข้อง
ตอบว่า thesis ดีขึ้น แย่ลง หรือเหมือนเดิม พร้อม source-backed evidence
ถ้าควรเก็บถาวร ให้ update Thesis History ใน entity page
```

### Compare Companies

```text
เทียบ NVDA, AMD, AVGO จากข้อมูลใน stock-second-brain
ใช้ entity notes และ normalized financials เป็นหลัก
ถ้า data gap สำคัญ ให้ mark gap แทนการเดา
สร้าง comparison memo ใน wiki/analysis/AI Semis Comparison YYYY-MM-DD.md
```

### Query The Vault

```text
จาก stock-second-brain ตอนนี้มีบริษัทไหนที่ revenue growth ดีแต่ source_gap_count สูง
อ่าน index.md และ wiki/entities/ ก่อน
ตอบพร้อม link ไปยัง entity pages และบอกว่า gap ไหนต้องหาต่อ
```

### Source Integrity Audit

```text
lint stock-second-brain ให้หน่อย
หา uncited numbers, source conflicts, stale thesis, orphan notes,
entity ที่ไม่มี fundamentals file, และ analysis memo ที่ไม่ได้ link กลับ entity
เขียนผลไว้ที่ wiki/analysis/Source Integrity Audit YYYY-MM-DD.md
```

### Decision Memo

```text
สร้าง decision memo สำหรับ MSFT ว่าควร add, hold, wait หรือ trim
ใช้ข้อมูลใน vault เป็นหลัก ถ้าต้องใช้ราคาหรือ valuation ปัจจุบันให้ค้นใหม่
แยก facts, assumptions, calculations, และ judgment
บันทึกใน wiki/analysis/MSFT Decision Memo YYYY-MM-DD.md
```

### Batch Screener

```text
นี่คือ screener list: MSFT, NVDA, ASML, PANW, NOW
ทำ triage ก่อน ไม่ต้อง full report ทุกตัว
จัดอันดับจาก quality, valuation, catalyst density, downside risk, source coverage
และ data gaps
บันทึกเป็น wiki/analysis/Screener Triage YYYY-MM-DD.md
```

## Output Standards

Entity pages live in `wiki/entities/TICKER.md` and should include:

- Snapshot
- Source Map
- Business Model
- Segments / Revenue Mix
- Financial Facts
- Charts
- Transcript / Management Commentary
- Thesis
- Risks
- Catalysts
- Valuation Watch Items
- Reports / Source Notes
- Follow-Up
- Missing / Unverified Data

Raw source notes live in `raw/imports/` and should preserve:

- URLs or local source paths
- filing type or source kind
- publication date
- reporting period
- currency and units
- extracted tables or source-backed excerpts
- missing/unverified fields

Financial facts live in `raw/financials/` and should be repeatable:

- do not overwrite source meaning
- keep period labels as stated by the source
- calculate only ratios with complete inputs
- label every calculation
- keep source gaps visible

## Stop Conditions

Stop and report `ไม่พบข้อมูลที่ยืนยันได้` when:

- no official source can be found
- ticker/company identity is ambiguous
- period labels, currency, or units are unclear
- source data conflicts and cannot be resolved
- ratio inputs are incomplete
- source is only a secondary summary with no traceable primary source
