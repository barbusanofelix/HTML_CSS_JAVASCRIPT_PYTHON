"""
EXPRESIONES REGULARES O REGEX.

Se usan como patrones de búsqueda o validaciones.

Es como varios IF anidados para evaluar si hay cierto patron en una cadena de texto.
Se puede saber si el patron esta en una cadena, la cantidad de veces que aparece y saber donde empieza y donde termina.

Para saber si esta se usa                       : search()
Cuantas veces esta presemte                     : findall
Donde se ubica el inicio                        : start()
Donde esta el final del elemento, en la cadena  : end()

"""

"""   NECESITAMOS IMPORTAR EL MODULO import re   r= regular e= expression"""

import re        # Importamos el modulo

cadena="Hola Mundo"

patron="Mundo"

encontrado=re.search(patron,cadena)

if encontrado:
    print(f'Se encontro {patron} en {cadena}')
else:
    print(f'No se encontro {patron} en {cadena}')

# group() muestra el patron encontrado
print("El patron encontrado fue ",encontrado.group())

# posicion del patron en la cadena
print(f"La posicion de {patron} en {cadena} es :", encontrado.start())

""" USANDO PATRON MAS GENERAL"""
cadena="Hola Mundo"

patron=r"[a-z]n"    # Letras desde a hasta z , seguidas de una n. La r viene de raw y es una cadena cruda... la tomará
                    # textualmente igual a lo escrito y  por ejemplo no tomará \ como parte de una cadena de escape

encontrado=re.search(patron,cadena)

if encontrado:
    print(f'Se encontró {patron} en {cadena}')
else:
    print(f'No se encontró {patron} en {cadena}')

# group() muestra el patron encontrado
print("El patron encontrado fue ",encontrado.group())

# posición del patron en la cadena
print(f"La posición de {patron} en {cadena} es :", encontrado.start())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e índica en que posición empieza y termina la coincidencia.

cadena2 = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver que pasa"
patron = "IA"
found_ia = re.search(patron, cadena)

if found_ia:
    print(f"He encontrado el patrón en el texto en la posición {found_ia.start()} y termina en {found_ia.end()}")
else:
    print("No he encontrado el patrón en el texto")

#

### Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias

cadena3 = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
patron3 = r"[aeiou]"    # Buscará todas las vocales indicadas por separado

veces_encontrado=re.findall(patron3,cadena3)                        # Hace una lista con todas las coincidencias de vocales
print(f"Lista de veces encontrado {veces_encontrado},  apareció , {len(veces_encontrado)}")  #Muestra la lista y cantidad de elementos en ella

"""     CREACION DE UN ITERADOR 
        ESTA ES LA BÚSQUEDA MAS COMPLETA PUES INDICA CUANTAS VECES ESTA EL PATRON Y LAS POSICIONES DE CADA UNO

"""
cadena4 = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
patron4 = "Python"
print("CREACIÓN DE UN ITERADOR PARA ENCONTRAR Python")
print(f'Mostrará el inicio y fin de "{patron4}" en la cadena "{cadena4}"')
print(("El inicio es en base a la longitud de la cadena empezando con indice 0 y cada fin de ocurrencia es +1"))

cantidad_encontrado= re.findall(patron4, cadena4)
ocurrencias = re.finditer(patron4, cadena4)  # finditer creara un iterador con las ocurrencias, entonces en ocurrencias se guarda un iterador
print(f'La cantidad de veces de "{patron4}" en "{cadena4}" es : {len(cantidad_encontrado)} veces')
for vez in ocurrencias:
    print(vez.group(),vez.start(), vez.end())

"""  EXPRESIONES REGULARES PARA BÚSQUEDA DE FAMILIA DE PALABRAS  """

"""  NAVIDAD NAVIDEÑO  NAVIDEÑA """

cadena5 = "Me gusta la navidad porque se crea un gran ambiente navideño"
patron5 = r"navid\w*"  # Modificamos el patrón para capturar palabras completas, \w* agrega cualquier combinación de letras y dígitos

"""
\w:
Este componente representa "caracteres de palabra". En términos más específicos, coincide con cualquier carácter alfanumérico.
Esto incluye:
Letras (tanto mayúsculas como minúsculas): a-z, A-Z
Dígitos: 0-9
El guion bajo: _
Es importante notar que la definición exacta de "caracteres de palabra" puede variar ligeramente dependiendo del motor de 
expresiones regulares y la configuración de Unicode, pero en Python, generalmente sigue esta definición.
*:
Este es un cuantificador. En las expresiones regulares, los cuantificadores indican cuántas veces puede aparecer el elemento 
precedente.
El asterisco (*) significa "cero o más ocurrencias". Esto significa que el carácter o grupo precedente puede aparecer:
Cero veces: No estar presente en absoluto.
Una vez.
Múltiples veces.
En conjunto, \w* significa:
"Cero o más caracteres alfanuméricos o guiones bajos".
"""

print(f'Mostrará el inicio y fin de "{patron5}" en la cadena "{cadena5}"')
print(("El inicio es en base a la longitud de la cadena empezando con indice 0 y cada fin de ocurrencia es +1"))

cantidad_encontrado= re.findall(patron5, cadena5)
ocurrencias = re.finditer(patron5,cadena5)
print(f'Cantidad encontrados palabras navid* : {len(cantidad_encontrado)}')

for vez in ocurrencias:
    print(vez.group(), vez.start(), vez.end())  # vez.group() recupera la palabra que cumplió patron5 = r"navid\w*" y el start y end el inicio y fin

"""
BUSCAR Y REMPLAZAR 
"""
### Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patrón en un texto

text = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern = "hola"
replacement = "Adiós"

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)  # flags=re.IGNORECASE lo toma en minúscula.
print(f'Toma la oración "{text}" y remplazará "{pattern}" por "{replacement}", obteniendo "{new_text}"')