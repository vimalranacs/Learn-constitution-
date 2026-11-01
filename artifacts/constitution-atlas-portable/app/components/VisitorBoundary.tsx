'use client';
import {useEffect,useState} from 'react';
export default function VisitorBoundary({children}:{children:React.ReactNode}){
 const [ready,setReady]=useState(false),[failed,setFailed]=useState(false);
 useEffect(()=>{fetch('/api/visitor',{signal:AbortSignal.timeout(10000)}).then(r=>{if(!r.ok)throw Error();setReady(true)}).catch(()=>setFailed(true));},[]);
 return <>{!ready&&<p className="fine" role="status">{failed?'Device storage is unavailable. Reading remains available; saved items may not work.':'Preparing your device workspace…'}</p>}{(ready||failed)&&children}</>;
}
