import random

letras = list('abcdefghijklmnopqrstuvwxyz')
vocales = 'aeiou'

random. shuffle(letras)
print(''.join(letras))

print()
print("Modo de hacerlo en otros lenguajes")
for i in range(len(letras)):                                # MODO PROGRAMACION OTROS LENGUAJES
    if letras[i] in vocales:
        print('{} en la posición {}'.format(letras[i], i))
'''
Salida:
a la posición 11
e la posición 12
i la posición 13
o la posición 19
u la posición 22
'''

print()
print("Modo de hacerlo en Python")

# enumerate() nos permite recorrer una lista y obtener tanto el índice como el valor en cada iteración
# Es decir, enumerate le asigna un indice a cada elemento de la lista
for i, letra in enumerate(letras):                          # MODO PROGRAMACION PYTHON
    if letra in vocales:
        print('{} en la posición {}'.format(letra, i))

'''
Salida:
a la posición 11
e la posición 12
i la posición 13
o la posición 19
u la posición 22
'''
# Manera NO Pythónica

# Manera Pythónica