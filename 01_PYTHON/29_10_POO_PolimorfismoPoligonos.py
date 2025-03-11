
class Poligono:
    def __init__(self, lados, color=None):
        self.lados = lados
        self.color = color

    def show(self):
        print(f"Polígono de {self.lados} lados, color: {self.color}")

class Triangulo(Poligono):
    def __init__(self, base, altura, color=None):
        Poligono.__init__(self, 3, color)
        self.base = base
        self.altura = altura

    def show(self):
        super().show()
        print(f"Base: {self.base}, Altura: {self.altura}")

class Cuadrado(Poligono):
    def __init__(self, lado, color=None):
        Poligono.__init__(self, 4, color)
        self.lado = lado

    def show(self):
        super().show()
        print(f"Lado: {self.lado}")

# Declaramos instancias de Triangulo y Cuadrado
t1 = Triangulo(5, 4, 'rojo')
t2 = Triangulo(3, 6, 'azul')
c1 = Cuadrado(2, 'verde')

# Tupla con dos Triangulo y un Cuadrado
poligonos = t1, t2, c1

# Recorremos la tupla y llamamos al método show de cada elemento
for poligono in poligonos:
    poligono.show()
    print()  # Imprimimos una línea en blanco para separar los polígonos
    
    
'''
Clase Poligono:
Esta es la clase base que representa un polígono genérico.
El constructor __init__ inicializa los atributos lados y color.
El método show imprime información básica sobre el polígono.

Clase Triangulo:
Esta clase hereda de Poligono y representa un triángulo.
El constructor __init__ llama al constructor de la clase base (Poligono.__init__) para inicializar
los atributos heredados y luego inicializa los atributos específicos del triángulo (base y altura).
El método show llama al método show de la clase base (super().show()) para imprimir la información
del polígono y luego imprime la información específica del triángulo.

Clase Cuadrado:
Esta clase hereda de Poligono y representa un cuadrado.
El constructor __init__ llama al constructor de la clase base y luego inicializa el atributo específico
del cuadrado (lado).
El método show llama al método show de la clase base y luego imprime la información específica del cuadrado.

Ejemplo de uso:
Se crean instancias de las clases Triangulo y Cuadrado.
Se crea una tupla poligonos que contiene las instancias de los polígonos.
Se recorre la tupla y se llama al método show de cada polígono.

Puntos clave:
Herencia: Las clases Triangulo y Cuadrado heredan de la clase Poligono.
Polimorfismo: La función for poligono in poligonos: puede tratar objetos de diferentes clases de la misma 
manera, ya que todos tienen el método show.
super(): La función super() se utiliza para llamar a métodos de la clase base.
Con este código completo, puedes ejecutar el ejemplo y ver cómo el polimorfismo permite que el mismo método
show se comporte de manera diferente según el tipo de polígono.

'''