'''
POLIMORFISMO.
Ejemplo sonido animales.
Al final explicacion detallada del polimorfismo
'''

#Ejemplo 1
# Clase base
class Animal:
    def sonido(self):
        pass  # Método abstracto (sin implementación)

# Subclases que heredan de Animal
class Perro(Animal):
    def sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def sonido(self):
        return "¡Miau!"

class Vaca(Animal):
    def sonido(self):
        return "¡Muuu!"
    
# Crear objetos de diferentes clases
perro = Perro()
gato = Gato()
vaca = Vaca()

# Función que usa polimorfismo
def hacer_sonido(animal):
    print(animal.sonido())  # El método "sonido()" varía según la clase

# Llamar a la función con distintos objetos
hacer_sonido(perro)  # Output: ¡Guau!
hacer_sonido(gato)   # Output: ¡Miau!
hacer_sonido(vaca)   # Output: ¡Muuu!    

'''
Ejemplo sencillo de polimorfismo en Python. 
Qué significa polimorfismo?.
El polimorfismo permite que los objetos de diferentes clases sean tratados como objetos de una superclase común. Es uno de los 
cuatro principios principales de la programación orientada a objetos, junto con la encapsulación, la herencia y la abstracción.

Ver cómo diferentes clases pueden tener un método con el mismo nombre pero diferentes implementaciones. El ejemplo clásico es usar 
una superclase con un método que las subclases anulan.

Usar animales que hacen sonidos: 
Una clase base Animal con un método hacer_sonido(), y luego subclases como Dog y Cat que anulan hacer_sonido() con sus propias 
implementaciones.
En Python, puedes tener diferentes clases que no están relacionadas por herencia pero que aún tienen el mismo nombre de método. 
Por ejemplo, una clase de Auto y una clase de Bicicleta que tienen un método move(). Luego, puedes llamar a move() en instancias 
de ambas, demostrando que, aunque son clases diferentes, se pueden usar indistintamente en el código que espera el método move().

El ejemplo de la herencia es mejor para ilustrar el polimorfismo. 
Primero, cree una clase base con un método. Luego, las clases derivadas anulan ese método. Luego, cree instancias de cada una e 
invoque el método a través de una referencia a la clase base. De esa manera, la misma llamada al método da como resultado diferentes 
comportamientos.

En Python no necesitas necesariamente la herencia para el polimorfismo. El tipado de pato permite que se use cualquier objeto siempre 
que tenga el método requerido. Entonces, tal vez un ejemplo más Pythonico sería tener clases no relacionadas con el mismo nombre de 
método y mostrar cómo se pueden usar indistintamente.

clase Perro: def hacer_sonido((self): return "¡Guau!"
clase Gato: def hacer_sonido(self): return "¡Miau!"

Luego, creamos una lista de instancias de Dog y Cat, recorre cada una de ellas y llama a hacer_sonido(). Aunque son clases diferentes, 
el método hacer_sonido() funciona. Eso es polimorfismo a través de tipado de pato. ( Hace ruido de pato y camina como pato entonces es 
un pato = filosofia de Python)

Es un buen ejemplo. Muestra que, siempre que los objetos tengan el método hacer_sonido(), se los puede tratar de la misma manera. 
Es posible que el usuario no esté familiarizado con el tipado de pato, por lo que explicarlo podría ser útil.

Otra opción es usar la herencia: una clase base Animal con un método hacer_sonido() y subclases Dog y Cat que lo reemplazan. Luego, 
puedes tener una función que tome un Animal y llame a hacer_sonido(). Ese es un polimorfismo más tradicional.

¿Qué ejemplo es mejor? El usuario pidió uno sencillo. El ejemplo de tipificación de pato es más sencillo porque no requiere herencia. 
Vamos con eso. Déjame escribirlo.

Permítame incluir ambos ejemplos. Primero, el ejemplo de tipificación de pato, luego el basado en herencia. De esa manera, el usuario 
obtiene una comprensión más amplia.
Además, es necesario explicar qué es el polimorfismo en términos simples. Por lo tanto, comience con una definición y luego muestre 
ejemplos de código.


Definir polimorfismo.
Ejemplo 1: Tipificación de pato con diferentes clases que tienen el mismo método.
Ejemplo 2: Uso de herencia con una clase base y métodos anulados.
Explicación de cómo ambos ejemplos demuestran polimorfismo.
Asegúrate de que el código sea simple y claro. Utiliza comentarios para explicar cada parte.


'''