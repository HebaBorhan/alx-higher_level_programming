-- This script displays the average temp. by city ordered by temperature (desc.)

SOURCE C:\Users\h_bor\Downloads\temperatures.sql
SELECT city, AVG((value * 9/5) + 32) AS avg_temp FROM temperatures ORDER BY avg_temp DESC;
