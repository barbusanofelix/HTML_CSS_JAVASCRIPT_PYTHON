
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', 60]
d = dict(zip(keys, values))       # Creamos el diccionario juntando. dict crea diccionario y zip une las listas

for k, v in d.items(): # d.items devuelve tupla con clave, valor
    print('{}: {}'.format(k, v))


for k in d.keys():          # recorre solo la clave
    print(k, end= ' ')
    # salida: apellidos edad nombre

print()
for v in d.values():    # recorre solo el valor
    print(v, end= ' ')
    #salida :Van Rossum 60 Guido

    '''
Tened en cuenta que no podemos acceder directamente a estas listas, sino que tenemos que, o bien 
recorrerlas como hemos visto antes, o bien envolverlas en listas para poder indexarlas, trocearlas, etc.:

d.keys()[1] # No podemos acceder a una vista de diccionario
------------------------------------------------------------
Lo anterior genera un error 
------------------------------------------------------------
Error. Texto omitido por simplicidad TypeError: 'dict_keys' object does not support indexing
-------------------------------------------------------------------------------------------
'''
# En cambio si lo hacemos de la siguiente manera, si podemos acceder a la clave de la posición 2

print("Imprimir la posicion 2 de Key que es Edad ( 0: Nombre, 1:Nombre y 2:Edad )")
print(list(d.keys())[2]) # Si podemos acceder a

 
