'''
POLIMORFISMO.
Gerente hereda de clase Empleado y por tanto compartes el metodo mostrar_detalles()
'''

#? --------- clase Empleado --------------------------------------------------
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        
    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'
    
    def mostrar_detalles(self):
        return self.__str__()

#?-----------Clase Gerente que hereda de Empleado ------------------------------
class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento:{self.departamento}] {super().__str__()}'
  
  #! Clase Gerente heredó de Empleado y por tanto tiene el metodo "mostrar_detalles() aunque no esta explicitamente
  # def mostrar_detalles(self):
      # return self.__str__()

#? ---- Funcion Imprimir_detalles que recibe una instancia de las clases Empleado o Gerente ----------
def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    
#?-------- CUERPO DEL PROGRAMA ----------------------------------------------------------------------
empleado = Empleado('Juan', 5000)            #* Creamos el objeto empleado como instancia de clase Empleado
imprimir_detalles(empleado)                  #* Ejecutamos la funcion imprimit_detalles enviando empleado

gerente = Gerente('Karla', 6000,'Sistemas')  #* Creamos el objeto gerente como instancia de clase Empleado
imprimir_detalles(gerente)                   #* Ejecutamos la funcion imprimit_detalles enviando gerente