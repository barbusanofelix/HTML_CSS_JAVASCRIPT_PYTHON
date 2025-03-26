
'''
Es un ejemplo para probar la importacion de un modulo.
Este archivo lo usaré como un modulo que importare desde Importar_modulo.py



'''

variable = "Variable de mi módulo, en la carpeta modulo_Ejemplo y es el ejemplo 3s"

def funcion_importada():
    print("Función de mi módulo (Ubicado en la carpeta modulos) en el ejemplo 3 ")

class Clase_importada():
    
    var_clase="Variable dentro de la clase Importada, dentro de la carpeta modulos, ejemplo 3"
    def __init__(self):
        print("Se creo una instancia de Clase importada, que se ubica dentro carpeta modulos, ejemplo 3")
        
        
if __name__=='__main__':
    print("Si este print se ejecuta significa que este modulo es la clase principal, dentro de la carpeta modulos, ejemplo 3.")        
        

