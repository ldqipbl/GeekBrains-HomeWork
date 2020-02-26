DROP DATABASE IF EXISTS Discount_MVP;
CREATE DATABASE Discount_MVP;

USE Discount_MVP;

DROP TABLE IF EXISTS users;
CREATE TABLE users(id SERIAL PRIMARY KEY, firsname VARCHAR(100), lastname VARCHAR(100));
INSERT INTO users VALUES
	(0, 'Leo_1', 'Simson'),
	(0, 'Leo_2', 'Simson'),
	(0, 'Leo_3', 'Simson'),
	(0, 'Leo_4', 'Simson'),
	(0, 'Leo_5', 'Simson');

DROP TABLE IF EXISTS products;
CREATE TABLE products(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        desription TEXT,
        price DECIMAL (11,4)
);

DROP TABLE IF EXISTS tbl_3;
CREATE TABLE tbl_3(id SERIAL PRIMARY KEY, firsname VARCHAR(100), lastname VARCHAR(100));

DROP TABLE IF EXISTS tbl_4;
CREATE TABLE tbl_4(id SERIAL PRIMARY KEY, firsname VARCHAR(100), lastname VARCHAR(100));

DROP TABLE IF EXISTS tbl_5;
CREATE TABLE tbl_5(id SERIAL PRIMARY KEY, firsname VARCHAR(100), lastname VARCHAR(100));

DROP TABLE IF EXISTS discounts;
CREATE TABLE discounts( 
	id SERIAL PRIMARY KEY, 
	discount FLOAT UNSIGNED COMMENT 'Величина скидки от 0.0 до 1.0',
        started_at DATETIME, 
	finished_at DATETIME
);

