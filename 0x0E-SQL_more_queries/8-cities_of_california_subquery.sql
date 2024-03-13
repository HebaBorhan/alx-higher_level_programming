-- This script lists all the cities of California found in the database hbtn_0d_usa

USE hbtn_0d_usa;
SELECT cities.id, cities.name, state.id
        FROM cities
WHERE state_id =        
          (SELECT id
           FROM states
           WHERE name = 'California')
ORDER BY cities.id ASC;
