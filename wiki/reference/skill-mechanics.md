# Skill Mechanics

Project skills live in `.codex/skills/SKILL-NAME/SKILL.md`. Match the user task
from frontmatter, read the selected skill, and follow its mode and output
contract.

## Mode Routing

| Signal | Mode |
|---|---|
| Explicit `mode:` | requested mode |
| full, deep dive, archive, legacy full chain | `full` |
| save, update, ingest, refresh, memo | `lean` |
| why, explain, outlook, predict, general question | `chat` |

## Prompt Aliases

| Alias | Skill/profile |
|---|---|
| P1 | `latest-results-web` |
| P4 | `financial-facts-ingest` |
| P6 | `official-source-stock-research` / new-ticker deep dive |
| P7 | `official-source-stock-research` / thesis refresh |
| P10 | `source-integrity-audit` |
| P11 | `dcf-valuation` |
| P13 | `stock-decision-pipeline` decision output |

## Available Local Skills

| Skill | Use when | Default output |
|---|---|---|
| `explain-market-move` | Why an asset moved over a recent window | chat |
| `market-scenario-research` | Theme, bottleneck, macro, rates, or FX scenarios | chat |
| `latest-results-web` | Latest official result discovery | source note |
| `financial-facts-ingest` | Normalize sourced financial facts | fundamentals + entity delta |
| `official-source-stock-research` | Deep dive, earnings, or thesis refresh | profile-dependent |
| `official-source-etf-research` | Passive equity ETF deep dive, comparison, or refresh | profile-dependent |
| `dcf-valuation` | Fair value or valuation sensitivity | valuation or compact blocker |
| `stock-decision-pipeline` | Chain or refresh a decision workflow | decision memo |
| `x-research` | Public market sentiment | chat |
| `source-integrity-audit` | Source and vault quality check | chat or audit memo |

## Instrument Routing

- `company`: use latest results, financial ingest, stock research, DCF, and the
  legacy P-code pipeline as applicable.
- `ETF`: require `entity_key: EXCHANGE:TICKER`; use
  `official-source-etf-research` and the ETF decision branch. Do not invoke
  P1/P4/P6/P7/P11.
- ETF v1 supports passive, index-tracking equity ETFs only. Stop for bond,
  commodity, multi-asset, active, leveraged, inverse, or derivative-heavy
  funds.

## Completion

Use links instead of duplicate content, append one workflow bullet to `log.md`,
answer briefly, validate changed skills, and commit only scoped files.
