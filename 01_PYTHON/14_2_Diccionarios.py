'''
Diccionarios
Los diccionarios, también llamados matrices asociativas, deben su nombre a que son colecciones que relacionan una 
clave y un valor.
Un diccionario es una colección desordenada, modificable e indexada. En Python, los diccionarios se escriben entre 
llaves y tienen claves y valores.
Son estructuras de datos que nos permiten almacenar valores de diferente tipo (números, strings, etc) e incluso 
listas y otros diccionarios.
La principal característica de los diccionarios es que los datos se almacenan asociados a una clave de tal forma 
que se crea una asociación de tipo clave-valor para cada elemento.
Los elementos almacenados no están ordenados.
Ejemplo: Crear e imprimir un diccionario.
'''
dic = {"Nombre":"Santiago","Apellido":"Hernandez","Pais":"España","Ciudad":"Madrid"}
print("1. Imprimo el diccionario, dic               ",dic)
# Otra forma de definir diccionarios con la funcion dict()
dic2 = dict(Nombre="Santiago",Apellido="Hernandez",Pais="España",Ciudad="Madrid")
print("1. Imprimo el diccionario, dic2              ",dic2)
'''
El primer valor se trata de la clave y el segundo del valor asociado a la clave. Como clave podemos utilizar cualquier 
valor inmutable: podríamos usar números, cadenas, booleanos, tuplas… pero NO listas O diccionarios, dado que son mutables. 
Esto es así porque los diccionarios se implementan como tablas hash, y a la hora de introducir un nuevo par clavevalor 
en el diccionario se calcula el hash de la clave para después poder encontrar la entrada correspondiente rápidamente. 
Si se modificara el objeto clave después de haber sido introducido en el diccionario, evidentemente, su hash también
cambiaría y no podría ser encontrado.

METODO              DESCRIPCION
clear()             Borra todos los elementos de un diccionario
copy()              Devuelve una copia de un diccionario
fromkeys()          Devuelve un diccionario con las claves y valores especificados
get()               Devuelve el valor de una clave
items()             Devuelve una lista que contiene una tupla por cada par clave-valor
keys()              Devuelve una lista que contiene las claves del diccionario
pop()               Borra el elemento con la clave especificada
popitem()           Borra el último par clave-valor insertado
setdefault()        Devuelve el valor de la clave especificada. Si no existe, inserta la clave con el valor especificado.
update()            Actualiza el diccionario con el par clave-valor que se especifique
values()            Devuelve una lista con los valores del diccionario


'''

print();print()
