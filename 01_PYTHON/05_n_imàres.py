# los n primeros numeros impares.

# Ingremos n por pantalla y convertimos el n, que esta en texto, a entero con int()
n = int(input("Ingrese el valor de n: "))

# Formas distintas de imprimir n
# 1. "f-string" o "string formateado". Los f-strings son una forma conveniente y legible de insertar variables y expresiones dentro de las cadenas de texto.
#     el f-string sustituye la n, dentro de {n} por su valor

print(f"El valor de n, usando f-string formateado, es:      {n}")

# 2. .format(n) sustituye la f y {n} pasa a {} 
print("El valor de n, usando .format(n), es:               {}".format(n))

# 3. Usando especificador de formato: %d para un numero entero y con % n, reemplaza el especificador %d con el valor de la variable n
print("El valor de n, usando especificador de formato, es: %d" % n)

#4  Concatenando con el "+". Hay que reconvertir a String la n con str(n)
print("El valor de n, concatendando con + y Str() :        "+ str(n))

# for incremental
for i in range(1,n+1):  # Sumamos 1 porque n empieza en 0
    print(i)

#for decreciente
print()                     # Linea en blanco
for i in range(n, 0, -1):   # va desde n hasta antes de 0 
    print(i)
