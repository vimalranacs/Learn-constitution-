import {DatabaseSync} from 'node:sqlite';
import {mkdirSync} from 'node:fs';
import {dirname,resolve} from 'node:path';
let database;
export function getDatabase(){
 if(database)return database;
 const path=resolve(process.env.ATLAS_DATABASE_PATH||'data/atlas.sqlite');mkdirSync(dirname(path),{recursive:true});
 database=new DatabaseSync(path);database.exec(`PRAGMA journal_mode=WAL; PRAGMA busy_timeout=5000;
 CREATE TABLE IF NOT EXISTS personal_records(user_id TEXT NOT NULL,kind TEXT NOT NULL,record_key TEXT NOT NULL,value_json TEXT NOT NULL,updated_at INTEGER NOT NULL,PRIMARY KEY(user_id,kind,record_key));
 CREATE TABLE IF NOT EXISTS ai_usage(user_id TEXT NOT NULL,day TEXT NOT NULL,count INTEGER NOT NULL DEFAULT 0,PRIMARY KEY(user_id,day));
 CREATE TABLE IF NOT EXISTS login_attempts(email TEXT PRIMARY KEY,window INTEGER NOT NULL,count INTEGER NOT NULL);`);
 return database;
}
export const env={get GEMINI_API_KEY(){return process.env.GEMINI_API_KEY},get GEMINI_MODEL(){return process.env.GEMINI_MODEL||'gemini-3.1-flash-lite'},DB:{prepare(sql){return {bind(...values){return {async all(){return {results:getDatabase().prepare(sql).all(...values)}},async first(){return getDatabase().prepare(sql).get(...values)||null},async run(){return getDatabase().prepare(sql).run(...values)}}}}}};
