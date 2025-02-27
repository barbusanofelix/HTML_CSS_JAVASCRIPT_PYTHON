

letras = list('abcdefghijklmnopqrstuvwxyz')
# Ejemplos de enumerate. Hay que envolverlo en list() o recorrerlo en un for
abcde = sorted(letras) [:5]  # Toma los primeros 5 elementos de la lista ordenada letras
print(abcde)

# Asi le coloca un indice a cada elemento de la lista
print(list(enumerate(abcde)))

# salida es:[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'),(4,'e')]

print(list(enumerate(abcde, 10)))
# salida : [(10, 'a'), (11,'b'),(12,'c'),(13,'d'),(14,'e')]

