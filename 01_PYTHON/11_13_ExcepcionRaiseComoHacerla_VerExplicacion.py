'''
EXPLICACION DE LOS ERRORES Y MEJORA DEL CODIGO CON ERROR
El código que proporcionaste tiene algunos problemas y puede mejorarse para seguir las buenas prácticas de Python. 
Aquí te explico los problemas y las sugerencias de mejora:

Problemas:
Lanzamiento de una cadena como excepción:
En Python, las excepciones deben ser instancias de clases que heredan de Exception. Lanzar una cadena como "algún error" 
no es la forma correcta de lanzar una excepción personalizada.
Captura de una cadena como excepción:
De manera similar, capturar una cadena en el bloque except no funcionará. El bloque except espera un tipo de excepción (clase) 
o una instancia de excepción.
Comparación de tipos:
La comparación '1' != 1 siempre será verdadera porque estás comparando una cadena con un entero. Esto significa que el bloque 
raise siempre se ejecutará.

Sugerencias de mejora:
Crear una excepción personalizada:
Define una clase que herede de Exception para representar tu error personalizado.
Lanzar y capturar la excepción personalizada:
Lanza una instancia de tu excepción personalizada en el bloque try.
Captura la excepción personalizada en el bloque except.
Realizar una comparación lógica:
Asegúrate de que la comparación en el bloque if tenga sentido y refleje la condición de error que deseas verificar.

Código mejorado:
------------------------------------------------------------
class AlgúnError(Exception):
    pass

try:
    if type('1') != type(1):  # Compara tipos en lugar de valores
        raise AlgúnError("Se ha producido algún error debido a la comparación de tipos")
    else:
        print("No se ha producido ningún error")
except AlgúnError as e:
    print(f"Se ha producido algún error: {e}")

-------------------------------------------------------------------------------    
Explicación de las mejoras:

class AlgúnError(Exception): pass: Se define una clase AlgúnError que hereda de Exception. Esto crea una excepción personalizada.
raise AlgúnError("Se ha producido algún error debido a la comparación de tipos"): Se lanza una instancia de AlgúnError con un 
mensaje descriptivo.
except AlgúnError as e: Se captura la excepción AlgúnError y se asigna a la variable e.
print(f"Se ha producido algún error: {e}"): Se imprime el mensaje de error de la excepción.
if type('1') != type(1): Se compara el tipo de '1' (cadena) con el tipo de 1 (entero). Esto es una comparación lógica que tiene sentido.

Puntos adicionales:
Mensajes de error descriptivos: Proporcionar mensajes de error claros y descriptivos facilita la depuración y el mantenimiento del código.
Capturar excepciones específicas: Es mejor capturar excepciones específicas en lugar de excepciones genéricas como Exception a menos 
que realmente necesites capturar cualquier tipo de excepción.
Con estas mejoras, el código es más robusto, legible y sigue las buenas prácticas de Python.
'''


#-----------------CODIGO CON ERROR ------------------------------------
try:
    if '1' != 1:
        raise "algún error"
    else:
        print ("no se ha producido algún error")
except "algún error":
    print ("se ha producido algún error")