import {requireChatGPTUser} from './chatgpt-auth';
export async function protectPage(path:string){return requireChatGPTUser(path);}
