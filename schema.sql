DROP DATABASE IF EXISTS wschat;

CREATE DATABASE wschat;
USE wschat;

CREATE TABLE messages (
       id INT PRIMARY KEY,
       user VARCHAR(50),
       message TEXT,
       timestamp DATETIME
);
