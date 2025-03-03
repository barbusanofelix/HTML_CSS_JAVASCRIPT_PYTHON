# Programa que pide una nota por
'''
Programa que pide la nota de un alumno por consola y valora si el alumno ha aprobado
o no.
'''

notaIn=int(input("Introduzca nota:"))

if notaIn<5:
    calificacion="Suspendido"
else: calificacion="Aprobado"

print("El alumno esta :", calificacion)
print()
# IF no sólo evalúa un boleano, también si una variable contiene información
variable = 19

if variable:
    print(f"La variable contiene información : {variable}")
else:
    print("No contiene información")

print()
#En este ejemplo sí evalúa un boleano
variable = 19
if variable == True:
    print("if variable == True: es positivo")
else:
    print("No contiene , variable == True:, información")

print()
# Programa que pide una edad por consola y valora si el usuario es mayor
# de edad o no.
edad=int(input("Introduce edad: "))
if edad<18:
    print("No puedes pasar, <18 años")
elif edad>100:
    print("Edad incorrecta, >100 años")
else:
    print("Adelante, edad entre 18 a 99 años")

# Programa que pide una nota por consola y valora las posibles 
#calificaciones del alumno.
nota=int(input("Introduce tu nota: "))
if nota<5:
    print("Suspendido, nota <5")
elif nota<7:
    print("Aprobado, nota 5 a 6")
elif nota<9:
    print("Notable, nota 7 a 8")
elif nota<=10:
    print("Sobresaliente, 9 a 10")
else:
    print("Nota incorrecta")

print()
print("Ejemplos de IF abreviados")
# IF abreviado
n_num1 = 5
n_num2 = 10
if n_num1 > n_num2: print(f"{n_num1} , 'es mayor que' , {n_num2}")

print()
print('Ejemplos de IF...ELSE abreviados, print("A") if a > b else print("B")')
# IF...ELSE abreviado
a = 2
b = 330
print("A") if a > b else print("B")

print()

print( "Ejemplo de IF en rango, if 0<edad<100:")
# Se pueden concatenar operadores de comparación:
edad=117
if 0<edad<100: # Sería como poner: if edad>0 and edad<100
    print("Edad correcta")
else:
    print("Edad incorrecta")

print()
print("Ejemplo de IF concatenados con operadores de comparación")
print("if salarioOperario<salarioJefe<salarioDirector<salarioPresidente:")
print()

# Otro ejemplo de operadores de comparación concatenados
salarioPresidente = int(input("Introduce salario presidente: "))
print("El salario del presidente es de" ,salarioPresidente)
salarioDirector = int(input("Introduce salario Director: "))
print("El salario del director es de" , salarioDirector)
salarioJefe = int(input("Introduce salario jefe: "))
print("El salario del jefe es de" , salarioJefe)
salarioOperario = int(input("Introduce salario operario: "))
print("El salario del operario es de" , salarioOperario)
if salarioOperario<salarioJefe<salarioDirector<salarioPresidente:
    print("Todo ok")
else:
    print("Algo no va bien")

print()
print("Ejemplo operadores concatenados con OR")
print("if distancia>20 or numHermanos<2 or notaMedia<=5:")
# Operadores AND y OR
distancia = int(input("Introduce distancia: "))
numHermanos = int(input("Introduce número de hermanos en el centro: "))
notaMedia = int(input("Introduce notaMedia: "))
if distancia>20 or numHermanos<2 or notaMedia<=5:
    print("NO eres candidato a la beca")
else:
    print("Sí eres candidato a la beca")

print()
print("Ejemplo de operador IN")
# Operador IN
opcion = input("Escreibe la  opcion: opcion1, opcion2, opcion3, opcion4: ")
print('if pasoMinusculas in("opcion1", "opcion2", "opcion3", "opcion4"):')
pasoMinusculas = opcion.lower()
if pasoMinusculas in("opcion1", "opcion2", "opcion3", "opcion4"):
    print("Opción válida: " +
pasoMinusculas)
else:
    print("Opción inválida: " + pasoMinusculas)

print()
print("If anidados. Comprar un coche si somos mayores de edad y tener >=20000€")

    # If anidados. Queremos comprar un coche. Necesitamos ser mayores de edad y tener 20000€
n_edad = int(input("Introduzca su edad:"))
n_dinero = int(input("Introduzca presupuesto: "))
if n_edad < 18:
    print("No tienes la edad suficiente para conducir.")
else:
    if n_dinero < 20000:
        print("Tienes la edad pero no el dinero para comprar el coche.")
    else:
        print("Puedes comprar el coche.")