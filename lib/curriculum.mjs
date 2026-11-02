// Presentation only: original curriculum and source metadata stay intact.
export function cleanCurriculum(text,labels,lessonId){
 const href=id=>'/explore?selected='+encodeURIComponent(id)+(lessonId?'&lesson='+encodeURIComponent(lessonId):'');
 const plain=label=>label.replace(/[\p{Extended_Pictographic}\uFE0F\u200D]/gu,'').trim();
 let result=text.replace(/`(\[[^\]]+\]\([^)]*\/atlas\/[^)]+\))`/g,'$1').replace(/\[([^\]]+)\]\(([^\s)]+)\)/g,(all,label,url)=>{let path;try{path=new URL(url,'https://atlas.local').pathname}catch{return all}const match=path.match(/^\/atlas\/([a-zA-Z0-9_]+)\/?$/);if(!match)return all;return labels[match[1]]?'['+plain(label)+']('+href(match[1])+')':plain(label)});
 result=result.replace(/\s*\((?:PDF\s+(?:p(?:ages?)?\.?|pp\.?)|PDF\s*:)\s*[^)]+\)/gi,'');
 result=result.replace(/(?<![\w/])(https?:\/\/chatgpt\.com)?\/atlas\/([a-zA-Z0-9_]+)(?![\w])/g,(all,host,id)=>labels[id]?'['+plain(labels[id])+']('+href(id)+')':'');
 const pageCitation='(?:Official\\s+\\d{4}\\s+Constitution\\s+)?PDF\\s*,?\\s*(?:pp?\\.?|pages?)\\s*\\d+(?:\\s*[-–—,]\\s*\\d+)*(?:\\s*,?\\s*(?:fn\\.?|footnote)\\s*\\d+)*';
 result=result.replace(new RegExp('\\s*\\(\\s*'+pageCitation+'\\s*\\)','gi'),'');
 result=result.replace(new RegExp('(?:,|;)?\\s*'+pageCitation,'gi'),'').replace(/\(\s*\)/g,'');
 result=result.replace(/\s*\((?:pp?\.?|Page)\s+\d+(?:\s*[-–—,]\s*\d+)*\)/gi,'');
 const lines=result.split('\n');for(let i=0;i<lines.length;i++){if(!lines[i].trim().startsWith('|'))continue;const cells=lines[i].split('|');const remove=[];cells.forEach((cell,j)=>{if(/^\s*PDF\s+Pages?\s*$/i.test(cell))remove.push(j)});if(remove.length){for(let j=i;j<lines.length&&lines[j].trim().startsWith('|');j++){const row=lines[j].split('|');lines[j]=row.filter((_,column)=>!remove.includes(column)).join('|')}}}
 result=lines.join('\n').replace(/\s*&\s*PDF Page/g,'');
 // Link unmarked Article/Preamble mentions without touching existing links or code.
 result=result.split(/(\[[^\]]*\]\([^)]*\)|`[^`]*`)/g).map((part,i)=>i%2?part:part.replace(/\b(Preamble|Article\s+(\d+[A-Z]?))\b/g,(label,_,number)=>{const id=number?'art_'+number:'preamble';return labels[id]?'['+label+']('+href(id)+')':label})).join('');
 return result;
}

export function lessonReturnHref(id){return (id.startsWith('les_')?'/courses/':'/learn/')+encodeURIComponent(id)}
