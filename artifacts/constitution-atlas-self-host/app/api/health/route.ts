import {env} from '@/lib/runtime.mjs';
export function GET(){return Response.json({status:'ok',milestone:'atlas-course-workspace',personalPersistence:Boolean(env.DB),aiConfigured:Boolean(env.GEMINI_API_KEY&&env.GEMINI_MODEL)});}
