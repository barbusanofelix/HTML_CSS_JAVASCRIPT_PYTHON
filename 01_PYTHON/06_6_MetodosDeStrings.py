# TRABAJAR CON STRINGS
"""Los strings son secuencias de caracteres de texto.
Todos los objetos en Python se engloban en dos categorias: 
    mutables o inmutables.
Los tipos basicos mutables son las LISTAS, los DICCIONARIOS y los SETS.
Los tipos basicos inmutables son los numeros, los STRINGS y las TUPLAS.
Los objetos mutables pueden ser cambiados en el mismo objeto, mientras que los
inmutables no.
"""

# Para concatenar textos se hace con “+” o simplemente con una coma.
# Si ponemos coma nos pone entre los textos un espacio, con + no lo hace.
print("Esta frase" , "termina aqui.")
print("Esta frase " + "termina aqui.")
# Contatenacion y multiplicacion de strings
a = "uno"
b = "dos"
c = a + b       # c es "unodos"
c = a * 3       # c es "unounouno"
#----------------------------------------------
# MÉTODOS DE LOS STRINGS:
# lower(): Convierte en minusculas un string.
s_texto1 = "ESTE TEXTO ESTA INICIALMENTE EN MAYuSCULAS"
print("Convierte texto a minuscula, con variable.lower() :",s_texto1.lower())
# capitalize(): Pone la primera letra en mayuscula.
s_texto2 = "este texto no tenia la primera letra en mayusculas"
print("Coloca primera letra en mayuscula con variable.capitalize() :",s_texto2.capitalize())
# count(): Cuenta cuantas veces aparece una letra o una cadena de caracteres.
s_texto3 = "Vamos a ver cuantas veces aparece la letra c"
print("Cuenta cuantas 'c' hay en el texto.count('c') :", s_texto3.count('c'))
# find(): Representa el indice o la posicion en el cual aparece un caracter o 
# un grupo de caracteres. Si aparece VARIAS VECES ME DICE SOLO EL PRIMERO.
s_texto4 = "Vamos a ver en qué posicion aparece primero la letra e"
print("Indica la primera posicion que aparece la 'e' con variable.find('e'): ", s_texto4.find('e'))
# rfind(): Igual que find() pero contando desde atras.
s_texto5 = "Vamos a ver en qué posicion aparece la palabra desde, contando desde atras"
print("Posicion de derecha-izq, con variable.rfind('desde') :", s_texto5.rfind('desde'))
# isdigit(): Devuelve un boolean, nos dice si el valor introducido es un
# string. Tiene que ser un valor introducido entre comillas o dara error.
s_texto6 = "6"
print('Indica si hay un string en "6" con variable.isdigit() :',s_texto6.isdigit())
# isalnum():  is al ( Alfa ) y num ( numerico)
# Devuelve un boolean, Devuelve verdadero si todos los caracteres de 
# la cadena son numéricos ( 0 a 9) y alfanumericos ( a/A - z/Z). En caso contrario, 
# devuelve falso. Un espacio, o cualquier otro como , por ejemplo como !, #, /, & ...dara false
s_texto7 = "985765456&7"  # "9857654gf7"
print(f"Indica si el string {s_texto7} es solo de numeros con variable.isalnum() :",s_texto7.isalnum())
# isalpha(): Devuelve un boolean, comprueba si hay solo letras. Los espacios no cuentan.
s_texto8 = "Holamundo"
print("Comprueba si solo hay letras en 'Holamundo',los espacios no cuentan. variable.isalpha() : ",s_texto8.isalpha())
# split(): Separa por palabras utilizando espacios. Crea una lista.
s_texto9 = "Vamos a separar esta frase por los espacios"
print(s_texto9.split())
# Podemos usar otro caracter como separador, por ejemplo una coma:
s_texto10 = "Esta seria la primera parte,y esta la segunda"
print('Separa con comas la palabra variable.split(",") : ',s_texto10.split(","))
# strip""(): Borra los espacios sobrantes al principio y al final.
s_texto11 = " En este texto habia espacios al principio y al final "
print("Uso de variable.strip() ",s_texto11.strip())
# replace(): Cambia una palabra o una letra por otra.
s_texto12 = "Vamos reemplazar la palabra casa"
print('Remplaza un texto por otro con variable.replace("casa","hogar") ',s_texto12.replace("casa", "hogar"))
# Convertir a caracteres individuales una cadena de texto.
palabra1="Esta es una casa"
palabra1_ComoLista = list(palabra1)
print(f"Convertimos la palabra1,  {palabra1} a una lista: var.list(palabra1)", palabra1_ComoLista)
# Obtener las vocales que estan dentro de una cadena de usando lo que se llama compresion
palabra2 ="Esta es una forma facil de obtener las vocales"
vocales = [caracter for caracter in  palabra2 if caracter in 'aeioufm'  ]  
print(f"Obtener vocales en {palabra2} : ", vocales)

# Obtener vocales y ciertas letras en una cadena de caracteres
# ciertamente se ubiera podido colocar in 'aeiouxy' pero quise hacer la condicon con un "or" y separa en 2 in
# Ojo, es distinto colocar in 'aeiou' que set{'aeiou'}  el set lleva {} y se refiere a todo el conjunto de letras unidas y no por separadas 

palabra = "Hola mundo xy"
caracteres_especiales = [caracter for caracter in palabra if (caracter.lower() in 'aeiou' or caracter.lower() in 'xy')]
print(f"Obtener 'aeiou' o 'xy' en {palabra} :", caracteres_especiales)  # Salida: ['o', 'a', 'u', 'o', 'x', 'y']

# Te invito a que inspecciones el resto de funciones predefinidas para los
# strings en:
# https://www.freecodecamp.org/espanol/news/metodos-de-string-de-pythonexplicados-con-ejemplo/
