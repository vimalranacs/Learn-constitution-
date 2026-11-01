import {cookies} from 'next/headers';
export async function getChatGPTUser(){const id=(await cookies()).get('atlas_visitor')?.value;return id&&/^[0-9a-f-]{36}$/.test(id)?{userId:'visitor:'+id,email:'',displayName:'This device',fullName:null}:null}
export async function requireChatGPTUser(_path:string){return getChatGPTUser()}
