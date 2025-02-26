# Módulo. Nos devuelve el resto de una división:
n_numerador = 85
n_denominador = 9
n_resto = n_numerador%n_denominador
print(f"La division normal entre {n_numerador}/{n_denominador}={n_numerador/n_denominador}")
print(f"Si tomamos la parte entera de la division: {int(n_numerador/n_denominador)} x denomidor {n_denominador} = {int(n_numerador/n_denominador)} x {n_denominador} = {int(n_numerador/n_denominador)*n_denominador}" )
print(f"El resto de dividir {n_numerador}/{n_denominador}=" ,
n_resto)
# == Igual que...
# No confundir con el operador de asignación =
# Con = le damos un valor a una variable. Con == comprobamos si dos
# objetos son iguales.
n_numero1 = 34
s_texto1 = "34"
print(f"Es n_numero1 = 34 igual a s_texto1 = '34' : {n_numero1 == s_texto1}")
n_numero2 = 34
n_numero3 = 34
print(f"Es n_numero2 = 34 igual a n_numero3 = 34 : {n_numero2 == n_numero3}")
# != Diferente que...
n_numero4 = 34
n_numero5 = 34
n_numero4 != n_numero5
print(f"Es n_numero4 = 34 es diferente a n_numero5 = 34 : {n_numero4 != n_numero5}")
# += Suma e incremento
n_numero6 = 34
n_numero6 += 1 #Sería como poner:n_numero6 = n_numero6 +1
# en la print(f"n_numero6 =.....) no permite aplicar el n_numero6 += 1 directamente entre corches.
# esa operacion no la resuelve
print(f"n_numero6 = 34 y n_numero6 += 1, seria como poner n_numero6 = n_numero6 +1  : {n_numero6}")
