# CONSTITUTION ATLAS — LEARNING MODE MASTER SPECIFICATION (`LEARNING_MASTER_SPEC.md`)

**Document ID:** `CA-LMS-001`  
**Version:** `1.0.0-PRODUCTION`  
**Target Implementation Agent:** Codex / Full-Stack Engineering Pipeline  
**Primary Constitutional Source:** *The Constitution of India* (Official Ministry of Law and Justice, Legislative Department Edition, as on 1st May 2026, 402 pages, incorporating up to the 106th Constitutional Amendment Act, 2023)  
**Canonical Knowledge Graph Baseline:** `constitution_atlas.db` / `atlas_data.json` (635 existing canonical nodes, 1,255 verified directional edges, plus 68 proposed Learning Mode expansion nodes explicitly cataloged in `manifests/canonical_graph_mapping.json`)

---

## 1. Executive Vision & Dual-Mode Architectural Philosophy

**Constitution Atlas** is an integrated scholarly and civic learning platform designed to make the entire architecture of Indian constitutional democracy comprehensible as a single, living, interconnected system of ideas, rules, institutions, procedures, and administrative realities.

Most civic and legal education platforms fail for one of two structural reasons:
1. **Atomized Textualism (The Bare-Act Trap):** They present the Constitution as a flat sequential list of 395+ Articles to be memorized by rote (e.g., memorizing that Article 75(3) says *"The Council of Ministers shall be collectively responsible to the House of the People"* without understanding how a No-Confidence Motion under Lok Sabha Rule 198, Money Bill supply refusals under Article 114, or anti-defection disqualifications under the Tenth Schedule actually determine whether a government survives).
2. **Decontextualized Abstraction (The Civics-Textbook Trap):** They offer simplified summaries of the "Three Branches of Government" divorced from actual constitutional text, judicial interpretation, statutory scaffolding, and on-the-ground district administration (such as how an Act of Parliament travels through Union Ministry Rules under Article 77(3) to a District Magistrate/Collector, Sub-Divisional Magistrate, and Tehsildar).

To overcome both failure modes, **Constitution Atlas** operates through two tightly coupled, state-synchronized modes built atop a **single shared Constitutional Knowledge Graph**:

### 1.1 Mode A: ATLAS MODE (Spatial & Relational Discovery)
* **Purpose:** Free-form, non-linear spatial exploration, multi-hop relationship tracing, shortest-path discovery, verbatim bare-act reading (all 470 active and historical Articles, 25 Parts, 12 Schedules, 3 Appendices), and comparative research.
* **Mental Model:** *Google Earth + Obsidian + Neo4j for Indian Constitutional Democracy.*
* **Core Primitives:** Nodes (`Constitutional`, `Cluster`, `Institutional`, `Administrative`, `Philosophical`, `Judicial`, `Historical`, `Process`), Directional Edges (`CONTAINS`, `ESTABLISHES`, `EMPOWERS`, `LIMITS`, `PROTECTS`, `INTERPRETS`, `ACCOUNTABLE_TO`, `CHECKS_AND_BALANCES`, `IMPLEMENTED_THROUGH`, `DEFINED_BY`, `RELATED_TO`, `HISTORICALLY_CONNECTED_TO`), and Multi-Depth Explanations (`beginner`, `intermediate`, `advanced`, `research`).

### 1.2 Mode B: LEARNING MODE (Structured Developmental Progression)
* **Purpose:** A rigorous, scaffolded, mastery-based curriculum (Levels 0 through 11) that guides a learner from foundational questions of human society, rules, and legitimate authority (`Level 0`) all the way to advanced constitutional jurisprudence, administrative practice, and complex multi-institution crisis reasoning (`Level 11`).
* **Mental Model:** *A Digital Constitutional University + Interactive Casebook + Personal Concept Map.*
* **Core Primitives:**
  * **Courses & Levels (`Level 0` to `Level 11`):** 12 progressive developmental stages organized as a spiral-systems curriculum.
  * **Modules & Lessons:** Self-contained, deeply written instructional units containing 17 standardized pedagogical components (from real-world opening problems and beginner analogies to verbatim constitutional text, CAD historical debates, misconception diagnostics, interactive institutional simulations, active reasoning prompts, and spaced-repetition flashcards).
  * **Bidirectional Graph Bridge:** Every concept, Article, institution, doctrine, or judgment mentioned inside a Learning Mode lesson is bound to its canonical Knowledge Graph ID (e.g., `art_21`, `inst_lok_sabha`, `judg_kesavananda`, `admin_dm_collector`). Clicking any bound concept triggers **Explore This Concept** (opening the synchronized split-pane graph inspector or jumping to Atlas Mode with a persistent **Return to Lesson** breadcrumb banner). Conversely, inspecting any node in Atlas Mode displays a **"Learn This in Curriculum"** badge linking directly to the exact Lesson and Section that teaches that node in depth.
  * **Progressive Personal Knowledge Map ("Fog-of-War Mastery Unlocks"):** As a learner completes lessons and passes mastery checks, the corresponding nodes and edges in their personal graph transition from `unexplored` (muted slate outline) → `introduced` (illuminated border) → `practiced` (active color fill) → `mastered` (gold constitutional halo), visually demonstrating how their understanding of Indian democracy is expanding into a connected network.

