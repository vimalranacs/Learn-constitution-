# ADAPTIVE LEARNING & AI TUTORING ARCHITECTURE (`AI_TUTOR_DESIGN.md`)

**Document ID:** `CA-AIT-006`  
**Purpose:** Specification of a context-aware, graph-grounded, Socratic AI Tutoring system that enhances the prepared curriculum while operating seamlessly with **zero AI API calls** when offline or unconfigured.

---

## 1. Core Architectural Principle: Prepared Curriculum First, Grounded AI Second

In **Constitution Atlas**, prepared scholarly content—authored and verified against the 402-page official 2026 Constitution PDF—is always the primary source of truth. The AI Tutor is **never** used to hallucinate unverified lessons on the fly. Instead, the AI Tutor operates as a **Context-Aware Pedagogical Companion** layered atop:
1. The active lesson's structured sections, primary sources, and misconception library (`learning_lessons`),
2. The canonical 635-node Knowledge Graph (`nodes` and `edges`), and
3. The learner's personal mastery profile (`learner_node_mastery` and recent assessment errors).

Crucially, every AI Tutor feature is designed with a **Dual-Engine Architecture**:
* **Engine 1 (Zero-Cost Deterministic Pedagogical Engine — Always Active):** Uses pre-computed 4-depth explanations, structured 3-tier hints, rule-based misconception pattern matchers, and SQLite FTS5 + BFS graph traversal to answer questions, run Socratic dialogues, and diagnose errors instantaneously in the browser/local backend with **zero API cost or internet dependency**.
* **Engine 2 (Optional Live Gemini 2.5 Flash Graph-RAG Engine):** When the user configures a free-tier Google AI Studio `GEMINI_API_KEY`, the backend augments Engine 1 by passing the exact retrieved lesson section, canonical nodes, verified edges, and learner mastery state into `gemini-2.5-flash` under strict epistemic guardrails.

---

## 2. Four Explanation Depth Profiles

Every node in the graph and every AI Tutor clarification supports four explicit depth modes selectable via the header toggle:

