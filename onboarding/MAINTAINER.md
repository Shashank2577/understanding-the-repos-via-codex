# Onboarding for the developer and Claude maintaining this atlas

Read REQUEST.md, PROGRESS.md, METHODOLOGY.md and inventory.json first. The user asked that this work survive sessions; do not ask them to repeat the scope. Twenty source locations are represented by stable IDs. Their private absolute paths are stored only in the ignored .research/manifest.json on the original machine.

## Repository layout

- scripts/catalog.py: curated findings, user jobs, onboarding, evidence and prioritization for all projects.
- scripts/build.py: deterministic Markdown and static HTML generator.
- reports/<id>/REPORT.md: product/implementation review.
- reports/<id>/ONBOARDING.md: setup, UI journey, Claude behavior and acceptance checks.
- reports/<id>/EVIDENCE.md: source references, hashes and limits.
- portfolio/SYNTHESIS.md: overlap, proposed integrations, quick wins and high-stakes bets.
- onboarding/CAIRN.md: detailed five-layer walkthrough and savings interpretation.
- site/: generated deployable website, including report pages and copied assets.
- assets/: sanitized screenshots and fonts, with provenance in ASSETS.md.
- VALIDATION.md: commands actually run and their limitations.

## Make a change

Inspect the relevant source first, preferably through codebase-memory graph tools. Compare its current commit/worktree to the inventory. Read its local AGENTS.md before running or changing anything. Source repositories are not submodules and the atlas does not own their working-tree changes.

Update the catalog’s claim, evidence and limitation together. Keep an implementation fact separate from a user-demand hypothesis. Edit the Markdown guides for cross-project narrative. Run `python3 scripts/build.py`, then `python3 scripts/validate.py`. The generator requires markdown-it-py; requirements.txt pins the build dependency. The generated site itself needs no Python or JavaScript package installation.

Preview with `python3 -m http.server 8768 --bind 127.0.0.1` from this repository and open `/site/`. Inspect at desktop and narrow width. Search for a project, filter its category, compare two projects, open a report, switch persona guidance, follow onboarding and try the savings calculator. Expected outcomes are visible text changes, working links and labeled hypothetical arithmetic—not a silent button click.

## How Claude should react

- “What is X?” → open its REPORT.md and cite evidence plus validation limits.
- “Is it working?” → inspect VALIDATION.md; distinguish code existence, local tests and live deployment.
- “What should we build?” → consult SYNTHESIS.md and the buyer’s job; state the experiment that could disprove the recommendation.
- “Show savings” → explain the baseline and use actual ledger data or explicitly hypothetical inputs.
- “Merge the brains” → request/derive a canonical schema, tenancy and migration plan before porting; the portfolio diagram is a proposal, not a migration instruction.
- “Continue” → read PROGRESS.md and the latest workorder; resume outstanding steps rather than recreate folders or overwrite source repos.
- “Publish” → validate the curated site and Git diff, exclude raw source/secrets/customer content, then push the documentation repository and verify Pages.

Never turn screenshots into claims that a current backend worked. Never claim a test passed merely because a test file exists. Never copy source-repository .env files, session logs or internal datasets into the atlas. Preserve upstream ownership and licenses.

## Publication

The requested destination is Shashank2577/understanding-the-repos-via-codex. Only this documentation project is published. GitHub Pages serves site/ through an Actions workflow. The source repositories retain their original remotes and visibility. The official publishing mechanism is documented in [GitHub Pages configuration](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

Record the deployed URL and commit in PROGRESS.md. When source evidence changes, retain a dated validation entry so another developer can tell what was checked and when.
