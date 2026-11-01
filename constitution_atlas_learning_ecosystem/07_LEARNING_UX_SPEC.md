# LEARNING MODE UI/UX & EDITORIAL DESIGN SPECIFICATION (`LEARNING_UX_SPEC.md`)

**Document ID:** `CA-LUX-007`  
**Purpose:** Complete interface, layout, typography, interaction, and responsive specification for **Constitution Atlas — Learning Mode**, preserving the restrained scholarly editorial identity of the platform.

---

## 1. Visual & Editorial Design Language ("Digital Constitutional University")

Learning Mode rejects the noisy, infantile tropes of mass-market gamified apps (no cartoon mascots, no spinning loot boxes, no neon confetti). Instead, it embodies the calm, authoritative aesthetic of a **Digital Constitutional University combined with an Interactive Research Atlas**:

* **Color Palette (Dark & Light Scholarly Themes):**
  * **Dark Scholarly Theme (Default):** Deep Midnight Parchment (`#070b14`), Slate Reading Surface (`#0f172a`), Elevated Card Surface (`#1e293b`), Warm Sandstone/Gold Primary Accent (`#f59e0b`), Ashoka Cobalt (`#3b82f6`), Emerald Verification (`#10b981`), Judicial Rose (`#f43f5e`).
  * **Light Editorial Theme (High-Comfort Long-Form Reading):** Warm Ivory Paper (`#faf8f5`), Alabaster Panel (`#ffffff`), Crisp Slate Ink (`#0f172a`), Deep Bronze Gold Accent (`#b45309`), Oxford Navy (`#1e3a8a`).
* **Typography & Scannable Measure:**
  * **Headings & Constitutional Titles:** `'Cormorant Garamond', Georgia, serif` (`600`/`700` weight, generous tracking).
  * **Long-Form Lesson Body:** `'Inter', system-ui, sans-serif` (`16px` / `1.0rem`, line-height `1.75`, strict optimal reading measure of `65ch–72ch` per column so the eye never fatigues across 3,000-word lessons).
  * **Constitutional Citations, Article Codes & Epistemic Badges:** `'JetBrains Mono', monospace` (`12px`, uppercase pill badges).

---

## 2. Core Screen Layouts & Component Responsibilities

### 2.1 Screen 1: Learning Dashboard & Curriculum Roadmap (`LearningDashboard.tsx`)
* **Layout Grid (12 Columns, Max-Width `1680px`):**
  * **Top Banner (12 cols):** Displays current Level (`Level 4: Parliament and the Union Government`), active Lesson resume card (*"Resume Lesson 4.1 — Section 3: Collective Responsibility under Art. 75(3)"*), overall Knowledge Graph Mastery coverage (`142 / 635 Nodes Mastered • 22.4%`), and today's due **FSRS Spaced-Review Queue** (`14 cards due • ~4 mins`).
  * **Left Main Area (8 cols) — The 12-Level Spiral Curriculum Roadmap:** A vertical architectural timeline displaying `Level 0` through `Level 11`. Each Level card expands to reveal its 3 Modules, individual Lessons, estimated reading/simulation time, target Bloom levels, and canonical node pills.
  * **Right Sidebar (4 cols) — Personal Concept Map Preview & Revision Pulse:** Displays the learner's live **Progressive Knowledge Map** (showing illuminated vs. unexplored clusters) and a breakdown of mastery by constitutional domain (*Fundamental Rights*, *Federalism*, *Parliament*, *Judiciary*, *Public Administration*).

