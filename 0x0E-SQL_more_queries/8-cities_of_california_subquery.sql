-- This script lists all the cities of California found in the database hbtn_0d_usa

SELECT id, name
        FROM hbtn_0d_usa
        WHERE id =        
          (SELECT id
           FROM states
           WHERE name = 'California');
