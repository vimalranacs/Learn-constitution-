"""Deterministic, honest Argon migration: preserve IDs and distinguish review states."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    raw=json.loads((ROOT/'constitution_atlas_fullstack/constitution_atlas_fullstack/backend/atlas_data.json').read_text(encoding='utf8'))
    nodes=[]
    for n in raw['nodes']:
        nodes.append({'id':n['id'],'title':n['title'],'type':n['node_type'],'category':n.get('subcategory',''),'summary':n.get('summary',''),'text':n.get('full_text',''),'basis':n.get('constitutional_basis',''),'authority':n.get('authority_type','Unspecified'),'page':n.get('page_start'),'pageEnd':n.get('page_end'),'part':n.get('part_id'),'omitted':n.get('is_omitted',False),'status':'source_checked' if n['id']=='art_79' else 'needs_review','powers':n.get('powers_and_functions',[]),'limits':n.get('checks_and_balances','')})
    edges=[{'id':'edge_'+hashlib.sha256(json.dumps([e['source'],e['type'],e['target']],separators=(',',':')).encode()).hexdigest()[:20],'source':e['source'],'target':e['target'],'type':e['type'],'explanation':e.get('explanation',''),'ref':e.get('ref',''),'status':'needs_review'} for e in raw['edges']]
    # Add a narrowly reviewed compositional relation; do not infer command.
    for target in ['inst_president','inst_lok_sabha','inst_rajya_sabha']:
        edges.append({'id':'art79_composition_'+target,'source':'inst_parliament','target':target,'type':'CONSISTS_OF','explanation':'Article 79 names the President and two Houses as components of Parliament. This is composition, not command.','ref':'Article 79; Legislative Department 1 May 2026 edition, PDF p. 67','status':'source_checked'})
    result={'nodes':sorted(nodes,key=lambda n:n['id']),'edges':sorted(edges,key=lambda e:e['id']),'edition':'1 May 2026','sourceUrl':raw['sources'][0]['url']}
    (ROOT/'atlas-web/content/knowledge.json').write_text(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf8')
    print(f'Exported {len(nodes)} nodes and {len(edges)} edges. Only Article 79 and its 3 composition edges are source-checked.')
if __name__=='__main__':main()
