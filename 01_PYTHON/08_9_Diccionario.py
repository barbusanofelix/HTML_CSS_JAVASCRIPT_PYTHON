# DICCIONARIOS
"""Los diccionarios, también llamados matrices asociativas, deben su nombre a que son colecciones que 
relacionan una clave y un valor.
Un diccionario es una colección desordenada, modificable e indexada. En Python, los diccionarios se 
escriben entre llaves y tienen claves y valores.
"""
print()
# Declaración de un diccionario
miDiccionario = {"brand": "Ford","model": "Mustang","year": 1964}
# --------------------Pagina 9 , inicio 10 ------------------------------------------------
print("1 ",miDiccionario)
print()
# A los valores almacenados en un diccionario se accede por su clave 
peliculas = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet"}
peliculas["Love Actually"]
# Reasignar valores a un diccionario
peliculas["Kill Bill"] = "Quentin Tarantino"
print("2 ", peliculas)
print()
# Usar una tupla dentro de un diccionario:
miDiccionario3={"nombre":"Jordan","Equipo":"Bulls", "Anillos":[1991, 1992,1993, 1996, 1997, 1998]}
print("3 ", miDiccionario3["Anillos"])
print()
# Quitar valores de un diccionario
peliculas = {"Love Actually": "Richard Curtis","Kill Bill": "Tarantino","Amélie": "Jean-Pierre Jeunet"}
peliculas.pop("Love Actually")
print("4 ", peliculas)
print()
# Crear un diccionario a partir de dos listas:
lista_claves=["nombre", "edad"]
lista_valores=["Angel", 43]
diccionario = dict(zip(lista_claves ,lista_valores))
print("5. ",diccionario)
print()
# ---------------------------10A ----------------------------------------
# Para comprobar si una clave está en el diccionario:
"nombre" in diccionario #Devuelve true o false
# Imprima las claves del diccionario:
peliculas = {"Love Actually": "RichardCurtis","Kill Bill": "Tarantino","Amélie": "Jean-Pierre Jeunet"}
print("6.")
for x in peliculas:
    print(peliculas[x])
print()
# Longitud de un diccionario:
peliculas = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet"}
print("7. :",len(peliculas))
print()
# Agregar elementos a un diccionario:
miDiccionario = { "brand": "Ford", "model": "Mustang", "year": 1964}
miDiccionario["color"] = "red"
print("8. ",miDiccionario)
print()
# Eliminar el último elemento insertado:
miDiccionario = { "brand": "Ford", "model": "Mustang", "year": 1964}
miDiccionario.popitem()
# --------------------------portiem 10B --------------------------------------------
print("9.",miDiccionario)
print()
# La palabra clave del elimina el elemento con el nombre de clave especificado:
miDiccionario = {"brand": "Ford","model": "Mustang","year": 1964}
del miDiccionario["model"]
print("10.", miDiccionario)
print()
# La palabra clave del también puede eliminar completamente el diccionario:
miDiccionario = { "brand": "Ford","model": "Mustang","year": 1964}
print(type(miDiccionario))
print()
del miDiccionario

print("11.Para borrar el diccionario usar: del miDiccionario")
print()
# La palabra clave clear() vacía el diccionario:
miDiccionario = {"brand": "Ford","model": "Mustang","year": 1964}
miDiccionario.clear()
print("12.con miDiccionario.clear() lo limpiamos:",miDiccionario)
print()
# Copiar un diccionario
miDiccionario = {"brand": "Ford","model": "Mustang","year": 1964}
print("13. Creamos un nuevo miDiccionario: ", miDiccionario)
print()
midict = miDiccionario.copy()
print("14. Creamos una copia miDiccionario.copy() ", midict)
print()
# Otra forma de copiar un diccionario
miDiccionario = {"brand": "Ford","model": "Mustang","year": 1964}
midict = dict(miDiccionario)
print("15. Otra forma de copiar dict(miDiccionario :",midict)
print()
# Diccionarios anidados
print("16. Titutlo diccionario anidados")
child1 = {"name" : "Emil","year" : 2004}
child2 = {"name" : "Tobias","year" : 2007}
child3 = {"name" : "Linus","year" : 2011}
myfamily = {"child1" : child1,"child2" : child2,"child3" : child3}
print("17. Diccionarios hijos",myfamily["child1"])
