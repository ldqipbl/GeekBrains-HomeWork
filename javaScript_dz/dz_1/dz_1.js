/*
	1. Задать температуру в градусах по Цельсию. 
    	Вывести в alert соответствующую температуру в градусах по Фаренгейту. 
    	Подсказка: расчёт идёт по формуле: Tf = (9 / 5) * Tc + 32, где Tf – температура по Фаренгейту, Tc – температура по Цельсию

	2. Объявить две переменные: admin и name. 
	Записать в name строку "Василий"; Скопировать значение из name в admin. 
	Вывести admin (должно вывести «Василий»).

	3. *Чему будет равно JS-выражение 1000 + "108"

	4. *Самостоятельно разобраться с атрибутами тега script (async и defer)
*/


function num_1(){
	var Tc = prompt("Введите температуру по Цельсию");
	var Tf = (9 / 5) * Tc + 32;
	alert("Температура по Фаренгейту = " + Tf);
}

function num_2(){
	var name = "Василий";
	var admin = name;
	alert("admin = " + admin);
}

function num_3(){
	alert("Приоритет канкатинации выше чем у сложения. 1000 + '108' = '1000108'");
}

function num_4(){
	alert(
		`
		defer
		Атрибут defer сообщает браузеру,
		что он должен продолжать обрабатывать страницу и
		загружать скрипт в фоновом режиме, 
		а затем запустить этот скрипт, когда он загрузится.
		
		async
		Если у нас есть несколько скриптов с async, 
		они могут выполняться в любом порядке.
		То, что первое загрузится – запустится в первую очередь
		`
	)
}

function num_5(){
	var a = 10;
	var b = 20;
	b = [a, a = b][0];
	alert("a = 10, b = 20\na = " + a + ", b = " + b);
}


while (true){
	var num_dz = prompt("Какое задание показать:\nзадание №1 (Введите 1),\nзадание №2 (Введите 2),\nзадание №3 (Введите 3),\nзадание №4 (Введите 4),\nзадание №5 (Введите 5),\nвсе задания (Введите all),\nвыход (q)");

	if (num_dz == "q"){
		break;
	}
	else if (num_dz == "1"){
		num_1();
	}
	else if (num_dz == "2"){
		num_2();
	}
	else if (num_dz == "3"){
		num_3();
	}
	else if (num_dz == "4"){
		num_4();
	}
	else if (num_dz == "5"){
                num_5();
        }
	else if (num_dz == "all"){
		num_1();
		num_2();
		num_3();
		num_4();
		num_5();
	}
	else{
		alert("Нет такой команды");
	}

}
