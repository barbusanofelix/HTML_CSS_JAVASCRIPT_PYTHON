''' VEREMOS USO DE SUM Y NEXT EN PYTHON'''

''' SUM
    Recibe un iterable, por ejemplo una lista
'''

lista= [1.3,2,3,4.3,5]      # lista por estar entre corchete []

suma=sum(lista)        # sumara los elementos sumables en la lista, es decir, los numeros. Sino son numeros int o float dara un error

print(f"El resultado de sumar los elmentos en nuestra {lista} es {suma}")  

'''USO DE SUM CON UNA VALOR INICIAL A SUMAR'''
'''PARA ELLO SIMPLEMENTE COLOCAMOS EL VALOR INICIAL COMO UN 2DO PARAMETRO'''

valor_inicial=10.0
suma_con_inicial = sum(lista, valor_inicial)

print(f"El resultado de sumar los elmentos en nuestra {lista} con valor inicial {valor_inicial} es: {suma_con_inicial}")  

'''FUNCION NEXT '''

'''LA FUNCION NEXT SE USA PARA PASAR AL SIGUIENTE ITERADOR '''

#? PASO 1: CREAMOS UN ITERADOR PARA DEL ELMENTO QUE ES ITERABLE USANTO EL METODO ITER()

lista= [1.3,2,3,4.3,5]  
iterador = iter(lista)

print(iterador)     # esto dara una salida de la direccion de memoria y no veremos el 

for i in iterador:
    print("El iterado es : ", i)  # devolvera cada elemetno del iterador
    
# print(f"Obtenemos un elmentos adicionales {next(iterador)}")     # Aqui devolvera error " StopIteracion" porque llego al final de iterador

"""CREAMOS UN ITERADOR PERSONALIZADO QUE PUEDE RETROCEDER PARA RECORRER UNA LISTA QUE SE INICIALIZA EN EL CONSTRUCTOR"""
class IteradorConRetroceso:
    def __init__(self, data):
        self.data = list(data)  # Asegurarse de que sea una lista para indexar. data pasa a ser la lista
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

    def retroceder(self):
        if self.index > 0:
            self.index -= 1

lista = [1.3, 2, 3, 4.3, 5]
mi_iterador = IteradorConRetroceso(lista)

print(next(mi_iterador))  # 1.3
print(next(mi_iterador))  # 2
mi_iterador.retroceder()
print(next(mi_iterador))  # 2 (otra vez, ya que retrocedimos)
mi_iterador.retroceder()
mi_iterador.retroceder() # Ahora el índice es -1
# El siguiente next() devolverá el primer elemento
print(next(mi_iterador)) # 1.3
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
mi_iterador.retroceder()  # Aqui retrocedio para no solicitar un valor del indice fuera del rango.
print(next(mi_iterador))