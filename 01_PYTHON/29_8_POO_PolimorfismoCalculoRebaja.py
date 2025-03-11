'''
Polimorfismo
Si hablamos de herencia, tenemos que hablar de polimorfismo. Este término se refiere a la capacidad
de que todos los objetos pertenecientes a una misma familia de clases, es decir que heredan de la misma
clase, pueden ser llamados con los métodos de la clase padre que han sobrecargado, pero se
comportarán con las llamadas a sus propios métodos sobrecargados.
El polimorfismo es una propiedad de la herencia por la que objetos de distintas subclases pueden
responder a una misma acción.
El polimorfismo está implícito en Python, ya que todas las clases son subclases de una superclase
común llamada Object.

APLICACION DEL POLIMORFISMO EN EL SIGUIENTE EJEMPLO:

Clases Alimento y Ropa:
Ambas clases tienen un atributo pvp que representa el precio del producto. ( Publico )
El método __str__ se utiliza para obtener una representación de cadena legible del objeto.
Función rebajar_producto:
Esta función toma un objeto producto y un valor de rebaja como argumentos.
Accede al atributo pvp del objeto producto y aplica la rebaja.
No necesita verificar el tipo del objeto producto, ya que confía en que el objeto tiene el atributo pvp.
Ejemplo de Uso:
Creamos instancias de las clases Alimento y Ropa.
Llamamos a la función rebajar_producto con diferentes objetos y valores de rebaja.
El polimorfismo permite que la misma función funcione con objetos de diferentes clases.
Salida del código:

Alimento: Aceite de Oliva, Precio: 5.00 euros
Alimento: Aceite de Oliva, Precio: 4.50 euros
Ropa: Camiseta Algodón, Precio: 20.00 euros
Ropa: Camiseta Algodón, Precio: 16.00 euros
Puntos clave:

El polimorfismo permite que la función rebajar_producto funcione con objetos de diferentes clases.
La función no necesita conocer el tipo específico del objeto, solo que tiene el atributo pvp.
Esto hace que el código sea más flexible y reutilizable.

VER EXPLIACION MAS A DETALLE AL FINAL 

'''

class Alimento():
    def __init__(self, nombre, pvp):
        self.nombre = nombre
        self.pvp = pvp

    def __str__(self):
        return f"Alimento: {self.nombre}, Precio: {self.pvp:.2f} euros"

class Ropa():
    def __init__(self, marca, pvp):
        self.marca = marca
        self.pvp = pvp

    def __str__(self):
        return f"Ropa: {self.marca}, Precio: {self.pvp:.2f} euros"
    
#! Funcion independiente de las clases definidas    
def rebajar_producto(producto, rebaja):
    producto.pvp = producto.pvp - (producto.pvp / 100 * rebaja)    
    
aceite = Alimento("Aceite de Oliva", 5.0)
camiseta = Ropa("Camiseta Algodón", 20.0)

print(aceite)
rebajar_producto(aceite, 10)
print(aceite)

print(camiseta)
rebajar_producto(camiseta, 20)
print(camiseta)    

'''
Por ejemplo, con aceite.pvp:

Atributos públicos:
En las clases Alimento y Ropa, el atributo pvp se ha definido como público (sin guiones bajos al principio). Esto significa que es accesible desde 
cualquier parte del programa, incluyendo la función "rebajar_producto".
Por lo tanto, cuando llamas a "rebajar_producto(aceite, 10)", la función puede acceder y modificar directamente el atributo aceite.pvp.
Independencia de la función:
La función rebajar_producto es independiente de las clases Alimento y Ropa. No necesita conocer los detalles de implementación de estas clases.
Solo necesita que el objeto que se le pase como argumento tenga un atributo pvp que se pueda modificar.
Esta es la base del polimorfismo, el poder usar una función sin tener que conocer la clase exacta del objeto que se le pasa.

2. Método __str__:

Activación automática:
El método __str__ se activa automáticamente cuando intentas convertir un objeto a una cadena, como cuando lo pasas a la función print().
Python llama al método __str__ del objeto para obtener su representación en forma de cadena.
Si no se implementa el metodo __str__, al hacer print del objeto, se mostrará la dirección de memoria de ese objeto.
Representación legible:
El método __str__ te permite definir cómo se debe representar un objeto como cadena, lo que facilita la lectura y la depuración del código.

Puntos adicionales sobre el polimorfismo:
Flexibilidad y extensibilidad:
El polimorfismo hace que el código sea más flexible y fácil de extender.
Puedes agregar nuevas clases de productos sin tener que modificar la función rebajar_producto, siempre que las nuevas clases tengan el atributo pvp.

Interfaces implícitas:
En Python, el polimorfismo se basa en interfaces implícitas. No es necesario definir interfaces explícitas como en otros lenguajes.
Si un objeto tiene los atributos y métodos necesarios, se considera compatible con la interfaz.
Duck typing:
Este concepto es el que se usa en python, que dice que "Si camina como un pato y suena como un pato, entonces es un pato".
En el caso del codigo de ejemplo, la función "rebajar_producto" solo necesita que el objeto tenga el atributo pvp, sin importar la clase del objeto.

'''    