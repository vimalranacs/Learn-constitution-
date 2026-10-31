'use client';
import {useEffect,useState} from 'react';import Link from 'next/link';import {readObject} from '../../lib/http';
export default function CourseRoadmap({lessons}:{lessons:{id:string;title:string;objective:string}[]}){
 const [progress,setProgress]=useState<Record<string,any>>({}),[error,setError]=useState('');
 useEffect(()=>{fetch('/api/personal').then(async r=>{const d=await readObject(r);if(!r.ok)throw Error(d.error);setProgress(Object.fromEntries(d.records.filter((x:any)=>x.kind==='progress').map((x:any)=>[x.key,x.value])))}).catch(e=>setError(e.message));},[]);
 const next=lessons.find(l=>progress[l.id]?.status!=='completed')||lessons[0];
 return <><Link className="button" href={'/learn/'+next.id}>{Object.keys(progress).length?'Continue learning':'Start from the beginning'} →</Link>{error&&<p className="fine">{error}</p>}<ol className="roadmap">{lessons.map((l,i)=><li key={l.id}><span className="section-number">{String(i+1).padStart(2,'0')}</span><div><h2><Link href={'/learn/'+l.id}>{l.title}</Link></h2><p>{l.objective}</p><span className="fine">{(progress[l.id]?.status||'not_started').replaceAll('_',' ')}</span></div></li>)}</ol></>;
}
