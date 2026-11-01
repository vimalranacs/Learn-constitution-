"""Read-only, reproducible Argon inventory and integrity audit. No trust promotion."""
import hashlib
import json
import sqlite3
from collections import Counter
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / 'constitution_atlas_fullstack' / 'constitution_atlas_fullstack'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def profile(data):
    nodes, edges = data['nodes'], data['edges']
    ids = Counter(n['id'] for n in nodes)
    keys = Counter((e['source'], e['target'], e['type']) for e in edges)
    return {
        'nodes': len(nodes), 'edges': len(edges),
        'node_types': dict(sorted(Counter(n['node_type'] for n in nodes).items())),
        'duplicate_node_ids': sorted(k for k,v in ids.items() if v > 1),
        'duplicate_edge_triples': [list(k) for k,v in sorted(keys.items()) if v > 1],
        'dangling_edges': [e for e in edges if e['source'] not in ids or e['target'] not in ids],
        'edges_without_reference': sum(not e.get('ref') for e in edges),
        'edges_without_evidence_id': sum(not e.get('evidence_id') for e in edges),
        'edges_without_stable_id': sum(not e.get('id') for e in edges),
        'article_records': sum(n.get('subcategory') == 'Article' for n in nodes),
        'nodes_without_page': sum(not n.get('page_start') for n in nodes),
        'journeys': len(data['journeys']), 'simulations': len(data['simulations']),
        'scope': 'Structural checks only; these counts do not verify legal accuracy or current law.'
    }

def main():
    files = sorted(p for p in LEGACY.rglob('*') if p.is_file() and not {'venv','__pycache__','node_modules'} & set(p.parts))
    files += [ROOT / 'constitution_atlas_explore_the_architecture_of_indian_democracy.html']
    inventory = [{'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size, 'sha256': digest(p)} for p in files]
    snapshot = ROOT / 'legacy' / 'argon-original.zip'
    if not snapshot.exists():
        with zipfile.ZipFile(snapshot, 'w', zipfile.ZIP_DEFLATED) as z:
            for p in files:
                z.write(p, p.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(snapshot) as z:
        for entry in inventory:
            if hashlib.sha256(z.read(entry['path'])).hexdigest() != entry['sha256']:
                raise RuntimeError('Original changed since checkpoint: ' + entry['path'])
    data = json.loads((LEGACY / 'backend/atlas_data.json').read_text(encoding='utf-8'))
    report = profile(data)
    db = LEGACY / 'backend/constitution_atlas.db'
    with sqlite3.connect(db.as_uri() + '?mode=ro', uri=True) as conn:
        report['sqlite_integrity'] = conn.execute('PRAGMA integrity_check').fetchone()[0]
        report['sqlite_foreign_key_violations'] = conn.execute('PRAGMA foreign_key_check').fetchall()
        report['sqlite_schema'] = conn.execute("SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
        report['source_reference_distribution'] = conn.execute('SELECT source_id,count(*) FROM source_references GROUP BY source_id').fetchall()
        report['json_sqlite_node_ids_match'] = {r[0] for r in conn.execute('SELECT id FROM nodes')} == {n['id'] for n in data['nodes']}
    for name, value in [('legacy-inventory.json', inventory), ('legacy-integrity.json', report)]:
        (ROOT / 'docs' / name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k != 'sqlite_schema'}, indent=2))

if __name__ == '__main__':
    main()
