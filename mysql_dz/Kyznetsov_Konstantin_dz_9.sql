/*
					Практическое задание по теме “Транзакции, переменные, представления”

	В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
	Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. 
	Используйте транзакции.

	Создайте представление, которое выводит название name товарной позиции из таблицы products и соответствующее название каталога name из таблицы catalogs.

	(по желанию) Пусть имеется таблица с календарным полем created_at. 
	В ней размещены разряженые календарные записи за август 2018 года '2018-08-01', '2016-08-04', '2018-08-16' и 2018-08-17. 
	Составьте запрос, 
		который выводит полный список дат за август, 
		выставляя в соседнем поле значение 1, 
		если дата присутствует в исходном таблице и 0, 
		если она отсутствует.

	(по желанию) Пусть имеется любая таблица с календарным полем created_at. 
	Создайте запрос, который удаляет устаревшие записи из таблицы, оставляя только 5 самых свежих записей.



					Практическое задание по теме “Администрирование MySQL” (эта тема изучается по вашему желанию)

	Создайте двух пользователей которые имеют доступ к базе данных shop. 
	Первому пользователю shop_read должны быть доступны только запросы на чтение данных, второму пользователю shop — любые операции в пределах базы данных shop.

	(по желанию) Пусть имеется таблица accounts содержащая три столбца id, name, password, содержащие первичный ключ, имя пользователя и его пароль. 
	Создайте представление username таблицы accounts, предоставляющий доступ к столбца id и name. 
	Создайте пользователя user_read, который бы не имел доступа к таблице accounts, однако, мог бы извлекать записи из представления username.



					Практическое задание по теме “Хранимые процедуры и функции, триггеры"

	Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
	С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", 
	с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
	с 18:00 до 00:00 — "Добрый вечер", 
	с 00:00 до 6:00 — "Доброй ночи".

	В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
	Допустимо присутствие обоих полей или одно из них. 
	Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
	Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
	При попытке присвоить полям NULL-значение необходимо отменить операцию.

	(по желанию) Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. 
	Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел. 
	Вызов функции FIBONACCI(10) должен возвращать число 55.

*/


/*
        В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных.
        Переместите запись id = 1 из таблицы shop.users в таблицу sample.users.
        Используйте транзакции.
 */

START TRANSACTION;

SELECT shop FROM users WHERE user_id = 1;

INSERT INTO sample(id, name, birthday_at, created_at, updated_at) VALUES (
	(SELECT id FROM shop WHERE id = 1),
	(SELECT name FROM shop WHERE id = 1),
        (SELECT birthday_at FROM shop WHERE id = 1),
        (SELECT created_at FROM shop WHERE id = 1),
        (SELECT updated_at FROM shop WHERE id = 1));

DELETE FROM shop WHERE id = 1;

COMMIT;


/*
        Создайте представление, которое выводит название name товарной позиции из таблицы products и соответствующее название каталога name из таблицы catalogs.
*/

CREATE VIEW cat AS SELECT products.name AS prod, catalogs.name AS cata FROM products JOIN catalogs ON products.catalog_id = catalogs.id;


/*
        Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
        С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", 
        с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
        с 18:00 до 00:00 — "Добрый вечер", 
        с 00:00 до 6:00 — "Доброй ночи".
 */

DELIMITER //

CREATE FUNCTION hello(value INT)
RETURNS VARCHAR(100) NOT DETERMINISTIC
BEGIN
        DECLARE hour INT;

        SET hour = value;

        CASE 
                WHEN hour <= 5 THEN
                        RETURN "Goodnight";
                WHEN hour <= 11  THEN
                        RETURN "good morning";
                WHEN hour <= 17  THEN
                        RETURN "good afternoon";
                WHEN hour <= 23 THEN
                        RETURN "good evening";
        END CASE;
END//

DELIMITER ;

/*
        В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
        Допустимо присутствие обоих полей или одно из них. 
        Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
        Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
        При попытке присвоить полям NULL-значение необходимо отменить операцию.
 */

DELIMITER //

DROP TRIGGER IF EXISTS products_name_not_null;
CREATE TRIGGER products_name_not_null BEFORE INSERT ON products
FOR EACH ROW
BEGIN
  	IF NEW.name IS NULL AND NEW.desription IS NULL THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'name or description = NULL';
	END IF;

END//

DELIMITER ;
