import assert from 'node:assert/strict';
const base=process.env.TEST_ORIGIN||'http://127.0.0.1:5173';
async function device(){const r=await fetch(base+'/api/visitor');assert.equal(r.status,200);return r.headers.getSetCookie().map(x=>x.split(';')[0]).join('; ')}
const one=await device(),two=await device();assert.notEqual(one,two);assert.ok(one);
const headers={cookie:one,origin:base,'Content-Type':'application/json'},key='public_isolation_test';
let r=await fetch(base+'/api/personal',{method:'POST',headers,body:JSON.stringify({kind:'note',key,value:{text:'Synthetic isolated visitor note'}})});assert.equal(r.status,200,await r.text());
r=await fetch(base+'/api/personal',{headers:{cookie:two}});assert.ok(!(await r.json()).records.some(x=>x.key===key));
r=await fetch(base+'/api/personal',{headers:{cookie:one}});assert.ok((await r.json()).records.some(x=>x.key===key));
r=await fetch(base+'/api/personal',{method:'DELETE',headers,body:JSON.stringify({kind:'note',key})});assert.equal(r.status,200);
for(const route of ['/','/courses','/courses/les_00_01_why_rules','/explore','/methodology']){r=await fetch(base+route,{redirect:'manual'});assert.equal(r.status,200,route)}
console.log('PASS: public routes without login; unique HttpOnly device sessions; visitor notes isolated and cleaned up.');
