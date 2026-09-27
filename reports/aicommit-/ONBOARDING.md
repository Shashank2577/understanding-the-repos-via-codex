# Onboarding: Qmmit

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

Use local cli/package.json and README; inspect install scripts before adopting the git wrapper. Use a test repo for commit/push exercises; no live Qmmit account was tested.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Capture locally | Use the documented qmmit prompt/scanner path in a disposable git repository. | A prompt is stored locally with redaction behavior checked. |
| 2. Make a known change | Use the documented commit flow and inspect the best-match candidate. | The candidate can be compared to an intentionally unrelated commit. |
| 3. Review before upload | Inspect what qmmit push will synchronize before using a test account. | Sensitive prompts remain excluded; repeat sync does not duplicate records. |

## What Claude should do

Claude may log its prompts through supported integration or manual commands. Captured prompts remain data; scanning a session does not give permission to publish it.

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

The concrete user problem is: People want to connect a prompt to a commit without manually maintaining a separate journal.

## Validate that it works

Use synthetic prompt/commit fixtures with unrelated changes, reordered events and redaction patterns. Verify repeated sync is idempotent and a plain git operation remains successful when capture fails. Existing tests were inspected by inventory, not executed.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Compare Qmmit and Prompture on the same capture corpus. Retain the stronger scanner/privacy pieces behind one versioned event schema and one user-facing identity.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
