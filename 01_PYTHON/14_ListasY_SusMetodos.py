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
#
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
print("26. Concatenando miLista5=[miLista4, miLista2]:          ",miLista5 )
del miLista5                                                # BORRAMOS miLista5
miLista5=list()       # Al tratar de iprimir miLista5 dio error por haberla borrado asi que la cree
print("27. Con 'del miLista5' borra miLIsta5 y la volvi a crear ",miLista5)
miLista5.extend(miLista4)           # Añadimos los elementos de miLista4 a miLista5  
miLista5.extend(miLista2)           # Añadimos los elementos de miLista2 a miLista5
print("28. Extendi miLista5 vacia con miLista2 y MiLista4       ",miLista5)
del miLista5[6]   # Borra el elemento en el indice 6 de miLista5 , es es 'nombre'
print("29. Borre indice 6, 'del miLista5[6], 'nombre'           ",miLista5)  
miLista5.clear()                    # Limpiamos la lista completa
print("30. Vaciamos completamente miLista5.clear()              ",miLista5)
miLista6 =['Texto1', 'Texto2']
miLista6 +=['Texto3', 'Texto4','Texto5', 'Texto6']
print("31. A miLista6 le aplicamos adicion elementos con +=     ", miLista6)
print("32. Imprime elementos [0:3]; real es 0,1,2 de miLista6   ", miLista6[0:3])
miLista6[0:3]=[1,2,3]     # Sustituira las posiciones 0,1,2 que tienen 'Texto1', 'Texto2', 'Texto3' por 1, 2, 3 y quedaria 'Texto4', 'Texto5', 'Texto6'
print("33. Cambiamos 3  posiciones, miLista6[0:3]=[1,2,3]       ",miLista6)
miLista6[0:3]=[1,2]
print("34. Cambiamos 3 x 2  posiciones, miLista6[0:3]=[1,2]     ",miLista6)  # La posicion de indice 2, queda vacia ..Imprime 1,2,'Texto4', 'Texto5', 'Texto6'
# Si repetimos la instruccion eliminara el 'Texto4', cambie el 1,2 por 3,4 para que se vea. Como 0:3 son 3 posiciones se comera una de la lista.
miLista6[0:3]=[3,4]  # Le estamos diciendo que 1,2,'Texto4', 'Texto5', 'Texto6' quedara 3,4, 'Texto5', 'Texto6'
print("35. Cambiamos 3 x 2  posiciones, miLista6[0:3]=[3,4]     ",miLista6) # Imprime [3, 4, 'Texto5', 'Texto6']
miLista6[2:2]=[5,6,7]
print("36. [2:2] inserta 3 elem. en [2], miLista6[2:2]=[5,6,7]  ",miLista6) # Equivale a insertar 3 elementos en la posicion 2
miLista6[0:6]=[]   # Vacia los elementos de 0 a 5.
print("37. miLista6[0:6]=[] , vacia los elementos de 0 a 5      ",miLista6)

# ANIDACION DE LISTAS
#   Anidacion= Listas dentro de listas
thislist = [["a1", "a2", "a3"],
            ["b1", "b2", "b3"],
            ["c1", "c2", "c3"]]  # thislist = Formada por 3 listas.
print("38. Lista Anidada, thislist                              ",thislist)

# Indexamos la 2da fila
print("38. Indexamos 2da fila... thislist[1]                    ",thislist[1])
# Indexamos desde la 2da a ultima.
print("39. Indexamos >=2da fila... thislist[1:]                 ",thislist[1:])
# 1era fila - ultimo elemento
print("40. Elemento 1era fila -ultima columna:thislist[0][-1]   ",thislist[0][-1])      # Por definicion el -1 es el ultimo elemento en una lista
print("41. Elemento 1era fila -ultima columna:thislist[0][2]    ",thislist[0][2])       # Igual que el anterio al tener 3 columnas: 0,1,2

# Imprime recomendacion de paquete para manejar matrices usado, por ejemplo, manejo de datos
print("42. Usar libreria Numpy para manejo de matrices grandes y problemas complejos")
listaAnidada = [1, [2, [3, 4], 5], 6]    # Vemos que tenemos 3 listas...La mas interna es 3,4, luego tenemos la 2, [3,4],5 y luego todo la lista
print("43. Lista anidas listaAnidada = [1, [2, [3, 4], 5], 6]   ", listaAnidada)
print("44. 1er elemento , listaAnidada[0]                       ", listaAnidada[0])
print("45. Ultimo elemento , listaAnidada[-1]                   ", listaAnidada[-1])
# El 4 esta en la 3era, entonces necesitamos 3 indices para llegarle. Del 3 y 4 esta en la posicion 1, que iria de ultimo.
# Luego el [3,4] esta dentro de la lista [2,[3,4],5] ...el 2 es la 0, y la [3,4] es la 1
# Luego de la lista completa [1, [2, [3, 4], 5], 6], el 1 es la posicion 0 y en la posicion 1 tenemos [2, [3, 4], 5]
print("46. Elemento 4  , listaAnidada[1][1][1]                  ", listaAnidada[1][1][1])  
# Vamos a obtener el 5: Para entrar en la lista que lo contiene [2, [3, 4], 5] es 1 y dentro del 1 seria el -1 que seria el ultimo de esa lista 
# o podemos usar el indice 2 . En resumen deberia ser lo mismo con [1,-1]  ó [1,2]
print("47. Elemento 5  , listaAnidada[1][-1]                    ", listaAnidada[1][-1])  
print("48. Elemento 5  , listaAnidada[1][2] ( igual que 47)     ", listaAnidada[1][2])  
# Obtener [3,4]....al ser la 3era lista :
# 1 para entrar en [2, [3, 4], 5]
# 1 para entrar en [3,4]
# [:] para que liste la lista [3,4]
print("49. Lista [3,4] dentro [1, [2, [3, 4], 5], 6]            ", listaAnidada[1][1][:])
# Otra forma de obtener [3,4]
# 1 por estar en la lista 2 ( n-1 ) [2, [3, 4], 5]
# 1 nuevamente porque [3,4] esta en la posicion 1 dentro de [2, [3, 4], 5]

