'''
USO DE Super: 
Se coloca dentro del constructor de clase que heredo de cierta clase Padre.
Super, hace referencia a los atributos de la clase Padre que son compartidos por la clase hija y asi 
no hay que reasignar los atributos de entrada a los de la clase , pues ya esa asignacion esta en 
la clase principal es como decirle que haga la asignacion.
Ver el cosntructor de la clase persona, def __init__(self) 

'''


class Persona():
    def __init__(self, nombre, edad,lugar):
        self.nombre=nombre
        self.edad=edad
        self.lugar=lugar
    
    def descripcion(self):
        print("Metodo descripcion en Clase Peronas")
        print("El nombre es ", self.nombre, ", tiene ", self.edad, "anyos", " y es de ", self.lugar)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_emp, edad_emp, lugar_epm):
        #! CON SUPER, DENTRO DEL CONSTRUCTOR, Solicita los atributos del constructor de Clase Padre
        #! Super esta dentro del constructor de esta clase y fijate que los 3 atributos que pide son los
        #! ultimos 3 : nombre_emp, edad_emp, lugar_epm, que ya estan en la clase Padre y en la asignacion no hay 
        #! que reescribir la asignacion
        #! por ejemplo: self.nombre_emp=nombre_emp, etc.....
        super().__init__(nombre_emp,edad_emp, lugar_epm)        
        self.salario=salario
        self.antiguedad=antiguedad
        
    def descripcion(self):
            #! LLAMA EL METODO descripcion(), usando super().descripcion  de la clase Padre y ademas le añadimos 
            #! salario y descripcion
            print("Metodo descripcion de clase Empleado: super().Descripcion + propia de ")
            super().descripcion()
            print("Salario: ", self.salario,", antiguedad: ", self.antiguedad)

#? Creamos una instancia de la clase Padre (Persona)
print("Instanciamos a Angel como clase Persona y lo hacemos con Angel, 43 y Malaga")
Angel=Persona("Angel", 43, "Malaga") 

print("Muestra la descripcion de Angel")                     
Angel.descripcion()
print("Creamos Empleado1, con datos salario, antiguedad, nombre, edad, lugar")
Empleado1=Empleado(2000, 2017, "Manolo", 33, "Madrid")
print("LLamamos a metodo descripcion de clase empleado")
Empleado1.descripcion()