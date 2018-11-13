Question 1: How could you use a subquery to extract all the data from exam_answers that had test durations that were greater than the average duration for the "Yawn Warm-Up" game? Start by writing the query that gives you the average duration for the "Yawn Warm-Up" game by itself (and don't forget to exclude negative values; your average duration should be about 9934):
%%sql
SELECT AVG(TIMESTAMPDIFF(minute,start_time,end_time)) AS Avg_Duration
FROM exam_answers
WHERE test_name = 'Yawn Warm-Up' AND TIMESTAMPDIFF(minute,start_time,end_time)>0;

Question 2: Once you've verified that your subquery is written correctly on its own, incorporate it into a main query to extract all the data from exam_answers that had test durations that were greater than the average duration for the "Yawn Warm-Up" game (you will get 11059 rows):
%%sql
SELECT *
FROM exam_answers
WHERE TIMESTAMPDIFF(minute,start_time,end_time) > 
(SELECT AVG(TIMESTAMPDIFF(minute,start_time,end_time)) AS Avg_Duration
FROM exam_answers
WHERE test_name = 'Yawn Warm-Up' AND TIMESTAMPDIFF(minute,start_time,end_time)>0);

Question 3: Use an IN operator to determine how many entries in the exam_answers tables are from the "Puzzles", "Numerosity", or "Bark Game" tests. You should get a count of 163022.
%%sql
SELECT COUNT(*)
FROM exam_answers
WHERE subcategory_name IN ('Puzzles','Numerosity','Bark Game');

Question 4: Use a NOT IN operator to determine how many unique dogs in the dog table are NOT in the "Working", "Sporting", or "Herding" breeding groups. You should get an answer of 7961.
%%sql
SELECT COUNT(*)
FROM dogs
WHERE breed_group NOT IN ('Working','Sporting','Herding');

Question 5: How could you determine the number of unique users in the users table who were NOT in the dogs table using a NOT EXISTS clause? You should get the 2226, the same result as you got in Question 10 of MySQL Exercise 8: Joining Tables with Outer Joins.
%%sql
SELECT DISTINCT u.user_guid AS uUserID
FROM users u
WHERE NOT EXISTS (SELECT *
                 FROM dogs d
                 WHERE u.user_guid=d.user_guid);
                 
Question 6: Write a query using an IN clause and equijoin syntax that outputs the dog_guid, breed group, state of the owner, and zip of the owner for each distinct dog in the Working, Sporting, and Herding breed groups. (You should get 10,254 rows; the query will be a little slower than some of the others we have practiced)
%%sql
SELECT DISTINCT d.dog_guid, d.breed_group, u.state, u.zip
FROM dogs d, users u
WHERE breed_group IN ('Working','Sporting','Herding') AND d.user_guid = u.user_guid;

Question 7: Write the same query as in Question 6 using traditional join syntax.
%%sql
SELECT DISTINCT d.dog_guid, d.breed_group, u.state, u.zip
FROM dogs d JOIN users u
ON d.user_guid=u.user_guid
WHERE breed_group IN ('Working','Sporting','Herding');

Question 8: Earlier we examined unique users in the users table who were NOT in the dogs table. Use a NOT EXISTS clause to examine all the users in the dogs table that are not in the users table (you should get 2 rows in your output).
%%sql
SELECT DISTINCT d.user_guid AS dUserID, d.dog_guid AS dDogID
FROM dogs d
WHERE NOT EXISTS (SELECT *
                 FROM users u
                 WHERE d.user_guid=u.user_guid);

Question 9: We saw earlier that user_guid 'ce7b75bc-7144-11e5-ba71-058fbc01cf0b' still ends up with 1819 rows of output after a left outer join with the dogs table. If you investigate why, you'll find out that's because there are duplicate user_guids in the dogs table as well. How would you adapt the query we wrote earlier (copied below) to only join unique UserIDs from the users table with unique UserIDs from the dog table?
%%sql
SELECT DistinctUUsersID.user_guid AS uUserID, d.user_guid AS dUserID, count(*) AS numrows
FROM (SELECT DISTINCT u.user_guid 
      FROM users u
     WHERE user_guid='ce7b75bc-7144-11e5-ba71-058fbc01cf0b') AS DistinctUUsersID 
LEFT JOIN dogs d
  ON DistinctUUsersID.user_guid=d.user_guid
GROUP BY DistinctUUsersID.user_guid
ORDER BY numrows DESC;

Question 10: Now let's prepare and test the inner query for the right half of the join. Give the dogs table an alias, and write a query that would select the distinct user_guids from the dogs table (we will use this query as a inner subquery in subsequent questions, so you will need an alias to differentiate the user_guid column of the dogs table from the user_guid column of the users table).
%%sql
SELECT DISTINCT d.user_guid
FROM dogs d;

Question 11: Now insert the query you wrote in Question 10 as a subquery on the right part of the join you wrote in question 9. The output should return columns that should have matching user_guids, and 1 row in the numrows column with a value of 1.
%%sql
SELECT DistinctUUsersID.user_guid AS uUserID, DistinctDUsersID.user_guid AS dUserID, count(*) AS numrows
FROM (SELECT DISTINCT u.user_guid 
      FROM users u
     WHERE user_guid='ce7b75bc-7144-11e5-ba71-058fbc01cf0b') AS DistinctUUsersID 
LEFT JOIN (SELECT DISTINCT d.user_guid
           FROM dogs d) AS DistinctDUsersID
  ON DistinctUUsersID.user_guid=DistinctDUsersID.user_guid
GROUP BY DistinctUUsersID.user_guid
ORDER BY numrows DESC;

Question 12: Adapt the query from Question 10 so that, in theory, you would retrieve a full list of all the DogIDs a user in the users table owns, with its accompagnying breed information whenever possible. HOWEVER, BEFORE YOU RUN THE QUERY MAKE SURE TO LIMIT YOUR OUTPUT TO 100 ROWS WITHIN THE SUBQUERY TO THE LEFT OF YOUR JOIN.
%%sql
SELECT DistinctUUsersID.user_guid AS uUserID, DistinctDUsersID.user_guid AS dUserID, 
DistinctDUsersID.dog_guid AS DogID, DistinctDUsersID.breed AS breed
FROM (SELECT DISTINCT u.user_guid
     FROM users u
     LIMIT 100) AS DistinctUUsersID
LEFT JOIN (SELECT DISTINCT d.user_guid, d.dog_guid, d.breed
          FROM dogs d) AS DistinctDUsersID
ON DistinctUUsersID.user_guid = DistinctDUsersID.user_guid
GROUP BY DistinctUUsersID.user_guid;

Question 13: You might have a good guess by now about why there are duplicate rows in the dogs table and users table, even though most corporate databases are configured to prevent duplicate rows from ever being accepted. To be sure, though, let's adapt this query we wrote above:
SELECT DistinctUUsersID.user_guid AS uUserID, d.user_guid AS dUserID, count(*) AS numrows
FROM (SELECT DISTINCT u.user_guid FROM users u) AS DistinctUUsersID 
LEFT JOIN dogs d
  ON DistinctUUsersID.user_guid=d.user_guid
GROUP BY DistinctUUsersID.user_guid
ORDER BY numrows DESC
Add dog breed and dog weight to the columns that will be included in the final output of your query. In addition, use a HAVING clause to include only UserIDs who would have more than 10 rows in the output of the left join (your output should contain 5 rows).
%%sql
SELECT DistinctUUsersID.user_guid AS uUserID, d.user_guid AS dUserID, d.breed, d.weight, count(*) AS numrows
FROM (SELECT DISTINCT u.user_guid 
      FROM users u) AS DistinctUUsersID 
LEFT JOIN dogs d
  ON DistinctUUsersID.user_guid=d.user_guid
GROUP BY DistinctUUsersID.user_guid
HAVING numrows>10
ORDER BY numrows DESC;
