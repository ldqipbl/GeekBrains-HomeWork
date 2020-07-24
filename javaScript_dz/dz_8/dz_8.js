/*
	1. Для практикума из занятия 7 продумать, где можно применить замыкания.


	2. Не выполняя кода, ответить, что выведет браузер и почему:

	if (!("a" in window)) { var a = 1 }
	alert(a);

	var b = function a(x) { x && a(--x) };
	alert(a);

	function a(x) { return x * 2 }
	var a;
	alert(a);

	function b(x, y, a) { arguments[2] = 10; alert(a); }
	b(1, 2, 3);

	function a() { alert(this) }
	a.call(null)i;
*/

//if (!("a" in window)) { var a = 1 ;}
//alert(a);		// undefined

//var b = function a(x) { x && a(--x) };
//alert(a);		// Error a = undefine

//function a(x) { return x * 2 };
//var a;
//alert(a);		// a = function a(x) { return x * 2 }

//function b(x, y, a) { arguments[2] = 10; alert(a); };
//b(1, 2, 3);		// a = 10

//function a() { alert(this) };
//a.call(null);		// obj.windiws 
