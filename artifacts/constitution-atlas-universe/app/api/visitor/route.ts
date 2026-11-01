import {cookies} from 'next/headers';
export async function GET(){
 const current=(await cookies()).get('atlas_visitor')?.value;
 if(current&&/^[0-9a-f-]{36}$/.test(current))return Response.json({ready:true},{headers:{'Cache-Control':'private, no-store'}});
 return Response.json({ready:true},{headers:{'Cache-Control':'private, no-store','Set-Cookie':`atlas_visitor=${crypto.randomUUID()}; HttpOnly; SameSite=Lax; Path=/; Max-Age=31536000; Secure`}});
}
