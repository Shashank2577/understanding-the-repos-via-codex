# Onboarding: Scratch

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

README documents npm install and npm run tauri dev with Rust and OS tooling. The browser-only Vite view cannot validate all Tauri filesystem behavior.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Choose a folder | Open the native app with a disposable Markdown directory. | Notes are real local files and can be opened outside the app. |
| 2. Edit both ways | Switch between the rich editor and Markdown; edit externally and return. | Formatting survives round trips and external edits are recognized. |
| 3. Try AI carefully | Select a configured AI CLI and request a small note edit. | Streaming, cancellation and file diffs behave correctly before you retain the change. |

## What Claude should do

Claude is an optional editing backend selected by the user. Its job is to modify the requested note; it does not automatically maintain the company graph.

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

The concrete user problem is: A person wants rich editing and search without a cloud account or a heavyweight team knowledge system.

## Validate that it works

Use a disposable note, edit in rich/source mode, reopen the Markdown file, make an external edit and verify refresh, then invoke/cancel a harmless local AI request. Check diffs before saving.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Pilot a folder-based integration: approved exports from Cairn or Spreix become readable Markdown in Scratch. Keep round-trip ownership explicit and avoid auto-overwriting human edits.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
