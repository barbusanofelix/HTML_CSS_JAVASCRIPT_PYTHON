'''
ENTRADA DE DATOS EN TUPLAS
Sabemos que las tuplas son inmutables, no hay métodos disponibles para agregar elementos a las
tuplas. Para agregar un nuevo elemento a una tupla, primero deberemos convertir la tupla en lista, 
luego agregaremos el elemento a la lista y nuevamente convertiremos la lista en una tupla.
'''

T = (2, 3, 4, 5, 6)   # Define la Tupla
print("Tupla inicial")
print(T)
L = list(T)
L.append(int(input("Introduzca el nuevo elemento: ")))
L.sort()  # Ordenamos la Lista L 
T = tuple(L)  # sobre-esceibe la Tupla T
print("Tupla final")
print(T)
print("La T es del tipo", type(T))