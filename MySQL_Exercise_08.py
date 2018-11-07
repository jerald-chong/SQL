Question 1: How would you re-write this query using the traditional join syntax?
%%sql
SELECT d.user_guid AS UserID, d.dog_guid AS DogID, d.breed, d.breed_type, d.breed_group
FROM dogs d JOIN complete_tests c
ON d.dog_guid=c.dog_guid
WHERE test_name='Yawn Warm-up';

Question 2: How could you retrieve this same information using a RIGHT JOIN?
%%sql
SELECT r.dog_guid AS rDogID, d.dog_guid AS dDogID, r.user_guid AS rUserID, d.user_guid AS dUserID, AVG(r.rating) AS AvgRating, COUNT(r.rating) AS NumRatings, d.breed, d.breed_group, d.breed_type
FROM dogs d RIGHT JOIN reviews r
ON r.dog_guid=d.dog_guid AND r.user_guid=d.user_guid
WHERE r.dog_guid IS NOT NULL
GROUP BY r.dog_guid
HAVING NumRatings >= 10
ORDER BY AvgRating DESC;

Question 3: How would you use a left join to retrieve a list of all the unique dogs in the dogs table, and retrieve a count of how many tests each one completed? Include the dog_guids and user_guids from the dogs and complete_tests tables in your output. (If you do not limit your query, your output should contain 35050 rows. HINT: use the dog_guid from the dogs table to group your results.)
%%sql
SELECT d.dog_guid AS dDogID, c.dog_guid AS cDogID, d.user_guid AS dUserID, c.user_guid AS cUserID, COUNT(c.test_name)
FROM dogs d LEFT JOIN complete_tests c
ON d.dog_guid=c.dog_guid
GROUP BY d.dog_guid;

Question 4: Repeat the query you ran in Question 3, but intentionally use the dog_guids from the completed_tests table to group your results instead of the dog_guids from the dogs table. (Your output should contain 17987 rows)
%%sql
SELECT d.dog_guid AS dDogID, c.dog_guid AS cDogID, d.user_guid AS dUserID, c.user_guid AS cUserID, COUNT(c.test_name)
FROM dogs d LEFT JOIN complete_tests c
ON d.dog_guid=c.dog_guid
GROUP BY c.dog_guid;

Question 5: Write a query using COUNT DISTINCT to determine how many distinct dog_guids there are in the completed_tests table.
%%sql
SELECT COUNT(DISTINCT dog_guid)
FROM complete_tests;

Question 6: We want to extract all of the breed information of every dog a user_guid in the users table owns. If a user_guid in the users table does not own a dog, we want that information as well. Write a query that would return this information. Include the dog_guid from the dogs table, and user_guid from both the users and dogs tables in your output. (HINT: you should get 952557 rows in your output!)
%%sql
SELECT u.user_guid AS uUserID, d.user_guid AS dUserID, d.dog_guid AS dDogID, d.breed
FROM users u LEFT JOIN dogs d
ON u.user_guid=d.user_guid;

Question 7: Adapt the query you wrote above so that it counts the number of rows the join will output per user_id. Sort the results by this count in descending order. Remember that if you include dog_guid or breed fields in this query, they will be randomly populated by only one of the values associated with a user_guid 
%%sql
SELECT u.user_guid AS uUserID, d.user_guid AS dUserID, d.dog_guid AS dDogID, d.breed, COUNT(*) AS Num_rows
FROM users u LEFT JOIN dogs d
ON u.user_guid=d.user_guid
GROUP BY u.user_guid
ORDER BY Num_rows DESC;

Question 8: How many rows in the users table are associated with user_guid 'ce225842-7144-11e5-ba71-058fbc01cf0b'?
%%sql
SELECT COUNT(user_guid)
FROM users
WHERE user_guid='ce225842-7144-11e5-ba71-058fbc01cf0b'

Question 9: Examine all the rows in the dogs table that are associated with user_guid 'ce225842-7144-11e5-ba71-058fbc01cf0b'?
%%sql
SELECT *
FROM dogs
WHERE user_guid='ce225842-7144-11e5-ba71-058fbc01cf0b'

Question 10: How would you write a query that used a left join to return the number of distinct user_guids that were in the users table, but not the dogs table (your query should return a value of 2226)?
%%sql
SELECT COUNT(DISTINCT u.user_guid)
FROM users u LEFT JOIN dogs d
ON u.user_guid=d.user_guid
WHERE d.user_guid IS NULL;

Question 11: How would you write a query that used a right join to return the number of distinct user_guids that were in the users table, but not the dogs table (your query should return a value of 2226)?
%%sql
SELECT COUNT(DISTINCT u.user_guid)
FROM dogs d RIGHT JOIN users u
ON u.user_guid=d.user_guid
WHERE d.user_guid IS NULL;

Question 12: Use a left join to create a list of all the unique dog_guids that are contained in the site_activities table, but not the dogs table, and how many times each one is entered. Note that there are a lot of NULL values in the dog_guid of the site_activities table, so you will want to exclude them from your list.
%%sql
SELECT s.dog_guid, COUNT(*) AS Num_Entries
FROM site_activities s LEFT JOIN dogs d
ON s.dog_guid=d.dog_guid
WHERE d.dog_guid IS NULL AND s.dog_guid IS NOT NULL
GROUP BY s.dog_guid;
