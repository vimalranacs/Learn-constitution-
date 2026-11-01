import React, { useEffect, useState } from 'react';
import { useAtlasStore } from './store/useAtlasStore';

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000/api';

export default function App() {
  const {
    activeNodeId,
    depthLevel,
    activeTab,
    searchQuery,
    setActiveNode,
    setDepthLevel,
    setActiveTab,
    setSearchQuery,
  } = useAtlasStore();

  const [nodeDetail, setNodeDetail] = useState<any>(null);
  const [searchResults, setSearchResults] = useState<any[]>([]);
  const [aiQuestion, setAiQuestion] = useState('');
  const [aiResponse, setAiResponse] = useState<any>(null);

  useEffect(() => {
    fetch(`${API_BASE}/nodes/${activeNodeId}`)
      .then((r) => r.json())
      .then(setNodeDetail)
      .catch(console.error);
  }, [activeNodeId]);

  useEffect(() => {
    if (!searchQuery.trim()) {
      setSearchResults([]);
      return;
    }
    fetch(`${API_BASE}/search?q=${encodeURIComponent(searchQuery)}`)
      .then((r) => r.json())
      .then((d) => setSearchResults(d.results || []))
      .catch(console.error);
  }, [searchQuery]);

  const askAi = async () => {
    if (!aiQuestion.trim()) return;
    const res = await fetch(`${API_BASE}/ai/ask`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        question: aiQuestion,
        active_node_id: activeNodeId,
        depth_level: depthLevel,
      }),
    });
    setAiResponse(await res.json());
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
      <header className="border-b border-amber-500/20 bg-slate-900/90 px-6 py-3 flex items-center justify-between">
        <div>
          <h1 className="text-xl font-serif font-bold text-amber-400 tracking-wide">
            CONSTITUTION ATLAS
          </h1>
          <p className="text-xs text-slate-400">
            Explore the Architecture of Indian Democracy • 402-Page Official 2026 Edition
          </p>
        </div>
        <div className="flex items-center gap-3">
          <input
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search 470 Articles, Parts, Judgments, Doctrines..."
            className="bg-slate-800 border border-slate-700 rounded-lg px-3 py-1.5 text-sm w-80"
          />
          <select
            value={depthLevel}
            onChange={(e) => setDepthLevel(e.target.value as any)}
            className="bg-slate-800 border border-slate-700 rounded-lg px-3 py-1.5 text-sm"
          >
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
            <option value="research">Research</option>
          </select>
        </div>
      </header>
      <main className="flex-1 grid grid-cols-12 gap-4 p-4">
        <section className="col-span-8 bg-slate-900 rounded-xl border border-slate-800 p-4">
          {nodeDetail?.node && (
            <div>
              <span className="text-xs uppercase px-2 py-0.5 rounded bg-amber-500/20 text-amber-300">
                {nodeDetail.node.node_type} • {nodeDetail.node.code}
              </span>
              <h2 className="text-2xl font-serif font-bold mt-2">{nodeDetail.node.title}</h2>
              <p className="text-slate-300 mt-3">
                {nodeDetail.node.explanations?.[depthLevel] || nodeDetail.node.summary}
              </p>
              <pre className="mt-4 p-4 bg-slate-950 rounded-lg text-xs text-slate-300 whitespace-pre-wrap max-h-96 overflow-y-auto">
                {nodeDetail.node.full_text}
              </pre>
            </div>
          )}
        </section>
        <aside className="col-span-4 bg-slate-900 rounded-xl border border-slate-800 p-4 flex flex-col gap-4">
          <h3 className="font-semibold text-amber-400">Connected Constitutional Nodes</h3>
          <div className="space-y-2 max-h-64 overflow-y-auto">
            {nodeDetail?.neighbors?.map((nb: any, idx: number) => (
              <button
                key={idx}
                onClick={() => setActiveNode(nb.node.id)}
                className="w-full text-left p-2 rounded bg-slate-800/70 hover:bg-slate-800 text-xs"
              >
                <div className="font-medium text-slate-200">{nb.node.title}</div>
                <div className="text-amber-400/90">{nb.edge.type} ({nb.edge.ref})</div>
                <div className="text-slate-400 mt-0.5">{nb.edge.explanation}</div>
              </button>
            ))}
          </div>
          <div className="border-t border-slate-800 pt-3">
            <h3 className="font-semibold text-amber-400 mb-2">Gemini Constitutional Research AI</h3>
            <div className="flex gap-2">
              <input
                value={aiQuestion}
                onChange={(e) => setAiQuestion(e.target.value)}
                placeholder="Ask a constitutional question..."
                className="flex-1 bg-slate-800 border border-slate-700 rounded px-2 py-1 text-xs"
              />
              <button onClick={askAi} className="bg-amber-500 text-slate-950 px-3 py-1 rounded text-xs font-bold">
                Ask
              </button>
            </div>
            {aiResponse && (
              <div className="mt-3 text-xs text-slate-300 whitespace-pre-wrap max-h-56 overflow-y-auto bg-slate-950 p-3 rounded">
                {aiResponse.answer}
              </div>
            )}
          </div>
        </aside>
      </main>
    </div>
  );
}
