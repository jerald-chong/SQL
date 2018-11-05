%load_ext sql
%sql mysql://studentuser:studentpw@mysqlserver/dognitiondb
%sql USE dognitiondb

Question 1: How would you change the title of the "start_time" field in the exam_answers table to "exam start time" in a query output? Try it below:
%%sql
SELECT start_time AS 'exam start time'
FROM exam_answers
LIMIT 10;

Question 2: How would you list all the possible combinations of test names and subcategory names in complete_tests table? (If you do not limit your output, you should retrieve 45 possible combinations)
%%sql
SELECT DISTINCT test_name subcategory_name
FROM complete_tests;

Question 3: Below, try executing a query that would sort the same output as described above by membership_type first in descending order, and state second in ascending order:
%%sql
SELECT DISTINCT user_guid, state, membership_type
FROM users
WHERE country="US" AND state IS NOT NULL and membership_type IS NOT NULL
ORDER BY membership_type DESC, state ASC;

Question 4: How would you get a list of all the subcategories of Dognition tests, in alphabetical order, with no test listed more than once (if you do not limit your output, you should retrieve 16 rows)?
%%sql
SELECT DISTINCT subcategory_name 
FROM complete_tests
ORDER BY subcategory_name;

Question 5: How would you create a text file with a list of all the non-United States countries of Dognition customers with no country listed more than once?
non_us_countries=%sql SELECT DISTINCT country FROM users WHERE country!='US'
non_us_countries.csv('non_us_countries.csv')

Question 6: How would you find the User ID, Dog ID, and test name of the first 10 tests to ever be completed in the Dognition database?
%%sql
SELECT user_guid, dog_guid, test_name
FROM complete_tests
ORDER BY created_at ASC
LIMIT 10;

Question 7: How would create a text file with a list of all the customers with yearly memberships who live in the state of North Carolina (USA) and joined Dognition after March 1, 2014, sorted so that the most recent member is at the top of the list?
NC_yearly_after_March_1_2014=%sql SELECT DISTINCT user_guid, state, created_at FROM users WHERE membership_type=2 AND state='NC' AND country='US' AND created_at>'2014-03-01' ORDER BY created_at DESC;
NC_yearly_after_March_1_2014.csv('NC_yearly_after_March_1_2014')

Question 8: See if you can find an SQL function that would allow you to output all of the distinct breed names in UPPER case. Create a query that would output a list of these names in upper case, sorted in alphabetical order.
%%sql
SELECT DISTINCT UPPER(breed)
FROM dogs
ORDER BY breed ASC;
