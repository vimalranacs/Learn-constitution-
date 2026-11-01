# CONSTITUTIONAL ACCURACY, SOURCE POLICY & CODEX IMPLEMENTATION GUIDE (`08_CONTENT_AND_SOURCE_POLICY.md` & `09_LEARNING_IMPLEMENTATION_GUIDE.md`)

**Document ID:** `CA-CSP-008 / CA-IMP-009`  
**Purpose:** Primary source verification rules, epistemic boundaries, and the exact technical handoff guide for Codex to implement Learning Mode.

---

## PART A: CONTENT & SOURCE VERIFICATION POLICY (`CONTENT_AND_SOURCE_POLICY.md`)

### 1. Primary Source Hierarchy & Citation Format
Every factual, legal, institutional, and historical claim in **Constitution Atlas — Learning Mode** adheres to the following strict verification protocol:

1. **Constitutional Text (`CONST_TEXT`):**
   * **Primary Authority:** *The Constitution of India* (Ministry of Law and Justice, Legislative Department, Government of India, 1st May 2026 Edition, 402 pages, incorporating up to the 106th Constitutional Amendment Act, 2023) and the India Code 10 September 2026 Edition.
   * **Citation Standard:** Every constitutional reference must state the exact **Part**, **Article** (including clause/sub-clause/proviso), and **Official PDF Page Number** (e.g., `Article 21, Part III, Official 2026 PDF p. 41`; `Article 75(3), Part V Ch. I, Official 2026 PDF p. 63`; `Article 330A, Part XVI, Official 2026 PDF p. 221`).
   * **Omitted / Historical Articles:** Whenever referencing omitted provisions (e.g., Article 31 Right to Property omitted by the 44th Amendment Act, 1978, p. 45; or Part VII omitted by the 7th Amendment Act, 1956), the text must explicitly state its omitted status, the repealing Amendment Act, and where the subject matter currently resides (e.g., Article 300A, Part XII Ch. IV, PDF p. 201).

2. **Statutory Provisions (`STATUTORY_LAW`):**
   * **Distinction Rule:** Never state that "the Constitution provides X" when X is actually governed by an ordinary Act of Parliament. For example:
     * The Constitution (`art_324`–`art_329`) establishes the Election Commission and adult suffrage, but deposit amounts, nomination papers, corrupt practices, and registration of political parties (Section 29A) are governed by the **Representation of the People Act, 1951**.
     * The Constitution (`art_312`) authorizes All-India Services, but service conditions and cadre rules are governed by the **All-India Services Act, 1951** and rules framed under Article 309.
     * Executive magistracy and preventive orders by a District Magistrate/SDM are governed by the **Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)** (formerly Code of Criminal Procedure, 1973), while land revenue hierarchy (Collector → SDM → Tehsildar → Kanungo → Patwari/Lekhpal) is governed by **State Land Revenue Codes** (Entry 18 & 45, List II, Seventh Schedule), with nomenclature varying across states (e.g., *Mamlatdar* in Gujarat/Maharashtra, *Tahsildar* in UP/MP/Rajasthan/Tamil Nadu, *Mandal Revenue Officer* in Andhra Pradesh/Telangana).

