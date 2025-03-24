
'''
Ejemplo de uso de modulo.
Principal_modulo.py es un archivo python creado por mi que tiene la definion de una funcion y una clase
y la idea es probar la importacion y llamada de la funcion e instanciar la clase.


'''
# import Importar_modulo   # Importar modulo completo. No es usual.
import modulo_Ejemplo as mod   # Palabra clave "import" + nombre del modulo ó programa.py. "as" para ponerle un alias.
# Sino colocamos un alias ( "as" para llamar cualquier elemento del modulo escribimos "modulo_ejemplo." y luego una variable, funcion, clase...."
# Mas usual y conveniente es importar lo que se necesite:
#from modulo_Ejemplo import variable as va, funcion_importada as func # Asi no es necesario colocar modulo_Ejemplo. , Es decvir, lo importado se llama derecho.
#from modulo_Ejemplo import *  # Importa todos los elementos del modulo y se llaman directamente , sin notacion de . 

import modulos.modulo_Ejemplo2 as mod2     # nombre de la carpeta ( modulos ) y luego el nombre del archivo 

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
    
# Hay que separarlo con este if para que el punto de entrada sea aca.
if __name__=="__main__":
    ejecutar_modulo_en_igual_directorio()
    print("\nVamos con la llamada al modulo dentro de carpeta ubicada en mismo directorio que este programa:\n")
    ejecutar_modulo_en_igual_directorio2()
