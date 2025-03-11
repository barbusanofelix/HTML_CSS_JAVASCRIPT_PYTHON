'''
Comparacion al NO usar Super() vs. Usar super()

'''
#? -----------------  CLASE PADRE E HIJA SIN USAR SUPER ---------------------------------
#! LAS CLASES PADRES SE PUEDEN CREAR HEREDANDO DE object o SIMPLEMENTE NO COLOCARLA.
class PadreSin_super(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas):
    #Definimos los Atributos en el constructor de la clase
        self.ojos = ojos
        self.cejas = cejas
        
class HijoSin_super(PadreSin_super): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #Definimos los atributos en el constructor
        self.ojos = ojos #Sobreescribimos cada atributo
        self.cejas = cejas
        self.cara = cara #Especificamos el nuevo atributo para Hijo


# PROGRAMA PRINCIPAL
Tomas = HijoSin_super('Marrones', 'Negras','Larga') #Instanciamos
print ("\n",Tomas.ojos, Tomas.cejas,Tomas.cara) #Imprimimos los atributos del objeto
#? ------------- FIN DE EJEMPLO SIN USAR SUPER ----------------------------------------------

print("\n AQUI EL EJEMPLO USANDO SUPER O SU EQUIVALENTE EN EL CONSTRUCTOR LLAMANDO AL CONSTRUCTOR DEL PADRE\n")

#? ------------- CLASE PADRE E HIJA USANDO SUPER ( Padre.__init__()----------------------------
class Padre(): #Creamos la clase Padre
    def __init__(self, ojos, cejas):
    #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
        
class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        Padre.__init__(self, ojos, cejas)  #! ASIGNA USANDO LA CLASE PADRE.NOTAR QUE PEDIMOS LOS PRIMEROS ATRIBUTOS, OJOS Y CEJAS
        #Especificamos la clase y llamamos a su constructor + Atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo

Tomas = Hijo('Marrones', 'Negras', 'Larga')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)
#? ------------- FIN DE EJEMPLO USANDO SUPER CON NOMBRE DE LA CLASE PADRE -----------------------------------
'''
Utilizando super(). De esta forma es casi el mismo código, pero no necesitamos especificar la clase
padre, por lo que podremos cambiarle el nombre en cualquier momento y nuestro código seguirá
funcional.

De todas estas opciones *** debemos quedarnos con el uso de super() *** como forma de programar más
correcta.
Nota: En el caso de la Herencia Múltiple super() no Nos sirve. Debemos llamar a los constructores de
ambas clases especificándolas por su nombre y si cambiamos el nombre u orden de la clase deberemos
especificarlo.

'''

#? --------------EJEMPLO USANDO SUPER -----------------------------------------------------------------------

class Padre(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas):
    #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas

class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        super().__init__(ojos, cejas)#Solicitamos a super llamar de la clase padre de esos atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo

Tomas = Hijo('Marrones', 'Negras', 'Larga')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)
#? --------------FIN DE EJEMPLO USANDO SUPER -----------------------------------------------------------------
