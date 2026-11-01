# INTERACTIVE LEARNING ACTIVITIES & ASSESSMENT SYSTEM SPECIFICATION (`ACTIVITY_AND_ASSESSMENT_SYSTEM.md`)

**Document ID:** `CA-AAS-005`  
**Purpose:** Complete specification of 15 browser-feasible interactive learning activity archetypes, multi-tier assessment formats, misconception diagnostics, and the FSRS-4.5 spaced repetition & mastery engine.

---

## 1. Design Philosophy: Moving Beyond Passive Reading & Multiple-Choice

Conventional e-learning platforms rely on passive video/text consumption followed by shallow 4-option multiple-choice questions that test surface recognition rather than structural reasoning. To train learners to think like constitutional scholars, parliamentarians, judges, and administrators, **Constitution Atlas** implements **15 Interactive Activity Archetypes**. Every archetype runs 100% client-side in standard browser JavaScript/TypeScript (React + Zustand + Cytoscape.js) backed by static JSON configurations stored in `learning_lessons.interactive_activities_json`—requiring **zero expensive cloud compute or paid third-party APIs**.

---

## 2. Engineering & Pedagogical Specifications for the 15 Interactive Archetypes

### Archetype 1: Interactive Constitutional Diagrams (`ARCH_INTERACTIVE_DIAGRAM`)
* **Educational Purpose:** Dual-coding visualization of complex structural hierarchies (e.g., *The Three Funds of India: Consolidated Fund Art. 266(1), Public Account Art. 266(2), Contingency Fund Art. 267*; or *The Integrated Judicial Hierarchy & Appellate Paths Arts. 132–136*).
* **Interaction Mechanics:** SVG/Canvas layered diagram with clickable hotspots, toggleable flow arrows (e.g., toggle *"Requires Parliamentary Appropriation Bill"* vs. *"Executive Disbursement"*), and synchronized side-panel textual breakdown.
* **Data Contract:** `{ diagram_id, layers: [{ id, label, nodes, flow_paths, constitutional_refs }], quiz_hotspots: [{ prompt, target_layer_id, feedback }] }`.
* **Success Condition:** Learner inspects all layers and correctly identifies the target constitutional pathway on 3 hotspot challenges.

### Archetype 2: Build-Your-Own-Government Constitutional Sandbox (`ARCH_GOVT_SANDBOX`)
* **Educational Purpose:** Used in Levels 1 and 2 to let learners discover *why* institutional checks and balances are necessary by experiencing what breaks when they are omitted.
* **Interaction Mechanics:** Learners configure 5 constitutional design sliders/toggles for a hypothetical diverse republic:
  1. *Executive Model:* Westminster Parliamentary (Art. 75(3)) vs. Fixed-Term Presidential vs. Unchecked Monarch.
  2. *Territorial Structure:* Unitary vs. Cooperative Federalism with 3 Lists (Art. 246) vs. Loose Confederation.
  3. *Judicial Review:* Strong Writ Review (Arts. 13, 32, 226) vs. Advisory Only vs. None.
  4. *Franchise:* Universal Adult Suffrage (Art. 326) vs. Property/Tax Qualification.
  5. *Minority & Social Safeguards:* Enforceable Part III Rights + Affirmative Action (Arts. 15–17, 29–30) vs. Majoritarian Plebiscite.
* **Feedback Logic:** The simulator runs 4 stress-test historical shocks (*Linguistic State Demand*, *Parliamentary Majority Passes Censorship Law*, *Regional Famine & Fiscal Imbalance*, *Executive Refuses to Convene Legislature*) and computes a **Constitutional Stability, Liberty & Cohesion Report** comparing the learner's design with the actual choices made by the Indian Constituent Assembly (1946–1949).

### Archetype 3: Simulated Parliamentary Lawmaking (`ARCH_PARLIAMENT_LAWMAKING`)
* **Educational Purpose:** Teaches procedural discrimination across **Ordinary Bills (Art. 107)**, **Money Bills (Arts. 109–110)**, **Financial Bills Cat. I & II (Art. 117)**, and **Constitutional Amendment Bills (Art. 368)**.
* **Interaction Mechanics:** Learner is handed a drafted legislative bill (e.g., *The Goods and Services Tax Constitutional Amendment Bill* or *The Annual Finance Bill*). At each stage, they must choose:
  1. Which House can introduce it? (`Lok Sabha Only` vs. `Either House`)
  2. Is prior recommendation of the President required? (`Yes, Art. 117(1)` vs. `No`)
  3. What majority is required in Lok Sabha and Rajya Sabha? (`Simple Majority` vs. `Art. 368 Special Majority`)
  4. What happens when Rajya Sabha proposes amendments or delays for 6 months? (`14-Day Override under Art. 109` vs. `Joint Sitting under Art. 108` vs. `Bill Fails — No Joint Sitting under Art. 368`)
  5. What options does the President have under Article 111 / 368(2)?

