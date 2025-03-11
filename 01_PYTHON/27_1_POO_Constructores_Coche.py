
'''
Constructores
Un constructor se define como un método especial con el que damos un estado inicial a nuestros objetos.

Siguiendo con el ejemplo de nuestra clase Coche, podemos crear un constructor con el que demos un
estado inicial a los objetos de clase Coche que creemos, de tal forma que cada coche creado ya
disponga de una serie de atributos y métodos “por defecto”. Luego podremos cambiarlos si queremos,
pero “de fábrica” todos los coches saldrán con los atributos y métodos que pongamos en el constructor.
'''
# Declaración de la clase
# Declaración del constructor de la clase
class Coche():
    
    #? CONSTRUCTOR : ATRIBUTOS DE LA CLASE
    def __init__(self):
        self.largo = 250
        self.ancho = 120
        self.ruedas = 4
        self.peso = 900
        self.color = "rojo"
        self.is_enMarcha = False
        
#* Declaración de métodos
    def arrancar(self): #self hace     referencia a la instancia de clase.
        self.is_enMarcha = True #Es como si pusiésemos miCoche.is_enMarcha = True
        
    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"

# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
coche_1 = Coche()
# Acceso a un atributo de la clase Coche.Nomenclatura del punto.
coche_1.ruedas = 7
print("El largo del coche es de" , coche_1.largo, "cm.")
coche_1.arrancar()
print("Estado : ", coche_1.estado())
# Acceso a un método de la clase Coche.Nomenclatura del punto.
print("El coche está arrancado:" ,coche_1.arrancar(), " Imprime None porque coche_1.arrancar() no imprime nada")  #! No imprime nada porque el metodo NO imprime.
# Mejor cambiamos a la impresion de is_enMarcha
print("El coche está arrancado:" ,coche_1.is_enMarcha)
