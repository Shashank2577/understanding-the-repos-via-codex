# Confirmed findings — 2026-09-26

- 20 supplied locations; spreix-company-brain is empty. aisdlc and free have nested project roots; foundry-stage0 is a seed bundle.
- Cairn contains the requested five layers. Existing docs/onboarding.md already covers them, so the atlas should extend it with an evidence-based savings interpretation and validation examples.
- Cairn live UI inspected at local port 4747. Overview: 391 tokens served via one MCP query against 144,228 estimated source tokens in 33 files. This is an estimated context compression comparison, not billed savings or measured avoided reads. source_cost uses bytes // 4; Overview prioritizes MCP totals when present, excludes briefings and counts file labels from a limited recent window.
- Cairn targeted tests: only two sandbox socket-binding failures; both passed when rerun outside the sandbox.
- Sovix CLI: 153 tests passed.
- Receipts: full local pytest command completed successfully.
- Spreix Brain: installed runner produced 47 passes and 5 database-dependent failures because localhost:5433 was unreachable. pnpm wrapper separately attempted dependency refresh and aborted without a TTY.
- Cortex applyIngestPlan does transactional new/merge/crossref writes; cascade currently only touches timestamps, not semantic rewrites.
- FreeLLMAPI README says embeddings unsupported, while current source exposes embeddings UI/router/provider adapters and tests. Documentation is stale.
- Spreix Platform README says design-only and Aurora while code implements agent-run workers and AGENTS records migration to standard Postgres/Neon. Documentation is stale.
- ai-java-scaffold promises enforcement stronger than example/pom.xml: no Testcontainers dependency, no Failsafe plugin despite an *IT test name, no branch coverage minimum or Enforcer plugin in inspected POM.
- Foundry policies/dod.yaml still lists several checks as enforced:false; policy prose is not an active gate.
- Source ownership differs: Scratch and FreeLLMAPI point upstream, Qmmit points to pandey019, Java scaffold points to taazaainc. Publish analysis only, retain attribution, do not copy these repos into a new personal umbrella.
- User explicitly said ignore BOPUS. Five-engine clarification was also dismissed; no further clarification required.
