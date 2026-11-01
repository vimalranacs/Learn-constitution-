# Active checkpoint — 1 November 2026
Latest user request overrides earlier graph designs: immersive white/black circular universe, expand in place, near-node popup, animated camera, in-canvas reader/AI. Implemented in app/components/UniverseExplorer.tsx, app/universe.css and lib/universe.mjs using D3, GSAP, Lenis reader and optional Vanta atmosphere. Old Explorer is unused by /explore.

Deployed source ea0a54c23b901fdaab156453cf5c01b2473430a3, version6 appgprj_6ae6663707bc819186fad83fa35bb747~appgver_76611614d5d88191aad16bb836b770a3. Deployment appgdep_6ae76a000a208191b6518daa0e27e6b5 succeeded, env revision3. Public URL https://constitution-atlas-vimal.blondebarge1.chatgpt.site/explore . PUBLIC audience explicitly requested. Preserve it.

Features: eight themes, progressive cumulative expansion/collapse, collision relaxation for new nodes, drag/zoom/pan, minimap, visit trail, guided journey, save/restore, search, small node cards, typed relationship details, reader and contextual AI. 140 visible-node budget keeps exploration responsive; reveal/fold to continue. GSAP mutates positions with circular cache: always serialize cleanPositions only.

Production navigation fixed by native anchors: next/link prefetch in Vinext threw TypeError f is not a function and prevented clicks. Do not reintroduce without production verification. Public device workspaces use random HttpOnly cookie, per-owner storage and CSRF validation. No sign-in gate. Existing account records remain separately keyed.

AI configured server-side: gemini-3.1-flash-lite. No key in source/export. Summary/explain/example/quiz uses selected entity or exact lesson section, language/depth and last4 exchanges. Exact citations/quotes validated; semantic review still needed. Daily limits30per visitor and150sitewide. Live Article79 AI previously verified with source quote.

Content:635 canonical nodes/1258 edges; only Article79/3 composition edges source-checked. 20 ecosystem lessons/300 reading sections plus original15 lessons. Volume7 excluded due Article2/2A omission-boundary defect. Do not claim complete legal verification or implemented curriculum simulations.

Portable deliverable artifacts/constitution-atlas-universe.zip (76files, source plus lockfile, no dependencies/build/data/secrets). Standard Next16.4.3, Node24/Docker, SQLite durable disk. Build and runtime public-http pass. Set ATLAS_ORIGIN, ATLAS_DATABASE_PATH, GEMINI_API_KEY privately, GEMINI_MODEL. No domain chosen. Guide docs/CUSTOM_URL_AND_HOSTING.md. Docker configuration supplied but Docker execution not tested.

Validation:15 Node tests and TypeScript passed; final Sites and portable production builds pass. Final live and standalone public-http pass (public routes, unique sessions, isolated note roundtrip cleanup). Browser verified expansion, nearby card, in-canvas reader, live save. Full accessibility/mobile/content acceptance remains open. Dev5173 and portable3001 may be running.

Final live Gemini check: HTTP200, engine gemini, summary restricted to citation art_79. Mobile390x844 graph fit inspected; desktop viewport restored. Live save/reset/restore recovered19nodes successfully. Portable source ZIP integrity verified.
