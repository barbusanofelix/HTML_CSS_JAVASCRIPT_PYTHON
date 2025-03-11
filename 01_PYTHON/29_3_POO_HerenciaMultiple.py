'''
HERENCIA MULTIPLE 
EN ESTE EJEMPLO TRATE DE QUE PATINETA ELECTRICA HEREDE DE Vehiculo y VehiculoElectrico

MUY IMPORTANTE: SE DA PREFERENCIA SIEMPRE A LA PRIMERA CLASE QUE SE INDIQUE ENTRE PARÉNTESIS.
HEREDA EL CONSTRUCTOR DE LA PRIMERA CLASE QUE PUSIMOS EN EL PARÉNTESIS, Y EN CASO DE QUE HAYA
MÉTODOS COMUNES, TAMBIÉN HEREDA EL DEL PRIMERO.
PARA SOBRESCRIBIR UN MÉTODO HEREDADO DE LA CLASE PADRE, SIMPLEMENTE VOLVEMOS A ESCRIBIR EL MÉTODO
CON TODOS SUS ARGUMENTOS Y AÑADIMOS EL NUEVO ARGUMENTO.
'''

#? CLASE PADRE: Vehiculo()
class Vehiculo():
    
#? Coonstructor de Vehiculo. NOTA: Solo pide marca y modelo pero hay color="Negro", arrancado(False), Parado=True.    
    def __init__(self, marca, modelo, nombreObjeto=None):
        self.marca = marca
        self.modelo = modelo
        self.color = "Negro"
        self.arrancado = False
        self.parado = True
        print(f"Usamos el Constructor de Vehiculo para inicializar {nombreObjeto} con {self.marca} : {self.modelo} ")

#? DEFINICION DE METODOS
    def arrancar(self):
        print("Metodo arrancar() dentro de Clase Vehiculo")
        self.arrancado = True
        self.parado = False

    def parar(self):
        print("Metodo parar() dentro de Clase Vehiculo")
        self.parado = True
        self.arrancado = False

    def resumen(self):
        print("Metodo resumen dentro de clase Vehiculo")
        print("Marca:", self.marca, "\n","Modelo:", self.modelo,"\n",
                "Color:", self.color, "\n","Está arrancado:",self.arrancado,"\n",
                "Está parado:", self.parado)
    
    def resumenOrdenado(self):  #? RESUMEN DE LOS ATRIBUTOS DEL USUARIO.    
        print("Metodo ResumenOrdenado dentro de clase Vehiculo:")
        for atributo, valor in vars(self).items():  # o self.__dict__.items()
            print(f"  {atributo:<25}: {valor}")     #* Formateo para 2 columnas :<25 hace que la 2da empiece en 25
        print()    
        

#? ---------------------  FIN DE MTODOS CLASE VEHICULO-----------------------------------------------

#? CLASE VehiculoElectrico()
class VehiculoElectrico():
    
#? Coonstructor de Vehiculo. NOTA: Solo pide marca y modelo pero hay color="Negro", arrancado(False), Parado=True.    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Rojo"
        self.cargado = False
        self.enchufado = False

#? DEFINICION DE METODOS
    def cargar(self):
        print("Metodo cargar dentro de clase VehiculoElectrico")
        self.cargado = True
        self.enchufado = False

    def usar(self):
        print("Metodo usar() dentro de clase VehiculoElectrico")
        self.enchufado = False

    def resumenElec(self):
        print("Metodo resumenElec dentro de clase VehiculoElectrico")
        print("Marca:", self.marca, "\n","Modelo:", self.modelo,"\n",
                "Color:", self.color, "\n","Está cargado:",self.cargado,"\n",
                "Está enchufado:", self.enchufado)
    
    def resumenOrdenado(self):  #? RESUMEN DE LOS ATRIBUTOS DE LA CLASE.    
        print("Metodo resumenOrdenado dentro de Clase VehiculoElectrico:")
        for atributo, valor in vars(self).items():  # o self.__dict__.items()
            print(f"  {atributo:<25}: {valor}")     #* Formateo para 2 columnas :<25 hace que la 2da empiece en 25
        print()    
        

