# DEEP KNOWLEDGE GRAPH & LEARNING MODE INTEGRATION SPECIFICATION (`GRAPH_LEARNING_INTEGRATION.md`)

**Document ID:** `CA-GLI-004`  
**Purpose:** Full UX, cognitive, and technical specification for bidirectional integration between **Learning Mode** and **Atlas Mode**, ensuring both modes operate on the single canonical 635-node Constitutional Knowledge Graph (`constitution_atlas.db` / `atlas_data.json`).

---

## 1. Theoretical Foundation: Why Spatial Graph Integration Accelerates Constitutional Mastery

In cognitive psychology, expert legal and institutional thinkers differ from novices not in the sheer volume of isolated facts they recall, but in the **relational density of their mental schemas** (Chi, Feltovich & Glaser, 1981; Novak & Cañas, 2008). When a novice reads Article 75(3) (`art_75`), they encode an isolated sentence. When a constitutional scholar reads Article 75(3), they immediately activate a connected topological neighborhood:
* `inst_council_ministers` —[`ACCOUNTABLE_TO` (Art. 75(3))]→ `inst_lok_sabha`
* `inst_lok_sabha` —[`EMPOWERS` (Arts. 109–110, 114)]→ `proc_money_bill` (Control of the Purse)
* `inst_pm` —[`HEADS` (Art. 74(1))]→ `inst_council_ministers`
* `inst_pm` —[`ADVISES` (Arts. 74(1), 78)]→ `inst_president`
* `sched_10` (Anti-Defection Law) —[`REGULATES` (Art. 102(2))]→ `inst_lok_sabha` voting stability during confidence motions.

By coupling the linear narrative of **Learning Mode** with the spatial topology of **Atlas Mode**, Constitution Atlas externalizes this expert semantic network directly on screen.

---

## 2. Canonical Graph Identifier Contract & Proposed Additions Policy

Every lesson in Learning Mode MUST reference existing canonical graph IDs from `atlas_data.json` verbatim whenever they exist:
* **Constitutional Nodes:** `const_india`, `preamble`, `part_I` to `part_XXII` (including `part_IVA`, `part_IXA`, `part_IXB`, `part_XIVA`), `art_1` to `art_395` (including all alphanumeric articles such as `art_14`, `art_19`, `art_21`, `art_21A`, `art_31A`, `art_31B`, `art_31C`, `art_32`, `art_38`, `art_39`, `art_39A`, `art_44`, `art_50`, `art_51A`, `art_52`, `art_53`, `art_72`, `art_74`, `art_75`, `art_76`, `art_78`, `art_79`, `art_80`, `art_81`, `art_83`, `art_84`, `art_93`, `art_105`, `art_107`, `art_108`, `art_109`, `art_110`, `art_111`, `art_112`, `art_123`, `art_124`, `art_131`, `art_136`, `art_141`, `art_142`, `art_143`, `art_148`, `art_153`, `art_163`, `art_164`, `art_168`, `art_200`, `art_213`, `art_214`, `art_226`, `art_227`, `art_239AA`, `art_243` to `art_243ZT`, `art_245`, `art_246`, `art_246A`, `art_254`, `art_262`, `art_263`, `art_266`, `art_267`, `art_279A`, `art_280`, `art_300A`, `art_309`, `art_310`, `art_311`, `art_312`, `art_315`, `art_323A`, `art_324`, `art_326`, `art_330`, `art_330A`, `art_332`, `art_332A`, `art_334A`, `art_338`, `art_338A`, `art_338B`, `art_352`, `art_355`, `art_356`, `art_358`, `art_359`, `art_360`, `art_368`, `art_370`, `art_371` to `art_371J`, `art_395`), `sched_1` to `sched_12`, `appendix_1` to `appendix_3`, and `amend_1`, `amend_42`, `amend_44`, `amend_73_74`, `amend_86`, `amend_101`, `amend_106`.
* **Institutional Nodes:** `inst_parliament`, `inst_lok_sabha`, `inst_rajya_sabha`, `inst_speaker_ls`, `inst_parl_committees`, `inst_president`, `inst_vice_president`, `inst_pm`, `inst_council_ministers`, `inst_supreme_court`, `inst_high_courts`, `inst_subordinate_courts`, `inst_eci`, `inst_cag`, `inst_finance_comm`, `inst_gst_council`, `inst_upsc`, `inst_ag`, `inst_ncsc`, `inst_state_govt`, `inst_governor`, `inst_state_legislature`, `inst_panchayati_raj`, `inst_municipalities`, `inst_citizens`.
* **Administrative Nodes:** `admin_ministries`, `admin_cabinet_sec`, `admin_civil_services`, `admin_dm_collector`, `admin_sdm`, `admin_tehsildar`, `admin_regulatory_bodies`.
* **Philosophical Nodes:** `phil_liberty`, `phil_equality`, `phil_justice`, `phil_fraternity`, `phil_const_morality`, `phil_rule_of_law`, `phil_dignity`, `phil_privacy`, `phil_secularism`, `phil_federalism`, `phil_sep_powers`.
* **Judicial Nodes:** `doc_basic_structure`, `doc_golden_triangle`, `doc_harmonious_const`, `doc_proportionality`, `doc_pith_substance`, `judg_kesavananda`, `judg_maneka`, `judg_minerva`, `judg_puttaswamy`, `judg_bommai`, `judg_golaknath`, `judg_gopalan`, `judg_indra_sawhney`, `judg_vishaka`, `judg_coelho`, `judg_njac`, `judg_kihoto`, `judg_navtej`, `judg_shreya_singhal`, `judg_olga_tellis`, `judg_dk_basu`, `judg_art370`.
* **Historical & Process Nodes:** `hist_goi_1935`, `hist_const_assembly`, `hist_obj_resolution`, `hist_drafting_comm`, `hist_adoption_1949`, `proc_ordinary_bill`, `proc_money_bill`, `proc_const_amend_bill`, `proc_govt_formation`, `proc_judicial_review`, `proc_emergency`, `proc_rpa_1951`.

