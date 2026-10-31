import {sqliteTable,text,integer,primaryKey,index} from 'drizzle-orm/sqlite-core';
export const personalRecords=sqliteTable('personal_records',{
 userId:text('user_id').notNull(),kind:text('kind').notNull(),key:text('record_key').notNull(),
 value:text('value_json').notNull(),updatedAt:integer('updated_at').notNull()
},t=>[primaryKey({columns:[t.userId,t.kind,t.key]}),index('personal_updated').on(t.userId,t.updatedAt)]);
export const aiUsage=sqliteTable('ai_usage',{
 userId:text('user_id').notNull(),day:text('day').notNull(),count:integer('count').notNull().default(0)
},t=>[primaryKey({columns:[t.userId,t.day]})]);
