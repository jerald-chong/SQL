Question 1: Output a table that calculates the number of distinct female and male dogs in each breed group of the Dogs table, sorted by the total number of dogs in descending order (the sex/breed_group pair with the greatest number of dogs should have 8466 unique Dog_Guids):
%%sql
SELECT gender, breed_group, COUNT(DISTINCT dog_guid) AS number_of_dogs
FROM dogs
GROUP BY gender, breed_group
ORDER BY number_of_dogs DESC;

Question 2: Revise the query your wrote in Question 1 so that it uses only numbers in the GROUP BY and ORDER BY fields.
%%sql
SELECT gender, breed_group, COUNT(DISTINCT dog_guid) AS number_of_dogs
FROM dogs
GROUP BY 1, 2
ORDER BY 3 DESC;

Question 3: Revise the query your wrote in Question 2 so that it (1) excludes the NULL and empty string entries in the breed_group field, and (2) excludes any groups that don't have at least 1,000 distinct Dog_Guids in them. Your result should contain 8 rows. 
%%sql
SELECT gender, breed_group, COUNT(DISTINCT dog_guid) AS number_of_dogs
FROM dogs
WHERE breed_group!="None" AND breed_group!=""
GROUP BY 1, 2
HAVING number_of_dogs>=1000
ORDER BY 3 DESC;

Question 4: Write a query that outputs the average number of tests completed and average mean inter-test-interval for every breed type, sorted by the average number of completed tests in descending order (popular hybrid should be the first row in your output).
%%sql
SELECT breed_type, AVG(total_tests_completed) AS Avg_tests, AVG(mean_iti_minutes) AS Avg_mean_time
FROM dogs
GROUP BY breed_type
ORDER BY Avg_tests DESC;

Question 5: Write a query that outputs the average amount of time it took customers to complete each type of test where any individual reaction times over 6000 hours are excluded and only average reaction times that are greater than 0 seconds are included (your output should end up with 67 rows).
%%sql
SELECT test_name, AVG(TIMESTAMPDIFF(HOUR, start_time, end_time)) AS Avg_Time_Taken
FROM exam_answers
WHERE TIMESTAMPDIFF(HOUR, start_time, end_time) < 6000
GROUP BY test_name
HAVING AVG(TIMESTAMPDIFF(SECOND, start_time, end_time)) > 0
ORDER BY Avg_Time_Taken DESC;

Question 6: Write a query that outputs the total number of unique User_Guids in each combination of State and ZIP code (postal code) in the United States, sorted first by state name in ascending alphabetical order, and second by total number of unique User_Guids in descending order (your first state should be AE and there should be 5043 rows in total in your output).
%%sql
SELECT state, zip, COUNT(DISTINCT user_guid) AS number_of_users
FROM users
WHERE country='US'
GROUP BY state, zip
ORDER BY state ASC, number_of_users DESC;

Question 7: Write a query that outputs the total number of unique User_Guids in each combination of State and ZIP code in the United States that have at least 5 users, sorted first by state name in ascending alphabetical order, and second by total number of unique User_Guids in descending order (your first state/ZIP code combination should be AZ/86303).
%%sql
SELECT state, zip, COUNT(DISTINCT user_guid) AS number_of_users
FROM users
WHERE country='US'
GROUP BY state, zip
HAVING number_of_users >= 5
ORDER BY state ASC, number_of_users DESC;
