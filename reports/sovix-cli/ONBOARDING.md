# Onboarding: Sovix CLI

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

Node is sufficient for local source use; no runtime dependency installation is needed. The interface is a terminal and Markdown/JSON export, not a missing browser application.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Inspect help | Run node bin/sovix.js --help in the checked-out project. | The source CLI works without assuming an npm release. |
| 2. Scan a fixture | Run node bin/sovix.js scan <fixture-repo> --json with the documented window options. | JSON contains explicit scope and caveats. |
| 3. Explain one number | Export the evidence pack and recompute one signed-activity metric. | Unsigned work remains unknown and personal data follows the aggregate-only contract. |

## What Claude should do

Claude may run the scanner and explain the evidence pack. It should quote the floor and coverage caveat together, and never turn it into employee rankings or exact AI authorship.

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

The concrete user problem is: A team wants evidence before installing invasive capture agents or giving a service tokens. A local git repository is already available.

## Validate that it works

Run npm test. Then node bin/sovix.js scan <fixture-repo> --json and export with the same fixed since date twice. Introduce known signed/unsigned/merge/bot commits and verify denominators and privacy.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Use the checked-out CLI for a clean example report, verify deterministic output twice and document installation honestly. Keep it as a small front door to the broader evidence product.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
