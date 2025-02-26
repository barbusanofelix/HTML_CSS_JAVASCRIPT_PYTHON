# Obtener la dirección de memoria de una variable
a = 65
print("1.La dirección de memoria de a = 65 es              " , id(a))
# Obtener la dirección de memoria de una variable que apunta a otra
miNumero = 65
miNumero2 = miNumero
print("2.La dirección de memoria de miNumero = 65 es       " , id(miNumero))
print("2.La dirección de memoria de miNumero2 = miNumero  es" , id(miNumero2))
# Si cambio la variable, realmente creo una copia en otra dirección de memoria:
a = 65
print("4.La dirección de memoria de a = 65 es             " , id(a))
a+=2
print("5.La dirección de memoria a+=2 es                  " , id(a))
# Obtener la dirección de memoria de una tupla. Las tuplas son inmutables ( no se pueden cambiar)
a = (1, 2, 3, 4, 5)
print("6.La dirección de memoria de a = (1, 2, 3, 4, 5) es" , id(a))
# Obtener la dirección de memoria de una lista
a = [1, 2, 3, 4, 5]
print("7.La dirección de memoria de a = [1, 2, 3, 4, 5] es" ,id(a))
# Obtener la dirección de memoria de un diccionario
a = {'a': 1, 'b': 2}   # Crea un diccionario y para ello se usan las llaves {}
print(a)
print("8.La dirección de memoria de a = {'a': 1, 'b': 2} es" , id(a))
a["c"] = 3  # Los [ ] se usan para añadir o modificar elementos a un diccionario, entonces esto se refiere al diccionario
print(a)
# El id(a) sigue siendo el mismo porque es el mismo diccionario aunque se le haya añadido un valor
print('9.La dirección de memoria de a["c"] = 3 es            ' ,id(a))