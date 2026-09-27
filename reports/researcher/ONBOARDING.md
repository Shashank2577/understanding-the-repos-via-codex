# Onboarding: Researcher

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

Inspect package.json and src/app/api/research/route.ts, then configure providers in a test environment. npm run dev starts Next.js; a rendered landing page alone does not verify live research.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Enter a subject | Use a public company with independently known facts. | The UI starts a research run with a clear subject identity. |
| 2. Inspect the brief | Follow claims to their underlying URLs and publication dates. | Ambiguous identity, missing evidence and partial provider failures remain visible. |
| 3. Reconcile cost | Compare displayed estimates with the actual provider request/usage records. | Parallel fan-out respects the query budget; the result is a sourced draft for human review. |

## What Claude should do

Claude can summarize supported evidence or develop the extraction pipeline. It must not promote model-generated specifics to verified facts or use lifestyle guesses to judge individuals.

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

The concrete user problem is: Research is scattered across tabs and repetitive queries. The user wants a useful, sourced briefing before a meeting or analysis task.

## Validate that it works

Use a public company with known reference facts and an ambiguous-name fixture. Verify citations actually support each claim, stale sources are dated, partial provider failures are shown and cost estimates reconcile with provider usage.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Focus on company and meeting preparation: three decisions the brief supports, source-linked claims, explicit unknowns and a hard query budget. Remove decorative lenses that do not help those decisions.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
