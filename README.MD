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
- Language style: Thai-first narrative analysis with English headings,
  structured fields, ticker/source labels, and finance terms such as DCF, FCF,
  WACC, valuation, and margin of safety kept in English for precision and
  searchability.
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

Dexter skill mapping:

| Dexter skill | Stock Second Brain skill | Status |
|---|---|---|
| `stock-research` | `official-source-stock-research` | Adapted for Obsidian entity/source notes. |
| `dcf-valuation` | `dcf-valuation` | Adapted for source-backed valuation memos. |
| `x-research` | `x-research` | Adapted as lower-priority sentiment/context, not fact source. |

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
      dcf-valuation/
      x-research/
      source-integrity-audit/
      stock-decision-pipeline/
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

X/Twitter sentiment is a separate lower-priority context layer. It should never
override official filings, transcripts, or verified financial facts.

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

### 4. DCF Valuation

Use `.codex/skills/dcf-valuation/SKILL.md`.

Goal: estimate fair value through a transparent, source-backed DCF, with
explicit assumptions and sensitivity matrix.

Expected output:

- `wiki/analysis/TICKER DCF Valuation YYYY-MM-DD.md`
- input table, FCF projection, valuation summary, sensitivity matrix
- entity update only when the valuation changes thesis or watch items
- `log.md` entry

### 5. X / Market Sentiment

Use `.codex/skills/x-research/SKILL.md`.

Goal: capture public market sentiment as context, not as a source of financial
facts.

Expected output:

- `wiki/analysis/TICKER X Sentiment YYYY-MM-DD.md`
- bullish/bearish/mixed themes
- caveats about sample bias and rumor risk
- entity follow-up update only when useful

### 6. Decision-Grade Pipeline

Use `.codex/skills/stock-decision-pipeline/SKILL.md`.

Goal: chain the common decision workflow from source discovery to financial
facts, entity thesis, valuation, and a final decision memo.

Expected output for a new ticker:

- `raw/imports/TICKER_latest_results_source.md`
- `raw/financials/TICKER_fundamentals.md`
- `wiki/entities/TICKER.md`
- `wiki/analysis/TICKER DCF Valuation YYYY-MM-DD.md`
- `wiki/analysis/TICKER Decision Memo YYYY-MM-DD.md`
- `log.md` entries

For an existing ticker, use the lightest sufficient refresh: P13 only when the
vault and latest DCF are still valid, P11 -> P13 when valuation is stale, or
P7 -> P11 -> P13 when the thesis also needs refresh.

### 7. Source Integrity Audit

Use `.codex/skills/source-integrity-audit/SKILL.md`.

Goal: lint the vault for source gaps, stale current data, unsupported numbers,
chart/table mismatches, orphan notes, and missing links.

Expected output:

- `wiki/analysis/Source Integrity Audit YYYY-MM-DD.md`
- severity-ranked findings
- fixes applied when requested
- `log.md` entry

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
| Latest Results Source Discovery | It asks the agent to find official latest sources first. | `raw/imports/TICKER_latest_results_source.md` |
| SEC Filing First | It starts from SEC/official filings before writing notes. | source note plus entity update |
| Earnings Transcript Digest | It asks the agent to find or verify a transcript source. | `wiki/analysis/TICKER Earnings Transcript Digest YYYY-MM-DD.md` |
| News / Catalyst Update | It can search current news, but must label news as lower-priority context. | catalyst memo |
| Company Deep Dive | It includes official-source research and can build the first entity page. | `wiki/entities/TICKER.md` |
| Stock Decision Pipeline | It chains source discovery, ingest, thesis, DCF, and decision memo. | source note, fundamentals, entity page, valuation memo, decision memo |
| Batch Screener | It starts from a ticker list or screener file, but output is triage, not a decision-grade memo. | screener triage memo |
| X Sentiment | It can start from a ticker/event and search public sentiment when X/search access exists. | sentiment memo |

#### Needs Existing Vault Data Or Source Files

Use these after at least one source note, entity page, or normalized financial
file exists:

| Prompt | Required input | Run this first if missing |
|---|---|---|
| Financial Statements Normalize | `raw/imports/TICKER_latest_results_source.md` or another source file | Latest Results Source Discovery or SEC Filing First |
| Thesis Refresh | `wiki/entities/TICKER.md` and ideally `raw/financials/TICKER_fundamentals.md` | Company Deep Dive or Financial Statements Normalize |
| Compare Companies | entity/fundamentals files for the compared tickers | Company Deep Dive for each ticker |
| Query The Vault | enough notes in `index.md`, `wiki/entities/`, or `wiki/analysis/` | ingest one or more tickers first |
| Source Integrity Audit | a non-empty vault with multiple notes | create or ingest source/entity notes first |
| Decision Memo | entity thesis plus current price/valuation if action depends on market data | Company Deep Dive, then refresh current market data |
| Decision Memo Price Refresh | existing entity/fundamentals and preferably latest DCF | P13 only if valuation is still valid; otherwise P11 -> P13 |
| DCF Valuation | verified FCF, cash/debt, shares, current price, and assumptions | Latest Results Source Discovery, Financial Statements Normalize, then fresh market-data check |

