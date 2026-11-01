import knowledge from '../content/knowledge.json';
export const nodes=knowledge.nodes;
export const edges=knowledge.edges;
export const byId=new Map(nodes.map(n=>[n.id,n]));
export const sourceUrl=knowledge.sourceUrl;
export type AtlasNode=typeof nodes[number];
export type AtlasEdge=typeof edges[number];
