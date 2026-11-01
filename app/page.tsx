
import Shell from './components/Shell';
import {protectPage} from './access';
export const dynamic='force-dynamic';
export default async function Home() {
  await protectPage('/');
  return <Shell mode="atlas"><section className="welcome"><p className="eyebrow">Explore the architecture of Indian democracy</p><h1>A clearer view<br/>of how India works.</h1><p className="lede">Follow the institutions. Read the sources. Build your understanding, one connection at a time.</p><div className="entry-options"><a href="/atlas"><span className="eyebrow">01 / Explore</span><h2>Open the Atlas <span>↗</span></h2><p>Explore Articles, institutions and ideas. Inspect the source and the review status behind each connection.</p></a><a href="/learn"><span className="eyebrow">02 / Understand</span><h2>Begin learning <span>→</span></h2><p>Fifteen foundational lessons, worked examples, reasoning checks and a private place to save your progress.</p></a></div><p className="release-note">Explore with sources in view. Read our methodology for the distinction between constitutional text, educational commentary and reviewed evidence.</p></section></Shell>;
}