---

## 2. Epistemic Rigor & Eight-Layer Source Separation Policy

A core requirement of Constitution Atlas is **epistemic transparency**. Learners must never confuse a teaching analogy with a legal rule, or confuse an executive convention with an explicit constitutional text. Every paragraph block, callout card, simulation rule, and AI tutor response in Learning Mode carries an explicit `epistemic_layer` tag from the following eight-layer taxonomy:

| Layer Code | Epistemic Category | Visual Badge Color | Definition & Primary Authority Standard |
| :--- | :--- | :--- | :--- |
| `CONST_TEXT` | **Official Constitutional Text** | Warm Gold (`#f59e0b`) | Verbatim provisions, clauses, provisos, explanations, Schedules, and Amendment footnotes from the official 402-page Government of India Constitution PDF (1 May 2026 Edition). Always cited with exact Article/Clause and PDF page number (`p. 32–402`). |
| `STATUTORY_LAW` | **Statutory Enactment** | Emerald (`#10b981`) | Laws enacted by Parliament or State Legislatures under Article 246/327 (e.g., Representation of the People Acts 1950 & 1951, Right to Information Act 2005, Bharatiya Nagarik Suraksha Sanhita 2023 / CrPC, Contempt of Courts Act 1971, Lokpal and Lokayuktas Act 2013, Disaster Management Act 2005). |
| `JUDICIAL_HOLDING` | **Judicial Interpretation & Doctrine** | Rose Crimson (`#f43f5e`) | Binding ratios (`ratio decidendi` under Article 141), constitutional doctrines (Basic Structure, Golden Triangle, Pith and Substance, Proportionality), and legal tests established by the Supreme Court of India. Distinguished from *obiter dicta* and dissenting opinions. |
| `ADMIN_PRACTICE` | **Administrative Rules & Practice** | Teal Cyan (`#06b6d4`) | Subordinate legislation, executive rules, and institutional procedures (e.g., Government of India Allocation of Business Rules 1961 & Transaction of Business Rules 1961 under Article 77(3), Rules of Procedure and Conduct of Business in Lok Sabha/Rajya Sabha under Article 118, All-India Services Rules, State Land Revenue Manuals, Collectorate field practice). |
| `CONST_CONVENTION` | **Constitutional Convention** | Sky Blue (`#38bdf8`) | Unwritten practices that govern institutional behavior where the text is silent or discretionary (e.g., inviting the single largest party/pre-poll coalition in a hung Lok Sabha, the Speaker resigning from party forums upon election, collective cabinet confidentiality). |
| `HIST_EVIDENCE` | **Historical Primary Evidence** | Amber Ochre (`#eab308`) | Verbatim records from the Constituent Assembly Debates (CAD Volumes I–XII, 1946–1949), Drafting Committee minutes, B.N. Rau's notes, Government of India Act 1935, and historical Amendment Statements of Objects and Reasons. |
| `PHIL_ANALYSIS` | **Political & Constitutional Philosophy** | Royal Purple (`#a855f7`) | Normative and analytical frameworks (e.g., negative vs. positive liberty, formal vs. substantive equality, asymmetric federalism, transformative constitutionalism, competing originalist vs. living-tree interpretive theories). Disputed scholarly debates are always presented pluralistically with competing arguments treated fairly. |
| `PEDAGOGICAL_ANALOGY` | **Teaching Analogy & Civic Scenario** | Slate Indigo (`#94a3b8`) | Everyday Indian village, school, housing society, municipal ward, or district scenario designed to scaffold intuition before introducing formal legal terminology. Explicitly marked so learners never cite an analogy as black-letter law. |

---

## 3. System-Wide Architecture & Data Flow for Codex

Codex must implement Learning Mode as an extension of the existing FastAPI + SQLite/FTS5 backend (`backend/`) and React + TypeScript + Zustand + Cytoscape.js frontend (`frontend/`).

### 3.1 Shared Database Schema Extensions (`constitution_atlas.db`)

