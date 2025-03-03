
# -------------------------------------
# FUNCIONES
# -------------------------------------
# Definición de una función. Importante la identación:

def my_funcion():
    print("1. Estamos ejecutando la función, que solo imprime.")

# Llamada a la función. En otra parte de mi código, llamamos a la función para que se ejecute:
my_funcion()
# -------------------------------------
def suma():
    num1 = 3
    num2 = 5
    print("2. suma 3 +5, imprime dentro de la funcion=", num1+num2)

suma()
# Otra opción:
def suma():
    num1 = 3
    num2 = 5
    resultado = num1 + num2
    return resultado

print("3, LLama a suma y devuelve la suma de 8",suma())
# -------------------------------------
#El bloque de código que ejecutará la función incluye todas las declaraciones con indentación
# dentro de la función.
def miFunción():
    print('4. this will print')
    print('5. so will this')
    print("Demuestra que sin la indentacion correct< no se ejecuta el codigo...hay una x=7")
x = 7
# la asignación de x no es parte de la función ya que no está indentada
#---------------------------------------
#Las variables definidas dentro de una función solo existen dentro del ámbito de esa función.
def duplica(num):
    x = num * 2
    return x
print("6. Tal vez imprima el x=7 de lineas anteriores ",x) # error - x no está definida
print("7. Muestra 8 porque se paso 4 a la funcion",duplica(4)) # muestra 8
#---------------------------------------
#Si la definición de una función incluye parámetros, debe proporcionar el mismo número
# de parámetros cuando llame a la función.
def multiplica(arg1, arg2):
    return arg1 * arg2
#print(multiplica(3)) # TypeError: multiplica() utiliza exactamente 2 argumentos (0 proporcionados)
print("8. Multiplica la a x 5 =", multiplica('a', 5)) # 'aaaaa' mostrado en la consola
#print(multiplica('a', 'b')) #TypeError: Python no puede multiplicar dos strings
#---------------------------------------
#Puedes pasar los parámetros en el orden que desees, utilizando el nombre del parámetro.
def suma(a, b):
    return a + b
result = suma(b=2, a=3)
print("9.Debe retornar  ( 2 + 3 ) =5 ",result)
# result = 4
#---------------------------------------
#También podríamos pasar varios valores que retornar a return.
def f(x, y):
    return x * 2, y * 2
a, b = f(1, 2)
print("10. Retorna 2 y 4 ", a,b)
""" Sin embargo, esto no quiere decir que las funciones Python puedan de-volver varios valores,
lo que ocurre en realidad es que Python crea una tupla al vuelo cuyos elementos son los valores a 
retornar, y esta única variable es la que se devuelve."""
# -------------------------------------
# función con un parámetro
# -------------------------------------
# Declaración de una función
def miFuncion(num1, num2):
    return(num1+num2)
# Llamada a la función
print("11. 2+3 = 5 =",miFuncion(2, 3))
# -------------------------------------
def holaConNombre(name):
    print("12.Devolvera Hola Angel!", end=" ")
    print("Hola " + name + "!")

 # llamada a la función, 'Hola Angel!' se muestra en la consola
# -------------------------------------
#---------------------------------------
# Funcion con parametro por defecto
#---------------------------------------
def imprimir(precio, iva = 1.21):
    print("13. Imprime precio x iva que debe ser 500X.10=550 =",precio * iva)

# la llama desde aqui     
imprimir(500,1.10)
# Funciones con argumentos variables
# Me crea una tupla de nombre "otros"
"""
Llamadas a la función def varios(param1, param2, *otros):  MULTIPLES ARGUMENTOS

varios(1, 2):
param1 se asigna a 1.
param2 se asigna a 2.
No hay argumentos adicionales, por lo que otros es una tupla vacía ().
El bucle for no se ejecuta, ya que otros está vacío.
No se imprime nada.
varios(1, 2, 3):
param1 se asigna a 1.
param2 se asigna a 2.
El argumento adicional 3 se empaqueta en la tupla otros, que se convierte en (3,).
El bucle for se ejecuta una vez, imprimiendo:
3
varios(1, 2, 3, 4):
param1 se asigna a 1.
param2 se asigna a 2.
Los argumentos adicionales 3 y 4 se empaquetan en la tupla otros, que se convierte en (3, 4).
El bucle for se ejecuta dos veces, imprimiendo:
3
4
Resumen de la salida

La salida total del código será:

3
3
4
En resumen, la funcion imprime los valores que se pasen a la funcion, a partir del tercer parametro.

"""
def varios(param1, param2, *otros):
    for val in otros:
        print (val)

