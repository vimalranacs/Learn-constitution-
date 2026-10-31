'use client';
export default function ErrorPage({reset}:{error:Error;reset:()=>void}){return <main className="lesson"><p className="eyebrow">Something interrupted this page</p><h1>Let’s try that again.</h1><p>Your saved records remain in your private workspace. If this persists, check the connection and sign in again.</p><button onClick={reset}>Retry page</button> <a href="/">Return home</a></main>;}

