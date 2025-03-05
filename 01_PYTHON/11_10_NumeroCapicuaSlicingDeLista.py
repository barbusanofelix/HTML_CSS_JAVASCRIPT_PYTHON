'''
Capicua es un numero que se lee igual al derecho que al reves...
Por su puesto los digigitos son capicua pero por ejemplo : 123321 , o mas facil 121 se leerian igual.

Para resolverlo muy resumido se usa:
Slicing de cadenas en Python

El slicing (rebanado) de cadenas en Python es una técnica poderosa que te permite extraer porciones de una cadena especificando un 
rango de índices. La sintaxis general del slicing es:

cadena[inicio:fin:paso]

Donde:

inicio: El índice donde comienza la porción (inclusivo). Si se omite, se asume que es el inicio de la cadena.
fin: El índice donde termina la porción (exclusivo). Si se omite, se asume que es el final de la cadena.
paso: El tamaño del paso o incremento entre los índices. Si se omite, se asume que es 1.
Explicación de [::-1]

En el caso de [::-1], estamos utilizando los valores predeterminados de inicio y fin, pero especificando un paso de -1. Esto significa:

inicio omitido: Se comienza desde el final de la cadena.
fin omitido: Se llega hasta el principio de la cadena.
paso -1: Se recorre la cadena en orden inverso, tomando cada carácter de derecha a izquierda.
Ejemplo paso a paso:

Supongamos que tenemos la cadena "Hola". Veamos cómo funciona [::-1]:

Se comienza desde el final de la cadena: "a".
Se toma el carácter "a".
Se mueve un paso hacia la izquierda: "l".
Se toma el carácter "l".
Se mueve un paso hacia la izquierda: "o".
Se toma el carácter "o".
Se mueve un paso hacia la izquierda: "H".
Se toma el carácter "H".
El resultado es la cadena invertida: "aloH".

Aplicación en el código:

En el código que mencionaste, numero_str[::-1] se utiliza para invertir los dígitos de un número que ha sido convertido a una cadena. Por ejemplo:

Si numero_str es "123", entonces numero_str[::-1] será "321".
En resumen:

[::-1] es una forma concisa y eficiente de invertir una cadena en Python.
Utiliza el slicing de cadenas con un paso negativo para recorrer la cadena en orden inverso.
'''
print()
numero= int(input("Escrinbe un numero para ver si es CAPICUA ( se lee igual der-iz-der):"))

numero=str(numero)                  # convertimos a numero de caracteres para tratarlo como string y poderlo invertir
numeroInverso=numero[::-1]
print()
if numero==numeroInverso:
    print(f"El numero {numero} es igual a su inverso {numeroInverso} asi que es CAPICUA")
else:
    print(f"El numero {numero} NO es igual a su inverso {numeroInverso}, NO es Capicua")    
print()

