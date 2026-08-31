# 01: Queue one ETF Research Card from plain language

**What to build:** Deliver the thinnest end-to-end Intake slice: an explicit natural-language request for one ETF creates one Research Batch and one Ready Research Card through the deterministic queue interface, then exposes that card in Obsidian.

**Blocked by:** None

**Status:** ready-for-agent

- [ ] An explicit request to create, add, or queue one ETF produces exactly one Research Batch and exactly one Research Card.
- [ ] The Research Card has an immutable card ID, the ETF instrument type, the ETF-performance workflow route, normalized input ticker, Ready status, and valid creation/update timestamps.
- [ ] The Research Batch records the authorized intake and is complete when card creation finishes; it does not claim that research has completed.
- [ ] The card is created through one deterministic queue command boundary rather than by prompt-specific direct file editing.
- [ ] The new Ready card is visible in a minimal Obsidian Bases view whose displayed state comes from card properties.
- [ ] A behavioral test runs the command against a temporary vault and verifies the resulting batch, card, and visible Ready state.
