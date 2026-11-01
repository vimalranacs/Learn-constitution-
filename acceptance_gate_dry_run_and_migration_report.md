# ARGON DATA BRIEF & IMPORT CONTRACT — ACCEPTANCE GATE DRY-RUN REPORT (2 NOVEMBER 2026)

**Batch ID:** `argon-2026-11-02-unified-p0-to-p3-import-contract`  
**Schema Version:** `1` (UTF-8 JSON)  
**As-Of Date:** `2026-11-02`  
**Primary Source Audited:** *The Constitution of India* (Ministry of Law and Justice, Legislative Department, Official Edition as on 1st May 2026, 402 PDF pages, `88cca69e868e50b217f855be2fb8bdba.pdf`)  
**Verification Status Policy:** All proposed node patches, edge proposals, and lesson patches carry `"status": "needs_review"`. Zero records are marked `source_checked` prior to independent human/source sign-off.

---

## 1. Acceptance Gate Dry-Run Summary & Counts

| Contract Section | Count in Batch | Validation Gate Result |
| :--- | :--- | :--- |
| **`sources[]` (Primary Source Pinpoints & Verbatim Quotes)** | **36** | **PASS** — Every source includes official URL, publicationDate (`2026-05-01`), PDF page AND printed page pinpoint, verbatim quote, and edition string. |
| **`nodePatches[]` — Priority 0 Article Boundary Repairs (`operation: "update"`)** | **24** | **PASS** — Restores `is_omitted: false` (`legalStatus: "active"`) on 22 active articles (`art_2`, `art_30`, `art_31C`, `art_32`, `art_131`, `art_144`, `art_226`, `art_228`, `art_231`, `art_237`, `art_241`, `art_257`, `art_258A`, `art_268`, `art_271`, `art_277`, `art_290A`, `art_305`, `art_313`, `art_329`, `art_359`, `art_361B`, `art_371A`, `art_378A`) that previously had bracketed omitted sub-articles concatenated onto their titles and text, plus explicit clause-level omission annotations on `art_19` (`19(1)(f)`) and `art_22` (unnotified 44th Amendment s. 3). |
| **`nodePatches[]` — Priority 0 Split Article Additions (`operation: "add"`)** | **23** | **PASS** — Separates 22 whole-omitted articles (`art_2A`, `art_31`, `art_31D`, `art_32A`, `art_131A`, `art_144A`, `art_226A`, `art_228A`, `art_232`, `art_238`, `art_242`, `art_257A`, `art_259`, `art_268A`, `art_272`, `art_278`, `art_291`, `art_306`, `art_314`, `art_329A`, `art_359A`, `art_362`, `art_379_to_391`) and 1 active article (`art_371B` — Assam, PDF pp. 267–268, printed pp. 236–237) into standalone records. |
| **`nodePatches[]` — Priority 2 Amendment & Judgment Audits (`operation: "update"`)** | **5** | **PASS** — Distinguishes assent dates, multi-date staggered commencement dates, unnotified sections, and judicial invalidations for `amend_42`, `amend_44`, `amend_106`, `judg_kesavananda`, and `judg_minerva`. |
| **`edgeProposals[]` — Priority 1 Isolated-Entity Connections ($\le 30$ cap)** | **24 / 30** | **PASS** — 24 source-backed directed edges connecting the isolated entities (`admin_cabinet_sec`, `amend_1`, `amend_42`, `amend_44`, `amend_73_74`, `amend_86`, `amend_101`, `amend_106`, `doc_pith_substance`, `hist_adoption_1949`, `inst_ag`, `inst_vice_president`, `phil_federalism`, `phil_rule_of_law`, `phil_secularism`, `phil_sep_powers`, `proc_emergency`) with `status: "needs_review"`, `relationshipClass`, and `temporalScope`. |
| **`lessonPatches[]` — Priority 3 Primary-Source Lesson Audits** | **2** | **PASS** — Audited `les_00_01_why_rules` and `les_03_01_structure_territory_citizenship` with separate `learningObjectives`, `prerequisites`, `proposedText`, `beginnerExplanation`, `labelledHypothetical`, `misconceptionFeedback`, `assessment` + rubric, and runnable `activity` decision trees with acceptance fixtures. |
| **`unresolved[]` — Quarantined Records Requiring External Primary Sources** | **9** | **QUARANTINED** — Holds `admin_regulatory_bodies`, `amend_73_74` split migration, `judg_golaknath`, `judg_gopalan`, `judg_navtej`, `judg_vishaka`, `art_22` post-May-2026 Gazette check, `art_124A` status taxonomy, and CAD edition page alignment until external primary sources are imported. |

