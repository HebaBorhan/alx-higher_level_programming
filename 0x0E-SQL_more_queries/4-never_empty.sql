-- This script creates a table called id_not_null in the current database

CREATE TABLE if NOT EXISTS id_not_null(
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256) NOT NULL);
