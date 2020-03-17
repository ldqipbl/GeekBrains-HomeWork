/*
	Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.

	Выведите список товаров products и разделов catalogs, который соответствует товару.

	(по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
	Поля from, to и label содержат английские названия городов, поле name — русское. 
	Выведите список рейсов flights с русскими названиями городов.
*/


--        Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.

SELECT * FROM users WHERE (SELECT user_id FROM orders) = id;


--        Выведите список товаров products и разделов catalogs, который соответствует товару.

SELECT id, name, catalog_id FROM products WHERE catalog_id IN (SELECT id FROM catalogs);
