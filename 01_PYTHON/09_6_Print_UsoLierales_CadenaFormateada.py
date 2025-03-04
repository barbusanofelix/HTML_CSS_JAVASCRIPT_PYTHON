# USO DE LITERAL f PARA LA SALIDA DE IMPRESION
# Antes de la comilla simple o doble se escribe la f
# Entonces todo los que va entre comillas se imprimá y lo que este entre corchetes { } se sustituira
# por la variable que coloquemos en los corchetes.
# Declaramos una variable
name = "Antonio"
# Salida
print(f'hola {name}!. Qué tal?')

'''
Print con FORMAT()
la función format() para formatear nuestra salida para que se vea presentable. Las llaves { } funcionan como
marcadores de posición. Podemos especificar el orden en que aparecen las variables en la salida.
'''

# Declaramos de variables
a = 20
b = 10
# Suma
sum = a+b
# Resta
sub = a-b
# Salida

# FORMAT() EN ORDEN
# Lasvariables aparecen en el orden en que se colocan en el format
print('El valor de a es {} y b es {}'.format(a,b))
print()
print('Colocando b primero en el formato y sale mal porque no sale en la posicion correcta y SALE MAL,')
print('El valor de a es {} y b es {}'.format(b,a))
print()
# Expresear la posicion de lo colocado en format como un arreglo.
# El indice de format(a, b, sum) es 0 es a, 1 es b y 2 es sum  ( format(0,1,2))
print('{2} es la suma de {0} y {1}'.format(a, b, sum))
print()
#En format le asignamos un nombre y ese mismo nombre es que ira en los {}
print('{sub_value} es la resta de {value_a} y {value_b}'.format(value_a=a,value_b=b,sub_value=sub))
print()
print('{sub} es la resta de {a} y {b}'.format(a=a,b=b,sub=sub))    
