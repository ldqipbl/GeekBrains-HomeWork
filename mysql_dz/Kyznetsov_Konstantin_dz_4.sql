/*
	Не получилось добавить рандомные значения через filldb. 
		Использовал БД из прошлой домашней работы т.к. таблиц заполнять меньше, а суть работы таже.
*/

DROP DATABASE IF EXISTS vk;
CREATE DATABASE vk;

USE vk;

DROP TABLE IF EXISTS tbl_1;             -- Таблица 1
CREATE TABLE tbl_1 (
	id SERIAL PRIMARY KEY,          -- поле 1 (перечень полей)
	year INT,	                -- поле 2 (перечень полей)
	firstname VARCHAR(20),          -- поле 3 (перечень полей)
	INDEX (year)                	-- index.
);

DROP TABLE IF EXISTS tbl_2;             -- Таблица 2
CREATE TABLE tbl_2 (
	id SERIAL PRIMARY KEY,
	year INT,
	firstname VARCHAR(20),
	INDEX (firstname(10))
);

DROP TABLE IF EXISTS tbl_3;             -- Таблица 3
CREATE TABLE tbl_3 (
	id SERIAL PRIMARY KEY,
	year INT,
	firstname VARCHAR(20),
	INDEX (year, firstname(10))
);


/*
        i. Заполнить все таблицы БД vk данными (по 10-100 записей в каждой таблице)

        ii. Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке

        iii. Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false). 
                Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)

        iv. Написать скрипт, удаляющий сообщения «из будущего» (дата позже сегодняшней). 
		Не понятно 'дата позже сегодняшней' на момент запуска скрипта или на момент вэбинара.

        v. Написать название темы курсового проекта (в комментарии)
 */

--Заполнить все таблицы БД vk данными (по 10-100 записей в каждой таблице)
INSERT INTO tbl_1 (year, firstname) VALUES 
	(11, 'LEO'), (12, 'NIK'), (13, 'PIT'), (14, 'IOJ'), (15, 'OIKN'), (16, 'MKU'), (17, 'DTR'), (18, 'NNU'), (19, 'PLKM'), (110, 'PLKMG');

INSERT INTO tbl_2 (year, firstname) VALUES 
	(11, 'LEO'), (12, 'NIK'), (13, 'PIT'), (14, 'IOJ'), (15, 'OIKN'), (16, 'MKU'), (17, 'DTR'), (18, 'NNU'), (19, 'PLKM'), (110, 'PLKMG');

INSERT INTO tbl_3 (year, firstname) VALUES 
	(11, 'LEO'), (12, 'NIK'), (13, 'PIT'), (14, 'IOJ'), (15, 'OIKN'), (16, 'MKU'), (17, 'DTR'), (18, 'NNU'), (19, 'PLKM'), (110, 'PLKMG');

--Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке
SELECT distinct firstname FROM tbl_1 ORDER BY firstname;

--Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false). 
--Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)
ALTER TABLE tbl_1 ADD is_active VARCHAR(20) DEFAULT 'true';
UPDATE tbl_1 SET is_active = 'false' WHERE year < 18;

--Подготовка к 4 заданию
ALTER TABLE tbl_2 ADD (text VARCHAR(20), data VARCHAR(100));
UPDATE tbl_2 SET data = NOW();
UPDATE tbl_2 SET text = 'from the future', data = NOW() + INTERVAL 14 DAY WHERE year > 16;

SELECT * FROM tbl_2;

--Написать скрипт, удаляющий сообщения «из будущего» (дата позже сегодняшней). 
--	Не понятно 'дата позже сегодняшней' на момент запуска скрипта или на момент вэбинара.
UPDATE tbl_2 SET text = 'DELETE' WHERE data > NOW();

SELECT * FROM tbl_2;

--Написать название темы курсового проекта (в комментарии)

--	Еще не решил. Планирую зделать БД bigdata. Если найду пример какие колонки и значения должны быть.
