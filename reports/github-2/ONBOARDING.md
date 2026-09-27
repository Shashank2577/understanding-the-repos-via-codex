# Onboarding: Receipts

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

The checked-out Python environment is available. Use .venv/bin/python -m receipts --help and the README demo workflow. Real host collection requires read access; generated real organizational reports may contain private records.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Generate demo evidence | Use the checked-out receipts demo workflow. | A portable dashboard is generated from known fixtures without a model call. |
| 2. Inspect a metric | Open a metric and examine arithmetic, exclusions and records. | A reviewer can recompute it and see coverage limitations. |
| 3. Export and reproduce | Export CSV/Markdown and rerender saved JSON. | The same fixed dataset produces the same result; proxies are labeled. |

## What Claude should do

Claude can narrate an existing evidence pack but should not change deterministic arithmetic or claim causal productivity gains. Numbers and caveats must travel together.

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

The concrete user problem is: A dashboard gives a churn or AI-adoption number but nobody can reproduce its denominator, exclusions or source records.

## Validate that it works

Run receipts demo locally, click one metric, recompute its formula from the cited fixture records, export CSV and rerender saved JSON. Verify incomplete host API coverage is visible and no model calls occur.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Sell or pilot a weekly evidence review for a small engineering team. The first deliverable should answer one disputed question with raw evidence and a stable window, not produce more charts.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
