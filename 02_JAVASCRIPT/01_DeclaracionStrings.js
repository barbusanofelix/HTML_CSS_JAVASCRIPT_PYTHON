//Declarión de strings
//------------------------
//------------------------
let nombre = "Mi nombre es Angel";
let nombre2 = 'Mi nombre es Angel';
/* 
Aunque declaremos números, si lo hacemos entre comillas, nos lo tratará como strings 
*/
let edad2 = "43";
console.log(edad2+20); // Contanera el 43 con el 20 = 4320
//Las comillas anidadas siempre alternas,
let nombre3 = 'Mi nombre es "Angel" ';
let nombre4 = "Mi nombre es 'Angel' ";
/* 
Cuando declaremos numeros con los que no vamos a operar matemáticamente lo haremos como strings
*/
let telefono = "666666666";
//Los strings no se suman, se concatenan:
let nombre5 = "Angel";
let espacio = " ";
let apellido = "García";
let nombreCompleto =
nombre+espacio+apellido;
console.log(nombreCompleto);
//Otra forma de hacerlo
console.log(nombre5 + " " +apellido);
console.log(nombre5 + " " +edad2);