### Archetype 4: Government Formation & Hung-House Simulator (`ARCH_GOVT_FORMATION`)
* **Educational Purpose:** Teaches Articles 74, 75, 85, 164, the Tenth Schedule, and *S.R. Bommai* / *Rameshwar Prasad* conventions on government formation after an election.
* **Interaction Mechanics:** Displays a 543-seat Lok Sabha (or 243-seat Vidhan Sabha) seat tally where no single party has crossed the 272 majority mark. The learner acts as Constitutional Advisor to the President/Governor and must evaluate competing claims (Pre-Poll Alliance vs. Single Largest Party vs. Post-Poll Coalition), set a Floor Test deadline, and adjudicate a whip violation under the Tenth Schedule during the Confidence Vote.

### Archetype 5: Constitutional Rights Case Studies (`ARCH_RIGHTS_CASE_STUDY`)
* **Educational Purpose:** Teaches step-by-step application of Part III Fundamental Rights (`art_12` to `art_35`) to concrete citizen grievances.
* **Interaction Mechanics:** Structured 4-stage interactive docket:
  * *Stage 1 (State Action Check under Art. 12):* Is the respondent "the State" under Article 12 (*Ajay Hasia* / *Pradeep Kumar Biswas* tests)?
  * *Stage 2 (Right Identification):* Which specific Fundamental Right(s) are infringed?
  * *Stage 3 (Restriction & Proportionality Audit):* Is there a valid law, a legitimate aim under Art. 19(2)–(6) or Art. 21, and is the restriction proportionate (*Puttaswamy* 4-prong test)?
  * *Stage 4 (Writ Remedy Selection):* Which writ (`Habeas Corpus`, `Mandamus`, `Certiorari`, `Prohibition`, `Quo Warranto`) under Article 32 or 226 provides the appropriate relief?

### Archetype 6: Judicial Reasoning Bench Simulator (`ARCH_JUDICIAL_BENCH`)
* **Educational Purpose:** Places the learner on a 5-Judge Constitution Bench to weigh competing petitioner and respondent arguments and author a structured holding.
* **Interaction Mechanics:** Presents authentic oral arguments from landmark cases (*Kesavananda Bharati*, *Maneka Gandhi*, *Minerva Mills*, *Indra Sawhney*, *S.R. Bommai*, *Navtej Singh Johar*). The learner classifies each argument by interpretive method (*Textual*, *Originalist/CAD*, *Structural*, *Purposive*), selects the controlling constitutional doctrine, and sees how their reasoning aligns with the historic Supreme Court judgment.

### Archetype 7: Centre–State Federal Conflict Simulator (`ARCH_FEDERAL_CONFLICT`)
* **Educational Purpose:** Teaches Seventh Schedule legislative competence (`sched_7`, `art_246`), Doctrine of Pith and Substance (`doc_pith_substance`), Concurrent List Repugnancy (`art_254`), and Presidential Assent (`art_200`, `art_201`, `art_254(2)`).
* **Interaction Mechanics:** Learner resolves 4 federal legislative clashes (e.g., a State passes an agricultural marketing or university regulation bill that overlaps with a central statute on a Concurrent List entry).

### Archetype 8: Elections, Delimitation & Representation Lab (`ARCH_ELECTORAL_LAB`)
* **Educational Purpose:** Teaches First-Past-The-Post (Lok Sabha Art. 81) vs. Proportional Representation by Single Transferable Vote (Rajya Sabha Art. 80(4) & Presidential Election Art. 55), Delimitation freeze (Art. 82 proviso), SC/ST reservations (Arts. 330–332), and 106th Amendment women's reservation (`art_330A`, `art_332A`).
* **Interaction Mechanics:** Interactive calculator and ballot-transfer simulator where learners compute the value of an MLA/MP vote under Article 55(2) and simulate PR-STV quota transfers.

### Archetype 9: District Collectorate Administrative Crisis Scenarios (`ARCH_ADMIN_SCENARIO`)
* **Educational Purpose:** Teaches how constitutional and statutory authority actually operates on the ground in an Indian district (`Level 8`).
* **Interaction Mechanics:** The learner steps into the role of a **District Magistrate / Collector (`admin_dm_collector`)** facing a 48-hour district crisis (e.g., severe flood + communal tension + land acquisition protest + election model code of conduct in force). At each hour, the learner must:
  1. Distinguish which hat they are wearing (*District Magistrate* under BNSS/CrPC vs. *District Collector* under Land Revenue Act vs. *Chairman of DDMA* under Disaster Management Act 2005 vs. *District Election Officer* under ECI `inst_eci`),
  2. Delegate lawful tasks to the **SDM (`admin_sdm`)**, **Tehsildar (`admin_tehsildar`)**, **SP**, and **BDO**, and
  3. Ensure every order complies with Articles 14, 19, 21, and 22 so it is not quashed by the High Court under Article 226.

