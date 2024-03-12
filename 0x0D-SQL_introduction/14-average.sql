-- This script computes the score average of all records in second_table

ALTER TABLE second_table ADD average = AVG(score);
