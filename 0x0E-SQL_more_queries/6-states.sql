-- This script creates the database hbtn_0d_usa and the table states

CREATE DATABASE if NOT EXISTS hbtn_0d_usa;
CREATE TABLE if NOT EXISTS states(
    id INT NOT NULL UNIQUE,
    name VARCHAR(256) NOT NULL);
