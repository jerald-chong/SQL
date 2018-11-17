Question 1: Using the function you found in the websites above, write a query that will output one column with the original created_at time stamp from each row in the completed_tests table, and another column with a number that represents the day of the week associated with each of those time stamps. Limit your output to 200 rows starting at row 50.
%%sql
SELECT created_at, DAYOFWEEK(created_at) 
FROM complete_tests
LIMIT 49,200;

Question 2: Include a CASE statement in the query you wrote in Question 1 to output a third column that provides the weekday name (or an appropriate abbreviation) associated with each created_at time stamp.
%%sql
SELECT created_at, DAYOFWEEK(created_at), 
(CASE
WHEN DAYOFWEEK(created_at)=1 THEN 'Sun'
WHEN DAYOFWEEK(created_at)=2 THEN 'Mon'
WHEN DAYOFWEEK(created_at)=3 THEN 'Tue'
WHEN DAYOFWEEK(created_at)=4 THEN 'Wed'
WHEN DAYOFWEEK(created_at)=5 THEN 'Thu'
WHEN DAYOFWEEK(created_at)=6 THEN 'Fri'
WHEN DAYOFWEEK(created_at)=7 THEN 'Sat'
END) AS daylabel
FROM complete_tests
LIMIT 49,200;

Question 3: Adapt the query you wrote in Question 2 to report the total number of tests completed on each weekday. Sort the results by the total number of tests completed in descending order. You should get a total of 33,190 tests in the Sunday row of your output.
%%sql
SELECT COUNT(created_at) AS numtests, DAYOFWEEK(created_at),
(CASE
WHEN DAYOFWEEK(created_at)=1 THEN 'Sun'
WHEN DAYOFWEEK(created_at)=2 THEN 'Mon'
WHEN DAYOFWEEK(created_at)=3 THEN 'Tue'
WHEN DAYOFWEEK(created_at)=4 THEN 'Wed'
WHEN DAYOFWEEK(created_at)=5 THEN 'Thu'
WHEN DAYOFWEEK(created_at)=6 THEN 'Fri'
WHEN DAYOFWEEK(created_at)=7 THEN 'Sat'
END) AS daylabel
FROM complete_tests
GROUP BY daylabel
ORDER BY numtests DESC;

Question 4: Rewrite the query in Question 3 to exclude the dog_guids that have a value of "1" in the exclude column (Hint: this query will require a join.) This time you should get a total of 31,092 tests in the Sunday row of your output.
%%sql
SELECT COUNT(c.created_at) AS numtests, DAYOFWEEK(c.created_at),
(CASE
WHEN DAYOFWEEK(c.created_at)=1 THEN 'Sun'
WHEN DAYOFWEEK(c.created_at)=2 THEN 'Mon'
WHEN DAYOFWEEK(c.created_at)=3 THEN 'Tue'
WHEN DAYOFWEEK(c.created_at)=4 THEN 'Wed'
WHEN DAYOFWEEK(c.created_at)=5 THEN 'Thu'
WHEN DAYOFWEEK(c.created_at)=6 THEN 'Fri'
WHEN DAYOFWEEK(c.created_at)=7 THEN 'Sat'
END) AS daylabel
FROM complete_tests c JOIN dogs d
ON c.dog_guid=d.dog_guid
WHERE d.exclude=0 OR d.exclude IS NULL
GROUP BY daylabel
ORDER BY numtests DESC;

Question 5: Write a query to retrieve all the dog_guids for users common to the dogs and users table using the traditional inner join syntax (your output will have 950,331 rows).
%%sql
SELECT dog_guid
FROM dogs d JOIN users u
ON d.user_guid=u.user_guid;

Question 6: Write a query to retrieve all the distinct dog_guids common to the dogs and users table using the traditional inner join syntax (your output will have 35,048 rows).
%%sql
SELECT DISTINCT dog_guid
FROM dogs d JOIN users u
ON d.user_guid=u.user_guid;

Question 7: Start by writing a query that retrieves distinct dog_guids common to the dogs and users table, excuding dog_guids and user_guids with a "1" in their respective exclude columns (your output will have 34,121 rows).
%%sql
SELECT DISTINCT dog_guid
FROM dogs d JOIN users u
ON d.user_guid=u.user_guid
WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL);

