'''
EJERCICIO DE POLIMORFISMO: CALCULO DE AREA DE CIRCULO, CUADRADO Y TRIANGULO.

El truco es aplicar  area = forma.calcular_area() 
    donde:
          forma: Se sustituye por el nombre de las clases ( circulo, cuadrado, triangulo)
          calcular_area(): El metodo tiene el mismo nombre en las 3 clases.
          
AL FINAL UNA EXTENSION DE LA EXPLICACION.           
'''

import math

class Circulo:
    def __init__(self, radio, nombre="Circulo"):
        self.radio = radio
        self.nombre=nombre                           # Para asignar el nombre en calcular_area
        
    def calcular_area(self):                         #! Mismo nombre del metodo en las 3 clases
        return math.pi * self.radio ** 2

class Cuadrado:
    def __init__(self, lado, nombre="Cuadrado"):
        self.lado = lado
        self.nombre=nombre                           # Para asignar el nombre en calcular_area

    def calcular_area(self):                         #! Mismo nombre del metodo en las 3 clases
        return self.lado ** 2

class Triangulo:
    def __init__(self, base, altura, nombre="Triangulo"):
        self.base = base
        self.altura = altura
        self.nombre=nombre                           # Para asignar el nombre en calcular_area

    def calcular_area(self):                         #! Mismo nombre del metodo en las 3 clases
        return 0.5 * self.base * self.altura
    
#? ---------FUNCION CALCULO DE AREA ------------------------------------------------
def calcular_areas(formas):
    for forma in formas:                             #* Recorrer la lista de formas
        area = forma.calcular_area()                 #! Mismo nombre del metodo en las 3 clases
        print(f"El área de {forma.nombre} es: {area:.2f}")
#       print(f"El área de la forma es: {area:.2f}") #* imprime area
#?----------------------------------------------------------------------------------

#?------INSTANCIAMOS CLASE CIRCULO, CUADRADO, TRIANGULO------------------------------
circulo = Circulo(5)                        #* radio = 5
cuadrado = Cuadrado(4)                      #* lado  = 4
triangulo = Triangulo(3, 6)                 #* base y altura = 3 y 6

#?----CREAMOS UNA LISTA DE LAS CLASES INSTANCIADAS PARA HACER CALCULO EN SERIE-------
formas = [circulo, cuadrado, triangulo]  

#?------LLAMAMOS FUNCION Calcular_areas(formas)-------------------------------------
calcular_areas(formas)        

'''
Clases de Formas:
Cada clase representa una forma geométrica diferente (círculo, cuadrado, triángulo).
Cada clase tiene un método calcular_area() que calcula el área de la forma correspondiente.

Función calcular_areas:
Esta función toma una lista de objetos formas como argumento.(círculo, cuadrado, triángulo)
Itera sobre la lista y llama al método calcular_area() de cada objeto.
No necesita conocer el tipo específico de cada objeto, solo que tiene un método calcular_area().
Ejemplo de Uso:
Creamos instancias de las clases Circulo, Cuadrado y Triangulo.
Creamos una lista formas que contiene las instancias de las diferentes formas.
Llamamos a la función calcular_areas con la lista formas.

El polimorfismo permite que la función calcular_areas funcione con objetos de diferentes clases.
La función no necesita conocer el tipo específico de cada objeto, solo que tiene el método calcular_area().
Esto hace que el código sea más flexible y reutilizable.
En este ejemplo, el polimorfismo se manifiesta en el hecho de que la función calcular_areas puede tratar 
objetos de diferentes clases de la misma manera, siempre que tengan el método calcular_area().
'''