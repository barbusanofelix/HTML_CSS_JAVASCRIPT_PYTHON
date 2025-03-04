'''
Los roles de las excepciones en Python
• Manejo de errores: Se utilizan para informar de errores y/o de una situación anómala así como de detener el flujo de programa.
• Notificación de eventos: P. ej. terminar una búsqueda sin resultados sin tener que usar variables de control.
• Manejo de casos especiales: Podemos dejar el manejo de algunas situaciones especiales que ocurren con poca frecuencia a excepciones.
• Acciones de limpieza/finalización: Operaciones de limpieza que se ejecutan tanto como si ha habido errores como si no y que nos ayudan a
asegurarnos que este tipo de operaciones ocurren siempre, independientemente de que haya habido un error o no. Esto es útil para asegurarnos
 que cerramos una conexión, un fichero, etc.

En Python disponemos de 4 sentencias que podemos utilizar para manejar excepciones:

• try/except: Intercepta y recupera excepciones disparadas por Python o por nuestro código.

• try/finally: Realiza tareas de limpieza ocurran las excepciones o no.

• raise: Dispara una excepción manualmente en el código.

• assert: Dispara una excepción condicionalmente.

'''

def indexador(objeto, indice):  # Simplemente recibira un objeto 
    return objeto[indice]       # Devuelve la posicion en el objeto, segun el indice. 

try:
    print(indexador("Python",6))    # Le pasamos Python e indice 0, que devolvera la posicion Cero de Python, es decir , la P
    # El try la manda al except, en caso de erro
except Exception as e:    # NO RECOMENDADO DEJARLO TAN ABIERTO 
    print()
    print('Valor del indice es muy alto en print(indexador("Python",indice)) ')
    print()
    print(f"Tipo de error: {type(e).__name__}")                                 # Obtenemos el tipo de error
    print(f"Descripción del error: {e}")                                        # Descripcion adicional del error
    
    

print("Salimos del try/catch")    

'''try:
    print(indexador("Python",6))    # Le pasamos Python e indice 0, que devolvera la posicion Cero de Python, es decir , la P
    # El try la manda al except, en caso de erro
except Exception (IndexError,TypeError):     # RECOMENDADO DEJARLO TAN ABIERTO 
    print(f"Error ",{type(e).__name__})

print("Salimos del try/catch")    
'''
