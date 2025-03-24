
#import modulo_Ejemplo as mod     #Importamos el modulo_Ejemplo con alias mod
#from modulo_Ejemplo import * 

#! Importar un modulo que no este en el mismo directorio que el programa principal:
#! Caso 1:  El modulo que queremos importar esta una carpeta que se ubica dentro del
#!          directorio del script principal....digamos que la carpeta se llama modulos
#!          

#Cuando se importa un modulo Python crea una carpeta llamada pycache que 
# se usa para guardar los modulos compilados para acelerar la ejecucion.

print(dir())   # Espacio de nombres del modulo que se ejecuta.
# dir() genera ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__', 'mod']
# Fijate que mod es el alias de modulo que le colocamos.
# Cuando importamos el modulo completo con 'from modulo_Ejemplo import *' hacemos que el modulo parezca estar
# integrado al script principal pues podremos ver con 'print(dir()) ' los elementos dentro de modulo_Ejemplo.

print(__name__)  # Salida es __main__ porque este es el espacio de nombres que le asigna Python al fichero principal
print(__file__)  # Salida 'e:\Python\WorkSpace curso Python_HTML_CSS_JavaScript\01_PYTHON\nameSpace_en_Python.py' que es
                 # la direccion completa de este archivo y su nombre.
#print(dir(mod))  # Salida de dir(mod) : ['Clase_importada', '__builtins__', '__cached__', '__doc__', '__file__', 
                 # '__loader__', '__name__', '__package__', '__spec__', 'funcion_importada', 'variable']   
                 # Fijate que aparece los elementos definidos en el archivo  'modulo_Ejemplo' as mod , como 'Clase_importada', 
                 # funcion_importada y variable.
                           
#print(mod.__name__)  # Salida modulo_Ejemplo. Fijate que devuelve el nombre del archivo pero NO devuelve __main__,
                     # porque __main__ es exclusivo para el script principal.

               