var precio=30000;

// para usar en HTML
//var dinero=prompt("Introduce cuanto dinero tienes: ");
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  var dinero=0;

  readline.question('Introduce la cantidad de dinero: ', (cantidad) => {
    var dinero = parseFloat(cantidad); // Convierte la entrada a número
    if (isNaN(dinero)) {
      console.log('La cantidad introducida no es un número válido.');
    } else {
      console.log(`Tienes ${dinero} unidades de dinero.`);
    }
    readline.close();
  });

	if(dinero>precio){
		console.log("Te puedes comprar el coche");
        //alert("Te puedes comprar el coche");
	}else{
		//alert("Te vas en autobus");
        console.log("Te vas en autobus");
	}
