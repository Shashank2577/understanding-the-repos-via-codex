# Onboarding: Cairn

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

Existing checkout: .venv/bin/cairn doctor. New disposable repository: install cairn-brain using the README, then run cairn. Read docs/onboarding.md and this atlas’s extended Cairn guide. Initialization installs hooks/configuration, so understand its scope first.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Orient | Choose the project; open Overview, then Map and Impact. | Known source files and callers can be verified; sync age is visible. |
| 2. Recover intent | Open Specs, Timeline and Memory around a concrete task. | The cited requirement or prior decision actually supports the advice. |
| 3. Resume | Inspect Sessions and the next-session preview. | A new configured agent session receives relevant context; token accounting is scoped. |

Read the [extended five-layer UI, personas and savings guide](../../onboarding/CAIRN.md).

## What Claude should do

At session start Claude receives hook context when configured. Before editing it should call cairn_context or cairn_impact; ask cairn_why before guessing intent; store durable decisions via cairn_remember. Instructions encourage this, but do not enforce model obedience.

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

The concrete user problem is: Claude repeatedly rediscovers the same code, forgets a reverted approach, or cannot explain why a constraint exists. A folder of notes has no link to the changed symbol or task.

## Validate that it works

Run doctor; open Impact for a known symbol; check citations and a real caller; inspect the session-start preview; add and retire a harmless convention in a fixture; compare a task checked done with its actual file and tests. Measure total task tokens and elapsed time with and without Cairn.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Package a 30-minute tutorial with a disposable repo and before/after task benchmark. Make baseline assumptions, model ledger and net cost visible beside the compression ratio.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
