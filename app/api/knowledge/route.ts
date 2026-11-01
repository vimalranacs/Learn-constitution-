// Knowledge graph API — public read; graph data is non-personal educational content
import {nodes,edges,byId, type AtlasNode} from '../../../lib/knowledge';
import {traceResult,searchNodes,neighborhood} from '../../../lib/graph.mjs';
export async function GET(request:Request){
 const q=new URL(request.url).searchParams;let result:unknown;
 if(q.has("from")!==q.has("to"))return Response.json({error:"Choose both a start and destination."},{status:400});
 if(q.has('from')&&q.has('to')){
  const from=q.get('from')!,to=q.get('to')!;
  if(!byId.has(from)||!byId.has(to))return Response.json({error:'Choose two known entities to trace.'},{status:400});
  result=traceResult(nodes,edges,from,to,{directed:q.get('directed')!=='false',reviewedOnly:q.get('reviewed')==='true'});
 }
 else if(q.has('center')){if(!byId.has(q.get('center')!))return Response.json({error:'Unknown entity'},{status:404});result=neighborhood(nodes,edges,q.get('center'),Number(q.get('depth'))||1,q.get('reviewed')==='true');}
 else result={nodes:searchNodes(nodes,q.get('q')||'',q.get('type')||'',50).map(({id,title,type,status}:AtlasNode)=>({id,title,type,status}))};
 return Response.json(result,{headers:{'Cache-Control':'private, no-store'}});
}
