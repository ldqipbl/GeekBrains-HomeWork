/*
	Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.

	Подсчитать общее количество лайков, которые получили пользователи младше 10 лет..

	Определить кто больше поставил лайков (всего) - мужчины или женщины?
*/


--        Подсчитать общее количество лайков, которые получили пользователи младше 10 лет..

SELECT count(*) FROM likes WHERE (SELECT birthday FROM profiles WHERE likes.user_id = user_id) > NOW() - INTERVAL 18 year;


--        Определить кто больше поставил лайков (всего) - мужчины или женщины?
--		TODO сравнить.

SELECT 
	(SELECT count(*) FROM likes WHERE (SELECT gender FROM profiles WHERE likes.user_id = user_id) = 'm') as male,
       	(SELECT count(*) FROM likes WHERE (SELECT gender FROM profiles WHERE likes.user_id = user_id) = 'f') as female;

