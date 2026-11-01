"""Non-destructive primary-source extraction and Argon comparison, not legal verification."""
import argparse,hashlib,json,re
from pathlib import Path
import pdfplumber
ROOT=Path(__file__).resolve().parents[1]
def normalize(text):return re.sub(r'\s+',' ',text).strip()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pdf',type=Path,required=True);args=parser.parse_args()
    with pdfplumber.open(args.pdf) as document:
        pages=[p.extract_text() or '' for p in document.pages]
    if len(pages)!=402 or '1st May, 2026' not in pages[1]:raise ValueError('Unexpected source edition; review before importing')
    raw=json.loads((ROOT/'constitution_atlas_fullstack/constitution_atlas_fullstack/backend/atlas_data.json').read_text(encoding='utf8'))
    results=[]
    for n in raw['nodes']:
        if n.get('subcategory')!='Article':continue
        start=n.get('page_start');end=n.get('page_end') or start
        valid=isinstance(start,int) and isinstance(end,int) and 1<=start<=end<=len(pages)
        passage=n.get('full_text','').removeprefix('Article ')
        matched=bool(valid and passage and normalize(passage) in normalize(' '.join(pages[start-1:end])))
        results.append({'id':n['id'],'pageStart':start,'pageEnd':end,'normalizedTextMatch':matched})
    source={'edition':'1 May 2026','publisher':'Legislative Department, Government of India','sha256':hashlib.sha256(args.pdf.read_bytes()).hexdigest(),'url':raw['sources'][0]['url'],'pages':pages,'scope':'Raw PDF text extraction. PDF layout, amendment markings and footnotes should be checked in the original. Text matching is not legal verification.'}
    (ROOT/'atlas-web/content/source-pages.json').write_text(json.dumps(source,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf8')
    report={'pdfPages':len(pages),'articleRecords':len(results),'normalizedMatches':sum(r['normalizedTextMatch'] for r in results),'method':'Remove synthetic Article prefix; normalize whitespace; compare whole imported article against claimed source-page interval. A match does not validate boundaries, legal status or current law.','results':results}
    (ROOT/'docs/source-extraction-report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in report.items() if k!='results'}))
if __name__=='__main__':main()
