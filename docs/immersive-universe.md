# Immersive graph design revision
The latest direct user request supersedes earlier graph layouts: white/black, centered mind-map universe, expansion in place, small contextual cards, no forced page navigation. Reference: Downloads/Constitutional Education Mindmap.png.

Implementation: UniverseExplorer + universe.mjs. D3 handles pan/zoom, drag and deterministic collision relaxation of newly added nodes while existing positions stay fixed. GSAP animates camera, new positions and cards. Lenis smooths the optional in-canvas reader, not graph zoom. Vanta FOG supplies a very faint optional monochrome backdrop; no decorative graph edges are treated as data. Reduced-motion and atmosphere controls are available.

Root themes: Articles, Parts, Schedules, Amendments, Judgments, Preamble, History and Drafting. Canonical IDs reused. Theme links explicitly labelled browsing connections; typed relationships preserve recorded direction/evidence. Expanded nodes accumulate instead of replacing a neighborhood. Scoped140-node visible cap protects usability; fold/reset/reveal-more supports continued exploration. No claim that all constitutional history/judgments/amendments are exhaustively represented.

Reading card: source passage and AI inside the canvas; source PDF can open separately; same selected node remains the context. Guided introductory journey, search, breadcrumb trail, overview, saved view and map controls. Previous tree explorer retained in source as prior implementation but /explore now uses UniverseExplorer.

Perform validation at the end of this cohesive design pass, per user request; do not repeatedly rerun tests for cosmetic edits.
