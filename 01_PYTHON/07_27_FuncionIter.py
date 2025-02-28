
lista = [1, 2, 3,4]
iterador = iter(lista)
print(iterador) # salida <list_iterator object at 0x7f7f3c1b5b20>
print(next(iterador)) # salida 1
print(next(iterador)) # salida 2 
print(next(iterador)) # salida 3
print(next(iterador)) # salida 4
# En el siguiente print se produce una excepción StopIteration porque no hay más elementos en la lista y se le pide uno más
# print(next(iterador)) # StopIteration

for i in iter(lista):
    print(i, lista[i-1])  # La i inicio en 1 y la lista en 0


    # QUEDE EN PAG 29
