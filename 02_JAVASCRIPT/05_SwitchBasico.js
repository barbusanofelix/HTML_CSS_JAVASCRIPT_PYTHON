
var edad = 18;
	var imprime = "";
	switch (edad) {
	case 18:
		imprime = "Acabas de cumplir la mayoría de edad";
		break;
	case 25:
		imprime = "Eres un adulto";
		break;
	case 50:
	imprime = "Eres maduro";
	break;
	default:
	imprime = "Otra edad no contemplada"
	break;
	}
console.log(imprime);
// Esta instruccion seria para HTML
// document.write(imprime);