3. **Judicial Interpretations (`JUDICIAL_HOLDING`):**
   * **Zero Hallucination Rule:** Only real, verifiable Supreme Court of India and High Court judgments with authentic citations (`AIR`, `SCC`, `SCR`, `INSC`) may be cited.
   * **Ratio vs. Obiter vs. Dissent:** Clearly distinguish the binding majority holding (`ratio decidendi` under Article 141) from concurring nuances or historic dissents (such as Justice Fazl Ali's dissent in *A.K. Gopalan* (1950), Justice H.R. Khanna's dissent in *ADM Jabalpur* (1976), or Justice K. Subba Rao's dissent in *Kharak Singh* (1962), each of which was later vindicated by larger Constitution Benches).
   * **Unsettled & Evolving Questions:** Where constitutional questions remain debated among scholars or pending before larger benches (e.g., the exact contours of the Money Bill test under Article 110(1) referred to a 7-Judge Bench in *Roger Mathew v. South Indian Bank* (2020), or philosophical debates between originalism and living constitutionalism), present the competing constitutional arguments fairly and neutrally without declaring a partisan winner.

---

## PART B: CODEX IMPLEMENTATION HANDOFF GUIDE (`LEARNING_IMPLEMENTATION_GUIDE.md`)

### 1. How Codex Should Consume This Package

This specification package is organized so Codex can ingest both the **architectural specs** and the **machine-readable JSON manifests + Markdown lesson volumes** directly into the application build pipeline:

```
constitution_atlas_learning_ecosystem/
├── 01_LEARNING_MASTER_SPEC.md
├── 02_LEARNING_SCIENCE_RESEARCH.md
├── 03_CURRICULUM_ARCHITECTURE.md
├── 04_GRAPH_LEARNING_INTEGRATION.md
├── 05_ACTIVITY_AND_ASSESSMENT_SYSTEM.md
├── 06_AI_TUTOR_DESIGN.md
├── 07_LEARNING_UX_SPEC.md
├── 08_CONTENT_AND_SOURCE_POLICY.md
├── 09_LEARNING_IMPLEMENTATION_GUIDE.md
├── courses/
│   ├── VOL_1_LEVELS_0_TO_2_FOUNDATIONS_AND_ORIGINS.md
│   ├── VOL_2_LEVELS_3_TO_5_CONSTITUTIONAL_STRUCTURE_UNION_AND_STATES.md
│   ├── VOL_3_LEVELS_6_TO_8_JUDICIARY_ELECTIONS_AND_PUBLIC_ADMINISTRATION.md
│   └── VOL_4_LEVELS_9_TO_11_HISTORY_ADVANCED_THEORY_AND_APPLIED_REASONING.md
├── manifests/
│   ├── curriculum_manifest.json
│   ├── canonical_graph_mapping.json
│   └── progress_and_handoff_manifest.json
└── CONSTITUTION_ATLAS_COMPLETE_LEARNING_SPECIFICATION.md
```

### 2. Step-by-Step Engineering Implementation Sequence for Codex

1. **Step 1 — Run Graph Expansion & Curriculum Ingestion (`backend/ingest_learning.py`):**
   * Read `manifests/canonical_graph_mapping.json`. Insert the `proposed_addition` nodes (e.g., `prop_phil_state_sovereignty`, `prop_admin_patwari_lekhpal`, `prop_stat_bnss_2023`, `prop_stat_rti_act_2005`) and their verified edges into `nodes`, `edges`, and `fts_nodes` in `constitution_atlas.db`.
   * Read `manifests/curriculum_manifest.json` and parse the four Markdown course volumes (`courses/VOL_1` to `VOL_4`) into the `learning_levels`, `learning_modules`, `learning_lessons`, and `node_lesson_links` tables.
2. **Step 2 — Mount FastAPI Learning Endpoints (`backend/main.py`):**
   * `GET /api/learning/curriculum`: Returns all 12 Levels, Modules, lesson summaries, and learner mastery percentages.
   * `GET /api/learning/lessons/{lesson_id}`: Returns the complete 17-section lesson payload, bound canonical subgraph (`nodes` + `edges`), interactive simulation config, assessments, and FSRS review cards.
   * `GET /api/learning/node-lessons/{node_id}`: Returns all lessons that teach or reference a given graph node (powering the *"Learn This in Curriculum"* badge inside Atlas Mode).
   * `POST /api/learning/mastery`: Updates `learner_node_mastery` and `learner_review_schedule` using the FSRS-4.5 formulas specified in `05_ACTIVITY_AND_ASSESSMENT_SYSTEM.md`.
   * `POST /api/learning/tutor`: Executes the Dual-Engine Socratic AI Tutor (`06_AI_TUTOR_DESIGN.md`).
3. **Step 3 — Implement Frontend Learning Mode Components (`frontend/src/learning/`):**
   * `LearningDashboard.tsx`: 12-Level spiral roadmap + Personal Fog-of-War Knowledge Map + Daily FSRS Review queue.
   * `LessonWorkspace.tsx`: 3-zone Split-Pane Lesson Reader with epistemic layer badges, inline `[Node](node:id)` chips, and scroll-synchronized `Cytoscape.js` companion subgraph.
   * `ActivityRenderer.tsx`: Pluggable dispatcher rendering the 15 interactive archetypes (`ARCH_INTERACTIVE_DIAGRAM` through `ARCH_GRAPH_RECONSTRUCTION`).
   * `AtlasLearningBridge.tsx`: Manages the `LessonReturnContext` top banner when jumping between Learning Mode and Atlas Mode.
