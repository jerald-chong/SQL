Question 1: To get a feeling for what kind of values exist in the Dognition personality dimension column, write a query that will output all of the distinct values in the dimension column. Use your relational schema or the course materials to determine what table the dimension column is in. Your output should have 11 rows.
%%sql
SELECT DISTINCT dimension
FROM dogs;

Question 2: Use the equijoin syntax (described in MySQL Exercise 8) to write a query that will output the Dognition personality dimension and total number of tests completed by each unique DogID. This query will be used as an inner subquery in the next question. LIMIT your output to 100 rows for troubleshooting purposes.
%%sql
SELECT COUNT(c.created_at) AS num_tests, d.dog_guid AS DogID, d.dimension AS Dimension
FROM dogs d, complete_tests c
WHERE d.dog_guid = c.dog_guid
GROUP BY DogID
LIMIT 100;

Question 3: Re-write the query in Question 2 using traditional join syntax (described in MySQL Exercise 8).
%%sql
SELECT COUNT(c.created_at) AS num_tests, d.dog_guid AS DogID, d.dimension AS Dimension
FROM dogs d JOIN complete_tests c
ON d.dog_guid = c.dog_guid
GROUP BY DogID
lIMIT 100;

Question 4: To start, write a query that will output the average number of tests completed by unique dogs in each Dognition personality dimension. Choose either the query in Question 2 or 3 to serve as an inner query in your main query. If you have trouble, make sure you use the appropriate aliases in your GROUP BY and SELECT statements.
%%sql
SELECT AVG(numtests_per_dog.numtests) AS avg_tests_completed, dimension
FROM (SELECT COUNT(c.created_at) AS numtests, d.dog_guid AS DogID, d.dimension AS Dimension
      FROM dogs d JOIN complete_tests c
      ON d.dog_guid = c.dog_guid
      GROUP BY DogID) AS numtests_per_dog
GROUP BY numtests_per_dog.dimension;

Question 5: How many unique DogIDs are summarized in the Dognition dimensions labeled "None" or ""? (You should retrieve values of 13,705 and 71)
%%sql
SELECT dimension, COUNT(DogID) AS num_dogs
FROM (SELECT d.dog_guid AS DogID, d.dimension AS dimension
     FROM dogs d JOIN complete_tests c
     ON d.dog_guid = c.dog_guid
     WHERE d.dimension IS NULL OR d.dimension=''
     GROUP BY DogID) AS dogs_in_complete_tests
GROUP BY dimension;

Question 6: To determine whether there are any features that are common to all dogs that have non-NULL empty strings in the dimension column, write a query that outputs the breed, weight, value in the "exclude" column, first or minimum time stamp in the complete_tests table, last or maximum time stamp in the complete_tests table, and total number of tests completed by each unique DogID that has a non-NULL empty string in the dimension column.
%%sql
SELECT d.dimension, d.breed, d.weight, d.exclude, MIN(c.created_at) AS first_test, 
MAX(c.created_at) AS last_test, COUNT(c.created_at) AS numtests
FROM dogs d JOIN complete_tests c
ON d.dog_guid=c.dog_guid
WHERE d.dimension=''
GROUP BY d.dog_guid;

Question 7: Rewrite the query in Question 4 to exclude DogIDs with (1) non-NULL empty strings in the dimension column, (2) NULL values in the dimension column, and (3) values of "1" in the exclude column. NOTES AND HINTS: You cannot use a clause that says d.exclude does not equal 1 to remove rows that have exclude flags, because Dognition clarified that both NULL values and 0 values in the "exclude" column are valid data. A clause that says you should only include values that are not equal to 1 would remove the rows that have NULL values in the exclude column, because NULL values are never included in equals statements (as we learned in the join lessons). In addition, although it should not matter for this query, practice including parentheses with your OR and AND statements that accurately reflect the logic you intend. Your results should return 402 DogIDs in the ace dimension and 626 dogs in the charmer dimension.
%%sql
SELECT AVG(numtests_per_dog.numtests) AS avg_tests_completed, dimension, COUNT(DISTINCT DogID)
FROM (SELECT COUNT(c.created_at) AS numtests, d.dog_guid AS DogID, d.dimension AS Dimension
      FROM dogs d JOIN complete_tests c
      ON d.dog_guid = c.dog_guid
      WHERE (dimension IS NOT NULL AND dimension!='') AND (d.exclude IS NULL OR d.exclude=0)
      GROUP BY DogID) AS numtests_per_dog
