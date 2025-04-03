''' CLASE SERVICIO SNACKS'''

import os.path


class ServicioSnacks():
    NOMBRE_ARCHIVO='Snacks.txt'                 # Una constante.
    
    def __init__(self):
        self.snacks=[]                          # creamos una lista vacia 
        #Verificamos si existe el el archivo Snacks.txt
        #* Si existe cargamos los Snacks en la lista 
        if os.path.isfile(self.NOMBRE_ARCHIVO):             # verifica si existe el archivo
            self.snacks=self.obtener_Snacks
            
        
        #* Sino existe cargamos algunos Snacks iniciales
        
        
    def obtener_Snacks(self):
        pass
        
    
    
    def agregarSnacks(self):
        pass
    
    
    def agregarSnacks(self):
        pass
    
    
    def mostrarSnacks(self):
        pass
    
    
    
