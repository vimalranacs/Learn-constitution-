import data from '../../content/parliament.json';
export default function Source() {
  return <details className="source"><summary>Source & review scope <span>Article 79 · PDF p. 67</span></summary><p><a href={`${data.source.url}#page=67`} target="_blank" rel="noreferrer">Open the Legislative Department PDF ↗</a></p><p>{data.source.publisher}. Edition: {data.source.edition}. PDF page 67 (file page, not printed page number).</p><p>{data.source.method} Reviewed {data.source.reviewed}.</p><p>Educational explanations and the diagram are editorial interpretations of this passage. The original extraction added an “Article” prefix; the displayed passage removes that prefix.</p></details>;
}
