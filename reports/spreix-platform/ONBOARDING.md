# Onboarding: Spreix Platform

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

README local DB/seed loop, DEPLOY-RUNBOOK.md and package scripts are starting points. pnpm dev invokes SST and needs AWS access; web-only development is a different, narrower validation surface.

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
| 1. Establish workspace | Use the implemented auth/workspace/brain flow in a configured test deployment. | Organization and brain identity remain consistent across pages and worker inputs. |
| 2. Ingest and query | Add a synthetic source and inspect its knowledge/provenance. | Queries return only authorized sources with visible processing state. |
| 3. Run an agent | Start a bounded agent run and inspect checkpoints, output and tool availability. | Missing integrations are labeled; external actions follow the configured approval boundary. |

## What Claude should do

Claude may be a provider or external client, but the product’s own agents have tool belts, memory and run records. Explain this distinction so a developer does not confuse a Claude coding session with a deployed Spreix automation.

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

The concrete user problem is: Notetakers, wikis and automations are separate. Teams lose provenance when information moves between them, and repeatedly rebuild context before acting.

## Validate that it works

Use two fixture organizations, replay a source event, run an agent with one allowed and one forbidden tool, interrupt/resume from a checkpoint, and validate every resulting artifact’s source lineage and tenant scope. Then run the same test against a deployed dev stage.

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: Pick one paid workflow: meeting decision to living project brief to approved task. Establish the canonical knowledge store and cut the launch surface to that loop before adding more channels.

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
