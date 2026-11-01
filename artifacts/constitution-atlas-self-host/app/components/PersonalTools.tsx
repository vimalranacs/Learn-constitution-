'use client';
import {readObject} from '../../lib/http';
import {useEffect,useState} from 'react';
type RecordItem={kind:string;key:string;value:Record<string,unknown>};
export default function PersonalTools({id,title,lesson=false,completion,section=0,onCompletionChange}:{id:string;title:string;lesson?:boolean;completion?:boolean;section?:number;onCompletionChange?:(value:boolean)=>void}){
 const [note,setNote]=useState(''),[saved,setSaved]=useState(false),[status,setStatus]=useState(''),[ready,setReady]=useState(false),[storedComplete,setComplete]=useState(false);
 const complete=completion??storedComplete;
 useEffect(()=>{let active=true;setReady(false);fetch('/api/personal').then(async r=>{const d=await readObject(r);if(!r.ok)throw Error(d.error);if(active){const rows=d.records as RecordItem[];setNote(String(rows.find(x=>x.kind==='note'&&x.key===id)?.value.text||''));setSaved(rows.some(x=>x.kind==='bookmark'&&x.key===id));setComplete(rows.find(x=>x.kind==='progress'&&x.key===id)?.value.status==='completed');setReady(true);setStatus('');}}).catch(e=>active&&setStatus(e.message));return()=>{active=false};},[id]);
 async function write(kind:string,value:unknown,method='POST'){
  setStatus('Saving…');
  try{const r=await fetch('/api/personal',{method,headers:{'Content-Type':'application/json'},body:JSON.stringify({kind,key:id,...(method==='POST'?{value}:{})})});const d=await readObject(r);if(!r.ok)throw Error(d.error);setStatus('Saved to your private workspace.');return true;}
  catch(e){setStatus(e instanceof Error?e.message:'Unable to save');return false;}
 }
 return <details className="personal"><summary>Your notes & saved items</summary><div className="tool-row"><button disabled={!ready} className="secondary" onClick={async()=>{if(await write('bookmark',{title},saved?'DELETE':'POST'))setSaved(!saved)}}>{saved?'Remove bookmark':'Bookmark'}</button>{lesson&&<button disabled={!ready} onClick={async()=>{if(await write('progress',{status:complete?'in_progress':'completed',section})){setComplete(!complete);onCompletionChange?.(!complete)}}}>{complete?'Completed · mark in progress':'Mark lesson complete'}</button>}</div><label className="field">Private note<textarea value={note} maxLength={10000} onChange={e=>setNote(e.target.value)} rows={4}/></label><button disabled={!ready} onClick={()=>write('note',{text:note})}>Save note</button><p role="status" className="fine">{status}</p></details>;
}
