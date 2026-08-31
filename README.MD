# Stock Second Brain

Obsidian-native, source-backed public-equity and equity-ETF research vault. The
durable source of truth lives in `raw/` and `wiki/`; chat answers should stay
short and do not create files unless the request asks for durable work or
verified evidence materially changes an existing thesis.

## Quick Start

Use an explicit mode when the output shape matters:

| Mode | Use when | Contract |
|---|---|---|
| `chat` | General questions, why a stock moved, macro/theme outlook | <=400 words; no file writes |
| `lean` | Save, update, ingest, refresh, or decision work | Thin entity delta, compact memo, at most one chart |
| `full` | Explicit deep dive, archive, or full-chain research | More detail, but no duplicated tables or narrative |

Mode precedence is `mode:` first, then explicit `full/deep dive/archive`, then
save/update/ingest/refresh intent, then general-question routing to `chat`.

After durable work, keep the final chat handoff under 200 words.

## Markdown Research Queue

ใช้ project-scoped skills เพื่อสร้างและประมวลผลงานใน Obsidian โดย Intake
รับ ticker list ธรรมดาและสร้างการ์ด `Ready` ให้เอง

Use the project-scoped skills to create and process work in Obsidian. Intake
accepts a plain ticker list, Markdown bullets/table, or a project-relative file
and writes one Research Batch plus Ready Research Cards. ETF defaults to the
`check-etf-performance` route; Stock is reserved in the schema but remains
disabled until its processor ships.

```text
ใช้ $research-card-intake เพื่อ queue VIG, DGRO เป็น ETF
ใช้ $research-queue-manager ด้วย count: 1
```

Open `research-queue/Research Queue Intake.base` for the Ready/Blocked board
and `research-queue/Research Queue Monitor.base` for all statuses. The card
frontmatter is authoritative; Base Board and Bases are projections. CLI details
and the one-time Trello seed are documented in `research-queue/README.md`.

## Canonical Commands

### Explain A Market Move

```text
ใช้ $explain-market-move
mode: chat
ทำไม NVDA ขึ้นวันนี้
```

The skill verifies the session, timestamp, benchmark/sector performance, and
up to three evidence-labelled drivers. It corrects a false premise and does
not save a routine price explanation.

### Research A Theme Or Macro Scenario

```text
ใช้ $market-scenario-research
mode: chat
หลัง memory shortage คลายตัว AI bottleneck จะย้ายไปที่ไหน
```

```text
ใช้ $market-scenario-research
mode: chat
เศรษฐกิจญี่ปุ่นและ JPY ใน 12 เดือนข้างหน้ามี Base, Bull และ Bear scenario อะไรบ้าง
```

The output uses a causal chain, Base/Bull/Bear scenarios, three to five
signposts, and one falsifier. Save only when requested:

```text
ใช้ $market-scenario-research
mode: lean
บันทึกเป็น living note เรื่อง AI compute bottlenecks
```

### Find Latest Official Results

```text
ใช้ $latest-results-web สำหรับ MSFT
หา official latest results ตามลำดับ SEC/IR, earnings materials, financial statements แล้วสร้าง source note
```

Default durable profile is `minimal`: extract only facts needed by downstream
normalization, thesis, valuation, or the question. Use `full` only for explicit
archival extraction.

### Ingest A Source

```text
ใช้ $financial-facts-ingest
กับ raw/imports/MSFT_latest_results_source.md
mode: lean
normalize verified facts, update thin entity, และสร้าง JSON เฉพาะถ้าจำเป็น
```

Financial tables belong in `raw/financials/`; the entity links to them instead
of copying them. Market quotes stay in a dated market-data source or decision
check, not normalized company facts.

### Research An Equity ETF

ETF v1 supports passive, index-tracking equity funds. Always provide exchange
and ticker so listings cannot collide:

```text
ใช้ $official-source-etf-research สำหรับ AMEX:VIG
mode: full
สร้าง official source note, normalize fund facts, และอัปเดต thin ETF entity
```

The skill verifies sponsor, benchmark, passive status, official methodology,
holdings, costs, AUM/liquidity, NAV/price, tracking, distributions, FX, and
dated source compatibility. Durable files use `ETF_EXCHANGE_TICKER`:

```text
raw/imports/ETF_AMEX_VIG_fund_source_YYYY-MM-DD.md
raw/funds/ETF_AMEX_VIG_fund_facts.md
wiki/entities/ETF_AMEX_VIG.md
```

### Compare Or Decide On ETFs

```text
ใช้ $official-source-etf-research เปรียบเทียบ AMEX:VIG กับ AMEX:DGRO
mode: lean
เทียบ methodology, holdings overlap, concentration, expense, tracking และ income
```

