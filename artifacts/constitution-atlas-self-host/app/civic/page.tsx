import Shell from '../components/Shell';import CivicLab from '../components/CivicLab';import {protectPage} from '../access';
export const dynamic='force-dynamic';
export default async function Page(){await protectPage('/civic');return <Shell mode="learn"><section className="lesson"><p className="eyebrow">How India works / Civic lab</p><h1>Put an idea to work.</h1><p className="lede">Explore a public problem. Change an assumption. Follow the consequences and inspect the source.</p><CivicLab/></section></Shell>;}