print("50. Lista [3,4] dentro [1, [2, [3, 4], 5], 6]            ", listaAnidada[1][1])
# 1 para entrar [2, [3, 4], 5]
# [:] para listar la lista completa

print("51. Lista [2, [3, 4], 5] dentro [1, [2, [3, 4], 5], 6]   ", listaAnidada[1][:])
# 1 porque el 2 esta en la lista 2 ( n-1 ), [2, [3, 4], 5] 
# 0 porque el 2 esta en la posicion 1 ( n-1 )
print("52. Elemento 2  , listaAnidada[1][0]                     ", listaAnidada[1][0])  
# OPERADORES APLICAN A LA PRIMERA LISTA 
print("53. Esta [3,4] en [1, [2, [3, 4], 5], 6] = False         ",[3,4] in listaAnidada, " [3,4] esta en mas de un nivel interno" )
print("54. Esta [3,4] en [2, [3, 4], 5] = True                  ",[3,4] in listaAnidada[1], "  [3,4] esta a un nivel asi que la ve. Operador aplica sobre 1era lista" )

# INDEXING
lista = ["text1", "text2", "text3", "text4", "text5"]

print("55 iNDEXING, Tenemos la lista                            ",lista)
print("56 El elemento [0] es lista[0]                           ",lista[0])
print("57 El ultimo elemento [-1] es lista[-1]                  ",lista[-1])

# SLICING
print("58 Slicing de lista, lista[2:4]                          ",lista[2:4])  # ['text3', 'text4']
print("59 Slicing de lista, lista[:3]                           ",lista[:3])    #['text1', 'text2', 'text3']
print("60 Slicing de lista, lista[2:]                           ",lista[2:])    # ['text3', 'text4', 'text5']

# STRIDE ( DE UN INICIO A FINAL SALTANDO N ELEMENTOS )
print("61 STRIDE  de lista, lista[0:4:2]                        ",lista[0:4:2])  #['text1', 'text3']. Inicia en 0, termian 3 saltando de 2 en 2
print("62 STRIDE, DAR VUELTA A UNA LISTA, lista[::-1]           ",lista[::-1]) 
print("63 COPIA DEL OBJETO, lista[:]                            ",lista[:])

# LISTAS POR COMPRENSION

miLista=[1,2,3,4,5,6,7]
print("64 Listas por Comprension, miLista                       ", miLista)

## milista2 tiene los valores (2*elemento) siendo elemento los valores de la lista milista
miLista2 = [2*elemento for elemento in miLista]
print("65 miLista2 = [2*elemento for elemento in miLista]       ",miLista2)  # cada elemento x 2

##Crear una Lista solo con Los elementos pares
listaPares = [elemento for elemento in miLista if elemento%2 == 0]
print("66 Pares=[elemento for elemento in miLista if elemento%2 == 0]",listaPares) # Forma tradicional seria con un for

##A La manera tradicional seria:
listaPares=[]
for i in miLista:
    if i%2 == 0:
        listaPares.append(i)
print(listaPares)

##Anidar iteraciones dentro de la liata
a=["a", "b", "c"]
b=[1,2,3]
##Para cada elemento de a me recorre todos Los elmentos de b
c=[el1*el2 for el1 in a for el2 in b]
print("67 Tenemos lista a:                                              ",a)
print("68 Tenemos lista b:                                              ",b)
print("69 c=[el1*el2 for el1 in a for el2 in b]                         ",c)                                             
##Puedo incluso poner alguna condicion
c=[el1*el2 for el1 in a for el2 in b if el2 != 2]
print("70 Condicion, c=[el1*el2 for el1 in a for el2 in b if el2 != 2] ",c)
matriz=[['a1', 'a2', 'a3'], ['b1', 'b2', 'b3' ], ['c1', 'c2' , 'c3' ]]
print("71 Teniendo la matriz                                            ", matriz)
columna2 = [col[1] for col in matriz]   # generamos una lista de los elementos de la columna 1 ( la 2da ) de la matriz, es decir, a2, b2 y c2
print("72 La columna 2 esta formada por    [col[1] for col in matriz]    ", columna2)

import copy                     # importamos modulo copy
la = [1, 2, [31, 32, 33]]       # Lista anidada
lb = copy.copy(la)              # Copia 'plana' (igual que lb = la[:])
lc = copy.deepcopy(la)          # Copia profunda. Por si hay elementos anidados
la[1] = 'z'
la[2][2] = 'zz'

print(la)  #[1, 'z', [31, 32, 'zz']]


print(lb)  #[1, 2, [31, 32, 'zz']]      # Copia plana solo copia elementos de 1er nivel


print(lc)  # [1, 2, [31, 32, 33]]       # Copia profunda copia a todos los niveles