#? ---------------------  FIN DE METODOS CLASE VEHICULOELECTRICO-----------------------------------------------



    
'''
Aquí estamos indicando que la clase PatinetaElec que  hereda de Vehículo y VehiculoElectrico. 

MUY IMPORTANTE: SE DA PREFERENCIA SIEMPRE A LA PRIMERA CLASE QUE SE INDIQUE ENTRE PARÉNTESIS.
HEREDA EL CONSTRUCTOR DE LA PRIMERA CLASE QUE PUSIMOS EN EL PARÉNTESIS, Y EN CASO DE QUE HAYA
MÉTODOS COMUNES, TAMBIÉN HEREDA EL DEL PRIMERO.
PARA SOBRESCRIBIR UN MÉTODO HEREDADO DE LA CLASE PADRE, SIMPLEMENTE VOLVEMOS A ESCRIBIR EL MÉTODO
CON TODOS SUS ARGUMENTOS Y AÑADIMOS EL NUEVO ARGUMENTO.


 '''   
    
#? PatinetaElec HEREDA DE VEHICULO Y VEHICULOELECTRICO. Todos los atributos y metodos de vehiculo son heredados por Moto    
class PatinetaElec(Vehiculo, VehiculoElectrico):
   # pass   Al colocar atributos o metodos en la clase ya no es necesario el pass
    is_electrico = True
    #Método propio de la clase Moto, no heredado del padre.
    #La clase Moto sobrescribe el método resumen() heredado del padre ( Vehiculo)
        
#? ------------------ FINAL CLASE   PATINETAELEC QUE HEREDO DE VEHICULO Y VEHICULO ELECTRICO -------------------------------------------

#? -----------------DEFINICION CLASE COCHE ....HEREDA DE VEHICULO ----------------------------------------------------

class Coche(Vehiculo):
    #* No se definen atributos de Coche...son los mismos que Vehiculo, con EXCEPCION A CILINDRADA
    #* El atributo Cilindrada lo crea al ejecutar el metodo cilindrada()
    
    #METODOS
    def cilindrada(self):
        print("Metodo Cilindrada() dentro de clase Coche")
        self.cilindrada=3000
        
    def estado(self):
        print("Metodo estado() dentro de clase Coche. Sobre-escribe el metodo estado() de la clase Padre Vehiculo")
        print("Marca", self.marca,"Modelo",
        self.modelo, "Cilindrada", self.cilindrada)
    
#? ----------------------FIN DE CLASE Coche ------------------------------------------------------
    
miCoche = Vehiculo("Renault", "Megane")    # Ojo: miChoche es instancia de Vehiculo  
miCoche.arrancar()

miCocheVeh =Coche("Ford", "Eco-Sport","MiCocheVeh")  # Usa constructor de Vehiculo



#miCoche.resumen()
miCoche.resumenOrdenado()               # Escribe el resumen de los atributos en 2 columnas

miPatineta = PatinetaElec("Roller Patineta","Tri-Ruedas")      # Crea una instancia de Clase Moto que hereda de Vehiculo
# miMoto.resumen()

miPatineta.cargar()                 # LLama al metodo cargar que esta en VehiculoElectrico

print("LLamar a Metodo resumen() de miPatineta. LLama a resumen() en Vehiculo porque no esta sobre-escrito en PatinetaElec\n")
miPatineta.resumen()
print("Volver a llamar resumen sin ()...NO HACE NADA, HAY QUE COLOCARLE LOS ()")
miPatineta.resumen
print("Asigne azul Intenso al color, miPatineta.color='Azul Intenso' y al llamar resumen muestra azul intenso ")
miPatineta.color="Azul Intenso"
miPatineta.resumen()
print("miPatineta.arrancado:",miPatineta.arrancado)
print("miPatineta.arrancar():",miPatineta.arrancar(), " Aparece None porque el metodo no tiene un return. ")
print("miPatineta.cargado:",miPatineta.cargado)
print("miPatineta.cargar():",miPatineta.cargar(),  " Aparece None porque el metodo no tiene un return. ")
print("Metodo Resumen electrico , miPatenta.resumenElect(), que viene de la clase VehiculoElec", miPatineta.resumenElec(), "Aparece None porque el metodo no tiene un return. ")

