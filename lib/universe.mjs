export const universeCategories=[
 ['realm:articles','Articles','book','Explore constitutional provisions by Part, then unfold their connections.'],
 ['realm:amendments','Amendments','amend','Explore the available amendment records and their constitutional connections. This is a curated collection, not an exhaustive amendment history.'],
 ['realm:schedules','Schedules','layers','Explore the twelve Schedules and the provisions connected to them.'],
 ['realm:judgments','Judgments','scale','Explore recorded judgments and doctrines. Read each source and review status before drawing a legal conclusion.'],
 ['realm:history','History','clock','Explore constitutional origins and the events represented in this collection.'],
 ['realm:drafting','Drafting','pen','Follow the Constituent Assembly, drafting and the ideas behind the document.'],
 ['realm:preamble','Preamble','scroll','Begin with the Preamble and follow its connections to constitutional ideas.'],
 ['realm:parts','Parts','parts','Explore the available Parts of the Constitution and their Articles.'],
];
export function createUniverse(nodes,edges){
 const map=new Map(nodes.map(n=>[n.id,n]));
 for(const [id,title,icon,summary] of universeCategories)map.set(id,{id,title,icon,summary,type:'Browsing theme',category:'Theme',status:'group'});
 const parts=nodes.filter(n=>n.category==='Part').sort((a,b)=>(a.page??999)-(b.page??999)).map(n=>n.id);
 const groups=new Map([
 ['const_india',universeCategories.map(c=>c[0])],['realm:articles',parts],['realm:parts',parts],
 ['realm:amendments',nodes.filter(n=>n.id.startsWith('amend_')||n.id==='art_368').map(n=>n.id)],
 ['realm:schedules',nodes.filter(n=>n.category==='Schedule').map(n=>n.id)],
 ['realm:judgments',nodes.filter(n=>n.type==='Judicial').map(n=>n.id)],
 ['realm:history',nodes.filter(n=>n.type==='Historical').map(n=>n.id)],
 ['realm:drafting',nodes.filter(n=>['hist_const_assembly','hist_drafting_comm','hist_obj_resolution','hist_goi_1935'].includes(n.id)).map(n=>n.id)],
 ['realm:preamble',['preamble',...nodes.filter(n=>n.type==='Philosophical').map(n=>n.id)]]]);
 for(const id of parts)groups.set(id,nodes.filter(n=>n.category==='Article'&&n.part===id).sort((a,b)=>(a.page??999)-(b.page??999)||a.id.localeCompare(b.id,undefined,{numeric:true})).map(n=>n.id));
 const neighbors=new Map();for(const edge of edges){for(const [a,b] of [[edge.source,edge.target],[edge.target,edge.source]]){if(!neighbors.has(a))neighbors.set(a,[]);if(!neighbors.get(a).includes(b))neighbors.get(a).push(b)}}
 return {map,groups,neighbors,edges};
}
export function childrenOf(model,id){return model.groups.get(id)||model.neighbors.get(id)||[]}
export function universeGraph(model,opened,extra=[],relationships=true){
 const visible=new Set(['const_india',...extra]);const queue=['const_india',...extra];const grouping=[];const used=new Set();let clipped=false;
 while(queue.length){const id=queue.shift();if(used.has(id))continue;used.add(id);const count=opened[id]||0;const children=childrenOf(model,id).slice(0,count);for(const child of children){if(!model.map.has(child))continue;if(visible.size>=140&&!visible.has(child)){clipped=true;continue}if(model.groups.has(id))grouping.push(model.edges.find(e=>e.source===id&&e.target===child&&e.type==='CONTAINS')||{id:'group:'+id+':'+child,source:id,target:child,type:'BROWSING_GROUP',status:'group'});if(!visible.has(child)){visible.add(child);queue.push(child)}else if(!used.has(child))queue.push(child)}}
 const links=[...grouping,...model.edges.filter(e=>visible.has(e.source)&&visible.has(e.target)&&(relationships||!model.groups.has(e.source)))];
 const dedup=new Map(links.map(e=>[e.id,e]));return {nodes:[...visible].map(id=>model.map.get(id)).filter(Boolean),edges:[...dedup.values()],clipped};
}
export function nodeRadius(n){return n.id==='const_india'?104:n.category==='Theme'?72:n.category==='Part'?55:45}
export function shortTitle(n){if(n.id==='const_india')return ['Constitution','of India'];if(n.category==='Article')return ['Art. '+n.id.slice(4)];if(n.category==='Part')return ['Part '+n.id.slice(5)];if(n.category==='Schedule')return ['Schedule '+n.id.slice(6)];const title=n.title.replace(/\([^)]*\)/g,'').trim();const words=title.split(/\s+/),lines=[];let line='';for(const word of words){if((line+' '+word).trim().length>18){if(line)lines.push(line);line=word}else line=(line+' '+word).trim()}if(line)lines.push(line);return lines.length>2?[lines[0],lines[1].slice(0,16)+'…']:lines}
export function linkCurve(a,b){const dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy)||1;const sx=a.x+dx/d*a.r,sy=a.y+dy/d*a.r,tx=b.x-dx/d*b.r,ty=b.y-dy/d*b.r;const bend=Math.min(95,d*.15);return `M${sx},${sy} C${sx+dx*.33-dy/d*bend},${sy+dy*.33+dx/d*bend} ${tx-dx*.33-dy/d*bend},${ty-dy*.33+dx/d*bend} ${tx},${ty}`}

