'''
RECURSIVIDAD EN UNA LISTA PARA SUMAR SUS ELEMENTOS

Esta función calcula la suma de los elementos de una lista num_List utilizando recursividad.

Caso base:
if len(num_List) == 1:: Esta línea verifica si la longitud de la lista es 1. Si la longitud es 1, significa que la 
lista solo tiene un elemento.
return num_List[0]: En este caso, la función devuelve el único elemento de la lista. Este es el caso base que detiene 
la recursividad.

Caso recursivo:
else: Si la longitud de la lista no es 1, se ejecuta este bloque.
return num_List[0] + list_sum(num_List[1:]): Aquí es donde ocurre la recursividad: num_List[0]: Se toma el primer elemento de 
la lista. 
num_List[1:]: Se crea una nueva lista que contiene todos los elementos de num_List excepto el primero.
list_sum(num_List[1:]): Se llama a la función list_sum de nuevo, pero esta vez con la nueva lista más corta.
El resultado de la llamada recursiva se suma al primer elemento de la lista original.

Ejecución paso a paso:
Vamos a seguir la ejecución de list_sum([2, 5, 8, 9, 9]):

list_sum([2, 5, 8, 9, 9]):
La longitud de la lista es 5, así que no es el caso base.
La función devuelve 2 + list_sum([5, 8, 9, 9]).

list_sum([5, 8, 9, 9]):
La longitud de la lista es 4, así que no es el caso base.
La función devuelve 5 + list_sum([8, 9, 9]).

list_sum([8, 9, 9]):
La longitud de la lista es 3, así que no es el caso base.
La función devuelve 8 + list_sum([9, 9]).

list_sum([9, 9]):
La longitud de la lista es 2, así que no es el caso base.
La función devuelve 9 + list_sum([9]).

list_sum([9]):
La longitud de la lista es 1, así que es el caso base.
La función devuelve 9.

Ahora, las llamadas recursivas se resuelven en orden inverso:
9 + 9 = 18
8 + 18 = 26
5 + 26 = 31
2 + 31 = 33
Finalmente, list_sum([2, 5, 8, 9, 9]) devuelve 33.

En resumen:
La recursividad funciona dividiendo el problema en subproblemas más pequeños y resolviendo cada subproblema de la misma manera.
El caso base es esencial para detener la recursividad y evitar un bucle infinito.
Cada llamada recursiva reduce el tamaño de la lista hasta que se alcanza el caso base.

'''


def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])

# CORAZON DEL PROGRAMA    
print(list_sum([2, 5, 8, 9, 9]))