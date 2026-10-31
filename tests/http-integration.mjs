import assert from 'node:assert/strict';
const base='http://127.0.0.1:5173';
const anonymous=await fetch(base+'/api/personal');assert.equal(anonymous.status,401);
const spoof=await fetch(base+'/api/personal',{headers:{'oai-authenticated-user-id':'victim','oai-authenticated-user-email':'victim@example.test'}});assert.equal(spoof.status,401);
const login=await fetch(base+'/signin-with-chatgpt?return_to=/learn',{redirect:'manual'});const cookie=login.headers.getSetCookie().map(x=>x.split(';')[0]).join('; ');assert.ok(cookie);
const headers={cookie,origin:base,'Content-Type':'application/json'};
const key='integration_test_note';
let r=await fetch(base+'/api/personal',{method:'POST',headers,body:JSON.stringify({kind:'note',key,value:{text:'Persistence integration check'}})});assert.equal(r.status,200,await r.text());
r=await fetch(base+'/api/personal',{headers:{cookie}});assert.ok((await r.json()).records.some(x=>x.key===key));
r=await fetch(base+'/api/personal',{method:'POST',headers:{...headers,origin:'https://evil.test'},body:JSON.stringify({kind:'note',key,value:{text:'CSRF'}})});assert.equal(r.status,403);
r=await fetch(base+'/api/personal',{method:'POST',headers,body:JSON.stringify({kind:'note',key,userId:'victim',value:{text:'Attack'}})});assert.equal(r.status,400);
r=await fetch(base+'/api/personal',{method:'DELETE',headers,body:JSON.stringify({kind:'note',key})});assert.equal(r.status,200);
r=await fetch(base+'/api/knowledge?q=Article%2021',{headers:{cookie}});assert.equal((await r.json()).nodes[0].id,'art_21');
r=await fetch(base+'/api/knowledge?from=inst_president&to=inst_parliament&reviewed=true&directed=true',{headers:{cookie}});assert.equal(await r.json(),null);
r=await fetch(base+'/api/ai',{method:'POST',headers,body:JSON.stringify({question:'What is Parliament?',mode:'research',activeId:'art_79'})});assert.equal(r.status,200);assert.equal((await r.json()).engine,'retrieval-only');
for(const path of ['/atlas','/reader','/learn','/learn/rules','/civic','/paths','/compare','/workspace']){r=await fetch(base+path,{headers:{cookie}});assert.equal(r.status,200,path);}
console.log('HTTP integration PASS: unauthorized/spoofed identity 401, CSRF 403, owner override rejected, D1 write/read/delete, search, direction, no-key fallback, 8 pages.');