**Proposed Addition Rule:** Whenever a lesson in Level 0, 1, 8, or 10 introduces a foundational pre-constitutional or sub-district concept not yet in the base 635 nodes (e.g., `prop_phil_state_sovereignty`, `prop_admin_sho_police`, `prop_admin_patwari_lekhpal`, `prop_stat_rti_act_2005`, `prop_stat_bnss_2023`), it MUST be prefixed with `prop_` in lesson markup and cataloged in `manifests/canonical_graph_mapping.json` with `"status": "proposed_addition"` along with its full node and edge definition so Codex can ingest it cleanly into `constitution_atlas.db`.

---

## 3. Specification of the 8 Core Graph-Learning Interactions

### 3.1 Interaction 1: `Explore This Concept` (Inline Node Chip → Synchronized Split-Pane Graph)
* **Educational Purpose:** Eliminates split attention by letting learners inspect the exact constitutional wording, 1-hop institutional neighbors, and ontology classification of any concept mentioned in lesson prose without losing their reading position.
* **User Action:** Clicking an inline interactive chip in the lesson text—rendered as `[🏛️ Lok Sabha](node:inst_lok_sabha)` or `[📜 Article 21](node:art_21)`.
* **Expected System Behavior:**
  1. In desktop Split-Pane view, the right-hand **Companion Mini-Graph & Inspector** (4 columns wide) smoothly centers on `node_id` (`cy.animate({ center: { eles: node }, zoom: 1.3 }, { duration: 300 })`), expands its immediate 1-hop neighborhood (filtered to $\le 12$ relevant lesson nodes), and displays the verbatim text + PDF page badge below the mini-graph.
  2. If the user clicks **"Expand in Full Atlas Mode ↗"**, the application pushes a `LessonReturnBookmark` onto the navigation stack (`{ lessonId, sectionId, scrollOffset, activeMiniGraphNodes }`) and switches to full-screen Atlas Mode centered on `node_id`.
* **Accessibility & Fallback:** Keyboard accessible via `Tab` + `Enter`; if WebGL/Canvas is disabled, renders a structured accessible HTML table of incoming/outgoing constitutional relationships.

