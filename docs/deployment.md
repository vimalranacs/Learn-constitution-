# Using and deploying Constitution Atlas
Updated 1 November 2026.

## Open the website
Visit https://constitution-atlas-vimal.blondebarge1.chatgpt.site and sign in with an approved email. The owner is officialvimalrana@gmail.com; the other approved addresses are mindscalers@gmail.com, vimalrana877@gmail.com and reversemindset0@gmail.com. Access is private/custom, not public. An access gate before sign-in is expected. Use the same approved email in the sign-in flow; an unrelated account will not grant access.

Atlas explores imported entities, connections, primary text and comparisons. Learn provides the 15-lesson foundation. My workspace holds your notes, bookmarks, progress, reviews and saved graph views. A source-checked label applies only to the specifically checked passage or relationship. Other content remains explicitly under review.

## What is hosted
The app is a Vinext/React Worker deployed by Sites. Its DB binding is a D1 database with personal_records and ai_usage tables. Personal rows are scoped to authenticated user IDs. The server holds the Gemini secret and model configuration. Browser code does not receive that key. Questions and retrieved content are sent to Gemini when you ask; private notes are not included. AI has a 30-request daily per-user limit and may refuse an invalid response. Prepared lessons and reading do not require Gemini.

Current expanded source checkpoint: dd56d83c0a75304489e70b54683e1275cb6f0333. Deployment appgdep_6ae6704572808191b63d51d3efa7063f succeeded, including environment revision3 and D1 schema. See CODEX_RESUME.md for later checkpoints.

## Make and publish changes
1. Open the atlas-web folder. Keep its .openai/hosting.json project ID unchanged; this is the existing website, not a new Site.
2. Install dependencies using npm.cmd run install:ci. Start a local preview with npm.cmd run dev. Local preview uses a synthetic development identity; production uses real approved accounts.
3. For schema changes, generate a new Drizzle migration and test it locally. Do not rewrite migrations already applied to production or casually replay SQL. Preserve user data.
4. Run node --test tests/*.test.mjs and node node_modules/typescript/bin/tsc --noEmit. With the dev server running, run node tests/http-integration.mjs. That integration test expects no local Gemini key and verifies the honest retrieval fallback.
5. Use the installed Sites build-site.mjs helper to produce the Worker build. Inspect changed routes in a browser at desktop and mobile sizes. A build alone is not acceptance.
6. Obtain a short-lived source repository credential using the Sites connector for project appgprj_6ae6663707bc819186fad83fa35bb747. Supply it to site-workflow.mjs through hidden stdin. Never paste it into a shell argument, file, Git remote URL or documentation. Package an archive outside the source checkout.
7. The helper returns the exact pushed commit and artifact path. Use save_site_version with those values, then deploy_site_version with the returned saved-version ID. The Site now has approved external viewers, so the owner-only private deployment shortcut no longer applies. Preserve its custom audience.
8. If deployment is pending, inspect its status until succeeded or failed. Verify the D1 schema through Sites database overview. Do not declare success for a failed or pending deployment. Keep the exact source/version/deployment identifiers in CODEX_RESUME.md.
9. Sign in and check a lesson, save/reload a note and progress, ask a source-specific AI question, and follow its quoted evidence. Repeat with a second approved account to check separation. Never share login credentials for this test.

## Troubleshooting
Access denied: verify the exact email and existing allowlist. Do not make the Site public as a workaround.
Storage error: inspect deployment and DB binding/migration status. Reading should remain possible when progress cannot load.
AI error: check server model/key configuration and provider quota. An exact-quote/citation validation failure intentionally rejects the answer. Do not weaken validation to make an answer appear.
Failed deployment: retain the last working deployment and source. Fix the reported error, rebuild and save the exact new commit. Do not pair an old artifact with new source.

## Acceptance still pending
Authenticated production interactions and actual multi-account separation have not been observed; the user will test later. Direct Gemini provider validation passed, but live authenticated AI endpoint acceptance remains pending. Wider accessibility checks, full legal/source review, advanced curriculum and research corpus remain open. The application is not the completed master specification.
