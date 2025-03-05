'''
DIFERENTES METODOS Y PROPIEDADES DE LAS LISTAS 
'''

miLista=["Angel", "Maria", "Manolo","Antonio", "Pepe"]
miLista2=["nombre", 2, 5.56, True] #Se pueden mezclar diferentes elementos.

print("1. Imprime elemento en indice 1 :"                 ,miLista[1])   #Para un elemento en concreto, se empieza a contar desde La posición cero.
print("2. Imprime elemento entre indice >=0 y <2 ( No incluye el indice 2)",miLista[0:2]) #Empezando desde cero incluido hasta el dos sin incluir, esto es, "Angel y Maria".

miLista3=miLista.copy()   # crea una copia de miLista
print("3. miLista3, copia de miLista                    : ",miLista3)

# Ordena con sort(). Sort sobreescribe la lista a la cual se aplica. NO FUNCIONA SI MEZCLAMOS NUMEROS Y STRINGS
miLista3.sort() 
print("4. miLista3 ahora ordenada (sort la sobre-escribe )", miLista3)

#REVERSE ( coloca la lista alreves) - tamnien la sobreescribe. NO FUNCIONA SI MEZCLAMOS NUMEROS Y STRINGS
miLista3.reverse()
print("4. miLista3  con reverse (reverse sobre-escribe   )"  , miLista3)

l = [99, True, "una lista", [1, 2]]

mi_var = l[0:2]         # mi_var vale [99, True]. El indice tomado es 0 y 1 ( <2)
print('6. l = [99, True, "una lista", [1, 2]] -   mi_var = l[0:2]  ',mi_var)

mi_var = l[0:4:2]       # mi_var vale [99, "una lista"]. Del 0 al 3 ( <4) , saltando 2
print('7. l = [99, True, "una lista", [1, 2]] -   mi_var = l[0:4:2]  ',mi_var)

mi_var = l[1:4:2]       # mi_var vale [99, "una lista"]. Del 0 al 3 ( <4) , saltando 2
print('8. l = [99, True, "una lista", [1, 2]] -   mi_var = l[1:4:2]  ',mi_var)

print("9. miLista[:2] es igual a caso 2. miLista[0:2]           ",miLista[:2])      #Como en el ejemplo anterior, pero en el caso de que sea cero,
#si no pongo se sobreentiende.
 
print("10. miLista[1:3], incluye el 1 hasta 2 (<3):             ",miLista[1:3])  #Desde el elemento [1] incluido, hasta el tres sin incluir,
#es decir "María y Manolo".

print("11. miLista[2:] , imprime >=2 hasta el ultimo:           ", miLista[2:])  #Desde el elemento [2] hasta el final, es decir "Manolo, Antonio, Pepe".

print("12. miLista[-2], [-1] es ultima posicion [-2] penultima  ",miLista[-2])  #Desde el final, la segunda posición, es decir "Antonio".

print("13. miLista[:] repressenta la lista completa             ", miLista[:])  #Lista completa.

miLista.append("Federico")           #Añade el elemento al final de la lista.
print("14. Anadio a Federico al final de la lista               ", miLista)

miLista.insert(2,"Sandra")          #Añade el elemento en la posición [2].
print("15. Inserto a Sandra en la posicion 2  miLista           ", miLista)

miLista.extend(["Sara", "Diego"])   #Concatena la nueva lista a la anterior.
print("16. Concatena a Sara y Diego con miLista                 ", miLista)

print("17. Indice de  Antonio ( solo la 1era ocurrencia) :      ",miLista.index("Antonio"))     #Me dice en qué posición está "Antonio", en este caso 3,#si hay más elementos "Antonio", nos da el primero.

print('18. Indica si pepe esta en miLista                       ',"pepe" in miLista)             #Está este elemento en la lista ?. Imprime true o false.

miLista.remove("Angel")     #Elimina un elemento de la lista.REMOVE DESCARTA TOTALMENTE EL ELEMENTO MIENTRAS QUE POP PERMITE GUARDARLO
print("19. Elimino a Angel de mi Lista, con remove (se pierde):",miLista)
elimineA=miLista.pop()                        #Elimina el último elemento de una lista.PERO SE PUEDE RECUPERAR SI LO ASIGNAMOS 
print("20. Elimine el ultimo elemento de la lista con pop()     ", miLista)
print("21. El elemento eliminado con pop() fue                  ", elimineA)

miLista3=miLista+miLista2 #Crea una lista nueva que es el resultado de concatenar las dos anteriores.
miLista4=[4, 6, 7]*2  #Me crearía una lista como esta [4, 6, 7, 4, 6, 7]

print("22. Imprimimos miLista tal cual esta ahora               ",miLista[:])
print("23. Imprimimos miLista2 tal cual esta ahora              ",miLista2[:])
print("24. Suma de miLista + miLista2                           ", miLista3[:])
print("25. miLista4=[4,6,7]*2                                   ",miLista4[:])
miLista5=[miLista4, miLista2]
print("26. Creamos una lista concatenando miLista5=[miLista4, miLista2]: ",miLista5 )