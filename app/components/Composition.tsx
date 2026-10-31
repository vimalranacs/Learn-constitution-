export default function Composition() {
  return <figure className="composition"><svg viewBox="0 0 780 250" role="img" aria-labelledby="graph-title graph-description">
    <title id="graph-title">Composition of Parliament under Article 79</title><desc id="graph-description">Parliament consists of the President, Council of States and House of the People. Lines indicate composition, not command.</desc>
    <path d="M390 77 V120 M135 120 H645 M135 120 V160 M390 120 V160 M645 120 V160" fill="none" stroke="#7c9995" strokeWidth="2"/>
    <rect x="280" y="15" width="220" height="62" rx="8" fill="#285f62"/><text x="390" y="53" textAnchor="middle" fill="white" fontSize="21">Parliament</text>
    <rect x="327" y="104" width="126" height="30" rx="8" fill="#f1f3f0"/><text x="390" y="125" textAnchor="middle" fill="#285f62" fontSize="16">consists of</text>
    {[{x:25,label:'President'}, {x:280,label:'Council of States'}, {x:535,label:'House of the People'}].map(n=><g key={n.label}><rect x={n.x} y="160" width="220" height="72" rx="8" fill="white" stroke="#c5d3cf"/><text x={n.x+110} y="201" textAnchor="middle" fill="#202b30" fontSize="18">{n.label}</text></g>)}
    </svg><figcaption>Article 79 · Composition, not a chain of command.</figcaption><details><summary>Read as a list</summary><p>Parliament consists of:</p><ul><li>The President</li><li>The Council of States</li><li>The House of the People</li></ul></details></figure>;
}
