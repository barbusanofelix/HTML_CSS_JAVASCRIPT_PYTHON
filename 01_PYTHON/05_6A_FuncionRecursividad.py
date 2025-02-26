
def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1

# Esta la hice para ver el acumulado   paso a paso.
# Mas abajo se explica la recursividad de la funcion factorial(x) 
def factorialAcumulado(x, acumulador=1): # Truco: Recibe acumulado como parametro iniciado en 1
    print(f"x: {x}, acumulador: {acumulador}")  # Imprime los valores en cada llamada
    if x <= 1:
        return acumulador
    else:
        return factorialAcumulado(x - 1, acumulador * x) # Pasa el acumulador   
 
fact= factorial(5)
factAcum= factorialAcumulado(5)
print("Factorial de 5 :", fact)
print("Factoria de 5, viendo acumulado:",factAcum)
'''
EXPLICACION DE LA RECURSIVADAD
1. Llamada inicial: factorial(5)

Se llama a la función con x = 5.
Como 5 > 1, se ejecuta el primer return: 5 * factorial(4).
En este punto, la función no termina. En su lugar, se "suspende" temporalmente, esperando el resultado de factorial(4).
2. Llamadas recursivas:

factorial(4): 4 * factorial(3) (se suspende).
factorial(3): 3 * factorial(2) (se suspende).
factorial(2): 2 * factorial(1) (se suspende).
3. Caso base: factorial(1)

Se llama a la función con x = 1.
Como 1 no es mayor que 1, se ejecuta el else, y la función devuelve 1.
Aquí es donde la recursión comienza a "desenrollarse".
4. Desenrollado de la recursión:

factorial(2) recibe el valor 1 de factorial(1) y calcula 2 * 1 = 2. Devuelve 2.
factorial(3) recibe el valor 2 de factorial(2) y calcula 3 * 2 = 6. Devuelve 6.
factorial(4) recibe el valor 6 de factorial(3) y calcula 4 * 6 = 24. Devuelve 24.
factorial(5) recibe el valor 24 de factorial(4) y calcula 5 * 24 = 120. Devuelve 120.
Por qué no termina siempre en return 1:

El return 1 solo se ejecuta cuando x es 1 o menor.
Antes de llegar a ese punto, la función se llama a sí misma repetidamente, creando una "pila" de llamadas.
Cada llamada suspendida espera el resultado de la siguiente llamada.
Solo cuando se alcanza el caso base (x = 1), los resultados comienzan a propagarse hacia arriba a través de la pila, realizando las multiplicaciones acumuladas.
En resumen:

La recursión implica llamadas a funciones que se suspenden hasta que se alcanza un caso base.
El caso base (el return 1) proporciona el punto de partida para que los resultados se propaguen hacia atrás.
Cada llamada suspendida realiza su parte del cálculo a medida que los resultados regresan.
'''