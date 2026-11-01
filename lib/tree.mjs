export function compactLabel(node){if(node.category==='Article')return node.id.replace('art_','Art. ');if(node.category==='Part')return node.id.replace('part_','Part ');const title=node.title.replace(/\s*\([^)]*\)/g,'');return title.length>30?title.slice(0,27)+'…':title}
export function treeModel(nodes,organization='structure'){
 const root='const_india',map=new Map(nodes.map(n=>[n.id,{...n,label:compactLabel(n)}])),children=new Map(),parent=new Map();
 const add=(p,id)=>{if(!children.has(p))children.set(p,[]);children.get(p).push(id);parent.set(id,p)};
 const group=(id,title,p=root)=>{map.set(id,{id,title,label:title,type:'Teaching group',category:'Group',summary:'A browsing group, not a relationship of legal authority.'});add(p,id)};
 if(organization==='structure'){
 group('group:parts','Constitutional Parts');group('group:schedules','Schedules');
 for(const n of nodes){if(n.category==='Part')add('group:parts',n.id);else if(n.category==='Schedule')add('group:schedules',n.id);else if(n.id==='preamble')add(root,n.id)}
 for(const n of nodes)if(n.category==='Article'&&map.has(n.part))add(n.part,n.id);
 }else{
 for(const type of ['Constitutional','Institutional','Judicial','Philosophical','Historical','Administrative']){const id='group:'+type;group(id,type==='Constitutional'?'Constitutional text':type+' themes');for(const n of nodes)if(n.type===type&&n.id!==root){if(type==='Constitutional'&&n.category==='Article')continue;add(id,n.id)}}
 }
 return {root,map,children,parent};
}
export function visibleTree(model,expanded,limit=100){
 const items=[],links=[];let leaves=0,truncated=false;
 function visit(id,depth){if(items.length>=limit){truncated=true;return null}const item={...model.map.get(id),depth,x:0,y:-depth*160};items.push(item);const kids=expanded.has(id)?model.children.get(id)||[]:[];const positions=[];for(const child of kids){const p=visit(child,depth+1);if(p){links.push({id:'tree:'+id+':'+child,source:id,target:child,type:'BROWSING_GROUP'});positions.push(p.x)}}item.x=positions.length?(positions[0]+positions[positions.length-1])/2:leaves++*175;return item}
 visit(model.root,0);return {nodes:items,edges:links,truncated};
}
export function ancestors(model,id){const result=[];const seen=new Set();while(model.parent.has(id)&&!seen.has(id)){seen.add(id);id=model.parent.get(id);result.push(id)}return result}
