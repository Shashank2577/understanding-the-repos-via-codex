# Onboarding: Foundry / AI SDLC

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

Start with README.md, compiler/README.md, policies/dod.yaml and role-packs/developer. UI is primarily GitHub Issues/Projects/Actions/PRs plus generated portal pages; no standalone SaaS dashboard is required to begin.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Prepare work | Use GitHub Issues and the role-pack workflow to express a small story and acceptance checks. | The issue has the required fields and authorized readiness gate. |
| 2. Dispatch | Inspect the Actions run for the selected role, harness, target checkout and budget. | Artifacts identify the correct product and approved scope. |
| 3. Review | Open the resulting PR and its DoD checks. | A missing required gate blocks progress; documented-but-disabled checks are not counted as enforced. |

## What Claude should do

Claude acts as a role-bound worker. It reads the approved work item and compiled charter, produces commits/PR evidence and escalates blockers; the human approves gates. Do not grant the developer role permission to rewrite its own enforcement workflow.

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

The concrete user problem is: An agent can write a feature, but nobody can reconstruct its requirement, review decision, cost or authority to merge. Handoffs between agents repeatedly lose context.

## Validate that it works

Use synthetic unit fixtures for pack compilation and gates. In a sandbox GitHub repository, prove an unauthorized labeler, unsupported harness, missing trailer and exhausted budget each prevent dispatch or merge. Do not use the production control plane for experiments.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Run ten small stories in a separate pilot product with frozen acceptance criteria. Track first-pass acceptance, human intervention minutes, retries and total cost per accepted story.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
