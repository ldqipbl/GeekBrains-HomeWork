/*
	1. Доработать функцию замены картинки в галерее таким образом, чтобы она проверяла наличие картинки по указанному в src адресу.

	2. Реализовать модуль корзины. Создать блок товаров и блок корзины. 
	У каждого товара есть кнопка «Купить», при нажатии на которую происходит добавление имени и цены товара в блок корзины. 
	Корзина должна уметь считать общую сумму заказа.

	3) *Добавить в галерею функцию перехода к следующему изображению. 
	По сторонам от большой картинки должны быть стрелки «вперед» и «назад», 
		по нажатию на которые происходит замена изображения на следующее или предыдущее.
*/


var arr_prod = [
	{
		name: "Барсик ",
		count: 1,					// Количество на складе
		img_src: "img/kot_1.jpg",
		description: "Описание №1",
		price: 100,
	},
	{
		name: "Вася ",
		count: 0,
		img_src: "img/kot_2.jpg",
		description: "Описание №2",
		price: 200,
	},
	{
		name: "Пушок ",
		count: 1,
		img_src: "img/kot_3.jpg",
		description: "Описание №3",
		price: 300,
	},
	{
		name: "Сигизмунд ",
		count: 1,
		img_src: "img/kot_4.jpg",
		description: "Описание №4",
		price: 400,
	},
	{
		name: "Бастет ",
		count: 1,
		img_src: "img/kot_5.jpg",
		description: "Описание №5",
		price: 500,
	},
];



var smoll_img_div = document.querySelectorAll(".smoll_img div");
function inner_el(a){
	if (arr_prod[a].count == 0){
		alert("Этот петомец уже нашёл своих хозяев");
	}
	else {
		document.querySelector(".big_img div img").src = arr_prod[a].img_src;
		document.querySelector(".description_price h3").innerHTML = arr_prod[a].name;
		document.querySelector(".description_price p").innerHTML= arr_prod[a].description;
		document.querySelector(".description_price button").innerHTML= arr_prod[a].price;
	}
};

function inner_el_1(){inner_el(0)};
function inner_el_2(){inner_el(1)};
function inner_el_3(){inner_el(2)};
function inner_el_4(){inner_el(3)};
function inner_el_5(){inner_el(4)};
smoll_img_div[0].addEventListener('click', inner_el_1);
smoll_img_div[1].addEventListener('click', inner_el_2);
smoll_img_div[2].addEventListener('click', inner_el_3);
smoll_img_div[3].addEventListener('click', inner_el_4);
smoll_img_div[4].addEventListener('click', inner_el_5);


var buy_arr = [];
function buy(){
	for (var el of arr_prod){
		if (el.name == document.querySelector(".description_price h3").innerHTML && buy_arr.indexOf(el) === -1){
			buy_arr.push(el);
			document.querySelector(".buy").innerHTML += el.name;
		}
	};
};

document.querySelector(".description_price button").addEventListener('click', buy);





for (var i = 0; i < 4; i++){smoll_img_div[i].style.display = "inline-block"};

