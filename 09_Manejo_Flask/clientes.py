
'''DEFINICION DE LA CLASE CLIENTE'''

#! IMPORTANTE PONER LA BASE DE DATOS Zona_Fit_db COMO SET AS DEFAULT SCHEMA 

# Clase de Modelo o Dominio de la Aplicacion. En este caso la clase Cliente. Representa la informacion 
# mas imprtante a manejar por la aplicacion. 


class Cliente():
    
    

    # Definiremos todos los parametros como opcionales , es decir, por defecto cada uno sera None    
    def __init__(self, id=None, nombre=None, apellido=None,membresia=None):
        self.id=id                                       # Por cada cliente añadido incrementamos el id
        self.nombre     =nombre
        self.apellido   =apellido
        self.membresia  =membresia
        
        
    def __str__(self):
        return (f'{self.id:<6}{self.nombre:<35}'
                f'{self.apellido:<35}{self.membresia:<10}')   # Retornamos una cadena con los atributos
        

    