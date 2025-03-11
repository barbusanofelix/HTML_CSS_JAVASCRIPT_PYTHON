'''
NOMBRE DE UNA CLASE 

En Python 3, las tres formas son válidas, pero las dos primeras (class Padre(): y class Padre:) son las más comunes
y recomendadas. La tercera forma (class Padre(object):) es redundante en Python 3 y se utiliza principalmente para 
compatibilidad con código antiguo de Python 2.

Crearemos una clase Usuario que tendrá los siguientes atributos:
    • nombre : string
    • edad : number
    • login : string
    • password : string
    • email : string
    • telefono : number

Y los siguientes métodos:
    • Resumen(): Sacará un resumen de los datos del usuario
    • cambiaEdad(): Nos dará la posibilidad de pedir al
    usuario que introduzca una nueva edad.
    • muestraEdad(): Nos mostrará la edad del usuario
    
Por último, crearemos una instancia de la clase Usuario a la que llamaremos administrador y
llamaremos a los métodos de la clase Usuario para este administrador usando la nomenclatura del
punto.


'''
#? CREAMOS LA CLASE Usuario
class Usuario():
    #? Atributos
    nombre  :str
    edad    :int
    login   :str
    password:str
    email   :str
    telefono:int
    
    #? CONSTRUCTOR DE LA CLASE. ( def __init__)
        #* self es OBLIGATORIO, EN TODOS LOS METODOS
        #* Ponemos el nombre del Parametro : [tipo] [=Valor por defecto]
        #! ADEMAS DE INICIALIZAR LOS ATRIBUTOS EL CONSTRUCTOR PUEDE USARSE PARA HACER
        #! OTRAS ACTIVIDADES CMO ABRIR CONEXIONES, 
    def __init__(self, nombre :str, edad:int=None, login:str=None, password:str=None, 
                 email:str=None, telefono:int=None):
        #* Asignamos a los atributos de la clase ( self.) con el recibido
        self.nombre=nombre
        self.edad=edad
        self.login=login
        self.password=password
        self.email=email
        self.telefono=telefono
        
    #? ---------ZONA DE METODOS --------------------------------------------------------    
    # Imprime un resumen de los atributos del Usuario
    def resumen(self):  #? RESUMEN DE LOS ATRIBUTOS DEL USUARIO.    
        print("Resumen del usuario:")
        for atributo, valor in vars(self).items():  # o self.__dict__.items()
            print(f"  {atributo:<25}: {valor}")     #* Formateo para 2 columnas :<25 hace que la 2da empiece en 25
        print()
            
    # solicita una edad y la asigna a la edad del Usuario     
    def cambiaEdad(self):
        print()
        error = True
        mensajeError="\nError!!!...La edad debe ser numero entero:  18-100.\n"
        while error:
            try:
                edad = int(input("Suministra nueva edad: "))
                if (edad <18 or edad > 100 ):
                    raise ValueError(mensajeError)  # Lanza excepción personalizada
                self.edad = edad
                error = False
            except ValueError:  # Captura ValueError y su mensaje
                print(f"{mensajeError}")  # Imprime el mensaje de error
        self.resumen()
        
    # Muestra la edad del usuario
    def muestraEdad(self):
        print("EDAD de USUARIO:")
        print(f"\n  {self.nombre:<25}: {self.edad}\n")      # \n inserta salto de linea


#? CREACION OBJETOS, INSTANCIA, EJEMPLAR

administrador = Usuario(nombre="Felix", telefono=643537550)

administrador.resumen()             # Resumen de los atributos de 
administrador.cambiaEdad()
administrador.muestraEdad()     
        
    