#### Recommended Flow For A New Ticker

ใช้ส่วนนี้เมื่อ ticker ยังไม่มี entity page หรือ financial facts ใน vault.
ถ้าไม่แน่ใจว่าจะเริ่มตรงไหน ให้ใช้ **Scenario N1**.

| Scenario | ใช้เมื่อ | Prompt order | ผลลัพธ์ที่ควรได้ |
|---|---|---|---|
| N1: Full Foundation | หุ้นใหม่และอยากสร้างฐานข้อมูลให้ครบ | P1 -> P4 -> P6 | source note, fundamentals, entity page |
| N2: มี source/filing อยู่แล้ว | คุณมี SEC/IR URL, filing excerpt, Markdown, หรือ CSV แล้ว | P2 หรือ P4 -> P6 | ingest จาก source ที่มี แล้วสร้าง thesis/entity |
| N3: อยากอ่านเร็ว ยังไม่ ingest เต็ม | ต้องการ company deep dive แบบเร็ว แต่ยังไม่ต้อง normalize งบ | P6 | entity/memo แบบ source-grounded พร้อม data gaps |
| N4: เพิ่งประกาศงบ | มี earnings ล่าสุดและอยากเก็บงบ + transcript | P1 -> P4 -> P3 -> P6 | latest financials, transcript digest, thesis update |
| N5: อยากรู้ fair value | ต้องการ valuation หรือ upside/downside | P1 -> P4 -> P6 -> P11 | source-backed DCF memo |
| N6: มีข่าว/event ใหญ่ | หุ้นใหม่มี catalyst/news/controversy | P1 -> P5 -> P6 -> optional P12 | catalyst memo + entity update + sentiment context |
| N7: มาจาก screener list | มีหลาย ticker และต้องเลือกตัวที่จะขุดต่อ | P14 -> เลือก top names -> N1/N5 | screener triage แล้วค่อย full pipeline เฉพาะตัวที่ผ่าน |
| N8: Decision-grade ตั้งแต่ศูนย์ | หุ้นใหม่และอยากได้ decision memo พร้อม valuation | P15 หรือ P1 -> P4 -> P6 -> P11 -> P13 | source note, fundamentals, entity page, DCF, decision memo |

Prompt chain ที่ใช้บ่อยสุด:

```text
P1 -> P4 -> P6
```

ถ้าจะทำ decision-grade เพิ่ม:

```text
P15
หรือ
P1 -> P4 -> P6 -> P11 -> P13 -> optional P10
```

#### Recommended Flow For An Existing Ticker

ใช้ส่วนนี้เมื่อมี `wiki/entities/TICKER.md` หรือ
`raw/financials/TICKER_fundamentals.md` อยู่แล้ว. ถ้าไม่แน่ใจ ให้ใช้
**Scenario E1**.

| Scenario | ใช้เมื่อ | Prompt order | ผลลัพธ์ที่ควรได้ |
|---|---|---|---|
| E1: Refresh จาก vault เดิม | อยากรู้ thesis ล่าสุดจากข้อมูลที่มีอยู่ | P7 | thesis ดีขึ้น/แย่ลง/เหมือนเดิม พร้อม gaps |
| E2: มีงบใหม่ | บริษัทเพิ่งประกาศ quarter/year ใหม่ | P1 -> P4 -> P7 | update fundamentals + refresh entity/thesis |
| E3: Update valuation | อยากดู fair value ใหม่หรือราคาเปลี่ยนแรง | P7 -> P11 -> P13 | valuation memo + decision memo |
| E4: ข่าวหรือ catalyst ใหม่ | มีข่าว, product launch, regulation, M&A, downgrade/upgrade | P5 -> P7 -> optional P12 | catalyst note + thesis impact |
| E5: เทียบกับหุ้นอื่น | อยากเทียบ ticker นี้กับ peer หรือ basket | P7 ของแต่ละตัวถ้าข้อมูลเก่า -> P8 | comparison memo |
| E6: ถามจาก vault | อยาก query ข้อมูลที่สะสมไว้ ไม่อยากค้นเว็บใหม่ | P9 | answer จาก vault พร้อมไฟล์อ้างอิง |
| E7: ก่อนตัดสินใจจริง | ต้องการตรวจว่า note/source/chart น่าเชื่อถือไหม | P10 -> fix gaps -> P13 | audit memo + decision memo |
| E8: Sentiment หลัง event | price action แรงหรือ market chatter สำคัญ | P12 -> P7 | sentiment context + thesis refresh |
| E9: มี data แล้ว แค่อัปเดต decision ด้วยราคาปัจจุบัน | entity/fundamentals มีอยู่ และ DCF ล่าสุดยังน่าจะใช้ได้ | P13 เท่านั้น ถ้า valuation ยัง valid; ถ้า stale ใช้ P11 -> P13 | decision memo ใหม่พร้อม fresh price check |

