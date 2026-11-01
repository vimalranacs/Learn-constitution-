import ecosystem from '../../../content/ecosystem.json';
import {env} from '@/lib/runtime.mjs';import {getChatGPTUser} from '../../chatgpt-auth';import {nodes,byId} from '../../../lib/knowledge';import {lessonsById} from '../../../content/course';import {retrieve,validateAnswer,systemPrompt,responseSchema} from '../../../lib/ai.mjs';import {validWriteRequest} from '../../../lib/personal.mjs';import {z} from 'zod';
const input=z.object({question:z.string().trim().min(2).max(2000),mode:z.enum(['research','tutor']),activeId:z.string().max(120).optional(),lessonId:z.string().max(120).optional(),section:z.number().int().min(0).max(1000).optional(),history:z.array(z.object({question:z.string().max(2000),answer:z.string().max(4000)})).max(4).default([]),depth:z.enum(['beginner','intermediate','advanced','research']).default('beginner'),language:z.enum(['English','simple English','Hindi','Hinglish']).default('English')}).strict();
const reply=(data:unknown,status=200)=>Response.json(data,{status,headers:{'Cache-Control':'private, no-store'}});
export async function POST(request:Request){
 const user=await getChatGPTUser();if(!user)return reply({error:'Sign in required'},401);
 if(!validWriteRequest(request))return reply({error:'Same-origin JSON required'},403);
 let value;try{const body=await request.text();if(body.length>26000)return reply({error:'Request too large'},413);value=input.parse(JSON.parse(body));}catch{return reply({error:'Invalid question or context'},400)}
 if(value.activeId&&!byId.has(value.activeId))return reply({error:'Unknown context entity'},400);
 const prepared=value.lessonId?lessonsById.get(value.lessonId):undefined; const extended=ecosystem.lessons.find(l=>l.id===value.lessonId); const lesson=prepared||extended; const activeSection=extended?extended.sections[Math.min(value.section||0,extended.sections.length-1)]:prepared?{title:['Start with a problem','Build the idea','Work through an example','Take this with you'][Math.min(value.section||0,3)],text:[prepared.hook,prepared.explanation,prepared.example,prepared.recap][Math.min(value.section||0,3)]}:null;if(value.lessonId&&!lesson)return reply({error:'Unknown lesson'},400);
 const matches=retrieve(nodes,value.question,value.activeId,lesson?.sources||[]);
 const references=matches.map((n:any)=>({id:n.id,title:n.title,status:n.status,basis:n.basis}));
 if(!matches.length)return reply({answer:'No relevant evidence was found. Try an Article number or a specific institution.',citations:[],actions:[],references,engine:'retrieval-only'});
 const key=env.GEMINI_API_KEY;const model=env.GEMINI_MODEL;
 if(!key||!model)return reply({answer:'Gemini is not configured yet. The retrieved reading below is available without AI. Imported material is not automatically verified.',citations:matches.map((n:any)=>n.id),actions:[],references,engine:'retrieval-only'});
 if(!/^[a-zA-Z0-9._-]+$/.test(model))return reply({error:'The configured Gemini model is invalid.'},503);
 if(!env.DB)return reply({error:'Usage tracking unavailable; AI requests are paused.'},503);
 const day=new Date().toISOString().slice(0,10);
 const total=await env.DB.prepare('INSERT INTO ai_usage (user_id,day,count) VALUES (?,?,1) ON CONFLICT(user_id,day) DO UPDATE SET count=count+1 WHERE count<150 RETURNING count').bind('__public_daily_budget__',day).first();
 if(!total)return reply({error:'The site daily AI limit has been reached. Reading and lessons remain available.'},429);
 const quota=await env.DB.prepare('INSERT INTO ai_usage (user_id,day,count) VALUES (?,?,1) ON CONFLICT(user_id,day) DO UPDATE SET count=count+1 WHERE count<30 RETURNING count').bind(user.userId,day).first();
 if(!quota)return reply({error:'Daily limit reached (30 requests per user). Prepared lessons and source reading remain available.'},429);
 const context=matches.map((n:any)=>({id:n.id,title:n.title,status:n.status,authority:n.authority,basis:n.basis,text:n.text.slice(0,6500),summary:n.summary.slice(0,1000)}));
 try{
 const result=await fetch('https://generativelanguage.googleapis.com/v1beta/models/'+model+':generateContent',{method:'POST',headers:{'Content-Type':'application/json','x-goog-api-key':key},signal:AbortSignal.timeout(45000),body:JSON.stringify({systemInstruction:{parts:[{text:systemPrompt(value.mode,value.language)}]},contents:[{role:'user',parts:[{text:JSON.stringify({question:value.question,lesson:lesson?{id:lesson.id,title:lesson.title,activeSection}:null,depth:value.depth,conversation:value.history,context})}]}],generationConfig:{temperature:.2,maxOutputTokens:2000,responseMimeType:'application/json',responseSchema}})});
 if(!result.ok)return reply({error:result.status===429?'Gemini quota is currently exhausted. Try later.':'Gemini could not answer. Check the server model/key configuration; prepared sources remain available.',references},result.status===429?429:502);
 const body=await result.json() as {candidates?:{content?:{parts?:{text?:string}[]}}[]};
 const text=body.candidates?.[0]?.content?.parts?.map(p=>p.text||'').join('')||'';
 const answer=validateAnswer(JSON.parse(text),matches.map((n:any)=>n.id),context);
 return reply({...answer,references,engine:'gemini',notice:'AI-assisted explanation. Check the linked sources; valid citation IDs do not guarantee a correct interpretation.'});
 }catch{return reply({error:'AI response timed out or failed validation. No answer was accepted.',references},502);}
}