In addition to the existing `nodes`, `edges`, `sources`, `source_references`, `ai_enrichment`, and `fts_nodes` tables, Codex shall add the following normalized tables to `constitution_atlas.db`:

```sql
-- 1. Curriculum Levels (Levels 0 to 11)
CREATE TABLE learning_levels (
    level_id TEXT PRIMARY KEY,          -- e.g., 'level_00', 'level_01', ..., 'level_11'
    level_number INTEGER NOT NULL,
    title TEXT NOT NULL,
    subtitle TEXT NOT NULL,
    target_persona_stage TEXT NOT NULL, -- 'Foundational Civic Learner' -> 'Constitutional Scholar'
    estimated_hours REAL NOT NULL,
    prerequisite_level_ids_json TEXT NOT NULL,
    core_themes_json TEXT NOT NULL,
    mastery_gate_criteria_json TEXT NOT NULL
);

-- 2. Curriculum Modules within Levels
CREATE TABLE learning_modules (
    module_id TEXT PRIMARY KEY,         -- e.g., 'mod_00_01', 'mod_03_02'
    level_id TEXT NOT NULL,
    module_order INTEGER NOT NULL,
    title TEXT NOT NULL,
    summary TEXT NOT NULL,
    canonical_cluster_id TEXT,          -- Links to Primary Cluster in Atlas Mode
    FOREIGN KEY(level_id) REFERENCES learning_levels(level_id)
);

-- 3. Individual Lessons (Containing all 17 Pedagogical Sections)
CREATE TABLE learning_lessons (
    lesson_id TEXT PRIMARY KEY,         -- e.g., 'les_00_01_why_rules', 'les_03_04_art21_life_liberty'
    module_id TEXT NOT NULL,
    level_id TEXT NOT NULL,
    lesson_order INTEGER NOT NULL,
    title TEXT NOT NULL,
    estimated_minutes INTEGER NOT NULL,
    bloom_taxonomy_levels_json TEXT NOT NULL, -- e.g., '["Understand", "Analyze", "Evaluate"]'
    prerequisite_node_ids_json TEXT NOT NULL,
    target_node_ids_json TEXT NOT NULL,       -- Canonical graph nodes taught in this lesson
    target_edge_keys_json TEXT NOT NULL,      -- Canonical graph edges taught in this lesson
    opening_hook_json TEXT NOT NULL,          -- Compelling real-world dilemma
    sections_json TEXT NOT NULL,              -- Ordered teachable sections with epistemic tags
    everyday_examples_json TEXT NOT NULL,
    primary_sources_json TEXT NOT NULL,       -- Exact Articles, PDF pages, statutes, cases
    misconceptions_json TEXT NOT NULL,        -- Misconception -> Diagnostic -> Correction
    interactive_activities_json TEXT NOT NULL,-- Configured simulation/exercise specs
    active_reasoning_prompts_json TEXT NOT NULL,
    assessments_json TEXT NOT NULL,           -- Multi-format questions + explained rationales
    spaced_review_cards_json TEXT NOT NULL,   -- FSRS-compatible active recall cards
    graph_activities_json TEXT NOT NULL,      -- Guided graph tasks ('Explore', 'Trace', 'Reconstruct')
    advanced_reading_json TEXT NOT NULL,
    mastery_criteria_json TEXT NOT NULL,
    FOREIGN KEY(module_id) REFERENCES learning_modules(module_id),
    FOREIGN KEY(level_id) REFERENCES learning_levels(level_id)
);

-- 4. Bidirectional Node-to-Lesson Index
CREATE TABLE node_lesson_links (
    node_id TEXT NOT NULL,
    lesson_id TEXT NOT NULL,
    role TEXT NOT NULL,                 -- 'PRIMARY_SUBJECT' | 'PREREQUISITE' | 'CONNECTED_CONCEPT'
    section_anchor TEXT,
    PRIMARY KEY (node_id, lesson_id, role)
);

-- 5. Learner Progress, Mastery & FSRS Spaced Repetition State
CREATE TABLE learner_node_mastery (
    learner_id TEXT NOT NULL DEFAULT 'local_default',
    node_id TEXT NOT NULL,
    mastery_state TEXT NOT NULL,        -- 'UNEXPLORED' | 'INTRODUCED' | 'PRACTICED' | 'MASTERED'
    mastery_score REAL DEFAULT 0.0,     -- 0.0 to 1.0
    last_practiced_at TEXT,
    PRIMARY KEY (learner_id, node_id)
);

CREATE TABLE learner_review_schedule (
    card_id TEXT PRIMARY KEY,
    lesson_id TEXT NOT NULL,
    node_id TEXT NOT NULL,
    difficulty REAL DEFAULT 5.0,        -- FSRS D parameter (1.0 to 10.0)
    stability REAL DEFAULT 1.0,         -- FSRS S parameter (days until R drops to 90%)
    retrievability REAL DEFAULT 1.0,    -- Current probability of recall
    reps INTEGER DEFAULT 0,
    lapses INTEGER DEFAULT 0,
    due_at TEXT NOT NULL,
    last_reviewed_at TEXT
);
```

