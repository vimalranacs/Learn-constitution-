export const kinds=['note','bookmark','progress','review','view'];
const idPattern=/^[A-Za-z0-9_.:-]{1,120}$/;
export function validateRecord(input){
 if(!input||typeof input!=='object'||Array.isArray(input))throw new Error('Expected a record');
 if(Object.keys(input).some(k=>!['kind','key','value'].includes(k)))throw new Error('Unexpected field');
 const {kind,key,value}=input;
 if(!kinds.includes(kind)||typeof key!=='string'||!idPattern.test(key))throw new Error('Invalid record identity');
 if(!value||typeof value!=='object'||Array.isArray(value))throw new Error('Invalid value');
 if(JSON.stringify(value).length>16000)throw new Error('Record too large');
 if(kind==='note'&&(typeof value.text!=='string'||value.text.length>10000))throw new Error('Note must contain text (max 10,000 characters)');
 if(kind==='bookmark'&&(typeof value.title!=='string'||value.title.length>300))throw new Error('Bookmark needs a title');
 if(kind==='progress'&&(!['in_progress','completed','needs_review'].includes(value.status)||!Number.isInteger(value.section)||value.section<0||value.section>1000))throw new Error('Invalid progress');
 if(kind==='review'&&(!Number.isFinite(value.due)||!Number.isInteger(value.interval)||value.interval<1||value.interval>365))throw new Error('Invalid review schedule');
 if(kind==='view'&&(!Array.isArray(value.nodes)||value.nodes.length>100||value.nodes.some(n=>typeof n!=='string'||!idPattern.test(n))))throw new Error('Invalid saved view');
 return {kind,key,value};
}
export function nextReview(previous,remembered,now=Date.now()){
 const interval=remembered?Math.min(365,Math.max(1,(previous?.interval||0)*2||1)):1;
 return {interval,due:now+interval*86400000,lastReviewed:now,remembered};
}
export async function listRecords(db,userId){
 const rows=await db.prepare('SELECT kind,record_key,value_json,updated_at FROM personal_records WHERE user_id=? ORDER BY updated_at DESC LIMIT 2000').bind(userId).all();
 return rows.results.map(r=>({kind:r.kind,key:r.record_key,value:JSON.parse(r.value_json),updatedAt:r.updated_at}));
}
export async function putRecord(db,userId,input,now=Date.now()){
 const {kind,key,value}=validateRecord(input);
 await db.prepare('INSERT INTO personal_records (user_id,kind,record_key,value_json,updated_at) VALUES (?,?,?,?,?) ON CONFLICT(user_id,kind,record_key) DO UPDATE SET value_json=excluded.value_json,updated_at=excluded.updated_at').bind(userId,kind,key,JSON.stringify(value),now).run();
 return {kind,key,value,updatedAt:now};
}
export async function deleteRecord(db,userId,kind,key){
 if(!kinds.includes(kind)||typeof key!=='string'||!idPattern.test(key))throw new Error('Invalid record identity');
 await db.prepare('DELETE FROM personal_records WHERE user_id=? AND kind=? AND record_key=?').bind(userId,kind,key).run();
}
export function validWriteRequest(request){
 const origin=request.headers.get('origin');
 return origin===new URL(request.url).origin&&request.headers.get('content-type')?.split(';')[0]==='application/json';
}
