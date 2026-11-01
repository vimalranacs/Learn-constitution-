from pathlib import Path
import re,json
root=Path('.'); src=root/'constitution_atlas_learning_ecosystem'; manifest=json.loads((src/'manifests/curriculum_manifest.json').read_text(encoding='utf8')); knowledge=json.loads((root/'atlas-web/content/knowledge.json').read_text(encoding='utf8')); ids={n['id'] for n in knowledge['nodes']}; lessons=[]; missing=[]
for level in manifest['levels']:
 text=(src/level['course_volume_file']).read_text(encoding='utf8')
 chunks=re.split(r'(?=^## LESSON )',text,flags=re.M)
 for entry in level['lessons']:
  matches=[c for c in chunks if entry['lesson_id'] in c.split('\n')[0]]
  if not matches: missing.append(entry['lesson_id']);continue
  parts=re.split(r'^### (.+)$',matches[0],flags=re.M); sections=[]
  for i in range(1,len(parts),2):
   heading=parts[i].strip(); body=parts[i+1].strip()
   if any(x in heading.lower() for x in ['activity specification','mastery criteria']):continue
   body=re.sub(r'node:([A-Za-z0-9_]+)',lambda m:'/atlas/'+m[1] if m[1] in ids else '#unmapped-concept',body)
   sections.append({'title':heading,'text':body})
  lessons.append({'id':entry['lesson_id'],'title':entry['title'],'level':level['level_number'],'levelTitle':level['title'],'sources':[x for x in entry['canonical_nodes'] if x in ids],'unmapped':[x for x in entry['canonical_nodes'] if x not in ids],'sections':sections,'file':level['course_volume_file'],'reviewStatus':'editorial_review_pending'})
output={'levels':[{k:l[k] for k in ['level_id','level_number','title','prerequisites']} for l in manifest['levels']],'lessons':lessons}
(root/'atlas-web/content/ecosystem.json').write_text(json.dumps(output,ensure_ascii=False,separators=(',',':')),encoding='utf8')
report={'lessons':len(lessons),'sections':sum(len(l['sections']) for l in lessons),'missing':missing,'unmapped':sorted({x for l in lessons for x in l['unmapped']}),'policy':'Supplied completion/verification claims not inherited. Activity specifications excluded from learner prose; not represented as built simulations.'}
(root/'docs/learning-import-audit.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps(report))
