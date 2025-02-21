    var texto="Esto es el texto";
    // Indexof() busca la 1era aparecion de la palabra
	var busqueda= texto.indexOf("texto");
    // lastIndexOf() busca la ultima aparicion de la palabra o letra
    var ultimaUbicacion = texto.lastIndexOf("e");
    // Search() busca la 1era aparicion de la palabra. Funciona igual que IndexOf
    var busqueda2 = texto.search("texto");
    // match funciona igual que search pero con expresion regular muestra las ubicaciones de las letras
    var busqueda3= texto.match(/e/g);  // g es para que busque todas las e. Si colocamos gi busca todas las e y E
    // Substr() busca la palabra y muestra la cantidad de letras que le indiquemos
    var busqueda4 = texto.substring(5,7); // Busca la palabra desde la posicion 5 hasta la 7
    // ChartAt() busca la letra en la posicion que le indiquemos
    var busqueda5 = texto.charAt(5); // Busca la letra en la posicion 5
    // Slice() corta la palabra desde la posicion que le indiquemos
    var busqueda6 = texto.slice(4); // Corta la palabra desde la posicion 5
    // SPLIT() divide la palabra o cadena en un array. Se le puede indicar el separador
    var busqueda7 = texto.split(" "); // Divide la palabra en un array separado por espacio
    busqueda2++;  // Le sumo 1 porque indice empieza con cero
    busqueda++;  // Le sumo 1 porque indice empieza con cero
    ultimaUbicacion++; // Le sumo 1 porque indice empieza con cero
    console.log('Ubicacion de Texto dentro de "${texto}" posicion inicial :${busqueda}');
    console.log(`Ubicacion inicial de texto dentro de "${texto}" posicion inicial :${busqueda}`);
    console.log(`Ubicacion inicial de texto dentro de "${texto}" posicion inicial :${busqueda2} - con search()`);
    console.log(`Ubicacion final de e dentro de "${texto}" posicion final :${ultimaUbicacion}`);
    console.log("las e que contiene son:"+busqueda3);
    console.log("las letras que contiene son:"+busqueda4);
    console.log("la letra que contiene en posicion 5 debe ser una e:"+busqueda5); // Indice desde cero
    console.log("la palabra que contiene desde la posicion 4 es:"+busqueda6); // Indice desde cero
    console.log("la palabra que contiene :"+busqueda7); // Viene del Split y separo todas las palabras entre " "
    