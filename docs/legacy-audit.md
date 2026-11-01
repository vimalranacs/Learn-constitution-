# Argon audit — 1 November 2026

Inputs: extracted project in `constitution_atlas_fullstack/constitution_atlas_fullstack`, plus the standalone HTML at workspace root. No ZIP was supplied in the workspace; the extracted source is the baseline. Original files remain untouched. `legacy/argon-original.zip` preserves all 14 project/source artifacts (excluding installed dependencies and caches); `legacy-inventory.json` records actual paths, byte sizes and SHA-256 hashes. Re-running `python tools/audit_legacy.py` checks the checkpoint against originals.

## Observed baseline

Six legacy unittest tests pass using the supplied backend virtual environment. These exercise fixed report values, selected article strings, graph integrity, eight journey paths, undirected BFS and FTS/RAG. They do not establish complete PDF alignment or legal accuracy. FastAPI has `/api/health` and other `/api/*` routes but intentionally no root page. HTTP and visual checks are recorded separately in testing.md.

JSON: 635 nodes, 1,255 edges, 470 article records, eight journeys, six simulation definitions. No duplicate node IDs, duplicate edge triples or dangling graph edges. SQLite integrity is OK, foreign-key check is empty, and JSON/SQLite node ID sets match. These are structural findings only. Full schema and machine-readable results: `legacy-integrity.json`.

## Reuse matrix

| Asset | Decision | Reason / condition |
|---|---|---|
| atlas_data.json | MIGRATE | Preserve canonical IDs; quarantine unsupported claims; export small reviewed slices. |
| constitution_atlas.db | RETAIN AS REFERENCE | Read-only baseline and FTS behavior. Every one of 635 source-reference rows points to the same Constitution source. |
| curated_knowledge.py | REFACTOR | Useful institutional IDs, journeys and scenarios; independently review every substantive claim. |
| ingest_constitution.py | REFACTOR | Recover extraction logic; remove machine-specific default path, destructive DB replacement and unconditional verification labels. |
| extraction_validation_report.json | RETAIN AS REFERENCE | Self-reported counts, not independent validation. |
| main.py | REFACTOR | Reuse search/path concepts offline or in single TypeScript boundary; do not deploy unprotected write/AI endpoints. |
| tests/test_constitution_atlas.py | REUSE | Baseline regression tests, supplemented with adversarial and source checks. |
| frontend/src/App.tsx and store | REPLACE | Incomplete entry/build setup; crowded layout; search results fetched but never rendered; transient personal state. |
| frontend/package.json | RETAIN AS REFERENCE | Existing React/Cytoscape direction; no index.html, entry module, TS config or Vite config supplied. |
| standalone HTML | RETAIN AS REFERENCE | Full legacy interaction inventory; monolithic presentation is unsuitable as new application architecture. |
| requirements.txt, .env.example, README | RETAIN AS REFERENCE | Installation clues; README claims exceed the tested implementation. No secrets imported. |

## Material risks found in code

- Every edge lacks a stable ID and evidence-record ID. Free-text `ref` is present, but is not claim verification.
- Database edges default to `Verified (1.0)` without a verification operation.
- Report hardcodes 402 PDF pages, preamble success and a 100% PASS string; journey/simulation verification is merely a list length.
- Source attribution assigns the Constitution to every node, including judicial and administrative content. Do not inherit this as evidence.
- Clause parsing uses 260-character snippets and a 12-clause cap. It cannot support exact clause reconstruction.
- `find_shortest_path` traverses both directions and sometimes avoids the root, so it is neither a directed authority path nor always the graph's mathematical shortest path.
- Source POST writes without authentication; AI endpoint lacks auth/rate limits; permissive CORS; unrelated fallback nodes can imply evidence where retrieval failed.
- Ingestion entry point calls `ingest_pdf()` without parsing the README's `--pdf` argument and deletes the existing database before writing.
- Article 79 is assigned to `cluster_union_exec`; that categorization is not inherited by the new Parliament view.

## Source inspection and migration

Matching PDF found at the named Downloads location: 402 pages, preface dated 1 May 2026. Article 79 on PDF page 67 matches the legacy text after removal of the synthetic `Article ` prefix and whitespace normalization. This narrow check does not validate other articles or certify current law. Official source URL is retained with exact PDF-page locator.

Migration is additive and reversible: archive originals, retain node IDs, deterministic edge hashes, keep legacy assertions in a separate quarantine export, promote only reviewed content with recorded method, source hash, locator and review scope. Never overwrite the legacy DB or execute the old destructive importer on original files.
