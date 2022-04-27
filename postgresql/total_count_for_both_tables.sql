/*
Task: Write a query to show the total count per site_id and page_id
for the last two months until now, using the the both big and pre-aggregated tables.
*/

/* Solution: */
SELECT
	site_id,
    page_id,
    COUNT(host_ip) + (
    	SELECT COALESCE(SUM(visits_count), 0)
      	FROM daily_page_visits
      	WHERE
      		daily_page_visits.site_id = page_views.site_id AND
      		daily_page_visits.page_id = page_views.page_id AND
      		report_date::DATE > (NOW() - INTERVAL '14 days')::DATE and
      		report_date::DATE < NOW()::DATE
      	GROUP BY daily_page_visits.site_id, daily_page_visits.page_id
    )
FROM page_views
WHERE visit_time::DATE = NOW()::DATE
GROUP BY site_id, page_id;
