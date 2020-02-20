/*
	1 Установите СУБД MySQL. 
  	Создайте в домашней директории файл .my.cnf, задав в нем логин и пароль, который указывался при установке.
*/
system echo -e "[client]\n user=root\n password=ini" > ~/.my.cnf
system chmod go-rwx ~/.my.cnf


/*
	2 Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, числового id и строкового name.
*/
create database example;
USE example;
create table users ( id int, name varchar(20) );


/*
	3 Создайте дамп базы данных example из предыдущего задания, разверните содержимое дампа в новую базу данных sample.
*/
system mysqldump example > sample.sql	


/*
	4 (по желанию) Ознакомьтесь более подробно с документацией утилиты mysqldump. 
	Создайте дамп единственной таблицы help_keyword базы данных mysql. 
	Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.
*/
