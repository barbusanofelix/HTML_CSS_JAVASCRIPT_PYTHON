# WHILE
# Imprime edad cuando el contador llegue a 18
edad = 0
print("Imprime la edad hasta 18 años")
while edad < 18:
    edad=edad+1
    print("Tienes "+str(edad))

# Pregunta la edad mientras sea negativa
print()
print("pedira la edad mientras sea negativa:")
edad=int(input("Introduce edad: "))
while edad<0:
    print("Edad incorrecta")
    edad=int(input("Introduce edad: "))
print("tu edad es: "+str(edad))

# Calcula la raiz cuadrada de un número. Tenemos tres intentos y el número no puede ser negativo.
print()
print("Adivina la raiz cuadrada entera de un numero")
import math


while True:  # Controla que el num sea >0
    try:
        numero = float(input("Introduce un número positivo: "))
        if numero >= 0:
            break
        else:
            print("Por favor, introduce un número positivo.")
    except ValueError:
        print("Entrada inválida. Introduce un número >0 o un numero")

raiz_cuadrada = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es aproximadamente {raiz_cuadrada:.2f}")

for intento in range(3):
    try:
        intento_usuario = float(input(f"Intento {intento + 1}: Adivina la raíz cuadrada: "))
        if abs(intento_usuario - raiz_cuadrada) < 0.5:  # Que el valor absoluto de la raiz sea +/- 0,5
            # Muestra la resta y la raiz cuadrada con 2 decimales

            print(f"¡Correcto!, {intento_usuario} vs {raiz_cuadrada:.2f} es = {abs(intento_usuario-raiz_cuadrada):.2f} <0.50 : ")
            break  # Salir del bucle de intentos si acierta
        else:
            print("Incorrecto. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada inválida. Introduce un número.")
else: #El else se ejecuta si el bucle for termina sin un break.
    print(f"Fallaste. La raíz cuadrada era {raiz_cuadrada:.2f}")
# Bucle while con un if anidado y un break
# Salga del bucle cuando num sea 3:
print("Ejemplo de un while que cuanta de 1 a 5 pero se sale en 3 con break")
num = 1
while num < 6:
    print("El numero es :",num)
    if num == 3:
        print("Numero es 3 y aqui lo saca")
        break
    num += 1