GROUP BY numtests_per_dog.dimension;

Questions 8: Write a query that will output all of the distinct values in the breed_group field.
%%sql
SELECT DISTINCT breed_group
FROM dogs;

Question 9: Write a query that outputs the breed, weight, value in the "exclude" column, first or minimum time stamp in the complete_tests table, last or maximum time stamp in the complete_tests table, and total number of tests completed by each unique DogID that has a NULL value in the breed_group column.
%%sql
SELECT d.breed, d.weight, d.exclude, MIN(c.created_at) AS first_test, 
MAX(c.created_at) AS last_test, COUNT(c.created_at) AS numtests
FROM dogs d JOIN complete_tests c
ON d.dog_guid=c.dog_guid
WHERE d.breed_group IS NULL
GROUP BY d.dog_guid;

Question 10: Adapt the query in Question 7 to examine the relationship between breed_group and number of tests completed. Exclude DogIDs with values of "1" in the exclude column. Your results should return 1774 DogIDs in the Herding breed group.
%%sql
SELECT breed_group, AVG(numtests_per_dog.numtests) AS avg_tests_completed, COUNT(DISTINCT DogID)
FROM (SELECT d.dog_guid AS DogID, d.breed_group AS breed_group, COUNT(c.created_at) AS numtests
     FROM dogs d JOIN complete_tests c
     ON d.dog_guid=c.dog_guid
     WHERE d.exclude IS NULL OR d.exclude=0
     GROUP BY DogID) AS numtests_per_dog
GROUP BY breed_group;

Question 11: Adapt the query in Question 10 to only report results for Sporting, Hound, Herding, and Working breed_groups using an IN clause.
%%sql
SELECT breed_group, AVG(numtests_per_dog.numtests) AS avg_tests_completed, COUNT(DISTINCT DogID)
FROM (SELECT d.dog_guid AS DogID, d.breed_group AS breed_group, COUNT(c.created_at) AS numtests
     FROM dogs d JOIN complete_tests c
     ON d.dog_guid=c.dog_guid
     WHERE d.exclude IS NULL OR d.exclude=0
     GROUP BY DogID) AS numtests_per_dog
GROUP BY breed_group
HAVING breed_group IN ('Sporting','Hound','Herding','Working');

Question 12: Begin by writing a query that will output all of the distinct values in the breed_type field.
%%sql
SELECT DISTINCT breed_type
FROM dogs;

Question 13: Adapt the query in Question 7 to examine the relationship between breed_type and number of tests completed. Exclude DogIDs with values of "1" in the exclude column. Your results should return 8865 DogIDs in the Pure Breed group.
%%sql
SELECT breed_type, AVG(numtests_per_dog.numtests) AS avg_tests_completed, COUNT(DISTINCT DogID)
FROM (SELECT d.dog_guid AS DogID, d.breed_type AS breed_type, COUNT(c.created_at) AS numtests
      FROM dogs d JOIN complete_tests c
      ON d.dog_guid = c.dog_guid
      WHERE d.exclude=0 OR d.exclude IS NULL
      GROUP BY DogID) AS numtests_per_dog
GROUP BY breed_type;

