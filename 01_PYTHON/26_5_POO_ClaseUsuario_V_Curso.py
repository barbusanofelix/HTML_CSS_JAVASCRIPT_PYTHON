'''
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

# CREACIÓN DE LA CLASE
class Usuario():
# Declaración de atributos
    nombre = "Angel"
    edad = 47
    login = "admin"
    password = "1234"
    email = "angel@loquesea.com"
    telefono = 666666666
    
    # Declaración de métodos
    def resumen(self): # self hace referencia a la instancia de clase.
        print(f'Los datos del usuarioson:\n'
                f'Nombre: {self.nombre}\n'
                f'Edad: {self.edad}\n'
                f'Login: {self.login}\n'
                f'Password:{self.password}\n'
                f'Email: {self.email}\n'
                f'Teléfono:{self.telefono}')
        
    def cambiaEdad(self):
        edadIntroducida =int(input("Introduce edad entre 18-100:"))
        if 18 < edadIntroducida < 100:
            self.edad = edadIntroducida
            print("Edad introducida correcta")
            return ""
        else:
            print("La edad introducida no es correcta.")
            self.cambiaEdad()
            return ""
        
    def muestraEdad(self):
        print('La edad del usuario es:',
        self.edad, 'años.')
        return ""

 # Creación de una instancia de la clase Usuario a la que llamaremos administrador
administrador = Usuario()

 # Una vez creado el objeto administrador, hacemos uso del método “resumen()” perteneciente a la clase Usuario
administrador.resumen()
 # Usamos los métodos cambiaEdad() y muestraEdad() de la clase Usuario.
print(administrador.cambiaEdad())
print(administrador.muestraEdad())
