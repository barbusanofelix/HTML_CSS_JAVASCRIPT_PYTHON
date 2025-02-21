//Podemos trabajar con números, strings y booleans
	// Declaración de variables:
	// No puede empezar por un número
	// Esto de error: var 2_cliente;
	// Evitar tildes y Ñ
	//Variable correctamente declarada let _numero;
	// Inicialización de la variable
		_numero = 63;
	//Variable declara e inicializada
		var numero4 = 647;
	// Sepueden declara e inicializar varias variables a la vez.
		var a=3, b=4, c=5;
	//Sería lo mismo que poner:
	/*
		var a=3;
		let b=4;
		var c=5;
	*/
	// JavaScript es Case sensitive.
	//Distingue entre mayúsculas/minúsculas
		var numero = 10;
		var Numero = 20;
	console.log("La variable 'numero' vale:" + numero);
	console.log("La variable 'Numero' vale:"+ Numero);
	//Con variable numéricas podemos operar matemáticamente
		var sumando1 = 35;
		var sumando2 = 45;
		var resultado = sumando1+sumando2;

		console.log("El resultado de sumar " + sumando1 + " + " + sumando2 + " es " + resultado);
// Operador modulo o resto de la división
var resto = 46 % 5;
console.log("El resto de 46/5 es " + resto);
//Operador incremento
	var numeroInicial = 10;
	let numeroIncrementado = ++numeroInicial;
//Sería como poner que
//numeroIncrementado = numeroInicial +1;
console.log("El operador incremento sobre numeroInicial daría " + numeroIncrementado);
//IMPORTANTE: No es lo mismo ++variable que variable++
var numero5 = 5;
console.log("El número antes del incremento vale " + numero5++);
console.log("")
console.log("El número después del incremento vale " + numero5);
console.log("");
console.log("");
// Ahora al revés
let numero6 = 5;
console.log("El número antes del incremento vale " + ++numero6);
console.log("");
console.log("El número después del incremento vale " + numero6);
//Constantes. Como las variables pero no se puede cambiar su valor
// Se declaran en mayúsculas
const MICONSTANTE = 4765;
// MICONSTANTE = 345;//Esto daría error
// Hay que declararlas e inicializarlas obligatoriamente.
//const MICONSTANTE2; Esto daría error
console.log("El valor de la constante MICONSTANTE es " + MICONSTANTE);