// Deterministic collision projection: preserve the map's shape while opening breathing room.
export function spaceUniverse(points,gap=46,anchor='const_india',options={}){
 const result=points.map(p=>({...p})),pinned=new Set([anchor,...(options.pin?[options.pin]:[])]);
 const area=result.reduce((sum,p)=>sum+Math.PI*(p.r+gap/2)**2,0),xs=result.map(p=>p.x),ys=result.map(p=>p.y);
 const density=area/Math.max(1,(Math.max(...xs)-Math.min(...xs)+180)*(Math.max(...ys)-Math.min(...ys)+180));
 const clearance=gap+Math.min(18,Math.max(0,density-.55)*14);
 // Move crowded families together first, so connected branches keep their shape.
 if(options.branches){for(let pass=0;pass<5;pass++){const shifts=new Map();for(let i=0;i<result.length;i++)for(let j=i+1;j<result.length;j++){
 const a=result[i],b=result[j],ba=options.branches[a.id],bb=options.branches[b.id];if(!ba||!bb||ba===bb||pinned.has(a.id)||pinned.has(b.id))continue;
 const d=Math.hypot(b.x-a.x,b.y-a.y),overlap=a.r+b.r+clearance-d;if(overlap<=0)continue;const angle=d>.01?Math.atan2(b.y-a.y,b.x-a.x):(i+j)*2.399;
 for(const [branch,sign] of [[ba,-1],[bb,1]]){const v=shifts.get(branch)||{x:0,y:0,count:0};v.x+=Math.cos(angle)*overlap*.55*sign;v.y+=Math.sin(angle)*overlap*.55*sign;v.count++;shifts.set(branch,v)}}
 for(const p of result){if(pinned.has(p.id))continue;const v=shifts.get(options.branches[p.id]);if(v){p.x+=v.x/Math.sqrt(v.count);p.y+=v.y/Math.sqrt(v.count)}}}}
 for(let pass=0;pass<(options.iterations||1200);pass++){let moved=false;for(let i=0;i<result.length;i++)for(let j=i+1;j<result.length;j++){
 const a=result[i],b=result[j];let dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy);const min=a.r+b.r+clearance;
 if(d>=min-.01)continue;const af=pinned.has(a.id),bf=pinned.has(b.id);if(af&&bf)continue;if(d<.001){const angle=(i*2.399+j)*1.618;dx=Math.cos(angle);dy=Math.sin(angle);d=1}const amount=min-d+.1,ux=dx/d,uy=dy/d;
 a.x-=ux*amount*(af?0:bf?1:.5);a.y-=uy*amount*(af?0:bf?1:.5);b.x+=ux*amount*(bf?0:af?1:.5);b.y+=uy*amount*(bf?0:af?1:.5);moved=true;
 }if(!moved)break}return result;
}
export function universeBranches(model,visibleIds){
 const visible=new Set(visibleIds),branches={},queue=['const_india'],seen=new Set(queue);
 while(queue.length){const id=queue.shift();for(const child of childrenOf(model,id)){if(!visible.has(child)||seen.has(child))continue;seen.add(child);branches[child]=id==='const_india'?child:branches[id];queue.push(child)}}return branches;
}

// Fit every circle inside the usable viewport, excluding fixed page controls.
export function frameUniverse(points,width,height,inspector=false){
 if(!points.length||width<=0||height<=0)return {x:width/2,y:height/2,k:.5};
 const mobile=width<=760,left=mobile?22:70,right=mobile?22:inspector?350:50,top=mobile?180:205,bottom=mobile&&inspector?355:110;
 const usableW=Math.max(80,width-left-right),usableH=Math.max(80,height-top-bottom);
 const x1=Math.min(...points.map(p=>p.x-p.r-16)),x2=Math.max(...points.map(p=>p.x+p.r+16)),y1=Math.min(...points.map(p=>p.y-p.r-16)),y2=Math.max(...points.map(p=>p.y+p.r+16));
 const k=Math.min(1.15,usableW/Math.max(1,x2-x1),usableH/Math.max(1,y2-y1));
 return {x:left+usableW/2-(x1+x2)/2*k,y:top+usableH/2-(y1+y2)/2*k,k};
}
