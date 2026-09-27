# Onboarding: Architecture Foundry

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

Follow the plugin README for installation; inspect .claude-plugin/plugin.json. The UI is Claude conversation, generated documents and code-review output, not a standalone dashboard.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Install the bundle | Inspect the plugin manifest and follow its README installation instructions. | Claude can discover the architecture skills; no web dashboard is expected. |
| 2. Review a known flaw | Ask for an architecture audit of a small fixture with a missing timeout. | Findings cite real code and distinguish assumptions from established constraints. |
| 3. Turn a rule into a check | Generate a fitness check and run bad, good and waived fixtures. | The check detects the intended violation without a blanket false positive. |

## What Claude should do

Claude invokes the plugin’s design or review workflow, labels assumptions, names rejected alternatives and produces artifacts. Humans still own architecture acceptance and cost assumptions.

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

The concrete user problem is: An attractive architecture diagram hides missing capacity assumptions, failure analysis and rejected options. Teams repeatedly debate the same choices.

## Validate that it works

Run an architecture review on a disposable sample with a known outbound timeout flaw. Verify every finding cites a real line, then run the generated check on bad/good/waived inputs. Do not claim the historic test-drive was rerun.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Publish one narrow, documented audit-to-check demo with a versioned fixture and repeatable outputs. Correct distribution metadata and define the boundary with Foundry.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
