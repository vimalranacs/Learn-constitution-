# 🇮🇳 CONSTITUTION ATLAS — The Living Map of Indian Democracy

> **"Explore the Architecture of Indian Democracy."**
> An AI-Powered Interactive Knowledge Graph of the Constitution of India (Official 1 May 2026 Edition, 402 pages, updated through the 106th Constitutional Amendment Act, 2023), Indian Government, Administrative System, Landmark Jurisprudence, Constitutional History, and Political Philosophy.

---

## 1. System Architecture & Verification Summary

- **Complete PDF Ingestion Engine (`backend/ingest_constitution.py`)**:
  - Parses all **402 pages** of the official Ministry of Law and Justice (Legislative Department) Constitution of India PDF (`88cca69e868e50b217f855be2fb8bdba.pdf`).
  - **100% TOC-to-Body Alignment**: Extracts **The Preamble** (p. 32), all **25 Parts** (Parts I to XXII including IVA, IXA, IXB, XIVA), all **23 Chapters**, all **470 Articles** (Articles 1 to 395 plus all active and omitted alphanumeric insertions such as `21A`, `31A`–`31D`, `39A`, `51A`, `239AA`, `243`–`243ZT`, `246A`, `279A`, `300A`, `323A`–`323B`, `330A`, `332A`, `334A`, `338A`–`338B`, `370`, `371A`–`371J`) with **0 missing articles**, all **12 Schedules** (pp. 284–381), and **3 Appendices** (pp. 382–402).
- **Formal Constitutional Knowledge Graph (`backend/constitution_atlas.db` & `backend/atlas_data.json`)**:
  - **635 Verified Nodes** across 8 ontology categories: `Constitutional`, `Cluster` (16 primary hubs), `Institutional`, `Administrative`, `Philosophical`, `Judicial`, `Historical`, and `Process`.
  - **1,255 Verified Directional Edges** (`CONTAINS`, `ESTABLISHES`, `EMPOWERS`, `LIMITS`, `PROTECTS`, `INTERPRETS`, `ACCOUNTABLE_TO`, `CHECKS_AND_BALANCES`, `IMPLEMENTED_THROUGH`, `DEFINED_BY`, `RELATED_TO`, `HISTORICALLY_CONNECTED_TO`) with human-readable explanations and exact constitutional citations.
- **Epistemic Rigor & Neutrality**:
  - Every node and AI response explicitly distinguishes between:
    1. **Constitutional Text** (verbatim provisions with PDF page references)
    2. **Statutory Law** (Acts of Parliament such as RPA 1950/1951, RTI Act, BNSS/CrPC)
    3. **Judicial Interpretation** (verified Supreme Court Constitution Bench rulings and doctrines)
    4. **Constitutional Conventions & Administrative Practice** (Allocation of Business Rules, Collectorate hierarchy)
    5. **Philosophical & Historical Analysis** (Constituent Assembly Debates, political theory)

---

## 2. Local Setup Guide on Windows (Zero Paid Services Required)

### Prerequisites
- **Python 3.10+** (Download from [python.org](https://www.python.org/downloads/windows/))
- **Node.js 18+ LTS** (Optional if using the standalone `constitution_atlas.html` app; required for running the Vite dev server)
- **Google Gemini API Key** (Free tier from [Google AI Studio](https://aistudio.google.com/); optional—the platform includes an offline-ready deterministic Graph RAG fallback)

### Step 1: Set Up & Run the Python Backend + PDF Ingestion Pipeline (Windows PowerShell / CMD)

```powershell
# 1. Navigate to the backend folder
cd backend

# 2. Create and activate a Python virtual environment on Windows
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Configure your free Google Gemini API key
copy .env.example .env
# Edit .env in Notepad and paste GEMINI_API_KEY=...

# 5. Run the PDF Ingestion Pipeline (re-generates constitution_atlas.db, atlas_data.json, and extraction_validation_report.json)
python ingest_constitution.py --pdf path\to\88cca69e868e50b217f855be2fb8bdba.pdf

# 6. Run the automated test suite (verifies all 470 articles, 8 journeys, shortest path, and RAG)
python ..\tests\test_constitution_atlas.py

# 7. Start the FastAPI server at http://localhost:8000 (Swagger docs at http://localhost:8000/docs)
uvicorn main:app --reload --port 8000
```

### Step 2: Run the Frontend (Two Options)

1. **Instant Zero-Build Option**: Open `constitution_atlas.html` directly in any browser (Chrome, Edge, Firefox). It embeds the complete 635-node, 1,255-edge SQLite/JSON dataset, Cytoscape.js interactive graph, Full Constitution Reader, 6 Interactive Simulations, "Trace the Power", Historical Timeline, AI Research Assistant, and Learning Workspace.
2. **React + TypeScript + Vite Development Server**:
   ```powershell
   cd frontend
   npm install
   npm run dev
   ```
   Open `http://localhost:5173`.

---

## 3. Free-Tier Cloud Deployment Guide

- **Frontend (Vercel or Cloudflare Pages — Free Tier)**:
  - Push the repository to GitHub and import `frontend/` into Vercel or Cloudflare Pages (`Build command: npm run build`, `Output directory: dist`), or deploy `constitution_atlas.html` as a static site with zero backend latency.
- **Backend API & SQLite+FTS5 Database (Render Free Web Service)**:
  - Create a Web Service on Render pointing to `backend/`.
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
  - Environment Variable: `GEMINI_API_KEY` (from Google AI Studio Free Tier).
