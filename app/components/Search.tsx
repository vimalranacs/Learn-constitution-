'use client';
import {readObject} from '../../lib/http';
import {useState,useEffect} from 'react';import Link from 'next/link';
export default function Search(){
 const [query,setQuery]=useState(''),[items,setItems]=useState<{id:string;title:string;type:string}[]>([]),[error,setError]=useState('');
 useEffect(()=>{if(!query.trim()){setItems([]);setError('');return;}const controller=new AbortController();const timer=setTimeout(()=>{fetch('/api/knowledge?q='+encodeURIComponent(query),{signal:controller.signal}).then(async r=>{const d=await readObject(r);if(!r.ok)throw Error(d.error);setItems(d.nodes);setError(d.nodes.length?'':'No matching entities. Try an Article number or institution.');}).catch(e=>{if(e.name!=='AbortError')setError(e.message)})},200);return()=>{clearTimeout(timer);controller.abort();}},[query]);
 return <div className="search"><label className="sr-only" htmlFor="atlas-search">Search the Atlas</label><input id="atlas-search" type="search" value={query} onChange={e=>setQuery(e.target.value)} placeholder="Search Articles, institutions, ideas…"/>{query&&<div className="search-results" role="region" aria-label="Search results">{error&&<p role="status">{error}</p>}{items.map(n=><Link key={n.id} href={'/atlas/'+n.id} onClick={()=>setQuery('')}>{n.title}<small>{n.type}</small></Link>)}</div>}</div>;
}
