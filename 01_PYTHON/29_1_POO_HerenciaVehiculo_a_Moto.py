'''
HERENCIA DE UNA CLASE A OTRA
'''

#? CLASE PADRE: Vehiculo()
class Vehiculo():
    
#? Coonstructor de Vehiculo. NOTA: Solo pide marca y modelo pero hay color="Negro", arrancado(False), Parado=True.    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Negro"
        self.arrancado = False
        self.parado = True

#? DEFINICION DE METODOS
    def arrancar(self):
        self.arrancado = True
        self.parado = False

    def parar(self):
        self.parado = True
        self.arrancado = False

    def resumen(self):
        print("Marca:", self.marca, "\n","Modelo:", self.modelo,"\n",
                "Color:", self.color, "\n","Está arrancado:",self.arrancado,"\n",
                "Está parado:", self.parado)
    
    def resumenOrdenado(self):  #? RESUMEN DE LOS ATRIBUTOS DEL USUARIO.    
        print("Resumen del usuario:")
        for atributo, valor in vars(self).items():  # o self.__dict__.items()
            print(f"  {atributo:<25}: {valor}")     #* Formateo para 2 columnas :<25 hace que la 2da empiece en 25
        print()    
        

#? ---------------------  FIN DE MTODOS -----------------------------------------------
    
'''
Aquí estamos indicando que la clase Moto hereda de Vehículo. 
Se heredan atributos y métodos, incluido el constructor.
 '''   
    
#? Moto HEREDA DE VEHICULO. Todos los atributos y metodos de vehiculo son heredados por Moto    
class Moto(Vehiculo):
    pass

    
miCoche = Vehiculo("Renault", "Megane")  
miCoche.arrancar()
#miCoche.resumen()
miCoche.resumenOrdenado()               # Escribe el resumen de los atributos en 2 columnas

miMoto = Moto("Kawasaki", "Ninja")      # Crea una instancia de Clase Moto que hereda de Vehiculo
# miMoto.resumen()
miMoto.resumenOrdenado()                 # Escribe el resumen de los atributos en 2 columnas