```text
ใช้ $stock-decision-pipeline สำหรับ AMEX:VIG
instrument_type: ETF
mode: lean
refresh official ETF facts แล้วสรุป Portfolio Role + BUY/WATCH/AVOID
```

The ETF branch is `ETF research -> ETF decision`; it does not run company
stages P1/P4/P6/P7/P11. Without user-provided portfolio holdings, it reports
fund suitability only and does not claim portfolio fit or diversification.

### Run A New-Ticker Decision Pipeline

Lean is the default for durable pipeline work:

```text
ใช้ $stock-decision-pipeline สำหรับ ORCL
mode: lean
รัน P1 -> P4 -> P6 -> P11 stage gate -> P13
ถ้า P11 ทำ valuation ไม่ได้ ให้ส่ง blocker ไป P13 และไม่สร้าง valuation-gap memo
```

Use full only when you explicitly want archival depth:

```text
ใช้ $stock-decision-pipeline สำหรับ ORCL
mode: full
รัน full new-ticker decision-grade flow: P1 -> P4 -> P6 -> P11 -> P13
```

The pipeline uses one evidence set and this stage behavior:

1. P1 creates the official source note once.
2. P4 normalizes verified facts and creates a skeletal thin entity.
3. P6 completes the entity using the same evidence; it does not create a
   duplicate research memo without new durable analysis.
4. P11 creates a valuation memo only when inputs pass the valuation gate.
5. P13 creates one decision memo and receives a compact blocker when P11 stops.
6. `log.md` receives one pipeline bullet, not one bullet per stage.

### Refresh An Existing Ticker

```text
ใช้ $stock-decision-pipeline สำหรับ MSFT
mode: lean
อ่าน index.md, entity, fundamentals และ latest analysis ก่อน
ถ้าแค่ราคาปัจจุบันเปลี่ยน ให้รัน P13 เท่านั้น
ถ้า valuation stale ให้รัน P11 -> P13
ถ้า thesis stale ให้รัน P7 -> P11 -> P13
ถ้ามีงบใหม่ ให้รัน P1 -> P4 -> P7 -> optional P11 -> P13
```

### Run Direct Valuation Or Audit

```text
ใช้ $dcf-valuation สำหรับ MSFT
mode: lean
fresh check price, FCF, cash, debt, shares, guidance และทำ valuation gate ก่อนคำนวณ
```

```text
ใช้ $source-integrity-audit
mode: chat
ตรวจ scope `wiki/entities/MSFT.md` กับไฟล์ที่เกี่ยวข้องเรื่อง uncited numbers, stale data และ chart mismatch
```

Use `mode: lean` or `mode: full` for a saved audit memo. A scoped chat audit
does not write a file.

### Research Public Sentiment

```text
ใช้ $x-research สำหรับ NVDA หลัง earnings
mode: chat
สรุป bullish/bearish/mixed themes พร้อม confidence และ caveats
```

X/Twitter is context only and cannot replace filings, transcripts, or verified
financial facts.

## Pipeline Routing

### New Ticker

| Need | Flow | Main durable outputs |
|---|---|---|
| Foundation only | `P1 -> P4 -> P6` | source note, fundamentals, thin entity |
| New ticker with decision | `P1 -> P4 -> P6 -> P11 gate -> P13` | above plus decision; valuation only if ready |
| Explicit archive | same flow with `mode: full` | deeper narrative within full budgets |

### Existing Ticker

| Situation | Flow |
|---|---|
| Only current price changed | `P13` with fresh market data |
| Valuation assumptions stale | `P11 -> P13` |
| Thesis stale, no new results | `P7 -> optional P11 -> P13` |
| New quarter/year reported | `P1 -> P4 -> P7 -> optional P11 -> P13` |
| Source quality uncertain | `P10 -> fix decision-critical gaps -> P13` |

Do not infer upside/downside from price movement alone. If valuation inputs are
missing, write the blocker and prefer `wait` or `watchlist`.

### Equity ETF

| Situation | Flow | Main durable outputs |
|---|---|---|
| New supported ETF | `official-source-etf-research/deep-dive -> ETF decision` | ETF source, fund facts, entity, decision |
| Holdings/methodology/cost/tracking stale | `official-source-etf-research/thesis-delta -> ETF decision` | updated facts/entity/decision |
| Only price/NAV changed | fresh price/NAV check -> `ETF decision` | exchange-qualified decision memo |
| Peer or overlap question | ETF research -> comparison -> optional decision | comparison; decision only when requested |
| Source quality uncertain | `P10 ETF checks -> fix gaps -> ETF decision` | audit/fixes plus decision |

