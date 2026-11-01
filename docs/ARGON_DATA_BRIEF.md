# Argon data brief and import contract — 2 November 2026

## What the current data actually supports
635 canonical entities,1258 relationships;3 source_checked and1255 needs_review. 881 CONTAINS and254 RELATED_TO edges dominate the graph; only3 INTERPRETS and12 INTERPRETED_BY links are recorded. All references/explanations are nonempty but that does not verify their claims.23 entities have no recorded edges.20 ecosystem lessons now contain261 sections; their canonical anchors all resolve. Counts are reproducible with atlas-web/scripts/audit-content.mjs; full gap inventory is content/coverage-audit.json. The graph is not an exhaustive account of the Constitution or current law.

## Priority0: repair before expansion
Request corrected Article boundaries and legal-status annotations, especially Article2 versus2A and omitted provisions. Supply current knowledge.json, source-extraction-report.json, source-check.json and the original official PDF. Return proposed patches only: stable existing ID, current excerpt, corrected verbatim passage, PDF page AND printed page, Article/clause boundaries, amendment/commencement status, exact official URL, document edition/as-of date, evidence quote and correction rationale. Distinguish omitted clause annotations from omission of a whole Article. Do not publish Volume7 until these repairs are independently reviewed.

Prompt to Argon:
"Audit the supplied extraction against the supplied official primary text. Do not rely on memory. Start with art_2 and any passage mentioning2A or omission. Return JSON patches under the contract below, with unresolved records where evidence is missing. Preserve IDs and original text. Do not assert currentness without an official dated source. Do not mark any output source_checked."

## Priority1: connect existing isolated entities
Exact IDs: admin_cabinet_sec,admin_regulatory_bodies,amend_1,amend_101,amend_106,amend_42,amend_44,amend_73_74,amend_86,doc_pith_substance,hist_adoption_1949,inst_ag,inst_vice_president,judg_golaknath,judg_gopalan,judg_navtej,judg_vishaka,phil_const_morality,phil_federalism,phil_rule_of_law,phil_secularism,phil_sep_powers,proc_emergency.
These are research targets, not asserted legal connections. Split broad/composite entities only with explicit migration maps (especially amend_73_74 and generic regulators). No automatic ID renaming.

Prompt:
"Using this exact isolated-ID inventory and canonical node list, propose at most30 source-backed directed edges. Each must identify source,target,type, scoped explanation, primary-source URL and pinpoint, exact supporting quote, legal/temporal qualifications, and whether the connection is structural, interpretive, historical or pedagogical. If evidence does not support a link, return unresolved with the research needed. Never connect nodes merely because names co-occur. Preserve original edge direction and do not infer authority from association."

## Priority2: amendments and judgments
For the seven recorded amendment entities, request official Act text, assent and commencement dates distinguished, provision-by-provision before/after mapping, affected Article/Schedule IDs, implementation dependencies and unresolved temporal effects. Do not infer that enactment equals commencement. For each existing judgment, request official court judgment URL, date, neutral/reporter citation where verified, bench composition, precise holding paragraphs, provisions interpreted, majority/dissent distinction, relief, scope/limits and later treatment with dated evidence. Audit the direction of INTERPRETS/INTERPRETED_BY; do not create duplicate inverse edges without an explicit display policy.

Prompt:
"Produce one reviewable batch of five existing judgments or amendments. Return verified-source evidence records plus candidate node/edge patches; distinguish holding from illustration, dissent and later commentary. Flag uncertain later treatment rather than treating historical holdings as current law. Use official sources only. Supply short scoped quotes with paragraph or section pinpoints."

## Priority3: deepen teaching and history
Request lesson-to-evidence mappings for claims, prerequisites as pedagogical metadata, misconception/correction pairs with sources, worked hypotheticals clearly labelled as hypotheticals, one reasoning assessment plus rubric per lesson, glossary definitions and accessible summaries. Keep editorial metadata separate from published reading prose. Current activity blueprints are not all runnable simulations. Ask for structured decision branches, outcomes, feedback, source IDs and acceptance fixtures before implementing additional activities. For history/drafting, request dated events, committee mandates, primary Constituent Assembly Debates references (volume,date,page/speaker), and links explicitly marked historical influence rather than legal authority.

Prompt:
"For two supplied lesson IDs, identify unsupported or shallow claims and map each to a primary-source evidence record. Propose a beginner explanation, one labelled hypothetical, misconception feedback and one assessment with rubric. Return learningObjectives, prerequisites, sections and activities separately. No internal instructions or proposed-node metadata in learner prose. All new legal claims need evidence; unresolved claims must remain unpublished."

## JSON exchange contract
Return UTF-8 JSON with schemaVersion:1, batchId, asOf, sources[], nodePatches[], edgeProposals[], lessonPatches[], unresolved[]. Sources: id,title,publisher,url,publicationDate,accessedAt,pinpoint,quote,edition. Node patches: id,operation(add/update),fields,evidenceIds,limitations. Edge proposals: id,source,target,type,explanation,evidenceIds,temporalScope,relationshipClass,status:needs_review. Lesson patches: lessonId,sectionId,claim,evidenceIds,proposedText,activity(optional). Unresolved: targetId,question,reason,nextSourceNeeded. Never include credentials, runtime configuration or instructions for the application to execute. Avoid HTML and executable code. Keep each batch small enough for manual evidence review.

## Acceptance gate
Validate JSON/schema, unique stable IDs, endpoints, allowed relation vocabulary, source URLs and pinpoints, quote matching where source text is available, date/commencement consistency, duplicates/inverse edges and claim-to-evidence mapping. Run import dry-run with counts and human-readable diffs. Quarantine unresolved material. A human/source review must approve promotion from needs_review; Argon generation alone is never verification. No Argon import or fabricated relationship was added in this release.

## Implemented now versus waiting for evidence
Implemented now: trace capabilities/empty states, request recovery, reader retry, canonical search, graph coverage audit and accurate documentation. Requires Argon plus review: repaired provisions, new legal links, amendment effects, judgment treatment, expanded substantive explanations and activity outcomes. After data acceptance: build contextual learning paths and deeper evidence-backed graph expansion without inflating the visible canvas.
