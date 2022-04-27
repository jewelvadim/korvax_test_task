/*
Task: Create a function for populating the pre-aggregated table every hour
(you can use a helper table to hold the last update time);
*/

/* Solution */
CREATE TABLE last_update (update_timestamp timestamp default now());

