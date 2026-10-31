import {env} from 'cloudflare:workers';
import {getChatGPTUser} from '../../chatgpt-auth';
import {listRecords,putRecord,deleteRecord,validWriteRequest} from '../../../lib/personal.mjs';
const response=(body:unknown,status=200)=>Response.json(body,{status,headers:{'Cache-Control':'private, no-store'}});
export async function GET(){
 const user=await getChatGPTUser(); if(!user)return response({error:'Sign in to use your personal workspace.'},401);
 if(!env.DB)return response({error:'Personal storage is temporarily unavailable.'},503);
 return response({records:await listRecords(env.DB,user.userId)});
}
export async function POST(request:Request){
 const user=await getChatGPTUser(); if(!user)return response({error:'Sign in required'},401);
 if(!validWriteRequest(request))return response({error:'Same-origin JSON request required'},403);
 if(!env.DB)return response({error:'Storage unavailable'},503);
 const body=await request.text(); if(body.length>18000)return response({error:'Request too large'},413);
 try{return response({record:await putRecord(env.DB,user.userId,JSON.parse(body))});}
 catch(error){return response({error:error instanceof Error?error.message:'Unable to save'},400);}
}
export async function DELETE(request:Request){
 const user=await getChatGPTUser(); if(!user)return response({error:'Sign in required'},401);
 if(!validWriteRequest(request))return response({error:'Same-origin JSON request required'},403);
 if(!env.DB)return response({error:'Storage unavailable'},503);
 try{const {kind,key}=await request.json() as {kind:string;key:string};await deleteRecord(env.DB,user.userId,kind,key);return response({ok:true});}
 catch{return response({error:'Invalid deletion request'},400);}
}
