'''
POLIMORFISMO ....
Ejemplo basico, sin herencia.
Las clases Auto y Avion comparten un metodo con el mismo nombre: accion()
asi que al llamarlo, con instancias creadas de auto y avion, se ejecutara el 
metodo de cada clase.
'''


class Auto:
    def mover(self):
        return "El auto está conduciendo."

class Avion:
    def mover(self):
        return "El avión está volando."

def accion(objeto):
    print(objeto.mover())

auto = Auto()
avion = Avion()

accion(auto)   # Output: El auto está conduciendo.
accion(avion)  # Output: El avión está volando.