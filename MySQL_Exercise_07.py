Questions 1-4: How many unique dog_guids and user_guids are there in the reviews and dogs table independently?

%%sql 
SELECT COUNT(DISTINCT dog_guid) AS DogID_reviews
FROM reviews

%%sql 
SELECT COUNT(DISTINCT dog_guid) AS DogID_dogs
FROM dogs

%%sql 
SELECT COUNT(DISTINCT user_guid) AS UserID_reviews
FROM reviews

%%sql 
SELECT COUNT(DISTINCT user_guid) AS UserID_dogs
FROM dogs

Question 5: How would you extract the user_guid, dog_guid, breed, breed_type, and breed_group for all animals who completed the "Yawn Warm-up" game (you should get 20,845 rows if you join on dog_guid only)?
%%sql
SELECT d.dog_guid AS DogID, d.user_guid AS UserID, d.breed, d.breed_type, d.breed_group
FROM dogs d, complete_tests c
WHERE test_name = 'Yawn Warm-up' AND d.dog_guid=c.dog_guid;

Question 6: How would you extract the user_guid, membership_type, and dog_guid of all the golden retrievers who completed at least 1 Dognition test (you should get 711 rows)?
%%sql
SELECT DISTINCT d.user_guid as UserID, u.membership_type, d.dog_guid as DogID, d.breed
FROM dogs d, users u, complete_tests c
WHERE d.breed = 'Golden Retriever' AND d.total_tests_completed >=1 AND d.dog_guid=c.dog_guid AND d.user_guid=u.user_guid;

Question 7: How many unique Golden Retrievers who live in North Carolina are there in the Dognition database (you should get 30)?
%%sql
SELECT COUNT(DISTINCT d.dog_guid) AS Num_GR, u.state AS State, d.breed AS Breed
FROM dogs d, users u
WHERE d.user_guid=u.user_guid AND d.breed = 'Golden Retriever' AND State = 'NC';

Question 8: How many unique customers within each membership type provided reviews (there should be 2900 in the membership type with the greatest number of customers, and 15 in the membership type with the fewest number of customers if you do NOT include entries with NULL values in their ratings field)?
%%sql
SELECT COUNT(DISTINCT u.user_guid) AS Num_customers, u.membership_type
FROM users u, reviews r
WHERE u.user_guid = r.user_guid AND r.rating IS NOT NULL
GROUP BY u.membership_type;

Question 9: For which 3 dog breeds do we have the greatest amount of site_activity data, (as defined by non-NULL values in script_detail_id)(your answers should be "Mixed", "Labrador Retriever", and "Labrador Retriever-Golden Retriever Mix"?
%%sql
SELECT d.breed AS Breed, COUNT(s.script_detail_id) AS Activity
FROM dogs d, site_activities s
WHERE d.user_guid=s.user_guid AND s.script_detail_id IS NOT NULL
GROUP BY d.breed
ORDER BY Activity DESC
LIMIT 3;
