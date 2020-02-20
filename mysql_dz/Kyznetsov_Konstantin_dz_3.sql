USE vk; -- Не пишу DROP/CREATE т.к. в задании добавить
/*
	
    Написать крипт, 
	добавляющий в БД vk, которую создали на занятии, 
	3 новые таблицы 
	(с перечнем полей, указанием индексов и внешних ключей)

 */

DROP TABLE IF EXISTS tbl_1;		-- Таблица 1
CREATE TABLE tbl_1 (
	id SERIAL PRIMARY KEY,		-- поле 1 (перечень полей)
	column_1 INT,			-- поле 2 (перечень полей)	
	column_2 VARCHAR(20),		-- поле 3 (перечень полей)
	INDEX (column_1)		-- index без имени т.к. д\з не указано.
);

DROP TABLE IF EXISTS tbl_2; 		-- Таблица 2
CREATE TABLE tbl_2 (
        id SERIAL PRIMARY KEY,
        column_1 INT,
        column_2 VARCHAR(20),
        INDEX (column_2(10))
);

DROP TABLE IF EXISTS tbl_3; 		-- Таблица 3
CREATE TABLE tbl_3 (
        id SERIAL PRIMARY KEY,
        column_1 INT,
        column_2 VARCHAR(20),
        INDEX (column_1, column_2(10))
);


ALTER TABLE tbl_2
ADD CONSTRAINT fk_user_id
FOREIGN KEY (id) REFERENCES tbl_1(id) 	-- Внешний ключь
ON UPDATE CASCADE ON DELETE restrict;
