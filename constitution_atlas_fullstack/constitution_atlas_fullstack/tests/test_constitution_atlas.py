"""
Automated Test Suite for CONSTITUTION ATLAS (Runnable via both pytest and python3 unittest)
"""

import os
import re
import sys
import unittest

BACKEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
sys.path.insert(0, BACKEND_DIR)

from main import (
    ATLAS_DATA,
    NODES_BY_ID,
    ADJACENCY,
    find_shortest_path,
    search_knowledge_graph,
    generate_grounded_rag_answer,
    AIQueryRequest,
)


class TestConstitutionAtlas(unittest.TestCase):
    def test_01_pdf_extraction_completeness(self):
        report = ATLAS_DATA["validation_report"]
        self.assertEqual(report["total_pdf_pages"], 402)
        self.assertTrue(report["preamble_extracted"])
        self.assertEqual(report["parts_extracted"], 25)
        self.assertEqual(report["chapters_extracted"], 23)
        self.assertEqual(report["total_articles_extracted"], 470)
        self.assertEqual(report["toc_articles_count"], 470)
        self.assertEqual(report["missing_articles"], [])
        self.assertEqual(report["schedules_extracted"], 12)
        self.assertEqual(report["appendices_extracted"], 3)

    def test_02_key_constitutional_articles_and_pages(self):
        checks = [
            ("art_1", "India, that is Bharat, shall be a Union of States"),
            ("art_14", "Equality before law"),
            ("art_19", "Protection of certain rights regarding freedom of speech"),
            ("art_21", "Protection of life and personal liberty"),
            ("art_21A", "Right to education"),
            ("art_32", "Remedies for enforcement of rights"),
            ("art_51A", "Fundamental duties"),
            ("art_74", "Council of Ministers to aid and advise President"),
            ("art_75", "Other provisions as to Ministers"),
            ("art_246A", "Special provision with respect to goods and services tax"),
            ("art_279A", "Goods and Services Tax Council"),
            ("art_280", "Finance Commission"),
            ("art_324", "Superintendence, direction and control of elections"),
            ("art_330A", "Reservation of seats for women in the House of the People"),
            ("art_352", "Proclamation of Emergency"),
            ("art_368", "Power of Parliament to amend the Constitution"),
            ("art_370", "Temporary provisions with respect to the State of Jammu and Kashmir"),
            ("art_395", "Repeals"),
        ]
        for art_id, expected_substr in checks:
            self.assertIn(art_id, NODES_BY_ID, f"Missing {art_id}")
            node = NODES_BY_ID[art_id]
            combined = re.sub(r"\s+", " ", (node["title"] + " " + node["full_text"]).lower())
            self.assertIn(expected_substr.lower(), combined)
            self.assertTrue(32 <= node["page_start"] <= 283)

    def test_03_all_node_categories_and_edge_integrity(self):
        node_types = {n["node_type"] for n in ATLAS_DATA["nodes"]}
        for required_type in [
            "Constitutional",
            "Cluster",
            "Institutional",
            "Administrative",
            "Philosophical",
            "Judicial",
            "Historical",
            "Process",
        ]:
            self.assertIn(required_type, node_types)

        for edge in ATLAS_DATA["edges"]:
            self.assertIn(edge["source"], NODES_BY_ID, f"Dangling source {edge['source']}")
            self.assertIn(edge["target"], NODES_BY_ID, f"Dangling target {edge['target']}")
            self.assertTrue(edge.get("explanation"), f"Missing explanation on edge {edge['source']} -> {edge['target']}")

    def test_04_all_eight_mandatory_journeys(self):
        self.assertEqual(len(ATLAS_DATA["journeys"]), 8)
        for journey in ATLAS_DATA["journeys"]:
            nodes = journey["nodes"]
            self.assertGreaterEqual(len(nodes), 4)
            for nid in nodes:
                self.assertIn(nid, NODES_BY_ID, f"Journey {journey['id']} references missing node {nid}")
            for i in range(len(nodes) - 1):
                path = find_shortest_path(nodes[i], nodes[i + 1])
                self.assertGreaterEqual(
                    path["hops"],
                    1,
                    f"Disconnected hop in {journey['id']}: {nodes[i]} -> {nodes[i + 1]}",
                )

    def test_05_shortest_path_discovery(self):
        path = find_shortest_path("art_21", "judg_puttaswamy")
        self.assertTrue(1 <= path["hops"] <= 3)
        path_ids = [n["id"] for n in path["nodes"]]
        self.assertEqual(path_ids[0], "art_21")
        self.assertEqual(path_ids[-1], "judg_puttaswamy")

        path2 = find_shortest_path("inst_citizens", "admin_dm_collector")
        self.assertTrue(1 <= path2["hops"] <= 5)

    def test_06_fts5_search_and_grounded_rag(self):
        res_privacy = search_knowledge_graph("Right to Privacy Puttaswamy")
        self.assertTrue(any(n["id"] in ("phil_privacy", "judg_puttaswamy", "art_21") for n in res_privacy))

        res_art = search_knowledge_graph("Article 368")
        self.assertEqual(res_art[0]["id"], "art_368")

        rag = generate_grounded_rag_answer(
            AIQueryRequest(
                question="How does Article 21 protect the Right to Privacy and what did Puttaswamy hold?",
                active_node_id="art_21",
                depth_level="advanced",
                mode="standard",
            )
        )
        self.assertTrue("Constitutional Text" in rag["answer"] or "Judicial Interpretation" in rag["answer"])
        cited_ids = {c["node_id"] for c in rag["citations"]}
        self.assertIn("art_21", cited_ids)


if __name__ == "__main__":
    unittest.main(verbosity=2)
