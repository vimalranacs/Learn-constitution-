import data from '../../../../content/parliament.json';
import {getChatGPTUser} from '../../../chatgpt-auth';
export async function GET(_request:Request,{params}:{params:Promise<{id:string}>}) {
  if(process.env.NODE_ENV!=='development'&&!await getChatGPTUser()) return Response.json({error:'Sign in required'},{status:401});
  const {id}=await params;
  if(id!=='art_79') return Response.json({error:'Entity not available in this reviewed slice'},{status:404});
  return Response.json(data,{headers:{'Cache-Control':'private, no-store'}});
}
