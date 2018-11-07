Question 1: What does the Month column represent in this output? Take a look and see what you think:
%%sql
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
GROUP BY test_name
ORDER BY test_name ASC, Month ASC;

Question 2: What does test_name mean in this case? Try it out:
%%sql
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
GROUP BY Month
ORDER BY Month ASC, test_name ASC;
