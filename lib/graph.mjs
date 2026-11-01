export function searchNodes(nodes,query,type='',limit=30){
 const q=query.trim().toLowerCase();const explicit=q.replace(/^(article|art\.?)\s*/,'');
 return nodes.filter(n=>(!type||n.type===type)&&(!q||(n.title+' '+n.id+' '+n.basis).toLowerCase().includes(q)||n.id==='art_'+explicit.toUpperCase()))
 .sort((a,b)=>Number(b.id==='art_'+explicit.toUpperCase())-Number(a.id==='art_'+explicit.toUpperCase())||a.title.localeCompare(b.title)).slice(0,Math.max(1,Math.min(100,limit)));
}
export function findPath(nodes,edges,from,to,{directed=true,reviewedOnly=false}={}){
 const ids=new Set(nodes.map(n=>n.id));if(!ids.has(from)||!ids.has(to))return null;
 const adjacent=new Map();for(const e of edges){if(reviewedOnly&&e.status!=='source_checked')continue;if(!ids.has(e.source)||!ids.has(e.target))continue;
  if(!adjacent.has(e.source))adjacent.set(e.source,[]);adjacent.get(e.source).push({id:e.target,edge:e,reverse:false});
  if(!directed){if(!adjacent.has(e.target))adjacent.set(e.target,[]);adjacent.get(e.target).push({id:e.source,edge:e,reverse:true});}}
 const queue=[from],seen=new Set([from]),parents=new Map();
 for(let i=0;i<queue.length;i++){const current=queue[i];if(current===to){const result={nodes:[to],steps:[]};let cursor=to;while(cursor!==from){const p=parents.get(cursor);result.nodes.unshift(p.from);result.steps.unshift({edge:p.edge,reverse:p.reverse});cursor=p.from;}return result;}
 for(const next of adjacent.get(current)||[]){if(!seen.has(next.id)){seen.add(next.id);parents.set(next.id,{from:current,...next});queue.push(next.id);}}}return null;
}
export function neighborhood(nodes,edges,center,depth=1,reviewedOnly=false){
 const selected=new Set([center]);const usable=edges.filter(e=>!reviewedOnly||e.status==='source_checked');
 for(let level=0;level<Math.min(2,depth);level++){const current=new Set(selected);for(const e of usable){if(current.has(e.source)||current.has(e.target)){selected.add(e.source);selected.add(e.target);}}}
 const resultNodes=nodes.filter(n=>selected.has(n.id)).sort((a,b)=>Number(b.id===center)-Number(a.id===center)).slice(0,80);const visible=new Set(resultNodes.map(n=>n.id));
 return {nodes:resultNodes,edges:usable.filter(e=>visible.has(e.source)&&visible.has(e.target)),truncated:selected.size>80};
}

// Capability checks use recorded edges only; an unavailable path is an empty state.
export function traceOptions(nodes,edges,from,to,directed=true){
 const any=findPath(nodes,edges,from,to,{directed:false});
 const arrows=findPath(nodes,edges,from,to,{directed:true});
 const checked=findPath(nodes,edges,from,to,{directed:directed&&!!arrows,reviewedOnly:true});
 return {connected:!!any,directionAvailable:!!arrows,reviewedAvailable:!!checked};
}
export function traceResult(nodes,edges,from,to,options){
 return findPath(nodes,edges,from,to,options) || {noPath:true,nodes:[],steps:[]};
}
