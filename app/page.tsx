import Link from 'next/link';
import Shell from './components/Shell';
import {protectPage} from './access';
export const dynamic='force-dynamic';
export default async function Home() {
  await protectPage('/');
  return <Shell mode="atlas"><section className="welcome"><p className="eyebrow">Explore the architecture of Indian democracy</p><h1>A clearer view<br/>of how India works.</h1><p className="lede">Follow the institutions. Read the sources. Build your understanding, one connection at a time.</p><div className="entry-options"><Link href="/atlas/art_79"><span className="eyebrow">01 / Explore</span><h2>Open the Atlas <span>↗</span></h2><p>Start with Parliament and the constitutional rule that brings its parts together.</p></Link><Link href="/learn/parliament-composition"><span className="eyebrow">02 / Understand</span><h2>Begin learning <span>→</span></h2><p>A short guided introduction. One idea, a visual explanation, and a question to think through.</p></Link></div><p className="release-note">First working slice: Parliament under Article 79. The wider Atlas and fifteen-lesson beginner course are being built in tested phases.</p></section></Shell>;
}
