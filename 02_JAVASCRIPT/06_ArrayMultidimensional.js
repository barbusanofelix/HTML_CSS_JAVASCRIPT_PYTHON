var peliculas = ['Batman', 'Cars', 'It'];
var categoria = ['Acción', 'infantil', 'Terror'];
var cine = [peliculas, categoria];
console.log(cine);
console.log("Nombre pelicula :" + cine[0][1]);// 0 se refiere a peliculas y 1 a posicion 1 en peliculas : Cars
console.log("Nombre categoria :" + cine[1][1]); //1_se refiere a categoria y 1 a posicion 1 en categoria : infantil