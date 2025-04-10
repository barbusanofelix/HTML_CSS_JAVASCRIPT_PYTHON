"""
LOS PARAMETROS DE RANGE SON :
range(inicio, <>fin , paso)
    * inicio    : El valor de inicio. Siempre es inclusivo....es decir, inicia en ese valor.
    * <>fin     :

Pasar Range a Lista.

Definimos el range y luego le hacemos un Casting para convertirlo en lista.

El range no es una lista y por eso no es recorrible.

El range funciona:
range(10)       : Rango de 0 a 9 ( Siempre el último no va incluido)
range(10,2,-1)  : Ahora el 10 es valor inicial, el 2 es hasta donde llegará, pero siempre llega 2+1 ( 2 es < 10 y es descendente ) y -1 indica que avanzará de 1 en 1

"""
num = range(-2,10,1)    # Crea un rango de -2 a 10 , sin incluir el 10.
num_lista = list(num)   # Lo convierte en lista


print("imprimo num que tiene range(-2,10,1) :", num)                        #salida range(-2, 10)
print("Imprimo num_lista que tiene el casteo de list(num) :",num_lista)     # salida : [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num1 = range(1,20,2)    # Crea un rango de -2 a 10 , sin incluir el 10.
num_lista1 = list(num1)   # Lo convierte en lista

print("imprimo num que tiene range(-2,10,1) :", num1)                        # salida range(1, 20, 2)
print("Imprimo num_lista que tiene el casteo de list(num) :",num_lista1)     # salida : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Con Variables:

# Definimos variables para los parámetros de range
inicio = 5
fin = 20
paso = 3

# Usamos la función range con las variables
mi_rango = range(inicio, fin, paso)

# Iteramos sobre el rango para ver los valores que genera
print("\nValores generados por range, recorriendo el rango range(5, 20 ( <20), 3):")
for numero in mi_rango:
    print(numero)

# También podemos convertir el rango a una lista para ver todos los valores de una vez
lista_de_rango = list(mi_rango)
print("\nLista creada a partir del rango, range(5, 20 ( <20), 3):", lista_de_rango)  # salida [5, 8, 11, 14, 17]

# Ejemplo con un paso negativo para generar una secuencia descendente
inicio_descendente = 10
fin_descendente = 1
paso_descendente = -2

rango_descendente = range(inicio_descendente, fin_descendente, paso_descendente)

print("\nValores generados por range descendente:Recorriendo el rango")
for numero in rango_descendente:
    print(numero)

lista_descendente = list(rango_descendente)
print("\nLista creada a partir del rango descendente:", lista_descendente)    # salida [10, 8, 6, 4, 2]