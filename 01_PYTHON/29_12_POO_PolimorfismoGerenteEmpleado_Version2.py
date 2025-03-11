'''
POLIMORFISMO. - Mejorado en la presentacion de resultados
Gerente hereda de clase Empleado y por tanto compartes el metodo mostrar_detalles()

DETALLES AL FINAL
'''

#? --------- clase Empleado --------------------------------------------------
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Nombre: {self.nombre}, Sueldo: {self.sueldo}'

    def mostrar_detalles(self):
        return self.__str__()
    
#?-----------Clase Gerente que hereda de Empleado ------------------------------
class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    #? {super().__str__() : Ejecuta el metodo de Empleado, colocando el nombre y sueldo
    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}, {super().__str__()}]'

    def mostrar_detalles(self):
        return self.__str__()

#? ---- Funcion Imprimir_detalles que recibe una instancia de las clases Empleado o Gerente ----------
def imprimir_detalles(objeto):
    print(objeto.__class__.__name__)  # Imprime solo el nombre de la clase
    print(objeto.mostrar_detalles())  # Segun el objeto, se ejecuta el metodo Gerente y Empleado

#? --------CUERPO PROGRAMA ---------------------------------------------------------------------------
empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)

'''
En relacion a la version 29_11_POO_PolimorfismoGerenteEmpleados.py
 Cambiar el formato de type(objeto):

En lugar de imprimir <class '__main__.Empleado'> o <class '__main__.Gerente'>, imprimir solo el nombre de la clase 
utilizando objeto.__class__.__name__ , en la funcion "imprimir_detalles(objeto)"

2. Cambiar el formato de __str__:
   Modifique los métodos __str__ de las clases Empleado y Gerente para que la información se muestre en un formato más
   legible, usando dos puntos (:) en lugar de corchetes ([]) y eliminar la palabra "Empleado" redundante.
 
3. Eliminar la redundancia del método mostrar_detalles():
   El metodo mostrar_detalles() no es necesario, pues ya el metodo __str__ realiza la misma funcionalidad, pero para que 
   sea mas legible, lo coloque visible en la clase Gerente.
   
Cambios clave:

En la función imprimir_detalles(), he cambiado type(objeto) a objeto.__class__.__name__.
He modificado los métodos __str__ de las clases Empleado y Gerente para que la salida sea más legible.

'''