---

## 4. Complete Deliverable Inventory in This Specification Package

To ensure Codex can implement the entire Learning Mode without inventing curriculum structure, learning science logic, UX flows, or lesson prose, this package provides:

1. **`01_LEARNING_MASTER_SPEC.md`** *(This file)*: Dual-mode architecture, 8-layer epistemic policy, database schemas, and system invariants.
2. **`02_LEARNING_SCIENCE_RESEARCH.md`**: Critical review of 19 learning science domains with empirical strength ratings, cognitive pitfalls, and exact engineering specifications for Constitution Atlas.
3. **`03_CURRICULUM_ARCHITECTURE.md`**: Complete 12-Level (Levels 0–11), 36-Module, 108-Lesson curriculum blueprint with pedagogical justification of the spiral-systems progression.
4. **`04_GRAPH_LEARNING_INTEGRATION.md`**: Full technical and UX specification for the 8 bidirectional Learning ↔ Atlas graph interactions and canonical node/edge binding rules.
5. **`05_ACTIVITY_AND_ASSESSMENT_SYSTEM.md`**: Engineering blueprints, state machines, and JSON schemas for all 15 interactive learning activity archetypes and the FSRS-4.5 spaced repetition & mastery engine.
6. **`06_AI_TUTOR_DESIGN.md`**: Graph-RAG Socratic Tutor design, 4-depth adaptive explanation engine, misconception detector, progressive 3-stage hint generator, and 100% offline deterministic fallback architecture.
7. **`07_LEARNING_UX_SPEC.md`**: Editorial design system, typography, wireframes, component hierarchy, split-pane lesson/graph reader, personal knowledge map, and WCAG 2.2 AA accessibility specs.
8. **`08_CONTENT_AND_SOURCE_POLICY.md`**: Primary source citation rules, judicial holding vs. dicta distinction, statutory/administrative layer separation, and neutral treatment of unsettled constitutional questions.
9. **`09_LEARNING_IMPLEMENTATION_GUIDE.md`**: Step-by-step Codex implementation handoff, FastAPI endpoints, React/Zustand store slices, and verification test suite specifications.
10. **Four Comprehensive Teaching Content Volumes (`courses/VOL_1` through `courses/VOL_4`)**:
    * **`courses/VOL_1_LEVELS_0_TO_2_FOUNDATIONS_AND_ORIGINS.md`**: Complete, unabridged teaching lessons for Levels 0, 1, and 2 (Society, Rules, Authority, Political Philosophy, Colonial Antecedents, and Constituent Assembly Debates).
    * **`courses/VOL_2_LEVELS_3_TO_5_CONSTITUTIONAL_STRUCTURE_UNION_AND_STATES.md`**: Complete, unabridged teaching lessons for Levels 3, 4, and 5 (Preamble, Rights, DPSPs, Duties, Amendments, Emergencies, Federalism, President, PM, Cabinet, Parliament, State Governments, and Panchayati Raj / Municipalities).
    * **`courses/VOL_3_LEVELS_6_TO_8_JUDICIARY_ELECTIONS_AND_PUBLIC_ADMINISTRATION.md`**: Complete, unabridged teaching lessons for Levels 6, 7, and 8 (Supreme Court, High Courts, Writs, Judicial Review, Election Commission, RPA 1950/1951, Anti-Defection, Ministries, Civil Services, District Magistrate/Collector, SDM, Tehsildar, Police, Revenue, and Public Finance).
    * **`courses/VOL_4_LEVELS_9_TO_11_HISTORY_ADVANCED_THEORY_AND_APPLIED_REASONING.md`**: Complete, unabridged teaching lessons for Levels 9, 10, and 11 (Constitutional Amendments 1st–106th, Basic Structure Evolution, Constitutional Morality, Competing Interpretive Philosophies, and Complex Multi-Institution Applied Constitutional Scenarios).
11. **Machine-Readable JSON Manifests (`manifests/`)**:
    * `manifests/curriculum_manifest.json`
    * `manifests/canonical_graph_mapping.json`
    * `manifests/progress_and_handoff_manifest.json`
12. **`CONSTITUTION_ATLAS_COMPLETE_LEARNING_SPECIFICATION.md`**: Single unified master compilation combining all architectural specifications and all four teaching volumes in one continuous document for single-file ingestion or review.
