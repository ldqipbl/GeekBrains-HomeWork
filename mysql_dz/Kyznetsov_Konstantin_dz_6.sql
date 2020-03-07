/*
	Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.

	Подсчитать общее количество лайков, которые получили пользователи младше 10 лет..

	Определить кто больше поставил лайков (всего) - мужчины или женщины?
*/

--      Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.

SELECT count(*) AS max_num FROM media WHERE 
	user_id IN (
		SELECT initiator_user_id FROM friend_requests WHERE (target_user_id = 10) AND status='approved' 
		union 
		SELECT target_user_id FROM friend_requests WHERE (initiator_user_id = 10) AND status='approved') 
	GROUP BY user_id 
	ORDER BY max_num DESC LIMIT 1;


--      Подсчитать общее количество лайков, которые получили пользователи младше 10 лет..

SELECT count(*) FROM likes WHERE (SELECT birthday FROM profiles WHERE likes.user_id = user_id) > NOW() - INTERVAL 18 year;


--      Определить кто больше поставил лайков (всего) - мужчины или женщины?

SELECT 
	(SELECT count(*) AS gender FROM likes WHERE (SELECT gender FROM profiles WHERE likes.user_id = user_id) = 'm') AS gender 
	union 
	(SELECT count(*) FROM likes WHERE (SELECT gender FROM profiles WHERE likes.user_id = user_id) = 'f') 
	ORDER BY gender DESC LIMIT 1;
