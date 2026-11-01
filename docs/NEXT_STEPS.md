# Next work
Read CODEX_RESUME.md and docs/IMPLEMENTATION_PLAN.md first. Expanded Site is live; do not recreate it.

## Session 2026-11-01 — Fixes applied (rebuild + redeploy required)
- **Trace Connections fixed:** Removed `getChatGPTUser()` auth guard from `/api/knowledge`. Also fixed `findPath → null → readObject` crash by wrapping null in `{noPath:true}` object.
- **Compare fixed:** Added `method="get"`, `type="submit"`, replaced `defaultValue` with `selected` prop on options for correct SSR rendering.
- **Ecosystem metadata removed:** 20 "Prerequisite Concepts" sections, 20 "Canonical Knowledge Graph Connections" sections, 41 inline content-type tags, and all `Required Prior Nodes`/`Target Canonical Nodes Introduced` bullet lines removed from `ecosystem.json`. Graph connections preserved in `lesson.sources` and surfaced via "Explore in Atlas" UI.
- **URL change:** Requires manual action in ChatGPT Sites dashboard. See `docs/CUSTOM_URL_AND_HOSTING.md` and session changelog.

## Remaining items
1. **Rebuild & redeploy** `atlas-web/` to ChatGPT Sites for all fixes to go live.
2. **Check `/api/entities/[id]`** — may have a similar auth guard to the one removed from `/api/knowledge`.
3. Review/correct Article extraction boundaries and add targeted regression fixtures.
4. Improve completion/progress coordination, offline recovery and mobile/accessibility behavior.
5. Expand advanced curriculum, reviewed judicial corpus, constitutional history and jurisdiction-specific civic scenarios.
6. Keep publishing independently tested phases and maintain explicit unresolved acceptance gates.
