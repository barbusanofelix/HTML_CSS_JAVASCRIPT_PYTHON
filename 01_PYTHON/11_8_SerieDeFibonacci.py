'''
La serie de Fibonacci es una secuencia infinita de números naturales en la que cada número es la suma de los dos anteriores.

Origen y Matemáticas:
Fue descrita por primera vez por el matemático italiano Leonardo de Pisa, conocido como Fibonacci, en su libro "Liber Abaci" (1202).
La secuencia comienza con 0 y 1. A partir de ahí, cada número siguiente se obtiene sumando los dos anteriores.
La secuencia comienza así:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Donde:

0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
Y así sucesivamente.
Importancia y aplicaciones:

La serie de Fibonacci aparece sorprendentemente en diversos contextos de la naturaleza, el arte y la ciencia:

Naturaleza:
Disposición de las hojas en algunas plantas.
Patrones de espirales en conchas de caracol y girasoles.
Ramificación de árboles.
Arte y arquitectura:
Proporciones en obras de arte y edificios famosos.
Matemáticas y ciencias de la computación:
Algoritmos y estructuras de datos.
Estudios de patrones y secuencias.
Mercados financieros:
Análisis técnico de los mercados financieros.
Propiedades Notables:

Proporción áurea: A medida que avanzamos en la serie, la proporción entre dos números consecutivos se acerca a la proporción áurea (aproximadamente 1.618). Esta proporción se encuentra en muchas formas de la naturaleza y el arte.
En resumen, la serie de Fibonacci es una secuencia matemática fascinante con aplicaciones sorprendentes en diversos campos.

'''
# Programa principal

n=int(input("Introduzca el número de valores de 'n' : ") )

first=0
second=1
sum=0

count=1
print("Secuencia de Fibonacci: ")
while(count <= n):
    print(sum)
    count+=1
    first=second
    second=sum
    sum=first+second