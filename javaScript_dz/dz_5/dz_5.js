/*
	1. Создать функцию, генерирующую шахматную доску. 
	При этом можно использовать любые html-теги по своему желанию. 
	Доска должна быть разлинована соответствующим образом, т.е. чередовать черные и белые ячейки. 
	Строки должны нумероваться числами от 1 до 8, столбцы – латинскими буквами A, B, C, D, E, F, G, H.

	2. Заполнить созданную таблицу буквами, отвечающими за шахматную фигуру, 
		например К – король, Ф – ферзь и т.п., 
		причем все фигуры должны стоять на своих местах и быть соответственно черными и белыми.

	3. *Заменить буквы, обозначающие фигуры, картинками.
*/

// Порядок фигур в цмкле (l = Лодья, k = Конь, s = Слон, K = Король, F = Ферзь, p = Пешка). Верхние белые (W), нижние черные (B).
var figures_sprit = {
	Wl: "&#9814;", 
	Wk: "&#9816;", 
	Ws: "&#9815;", 
	WK: "&#9812;", 
	WF: "&#9813;", 
	Wp: "&#9817;",
	Bl: "&#9820;", 
	Bk: "&#9822;", 
	Bs: "&#9821;", 
	BK: "&#9818;", 
	BF: "&#9819;", 
	Bp: "&#9823;",
}

// Для удобной вставки на доску.
var arr_figures = [
	figures_sprit.Wl, figures_sprit.Wk, figures_sprit.Ws, figures_sprit.WK, figures_sprit.WF, figures_sprit.Ws, figures_sprit.Wk, figures_sprit.Wl,
	figures_sprit.Wp,
	figures_sprit.Bl, figures_sprit.Bk, figures_sprit.Bs, figures_sprit.BK, figures_sprit.BF, figures_sprit.Bs, figures_sprit.Bk, figures_sprit.Bl,
	figures_sprit.Bp,
]

var arr_liter = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '']


function createDasc(){
	var desc_id = 0;

	// Создаем края (буквы, цыфры), и облость для игры
	for (var i = 1; i < 101; i++){
		// На первой и последней линии вставляем буквы из arr_liter[]
		if (i % 10 == 1 || i % 10 == 0){ document.write("<div>" + arr_liter[Math.ceil(i / 10) - 1] + "</div>") }
		// На верхней и нижней линии вставляем цыфры
		else if (Math.floor(i / 10) == 0 || Math.floor(i / 10) == 9){ document.write("<div>" + (i % 10 - 1) + "</div>") }
		// облость для игры
		else{ document.write("<div class='desc' id='desc_id_" + desc_id++ + "'></div>") }
		
		if (i % 10 == 0){ document.write("<br>") };
	}
        var desc = document.querySelectorAll(".desc");

	// красим нужные квадраты
	for (var i = 0; i < 8 * 8; i++){					// 8 линий по 8 ячеек. 
		if (Math.floor(i / 8) % 2 == 0 && i % 2 == 0){			// На четных линиях берем четные квадраты
			desc[i].style.backgroundColor = "#000";
		}
		else if(Math.floor(i / 8) % 2 != 0 && i % 2 != 0){
			desc[i].style.backgroundColor = "#000";
		}
	};
};

function draw_figures(){
	var desc = document.querySelectorAll(".desc");

	for (var i = 0; i < 64; i++){
		if (i < 8){ desc[i].innerHTML = arr_figures[i] }
		else if (i < 16){ desc[i].innerHTML = arr_figures[8] }
		else if (i == 16){ i += 4 * 8 - 1 }				// пропускаем пустые клетки
                else if (i < 56){ desc[i].innerHTML = arr_figures[17] }
		else if (i < 64){ desc[i].innerHTML = arr_figures[i - 47] }
	};
};



createDasc();
draw_figures();

