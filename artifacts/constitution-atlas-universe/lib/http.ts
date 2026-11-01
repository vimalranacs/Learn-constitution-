export async function readObject(response:Response):Promise<Record<string,any>> {
  const value:unknown=await response.json();
  if(!value||typeof value!=='object'||Array.isArray(value))throw new Error('Unexpected server response');
  return value as Record<string,any>;
}
