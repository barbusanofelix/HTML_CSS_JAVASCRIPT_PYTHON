
"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos
Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )
Coche (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de
Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )
Bicicleta (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de
Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""

class Vehiculo():
    #Atributos
    color  :str
    ruedas :int
  
    #Metodos
    #Constructor clase Coche
    def __init__(self, color, ruedas):
        self.color  =color
        self.ruedas =ruedas
        
    
    def __str__(self):
        return f"Color {self.color} - Tiene {self.ruedas} ruedas"
    
    def accion(self):
        print("El vehiculo se mueve")
    
class Coche(Vehiculo):
    velocidad_km_hr:int

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)                 #! NO LLEVA EL SELF
        self.velocidad_km_hr=velocidad
    
    def __str__(self):
        return f"Coche con v={self.velocidad_km_hr} {super().__str__()} \n"

    def accion(self):
        print("El coche corre")
    
class Bicicleta(Vehiculo):
    #atributos
    tipo:str    # (urbana, montaña, etc--)    
    
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)         # Aqui van los atributos de Clase Padre Vehiculo
        self.tipo=tipo
        
    def __str__(self):        #? IMPRIMIRA LO INDICADO ENTRE COMILLAS + LLAMAR  super().__str__() QUE IMPRIME EN LA CLASE PADRE, VEHICULO          
        return '\nEsta bici es '+self.tipo+ super().__str__()+'\n'   #f"Esta bici es {self.tipo} : {super().__str__()}"
    
    def accion(self):
        print("La Bici pira")  
                
bici=Bicicleta("Roja",3,"urbana")   #* Creamos una instancia de Bicicleta llamada bici
carro=Coche("Verde",4,120)          #* Creamos una instancia de Coche llamada carro
vehiculo=Vehiculo("Azul",2)         #* Creamos una instancia de Vehiculoa llamada vehiculo

print(bici)         # LLama a __str__ de la Clase Bicicleta 
print(carro)        # LLama a __str__ de la Clase Coche.

print("POLIMORFISMO: EJECUTAREMOS EL METODO ACCION DE LOS 3 OBJETOS.")
print( "Realmente se llama el metodo accion de cada clase: bici.accion(), carro.accion(), vehiculo.accion()\n")
veh= bici,carro,vehiculo    # Defino una tupla con los objetos creados

for v in veh:      # recorro la Tupla y aplicamos el polimorfismo
    v.accion()     # vamos llamamdo al metodo accion() de bici.accion(), carro.accion() y vehiculo.accion()


         