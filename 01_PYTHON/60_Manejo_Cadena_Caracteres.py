


# DIVIDIR CADENA USANDO SPLIT 


cadena= "Hola Mundo la casa es bonita"

palabra_cadena= cadena.split()   # Divide la cadena usando el caracter dentro del split. Espacio por defecto

print(palabra_cadena)

palabra_cadena=cadena.split("o")  # Divide en la o de la cadena 

print(palabra_cadena)


# BUSCAR Y REEMPLAZAR CON FIND() Y REPLACE.


cadena="Esto es un ejemplo para reemplazar elementos dentro de una cadena y asi es como podemos buscar y reemplazar"

# BUSQUEDA FIND()  ... SI NO ESTA DEVUELVE -1. SINO DEVUELVE LA POSICION DE LA PRIMERA OCURRENCIA

posicion=cadena.find("es")

print(posicion)

texto = "Este es un ejemplo de cadena."

# Buscar la primera ocurrencia de "es" en toda la cadena
indice1 = texto.find("es")
print(f"Índice de 'es': {indice1}")  # Salida: Índice de 'es': 2

# Buscar "es" comenzando desde el índice 5
indice2 = texto.find("es", 5)
print(f"Índice de 'es' desde el índice 5: {indice2}")  # Salida: Índice de 'es' desde el índice 5: 8

# Buscar "es" dentro del rango de índices 0 a 7 (sin incluir el 7)
indice3 = texto.find("es", 0, 7)
print(f"Índice de 'es' en el rango 0-7: {indice3}")  # Salida: Índice de 'es' en el rango 0-7: 2

# Buscar una subcadena que no existe
indice4 = texto.find("inexistente")
print(f"Índice de 'inexistente': {indice4}")  # Salida: Índice de 'inexistente': -1

indice5=texto.find("ejemplo", 10,27 )

print(f"Indice5 : {indice5}")


cadena1 = "Hola"
longitud1 = len(cadena1)
print(f"La longitud de '{cadena1}' es: {longitud1}")  # Salida: La longitud de 'Hola' es: 4

cadena2 = "Este es un ejemplo."
longitud2 = len(cadena2)
print(f"La longitud de '{cadena2}' es: {longitud2}")  # Salida: La longitud de 'Este es un ejemplo.' es: 18

cadena_vacia = ""
longitud_vacia = len(cadena_vacia)
print(f"La longitud de la cadena vacía es: {longitud_vacia}")  # Salida: La longitud de la cadena vacía es: 0

cadena_con_espacios = "  Espacios  "
longitud_con_espacios = len(cadena_con_espacios)
print(f"La longitud de '{cadena_con_espacios}' es: {longitud_con_espacios}")  # Salida: La longitud de '  Espacios  ' es: 11


saludo="Hola Mundo"

# Si queremos la posicion de Mundo en la cadena saludo

posicion= saludo.find("Mundo")
print(f'La posicon de Mundo en "{saludo}" es {posicion}')

nuevo_saludo=saludo.replace("Mundo","Amigo")
print(f'Ahora la cadena "{saludo}" cambio a "{nuevo_saludo}"')

# MULTIPLICACION DE CADENAS

divisor_linea="-"

print(divisor_linea*100)

# USO DE STRIP PARA LIMPIAR CADENA AL PRINCIPIO Y AL FINAL ( ELIMINA TAMBIEN LOS SALTOS DE LINEA U OTRAS ESCAPE , PERO SOLO AL PRINCIPIO Y FINAL.)

cadena = "\n    Hola mundo  \n Hola mundo      "
print(f'Esta es la cadena original: {cadena} con longitud : {len(cadena)}')

nueva_cadena=cadena.replace("\n","")
print(f"Cadena eliminando los saltos de linea : {nueva_cadena} con longitud {len(nueva_cadena)}")

cadena_limpia=nueva_cadena.strip()

print(f"Cadena totalmente limpia, sin saltos y espacios:{cadena_limpia} con longitud  {len(cadena_limpia)}")

#QUITAR CARACTERES COMO . AL FINAL O PRINCIPIO DE CADENA CON STRIP()

cadena=" ....Hola Mundo ...."
print("Asi es la cadena ", cadena)
nueva_cadena=cadena.strip(".")

print('Asi quedo la cadena luego se usar el metodo strip(".")', nueva_cadena, "Interesante: antes de los 4 puntos del inicio habia un espacio y obvio los puntos")