ETF valuation uses price/NAV, premium/discount, look-through multiples, yield,
expense drag, tracking, and compatible peers. It never creates a corporate DCF
or intrinsic-value target.

## Supported Skills

| Skill | Use when | Default output |
|---|---|---|
| `explain-market-move` | Why a stock, sector, ETF, index, commodity, or currency moved | chat |
| `market-scenario-research` | AI bottlenecks, themes, macro, rates, FX, and market regimes | chat |
| `latest-results-web` | Discover current official company results | source note |
| `financial-facts-ingest` | Normalize verified operating-company financial facts | fundamentals + entity delta |
| `official-source-stock-research` | Operating-company deep dive, earnings review, or thesis refresh | profile-dependent |
| `official-source-etf-research` | Passive equity ETF deep dive, comparison, refresh, or decision handoff | profile-dependent |
| `dcf-valuation` | Operating-company fair value, DCF, multiples, or sensitivity | valuation or blocker |
| `stock-decision-pipeline` | Chain or refresh company or supported ETF decision work | decision memo |
| `x-research` | Public X/Twitter sentiment | chat or sentiment memo |
| `source-integrity-audit` | Audit sources, numbers, links, charts, and gaps | chat or audit memo |

Detailed behavior belongs in `.codex/skills/*/SKILL.md`; this README only gives
the routing and copy-paste interface.

## Legacy P-Code Aliases

These aliases remain supported:

P1/P4/P6/P7/P11 are company stages. They do not apply to ETFs.

| Alias | Meaning |
|---|---|
| P1 | latest official source discovery |
| P4 | financial facts ingest |
| P6 | new-ticker company deep dive |
| P7 | existing-ticker thesis refresh |
| P10 | source integrity audit |
| P11 | valuation |
| P13 | decision memo |

Older labels such as P2, P3, P5, P8, P9, P12, P14, and P15 are not current
runtime aliases. Use the skill names above instead. There is no active local
`batch-screener` skill.

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
    funds/
    assets/
  wiki/
    entities/
    analysis/
      decisions/
      valuations/
      earnings/
      catalysts/
      comparisons/
      sentiment/
      audits/
    overview/
      themes/
      macro/
    reference/
  .codex/skills/
    explain-market-move/
    market-scenario-research/
    latest-results-web/
    financial-facts-ingest/
    official-source-stock-research/
    official-source-etf-research/
    dcf-valuation/
    stock-decision-pipeline/
    x-research/
    source-integrity-audit/
  .codex/agents/
    source-verifier.toml
```

## Source And Output Rules

Source priority:

1. SEC and official company filings
2. Earnings transcripts and call materials
3. Financial statements and metrics
4. News and web research
5. X/Twitter as lower-priority context

For ETFs use official issuer prospectus/product/factsheet and holdings first,
then official index methodology, regulator/exchange materials, and reputable
dated market data. Record separate as-of dates for each metric family.

Ownership is intentionally separated:

| Layer | Owns |
|---|---|
| `raw/imports/` | Raw evidence, source map, extraction gaps |
| `raw/financials/` | Normalized numbers, ratios, and source-backed tables |
| `raw/funds/` | Normalized ETF structure, holdings, cost, tracking, and methodology facts |
| `wiki/entities/` | Thin living company or exchange-qualified ETF summary and instrument-level gaps |
| `wiki/analysis/valuations/` | Valuation assumptions and calculations |
| `wiki/analysis/decisions/` | Action read and decision-changing evidence |
| `wiki/overview/themes/` | Living investment-theme scenarios |
| `wiki/overview/macro/` | Living country, rates, and FX scenarios |

Use links instead of copying full tables, source maps, bull/bear cases, or gap
lists across layers. Every durable number needs a URL, local path, filing
reference, or shown calculation. If a value cannot be verified, write
`ไม่พบข้อมูลที่ยืนยันได้` or `not disclosed`.

## Stop Conditions

Stop and report the exact gap when:

- ticker/company identity is ambiguous
- ETF exchange-qualified identity, benchmark, passive status, official
  methodology, or holdings cannot be verified
- official or traceable primary sources cannot be found
- period labels, currency, or units are unclear
- source conflicts change the conclusion and cannot be resolved
- current market data cannot be freshly checked for an action call
- valuation inputs are incomplete or unsuitable for a point estimate

ETF v1 does not support bond, commodity, multi-asset, active, leveraged,
inverse, or derivative-heavy funds. Stop with `unsupported ETF type` rather
than adapt company or passive-equity rules.

Do not force a target price, action, or scenario probability from unsupported
assumptions.
