-- This script displays the average temp. by city ordered by temperature (desc.)

SOURCE D:\ALX\temperatures.sql;
SELECT city, AVG((value * 9/5) + 32) AS avg_temp FROM temperatures ORDER BY avg_temp DESC;
