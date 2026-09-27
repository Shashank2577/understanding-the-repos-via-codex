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
