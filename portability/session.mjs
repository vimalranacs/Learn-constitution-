import {createHmac,scryptSync,timingSafeEqual} from 'node:crypto';
export const cookieName='atlas_session';
export function users(){try{return JSON.parse(process.env.ATLAS_USERS_JSON||'{}')}catch{return {}}}
function secret(){const value=process.env.ATLAS_SESSION_SECRET;if(!value||value.length<32)throw Error('Configure a session secret of at least 32 characters');return value;}
function signature(value){return createHmac('sha256',secret()).update(value).digest('base64url')}
export function createSession(email,now=Date.now()){const body=Buffer.from(JSON.stringify({email,expires:now+7*86400000})).toString('base64url');return body+'.'+signature(body)}
export function verifySession(token,now=Date.now()){
 try{const [body,sig,...rest]=token.split('.');if(rest.length||!body||!sig)return null;const expected=signature(body);if(sig.length!==expected.length||!timingSafeEqual(Buffer.from(sig),Buffer.from(expected)))return null;const data=JSON.parse(Buffer.from(body,'base64url').toString());if(!Number.isFinite(data.expires)||data.expires<=now||!Object.hasOwn(users(),data.email))return null;return {userId:'email:'+data.email,email:data.email,displayName:data.email,fullName:null}}catch{return null}
}
export function verifyPassword(email,password){
 const encoded=users()[email];const [salt,hash]=(typeof encoded==='string'?encoded:'00000000000000000000000000000000:'+ '0'.repeat(128)).split(':');
 try{if(password.length>1024||!salt||!hash)return false;const actual=scryptSync(password,salt,64),expected=Buffer.from(hash,'hex');return Boolean(encoded)&&expected.length===actual.length&&timingSafeEqual(actual,expected)}catch{return false}
}
export function safeReturn(value){return typeof value==='string'&&value.startsWith('/')&&!value.startsWith('//')&&!value.includes('\\')&&!value.startsWith('/signin')&&!value.startsWith('/signout')?value:'/learn'}
