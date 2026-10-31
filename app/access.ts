import {requireChatGPTUser} from './chatgpt-auth';
// Only Sites authenticated dispatch may supply production identity headers.
// Local development serves public constitutional material, never personal records.
export async function protectPage(path:string) {
  if(process.env.NODE_ENV==='development') return;
  await requireChatGPTUser(path);
}
