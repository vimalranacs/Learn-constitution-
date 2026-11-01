import unittest
from tools.audit_legacy import profile

class AuditTests(unittest.TestCase):
    def test_detects_duplicate_and_dangling_data(self):
        node = {'id':'a','node_type':'Constitutional'}
        edge = {'source':'a','target':'missing','type':'CONTAINS'}
        result = profile({'nodes':[node,node], 'edges':[edge,edge], 'journeys':[], 'simulations':[]})
        self.assertEqual(result['duplicate_node_ids'], ['a'])
        self.assertEqual(len(result['dangling_edges']), 2)
        self.assertEqual(result['duplicate_edge_triples'], [['a','missing','CONTAINS']])
        self.assertEqual(result['edges_without_evidence_id'], 2)

if __name__ == '__main__':
    unittest.main()
