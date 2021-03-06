%load_ext sql
%sql mysql://studentuser:studentpw@mysqlserver/dognitiondb
%sql USE dognitiondb

Question 1: How many columns does the "dogs" table have? Enter the appropriate query below to find out:
%sql SHOW columns FROM dogs

Question 2: Try using the DESCRIBE function to learn how many columns are in the "reviews" table:
%sql DESCRIBE reviews

Questions 3-6: In the cells below, examine the fields in the other 4 tables of the Dognition database:
%sql DESCRIBE complete_tests
%sql DESCRIBE exam_answers
%sql DESCRIBE site_activities
%sql DESCRIBE users

Question 7: In the next cell, try entering a query that will let you see the first 10 rows of the breed column in the dogs table.
%%sql 
SELECT breed 
FROM dogs LIMIT 10;

Question 8: Try using the wild card to query the reviews table:
%%sql
SELECT *
FROM dogs LIMIT 5, 10;

Question 9: Go ahead and try it, adding in a column to your output that shows you the original median_iti in minutes.
%%sql
SELECT median_iti_minutes/60, median_iti_minutes
FROM dogs LIMIT 5, 10;

Question 10: How would you retrieve the first 15 rows of data from the dog_guid, subcategory_name, and test_name fields of the Reviews table, in that order?
%%sql
SELECT dog_guid, subcategory_name, test_name
FROM reviews 
LIMIT 15;

Question 11: How would you retrieve 10 rows of data from the activity_type, created_at, and updated_at fields of the site_activities table, starting at row 50? What do you notice about the created_at and updated_at fields?
%%sql
SELECT activity_type, created_at, updated_at
FROM site_activities 
LIMIT 49, 10;

Question 12: How would you retrieve 20 rows of data from all the columns in the users table, starting from row 2000? What do you notice about the free_start_user field?
%%sql
SELECT *
FROM users 
LIMIT 1999, 20;