| Depth Level | Target Learner Profile | Vocabulary & Citation Rules | Example Treatment of Article 21 (`art_21`) |
| :--- | :--- | :--- | :--- |
| **`beginner`** | High school student or first-time civic learner (Levels 0–2) | Plain everyday English; zero unexplained Latin maxims; leads with concrete Indian life examples before naming the Article. | Explains how Article 21 protects every person's right to live with dignity, safety, and personal freedom, using everyday examples of fair police procedure, clean environment, and privacy. |
| **`intermediate`** | Undergraduate student, civil services aspirant, or informed citizen (Levels 3–6) | Standard constitutional terminology; cites key Articles, clauses, and major Supreme Court landmarks (*Maneka Gandhi*, *Puttaswamy*). | Explains the text of Article 21 (*"No person shall be deprived of his life or personal liberty except according to procedure established by law"*), the shift from *A.K. Gopalan* (1950) to *Maneka Gandhi* (1978), and the Golden Triangle (`art_14`, `art_19`, `art_21`). |
| **`advanced`** | Advanced law/political science student or policy analyst (Levels 7–9) | Doctrinal precision; distinguishes *ratio decidendi*, constitutional text vs. judicial expansion, and 44th Amendment non-suspendability under Article 359. | Analyzes substantive vs. procedural due process, the four-prong *Puttaswamy* proportionality standard (`doc_proportionality`), horizontal vs. vertical application (*Kaushal Kishor* 2023), and Article 359(1) post-1978 protection. |
| **`research`** | Constitutional scholar, litigator, or judicial clerk (Levels 10–11) | Primary CAD citations (B.N. Rau's discussions with Justice Felix Frankfurter; CAD Vol. VII, 6 & 13 Dec 1948), bench strengths, dissents, and unsettled doctrinal tensions. | Examines CAD debates on dropping *"without due process of law"* in Draft Article 15, Justice Fazl Ali's dissent in *Gopalan* (`AIR 1950 SC 27`), *ADM Jabalpur* (`(1976) 2 SCC 521`) overruled in *Puttaswamy* (`(2017) 10 SCC 1`), and critiques of unenumerated rights under Article 21. |

---

## 3. Misconception Identification & Diagnostic Intervention Library

Novices and even intermediate students harbour predictable, systematic misconceptions about Indian constitutional law and administration. Every lesson in Volumes I–IV defines structured **Misconception Diagnostic Rules** (`misconceptions_json`) that both the assessment engine and the AI Tutor monitor:

```json
{
  "misconception_id": "misc_art74_president_discretion",
  "trigger_pattern": "Learner claims the President can reject any Cabinet advice or refuse assent to a Constitutional Amendment Bill",
  "conflicted_nodes": ["inst_president", "inst_pm", "inst_council_ministers", "art_74", "art_111", "art_368"],
  "diagnostic_category": "FORMAL_VS_REAL_EXECUTIVE_CONFUSION",
  "socratic_counter_question": "Look closely at the text of Article 74(1) after the 42nd and 44th Amendments, and Article 368(2) after the 24th Amendment. If the Council of Ministers reconsider and resend their advice to the President, what does Article 74(1) say the President 'shall' do?",
  "corrective_explanation": {
    "constitutional_text": "Under Article 74(1) (PDF p. 62), the President 'shall, in the exercise of his functions, act in accordance with such advice', and the proviso added by the 44th Amendment (1978) states the President 'shall act in accordance with the advice tendered after such reconsideration.' Furthermore, under Article 368(2) (amended by the 24th Amendment, 1971), for a Constitutional Amendment Bill, the President 'shall give his assent to the Bill'—there is no veto.",
    "constitutional_convention": "Only in rare situational contingencies where no party commands a clear majority in the Lok Sabha (Art. 75(1)) or a Council of Ministers has lost confidence and advises dissolution does the President exercise limited situational discretion."
  }
}
```

---

## 4. Progressive 3-Tier Hinting & Socratic Tutoring State Machine

When a learner gets stuck on a simulation step, active reasoning prompt, or assessment question, clicking **"💡 Ask Tutor for a Hint"** never dumps the final answer on the first click. Instead, it advances through a 3-stage state machine:
* **Stage 1 (`HINT_CONCEPTUAL_CUE`):** Highlights the relevant ontology concept or asks a framing question (*"Think about which House of Parliament holds the power to remove the Council of Ministers under Article 75(3). Why would financial supply bills be tied to that specific House?"*).
* **Stage 2 (`HINT_GRAPH_AND_TEXT_POINTER`):** Automatically focuses the companion mini-graph on the exact target node (e.g., `art_109` and `art_110`) and highlights the operative clause in yellow.
* **Stage 3 (`HINT_WORKED_REASONING`):** Walks through the step-by-step constitutional deduction and explains how to apply it to the current problem.

---

## 5. Prompt Engineering & Epistemic Guardrails for Live Gemini Calls

When `GEMINI_API_KEY` is configured and `POST /api/ai/tutor` is invoked, Codex shall enforce the following system instruction and structured JSON output schema:

```python
TUTOR_SYSTEM_INSTRUCTION = """
You are the Constitution Atlas Scholarly AI Tutor.
HARD CONSTRAINTS:
1. Ground every statement in the provided Lesson Context and Canonical Knowledge Graph Nodes/Edges.
2. NEVER invent case names, citations, Article numbers, or historical quotes.
3. Explicitly separate your explanation into labeled epistemic blocks:
   - [CONSTITUTIONAL TEXT]: Verbatim rules from the Constitution of India (2026 Edition) with Article & PDF page numbers.
   - [STATUTORY / ADMINISTRATIVE PRACTICE]: Relevant Parliamentary Acts, Rules of Business, or District Collectorate practices.
   - [JUDICIAL INTERPRETATION]: Verified Supreme Court holdings and constitutional doctrines.
   - [PHILOSOPHICAL / HISTORICAL CONTEXT]: Constituent Assembly Debates and normative theory (presenting disputed scholarly interpretations neutrally).
4. In 'socratic' mode, end your response with one targeted follow-up question that guides the learner to discover the next link in the constitutional graph.
5. Attach canonical node IDs (e.g., [Article 21](node:art_21)) so the UI renders interactive graph chips.
"""
```
