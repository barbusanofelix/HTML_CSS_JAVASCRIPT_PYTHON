'''
HERENCIA DE UNA CLASE A VEHICULO -> MOTO -> KWAD

Ademas de la herencia sucesiva en la clase Moto se añade atributos propios de la clase Moto 
y se sobre-escribe el metodo resumen. 
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
        print("Resumen de atributos:")
        for atributo, valor in vars(self).items():  # o self.__dict__.items()
            print(f"  {atributo:<25}: {valor}")     #* Formateo para 2 columnas :<25 hace que la 2da empiece en 25
        print()    
        

#? ---------------------  FIN DE MTODOS CLASE VEHICULO-----------------------------------------------
    
'''
Aquí estamos indicando que la clase Moto hereda de Vehículo. 
Se heredan atributos y métodos, incluido el constructor.
 '''   
    
#? Moto HEREDA DE VEHICULO. Todos los atributos y metodos de vehiculo son heredados por Moto    
class Moto(Vehiculo):
   # pass   Al colocar atributos o metodos en la clase ya no es necesario el pass
    is_carenado = False
    #Método propio de la clase Moto, no heredado del padre.
    def poner_carenado(self):
        self.is_carenado = True
    #La clase Moto sobrescribe el método resumen() heredado del padre ( Vehiculo)
    def resumen(self):
        print("El modelo es una moto","\n","Marca:", self.marca, "\n","Modelo:", self.modelo, "\n",
        "Color:", self.color, "\n","Está arrancado:", self.arrancado,"\n","Está parado:", self.parado,"\n",
        "Tiene carenado:",self.is_carenado)
        
    def resumenOrdenado(self):  #? RESUMEN DE LOS ATRIBUTOS DEL USUARIO.    
        print("Resumen de atributos, en Moto:")
        for atributo, valor in vars(self).items():  # o self.__dict__.items()
            print(f"  {atributo:<25}: {valor}")     #* Formateo para 2 columnas :<25 hace que la 2da empiece en 25
        print()        
        
#? ------------------ FINAL CLASE MOTO QUE HEREDO DE VEHICULO -------------------------------------------

#? -------CLASE KWAD QUE HEREDO DE MOTO Y MOTO DE VEHICULO ----------------------------------------------
class kwad(Moto):   # Hereda todos los metodos de Moto y vehiculo.
    pass

#? ---------------FINAL CLASE KWAD ----------------------------------------------------------------------
    
miCoche = Vehiculo("Renault", "Megane")  
miCoche.arrancar()
#miCoche.resumen()
miCoche.resumenOrdenado()               # Escribe el resumen de los atributos en 2 columnas

miMoto = Moto("Kawasaki", "Ninja")      # Crea una instancia de Clase Moto que hereda de Vehiculo
# miMoto.resumen()
print("Metodo Resumen Ordenado de miMoto heredado de Vehiculo pero lo coloque en MiMoto\n")
miMoto.resumenOrdenado()                 # Escribe el resumen de los atributos en 2 columnas

print("Metodo Resumen de miMoto, sobre-escrito en la clase Moto\n")
miMoto.resumen()

print("Metodo Resumen de miKwad, heredado de clase Moto\n")
miKwad = kwad("Linhai", "LH 500")
print("El metodo resumen es heredado de Moto y lo aplica tal cual esta en Moto\n")
miKwad.resumen()
