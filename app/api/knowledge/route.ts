// Knowledge graph API — public read; graph data is non-personal educational content
import {nodes,edges,byId, type AtlasNode} from '../../../lib/knowledge';
import {findPath,searchNodes,neighborhood} from '../../../lib/graph.mjs';
export async function GET(request:Request){
 const q=new URL(request.url).searchParams;let result:unknown;
 if(q.has('from')&&q.has('to')){
  // Wrap null (no path found) in an object so the client can distinguish "no path" from an error
  const path=findPath(nodes,edges,q.get('from'),q.get('to'),{directed:q.get('directed')!=='false',reviewedOnly:q.get('reviewed')==='true'});
  result=path===null?{noPath:true,steps:[],nodes:[]}:path;
 }
 else if(q.has('center')){if(!byId.has(q.get('center')!))return Response.json({error:'Unknown entity'},{status:404});result=neighborhood(nodes,edges,q.get('center'),Number(q.get('depth'))||1,q.get('reviewed')==='true');}
 else result={nodes:searchNodes(nodes,q.get('q')||'',q.get('type')||'',50).map(({id,title,type,status}:AtlasNode)=>({id,title,type,status}))};
 return Response.json(result,{headers:{'Cache-Control':'private, no-store'}});
}
