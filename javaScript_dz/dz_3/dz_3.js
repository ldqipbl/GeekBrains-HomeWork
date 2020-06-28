/*
	1. С помощью цикла while вывести все простые числа в промежутке от 0 до 100.

	2. С этого урока начинаем работать с функционалом интернет-магазина. 
	Предположим, есть сущность корзины. 
	Нужно реализовать функционал подсчета стоимости корзины в зависимости от находящихся в ней товаров.

	3. Товары в корзине хранятся в массиве. Задачи:
		a) Организовать такой массив для хранения товаров в корзине;
		b) Организовать функцию countBasketPrice, которая будет считать стоимость корзины.

	4.*Вывести с помощью цикла for числа от 0 до 9, не используя тело цикла. Выглядеть это должно так:

		for(…){// здесь пусто}

	5. *Нарисовать пирамиду с помощью console.log, как показано на рисунке, только у вашей пирамиды должно быть 20 рядов, а не 5:

		x
		xx
		xxx
		xxxx
		xxxxx
*/

function num_1(){
	var arrNumbers = [];
	var i = 2, flag;

	while(i <= 100){
		flag = 0;

                for(var el of arrNumbers){
                        if(i % el == 0){
                                flag = 1;
                                break;
                        }
                };

                if(flag == 0){arrNumbers.push(i)};

		++i;
	}

	console.log(arrNumbers);
}

function num_2_3(){
	var arr = [
		{
			name: "prod_1",
			prise: 100,
			count: 1
		},
		{
			name: "prod_2",
                        prise: 200,
                        count: 2
		},
		{
			name: "prod_3",
                        prise: 300,
                        count: 3
		}
	]

	function countBasketPrice(){
		for (var i = 0, sum = 0; i < arr.length; i++){
			sum += arr[i].prise * arr[i].count;
		};

		return sum;
	}

	console.log(countBasketPrice())
}

function num_4(){
	for (var i = 0; i < 10; console.log(i++)){}
}

function num_5(){
	for (var i = 0, str = "x"; i <= 20; i++){
		console.log(str);
		str += "x";
	}
}


num_1()
num_2_3()
num_4()
num_5()
