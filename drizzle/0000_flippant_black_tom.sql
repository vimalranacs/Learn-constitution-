CREATE TABLE `ai_usage` (
	`user_id` text NOT NULL,
	`day` text NOT NULL,
	`count` integer DEFAULT 0 NOT NULL,
	PRIMARY KEY(`user_id`, `day`)
);
--> statement-breakpoint
CREATE TABLE `personal_records` (
	`user_id` text NOT NULL,
	`kind` text NOT NULL,
	`record_key` text NOT NULL,
	`value_json` text NOT NULL,
	`updated_at` integer NOT NULL,
	PRIMARY KEY(`user_id`, `kind`, `record_key`)
);
--> statement-breakpoint
CREATE INDEX `personal_updated` ON `personal_records` (`user_id`,`updated_at`);