### 2.2 Screen 2: Split-Pane Lesson Reader & Synchronized Companion Graph (`LessonWorkspace.tsx`)
This is the primary workspace where learners spend $80\%$ of their time.
* **Desktop 3-Zone Layout (`12-Column Grid`):**
  1. **Left Outline & Progress Rail (2 cols, Collapsible):**
     * Displays the 17 standardized sections of the current lesson with scroll-spy progress checkmarks.
     * Shows prerequisite nodes (with 1-click review popovers) and the lesson's Mastery Checklist (`[✓] Read Sections`, `[✓] Complete Simulation`, `[ ] Pass 4 Knowledge Checks`, `[ ] Complete Graph Reconstruction`).
  2. **Center Scholarly Reader Pane (6 cols, Optimal `68ch` Reading Column):**
     * **Section 1–3 Header:** Level/Module breadcrumb, Lesson Title, Learning Outcomes box, Prerequisite Node chips, and the **Compelling Opening Real-World Problem** card.
     * **Section 4–8 Teachable Narrative:** Structured into digestible 300–450 word subsections. Every block carries its **Epistemic Layer Badge** (`[CONSTITUTIONAL TEXT • Art. 75(3) • PDF p. 62]`, `[STATUTORY LAW • RPA 1951]`, `[JUDICIAL HOLDING • S.R. Bommai 1994]`, `[ADMIN PRACTICE • Allocation of Business Rules]`, or `[TEACHING ANALOGY]`).
     * **Inline Interactive Node Chips:** Clicking any `[📜 Article 21](node:art_21)` or `[🏛️ District Collector](node:admin_dm_collector)` chip updates the Right Companion Pane immediately.
     * **Inline Micro-Retrieval & Elaborative Interrogation Cards:** Embedded directly between major sections.
     * **Section 10 Misconception Diagnostic Cards:** High-contrast amber/rose comparison cards (*"Common Misconception vs. Constitutional Reality"*).
     * **Section 11–15 Interactive Simulation, Active Reasoning, Knowledge Checks & Graph Reconstruction:** Embedded interactive widgets right inside the lesson flow.
  3. **Right Companion Graph & Socratic Tutor Pane (4 cols, Sticky Viewport):**
     * **Top Half (`340px` height) — Synchronized Lesson Subgraph (`Cytoscape.js`):** Automatically filters the 635-node graph to the 6–14 canonical nodes and edges taught in the active lesson. As the user scrolls from Section 4.1 to Section 4.2, the mini-graph automatically highlights the corresponding nodes (`Scroll-Triggered Graph Choreography`). Includes a **"⤢ Open in Full Atlas Mode"** button that saves the `LessonReturnContext`.
     * **Bottom Half (`calc(100vh - 420px)`) — Tabbed Inspector / Socratic AI Tutor / Personal Notes:**
       * *Tab A (`Node Text`):* Verbatim constitutional text + 4-depth switcher for the currently clicked node chip.
       * *Tab B (`Socratic Tutor`):* Context-aware AI Tutor pre-loaded with the current lesson's context and 3-tier progressive hints.
       * *Tab C (`My Notes`):* Markdown-enabled study notes anchored to the current lesson and node, automatically synced to the Personal Study Dossier.

### 2.3 Screen 3: Interactive Simulation & Case Lab Viewport (`SimulationLabModal.tsx`)
* Can be used inline within the center column or expanded to a full-screen 2-column **Case & Institutional Simulation Studio** (Left: Constitutional Rules, Dockets & Decision Controls; Right: Live Institutional Consequence Graph & Judicial/Parliamentary Feedback Log).

### 2.4 Screen 4: Spaced Revision & Graph Reconstruction Studio (`RevisionWorkspace.tsx`)
* Presents due FSRS cards in an interleaved sequence mixing:
  1. **Textual & Doctrinal Recall Cards** (with confidence calibration buttons),
  2. **Misconception Trap Cards** (spot the constitutional flaw in a statement), and
  3. **Visual Subgraph Reconstruction Cards** (fill in the missing node or relationship verb on the mini-graph).

---

## 3. Responsive Breakpoints & Mobile Learning Experience

* **Desktop (`>= 1280px`):** Full 3-zone layout (Outline Rail + Scholarly Reader + Sticky Companion Graph/Tutor).
* **Tablet (`768px – 1279px`):** 2-zone layout (Collapsible Outline Drawer + Scholarly Reader + Slide-Over Graph/Tutor Drawer triggered by tapping any node chip or the floating `🌌 Mini-Graph` FAB).
* **Mobile (`< 768px`):** Single-column distraction-free reader (`16px` font, `1.7` line height, touch-friendly `44px × 44px` minimum tap targets) with a persistent bottom sheet (`Peek` state showing the active node title and relationship; `Expanded` state revealing the interactive touch-zoomable mini-graph and Socratic Tutor).
