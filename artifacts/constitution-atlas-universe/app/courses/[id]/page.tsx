import {notFound} from 'next/navigation';import Shell from '../../components/Shell';import EcosystemReader from '../../components/EcosystemReader';import data from '../../../content/ecosystem.json';
export const dynamic='force-dynamic';
export default async function Page({params}:{params:Promise<{id:string}>}){const {id}=await params;const lesson=data.lessons.find(l=>l.id===id);if(!lesson)notFound();return <Shell mode="learn"><EcosystemReader lesson={lesson}/></Shell>}
