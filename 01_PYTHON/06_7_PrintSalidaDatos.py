#Salida de directa de datos
print("En esta ocasión hemos imprimido por pantalla este string")
#Salida de datos calculados
n_numero_1 = 4
n_numero_2 = 6
print("El resultado de sumar" ,
n_numero_1, "y" , n_numero_2 , "es" ,
(n_numero_1+n_numero_2))
#Si concatenamos int y strings usando el signo + nos puede dar problemas.
# para evitar a error lo casteamos a str()
print("El resultado de sumar " +
str(n_numero_1) + " y " + str(n_numero_2) + " es "
+ str((n_numero_1+n_numero_2)))
print("El resultado de sumar" + " " + "los numeros")