Prompt chain ที่ใช้บ่อยสุด:

```text
P7
```

ถ้ามีงบใหม่:

```text
P1 -> P4 -> P7
```

ถ้าจะตัดสินใจซื้อ/ขาย:

```text
P7 -> P11 -> P10 -> P13
```

ถ้ามี data และ DCF อยู่แล้ว แค่อยากอัปเดต decision memo จากราคาปัจจุบัน:

```text
P13 only ถ้า thesis และ valuation assumptions ยัง valid
P11 -> P13 ถ้า valuation stale หรือราคาเปลี่ยนจน upside/downside เปลี่ยนมาก
P7 -> P11 -> P13 ถ้า thesis หรือ business facts อาจ stale
P1 -> P4 -> P7 -> P11 -> P13 ถ้ามีงบใหม่ที่ยังไม่ได้ ingest
```

### P1 - Latest Results Source Discovery

```text
ใช้ skill latest-results-web สำหรับ MSFT
หา source ทางการล่าสุดตามลำดับ SEC filings, earnings transcript, financial statements, news
แล้วสร้าง raw/imports/MSFT_latest_results_source.md
เขียน Handoff For Ingest ให้ชัดสำหรับ P4
ยังไม่ต้อง normalize งบหรืออัปเดต wiki/entities/MSFT.md ในขั้นนี้
```

### P2 - SEC Filing First

```text
ใช้ official-source-stock-research สำหรับ AAPL
เริ่มจาก 10-Q/10-K ล่าสุดและ 8-K earnings release ก่อน
ดึง revenue, gross margin, operating income, EPS, cash flow, capex, share count
บันทึกเป็น raw/imports/AAPL_sec_filing_source.md แล้ว ingest เข้า entity note
```

### P3 - Earnings Transcript Digest

```text
อ่าน earnings transcript ล่าสุดของ NVDA จากแหล่งทางการหรือ transcript ที่ trace กลับได้
สรุป management commentary, demand signals, supply constraints, guidance tone,
และ Q&A ที่กระทบ thesis
บันทึกเป็น wiki/analysis/NVDA Earnings Transcript Digest YYYY-MM-DD.md
และ update follow-up ใน wiki/entities/NVDA.md
```

### P4 - Financial Statements Normalize

```text
ใช้ financial-facts-ingest กับ raw/imports/MSFT_latest_results_source.md
normalize periods ตาม source labels เท่านั้น
สร้าง financial table, key ratios ที่ input ครบ, quarterly/YTD/annual charts,
missing data registry และ update wiki/entities/MSFT.md
ถ้าข้อมูลยืนยันไม่ได้ให้เขียนว่า ไม่พบข้อมูลที่ยืนยันได้
```

### P5 - News / Catalyst Update

```text
อัปเดต catalyst note ของ PANW จากข่าวล่าสุด
ใช้ news เป็น source ชั้นที่ 4 เท่านั้น และแยกชัดว่าอะไรเป็น official filing,
อะไรเป็น transcript, อะไรเป็น financial metric, และอะไรเป็น news context
ถ้า insight durable ให้บันทึกใน wiki/analysis/PANW Catalyst Update YYYY-MM-DD.md
```

### P6 - Company Deep Dive

```text
ใช้ official-source-stock-research ทำ company deep dive ของ ASML
ต้องมี business model, segments, revenue mix, moat, risks, catalysts,
valuation watch items, source map, และ unanswered questions
output หลักเป็น wiki/entities/ASML.md และถ้าจำเป็นให้สร้าง memo ใน wiki/analysis/
```

### P7 - Thesis Refresh

```text
refresh thesis ของ MSFT จากข้อมูลล่าสุดใน vault
อ่าน index.md ก่อน แล้วอ่าน wiki/entities/MSFT.md, raw/financials/MSFT_fundamentals.md,
และ analysis notes ที่เกี่ยวข้อง
ตอบว่า thesis ดีขึ้น แย่ลง หรือเหมือนเดิม พร้อม source-backed evidence
ถ้าควรเก็บถาวร ให้ update Thesis History ใน entity page
```

### P8 - Compare Companies

