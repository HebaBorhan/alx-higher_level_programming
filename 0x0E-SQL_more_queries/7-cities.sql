-- This script creates the database hbtn_0d_usa and the table cities

CREATE DATABASE if NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE if NOT EXISTS cities(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL FOREIGN KEY,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id));