Question 8: Now adapt your query from Question 4 so that it inner joins on the result of the subquery you wrote in Question 7 instead of the dogs table. This will give you a count of the number of tests completed on each day of the week, excluding all of the dog_guids and user_guids that the Dognition team flagged in the exclude columns.
%%sql
SELECT COUNT(c.created_at) AS numtests, DAYOFWEEK(c.created_at),
(CASE
WHEN DAYOFWEEK(c.created_at)=1 THEN 'Sun'
WHEN DAYOFWEEK(c.created_at)=2 THEN 'Mon'
WHEN DAYOFWEEK(c.created_at)=3 THEN 'Tue'
WHEN DAYOFWEEK(c.created_at)=4 THEN 'Wed'
WHEN DAYOFWEEK(c.created_at)=5 THEN 'Thu'
WHEN DAYOFWEEK(c.created_at)=6 THEN 'Fri'
WHEN DAYOFWEEK(c.created_at)=7 THEN 'Sat'
END) AS daylabel
FROM complete_tests c JOIN (SELECT DISTINCT dog_guid
                            FROM dogs d JOIN users u
                            ON d.user_guid=u.user_guid
                            WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)) AS dogs_cleaned
ON c.dog_guid=dogs_cleaned.dog_guid
GROUP BY daylabel
ORDER BY numtests DESC;

Question 9: Adapt your query from Question 8 to provide a count of the number of tests completed on each weekday of each year in the Dognition data set. Exclude all dog_guids and user_guids with a value of "1" in their exclude columns. Sort the output by year in ascending order, and then by the total number of tests completed in descending order. 
%%sql
SELECT COUNT(c.created_at) AS numtests, DAYOFWEEK(c.created_at) AS dayasnum, YEAR(c.created_at) AS year,
(CASE
WHEN DAYOFWEEK(c.created_at)=1 THEN 'Sun'
WHEN DAYOFWEEK(c.created_at)=2 THEN 'Mon'
WHEN DAYOFWEEK(c.created_at)=3 THEN 'Tue'
WHEN DAYOFWEEK(c.created_at)=4 THEN 'Wed'
WHEN DAYOFWEEK(c.created_at)=5 THEN 'Thu'
WHEN DAYOFWEEK(c.created_at)=6 THEN 'Fri'
WHEN DAYOFWEEK(c.created_at)=7 THEN 'Sat'
END) AS daylabel
FROM complete_tests c JOIN (SELECT DISTINCT dog_guid
                            FROM dogs d JOIN users u
                            ON d.user_guid=u.user_guid
                            WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)) AS dogs_cleaned
ON c.dog_guid=dogs_cleaned.dog_guid
GROUP BY year, daylabel
ORDER BY year ASC, numtests DESC;

Question 10: First, adapt your query from Question 9 so that you only examine customers located in the United States, with Hawaii and Alaska residents excluded. HINTS: In this data set, the abbreviation for the United States is "US", the abbreviation for Hawaii is "HI" and the abbreviation for Alaska is "AK". You should have 5,860 tests completed on Sunday of 2013.
%%sql
SELECT COUNT(c.created_at) AS numtests, DAYOFWEEK(c.created_at) AS dayasnum, YEAR(c.created_at) AS year,
(CASE
WHEN DAYOFWEEK(c.created_at)=1 THEN 'Sun'
WHEN DAYOFWEEK(c.created_at)=2 THEN 'Mon'
WHEN DAYOFWEEK(c.created_at)=3 THEN 'Tue'
WHEN DAYOFWEEK(c.created_at)=4 THEN 'Wed'
WHEN DAYOFWEEK(c.created_at)=5 THEN 'Thu'
WHEN DAYOFWEEK(c.created_at)=6 THEN 'Fri'
WHEN DAYOFWEEK(c.created_at)=7 THEN 'Sat'
END) AS daylabel
FROM complete_tests c JOIN (SELECT DISTINCT dog_guid
                            FROM dogs d JOIN users u
                            ON d.user_guid=u.user_guid
                            WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)
                           AND u.country='US' AND (u.state!='HI' AND u.state!='AK')) AS dogs_cleaned
ON c.dog_guid=dogs_cleaned.dog_guid
GROUP BY year, daylabel
ORDER BY year ASC, numtests DESC;

Question 11: Write a query that extracts the original created_at time stamps for rows in the complete_tests table in one column, and the created_at time stamps with 6 hours subtracted in another column. Limit your output to 100 rows.
%%sql
SELECT created_at, DATE_SUB(created_at, interval 6 hour) AS corrected_time 
FROM complete_tests
LIMIT 100;

