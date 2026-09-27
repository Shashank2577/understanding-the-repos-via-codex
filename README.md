# Understanding the repos via Codex

An implementation-grounded atlas of twenty local repository locations: what they do, who needs them, how they overlap, what is missing and what to build next.

**[Open the visual atlas](https://shashank2577.github.io/understanding-the-repos-via-codex/)** · [Portfolio decisions](portfolio/SYNTHESIS.md) · [Cairn onboarding and savings](onboarding/CAIRN.md) · [Validation record](VALIDATION.md)

## Start here

The review recommends three product lines: engineering evidence, agent memory and delivery, and team knowledge and action. Receipts/Sovix CLI provide a narrow evidence pilot; Cairn offers a concrete developer workflow; Meeting Intelligence offers a recurring team workflow. Spreix Platform, Foundry and OBSERVE have substantial scope and need separate proof of reliability and demand.

These are recommendations from selected source paths and local validation, not an exhaustive security audit or proof of market traction. Reports distinguish implementation, documentation claims, historical screenshots, live UI and hypotheses. [Read the method and limitations](METHODOLOGY.md).

## Repository reports

Each project has REPORT.md, ONBOARDING.md, EVIDENCE.md and a workflow diagram.

| Location ID | Product | Report |
|---|---|---|
| sovix-ai | Prompture | [Read](reports/sovix-ai/REPORT.md) |
| aisdlc | Foundry / AI SDLC | [Read](reports/aisdlc/REPORT.md) |
| cairn | Cairn | [Read](reports/cairn/REPORT.md) |
| sovix-cli | Sovix CLI | [Read](reports/sovix-cli/REPORT.md) |
| spreix-company-brain | Empty directory | [Read](reports/spreix-company-brain/REPORT.md) |
| cortex | Cortex compiled wiki | [Read](reports/cortex/REPORT.md) |
| ragpipeline | Lumen | [Read](reports/ragpipeline/REPORT.md) |
| ai-java-scaffold | Java governance scaffold | [Read](reports/ai-java-scaffold/REPORT.md) |
| spreix-brain | Spreix Brain | [Read](reports/spreix-brain/REPORT.md) |
| aicommit- | Qmmit | [Read](reports/aicommit-/REPORT.md) |
| kb | kb code graph | [Read](reports/kb/REPORT.md) |
| scratch | Scratch (upstream) | [Read](reports/scratch/REPORT.md) |
| archi-foundry | Architecture Foundry | [Read](reports/archi-foundry/REPORT.md) |
| foundry-stage0 | Bootstrap seed | [Read](reports/foundry-stage0/REPORT.md) |
| github-2 | Receipts | [Read](reports/github-2/REPORT.md) |
| spreix-notetaker | Meeting Intelligence | [Read](reports/spreix-notetaker/REPORT.md) |
| OBSERVE | OBSERVE | [Read](reports/OBSERVE/REPORT.md) |
| free | FreeLLMAPI (upstream) | [Read](reports/free/REPORT.md) |
| spreix-platform | Spreix Platform | [Read](reports/spreix-platform/REPORT.md) |
| researcher | Researcher | [Read](reports/researcher/REPORT.md) |

## Developer and Claude onboarding

Read [REQUEST.md](REQUEST.md), [PROGRESS.md](PROGRESS.md), then the [maintainer guide](onboarding/MAINTAINER.md). The original scope is saved so future sessions can continue without asking the user to repeat it. Source repositories retain their original remotes and working-tree changes.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/validate.py
python3 -m http.server 8768 --bind 127.0.0.1
```

Open http://127.0.0.1:8768/site/ to preview. Generated site/ is committed and deployed through GitHub Pages. It uses local assets and plain HTML/CSS/JavaScript, without a hosted model or build service at runtime. Rebuilding from this published repository preserves existing file hashes when original local checkouts are unavailable.

## Publication boundary

This repository publishes curated reports and reviewed visual assets. It does not publish the twenty source repositories, provider credentials, raw session records, internal datasets or ignored .research/ notes. Private source links still require the reader’s access. [Asset provenance and licenses](ASSETS.md) are preserved.