Question 14: For each unique DogID, output its dog_guid, breed_type, number of completed tests, and use a CASE statement to include an extra column with a string that reads "Pure_Breed" whenever breed_type equals 'Pure Breed" and "Not_Pure_Breed" whenever breed_type equals anything else. LIMIT your output to 50 rows for troubleshooting.
%%sql
SELECT d.dog_guid AS DogID, d.breed_type AS breed_type, COUNT(c.created_at) AS numtests,
    IF(d.breed_type='Pure Breed','pure_breed','not_pure_breed') AS pure_breed
FROM dogs d JOIN complete_tests c
ON d.dog_guid = c.dog_guid
GROUP BY DogID
LIMIT 50;

Question 15: Adapt your queries from Questions 7 and 14 to examine the relationship between breed_type and number of tests completed by Pure_Breed dogs and non_Pure_Breed dogs. Your results should return 8336 DogIDs in the Not_Pure_Breed group.
%%sql
SELECT numtests_per_dog.pure_breed AS pure_breed,
AVG(numtests_per_dog.numtests) AS avg_tests_completed, COUNT(DISTINCT dogID)
FROM(SELECT d.dog_guid AS DogID, d.breed_type AS breed_type, COUNT(c.created_at) AS numtests, 
     IF(d.breed_type='Pure Breed','pure_breed','not_pure_breed') AS pure_breed
     FROM dogs d JOIN complete_tests c
     ON d.dog_guid = c.dog_guid
     WHERE d.exclude IS NULL OR d.exclude=0
     GROUP BY DogID) AS numtests_per_dog
GROUP BY pure_breed;

Question 16: Adapt your query from Question 15 to examine the relationship between breed_type, whether or not a dog was neutered (indicated in the dog_fixed field), and number of tests completed by Pure_Breed dogs and non_Pure_Breed dogs. There are DogIDs with null values in the dog_fixed column, so your results should have 6 rows, and the average number of tests completed by non-pure-breeds who are neutered is 10.5681.
%%sql
SELECT numtests_per_dog.pure_breed AS pure_breed, neutered,
AVG(numtests_per_dog.numtests) AS avg_tests_completed, COUNT(DISTINCT dogID)
FROM(SELECT d.dog_guid AS DogID, d.breed_type AS breed_type, d.dog_fixed AS neutered, COUNT(c.created_at) AS numtests, 
     IF(d.breed_type='Pure Breed','pure_breed','not_pure_breed') AS pure_breed
     FROM dogs d JOIN complete_tests c
     ON d.dog_guid = c.dog_guid
     WHERE d.exclude IS NULL OR d.exclude=0
     GROUP BY DogID) AS numtests_per_dog
GROUP BY pure_breed, neutered;

Question 17: Adapt your query from Question 7 to include a column with the standard deviation for the number of tests completed by each Dognition personality dimension.
%%sql
SELECT dimension, AVG(numtests) AS avg_tests_completed, COUNT(DISTINCT dogID), STDDEV(numtests)
FROM(SELECT d.dog_guid AS dogID, d.dimension AS dimension, count(c.created_at) AS numtests
     FROM dogs d JOIN complete_tests c
     ON d.dog_guid=c.dog_guid
     WHERE (dimension IS NOT NULL AND dimension!='') AND (d.exclude IS NULL OR d.exclude=0)
     GROUP BY dogID) AS numtests_per_dog
GROUP BY numtests_per_dog.dimension;

Question 18: Write a query that calculates the average amount of time it took each dog breed_type to complete all of the tests in the exam_answers table. Exclude negative durations from the calculation, and include a column that calculates the standard deviation of durations for each breed_type group:
%%sql
SELECT d.breed_type AS breed_type, AVG(TIMESTAMPDIFF(minute,e.start_time,e.end_time)) AS AVG_Duration,
    STDDEV(TIMESTAMPDIFF(minute,e.start_time,e.end_time)) AS STDDEV_Duration
FROM dogs d JOIN exam_answers e
ON d.dog_guid=e.dog_guid
WHERE TIMESTAMPDIFF(minute,e.start_time, e.end_time)>0
GROUP BY breed_type;