print("14. Devolvera 3, 3, 4 ...la funcion no hace nada con param1 y param2 y solo *otros asi que imprime los valores en 3ero y 4to lugar")        

varios(1, 2)
varios(1, 2, 3)
varios(1, 2, 3, 4)
"""
También se puede preceder el nombre del último parámetro con **, en cuyo caso en lugar de una tupla se
utilizaría un diccionario.
Las claves de este diccionario serían los nombres de los parámetros indicados al llamar a la función y los
valores del diccionario, los valores asociados a estos parámetros.
"""
def varios(param1, param2, **otros):
    for i in otros.items():
        print (i)

varios(1, 2, tercero = 3)
# ---------------------------
#---------------------------------------
#ARGUMENTOS VARIABLES EN FUNCIONES. EL ARGUMENTO CON * SERÁ UNA TUPLA
# PYTHON NO TIENE SOBRECARGA DE FUNCIONES
#---------------------------------------
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

print("15 y 16 llaman a una funcion de impresion para que imprima arreglos de diferentes tamaños")
listarNombres('Juan', 'Karla', 'María', 'Ernesto')
print("15. Deberia imprimir 'Juan', 'Karla', 'María', 'Ernesto')")
listarNombres('Laura', 'Carlos')
print("16. Imprimira a Laura', 'Carlos")
#---------------------------------------
# hACER LO MISMO PERO PASANDO DICCIONARIOS COMO ARGUMENTOS. KWARGS
"""
Función listarTerminos(**KWARGS)

**KWARGS:
Este es un parámetro especial llamado "parámetro de longitud variable de palabras clave" (o "argumentos de palabras clave variables"). Permite que la función 
acepte un número arbitrario de argumentos de palabras clave (argumentos con nombre). Todos los argumentos de palabras clave se empaquetan en un diccionario 
llamado KWARGS.
for clave, valor in KWARGS.items()::
Este bucle for itera sobre los pares clave-valor del diccionario KWARGS. KWARGS.items() devuelve una vista de los pares clave-valor del diccionario.
En cada iteración, clave toma el valor de la clave y valor toma el valor correspondiente. print(f'{clave}: {valor}'):
Esta línea imprime la clave y el valor en el formato "clave: valor". Las f-strings permiten insertar variables directamente en las cadenas de texto.
Llamadas a la función

listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key'): Los argumentos de palabras clave IDE='Integrated Developement Environment' 
y PK='Primary Key' se empaquetan en el diccionario KWARGS.
KWARGS se convierte en {'IDE': 'Integrated Developement Environment', 'PK': 'Primary Key'}. El bucle for itera dos veces:
Primera iteración: clave es 'IDE', valor es 'Integrated Developement Environment'.
Segunda iteración: clave es 'PK', valor es 'Primary Key'.
La salida es:
IDE: Integrated Developement Environment
PK: Primary Key
listarTerminos(DBMS='Database Management System'): El argumento de palabra clave DBMS='Database Management System' se empaqueta en el diccionario KWARGS.
KWARGS se convierte en {'DBMS': 'Database Management System'}.
El bucle for itera una vez: Primera iteración: clave es 'DBMS', valor es 'Database Management System'. La salida es:
DBMS: Database Management System
En resumen
La función listarTerminos toma un número arbitrario de argumentos de palabras clave, los empaqueta en un diccionario y luego imprime cada par clave-valor 
del diccionario. Esto es muy útil para pasar configuraciones o datos con nombre a una función.
"""
def listarTerminos(**KWARGS):
    for clave, valor in KWARGS.items():
        print(f'{clave}: {valor}')

print("17: ")
listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
print("18:")
listarTerminos(DBMS='Database Management System')
#---------------------------------------
def mi_funcion(nombre, apellido):
    print('18 y 19 .saludos desde mi función')
    print(f'Nombre: {nombre}, Apellido:{apellido}')

 # Sería como imprimir así: print('Nombre:', nombre, 'Apellido:',apellido)
mi_funcion('Juan', 'Perez')
mi_funcion('Karla','Lara')
#---------------------------------------
# RETURN
#---------------------------------------
#function definiciones de function no pueden estar vacías, pero si por alguna razón tiene
# una definición de function sin contenido, ingrese la instrucción pass para evitar un error.
def myfunction():
    pass
