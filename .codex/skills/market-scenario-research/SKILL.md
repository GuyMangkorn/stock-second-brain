---
name: market-scenario-research
description: Use when the user asks about future market regimes, investment themes, technology or supply-chain bottlenecks, country economies, monetary policy, interest rates, currencies, FX, or scenario-based market outlooks.
---

# Market Scenario Research

## Core Principle

Replace point prediction with a causal map, three scenarios, observable
signposts, and falsifiers. Separate sourced facts from assumptions and judgment.

## Reference Routing

- Read `references/technology-supply-chain.md` for AI, semiconductors, energy,
  infrastructure, capacity, shortage, and bottleneck-migration questions.
- Read `references/macro-fx.md` for country economies, central banks, rates,
  inflation, fiscal policy, capital flows, and currencies.
- Read both only when the causal chain genuinely crosses both domains.

## Default Mode

Use `chat` for general outlook, why, and prediction questions. Keep the answer
at or below 400 words and do not write files.

Use `lean` when the user asks to save or update durable knowledge. Maintain one
living note under `wiki/overview/themes/` or `wiki/overview/macro/`; update by
delta and append one workflow bullet to `log.md`. Do not create a generic
discussion note.

## Workflow

1. State the question, geography or value chain, and time horizon.
2. Freshly gather the minimum primary or authoritative facts needed to anchor
   the current state.
3. Map the causal chain: demand, constrained input, capacity response,
   substitution, policy or price feedback, and downstream beneficiaries/risks.
4. Identify the variable that clears the system and the slowest lead-time step.
5. Build `Base`, `Bull / Upside`, and `Bear / Downside` scenarios. Label
   assumptions; do not attach precise probabilities without a sourced basis.
6. Select three to five leading indicators that distinguish the scenarios.
7. State the strongest falsifier and what would change the view.

## Chat Output Recipe

1. `Bottom line`: direct answer and time horizon.
2. `Causal chain`: compact sequence showing why the outcome could occur.
3. `Scenarios`: one compact bullet each for base, bull, and bear.
4. `Signposts`: three to five measurable indicators.
5. `Falsifier`: the observation that would invalidate the base case.

Place citations beside current facts. Clearly label scenario statements as
analysis rather than company, government, or market-disclosed facts.

## Durable Output

Living notes contain:

- current thesis and as-of date
- causal map
- scenario table
- leading indicators and latest readings
- falsifiers
- compact source map
- dated change log containing only thesis deltas

Link ticker-specific implications to existing entity or catalyst notes. Do not
copy company financial tables, DCF inputs, or full decision memos.

## Common Mistakes

- Predicting without specifying a horizon.
- Listing trends without a causal mechanism or capacity response.
- Treating the base case as a fact.
- Ignoring price, substitution, policy, or demand-destruction feedback.
- Loading both references when only one domain is relevant.
