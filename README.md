# Test task for KORVAX

## Postgresql:

We have the following table:

CREATE TABLE page_views (
    site_id int,
    page_id int,
    host_ip inet,
    visit_time timestamp default now()
);
CREATE INDEX site_id_idx ON page_views (site_id);
CREATE INDEX visit_time_idx ON page_views USING BRIN (view_time);

Task:
1. Write a query to show the total count per site_id and page_id for the last two months.
2. Create a table (daily_page_visits) for holding daily pre-aggregated data for the page visits count, grouped by site_id, page_id and day;
3. Create a function for populating the pre-aggregated table every hour (you can use a helper table to holld the last update time);
4. Write a query to show the total count per site_id and page_id for the last two months until now, using the the both big and pre-aggregated tables.

## Python:
5. Write a function with one parameter of type string, that returns a list containing the characters of the paramater. 
If a character in the string is a space or a digit greater than 5, remove them and do not include them in the array.
    ```python
    def str_to_list(param):
        # todo: write the logic
    ```

6. Write a function to convert Roman numerals to integers.
    ```python
    def convert(param):
        # todo: write the logic
    ```