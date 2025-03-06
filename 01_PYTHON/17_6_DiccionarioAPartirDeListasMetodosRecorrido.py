
#? CONSTRUIR UN DICCIONARIO PARTIENDO DE LOS LISTAS.
#? Una de claves y otras de Valores 
#? Las empaquetamos con zip y luego se crea el dict
print()
#?-------------------------------------------------------------------------------
#? FUNCIONES 
#?-------------------------------------------------------------------------------
def imprimirDic(diccionario):
    # Hay que usar el METODO ITEMS()
    for clave,valor in diccionario.items():   # Muestra la pareja clave y su valor
        print(clave, valor)
    print() 
#?--------------------------------------------------------------------------------

lista_claves=["nombre", "edad"]                             # Lista de claves
lista_valores=["Angel", 43]                                 # Lista de Valores
diccionario=dict(zip(lista_claves, lista_valores))          # Emapquetamos con zip y  luego las convertimos a diccionarios.

Lista = list(zip(lista_claves,lista_valores))

print(diccionario, " Diccionario, clave / Valor")
print()
print(Lista, " Asi crea una tupla")

#? Imprimir las claves del dicconario
for clave in diccionario:     # clave puede ser cualquier nombre de variable para recorrido
    print("Clave: ", clave)
print() # este printe esta fuera del for

#? IMPRIMIR EL VALOR EN EL DICCIONARIO

for valor in diccionario:
    print(diccionario[valor])   # OJO: EL NOMBRE DEL DICCIONARIO Y CORCHETES [VALOR]
print() # este printe esta fuera del for

#? O USAR LA FUNCION VALUES PARA DEVOLVER LOS VALORES DEL DICCIONARIO    
for valor in diccionario.values():  # values es metodo y entonces lleva ()
    print(valor)
print()    

#?   RECORRER EL PAR CLAVE-VALOR

imprimirDic(diccionario)

#? PREGUNTAR SI EN EL DICCIONARIO HAY UNA CLAVE ESPECIFICA.

if "nombre" in diccionario:
    print("Si, nombre esta en el diccionario")
else:
    print("Nombre no es clave del diccionario")    

# Igual que lo anterior pero parametrizado.
clave="edad"

if clave in diccionario:
    print(f"Si, {clave} es una clave del diccionario")
else:
    print(f"No, {clave} no es un clave de este diccionario")
    print("Las claves de este diccionario son:", end="")
    for clave in diccionario:
        print(clave, end="-" )    

#? NUMERO DE ELEMENTOS EN EL DICCIONARIO.
print("La cantidad de pares clave-valor en el diccionario es : ", len(diccionario))       
print()
#? AÑADIR UNA CLAVE VALOR NUEVA AL DICCIONADIO.
# Simplemente la asignamos con un corchete.

diccionario["Ciudad"]="Madrid"

print(diccionario)
print()
imprimirDic(diccionario)

#? ELIMINAR ELEMENTOS DE  UN DICCIONARIO:
# Existen varios metodos para eliminar elementos
# pop("Clave") ...elimina el elemento con la clave indicada

diccionario.pop("Ciudad")    # elimina la pareja clave y su valor de Ciudad. Colocar ciudad da error.
print('Eliminamos la pareja clave-valor, con la clave="ciudad"')
for clave,valor in diccionario.items():   # Muestra la pareja clave y su valor
    print(clave, valor)
print()    

# popitems() elimina el ultimo elemento insertado.
diccionario.popitem()
imprimirDic(diccionario)
print("Se elimino la edad....con popitem()")    
print()

#? añadimos un elemento para luego eliminarlo 
diccionario["Nacimiento"]=1959
for clave,valor in diccionario.items():   # Muestra la pareja clave y su valor
    print(clave, valor)
print("Se añadio una clave-valor Nacimiento - 1959")    
print()

#? BORRADO DE CLAVE VALOR USANDO DEL.
del diccionario["Nacimiento"]  #! BORRA LA CLAVE-VALOR Nacimiento
print("Borre la clave Nacimiento")
imprimirDic(diccionario)

#! del diccionario   BORRA TODO EL DICCIONARIO.
#? AGREGAMOS CLAVES-VALOR PARA RESTITUIR EL DICCIONARIO
diccionario["Ciudad"]="Barcelona"
diccionario["Nacimiento"]=1960
diccionario["Estudios"]="Universitarios"
imprimirDic(diccionario)

#? CREAMOS UNA COPIA DEL DICCIONARIO
#             ! Para crear una copia no se debe hacer dic=diccionario porque apunta a la misma direccion de memoria.
dic=diccionario.copy()
print("Cree una copia del diccionario en dic")
imprimirDic(dic)
print()

#? OTRA FORMA DE HACER UNA COPIA DEL DICCIONARIO ES USANDO  dict
dic2=dict(diccionario)
print("Cree otra copia del diccionario usando dic2=dict(diccionario)")
imprimirDic(dic2)
print()


#? LIMPIAR/VACIAR COMPLETAMENTE EL DICCIONARIO
print("Para limpiar un Diccionario : ", end=" ")
print("USAR nombreDiccionario.Clear()")
diccionario.clear()
print("Vaciamos el diccionario")
print(diccionario)

#? DICCIONARIO ANIDADOS
# Una forma es en la clave tendremos un nombre y en Valor un diccionario.
# Asi child1 es la clave y su valor el diccionario {"name": "Emil","year": 2004 },
print("Diccionario myfamily")
print()
myfamily = {"child1" : {"name": "Emil","year": 2004 },
            "Child2" : {"name": "Tobias","year":2007},
            "child3" : {"name" : "Linus","year":2011}}

imprimirDic(myfamily)

#? OTRA FORMA ES CREAR EL DICCIONARIO REFIRIENDONOS A CADA SUBDICCIONARIO.


child1 = {"name":"Emil", "year" : 2004}

child2 = {"name" : "Tobias","year" : 2007}

child3 = {"name": "Linus", "year" : 2011}

myfamily2 = {
    "child1" : child1,    # cada child hace referencia al diccionario que le corresponde
    "child2" : child2,
    "child3" : child3
    }

#? MOSTRAR EL AÑO DE NACIMIENTO DE Linus 
# Buscar el año de "Linus" recorriendo todos los hijos
for child in myfamily2.values():
    if child["name"] == "Linus":
        print(f'Año Nacimiento de {child["name"]} :', child["year"])  # Output: 2011
        break  # Salir del bucle una vez encontrado

#? USANDO METODO POR COMPRENSION DE LISTA 
# Filtrar el año usando una comprensión de lista
# myfamily2.values() devuelve una lista con los diccionarios de cada hijo (child1, child2, child3).
# child["name"] == "Linus" filtra el diccionario que contiene el nombre "Linus".
#child["year"] obtiene el valor del año asociado a ese nombre.

year = [child["year"] for child in myfamily2.values() if child["name"] == "Linus"][0]
print(year)  # Output: 2011