### Archetype 10: Institutional Accountability & Audit Challenge (`ARCH_ACCOUNTABILITY_AUDIT`)
* **Educational Purpose:** Traces financial and executive accountability across Union Ministries (`admin_ministries`), the CAG (`inst_cag`, Art. 148–151), the Public Accounts Committee (`inst_parl_committees`), Question Hour, and the RTI Act.
* **Interaction Mechanics:** Learner investigates an unauthorized diversion of funds from the Consolidated Fund (`art_266`) and selects the exact sequence of constitutional and parliamentary oversight tools to expose and remedy it.

### Archetype 11: Article 368 Constitutional Amendment & Basic Structure Simulator (`ARCH_AMENDMENT_SIM`)
* **Educational Purpose:** Tests mastery of the 3 amendment tracks (Simple Majority outside Art. 368, Special Majority under Art. 368(2), and Special Majority + $\ge 50\%$ State Ratification under Art. 368(2) Proviso) plus Basic Structure judicial review (`doc_basic_structure`).

### Archetype 12: Comparative Institutional Matrix Builder (`ARCH_COMPARATIVE_MATRIX`)
* **Educational Purpose:** Active discriminative comparison (e.g., `Art. 32 vs. Art. 226`, `Lok Sabha Speaker vs. Rajya Sabha Chairman`, `Governor vs. President`, `Constitutional Body (ECI/CAG) vs. Statutory Body (NHRC/CIC) vs. Executive Body (NITI Aayog)`).

### Archetype 13: Socratic Constitutional Dialogue (`ARCH_SOCRATIC_DIALOGUE`)
* **Educational Purpose:** 4-move branching Socratic conversation testing boundary conditions and value tensions (works both offline via pre-authored branching trees and online via Gemini 2.5 Flash).

### Archetype 14: 1946–1949 Constituent Assembly Historical Decision Simulator (`ARCH_CAD_SIMULATOR`)
* **Educational Purpose:** Immerses learners in the actual debates of the Constituent Assembly (`hist_const_assembly`) on language policy (Munshi-Ayyangar formula), federal emergency powers, due process vs. procedure established by law (B.N. Rau & Alladi Krishnaswami Ayyar vs. K.M. Munshi), and separate vs. joint electorates with reservations (Dr. B.R. Ambedkar & Sardar Patel).

### Archetype 15: Concept Graph Reconstruction (`ARCH_GRAPH_RECONSTRUCTION`)
* **Educational Purpose:** Active visual recall where learners rebuild a lesson's canonical subgraph from memory by placing missing nodes and selecting directional edge verbs.

---

## 3. FSRS-4.5 Spaced Repetition & Mastery Calculation Engine

Codex shall implement the following deterministic TypeScript/Python FSRS-4.5 scheduler for `learner_review_schedule`:

1. **Retrievability after $t$ elapsed days:**
   $$R(t, S) = \left(1 + \frac{19}{81} \cdot \frac{t}{S}\right)^{-0.5}$$
2. **Target Review Threshold:** Cards are scheduled due when $R(t, S) = 0.90$ (i.e., $t_{\text{next}} = S$ days).
3. **Grade Updates ($G \in \{1\text{ (Again)}, 2\text{ (Hard)}, 3\text{ (Good)}, 4\text{ (Easy)}\}$):**
   * On $G = 1$ (Lapse): $S_{\text{new}} = \max(0.5, S \cdot 0.25)$, $D_{\text{new}} = \min(10.0, D + 0.8)$, and the linked misconception card is immediately queued.
   * On $G \in \{2, 3, 4\}$ (Recall Success): $S_{\text{new}} = S \cdot \left(1 + e^{1.1} \cdot (11 - D) \cdot S^{-0.15} \cdot (e^{0.8(1 - R)} - 1) \cdot \gamma_G\right)$, where $\gamma_2 = 0.6, \gamma_3 = 1.0, \gamma_4 = 1.4$.
4. **Node Mastery Score Aggregation:**
   $$\text{Mastery}(v) = 0.30 \cdot \mathbb{I}(\text{LessonRead}) + 0.30 \cdot \text{SimScore}(v) + 0.25 \cdot \text{AssessmentScore}(v) + 0.15 \cdot \overline{R}_{\text{FSRS}}(v)$$
   When $\text{Mastery}(v) \ge 0.85$, node $v$ unlocks the `MASTERED` gold halo in both Learning Mode and Atlas Mode.
