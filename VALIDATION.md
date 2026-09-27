# Validation record

Date: 2026-09-26. No source fixes were made as part of this review.

| Project | Command / observation | Result | Limit |
|---|---|---|---|
| Sovix CLI | npm test | 153 passed, 0 failed | Local suite; not npm publication or real customer data |
| Receipts | .venv/bin/python -m pytest -q | Full command exited 0 | Local fixtures; host API availability and commercial adoption untested |
| Cairn | .venv/bin/python -m pytest -q tests/test_core.py tests/test_surfaces.py tests/test_agent_memory.py | Two socket-binding failures in sandbox; other selected tests passed | Environment prevented local port binding |
| Cairn | Same runner, test_surfaces.py -k 'foreground_server or stopped_server', outside sandbox | Both previously blocked tests passed | Selected coverage, not entire Cairn suite |
| Spreix Brain | pnpm test | Package-manager preflight aborted because dependency refresh required TTY | Existing modules were not intentionally purged/reinstalled |
| Spreix Brain | node node_modules/vitest/vitest.mjs run | 47 passed, 5 failed; one suite teardown also failed | Database-dependent tests could not reach localhost:5433; no claim of application defect established |
| Cairn UI | Read-only Overview, Map and Specs | Populated views rendered | No sync, memory mutation, live model request or team deployment exercise |
| All other projects | Graph/source/config inspection | Reported per project | No fresh full test suite or runtime validation |

Cairn Overview at observation: 391 estimated tokens sent via one MCP query, 144,228 estimated source tokens in 33 files, displayed ratio 369×. These are existing accounting records read from the live UI, not a benchmark created by this review. The map showed 16,144 nodes, 42,969 links and 505 communities; Specs showed 75/75 tasks while also identifying Analyze as the next stage. That is a useful example of why a completed task count does not establish full verification.

The preferred chrome-devtools-axi wrapper failed due to a pageId API mismatch. The browser fallback was used for read-only visual inspection. A separate app on port 3000 was observed but not attributed to the requested repositories or used as evidence.

Static-site checks and publication status are appended after generation.

## Field guide site

- Generator rebuilt 20 project report folders and 94 HTML pages.
- `python3 scripts/validate.py` passed local links, fragments, images, completeness for all 20 report folders, and a publication scan for private absolute paths and common credential patterns.
- `node --check assets/app.js` passed.
- Read-only browser review at desktop and 390px mobile width confirmed the vision-led start page, persistent navigation, project breadcrumbs, report/onboarding/evidence tabs and a responsive project report table.
- The project search was entered for “Cairn” and the directory showed one matching project. The comparison panel loaded Cairn and kb from the local catalog.
- These are site checks. They do not substitute for the product-specific exercises listed in each onboarding document.
- GitHub Pages workflow completed successfully; public root URL returned HTTP 200 and the live browser displayed the deployed landing page and 20-project directory.
