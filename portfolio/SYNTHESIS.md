# What this portfolio can become

The strongest strategy is to organize the work around three customer jobs, with operations kept separate. These are recommendations from a local implementation review, not proof of customer demand. The code shows many useful capabilities; it does not establish willingness to pay, retention or a durable moat.

## Three coherent product lines

| Product line | Buyer question | Primary home | Supporting pieces | Keep outside the boundary |
|---|---|---|---|---|
| Engineering evidence | Are our delivery and AI-use claims supported? | Receipts for reports; Prompture for detailed capture | Sovix CLI as a low-friction scanner; Qmmit as a source of tested capture ideas | Do not make a signature floor into exact attribution or individual productivity |
| Agent memory and delivery | Can agents change this code safely without relearning it? | Cairn for context; Foundry for execution governance | Architecture Foundry and Java skills for domain discipline; kb as a migration/component source | Context does not grant authority to merge or deploy |
| Team knowledge and action | What did we decide, and what needs to happen next? | Spreix Meeting Intelligence as the entry workflow; Spreix Platform as the consolidation candidate | Cortex compiler, Spreix Brain clarification inbox, selected Researcher briefs | Avoid launching four separate “company brain” products |

OBSERVE serves an SRE/platform buyer and consumes production telemetry. Keep its product, permissions, rollout and commercial story distinct. FreeLLMAPI can be shared infrastructure after protocol and embedding compatibility tests. Scratch is a human-owned local writing surface, with upstream attribution preserved. Lumen is a standalone document platform only if a buyer needs its document parsing, self-hosting and API boundaries enough to justify the additional stack.

## Overlap does not mean equivalence

| Pair / cluster | Shared work | Important difference | Recommended treatment |
|---|---|---|---|
| Prompture / Qmmit | Session capture, prompt-to-commit matching, portfolio | Go multi-service/hooks versus TypeScript git wrapper; different IDs, stores and match semantics | One product direction; evaluate scanner/privacy modules on a shared fixture before porting |
| Sovix CLI / Receipts | Git corpus, deterministic metrics, evidence exports | Small aggregate-only floor versus broader leadership metrics and host API data | Share metric definitions and fixtures; retain different privacy/output contracts |
| Cairn / kb | Code graphs, history, explanations | Five-layer agent memory versus commit-driven file descriptions | Cairn as flagship; kb as minimal tool or adapter, not a second identical onboarding |
| Cairn / Foundry | Specs, agent context and history | Knowledge retrieval versus permissioned delivery execution | Integrate through cited artifacts; do not merge their authority models |
| Architecture Foundry / Java scaffold | Agent instructions, architecture and quality standards | General architecture reasoning versus Java-specific rules | Put domain packs under one documented hierarchy; make important rules executable |
| Foundry / foundry-stage0 | Delivery conventions and DoD checks | Current control plane versus seed archive | Maintain the seed as lineage, not another live system |
| Cortex / Lumen | Ingestion, provenance, grounded answers | Compiled concept notes versus query-time document retrieval | Choose by answer type; a note compiler does not replace faithful raw-document retrieval |
| Cortex / Spreix Brain | Source ingestion and knowledge graph | Concept wiki versus typed entities plus confidence-gated questions | Reuse complementary ideas after agreeing canonical source/entity IDs |
| Notetaker / Spreix Platform | Meetings, knowledge, agents, billing | Focused meeting product versus broad unified multi-channel platform | Migration only after parity, tenant and replay checks; keep a working product during transition |
| Company Brain / Spreix Platform | Name and intended territory only | Empty directory versus implementation | Resolve branding, avoid creating another codebase |
| Researcher / team brain | Source gathering and synthesis | On-demand external briefing versus persistent internal knowledge | Treat research as a bounded importer with source/date/confidence |
| FreeLLMAPI / every model client | Provider adaptation and usage | Transport compatibility versus application-specific quality, tools and vector semantics | Reuse endpoint contracts selectively; validate each capability |

## Combinations worth prototyping

### 1. Evidence-backed engineering review — easiest route to a useful deliverable

Begin with Sovix CLI’s local fixed-window scan. Use Receipts to explain delivery patterns and coverage. Add Prompture only when users need richer session provenance. A reviewer opens the dashboard, clicks a disputed metric and sees the exact arithmetic and records.

**Integration contract:** repository identity, commit SHA, UTC event timestamp, measurement window, metric ID, schema version, coverage and evidence links. Keep observed activity, matched attribution and inferred proxies in separate fields. Never silently add percentages with different denominators.

**Validation:** same fixture produces reproducible JSON; unsigned AI activity remains unknown; missing host API data is visible; an incorrect match can be rejected and recomputed. **Commercial hypothesis:** an engineering lead pays for a recurring decision review rather than another passive dashboard. Test this with three teams before adding sales infrastructure.

### 2. Memory-aware delivery — highest engineering differentiation hypothesis

Architecture Foundry produces requirements/ADRs. Cairn retrieves rationale and impact when the coding agent starts. Foundry dispatches a role-limited session and enforces gates. Receipts summarizes the outcome. The user follows one work item from intent to accepted change, with cited context at each step.

**Integration contract:** work-item ID, requirement ID, repository/commit, artifact hashes, actor role, approved scope and cost ledger entry. Retrieved memories are evidence, never authority to widen credentials or bypass a gate. A poisoned issue or memory must not rewrite the control plane’s policy.

**Validation:** one unsafe instruction is rejected, one stale decision is superseded, one independent reviewer catches an intentionally wrong implementation, and the total accepted-story cost is measurable. **Stop condition:** the system produces more supervision work than it removes across a fixed pilot set.

