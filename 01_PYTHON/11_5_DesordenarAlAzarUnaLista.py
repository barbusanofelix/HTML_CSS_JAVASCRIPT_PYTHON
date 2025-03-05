'''
PARA HACER EL BARAJADO ALEAORIO HAY QUE IMPORTAR PRIMERO :
import random

En un print no se puede hacer directamente el barajado de una lista.
Por que no? 
La razón por la que no puedes usar random.shuffle() directamente dentro de una función print() en Python es 
que random.shuffle() es una función que modifica la lista en su lugar (in-place), y no devuelve una nueva 
lista barajada.

¿Qué significa "modifica en su lugar"?
Cuando una función modifica una lista "en su lugar", significa que cambia la lista original directamente, 
en lugar de crear una nueva lista.
random.shuffle() toma la lista que le proporcionas y reorganiza sus elementos aleatoriamente. No crea una 
copia nueva de la lista.

¿Qué devuelve random.shuffle()?
La función random.shuffle() devuelve None. Esto significa que no devuelve ningún valor que puedas imprimir 
directamente.
Por lo tanto:
Si intentas print(random.shuffle(mi_lista)), estarías intentando imprimir el valor devuelto por random.shuffle(), 
que es None. Esto resultaría en la impresión de None en la consola.
Para ver la lista barajada, primero debes llamar a random.shuffle(mi_lista) para modificar la lista original, y 
luego llamar a print(mi_lista) para imprimir la lista modificada.

En resumen:
random.shuffle() modifica la lista original directamente. random.shuffle() no devuelve una nueva lista, sino None.
Debes llamar a random.shuffle() por separado y luego imprimir la lista para ver los cambios.
'''


import random

mi_Lista = [1,2,3,4,5,6,7,8,9,10]

random.shuffle(mi_Lista)                        # Aqui hace el bajarado de la lista.
print("Mi Lista ordenada al azar :",mi_Lista)   # No se puede usar directamente dentro del print pues devuelve None