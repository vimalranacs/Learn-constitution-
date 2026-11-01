import {notFound} from 'next/navigation';import Shell from '../../components/Shell';import LessonReader from '../../components/LessonReader';import {course,lessonsById,type Lesson} from '../../../content/course';import {parliamentLesson} from '../../../content/lesson';import {byId,sourceUrl} from '../../../lib/knowledge';import {protectPage} from '../../access';
export const dynamic='force-dynamic';
export default async function Learn({params}:{params:Promise<{id:string}>}){
 const {id}=await params;await protectPage('/learn/'+id);let lesson:Lesson|undefined=lessonsById.get(id);
 if(id==='parliament-composition')lesson={id,title:parliamentLesson.title,objective:parliamentLesson.subtitle,sources:['art_79'],hook:parliamentLesson.sections[0].text,explanation:parliamentLesson.sections[2].text,example:parliamentLesson.sections[3].text,question:parliamentLesson.question,options:parliamentLesson.answers.map(x=>x.text),correct:0,feedback:parliamentLesson.answers[0].feedback,recap:parliamentLesson.recap,prerequisites:[]};
 if(!lesson)notFound();const index=course.findIndex(l=>l.id===id);
 const sources=lesson.sources.map(id=>{const n=byId.get(id);return {id,title:n?.title||id,page:n?.page||null,url:sourceUrl}});
 return <Shell mode="learn"><LessonReader key={id} lesson={lesson} sources={sources} previous={index>0?course[index-1].id:undefined} next={index>=0?course[index+1]?.id:undefined}/></Shell>;
}
