/*
 						Требования к курсовому проекту:

	1. Составить общее текстовое описание БД и решаемых ею задач;
	2. минимальное количество таблиц - 10;
	3. скрипты создания структуры БД (с первичными ключами, индексами, внешними ключами);
	4. создать ERDiagram для БД;
	5. скрипты наполнения БД данными;
	6. скрипты характерных выборок (включающие группировки, JOIN'ы, вложенные таблицы);
	7. представления (минимум 2);
	8. хранимые процедуры / триггеры;
	
	Примеры: описать модель хранения данных популярного веб-сайта: кинопоиск, booking.com, wikipedia, интернет-магазин, geekbrains, госуслуги...

 */


-- 1. Составить общее текстовое описание БД и решаемых ею задач;

/*
	База хронит: 
		данные клиентов, 
		данные продуктов банка,
		данные по отдельным сигментам банка(кредиты, инвестиции, ...),
		данные по текущим и планируемым скидкам,
                данные по всем операцыям банка,
		рекомендации продукта клиентам(на основе из запросов и оперций)

	Задачи БД:
		1. Хранение и сбор информации о клиентах.
		2. Таргетная реклама скидок и новых продктов.
 */


DROP DATABASE IF EXISTS Discount_MVP;
CREATE DATABASE Discount_MVP;

USE Discount_MVP;


--Таблица №1
DROP TABLE IF EXISTS users;			--Клиенты
CREATE TABLE users(
	id SERIAL PRIMARY KEY, 
	firsname VARCHAR(100), 
	lastname VARCHAR(100));

INSERT INTO users VALUES
	(0, 'Leo_1', 'Simson'),
	(0, 'Leo_2', 'Simson'),
	(0, 'Leo_3', 'Simson'),
	(0, 'Leo_4', 'Simson'),
	(0, 'Leo_5', 'Simson');


--Таблица №2
DROP TABLE IF EXISTS products;			--Продукты банка
CREATE TABLE products(
        id SERIAL PRIMARY KEY,		
        name VARCHAR(255),				--Название товара
        desription TEXT,				--Описание товара
        price DECIMAL (11,4));				--цена


--Таблица №3
DROP TABLE IF EXISTS tbl_3;                     --Инвестиции
CREATE TABLE tbl_3(
        id SERIAL PRIMARY KEY,
        firsname VARCHAR(100),
        lastname VARCHAR(100));


--Таблица №4
DROP TABLE IF EXISTS tbl_4;                     --Карты(дебетовый, кредитные)
CREATE TABLE tbl_4(
        id SERIAL PRIMARY KEY,
        firsname VARCHAR(100),
        lastname VARCHAR(100));

--Таблица №5
DROP TABLE IF EXISTS tbl_5;                     --Кредиты
CREATE TABLE tbl_5(
        id SERIAL PRIMARY KEY,
        firsname VARCHAR(100),
        lastname VARCHAR(100));



--Таблица №6
DROP TABLE IF EXISTS tbl_6;                    --???
CREATE TABLE tbl_6(
        id SERIAL PRIMARY KEY,
        firsname VARCHAR(100),
        lastname VARCHAR(100));


--Таблица №7
DROP TABLE IF EXISTS discounts_next_manf;	--Планируемые скидки
CREATE TABLE discounts_next_manf(
	id SERIAL PRIMARY KEY, 
	firsname VARCHAR(100), 
	lastname VARCHAR(100));


--Таблица №8
DROP TABLE IF EXISTS discounts_now;		--Скидки 
CREATE TABLE discounts_now( 
	id SERIAL PRIMARY KEY, 
	discount FLOAT UNSIGNED,			--Величина скидки от 0.0 до 1.0
        started_at DATETIME, 
	finished_at DATETIME);


--Таблица №9
DROP TABLE IF EXISTS tbl_9;                     --Таблица всех операцый всех клиентов TODO index
CREATE TABLE tbl_9(
        id SERIAL PRIMARY KEY,
        firsname VARCHAR(100),
        lastname VARCHAR(100));


--Таблица №10
DROP TABLE IF EXISTS tbl_10;			--Рекомендация продуктов клиенту на основе его действий.
CREATE TABLE tbl_10(
	id SERIAL PRIMARY KEY, 
	firsname VARCHAR(100), 
	lastname VARCHAR(100));
