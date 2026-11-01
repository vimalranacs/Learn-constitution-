import type {Metadata} from 'next';
import './globals.css';
import './globals-extension.css';
import './universe.css';
export const metadata:Metadata={title:'Constitution Atlas',description:'Explore the institutions and learn the architecture of Indian democracy through visible sources.'};
export default function RootLayout({children}:{children:React.ReactNode}) {return <html lang="en"><body>{children}</body></html>;}

