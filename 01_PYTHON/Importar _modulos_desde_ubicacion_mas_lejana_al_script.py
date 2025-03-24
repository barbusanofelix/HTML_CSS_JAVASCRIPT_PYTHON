'''

Dudas: Ver video: https://www.youtube.com/watch?v=hWbD_6xhYe0

Ejemplo de uso de importar modulos en ubicaciones distintas.
1. Desde misma carpeta que el script de Python: import modulo_Ejemplo as mod 
2. Desde una carpeta que esta ubicada en una carpeta paralela a la que tiene e script de Python.
   import modulos.modulo_Ejemplo2 as mod2  
   "E:\Python\WorkSpace curso Python_HTML_CSS_JavaScript\01_PYTHON\modulos"
   El script esta en : 
   "E:\Python\WorkSpace curso Python_HTML_CSS_JavaScript\01_PYTHON\Importar_modulo_desde_otra_ubicacion.py"
3. Desde una carpeta no paralela al Script . En ese caso hay que añadir el path de ubicación al sistema.   
   La ubicacion del modulo esta en la carepta:
   E:\Python\WorkSpace curso Python_HTML_CSS_JavaScript\modulos_Ejemplo
   En estos casos hay que añadir el path de busqueda de la importacion y será valido solo mientras corre el
   programa. Es decir, el path NO queda grabado en el sistema.
    Pasos serian:
    a) importamos sys y os, para el manejo correcto de path
    b) guardamos la ruta absoluta de la carpeta donde esta el modulo:
        ruta_modulo = r"E:\Python\WorkSpace curso Python_HTML_CSS_JavaScript\modulos_Ejemplo"
    c) Aadimos la ruta al path:
        sys.path.append(ruta_modulo)
    d) importamos el modulo:
        import modulo_Ejemplo3 as mod3            

'''




# import Importar_modulo   # Importar modulo completo. No es usual.
import modulo_Ejemplo as mod   # Palabra clave "import" + nombre del modulo ó programa.py. "as" para ponerle un alias.
# Sino colocamos un alias ( "as" para llamar cualquier elemento del modulo escribimos "modulo_ejemplo." y luego una variable, funcion, clase...."
# Mas usual y conveniente es importar lo que se necesite:
#from modulo_Ejemplo import variable as va, funcion_importada as func # Asi no es necesario colocar modulo_Ejemplo. , Es decvir, lo importado se llama derecho.
#from modulo_Ejemplo import *  # Importa todos los elementos del modulo y se llaman directamente , sin notacion de . 

import modulos.modulo_Ejemplo2 as mod2     # nombre de la carpeta ( modulos ) y luego el nombre del archivo 

#? -------- PROCESO PARA AÑADIR PATH PARA IMPORTAR UN MODULO EN UNA UBICACION "INUSUAL"
import sys   # se encarga de la parte de Python relacionada con la importación de módulos
import os    # se encarga de la parte del sistema operativo relacionada con las rutas de archivos.

# Ruta absoluta al directorio del módulo
ruta_modulo = r"E:\Python\WorkSpace curso Python_HTML_CSS_JavaScript\modulos_Ejemplo"

# Añadir la ruta a sys.path
sys.path.append(ruta_modulo)

# Importar el módulo
import modulo_Ejemplo3 as mod3   #! DA ABVERTENCIA PORQUE LA RUTA ( "ruta_modulo") no se agregara hasta correr pero funciona.

''' LLamar la funcion en el modulo'''
def ejecutar_modulo_en_igual_directorio():
    #print(variable)  # Cuando importamos con from [modulo] import variable NO hay que escribir 
    #funcion_importada()
    #instancia=Clase_importada()
    print(mod.variable)
    mod.funcion_importada()                    # imprimirá un mensaje
    instancia_clase=mod.Clase_importada()
    print("Atributo dentro de la clase:",instancia_clase.var_clase)

''' LLamar la funcion en el modulo'''
def ejecutar_modulo_en_igual_directorio2():
    #print(variable)  # Cuando importamos con from [modulo] import variable NO hay que escribir 
    #funcion_importada()
    #instancia=Clase_importada()
    print(mod2.variable)
    mod2.funcion_importada()                    # imprimirá un mensaje
    instancia_clase=mod2.Clase_importada()
    print("Atributo dentro de la clase:",instancia_clase.var_clase)

def ejecutar_modulo_en_igual_directorio3():
    #print(variable)  # Cuando importamos con from [modulo] import variable NO hay que escribir 
    #funcion_importada()
    #instancia=Clase_importada()
    print(mod3.variable)
    mod3.funcion_importada()                    # imprimirá un mensaje
    instancia_clase=mod3.Clase_importada()
    print("Atributo dentro de la clase:",instancia_clase.var_clase)
    
# Hay que separarlo con este if para que el punto de entrada sea aca.
if __name__=="__main__":
    ejecutar_modulo_en_igual_directorio()
    print("\nVamos con la llamada al modulo dentro de carpeta ubicada en mismo directorio que este programa:\n")
    ejecutar_modulo_en_igual_directorio2()
    print(sys.path)         
    #! print(sys.path) : Muestra los directorios donde Python buscará por defecto un modulo para añadir a nuestro script
    #! Si el modulo que queremos importar se encuentra dentro de cualquier de estos directorios ( sin haber agregado el path de la carpeta del modulo )
    #! La salida del path del sistema es:
    '''
    ['e:\\Python\\WorkSpace curso Python_HTML_CSS_JavaScript\\01_PYTHON', 
    'C:\\Users\\barbu\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 
    'C:\\Users\\barbu\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 
    'C:\\Users\\barbu\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 
    'C:\\Users\\barbu\\AppData\\Local\\Programs\\Python\\Python313', 
    'C:\\Users\\barbu\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']
    
    '''
    print("\nCreamos un path para importar modulo_Ejemplo3:\n")
    ejecutar_modulo_en_igual_directorio3()
