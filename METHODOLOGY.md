# Method, scope and evidence

Review date: 2026-09-26. All twenty supplied locations were inventoried. Nested roots were resolved; one directory is empty and two locations are unpacked non-git bundles. Git HEADs, remote ownership and working-tree state are recorded in inventory.json. Reports describe the local snapshot, including pre-existing uncommitted edits. They are not claims about what is currently deployed.

## What was inspected

1. Project README, manifests, available onboarding and agent instructions.
2. Codebase-memory graph discovery, with fast indexing for missing projects. Existing graph results were checked through concrete snippets; indexes can omit docs, examples, scripts and generated files.
3. Representative implementation paths: matching, ingestion, agent run, model routing, metric queries, session accounting, source extraction and bootstrap policy.
4. Targeted local tests for Sovix CLI, Receipts, Cairn and Spreix Brain.
5. Live read-only Cairn UI and its source CSS. Other included product screenshots are explicitly marked historical repository assets. No production cluster, meeting bot, paid-provider research run or full cross-product deployment was executed.
6. Limited primary-source checks for adjacent capabilities and GitHub Pages publication.

This is an implementation-grounded product and architecture review with deep selected paths, not a line-by-line audit of every repository, security certification or exhaustive QA run. Each report lists the gap between demonstrated code and outcomes still needing validation. Test-file presence alone is not recorded as a passing test.

## Evidence labels

- **Code inspected:** a concrete file/function or config was read. This demonstrates implementation intent/behavior at that point, not end-to-end success.
- **Live UI:** rendered state observed during this review. Data may have been produced before the review; the caption states that limit.
- **Test run:** a command executed in this session, with result and environment limitations in VALIDATION.md.
- **Historical asset / documentation claim:** existing screenshot/report/README, not regenerated evidence.
- **Recommendation / hypothesis:** reasoned advice that still needs product or technical validation.

Source references include paths and line starts. Where a git remote exists, links use the recorded commit. A dirty file or untracked addition can differ from that commit; the local path and current file hash in EVIDENCE.md are authoritative for this snapshot. Private repository links require the reader’s access. No source code, provider secrets, session databases or private customer datasets are bundled into this documentation repository.

## Ranking rubric

Effort, upside and risk use 1–5 ordinal judgments with explicit definitions in portfolio/SYNTHESIS.md. Empty/archive entries are parked rather than ranked as implemented products. No arithmetic score implies commercial validation. Proposed integrations are labeled proposals; overlap does not establish existing API wiring or code lineage.

## Maintaining the analysis

Update a report when its recorded commit or relevant working tree changes. Re-run only checks affected by the new evidence. Record command, date, dataset, observed result and what was not exercised. Keep historical findings dated instead of silently replacing the evidence with a claim. REQUEST.md, PROGRESS.md and onboarding/MAINTAINER.md preserve the original scope and continuation procedure.
