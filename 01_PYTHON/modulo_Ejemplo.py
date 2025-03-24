
'''
Es un ejemplo para probar la importacion de un modulo.
Este archivo lo usaré como un modulo que importare desde Importar_modulo.py



'''

variable = "Variable de mi módulo"

def funcion_importada():
    print("Función de mi módulo")

class Clase_importada():
    
    var_clase="Variable dentro de la clase Importada"
    def __init__(self):
        print("Se creo una instancia de Clase importada")
        
        
if __name__=='__main__':
    print("Si este print se ejecuta significa que este modulo es la clase principal")        
        

