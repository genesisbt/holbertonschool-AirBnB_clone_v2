-- Script to create the test database, user, and privileges

-- Create  database if doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create  user if  doesn't  exist and sets password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges to created user on created database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant SELECT privilege to created user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';