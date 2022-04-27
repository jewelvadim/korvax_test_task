/* Task: Write a query to show the total count per site_id and page_id for the last two months. */

/* Solution */
SELECT site_id, page_id, COUNT(host_ip)
FROM page_views
WHERE visit_time::DATE >= (NOW() - INTERVAL '14 days')::DATE
GROUP BY site_id, page_id;
