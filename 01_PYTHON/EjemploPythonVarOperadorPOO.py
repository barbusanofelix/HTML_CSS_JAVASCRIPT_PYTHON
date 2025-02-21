# Variables
edad = 30
altura = 1.85
nombre = "Juan"

# Operadores
suma = edad + 10
mayor_de_edad = edad >= 18
print("edad ="+str(edad))
print("suma ="+str(suma))
print("mayor_de_edad:"+str(mayor_de_edad))

# Condicionales
if mayor_de_edad:
  print(nombre + " es mayor de edad.")
else:
  print(nombre + " no es mayor de edad.")

# Bucles
for i in range(5):
  print("Contador:", i)

# POO
class Persona:
  def __init__(self, nombre, edad):        # __init__ es el constructor.
                                           # self como el nombre estándar para el primer parámetro de los métodos de instancia (incluido el constructor)
    self.nombre = nombre
    self.edad = edad

  def saludar(self):
    print("Hola, mi nombre es " + self.nombre + " y tengo " + str(self.edad) + " años.")

persona1 = Persona("Ana", 25)
persona1.saludar()
