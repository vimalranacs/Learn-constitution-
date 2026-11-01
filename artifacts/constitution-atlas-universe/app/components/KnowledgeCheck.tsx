'use client';
import {useState} from 'react';
import {parliamentLesson as lesson} from '../../content/lesson';
export default function KnowledgeCheck() {
  const [selected,setSelected]=useState<number|null>(null);
  const [checked,setChecked]=useState(false);
  return <section className="check" aria-labelledby="check-title"><span className="eyebrow">Pause & reason</span><h2 id="check-title">Check the distinction</h2><p>{lesson.question}</p><fieldset><legend className="sr-only">Choose a correction</legend>{lesson.answers.map((answer,i)=><label key={i}><input type="radio" name="answer" checked={selected===i} onChange={()=>{setSelected(i);setChecked(false);}}/>{answer.text}</label>)}</fieldset><button disabled={selected===null} onClick={()=>setChecked(true)}>Check reasoning</button><div aria-live="polite">{checked&&selected!==null&&<p className="feedback">{lesson.answers[selected].feedback}</p>}</div><p className="fine">Practice works without AI. This early slice does not save answers or infer mastery.</p></section>;
}
