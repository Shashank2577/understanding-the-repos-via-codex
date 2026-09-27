# Onboarding: Prompture

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

Use the existing DEVELOPER_ONBOARDING.md and README. Local stack requires Go, Python, pnpm, Postgres/pgvector, Redis and configured auth/model providers. For a demo, prefer a dedicated workspace and synthetic sessions.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Connect and capture | Use the existing developer onboarding to connect a disposable repository and supported coding tool. | A session and repository identity appear; unsupported capture is explicit. |
| 2. Review attribution | Open the prompt/commit review Inbox; inspect one candidate and reject an unrelated pair. | Accepted and rejected associations remain distinguishable. |
| 3. Read the result | Open the project dashboard and follow the evidence behind one metric. | The same event IDs and fixed time window reconcile with the capture record. |

## What Claude should do

Claude can be a captured coding agent and can consume the documented MCP surface. It must not infer that every captured prompt caused a commit. Keep review corrections and sensitive prompt redaction visible.

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

The concrete user problem is: A team pays for multiple coding assistants but cannot explain how activity relates to shipped work. Git signatures alone miss manually committed AI-assisted work.

## Validate that it works

Create a synthetic prompt and a known commit in a disposable repo. Confirm the same prompt ID appears once after repeated sync, rejected matches stop contributing to accepted attribution, and tokens match raw capture. Test an unrelated commit as a negative control.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Choose one supported tool and one repo; show an end-to-end capture, sync, candidate match, rejection/confirmation and dashboard reconciliation. Publish a coverage matrix with explicit unknowns.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
