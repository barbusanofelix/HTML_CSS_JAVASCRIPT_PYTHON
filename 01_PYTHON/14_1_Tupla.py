# Tuplas.
'''
Tuplas
Las tupas son un tipo de dato complejo y particular del lenguaje de programación Python. Una tupla es un objeto idéntico a una lista excepto por las 
siguientes propiedades:
• Al igual que las listas, definen una colección ordenada de objetos, sin embargo, utilizan la sintaxis (obj1, obj2, ..., objn) en lugar de 
  [obj1,obj2, ..., objn]
• Las tuplas son inmutables, es decir, no se pueden modificar después de su creación.
• No permiten añadir, eliminar, mover elementos (no append, extend, remove)
• Sí permiten extraer porciones, pero el resultado de la extracción es una tupla nueva.
• No permiten búsquedas (no index)
• Permiten comprobar si un elemento se encentra en la tupla.
Las tuplas se representan dentro de Python con el tipo de dato tuple.
¿Qué utilidad o ventaja presentan las tuplas
respecto a las listas?
• Más rápidas
• Manos espacio (mayor optimización)
• Formatean string.
• Pueden utilizarse como claves en un diccionario (las listas no).
'''

thistuple =("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("1. Tupla original :                                          ",thistuple)
print("2. Tupla desde -4 a -1 ( no incluido -1)                     ",thistuple[-4 :- 1])

'''
Cambiar valores de tupla
Una vez que se crea una tupla, no puede cambiar sus valores. Las tuplas son inmutables.
Pero hay una solución alternativa. Podemos convertir la tupla en una lista, cambiar la lista y volver a convertir la lista en una tupla.
'''
x = ("apple", "banana", "cherry")   # TUPLA 
print("3. Vemos la Tupla Original que queremos cambiar              ", x)
y = list(x)                         # TUPLA -> LISTA
y[1] = "kiwi"                       # EN LA LISTA MODIFICAMOS EL ELEMENTO EN POSICION 1
x = tuple(y)                        # LISTA -> TUPLA
print("4. Tupla modificada como lista y luego convertida a Tupla    ",x)                            # MOSTRAMOS LA TUPLA MODIFICADA

'''
Crear tupla con un artículo
Para crear una tupla con un solo elemento, debes AGREGAR UNA COMA DESPUES DEL ELEMETO, a menos que Python no reconozca la variable como una tupla.
Ejemplo: Tupla de un artículo, recuerda la coma
'''
thistuple = ("apple",)    # AQUI SE RESPETA COLOCAR UNA COMA DESPUES DEL ELEMENTO Y ESO HACE QUE SE CREE COMO TUPLA
print("5. Tipo de la variable thistuple que se creo correctamente    ",type(thistuple))
#NOT a tuple
thistuple = ("apple")
print("6. Tipo de la variable thistuple que NO se creo correctamente ",type(thistuple))

'''
Recorrer una tupla
Puedes recorrer los elementos de la tupla utilizando
un bucle for.
Ejemplo: Iterar a través de los elementos e imprimir
los valores.
'''
thistuple =("apple", "banana", "cherry")
for x in thistuple:
 print(x)
'''
El constructor tuple ()
También es posible usar el constructor tuple () para
hacer una tupla.
Ejemplo: Usando el método tuple () para hacer una
tupla.
'''
thistuple =tuple(("apple", "banana", "cherry")) #note the double round-brackets
print("7. Uso de constructor de tupla                               ",thistuple)

# Une dos tuplas Para unir dos o más tuplas, puedes usar el operador + :
#Ejemplo: Une dos tuple.
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print("8. Unir 2 tuplas                                             ",tuple3)

miTupla=("Angel", 4, 5.345, True, 4)
print("8. Imprime la tupla                                          ", miTupla)
tuplaUnitaria=("Sara",)                 #Tupla unitaria.Hay que poner al final ","
print("9. Imprime la tupla unitaria  ( elemento ,)                  ", miTupla, "Tupla unitaria: Al crearla hay que añadir , despues del elemento")
print("10. Imprime el elemnto con indice 2 ( igual que las listas)  ", miTupla[2])                       #Igual que en las listas
miLista=list(miTupla) #Con list convierto una tupla en una lista
print("11. Imprime miTupla convertida en lista)                     ", miLista)
miTupla2=tuple(miLista) #Con tuple convierto una lista en una tupla.
print("12. Imprime miLista convertida en tupla)                     ", miTupla2)
print("13. Verifica si Angel esta en la tupla                       ","Angel" in miTupla, " Devuelve True o False") #Está "Angel" en miTupla?, devuelve True o False
print("14. Cuenta cuantos 4 hay mi tupla, miTupla.count(4)           ",miTupla.count(4)) #Cuantas veces se encuentra el elemento 4 en miTupla?
print("15. Longitud de la tupla ( cantidad de elementos)             ", len(miTupla)) #Longitud de miTupla




print();print()