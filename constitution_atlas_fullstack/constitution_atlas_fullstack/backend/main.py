"""
CONSTITUTION ATLAS — FastAPI Backend, Graph Engine, FTS5 Search, Source Manager & Gemini RAG Service
"""

import os
import re
import json
import sqlite3
from collections import deque
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "constitution_atlas.db")
JSON_DATA_PATH = os.path.join(BASE_DIR, "atlas_data.json")
REPORT_PATH = os.path.join(BASE_DIR, "extraction_validation_report.json")

STOPWORDS = {"the", "to", "of", "in", "and", "or", "for", "on", "with", "as", "by", "at", "is", "are", "how", "what", "who", "why", "does"}

app = FastAPI(
    title="CONSTITUTION ATLAS API",
    description="AI-Powered Interactive Knowledge Graph of the Indian Constitution, Government, Democracy, and Political Philosophy",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


with open(JSON_DATA_PATH, "r", encoding="utf-8") as f:
    ATLAS_DATA = json.load(f)

NODES_BY_ID: Dict[str, Dict[str, Any]] = {n["id"]: n for n in ATLAS_DATA["nodes"]}
ADJACENCY: Dict[str, List[Dict[str, Any]]] = {n["id"]: [] for n in ATLAS_DATA["nodes"]}
for edge in ATLAS_DATA["edges"]:
    s, t = edge["source"], edge["target"]
    if s in ADJACENCY and t in ADJACENCY:
        ADJACENCY[s].append({"neighbor": t, "direction": "outgoing", "edge": edge})
        ADJACENCY[t].append({"neighbor": s, "direction": "incoming", "edge": edge})


class AIQueryRequest(BaseModel):
    question: str
    active_node_id: Optional[str] = None
    depth_level: str = "intermediate"
    mode: str = "standard"


class NewSourceRequest(BaseModel):
    id: str
    title: str
    category: str
    authority: str
    publication_date: str
    url: str
    pages: Optional[int] = None


def find_shortest_path(source_id: str, target_id: str) -> Dict[str, Any]:
    """BFS shortest meaningful constitutional path between two nodes."""
    if source_id not in NODES_BY_ID or target_id not in NODES_BY_ID:
        raise ValueError("Source or target node ID not found in Knowledge Graph.")
    if source_id == target_id:
        return {"source": source_id, "target": target_id, "nodes": [NODES_BY_ID[source_id]], "edges": [], "hops": 0}

    queue = deque([(source_id, [source_id], [])])
    visited = {source_id}

    while queue:
        curr, path_nodes, path_edges = queue.popleft()
        for item in ADJACENCY.get(curr, []):
            nxt = item["neighbor"]
            if nxt == "const_india" and target_id != "const_india" and source_id != "const_india":
                continue
            if nxt in visited:
                continue
            new_nodes = path_nodes + [nxt]
            new_edges = path_edges + [item["edge"]]
            if nxt == target_id:
                return {
                    "source": source_id,
                    "target": target_id,
                    "nodes": [NODES_BY_ID[nid] for nid in new_nodes],
                    "edges": new_edges,
                    "hops": len(new_edges),
                }
            visited.add(nxt)
            queue.append((nxt, new_nodes, new_edges))

    queue = deque([(source_id, [source_id], [])])
    visited = {source_id}
    while queue:
        curr, path_nodes, path_edges = queue.popleft()
        for item in ADJACENCY.get(curr, []):
            nxt = item["neighbor"]
            if nxt in visited:
                continue
            new_nodes = path_nodes + [nxt]
            new_edges = path_edges + [item["edge"]]
            if nxt == target_id:
                return {
                    "source": source_id,
                    "target": target_id,
                    "nodes": [NODES_BY_ID[nid] for nid in new_nodes],
                    "edges": new_edges,
                    "hops": len(new_edges),
                }
            visited.add(nxt)
            queue.append((nxt, new_nodes, new_edges))

    return {"source": source_id, "target": target_id, "nodes": [], "edges": [], "hops": -1}


def search_knowledge_graph(query: str, node_type: Optional[str] = None, limit: int = 25) -> List[Dict[str, Any]]:
    conn = get_db()
    cur = conn.cursor()
    q_clean = query.strip()
    if not q_clean:
        conn.close()
        return []

    results = []
    seen_ids = set()

    # Prioritize explicit Article mentions in the query (e.g. "Article 21", "Art 368", or bare "21")
    for m_art in re.finditer(r"(?:art(?:icle)?\.?\s*)(\d+[A-Za-z]*)\b", q_clean, re.IGNORECASE):
        aid = f"art_{m_art.group(1).upper()}"
        if aid in NODES_BY_ID and aid not in seen_ids:
            results.append(NODES_BY_ID[aid])
            seen_ids.add(aid)

    m_bare = re.match(r"^(\d+[A-Za-z]*)$", q_clean)
    if m_bare:
        aid = f"art_{m_bare.group(1).upper()}"
        if aid in NODES_BY_ID and aid not in seen_ids:
            results.append(NODES_BY_ID[aid])
            seen_ids.add(aid)

    raw_tokens = [re.sub(r"[^\w]", "", t) for t in q_clean.split() if re.sub(r"[^\w]", "", t)]
    tokens = [t for t in raw_tokens if t.lower() not in STOPWORDS] or raw_tokens
    if tokens:
        fts_query = " OR ".join(f'"{t}"*' for t in tokens)
        sql = "SELECT id FROM fts_nodes WHERE fts_nodes MATCH ? ORDER BY bm25(fts_nodes, 10.0, 8.0, 2.0, 2.0, 4.0, 5.0, 1.0) LIMIT ?"
        for row in cur.execute(sql, (fts_query, limit * 3)):
            nid = row["id"]
            if nid not in seen_ids and nid in NODES_BY_ID:
                node = NODES_BY_ID[nid]
                if not node_type or node["node_type"].lower() == node_type.lower():
                    results.append(node)
                    seen_ids.add(nid)
                    if len(results) >= limit:
                        break
    conn.close()
    return results


def generate_grounded_rag_answer(req: AIQueryRequest) -> Dict[str, Any]:
    retrieved = search_knowledge_graph(req.question, limit=6)
    if req.active_node_id and req.active_node_id in NODES_BY_ID:
        active_node = NODES_BY_ID[req.active_node_id]
        retrieved = [active_node] + [n for n in retrieved if n["id"] != active_node["id"]]

    if not retrieved:
        retrieved = [NODES_BY_ID["const_india"], NODES_BY_ID["art_21"], NODES_BY_ID["inst_parliament"]]

    citations = []
    sections_by_authority = {
        "Constitutional Text": [],
        "Judicial Interpretation": [],
        "Statutory & Administrative Practice": [],
        "Philosophical & Historical Context": [],
    }

    for n in retrieved[:6]:
        exp = (n.get("explanations") or {}).get(req.depth_level) or n.get("summary", "")
        cite_entry = {
            "node_id": n["id"],
            "title": n["title"],
            "code": n.get("code", ""),
            "node_type": n["node_type"],
            "authority_type": n.get("authority_type", "Constitutional Text"),
            "page_start": n.get("page_start"),
            "constitutional_basis": n.get("constitutional_basis", ""),
        }
        citations.append(cite_entry)

        auth = n.get("authority_type", "Constitutional Text")
        if auth == "Constitutional Text":
            pg_str = f" (Official PDF p. {n['page_start']})" if n.get("page_start") else ""
            sections_by_authority["Constitutional Text"].append(f"• **{n['title']}**{pg_str}: {exp}")
        elif auth == "Judicial Interpretation":
            sections_by_authority["Judicial Interpretation"].append(f"• **{n['title']}** ({n.get('code', '')}): {exp}")
        elif auth in ("Statutory Law", "Administrative Practice", "Constitutional Conventions"):
            sections_by_authority["Statutory & Administrative Practice"].append(f"• **{n['title']}** [{auth}]: {exp}")
        else:
            sections_by_authority["Philosophical & Historical Context"].append(f"• **{n['title']}**: {exp}")

    retrieved_ids = {n["id"] for n in retrieved[:6]}
    related_edges = []
    for nid in list(retrieved_ids)[:3]:
        for adj in ADJACENCY.get(nid, [])[:4]:
            e = adj["edge"]
            related_edges.append({
                "source": e["source"],
                "target": e["target"],
                "type": e["type"],
                "ref": e.get("ref", ""),
                "explanation": e.get("explanation", "")
            })

    gemini_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if gemini_key:
        try:
            from google import genai
            client = genai.Client(api_key=gemini_key)
            context_block = "\n".join(
                f"[{c['node_id']}] {c['title']} ({c['authority_type']}, {c['constitutional_basis']}): {NODES_BY_ID[c['node_id']].get('summary', '')}"
                for c in citations
            )
            prompt = (
                f"You are the CONSTITUTION ATLAS Research Assistant. Answer the user's question strictly grounded in the retrieved nodes below.\n"
                f"Explicitly distinguish: (1) Constitutional Text, (2) Judicial Interpretation, (3) Statutory/Administrative Practice, and (4) Philosophical Context.\n"
                f"Depth Level: {req.depth_level} | Mode: {req.mode}\n\n"
                f"Retrieved Nodes:\n{context_block}\n\nUser Question: {req.question}"
            )
            resp = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
            if resp and resp.text:
                return {
                    "answer": resp.text,
                    "citations": citations,
                    "related_edges": related_edges[:6],
                    "engine": "gemini-2.5-flash + FTS5 Graph RAG",
                }
        except Exception:
            pass

    parts_md = [f"### Grounded Constitutional Analysis ({req.depth_level.title()} Depth)"]
    for section_title, bullets in sections_by_authority.items():
        if bullets:
            parts_md.append(f"\n**{section_title}**\n" + "\n".join(bullets))

    if related_edges:
        edge_lines = [
            f"• `{e['source']}` **{e['type']}** `{e['target']}` ({e['ref']}): {e['explanation']}"
            for e in related_edges[:4]
        ]
        parts_md.append("\n**Verified Knowledge Graph Connections**\n" + "\n".join(edge_lines))

    if req.mode == "socratic":
        parts_md.append(
            f"\n**Socratic Inquiry Prompt**: How does the constitutional balance in **{citations[0]['title']}** prevent arbitrary concentration of power while enabling democratic governance?"
        )

    return {
        "answer": "\n".join(parts_md),
        "citations": citations,
        "related_edges": related_edges[:6],
        "engine": "Constitution Atlas Deterministic Graph RAG (Offline-Ready)",
    }


@app.get("/api/health")
def health_check():
    return {"status": "ok", "nodes": len(NODES_BY_ID), "edges": len(ATLAS_DATA["edges"])}


@app.get("/api/validation-report")
def get_validation_report():
    return ATLAS_DATA["validation_report"]


@app.get("/api/graph/overview")
def get_graph_overview():
    return {
        "root": NODES_BY_ID["const_india"],
        "clusters": ATLAS_DATA["clusters"],
        "journeys": ATLAS_DATA["journeys"],
        "trace_the_power": ATLAS_DATA["trace_the_power"],
    }


@app.get("/api/nodes/{node_id}")
def get_node_detail(node_id: str):
    if node_id not in NODES_BY_ID:
        raise HTTPException(status_code=404, detail=f"Node '{node_id}' not found")
    node = NODES_BY_ID[node_id]
    neighbors = []
    for item in ADJACENCY.get(node_id, []):
        nb = NODES_BY_ID.get(item["neighbor"])
        if nb:
            neighbors.append({
                "direction": item["direction"],
                "edge": item["edge"],
                "node": {
                    "id": nb["id"],
                    "title": nb["title"],
                    "code": nb.get("code", ""),
                    "node_type": nb["node_type"],
                    "subcategory": nb.get("subcategory", ""),
                    "cluster_id": nb.get("cluster_id", ""),
                },
            })
    return {"node": node, "neighbors": neighbors}


@app.get("/api/graph/shortest-path")
def api_shortest_path(source: str = Query(...), target: str = Query(...)):
    try:
        return find_shortest_path(source, target)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/api/search")
def api_search(q: str = Query(""), node_type: Optional[str] = Query(None), limit: int = Query(25)):
    return {"query": q, "results": search_knowledge_graph(q, node_type=node_type, limit=limit)}


@app.get("/api/journeys")
def api_journeys():
    return ATLAS_DATA["journeys"]


@app.get("/api/simulations")
def api_simulations():
    return ATLAS_DATA["simulations"]


@app.get("/api/trace-the-power")
def api_trace_the_power():
    return ATLAS_DATA["trace_the_power"]


@app.get("/api/timeline")
def api_timeline():
    return ATLAS_DATA["timeline"]


@app.get("/api/sources")
def api_sources():
    conn = get_db()
    rows = [dict(r) for r in conn.execute("SELECT * FROM sources").fetchall()]
    conn.close()
    return rows


@app.post("/api/sources")
def api_add_source(src: NewSourceRequest):
    conn = get_db()
    conn.execute(
        "INSERT OR REPLACE INTO sources VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (src.id, src.title, src.category, src.authority, src.publication_date, src.url, "User Uploaded & Indexed", src.pages),
    )
    conn.commit()
    conn.close()
    return {"status": "indexed", "source": src.model_dump()}


@app.post("/api/ai/ask")
def api_ai_ask(req: AIQueryRequest):
    return generate_grounded_rag_answer(req)