---

## 2. Priority 0 Diff Highlights: Root Cause & Exact Boundary Repairs

### 2.1 Root Cause Identified in Primary-Source Audit
In the Table of Contents of the official 1 May 2026 PDF (PDF pp. 4–30, printed pp. i–xxvii), repealed/omitted articles are printed in square brackets on the line immediately below the preceding active article (for example, `[2A. Sikkim to be associated with the Union.—Omitted.]` immediately below `2. Admission or establishment of new States.`). Because the initial TOC regex did not match leading square brackets, the parser concatenated 22 bracketed omitted articles onto the titles and `full_text` of the preceding active articles—and then triggered `is_omitted = True` on those 22 active articles! Additionally, on TOC PDF p. 28, `371B .` had a space before the period, causing active Article 371B (Assam) to merge into the tail of `art_371A` (Nagaland).

### 2.2 Sample Human-Readable Diff (`art_2` vs. `art_2A`, PDF p. 33 / Printed p. 2)
```diff
 Node ID: art_2
-title: "Article 2 — Admission or establishment of new States. [2A. Sikkim to be associated with the Union.—Omitted.]"
+title: "Article 2 — Admission or establishment of new States"
-is_omitted: true
+is_omitted: false
+legalStatus: "active"
+pdfPageStart: 33, pdfPageEnd: 33, printedPageStart: 2, printedPageEnd: 2
 full_text:
   Article 2. Admission or establishment of new States.—Parliament may
   by law admit into the Union, or establish, new States on such terms and
   conditions as it thinks fit.
-  3[2A. [Sikkim to be associated with the Union.].—Omitted by the
-  Constitution (Thirty-sixth Amendment) Act, 1975, s. 5 (w.e.f. 26-4-1975).]

+Added Node ID: art_2A (operation: "add", status: "needs_review")
+title: "Article 2A — [Sikkim to be associated with the Union.—Omitted.]"
+is_omitted: true
+legalStatus: "omitted_whole_article"
+pdfPageStart: 33, pdfPageEnd: 33, printedPageStart: 2, printedPageEnd: 2
+amendmentStatus: "Inserted by 35th Amendment Act, 1974, s. 2 (w.e.f. 01-03-1975); Omitted by 36th Amendment Act, 1975, s. 5 (w.e.f. 26-04-1975)."
```

