# Crear un diccionario

#Partiendo de un dicconario vacío y añadiendo
#campos uono a uno

miDiccionario = {}
miDiccionario["nombre"] = "Ana"
miDiccionario["edad"] = 9
miDiccionario["grupo"] = "4 primaria"
print("El diccionario es :", miDiccionario)  #{'nombre': 'Ana', 'edad': 9, 'grupo': '4 primaria'}

{'nombre': 'Ana', 'edad': 9, 'grupo': '4 primaria'}

#Utilizando la función dict()
#Las claves son parámetros de la función dict()
miDiccionario = dict(nombre="Ana", edad=9,grupo="4 primaria",nota="Sobresaliente")

print("MiDiccionario es :",miDiccionario)  # {'nombre': 'Ana', 'edad': 9, 'grupo': '4 primaria', 'nota': 'Sobresaliente'}

#Uniendo listas de claves-valores con la función zip()

claves = ["nombre", "edad", "grupo", "nota"]
valores = ["Ana", 9, "4 primaria", "Sobresaliente"]
miDiccionario = dict(zip(claves, valores))

print("El diccionario es ",miDiccionario) # {'nombre': 'Ana', 'edad': 9, 'grupo': '4 primaria', 'nota': 'Sobresaliente'}


#Uniendo Listas de claves-valores con la función zip()

claves = ["nombre", "edad", "grupo", "nota"]
valores = ["Ana", 9, "4 primaria", "Sobresaliente"]
zip(claves, valores)

list(zip(claves, valores))

[('nombre', 'Ana'),
('edad', 9),
('grupo', '4 primaria'),
('nota', 'Sobresaliente' )]

#convertimos el zip en una lista



