# El bucle for
# Ejecuta el print dos veces
print()
print("Bucle for, for i in [1,10]: Imprimira Hola 2 veces")
for i in [1,10]:
    print("Hola")

print()
print("Imprimira las 4 esciones del año")    
# Imprime el contenido del diccionario
for estacion in ["primavera", "verano", "otoño", "invierno"]:
    print(estacion)

# Es lo mismo que el ejemplo anterior pero con una lista
print()
print("Imprime las 4 escaiones del año con una lista") 
estaciones =["primavera", "verano", "otoño", "invierno"]
for estacion in estaciones:
    print(estacion)    

# Repite el print tantas veces como caracteres hay en el string
print()
print("Repite el print tantas veces como caracteres hay en el string, es decir, 6 veces")
# Evaluamos si un mail contiene el caracter @
for i in "frase":
    print("Hola", "letra de palabra frase:", i)

print()
print("Verifica si un emal tiene el @")    
miEmail=input("Introduce email")
email=False
for i in miEmail:
    if i=="@":
        email=True
if email==True: #Se puede simplificar if email:
    print("El email es correcto")
else:
    print("EL mail no es correcto")
# Podemos unir valores de texto con valores de variable a la hora de imprimir:
for i in range(5):
    print(f"Valor de la variable, range(5) {i}")
for i in range(5,10):
    print(f"Valor de la variable range (5 a 19) {i}")
# Podemos poner un tercer argumento con el que especificamos de cuanto en cuanto va el conteo:
for i in range(5,10,2):
    print(f"Valor de la variable, de 5 a 10, saltando de 2 en 2. {i}")
# validar un mail en función de si tiene @ simplemente recorriendo la logitud del string:
valido=False
email=input("Introduce tu email: ")
for i in range(len(email)):
    if email[i]=="@":
        valido=True
if valido:
    print(f"Email, {valido}, correcto")
else:
    print(f"Email,{valido},  incorrecto")
# Las cadenas son objetos iterables, contienen una secuencia de caracteres:
for x in "banana":
    print(x)
# Con la instrucción break podemos detener el ciclo antes de que haya pasado
# por todos los elementos:
# Salga del bucle cuando x es "banana"
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    print(x)
    if x == "banana":
        break
        # Salga del bucle cuando x es "banana", pero esta vez el corte se produce antes
        # de la impresión:

frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    if x == "banana":
        break
    print(x)

# Con la instrucción continue podemos detener la iteración actual del ciclo y
# continuar con la siguiente:
# En este caso no me imprimiría
"banana"
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    if x == "banana":
        continue
    print(x)

# Para recorrer un conjunto de código un número específico de veces, podemos
# usar la función range ()
for x in range(6):
    print(x)
# Función range con parámetro de inicio incrementado por defecto en 1.
for x in range(2, 6):
    print(x)
# Función range con parámetro de inicio incrementado en 3.
for x in range(2, 30, 3):
    print(x)
# Bucle for anidado
# Imprime cada color para cada fruta:
color = ["verde", "amarilla", "roja"]
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    for y in color:
        print(x, y)
# Los bucles for no pueden estar vacíos. 
# Si por alguna razón tenemos un bucle for sin contenido, usaremos la
# instrucción pass para evitar un error.
for x in [0, 1, 2]:
    pass