class Coche():
    # Método constructor
    def __init__(self):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__peso = 900
        self.__color = "rojo"
        self.__is_enMarcha = False
        
    def get_ruedas(self):
        return self.__ruedas 
       
    def set_ruedas(self, ruedas):
        self.__ruedas=ruedas   
            
    def get_is_enMarcha(self):
        return self.__is_enMarcha
    
    # Declaración de métodos
    def arrancar(self): # self hace referencia a la instancia de clase.
        self.__is_enMarcha = True # Es como si pusiésemos miCoche.is_enMarcha =True
        print(self.__color)
        
    def estado(self):                       #! El Metodo tiene return de texto asi que hay que imprimrlos
        print("Estado de mi coche: ")
        if self.__is_enMarcha:
            return "El coche está arrancado"
        else:
            return "El coche está parado"
    # Declaración de una instancia de clase, objeto de clase o ejemplar de clase.

miCoche = Coche()
print(miCoche.get_ruedas())
miCoche.set_ruedas(9)
print(miCoche.get_ruedas())
print("Mi coche tiene", miCoche.get_ruedas(),"ruedas.")
miCoche.arrancar()
print("El estado del coche: ", miCoche.estado())  
print("Esta en marcha : ",miCoche.get_is_enMarcha())
#print(miCoche.__color)
#print("El estado de la variable is_enMarcha es :",miCoche.__is_enMarcha)
