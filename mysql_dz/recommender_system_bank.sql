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
	lastname VARCHAR(100),
	telephon VARCHAR(100),
	date_of_creation DATE,
	update_date DATE);				--дата обновления(покупкка или использование продукта банка)

INSERT INTO users VALUES
	(0, 'Leo_1', 'Simson', '89996667878', '2000-04-12', '2000-04-12'),
	(0, 'Leo_2', 'Simson', '89996667878', '2000-04-12', '2000-04-12'),
	(0, 'Leo_3', 'Simson', '89996667878', '2000-04-12', '2000-04-12'),
	(0, 'Leo_4', 'Simson', '89996667878', '2000-04-12', '2000-04-12'),
	(0, 'Leo_5', 'Simson', '89996667878', '2000-04-12', '2000-04-12');


--Таблица №2	
DROP TABLE IF EXISTS products;			--Продукты банка
CREATE TABLE products(
        id SERIAL PRIMARY KEY,		
        group_name VARCHAR(255),
        name VARCHAR(100));				--Товар

INSERT INTO products VALUES
	(0, 'investments', 'gold'),
        (0, 'investments', 'USE'),
        (0, 'investments', 'EUR'),
        (0, 'investments', 'bonds'),
        (0, 'investments', 'stocks'),
	(0, 'card', 'credit_debit'),
        (0, 'credit', 'Mortgage'),
	(0, 'credit', 'consumer_credit'),
	(0, 'insurance', 'life'),
	(0, 'insurance', 'property');


--Таблица №3
DROP TABLE IF EXISTS investments;               --Инвестиции
CREATE TABLE investments(
        id SERIAL PRIMARY KEY,
	user_id INT,
	products_id INT,
	ue INT,
	date_of_creation DATE);

INSERT INTO investments VALUES
	(0, 1, 3, 5000, '2000-05-24'),
	(0, 1, 1, 5, '2005-02-24'),
	(0, 3, 4, 50, '2010-07-24'),
	(0, 5, 5, 10, '2020-09-24');


--Таблица №4
DROP TABLE IF EXISTS card;                      --Карты(дебетовый, кредитные)
CREATE TABLE card(
        id SERIAL PRIMARY KEY,
        user_id INT,
        products_id INT,
	debit_ue INT,
	credit_ue INT,
	annual_percentage INT,
        date_of_creation DATE);

INSERT INTO card VALUES
	(0, 2, 6, 20000, 100000, 2, '2000-01-21'),
	(0, 2, 6, 20000, 0, 2, '2005-02-12'),
	(0, 3, 6, 0, 100000, 2, '2010-03-23'),
	(0, 3, 6, 20000, 100000, 2, '2015-04-04'),
	(0, 3, 6, 20000, 100000, 2, '2020-05-25');


--Таблица №5
DROP TABLE IF EXISTS credit;                    --Кредиты процент(annual_percentage), сумма(ue)
CREATE TABLE credit(
        id SERIAL PRIMARY KEY,
	user_id INT,
        products_id INT,
	ue INT,
	annual_percentage INT,
	date_of_creation DATE,
	date_of_end DATE);

INSERT INTO credit VALUES
	(0, 1, 7, 100000, 5, '2015-04-04', '2017-04-04'),
	(0, 1, 8, 100000, 8, '2017-04-04', '2019-04-04'),
	(0, 2, 8, 100000, 8, '2015-04-04', '2017-04-04'),
	(0, 3, 7, 100000, 5, '2015-04-04', '2017-04-04'),
	(0, 5, 7, 100000, 5, '2015-04-04', '2017-04-04');


--Таблица №6
DROP TABLE IF EXISTS insurance;                 --Страхование
CREATE TABLE insurance(
        id SERIAL PRIMARY KEY,
	user_id INT,
        products_id INT,
	ue INT,
        date_of_creation DATE);

INSERT INTO insurance VALUES
	(0, 4, 9, 5000, '2015-04-04'),
	(0, 4, 10, 5000, '2015-04-04'),
	(0, 5, 9, 5000, '2015-04-04'),
	(0, 5, 10, 5000, '2015-04-04'),
	(0, 5, 10, 5000, '2015-04-04');


--Таблица №7
DROP TABLE IF EXISTS discounts_next_manf;	--Планируемые скидки
CREATE TABLE discounts_next_manf(
	id SERIAL PRIMARY KEY,
       	products_id INT,
	discount INT,
	date_start DATE,
	date_stop DATE);

INSERT INTO discounts_next_manf VALUES
	(0, 6, 5, '2015-04-04', '2015-06-04'),
	(0, 8, 5, '2015-04-04', '2015-06-04'),
	(0, 8, 5, '2015-04-04', '2015-06-04'),
	(0, 9, 5, '2015-04-04', '2015-06-04'),
	(0, 10, 5, '2015-04-04', '2015-06-04');


--Таблица №8
DROP TABLE IF EXISTS discounts_now;		--Скидки 
CREATE TABLE discounts_now( 
	id SERIAL PRIMARY KEY,
       	products_id INT,	
	discount INT,
        date_start DATE, 
	date_stop DATE);

INSERT INTO discounts_now VALUES
	(0, 6, 5, '2015-04-04', '2015-06-04'),
	(0, 6, 5, '2015-04-04', '2015-06-04'),
	(0, 6, 5, '2015-04-04', '2015-06-04'),
	(0, 6, 5, '2015-04-04', '2015-06-04'),
	(0, 6, 5, '2015-04-04', '2015-06-04');


--Таблица №9
DROP TABLE IF EXISTS tbl_9;                     --Таблица клиентов по использованию продуктов
CREATE TABLE tbl_9(
        id SERIAL PRIMARY KEY,
        user_id INT,
        investments INT,
	card INT,
	credit INT,
	insurance INT);

INSERT INTO tbl_9 VALUES
	(0, 1, 1, 0, 1, 0),
	(0, 2, 0, 1, 1, 0),
	(0, 3, 1, 1, 1, 0),
	(0, 4, 0, 0, 0, 1),
	(0, 5, 1, 0, 1, 1);


--Таблица №10
DROP TABLE IF EXISTS tbl_10;			--Рекомендация продуктов клиенту на основе его действий.
CREATE TABLE tbl_10(
	id SERIAL PRIMARY KEY, 
	user_id INT, 
	investments INT,
        card INT,
        credit INT,
        insurance INT);

INSERT INTO tbl_10 VALUES
	(0, 1, 0, 1, 0, 1),
        (0, 2, 1, 0, 0, 1),
        (0, 3, 0, 0, 0, 1),
        (0, 4, 1, 1, 1, 0),
        (0, 5, 0, 1, 0, 0);
