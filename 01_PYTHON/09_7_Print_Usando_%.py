'''
Podemos usar el operador '%'. Los valores de % se reemplazan con cero o más valores de elementos. El
formateo usando % es similar al de 'printf' en el lenguaje de programación C.
%d - entero
%f - flotante
%s - cadena
%x - hexadecimal
%o - octal
'''

# Entrada de datos
num = float(input("Introduzca un número:"))
add = num+5
# Salida
print("Entero: La suma es %d" %add)
print(f'El numero {num} es ',type(add))
print("flotante: La suma es %f" %add)
print("La variable add es del tipo :",type(add))
print("string: La suma es %s" %add)
add=int(add)  # Hay que convertirlo a entero pues %x y %o solo acepta enteros
print("hexadecimal : La suma es %x" %add)
print("octal La suma es %o" %add)