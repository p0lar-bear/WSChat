DROP DATABASE IF EXISTS wschat;

CREATE DATABASE wschat;
USE wschat;

CREATE TABLE users (
       id INT PRIMARY KEY,
       name VARCHAR(50) UNIQUE NOT NULL,
       password CHAR(40) NOT NULL,
       regtime DATETIME NOT NULL
);

CREATE TABLE messages (
       id INT PRIMARY KEY,
       user_id INT NOT NULL,
       anon_name VARCHAR(50) NULL,
       message TEXT NOT NULL,
       timestamp DATETIME,
       ip INT NOT NULL
);

CREATE TABLE sessions (
       id CHAR(40) PRIMARY KEY,
       user_id INT NOT NULL,
       last_update DATETIME NOT NULL,
       created DATETIME NOT NULL
);
