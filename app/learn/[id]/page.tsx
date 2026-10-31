import {notFound} from 'next/navigation';
import Link from 'next/link';
import Shell from '../../components/Shell';
import Composition from '../../components/Composition';
import KnowledgeCheck from '../../components/KnowledgeCheck';
import Source from '../../components/Source';
import {protectPage} from '../../access';
import {parliamentLesson as lesson} from '../../../content/lesson';
export const dynamic='force-dynamic';
export default async function Learn({params}:{params:Promise<{id:string}>}) {
  const {id}=await params; await protectPage(`/learn/${id}`); if(id!==lesson.id) notFound();
  return <Shell mode="learn"><article className="lesson"><div className="crumb"><Link href="/">Home</Link> / Learn / An introduction</div><p className="eyebrow">A first constitutional connection · About 5 minutes</p><h1>{lesson.title}</h1><p className="lede">{lesson.subtitle}</p><div className="objectives"><h2>By the end, you can…</h2><ul>{lesson.objectives.map(x=><li key={x}>{x}</li>)}</ul><p className="fine">No prior constitutional knowledge required.</p></div>{lesson.sections.map((s,i)=><section key={s.title} className="lesson-section"><span className="section-number">0{i+1}</span><h2>{s.title}</h2><p>{s.text}</p></section>)}<Composition/><Link className="text-link" href="/atlas/art_79">Inspect this connection in Atlas →</Link><Source/><KnowledgeCheck/><section className="recap"><p className="eyebrow">Take this with you</p><h2>Whole institution ≠ one House.</h2><p>{lesson.recap}</p></section><p className="release-note">Next in development: representation and the different functions of Parliament’s components. This is one introductory lesson; the complete beginner course is not yet available. Saved progress and the tutor are not enabled in this slice.</p></article></Shell>;
}
