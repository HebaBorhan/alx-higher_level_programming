-- This script creates a table called unique_id in the current database

CREATE TABLE if NOT EXISTS unique_id(
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL);
