-- This script lists number of records with same score in first_table

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
