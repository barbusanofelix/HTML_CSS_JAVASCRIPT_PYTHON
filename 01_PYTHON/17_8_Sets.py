
#? CREACION DE UN SET
#* Notar que los set usan {}
#* Las listas []
#* Las Tuplas ()

thisset = {"apple", "banana", "cherry"}
print("El set es :", thisset)

#? AÑADIR UN NUEVO ELEMENTO ( .add )

print("Añadire Orange")
thisset.add("Orange")
print("El set es :", thisset, " Notar que los elementos tal vez no mantienen el orden")
print()

#? AÑADIR VARIOS ELEMENTOS AL SET ( .update )
print("Añadire Melon y Cambur")
thisset.update({"Melon","Cambur"})  #! notar que los 2 elementos se arropan con {}
print("El set es :", thisset, " Notar que los elementos tal vez no mantienen el orden")
print()

#? LOS SET NO REPITEN ELEMENTOS
print("Vuelvo a añadir Orange: Notar que solo aparece una vez")
thisset.add("Orange")
print("El set es :", thisset, " Notar que los elementos tal vez no mantienen el orden")
print()

#? UNION DE SETS ( NO REPITE ELEMENTOS)
mi_conjunto={"Angel", "Sara", "Pilar"}
mi_conjunto2={"Angel", "Manolo", "Juan"}
print()

print("UNION DE CONJUNTOS , SE USA | ")
print("mi_conjunto :", mi_conjunto)
print("mi_conjunto2 :", mi_conjunto2)
union= mi_conjunto | mi_conjunto2

print("Union de los conjuntos :", union, "Notar que Angel solo aparece una vez")  # salida {'Angel', 'Juan', 'Manolo', 'Pilar', 'Sara'}
print()

#? INTERSECCION DE CONJUNTOS ( & )
# Son los elementos repetidos.

interseccion= mi_conjunto  & mi_conjunto2   #* Interseccion, valores comunes a cada set
print("Interseccion  de los conjuntos :", interseccion, "Solo los valores comunes")  

#? ELIMINAR REPETIDOS DE CADENAS DE CARACTERES 

#Eliminamos duplicados pero desordenamos

letras = "aaabbbcccdddeeefff"
print("La cadena de letras es :", letras)
letras=set(letras)                                  #* Eliminamos duplicados
print("Ahora letras es un set", letras)

letras=list(letras)                                 #* Convertimos a lista para ordenar
letras.sort()                                       #* Ordenamos 
letras=''.join(letras)                              #* Unimos las letras en un unico string
print("Imrimimos letras nuevamente pero ordenada : ", letras)
print()
#Devolvemos una lista ordenada, pero sigue siendo lista.

#? TEST DE MEMBRESIA : Basicamente ve si una cadena esta dentro de otra...
#! Aplica para String aunque lo pusieron como un ejemplo en los sets
if "th" in "Python":
    print( "Si, th esta dentro de la cadena Python")
    
#? ELEMENTO PRESENTE EN EL SET
    print("Pilar esta en mi_conjunto2 ", "Pilar" in mi_conjunto2)
    print()
#? DIFERENCIA DE CONJUNTOS 

mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto2 = {"Angel", "Manolo", "Juan"}
print("mi_conjunto :", mi_conjunto)
print("mi_conjunto2 :", mi_conjunto2)

diferencia= mi_conjunto - mi_conjunto2
print("Veamos que elementos estan en mi-conjunto quitando el repetido en mi_conjunto2",diferencia) # salida 'Pilar', 'Sara'

#? COMPROBAR SI UN ELEMENTO ESTA EN UN CONJUNTO  
print("'Angel' esta en mi_conjunto? ", "Angel" in mi_conjunto)

#? COMPROBAR SI UN ELEMENTO ESTA EN LOS DOS CONJUNTOS
print("'Angel' esta en mi_conjunto y en mi_conjunto2? ", "Angel" in (mi_conjunto & mi_conjunto2))


#? COMPROBAR SI UN ELEMENTO ESTA ALGUNO DE LOS CONJUNTOSS
print("'Sara' esta en mi_conjunto ó en mi_conjunto2? ", "Angel" in (mi_conjunto | mi_conjunto2))

#? RECORRER EL SET E IMPRIMIR LOS VALORES DEL INDICE Y EL ELEMENTO.
for indice, elemento in enumerate(mi_conjunto2):
    print(f"{indice}: {elemento}")
print()

#? AGREGAR ELEMENTOS AL CONJUNTO ( .add)
print("Añadimos a Pepe a mi conjunto ")
mi_conjunto.add("Pepe")
print("Añadid0 Pepe a mi conjunto ", mi_conjunto)
print()
#? CANTIDAD DE ELEMENTOS EN UN CONJUNTO
print("En mi_conjunto hay ", len(mi_conjunto)," elementos")

#? ELIMINAR UN ELEMENTO : REMOVE o DISCARD Ó POP
 #! discard NO genera error sino existe pero REMOVE SI GENERA ERROR.
 #! POP elimina el ultimo elemento PERO OJO, LOS SETS NO ESTAN ORDENADOS ASI QUE NO SABREMOS QUE SE VA A ELIMINAR.
 #*   AL MENOS POP DEVUELVE EL ELEMENTO ELIMINADO ASI QUE SE PODRIA CHEQUEAR O GUARDAR EN UNA VARIABLE.
mi_conjunto.discard("Pepe")                            
print("Elimine a  Pepe a mi conjunto ", mi_conjunto)
print()
#? UNIR DOS CONJUNTOS 
mi_conjunto3=mi_conjunto.union(mi_conjunto2)
print("Union de mi_conjunto y mi_conjunto2", mi_conjunto3 )
print()

#? INSERTAR LOS ELEMENTOS DE UN CONJUNTO EN OTRO ( UNO )
mi_conjunto.update(mi_conjunto2)
print("Ahora mi_conjunto queda ", mi_conjunto )
print()