### 3. Meeting-to-decision-to-action — strongest team workflow

Use Notetaker to capture a meeting and preserve timestamped quotes. Compile the useful material into a project brain. Use Spreix Brain’s uncertainty pattern when an owner or decision is ambiguous. Have Spreix Platform generate an actionable draft with provenance, then require the workflow’s human approval before sending or changing another system.

**Integration contract:** org ID, project/brain ID, source ID, recording/time range, entity IDs, source version, processing status, idempotency key, permissions and retention policy. Decide which repository owns each entity before migrating. Avoid dual writes to several independent graphs.

**Validation:** correcting a transcript updates downstream artifacts; a repeated event creates no duplicates; deleting a source removes or invalidates derived claims; org A cannot retrieve org B’s facts; a discarded draft causes no external action. **Commercial hypothesis:** one recurring team workflow can earn retention before the full platform exists.

### 4. Incident context loop — promising but keep it bounded

OBSERVE detects and investigates a production symptom. Cairn can explain the relevant code and previous fixes. Foundry can prepare a reviewed remediation PR. This is a proposed integration, not an observed connection between the repositories.

**Boundary:** telemetry tools remain read-only during investigation; code edits go through normal tests/review; production remediation is separately authorized. **Validation:** a synthetic incident is diagnosed with the correct time window and version, and an irrelevant old fix is not applied automatically.

## Lowest-hanging fruit

Planning ranges below are rough focused-engineer estimates, not commitments; they assume existing development environments and exclude customer procurement.

1. **1–2 days: align documentation with code.** Fix Platform’s design-only/Aurora story, FreeLLMAPI’s embeddings contradiction, Researcher’s boilerplate README and Java scaffold’s enforcement claims. Acceptance: a new developer can follow documented commands and distinguish shipped, stubbed and untested behavior.
2. **2–4 days: create one canonical evidence fixture.** Reuse it across Sovix CLI and Receipts, with signed/unsigned commits, merges, bot identities and missing API fields. Acceptance: formulas and privacy contracts are explicit and outputs deterministic.
3. **3–5 days: make Cairn’s value measurable.** Keep context compression, added briefing tokens, enrichment spend and actual task outcomes separate. Acceptance: matched tasks can be compared without claiming source-file size is a bill saving.
4. **3–5 days: make degraded AI states visible.** Spreix Brain stub extraction, Platform missing external tools and kb failed descriptions should have explicit status. Acceptance: users can distinguish a real result from a fallback.
5. **1–2 weeks: prove one meeting workflow.** A synthetic recording becomes cited decisions and a reviewed draft, with replay, correction and retry checks. Acceptance: a team can repeat it without developer intervention.

## Highest-upside, highest-stakes bets

| Bet | Why the upside could be large | Why the stakes are high | Evidence needed before more investment |
|---|---|---|---|
| Spreix Platform | Shared memory that drives repeated team actions | Huge scope; tenant isolation; external actions; migration from working products | Weekly active teams, correction trust, repeatable deployment, safe action completion |
| Foundry | Repeatable delivery across agents and products | Credentials, policy enforcement, review quality and runaway retries | Accepted-story cost, external pilots, gate bypass tests, intervention rate |
| OBSERVE | Production incident and telemetry spend pain | Operational responsibility; cluster compatibility; false diagnosis | Successful installs across environments, incident drills, measured retention/cost |
| Cairn | Low-friction daily developer habit | Context relevance, stale memory, hidden processing cost | Faster accepted changes with equal/better correctness and repeat usage |
| Meeting Intelligence | A clear recurring input and tangible output | Capture reliability, attribution accuracy, privacy, cost per hour | Teams using follow-ups repeatedly, successful-hour rate and retention |

The atlas’s effort/upside/risk scores are ordinal reviewer judgments from 1 to 5. Effort means effort to a credible narrow pilot, not remaining completion percentage. Upside means plausible breadth and recurrence of the buyer problem, not valuation. Risk means integration/operational/consequence exposure. They are deliberately not averaged into a fake precise winner score.

## A practical sequence

**First fortnight:** fix evidence/documentation gaps; demo Receipts and Cairn to three independent users each; collect friction and outcome observations. Keep Notetaker usable and do not begin a second company-brain implementation.

**Next month:** choose one primary commercial experiment: engineering evidence review or meeting follow-through. Build the smallest repeatable workflow and measure retention. Use Foundry and the model gateway internally while collecting their true maintenance costs.

**Only after that:** integrate the selected product into a broader platform if users repeatedly cross that boundary. Migrate schema and provenance deliberately; keep import/export contracts and rollback. Park duplicate brands and unvalidated feature breadth.

## External context checked 2026-09-26

These primary sources establish adjacent capabilities, not a comprehensive competitive study. The differentiation judgments above are our inferences.

- [LiteLLM routing](https://docs.litellm.ai/docs/routing) already covers routing, retries and fallback; a gateway needs a sharper promise than “one API.”
- [Graphiti](https://github.com/getzep/graphiti) provides temporal knowledge graphs for agents; merely having a graph is not a moat. A strong workflow, quality evaluations and usable provenance matter.
- [OpenTelemetry](https://opentelemetry.io/docs/) standardizes telemetry collection and signals. OBSERVE’s value must come from the integrated operating experience and diagnosis quality, beyond collecting standard signals.

No market-size, pricing comparison, uniqueness claim or production SLA has been validated in this review.
