-- Script to create the database, user, and privileges

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges to created user on created database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant select privileges to created user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';