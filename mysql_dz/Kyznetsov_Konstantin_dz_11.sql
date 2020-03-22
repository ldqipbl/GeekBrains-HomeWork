/*
						Практическое задание по теме “Оптимизация запросов”
	
	Создайте таблицу logs типа Archive. 
	Пусть при каждом создании записи в таблицах 
		users, catalogs и products в таблицу logs помещается
	       	время и дата создания записи, название таблицы, идентификатор первичного ключа и содержимое поля name.

	(по желанию) Создайте SQL-запрос, который помещает в таблицу users миллион записей.


						Практическое задание по теме “NoSQL”

	В базе данных Redis подберите коллекцию для подсчета посещений с определенных IP-адресов.
	
	При помощи базы данных Redis решите задачу поиска имени пользователя по электронному адресу и наоборот, поиск электронного адреса пользователя по его имени.

	Организуйте хранение категорий и товарных позиций учебной базы данных shop в СУБД MongoDB.

 */


/*
        Создайте таблицу logs типа Archive. 
        Пусть при каждом создании записи в таблицах users, catalogs и products 
		в таблицу logs помещается время и дата создания записи, название таблицы, идентификатор первичного ключа и содержимое поля name.
*/

DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
	date_and_time DATETIME,
	name_table VARCHAR(100),
	pramoru_key_id INT,
	value_colomn_name VARCHAR(255)) ENGINE=Archive;


DELIMITER //

DROP TRIGGER IF EXISTS lods_users;
CREATE TRIGGER lods_users AFTER INSERT ON users
FOR EACH ROW
BEGIN
  	INSERT INTO logs VALUES (NOW(), 'users', (SELECT MAX(id) FROM users), NEW.name);
END//


DROP TRIGGER IF EXISTS lods_catalogs;
CREATE TRIGGER lods_catalogs AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
        INSERT INTO logs VALUES (NOW(), 'catalogs', (SELECT MAX(id) FROM catalogs), NEW.name);
END//


DROP TRIGGER IF EXISTS lods_products;
CREATE TRIGGER lods_products AFTER INSERT ON products
FOR EACH ROW
BEGIN
        INSERT INTO logs VALUES (NOW(), 'products', (SELECT MAX(id) FROM products), NEW.name);
END//


DELIMITER ;


/*
        В базе данных Redis подберите коллекцию для подсчета посещений с определенных IP-адресов.
 */

SADD '192.168.0.0' 'DATETIME_1' 'DATETIME_2' 'DATETIME_3'
SADD '192.168.1.1' 'DATETIME_1' 'DATETIME_2'
SADD '192.168.1.2' 'DATETIME_1'

SCARD 192.168.0.0

/*
        При помощи базы данных Redis решите задачу поиска имени пользователя по электронному адресу и наоборот, поиск электронного адреса пользователя по его имени.
*/

HMSET admin name_1 "values_1@***" name_2 "values_2@***" name_3 "values_3@***"
HVALS admin
HGET admin name_3


/*
        Организуйте хранение категорий и товарных позиций учебной базы данных shop в СУБД MongoDB.
*/

db.shop.insert({name: 'categories'})
db.shop.insert({name: 'ovarian positions'})

