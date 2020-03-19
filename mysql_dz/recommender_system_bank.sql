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
	(0, 'card', 'debit'),
	(0, 'card', 'credit'),
        (0, 'credit', 'mortgage'),
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
	date_of_creation DATE,
	INDEX (id));

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
	ue INT,
        date_of_creation DATE,
	INDEX (id));

INSERT INTO card VALUES
	(0, 2, 6, 20000, '2000-01-21'),
	(0, 2, 7, 100000, '2000-01-21'),
	(0, 3, 7, 100000, '2010-03-23'),
	(0, 3, 7, 100000, '2015-04-04'),
	(0, 3, 6, 20000, '2020-05-25');


--Таблица №5
DROP TABLE IF EXISTS credit;                    --Кредиты процент(annual_percentage), сумма(ue)
CREATE TABLE credit(
        id SERIAL PRIMARY KEY,
	user_id INT,
        products_id INT,
	ue INT,
	annual_percentage INT,
	date_of_creation DATE,
	date_of_end DATE,
	INDEX (id));

INSERT INTO credit VALUES
	(0, 1, 8, 100000, 5, '2015-04-04', '2017-04-04'),
	(0, 1, 9, 100000, 8, '2017-04-04', '2019-04-04'),
	(0, 2, 9, 100000, 8, '2015-04-04', '2017-04-04'),
	(0, 3, 8, 100000, 5, '2015-04-04', '2017-04-04'),
	(0, 5, 8, 100000, 5, '2015-04-04', '2017-04-04');


--Таблица №6
DROP TABLE IF EXISTS insurance;                 --Страхование
CREATE TABLE insurance(
        id SERIAL PRIMARY KEY,
	user_id INT,
        products_id INT,
	ue INT,
        date_of_creation DATE,
	INDEX (id));

INSERT INTO insurance VALUES
	(0, 4, 10, 5000, '2015-04-04'),
	(0, 4, 11, 5000, '2015-04-04'),
	(0, 5, 10, 5000, '2015-04-04'),
	(0, 5, 11, 5000, '2015-04-04'),
	(0, 5, 11, 5000, '2015-04-04');


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
DROP TABLE IF EXISTS call_agent;               --Колл центр
CREATE TABLE call_center(
	id SERIAL PRIMARY KEY,
        firsname VARCHAR(100),
        lastname VARCHAR(100),
        telephon VARCHAR(100));

INSERT INTO call_center VALUES
        (0, 'Alex_1', 'Black', '89996660000'),
        (0, 'Alex_2', 'Black', '89996660000'),
        (0, 'Alex_3', 'Black', '89996660000'),
        (0, 'Alex_4', 'Black', '89996660000'),
        (0, 'Alex_5', 'Black', '89996660000');


--Таблица №10
DROP TABLE IF EXISTS tech_support;              --Тех поддержка
CREATE TABLE tech_support(
	id SERIAL PRIMARY KEY,
        user_id INT,
	call_agent_id INT,
	question_user TEXT,
	enswer_agent TEXT,
	INDEX (id));

INSERT INTO tech_support VALUES
        (0, 1, 2, 'error = 2342423', 'text support'),
	(0, 5, 1, 'error = 2342423', 'text support'),
	(0, 3, 3, 'error = 2342423', 'text support'),
	(0, 1, 1, 'error = 2342423', 'text support'),
	(0, 4, 4, 'error = 2342423', 'text support');


--Представление №1, JOIN
DROP VIEW IF EXISTS client_get_products;
CREATE VIEW client_get_products AS SELECT
        users.id AS id,
        investments.products_id AS invest_prod,
        card.products_id AS card_prod,
        credit.products_id AS credit_prod,
        insurance.products_id AS insurance_prod
FROM users       
LEFT JOIN investments ON investments.user_id = users.id
LEFT JOIN card ON card.user_id = users.id
LEFT JOIN credit ON credit.user_id = users.id
LEFT JOIN insurance ON insurance.user_id = users.id
ORDER BY id, invest_prod;

SELECT * FROM client_get_products;

--Представление №2, групперовка
DROP VIEW IF EXISTS count_client_get_products;
CREATE VIEW count_client_get_products AS SELECT
        id,
        count(invest_prod) AS invest_prod,                                                       
        count(card_prod) AS card_prod, 
        count(credit_prod) AS credit_prod, 
        count(insurance_prod) AS insurance_prod
FROM client_get_products GROUP BY id ORDER BY id;

SELECT * FROM count_client_get_products;


--Процедура, вложенные таблицы
DELIMITER //

DROP PROCEDURE IF EXISTS mvp;
CREATE PROCEDURE mvp (value INT)
BEGIN
        IF value > (SELECT MAX(id) FROM users) THEN
                SELECT "count user" AS error, (SELECT MAX(id) FROM users) AS last_user_id;
        END IF;

        IF (SELECT invest_prod FROM count_client_get_products WHERE id = value) > 3 THEN
                SELECT value AS users, "investments > 3" AS recomend;
        ELSEIF (SELECT invest_prod FROM count_client_get_products WHERE id = value) = 0 THEN
                SELECT value AS users, "investments = 0" AS recomend;
        END IF;

        IF (SELECT card_prod FROM count_client_get_products WHERE id = value) > 3 THEN
                SELECT value AS users, "card > 3" AS recomend;
        ELSEIF (SELECT card_prod FROM count_client_get_products WHERE id = value) = 0 THEN
                SELECT value AS users, "card = 0" AS recomend;
        END IF;

        IF (SELECT credit_prod FROM count_client_get_products WHERE id = value) > 3 THEN
                SELECT value AS users, "credit > 3" AS recomend;
        ELSEIF (SELECT credit_prod FROM count_client_get_products WHERE id = value) = 0 THEN
                SELECT value AS users, "credit = 0" AS recomend;
        END IF;

        IF (SELECT insurance_prod FROM count_client_get_products WHERE id = value) > 3 THEN
                SELECT value AS users, "insurance > 3" AS recomend;
        ELSEIF (SELECT insurance_prod FROM count_client_get_products WHERE id = value) = 0 THEN
                SELECT value AS users, "insurance = 0" AS recomend;
        END IF;

END //

DELIMITER ;
