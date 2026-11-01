export async function readObject(response:Response):Promise<Record<string,any>> {
 let value:unknown;try{value=await response.json()}catch{throw new Error(response.status===401||response.status===403?'Your access session is unavailable. Reload the page to reconnect.':'The service returned an unreadable response. Please retry shortly.')}
 if(!response.ok)throw new Error(value&&typeof value==='object'&&'error' in value&&typeof value.error==='string'?value.error:response.status>=500?'The service is temporarily unavailable. Please retry shortly.':'The request could not be completed. Reload and try again.');
 if(!value||typeof value!=='object'||Array.isArray(value))throw new Error('The service returned incomplete data. Please retry.');return value as Record<string,any>;
}