#---------------------------------------
print("20. Al llamar a myfunction NO pasa nada porque el cuerpo tiene solo pass ", myfunction)

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f'21. Resultado sumar 5 + 3, usando variableresultado = sumar(5, 3) : {resultado}')
# print(f'Resultado sumar: {sumar(5,3}')
#También podíamos haber llamado a la función dentro de nuestro método print
print(f'22. Igual que anterior pero lalmado directo desde metodo print "sumar(5,3)"Resultado sumar: {sumar(5,3)}')
# ---------------------------
# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
    return val1 * val2

print("23. Multplicar multiplica(3, 5)= muestra 15 en la consola", multiplica(3,5))
#---------------------------------------
# esta es una función básica de suma
def suma(a, b):
    return a + b
result = suma(1, 2)
print("24. Suma de 1 + 2 =",result)
# result = 3
#---------------------------------------
# VALORES POR DEFECTO
#---------------------------------------
# esta es una función básica de suma con balores predeterminados
def suma(a, b=3):
    return a + b
result = suma(1)
print("25. Suma 1 + 3 por defecto= 4 :",result)
# result = 4
#---------------------------------------
# Indicio de qué tipo de dato vamos a manejar:
#---------------------------------------
def sumar(a:int = 0, b:int = 0) -> int:
#def sumar(a = 0, b = 0):
    return a + b
resultado = sumar()
#print(f'Resultado sumar: {resultado}')
print("Funcion con tipo de datos, INT pero acepta Strings,  y parametros por defecto")
print(f'26. Resultado sumar: {sumar(45,654)}')
#uanque le hemos dicho el tipo de los parámetros no estamos obligados a cumplirlo.
print(f'27. Aqui la misma anterior pero con strings, Resultado sumar: {sumar("aNGEL","Garcia")}')
#---------------------------------------
"""
Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables *args
como parámetro de la función y regresar como resultado la suma de todos los valores pasados como argumentos.
"""
# Definimos nuestra funcion para sumar valores
def sumar_valores(*args):
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
    # resultado = resultado + valor
        resultado += valor
    return resultado
# Llamada a la funcion
print("28. Funcion de suma multivalores ...Todos los que quieras:", sumar_valores(3, 5, 9, 4, 6, 45,444))
#---------------------------------------
# Distintos tipos de datos como argumentos en Python
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

print("29. Funcion para desplegar numeros o nombres ....se le pasa el set , lo recorre y los imprime. ")        
#nombres = ['Juan', 'Karla', 'Guillermo']
#desplegarNombres(nombres)
#desplegarNombres('Carlos')
#desplegarNombres((8, 9))
print("29A Desplaegando 2 numeros 10 y 11 :")
desplegarNombres([10, 11])
print("Desplegando 3 nombres, Felix Lucy y Carlos: ")
desplegarNombres(["Felix", "Lucy", "Carlos"])
#---------------------------------------
# FUNCIONES RECURSIVAS
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
numero = 6
resultado = factorial(numero)
print(f'30. Funcion recursivas : El factorial de {numero} es {resultado}')
#---------------------------------------
"""
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas. Puede ser cualquier valor positivo,
ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1
En caso de pasar el valor de 3, debe imprimir:
3
2
1
Si se pasan valores negativos no imprime nada
"""
def imprimir_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivo(numero- 1)
    elif numero == 0:
        return
    elif numero < 0:
        print('Valor incorrecto...')

print("31. Funcion recursiva imprimeinedo numero descendiente, 5-4-3-2-1")
imprimir_numero_recursivo(5)
#---------------------------------------
def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print (numero)
        cuenta_regresiva(numero)
    else:
        print ("Boooooooom!")
        print ("Fin de la función"),numero

print("32.- Cuenta regresiva aplicando recursividad, de 20 a 1 ")        
cuenta_regresiva(20)
#---------------------------------------
"""
Ejercicio: Calculadora de Impuestos Crear una función para calcular el total de un pago incluyendo un impuesto
aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""

# Funcion que calcula el total de un pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto,impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total
# Ejecutamos la funcion
pago_sin_impuesto = float(input('Proporcione el pago sin impuestos: '))
impuesto = float(input('Proporcione el monto del impuesto:'))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'33. Pago con impuesto:{pago_con_impuesto}')
#---------------------------------------
#---------------------------------------
"""
Ejercicio: Convertidor de Temperatura Realizar dos funciones para convertir de
grados celsius a fahrenheit y viceversa.
"""
# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
# Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
# Realizamos algunas pruebas de conversion
celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
# Imprimimos el resultado
print(f'{celsius} C a F:{resultado:.2f}')
# Realizamos la prueba de grados fahrenheit a celsius 
fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
# Imprimimos el resultado
print(f'{fahrenheit} F a C:{resultado:0.2f}')