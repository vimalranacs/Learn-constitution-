"""Export one source-checked Argon article; keep the remainder quarantined."""
import argparse, hashlib, json, re
from pathlib import Path
import pdfplumber
from audit_legacy import LEGACY, ROOT, profile

def normalized(value):
    return re.sub(r'\s+', ' ', value).strip()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--pdf',type=Path,required=True)
    args=parser.parse_args()
    raw=json.loads((LEGACY/'backend/atlas_data.json').read_text(encoding='utf-8'))
    audit=profile(raw)
    if audit['duplicate_node_ids'] or audit['dangling_edges']:
        raise ValueError('Structural integrity failure')
    original=next(n for n in raw['nodes'] if n['id']=='art_79')
    expected=original['full_text'].removeprefix('Article ')
    with pdfplumber.open(args.pdf) as pdf:
        if normalized(expected) not in normalized(pdf.pages[66].extract_text()):
            raise ValueError('Article 79 does not match source page 67')
        if '1st May, 2026' not in pdf.pages[1].extract_text():
            raise ValueError('Unexpected edition')
        pages=len(pdf.pages)
    source={'id':'src_const_2026_leg','title':'Constitution of India','publisher':'Government of India, Legislative Department','edition':'1 May 2026','url':raw['sources'][0]['url'],'pdfPage':67,'pageCount':pages,'sha256':hashlib.sha256(args.pdf.read_bytes()).hexdigest(),'reviewed':'2026-11-01','method':'Article 79 compared with PDF page 67 after whitespace normalization and removal of importer-added Article prefix. Preface edition checked. No current-law certification.'}
    result={'article':{'id':'art_79','title':original['title'],'text':expected,'status':'Source passage checked'},'source':source}
    target=ROOT/'atlas-web/content'
    target.mkdir(exist_ok=True)
    (target/'parliament.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    quarantine={'status':'needs_review','nodes':raw['nodes'],'edges':[{**e,'id':'legacy_'+hashlib.sha256(json.dumps([e['source'],e['type'],e['target']],separators=(',',':')).encode()).hexdigest()[:20],'reviewStatus':'needs_review'} for e in raw['edges']]}
    (ROOT/'data/legacy-quarantine.json').write_text(json.dumps(quarantine,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    (ROOT/'docs/source-check.json').write_text(json.dumps(source,indent=2)+'\n',encoding='utf-8')
    print('Exported checked Article 79; quarantined 635 nodes and 1255 edges.')

if __name__=='__main__': main()
