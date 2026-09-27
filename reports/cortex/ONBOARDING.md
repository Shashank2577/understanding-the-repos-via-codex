# Onboarding: Cortex / compiled wiki

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

Follow README: Bun/Node, local Postgres, migrations, server model credentials; web is documented on 3003 and server on 3002. Start with paste input to avoid external fetch dependencies.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Add a source | Start with paste ingestion in the web app using synthetic text. | The source appears and compilation has a visible outcome. |
| 2. Inspect the wiki | Open the concept note and its source/connection references. | Merged content retains provenance; related-note bodies are checked separately from timestamps. |
| 3. Ask and revise | Ask a question, then revise the original source and rerun ingestion. | The answer changes only when evidence warrants it; stale/conflicting claims are visible. |

## What Claude should do

Claude can help maintain compiler prompts and diagnose note lineage. This review did not establish a Claude session hook or native MCP integration for Cortex; do not assume Cairn behavior applies.

A useful starting instruction is: “Help me complete the first workflow in this guide. Check the current README and configuration, identify any unavailable dependency, show the source evidence behind the result, and run the relevant acceptance check. Distinguish what you observed from what you inferred.”

If a tool or provider fails, Claude should name the failed dependency, preserve successful intermediate work and report the degraded state. It should not replace an unavailable result with a confident-looking invented answer. A screenshot, generated summary or green counter is evidence of only the state it actually shows.

## Use it by role

| Role | First objective | Evidence of value |
|---|---|---|
| End user / individual developer | Complete the three-step journey for the problem below | A useful result whose supporting source can be checked |
| Implementing developer | Trace input → transformation → persistence/output; then test failure and replay | Correct identifiers, no silent duplicate work, actionable error state |
| Reviewer / team lead | Challenge one result and inspect its derivation | Corrections survive the next run and limitations stay visible |
| Owner / operator | Prove setup, scope, permissions and cost behavior in the intended environment | Repeatable operation without hidden manual repair |
| Claude / coding assistant | Follow the repository-specific role described above | Real tool results, scoped changes, explicit verification and no invented evidence |

The concrete user problem is: Bookmarks grow while knowledge stays fragmented. Several sources discuss the same concept and need one evolving explanation with provenance.

## Validate that it works

Ingest two synthetic documents with a deliberate contradiction. Inspect raw sources, merged note, conflict flags, related note body and operation log. Delete/revise one source and verify the remaining answer cites valid evidence.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Implement and test a real semantic cascade, or rename it to freshness marking. Prove source revision and deletion update every derived claim before exporting the compiler.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