### 2.3 Distinguishing Whole-Article Omission vs. Clause-Level Omission vs. Uncommenced Amendment
1. **Whole-Article Omission (`legalStatus: "omitted_whole_article"`):** `art_2A`, `art_31`, `art_31D`, `art_32A`, `art_131A`, `art_144A`, `art_226A`, `art_228A`, `art_238`, `art_242`, `art_257A`, `art_259`, `art_268A`, `art_272`, `art_278`, `art_291`, `art_306`, `art_314`, `art_329A`, `art_359A`, `art_362`, `art_379_to_391`.
2. **Active Article with Omitted Sub-Clause (`legalStatus: "active_with_omitted_clauses"`):** `art_19` (PDF pp. 40–41, printed pp. 9–10), where sub-clause `(1)(f)` (`2[(f)* * * * *]`) was omitted by Section 2 of the 44th Amendment Act, 1978 (w.e.f. 20-06-1979), while clauses `(1)(a)–(e)`, `(1)(g)`, and `(2)–(6)` remain active.
3. **Active Article with Unnotified/Uncommenced Omission (`legalStatus: "active_with_uncommenced_amendment_annotation"`):** `art_22` (PDF p. 44, printed p. 13), where the starred footnote records: `* Sub-clause (a) shall stand omitted by the Constitution (Forty-fourth Amendment) Act, 1978, s. 3(b)(i) (date to be notified).`
4. **Provisions Struck Down by Judicial Order (`legalStatus: "struck_down_unconstitutional"`):** `art_31C` (expanded phrase *"all or any of the principles laid down in Part IV"* struck down in *Minerva Mills*, PDF p. 49 fn. 4; declaration finality clause struck down in *Kesavananda Bharati*, PDF p. 49 fn. 6), `art_124A`–`art_124C` and `art_231(2)(a)` omission (99th Amendment struck down in *SCARA / NJAC Case*, PDF p. 89 fn. 1 & p. 139 fn. 1), and `art_368(4)–(5)` (Section 55 of 42nd Amendment struck down in *Minerva Mills*, PDF p. 257 fn. 3).

---

## 3. Priority 1 & Priority 2 Policies: Edge Directionality & Composite Entity Migration Maps

### 3.1 Canonical Direction Policy for `INTERPRETS` vs. `INTERPRETED_BY`
* **Audit Finding:** The baseline graph recorded 3 `INTERPRETS` edges (`Judicial/Doctrine -> Constitutional Provision`) and 12 `INTERPRETED_BY` edges (`Constitutional Provision -> Judicial Node`).
* **Display & Storage Policy:** To prevent duplicate inverse edges, canonical storage standardizes on a **single directed edge per interpretive relationship**:
  * **Canonical Stored Direction:** `Judicial / Doctrinal Node` —[`INTERPRETS`]→ `Constitutional / Statutory Provision` (e.g., `doc_pith_substance -> INTERPRETS -> art_246`).
  * **UI Inverse Rendering Rule:** When inspecting the target Constitutional Provision (`art_246`), the UI reader automatically renders incoming `INTERPRETS` edges under the heading **"Interpreted By"** without storing a second `INTERPRETED_BY` row in the database.

### 3.2 Explicit Migration Maps for Composite Entities (No Automatic ID Renaming)
1. **`amend_73_74` Split Migration Map (Quarantined Pending Approval):**
   * Retain `amend_73_74` as a deprecated alias during transition, and introduce:
     * `amend_73`: *The Constitution (Seventy-third Amendment) Act, 1992* (Assented: `1993-04-20`, Commenced: `1993-04-24`, Target: `part_IX`, `art_243` to `art_243O`, `sched_11`, PDF p. 151 fn. 1).
     * `amend_74`: *The Constitution (Seventy-fourth Amendment) Act, 1992* (Assented: `1993-04-20`, Commenced: `1993-06-01`, Target: `part_IXA`, `art_243P` to `art_243ZG`, `sched_12`, PDF p. 158 fn. 1).
2. **`admin_regulatory_bodies` Split Migration Map (Quarantined Pending Statutory Sources):**
   * Retain `admin_regulatory_bodies` as a category container and migrate specific statutory claims to dedicated statutory authority nodes once primary India Code Act texts are imported: `admin_cic` (*Central Information Commission — RTI Act, 2005, s. 12*), `admin_lokpal` (*Lokpal — Lokpal and Lokayuktas Act, 2013, s. 3*), `admin_nhrc` (*NHRC — Protection of Human Rights Act, 1993, s. 3*), `admin_rbi` (*RBI Act, 1934*), `admin_sebi` (*SEBI Act, 1992*), and `admin_trai` (*TRAI Act, 1997*).