```text
เทียบ NVDA, AMD, AVGO จากข้อมูลใน stock-second-brain
ใช้ entity notes และ normalized financials เป็นหลัก
ถ้า data gap สำคัญ ให้ mark gap แทนการเดา
สร้าง comparison memo ใน wiki/analysis/AI Semis Comparison YYYY-MM-DD.md
```

### P9 - Query The Vault

```text
จาก stock-second-brain ตอนนี้มีบริษัทไหนที่ revenue growth ดีแต่ source_gap_count สูง
อ่าน index.md และ wiki/entities/ ก่อน
ตอบพร้อม link ไปยัง entity pages และบอกว่า gap ไหนต้องหาต่อ
```

### P10 - Source Integrity Audit

```text
ใช้ skill source-integrity-audit lint stock-second-brain ให้หน่อย
หา uncited numbers, source conflicts, stale thesis, orphan notes,
chart/table mismatch, entity ที่ไม่มี fundamentals file,
และ analysis memo ที่ไม่ได้ link กลับ entity
เขียนผลไว้ที่ wiki/analysis/Source Integrity Audit YYYY-MM-DD.md
```

### P11 - DCF Valuation

```text
ใช้ skill dcf-valuation สำหรับ MSFT
อ่าน wiki/entities/MSFT.md และ raw/financials/MSFT_fundamentals.md ก่อน
fresh check ราคาปัจจุบัน, market cap, shares, cash, debt, FCF และ guidance
ทำ base/bull/bear assumptions, 5-year FCF projection, sensitivity matrix,
sanity checks และ caveats
บันทึกเป็น wiki/analysis/MSFT DCF Valuation YYYY-MM-DD.md
```

### P12 - X / Market Sentiment

```text
ใช้ skill x-research สำหรับ NVDA หลัง earnings ล่าสุด
สรุป public sentiment เป็น bullish/bearish/mixed themes
แยก expert posts, retail chatter, source-backed posts และ rumor/noise
อย่าใช้ X เป็นแหล่งตัวเลขงบหรือ valuation
บันทึกเป็น wiki/analysis/NVDA X Sentiment YYYY-MM-DD.md
```

### P13 - Decision Memo

```text
สร้าง decision memo สำหรับ MSFT ว่าควร add, hold, wait หรือ trim
ใช้ข้อมูลใน vault เป็นหลัก ถ้าต้องใช้ราคาหรือ valuation ปัจจุบันให้ค้นใหม่
แยก facts, assumptions, calculations, และ judgment
บันทึกใน wiki/analysis/MSFT Decision Memo YYYY-MM-DD.md
```

### P14 - Batch Screener

Use directly when you already have a ticker list and want triage first. For
decision-grade output, use Batch Screener to select top candidates, then run
`latest-results-web -> financial-facts-ingest -> official-source-stock-research`
on the shortlist.

```text
นี่คือ screener list: MSFT, NVDA, ASML, PANW, NOW
ทำ triage ก่อน ไม่ต้อง full report ทุกตัว
อ่าน index.md และ wiki/entities/ ก่อนเพื่อดูว่าตัวไหนมีข้อมูลใน vault แล้ว
จัดอันดับจาก quality, valuation risk, catalyst density, downside risk,
source coverage และ data gaps
บันทึกเป็น wiki/analysis/Screener Triage YYYY-MM-DD.md
แนะนำ top 1-3 ตัวที่จะรัน latest-results-web ต่อ
```

### P15 - Stock Decision Pipeline

Use this when you want the common chain to run as one workflow.

New ticker / decision-grade from zero:

```text
ใช้ skill stock-decision-pipeline สำหรับ MSFT
รัน full new-ticker decision-grade flow: P1 -> P4 -> P6 -> P11 -> P13
P1 ให้สร้าง source note เท่านั้น, P4 ค่อย normalize และ update entity
fresh check current price, market cap, shares, cash, debt, FCF และ guidance ก่อน P11/P13
ถ้าขั้นไหน source ไม่พอ ให้หยุดและเขียน Missing / Unverified Data แทนการเดา
บันทึก durable outputs และ log.md ทุกขั้นที่มีการ update
```

Existing data / update decision memo with current price:

```text
ใช้ skill stock-decision-pipeline สำหรับ MSFT
vault มี entity/fundamentals และอาจมี DCF แล้ว
อ่าน index.md, wiki/entities/MSFT.md, raw/financials/MSFT_fundamentals.md,
และ valuation/decision memo ล่าสุดใน wiki/analysis/
fresh check ราคาปัจจุบันและ market data ที่จำเป็น
ถ้า thesis และ valuation assumptions ยัง valid ให้รัน P13 เท่านั้น
ถ้า valuation stale ให้รัน P11 -> P13
ถ้า thesis stale ให้รัน P7 -> P11 -> P13
บันทึกเป็น wiki/analysis/MSFT Decision Memo YYYY-MM-DD.md
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
