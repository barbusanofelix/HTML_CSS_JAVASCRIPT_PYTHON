'''
CONSTRCTORES
aunque se pueden simular varios constructores con valores por defecto o con la utilizacion
de @classmethod, solo existe un metodo __init__ por clase.

Aqui no hice el ejemplo de @classmethod , pero quise dejar la chuleta.
'''


# Declaración de la clase
class Coche():            #! Palabra clave clss y Nombre, inicia en Mayuscula y luego (): 
# Declaración de atributos
    largo = 250
    ancho = 120
    ruedas = 4
    peso = 900
    color = "rojo"
    is_enMarcha = False
    
    #! ESTA CLASE NO TIENE UN COSNTRUCTOR EXPLICITO. SINO LO COLOCAMOS SE CREA UNO INTERNO POR DEFECTO Y VACIO
    #! ES ALGO ASI:
    #  def __init__(self, largo, ancho, ruedas, peso, color, is_enMarcha):
    #      pass

    #*  Declaración de métodos
    #! OBLIGATORIO QUE EL 1er PARAMETRO SEA SELF
    def arrancar(self): # self hace referencia a la instancia de clase. 
        self.is_enMarcha = True # Es como si pusiésemos miCoche.is_enMarcha = True
        
    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"
        
#? FUNCION PARA RECORRER LOS ATRIBUTOS DE UNA ISNTANCIA CLASE. 

def imprimirAtributos(instancia):               #* Instancia es el nombre del objeto instanciado de una clase
# Recorrer los atributos utilizando vars()
    print("Atributos del coche usando vars():. Imprime solo atributos que se han modificado, pero el resto sigue existiendo")
    margen=80
    for atributo, valor in vars(instancia).items():
        print(f"{'Atributo-valor ':<{margen}}{atributo}   {valor}")
        
        #print(f"{atributo}: {valor}")        
        
#? CREAR OBJETOS, INSTANCIAS, EJEMPLARES
    #! TODA OBJETO O INSTANCIA Ó EJEMPLAR CREADO A PARTIR DE LA CLASE COCHE TENDRA LAS PROPIEDADES Y METODO DE LA CLASE
margen=80
miCoche=Coche()       #* Crea el objeto coche
miCoche2=Coche()      #* Creamos el objeto coche2       
print()
#! :<{margen} , regula la sangria antes de la impresion de la variable
#! margen=80, imprimira el texto hasta la columna 80, dejando espacios y en  
#! columna 80, la variable que queremos mostrar 
print(f"{'Imprimir el atributo is_enMarcha de miCoche2 :':<{margen}}{miCoche2.is_enMarcha}")
#print("Imprimir el atributo is_enMarcha de miCoche2 :", end=" ")
#print(miCoche2.is_enMarcha)
print(f"{'El estado es : ':<{margen}}{miCoche2.estado()}")

miCoche2.arrancar()
print()
print(f"{'CORRIMOS EL METODO coche2.arrancar() y ahora miCoche2.is_enMarcha es ':<{margen}}{miCoche2.is_enMarcha}")
print(f"{'Y ahora el estado es ':<{margen}}{miCoche2.estado()}")

print()
print(f"{'El ancho heredado de miCoche2.ancho es ':<{margen}}{miCoche2.ancho}")

miCoche2.ancho=150

print(f"{'El ancho modificado de miCoche2.ancho es ':<{margen}}{miCoche2.ancho}")
imprimirAtributos(miCoche2)
# print(dir(coche2))       #! Con estos mostramos todos los atributos y metodos de una instancia 
#* Acceso a un atributo de la clase Coche. Nomenclatura del punto.

print(f"{'El largo del miCoche2 es de ':<{margen}}{miCoche2.largo}"," cms")

miCoche2.arrancar()
print(f"{'El estado de miCoche2 es ':<{margen}}{miCoche2.estado()}")

# Acceso a un método de la clase Coche. Nomenclatura del punto.


miCoche2.ruedas = 10
print(f"{'Le asigne 10 ruedas a miCoche2 asi que tiene ruedas ':<{margen}}{miCoche2.ruedas}")
