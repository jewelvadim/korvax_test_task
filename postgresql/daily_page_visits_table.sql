/*
Task: Create a table (daily_page_visits) for holding daily pre-aggregated data
for the page visits count, grouped by site_id, page_id and day;
*/

/* Solution */
CREATE TABLE daily_page_visits (site_id int, page_id int, visits_count int, report_date date default now());
CREATE INDEX report_date_idx ON daily_page_visits (report_date);
