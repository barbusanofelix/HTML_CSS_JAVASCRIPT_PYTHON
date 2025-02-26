# POLIMORFISMO FUNCIONES
# La misma funcion devuelve diferentes tipos de datos segun lo que le pasemos.
# Si le pasamos enteros, float o string devolvera el mismo tipo que se envio

def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    return a+b # "return" devuelve el resultado de la función.
xint=suma (2, 3) # Función con ints ( Entero=)
# Resultado = 5


xfloat=suma(2.7, 4.0) # Función con floats ( Numero Flotante)
# Resultado = 6.7
xstring=suma('Me gusta', ' Python') # Función con strings

print("Suma devuelve un entero = ",xint)

print("Suma devuelve un float =", xfloat)

print("Suma de palabras = ", xstring)
