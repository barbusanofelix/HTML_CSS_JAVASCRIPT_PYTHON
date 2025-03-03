# LISTAS
"""
La lista es un tipo de colección ordenada y modificable.
Es decir, una secuencia de valores de cualquier tipo, ordenados y de tamaño variable.
Se escriben entre corchetes. []
"""
miLista1=["Angel", 43, 667767250]
miLista2 = [22, True, "una lista", [1,2]]


# MÉTODOS DE LAS LISTAS # Hacer una lista de una cadena
miLista = list("PYTHON")
print(miLista)

# Acceder a los elementos de una lista
miLista = [22, True, "una cadena", [1,2]]
print(miLista[0])

print("miLista = [[1,2] , [3,4] , [5,6]]" )
print("Sus indices son")
print("             0       1       2   , para cada par de valores")
print("            Para valor individual dentro de los pares seria 0 y 1    ")
print("            Asi para el 4, de la 2da pareja, debe ser miLista[1][1]         ")
miLista = [[1,2] , [3,4] , [5,6]]

miVar = miLista[1][1]  # El primer indice se refiere a la pareja [3,4] Posicion 1 ( 0,1,2) y el 2do  dentro de la tupla , 1=4
print(miVar)
 
print()
# Crea una lista combinada, partiendo de mi lista 
miLista = [[1, 2], [3, 4], [5, 6]]
parejas = []

for i in miLista[0]:  # Itera sobre los elementos de la primera sublista [1, 2]
    for j in miLista[1]:  # Itera sobre los elementos de la segunda sublista [3, 4]
        parejas.append((i, j))  # Añade la pareja (i, j) a la lista 'parejas'
    for k in miLista[2]: # Itera sobre los elementos de la tercera sublista [5,6]
        parejas.append((i, k))

print(parejas) # salida [(1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6)]

miLista = [[1, 2], [3, 4], [5, 6]]
parejas = []

for i in miLista[0]:  # Itera sobre [1, 2]
    for j in range(1, 3): # Itera sobre 1 y 2 para acceder a la segunda y tercera lista
        parejas.append((i, miLista[j][i -1])) # miLista[1][0], miLista[2][0], miLista[1][1], miLista[2][1]

print(parejas) #salida : [(1, 3), (1, 5), (2, 4), (2, 6)]

print()
# Función con una lista como parámetro
def miFunccion(listaFrutas):
    for x in listaFrutas:
        print(x)

frutas = ["Manzana", "banana", "cereza"]
miFunccion(frutas)