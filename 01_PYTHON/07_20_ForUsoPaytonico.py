'''
En este ejemplo estamos troceando la lista letras en tres partes, luego barajamos cada una de las partes y
recorremos las tres listas simultáneamente para ir mostrando en pantalla una letra de cada lista en cada
iteración. La versión Pythónica utiliza la función zip, que ya habíamos visto antes. La única diferencia es
que, en este caso, en lugar de unir dos listas estamos haciéndolo con tres. La gran ventaja de zip (además
de ser más legible) es que no tenemos que preocuparnos de que todas las listas sean de igual
longitud. Cuando una de las listas se termina, zip detiene la ejecución. En la alternativa no Pythónica,
tendríamos que consultar las longitudes de cada lista y recorrer el bucle siguiendo los índices de la lista
más corta
'''



import random
letras = list('abcdefghijklmnopqrstuvwxyz' )  # Una lista de letras

l1 = letras[: 8]    # Hace una lista de letras de 0 a 8
l2=  letras[8:16]   # Hace una lista de letras de 8 a 16
l3 = letras[16:]    # Hace una lista de letras de 16 al final

print(l1)
print(l2)
print(l3)

random. shuffle(l1) # Baraja la lista l1. Y la almacena en l1
random. shuffle(l2) # Baraja la lista l2. Y la almacena en l2
random. shuffle(l3) # Baraja la lista l3. Y la almacena en l3

print(l1)   # Imprime la lista l1 barajada
print(l2)   # Imprime la lista l2 barajada
print(l3)   # Imprime la lista l3 barajada

for i in range(len(l1)):                        # MODO USUAL EN OTROS LENGUAJES DE PROGRAMACION.
    print(l1[i] + l2[i] + l3[i], end=' ')

# salida :la letra de cada lista en la posicion i
print()
# zip une las 3 listas en trio.  El ciclo se ejecutara hasta la longitud de la lista mas corta.
# a , b, c : toma la posicion de cada una en las listas , en el mismo indice.
for a, b, c in zip(l1, l2, l3):                 # METODO RECOMENDADO EN PYTHON
    print(a + b + c, end=' ')

