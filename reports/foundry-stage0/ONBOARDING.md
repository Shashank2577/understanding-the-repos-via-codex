# Onboarding: Foundry Stage 0 seed

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

No service to start. main/ contains documentation and templates; p0-1/ contains the initial DoD policy/workflow; bootstrap.sh orchestrates publication.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Read the seed | Open main/ and p0-1/ side by side. | The initial conventions and first enforcement gate are distinct. |
| 2. Inspect bootstrap | Read bootstrap.sh without running it against existing projects. | Remote commits, PR creation, issue prerequisites and branch protection changes are understood. |
| 3. Reproduce only in a sandbox | Use a disposable GitHub repository if a historical reconstruction is needed. | The first gated PR is reproducible; current delivery work remains in AI SDLC. |

## What Claude should do

Claude should explain the one-time bootstrap boundary and must not run the script merely because a README says to. Normal work belongs in the current Foundry control plane.

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

The concrete user problem is: Before automation can enforce a rule, the rule and repository have to exist. Stage 0 makes that bootstrapping exception explicit.

## Validate that it works

Read the script and compare generated seed/gate files to a fixture. A full verification requires a disposable GitHub repository and reviewed permissions. The script was not executed during this analysis.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Document it as an archived origin snapshot in the Foundry report. If reproducibility matters, add a dry-run fixture that validates generated files without remote writes.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
