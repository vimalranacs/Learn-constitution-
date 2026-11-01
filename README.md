# 📜 Constitution Atlas (भारत का संविधान एटलस)
> **A field guide to Indian democracy, constitutional architecture, and civic institutions.**

Constitution Atlas is an interactive, full-stack educational platform and knowledge graph designed to help students, legal researchers, and citizens explore, trace, and understand the Constitution of India (2026 Edition) and the structural mechanisms of Indian democracy.

[![Live Demo](https://img.shields.io/badge/Demo-Live%20Website-teal?style=for-the-badge)](https://constitutionatlas.blondebarge1.chatgpt.site)
[![License](https://img.shields.io/badge/License-Proprietary%20%2F%20Educational-blue?style=for-the-badge)](#license)
[![Next.js](https://img.shields.io/badge/Next.js-16-black?style=for-the-badge&logo=next.js)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19-blue?style=for-the-badge&logo=react)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6?style=for-the-badge&logo=typescript)](https://www.typescriptlang.org/)

---

## 🏛️ Key Features

### 1. 🌌 Interactive Constitutional Knowledge Graph (`/explore`)
- **635 canonical constitutional entities** and **1,258 recorded relationships (3 source-checked; remaining relationships await review)**.
- **Dynamic Physics-Based Canvas:** Powered by D3.js and GSAP with smooth collision relaxation, drag/zoom/pan, and interactive minimap.
- **8 Visual Themes:** Light, dark, and specialized reading palettes.
- **Progressive Node Discovery:** Expand related nodes in place, explore nearby institutional cards, and inspect legal authorities and constitutional limits.
- **Guided Journeys:** Curated exploration paths through key constitutional structures (The Executive, Parliament, Judiciary, Fundamental Rights).

### 2. 📚 Comprehensive Curriculum & Learning Ecosystem (`/courses`, `/learn`)
- **12 Curated Levels (Levels 00–11):** From foundational concepts of society, law, and sovereignty up to advanced constitutional crisis synthesis and reasoning.
- **20 Deep-Dive Lessons:** Featuring real-world dilemmas (e.g., the Johad village aquifer crisis, executive power vs. arbitrary fiat, parliamentary collective responsibility).
- **Clean Educational Prose:** Fully cleaned of internal metadata, prompting tags, and agent instructions. Educational text is strictly preserved alongside verbatim articles and case law citations (*Maneka Gandhi*, *Kesavananda Bharati*, *Indra Sawhney*, *Minerva Mills*).
- **Direct Graph Integration:** Subtle, non-intrusive links connect every lesson directly to the interactive atlas graph.

### 3. 🔍 Trace Connections (`/paths`)
- Discover how any two constitutional articles, bodies, or offices are interconnected across the knowledge graph.
- Supports **directed** (arrow-following) and **bidirectional** traversals.
- **Evidence Filtering:** Filter by source-checked edges only or broaden the scope to include recorded historical associations.
- Step-by-step path explanation showing connection type, authority relationship, and source citation.

### 4. ⚖️ Constitutional Compare Engine (`/compare`)
- Side-by-side comparative analysis of constitutional offices and institutions (e.g., *The President* vs. *The Prime Minister*, *Lok Sabha* vs. *Rajya Sabha*, *Supreme Court* vs. *High Courts*).
- Compares claimed constitutional basis, scope of authority, constitutional limits, and review status.

### 5. 📖 Constitution Reader & Library (`/reader`, `/library`)
- Direct access to primary constitutional texts, articles, schedules, and landmark judicial holdings.
- Integrated search across articles, institutions, case laws, and legal doctrines.

### 6. 🧪 Civic Lab (`/civic`)
- Real-world simulation and application of constitutional rules to contemporary public dilemmas (e.g., passing an ordinary Bill vs. money Bill, citizen grievances, local governance under Panchayati Raj).

### 7. 🔒 Private Device Workspace (`/workspace`)
- Save personal study notes, bookmarks, lesson progress, and custom graph views.
- **Privacy by Design:** Stored server-side in a workspace identified by a secure HTTP-only device cookie without requiring complex third-party account registration.
- **Spaced Repetition:** Simple spaced review scheduling for key constitutional concepts.

### 8. 🤖 Contextual AI Constitutional Tutor
- Integrated AI tutor powered by Google Gemini (`gemini-3.1-flash-lite`).
- Strict grounding in constitutional text, primary sources, and active lesson context with quotation verification.

---

## 🏗️ Repository Architecture

```text
├── atlas-web/                              # Canonical web application (Next.js 16 + Cloudflare Workers / Sites)
│   ├── app/                                # Next.js App Router (pages & API routes)
│   │   ├── api/                            # Backend API (knowledge, entities, personal, ai, visitor)
│   │   ├── atlas/                          # Entity inspection views
│   │   ├── compare/                        # Side-by-side entity compare
│   │   ├── courses/                        # Full curriculum ecosystem
│   │   ├── explore/                        # Immersive knowledge graph canvas
│   │   ├── learn/                          # Interactive lesson reader
│   │   ├── paths/                          # Shortest path connection tracer
│   │   └── components/                     # Reusable UI & graph components
│   ├── content/                            # Core knowledge base & curriculum
│   │   ├── ecosystem.json                  # Cleaned curriculum (20 lessons, 300+ sections)
│   │   └── knowledge.json                  # Canonical knowledge graph (635 nodes, 1258 edges)
│   └── lib/                                # Core utilities (graph traversal, HTTP, runtime)
│
├── artifacts/
│   ├── constitution-atlas-portable/        # Standalone self-hostable build (Next.js 16 + Node 24 + SQLite)
│   │   ├── Dockerfile                      # Production Docker container
│   │   └── compose.yaml                    # Multi-container orchestration
│   └── constitution-atlas-self-host/       # Self-hosting distribution snapshot
│
├── docs/                                   # Project documentation & specs
│   ├── DELETED_CONTENT_ARCHIVE.md          # Complete verbatim archive of cleaned metadata & sections
│   ├── CUSTOM_URL_AND_HOSTING.md           # Guide for custom domains and hosting platforms
│   ├── NEXT_STEPS.md                       # Technical roadmaps & session handoffs
│   ├── architecture.md                     # System architecture & data flow
│   └── design-system.md                    # Visual guidelines, typography & palette
│
└── tools/                                  # Data extraction, audit & validation scripts
```

---

## 🚀 Getting Started (Local Development)

### Prerequisites
- **Node.js:** `v22.13.0` or higher (`v24.x LTS` recommended)
- **npm:** `v10.x` or higher

### 1. Clone the repository
```bash
git clone https://github.com/vimalranacs/Learn-constitution-.git
cd Learn-constitution-
```

### 2. Run the main web application (`atlas-web`)
```bash
cd atlas-web
npm install
npm run dev
```
Open [http://localhost:5173](http://localhost:5173) or [http://localhost:3000](http://localhost:3000) in your browser.

### 3. Run the portable standalone version (`artifacts/constitution-atlas-portable`)
The portable version uses native Node 24 SQLite storage and requires zero external database dependencies:
```bash
cd artifacts/constitution-atlas-portable
npm install
npm run dev
```

---

## 🐳 Docker Deployment (Self-Hosting)

To run the portable application inside a Docker container with persistent disk storage:

```bash
cd artifacts/constitution-atlas-portable

# 1. Create your environment configuration
cp .env.example .env   # Or set GEMINI_API_KEY if using AI features

# 2. Build and start with Docker Compose
docker compose up -d --build
```
Your instance will be running at `http://localhost:3000` with persistent data stored in the `atlas-data` volume.

---

## 🌐 Deployment Options

| Target Platform | Setup Description | Guide |
|---|---|---|
| **ChatGPT Sites** | Cloudflare Workers + D1 database (Current hosted production) | See [docs/deployment.md](docs/deployment.md) |
| **Railway** | Docker deployment with persistent volume ($5/mo free credit) | See [docs/CUSTOM_URL_AND_HOSTING.md](docs/CUSTOM_URL_AND_HOSTING.md) |
| **Fly.io** | 3 free shared VMs + 3 GB persistent disk volume | See [docs/CUSTOM_URL_AND_HOSTING.md](docs/CUSTOM_URL_AND_HOSTING.md) |
| **Custom VPS** | Node 24 / Docker + Caddy or Nginx reverse proxy with SSL | See [docs/CUSTOM_URL_AND_HOSTING.md](docs/CUSTOM_URL_AND_HOSTING.md) |

---

## 🛠️ Recent Improvements & Fixes

- **Learning Content Cleanup:** Removed internal generation instructions, raw graph edge notation (`const_india —[CONTAINS]→ part_III`), and prompt tags (`[PEDAGOGICAL_ANALOGY]`, `[PHIL_ANALYSIS]`) while preserving 100% of the educational material.
- **Trace Connections Fixed:** Resolved graph traversal response handling and public API routing so shortest paths between any two constitutional concepts resolve accurately.
- **Compare Engine Fixed:** Fixed form submission and server-side option rendering so comparing offices (e.g. *President* vs. *Prime Minister*) updates instantly.
- **Complete Content Archive:** Every cleaned section and metadata line is permanently recorded in [`docs/DELETED_CONTENT_ARCHIVE.md`](docs/DELETED_CONTENT_ARCHIVE.md).

---

## 📜 Sources & Methodology

All constitutional provisions are based on the **Constitution of India (1 May 2026 Official Edition)** published by the Legislative Department, Ministry of Law and Justice, Government of India. Historical debates refer to the official **Constituent Assembly Debates (CAD)**. For complete provenance and methodology, visit the in-app `/methodology` page.