### 3.2 Interaction 2: `Concept Journey` (Guided Multi-Hop Lesson Walkthrough)
* **Educational Purpose:** Teaches multi-step causal chains (e.g., how a citizen's fundamental right under `art_21` is interpreted through `judg_maneka` and `judg_puttaswamy` to constrain executive action under `doc_proportionality`).
* **User Action:** Clicking **"▶ Start Guided Concept Journey"** inside a lesson module, then stepping through `Step 1 of N` → `Step N of N` via Next/Previous buttons or arrow keys.
* **Expected System Behavior:**
  * At step $k$, node $v_k$ pulses with an amber ring (`border-color: #fef08a`), edge $e_{k-1 \to k}$ animates a directional particle flow from $v_{k-1}$ to $v_k$, and the synchronized narrative card explains the exact constitutional mechanism of that hop (`edge.type`, `edge.ref`, `edge.explanation`).

### 3.3 Interaction 3: `Progressive Knowledge Map` ("Fog-of-War" Curriculum Mastery Graph)
* **Educational Purpose:** Provides visual metacognitive feedback showing how isolated concepts learned across Levels 0–11 coalesce into a unified mental model of Indian democracy.
* **Data & Visual Mechanics:**
  * Queries `learner_node_mastery` table.
  * **Visual States on the Learner's Personal Map:**
    * `UNEXPLORED` ($0.0$): Node rendered at $25\%$ opacity with dashed slate border (`#334155`).
    * `INTRODUCED` ($0.33$ — Lesson read): Node rendered at $70\%$ opacity with solid category-colored border.
    * `PRACTICED` ($0.67$ — Activity completed): Node rendered at $100\%$ opacity with full category color fill.
    * `MASTERED` ($\ge 0.85$ — Assessment + Spaced Review passed): Node rendered with a warm gold outer halo (`#f59e0b`) and verified checkmark badge.

### 3.4 Interaction 4: `Institutional Relationship Exercises` (Drag-and-Connect Edge Builder)
* **Educational Purpose:** Active constructivist encoding of *how* institutions check, empower, or answer to one another.
* **Interaction Mechanics:**
  * The canvas displays 4–6 institutional/constitutional nodes (e.g., `inst_president`, `inst_pm`, `inst_council_ministers`, `inst_lok_sabha`, `inst_supreme_court`, `art_74`, `art_75`) with **no edges**.
  * The learner is given a prompt: *"Connect the institutions to show (1) who appoints the Prime Minister, (2) whose aid and advice binds the President, and (3) to which House the Council of Ministers is collectively responsible."*
  * The learner drags an arrow from Source Node $u$ to Target Node $v$ and selects the relationship type from a modal pill menu (`APPOINTS`, `ADVISES`, `ACCOUNTABLE_TO`, `CHECKS_AND_BALANCES`, `ESTABLISHES`).
* **Feedback Logic:**
  * If correct: Edge locks in emerald green and reveals the constitutional citation (`Article 75(3)`).
  * If direction is reversed (e.g., drawing `inst_lok_sabha` → `ACCOUNTABLE_TO` → `inst_council_ministers`): Triggers a targeted **Directionality Misconception Alert** (*"Careful! In a parliamentary democracy, the executive is accountable to the lower house of the legislature, not vice versa. Under Article 75(3), the Council of Ministers is collectively responsible to the Lok Sabha."*).

### 3.5 Interaction 5: `Trace the Authority` (Reverse-Chain Constitutional Audit)
* **Educational Purpose:** Trains learners to trace any concrete real-world official action back to its ultimate constitutional and statutory source of authority.
* **Interaction Mechanics:**
  * Presents a real-world administrative action at the bottom of the screen—for example: *"A Tehsildar (`admin_tehsildar`) issues an order mutating agricultural land records and a District Magistrate (`admin_dm_collector`) issues a prohibitory order under Section 163 of the Bharatiya Nagarik Suraksha Sanhita (BNSS)."*
  * The learner must click nodes upward in sequence to complete the **Chain of Authority** back to `const_india`:
    * `admin_dm_collector` → empowered by State Executive & Statutory Criminal/Revenue Codes (`inst_state_govt`) → enacted under Seventh Schedule List II Entry 1 (Public Order) &Entry 18 (Land) / List III Entry 2 (Criminal Procedure) (`sched_7` & `art_246`) → constrained by Fundamental Rights (`art_14`, `art_19`, `art_21`) and High Court Writ Supervision (`art_226`, `inst_high_courts`).

### 3.6 Interaction 6: `Why Are These Connected?` (Edge Prediction & Elaborative Interrogation)
* **Educational Purpose:** Prevents superficial clicking by requiring learners to predict the constitutional rationale of an edge before revealing its explanation.
* **Interaction Mechanics:**
  * Displays two connected nodes on the mini-graph—e.g., `inst_cag` (Comptroller and Auditor-General) and `inst_parl_committees` (Public Accounts Committee)—with a pulsing `[ ? MYSTERY CONNECTION ? ]` edge.
  * The learner selects or types why these two institutions depend on each other, then clicks **Reveal Verified Edge**, which animates the `ADVISES` edge (`Article 151 & PAC Rules`) and compares their reasoning against the canonical explanation.

### 3.7 Interaction 7: `Return to Lesson` (Zero-Loss Context Switching State Machine)
* **State Contract (`Zustand` slice `useLearningBridgeStore`):**
  ```typescript
  interface LessonReturnContext {
    active: boolean;
    lessonId: string;
    lessonTitle: string;
    sectionAnchor: string;
    scrollTop: number;
    originNodeId: string;
    exploredNodesDuringDetour: string[];
  }
  ```
* **UX Behavior:** Whenever a user jumps from a lesson into full-screen Atlas Mode, a floating top-center gold banner remains pinned:
  `📖 Exploring from Lesson 4.1: "President, PM & Council of Ministers" (3 nodes explored) — [↩ Return to Exact Lesson Spot]`
  Clicking the button restores the exact scroll offset and awards `+1 Graph Curiosity Exploration Point` to the learner's session log.

### 3.8 Interaction 8: `Graph-Based Revision` (Memory Reconstruction of Subgraphs)
* **Educational Purpose:** Combines **Dual Coding**, **Active Recall**, and **Spaced Repetition** by testing whether the learner can reconstruct a constitutional subsystem from memory days or weeks after completing a lesson.
* **Interaction Mechanics:**
  * In the Revision Workspace, when an FSRS subgraph card comes due, the learner is shown a partially masked 5-node constellation (e.g., the **Golden Triangle & Privacy Constellation** where `art_21` and `judg_puttaswamy` are visible, but two connected nodes `[ ? Node A ? ]`, `[ ? Node B ? ]` and one doctrine `[ ? Doctrine C ? ]` are masked).
  * The learner fills in the masked nodes (`art_14`, `art_19`, `doc_proportionality`) and grades their recall (`Again`, `Hard`, `Good`, `Easy`), updating the FSRS stability $S$ and difficulty $D$ for all constituent nodes.
