import {getChatGPTUser} from '../../chatgpt-auth';
import {nodes,edges,byId, type AtlasNode} from '../../../lib/knowledge';
import {findPath,searchNodes,neighborhood} from '../../../lib/graph.mjs';
export async function GET(request:Request){
 if(!await getChatGPTUser())return Response.json({error:'Sign in required'},{status:401});
 const q=new URL(request.url).searchParams;let result:unknown;
 if(q.has('from')&&q.has('to'))result=findPath(nodes,edges,q.get('from'),q.get('to'),{directed:q.get('directed')!=='false',reviewedOnly:q.get('reviewed')==='true'});
 else if(q.has('center')){if(!byId.has(q.get('center')!))return Response.json({error:'Unknown entity'},{status:404});result=neighborhood(nodes,edges,q.get('center'),Number(q.get('depth'))||1,q.get('reviewed')==='true');}
 else result={nodes:searchNodes(nodes,q.get('q')||'',q.get('type')||'',50).map(({id,title,type,status}:AtlasNode)=>({id,title,type,status}))};
 return Response.json(result,{headers:{'Cache-Control':'private, no-store'}});
}
