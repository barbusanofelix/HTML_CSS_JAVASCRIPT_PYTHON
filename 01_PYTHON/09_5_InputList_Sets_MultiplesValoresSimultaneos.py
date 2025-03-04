'''
Las listas y los Set son mutables: Es decir, pueden tener cualquier valor de elementos y se le pueden
añadir o eliminar elementos.

Listas (lists):
Ordenadas: Los elementos en una lista mantienen un orden específico, y puedes acceder a ellos mediante índices.
Mutables: Puedes modificar los elementos de una lista, añadir nuevos elementos o eliminar existentes.
Permiten duplicados: Una lista puede contener múltiples ocurrencias del mismo elemento.
Casos de uso:
Almacenar una secuencia ordenada de elementos.
Cuando el orden de los elementos es importante.
Cuando necesitas permitir elementos duplicados.

Conjuntos (sets):
No ordenados: Los elementos en un conjunto no tienen un orden específico, y no puedes acceder a ellos mediante índices.
Mutables: Puedes añadir o eliminar elementos de un conjunto, pero no puedes modificar los elementos existentes.
No permiten duplicados: Un conjunto solo puede contener elementos únicos. Si intentas añadir un elemento duplicado, se ignorará.
Casos de uso:
Almacenar una colección de elementos únicos.
Realizar operaciones de conjuntos, como unión, intersección y diferencia.
Eliminar duplicados de una colección.
Ventajas de los conjuntos sobre las listas:

Eficiencia en la búsqueda: Los conjuntos son muy eficientes para verificar si un elemento pertenece a la colección. La búsqueda en un conjunto es mucho más rápida que en una lista, especialmente para colecciones grandes.
Operaciones de conjuntos: Los conjuntos proporcionan operaciones eficientes para realizar uniones, intersecciones y diferencias entre colecciones.
Eliminación de duplicados: Los conjuntos eliminan automáticamente los duplicados, lo que puede ser útil cuando necesitas trabajar con elementos únicos.
Ventajas de las listas sobre los conjuntos:

Orden: Las listas mantienen el orden de los elementos, lo que es importante en muchos casos.
Acceso por índice: Puedes acceder a los elementos de una lista mediante su índice, lo que no es posible en un conjunto.
Permiten duplicados: Las listas permiten elementos duplicados, lo que puede ser necesario en algunos casos.
En resumen:

Si necesitas una colección ordenada de elementos y permites duplicados, usa una lista.
Si necesitas una colección de elementos únicos y realizar operaciones de conjuntos, usa un conjunto.


'''

Lista = list()
Set = set()

print("Introduce datos para la Lista")
Lista = list(map(int,input("Introduce n valores separados por comas : " ).split(",")))

print("Introduce datos para el Set")
Set = set(map(int,input("Introduce n valores separados por comas : " ).split(",")))

ListaOrdenada = list()
ListaOrdenada = Lista.copy() # Crea una nueva lista ordenada . Si aplicamos List.sort() la ordena pero la sobreescribe.
ListaOrdenada.sort() # Ordena la lista  

print("La Lista original fue ", Lista)
print("La lista ordenada es  ", ListaOrdenada)

print()
print("Los Sets NO se pueden ordenar y tampoco permite repetir elementos")
print("El Set original fue  ", Set)
print()
print("Posemos convertir el set en una list() y asi ordenarlo")
ListaDelSet= list(Set)
print("El Set convertido en Lista es ", ListaDelSet)
print('Ahora el "Set" ( realmente ya es una lista) es', ListaDelSet)

ListaDelSet.sort()
print("Ahora el Set ordenado es :", ListaDelSet)
Set =set(ListaDelSet)
print("El Set nuevamente convertido en Set es ", Set)
