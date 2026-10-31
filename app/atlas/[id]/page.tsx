import {notFound} from 'next/navigation';
import Link from 'next/link';
import Shell from '../../components/Shell';
import Composition from '../../components/Composition';
import Source from '../../components/Source';
import {protectPage} from '../../access';
import data from '../../../content/parliament.json';
export const dynamic='force-dynamic';
export default async function Atlas({params}:{params:Promise<{id:string}>}) {
  const {id}=await params; await protectPage(`/atlas/${id}`);
  if(!['art_79','inst_parliament'].includes(id)) notFound();
  return <Shell mode="atlas"><section className="atlas-page"><div className="crumb"><Link href="/">Home</Link> / Atlas / The Union</div><div className="page-heading"><div><p className="eyebrow">Institution / Parliament of India</p><h1>The whole and its parts.</h1><p className="lede">Begin with composition. Then ask what each part can do.</p></div><Link className="button secondary" href="/learn/parliament-composition">Learn this concept →</Link></div><div className="atlas-grid"><section className="map"><div className="map-heading"><h2>Parliament</h2><span>Article 79</span></div><Composition/><p className="map-note">Every connection here means “consists of”; none implies a chain of command.</p></section><aside className="inspector"><p className="eyebrow">Read the source</p><h2>Constitution of Parliament</h2><span className="status">Source passage checked</span><blockquote>{data.article.text}</blockquote><p className="fine">Edition of 1 May 2026 · Article 79</p><Source/></aside></div><section className="boundary"><h2>Composition is only the starting point.</h2><p>Article 79 identifies the components of Parliament. It does not by itself explain elections, lawmaking, ministerial responsibility, or every limit on power. Those require additional provisions and their own source review.</p><Link href="/learn/parliament-composition">Build the distinction in Learn →</Link></section></section></Shell>;
}
