'''
Encapsulación
En la mayoría de lenguajes que usan el paradigma de la POO nos encontramos con el concepto de encapsulación. Este consiste en poder ocultar los
atributos o métodos de una clase para que no se puedan cambiar salvo mediante otros métodos que dispongamos nosotros. Es decir, la encapsulación
consiste en denegar el acceso a los atributos y métodos internos de la clase desde el exterior.
Supongamos que tenemos una clase Coche con un atributo que sea color = “negro”. Cualquiera podría cambiar ese atributo simplemente poniendo color =
“rojo”, por ejemplo. A veces no nos interesa que un atributo se pueda cambiar. Una forma de “blindarlo” para que no se pueda cambiar su valor es mediante
la encapsulación.

Tendremos la posibilidad de especificar unos modificadores a nuestros atributos que permitirán o no que su valor se pueda cambiar.
Como norma general tendremos tres modificadores de acceso:
• Public: Los atributos public serán accesibles y modificables desde cualquier parte de nuestro código. Es el valor por defecto y sería el
equivalente a no poner nada.
• Protected: Podemos acceder a él desde la misma clase y clases hijas.
• Private: Accesible únicamente desde su clase.

Pero todo esto que hemos explicado no se aplica a Python. En Python no se especifican métodos o atributos privados ni públicos. Esto es así porque en
Python todos los atributos de una clase son públicos.

Es decir, técnicamente en Python no existe la encapsulación.

No obstante, si queremos tener algún atributo o método “oculto” a la interfaz pública, es posible indicarlo con la siguiente convención:
1. Por defecto, todos los atributos son públicos. Python asume que “Aquí todos somos adultos” y sabemos leer la documentación de nuestro código y
utilizarlo bien.
2. Si queremos indicar que algún atributo miembro de una clase es privado, lo haremos añadiendo el símbolo ‘_’ delante del nombre del tributo. Por
ejemplo: ‘MiClase._atributoPrivado’. Esto no hace que el atributo sea privado como en otros lenguajes de programación, es sólo una indicación al programador,
para que sepa que debe usarlo (aunque si quiere, puede hacerlo).
3. Si queremos una “protección extra” utilizaremos 2 guiones ‘__’, en lugar de uno: p. ej. ‘MiClase.__otroAtribPrivado’. Esto además hará que el
intérprete no lo muestre cuando llamemos a la función help para obtener más información de la clase, etc.
'''

class Ejemplo():
    
    atributo_Publico    = "Soy atributo publico. Ningun score antes del nombre"    
    _atributo_protected = "Soy atributo protegido solo alcanzable desde la clase o mis hijos"
    __atributo_privado  = "Soy un atributo inalcanzable desde fuera, DOBLE SCORE '__' ANTES DEL NOMBRE."
    
    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")
        print("   Me llamo el metodo_publico desde dentro de la clase.")
        
    def atributo_publico(self):         #! OJO: El atributo_Publico lleva la "P" en mayuscula para ser diferente a este metodo
        return self.__atributo_privado
    
    def metodo_publico(self):
        print("Al llamar a este metodo publico el puede llamar a un metodo privado")
        return self.__metodo_privado()
    
    def modificar__atributo_privado(self):   #! NO SE TE PUEDE OLVIDAR EL SELF PORQUE NO TE PUEDES REFERIR A LOS ATRIBUTOS U OTROS METODS.
        self.__atributo_privado=input("Valor para guardar en __atributo_privado: ")
        
    def mostrar_atributo_privado(self):
        print(self.__atributo_privado)    
        
        

#? --------------------DESARROLLO DEL CODIGO ----------------------------------------------------    
ej = Ejemplo()

print("1. Acceso a atributo publico:", ej.atributo_Publico)


try:
    print(ej._atributo_protected)
except Exception as e:
    print("Intente acceder a _atributo_protected")
    print(f"\n      Tipo de error/descripcion: {type(e).__name__} / {e} ")    # Da el tipo de error y su descripcion
    
try:    
    print(ej.__atributo_privado)
except Exception as e:
    print("Intente acceder a __atributo_privado")    
    print(f"\n      Tipo de error/descripcion: {type(e).__name__} / {e} ")    # Da el tipo de error y su descripcion     

try:
    print(ej.__metodo_privado())
except Exception as e:
    print("Intente acceder a __metodo_privado()")
    print(f"\n      Tipo de error/descripcion: {type(e).__name__} / {e} ")    # Da el tipo de error y su descripcion


print("\nAqui llamo a ej.metodo_publico()")
ej.metodo_publico()

print("\nHacer una modificacion de un atributo privado:")
ej.modificar__atributo_privado()

print("\nMostrar el valor de atributo privado usando un metodo :")
ej.mostrar_atributo_privado()