Question 12: Use your query from Question 11 to adapt your query from Question 10 in order to provide a count of the number of tests completed on each day of the week, with approximate time zones taken into account, in each year in the Dognition data set. Exclude all dog_guids and user_guids with a value of "1" in their exclude columns. Sort the output by year in ascending order, and then by the total number of tests completed in descending order. HINT: Don't forget to adjust for the time zone in your DAYOFWEEK statement and your CASE statement.
%%sql
SELECT COUNT(c.created_at) AS numtests, DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour)) AS dayasnum, YEAR(c.created_at) AS year,
(CASE
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=1 THEN 'Sun'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=2 THEN 'Mon'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=3 THEN 'Tue'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=4 THEN 'Wed'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=5 THEN 'Thu'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=6 THEN 'Fri'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=7 THEN 'Sat'
END) AS daylabel
FROM complete_tests c JOIN (SELECT DISTINCT dog_guid
                            FROM dogs d JOIN users u
                            ON d.user_guid=u.user_guid
                            WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)
                           AND u.country='US' AND (u.state!='HI' AND u.state!='AK')) AS dogs_cleaned
ON c.dog_guid=dogs_cleaned.dog_guid
GROUP BY year, daylabel
ORDER BY year ASC, numtests DESC;

Question 13: Adapt your query from Question 12 so that the results are sorted by year in ascending order, and then by the day of the week in the following order: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.
%%sql
SELECT COUNT(c.created_at) AS numtests, DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour)) AS dayasnum, YEAR(c.created_at) AS year,
(CASE
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=1 THEN 'Sun'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=2 THEN 'Mon'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=3 THEN 'Tue'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=4 THEN 'Wed'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=5 THEN 'Thu'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=6 THEN 'Fri'
WHEN DAYOFWEEK(DATE_SUB(c.created_at, interval 6 hour))=7 THEN 'Sat'
END) AS daylabel
FROM complete_tests c JOIN (SELECT DISTINCT dog_guid
                            FROM dogs d JOIN users u
                            ON d.user_guid=u.user_guid
                            WHERE (d.exclude=0 OR d.exclude IS NULL) AND (u.exclude=0 OR u.exclude IS NULL)
                           AND u.country='US' AND (u.state!='HI' AND u.state!='AK')) AS dogs_cleaned
ON c.dog_guid=dogs_cleaned.dog_guid
GROUP BY year, daylabel
ORDER BY year ASC, FIELD(daylabel,'Mon','Tue','Wed','Thu','Fri','Sat','Sun');

Question 14: Which 5 states within the United States have the most Dognition customers, once all dog_guids and user_guids with a value of "1" in their exclude columns are removed? Try using the following general strategy: count how many unique user_guids are associated with dogs in the complete_tests table, break up the counts according to state, sort the results by counts of unique user_guids in descending order, and then limit your output to 5 rows. California ("CA") and New York ("NY") should be at the top of your list.
%%sql
SELECT dogs_cleaned.state AS state, COUNT(DISTINCT dogs_cleaned.user_guid) AS numusers
FROM complete_tests c JOIN (SELECT DISTINCT dog_guid, u.user_guid, u.state FROM dogs d JOIN users u
                            ON d.user_guid=u.user_guid
                            WHERE ((u.exclude IS NULL OR u.exclude=0)
                                   AND u.country="US"
                                   AND (d.exclude IS NULL OR d.exclude=0))) AS dogs_cleaned 
ON c.dog_guid=dogs_cleaned.dog_guid
GROUP BY state
ORDER BY numusers DESC LIMIT 5;

Question 15: Which 10 countries have the most Dognition customers, once all dog_guids and user_guids with a value of "1" in their exclude columns are removed? HINT: don't forget to remove the u.country="US" statement from your WHERE clause.
%%sql
SELECT dogs_cleaned.country AS country, COUNT(DISTINCT dogs_cleaned.user_guid) AS numusers
FROM complete_tests c JOIN (SELECT DISTINCT dog_guid, u.user_guid, u.country 
                            FROM dogs d JOIN users u
                            ON d.user_guid=u.user_guid
                            WHERE ((u.exclude IS NULL OR u.exclude=0)
                                   AND (d.exclude IS NULL OR d.exclude=0))) AS dogs_cleaned 
ON c.dog_guid=dogs_cleaned.dog_guid
GROUP BY country
ORDER BY numusers DESC
LIMIT 10;
