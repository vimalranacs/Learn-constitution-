import Shell from '../components/Shell';
import Workspace from '../components/Workspace';
import {protectPage} from '../access';
export const dynamic='force-dynamic';
export default async function Page(){await protectPage('/workspace');return <Shell mode="learn"><section className="atlas-page"><p className="eyebrow">Your personal library</p><h1>A place to return to.</h1><p className="lede">Private notes, bookmarks, learning progress and review. Stored under your signed-in identity.</p><Workspace/></section></Shell>;}
