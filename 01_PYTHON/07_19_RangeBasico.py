# Ejemplos de uso de range
# Hay que envolverlo en lista o recorrerlo en for
# range(5) devuelve 5 elementos empezando en 0 en una lista al igual que los siguientes ejemplos.
print("lISTA DE 0 A 4:",list(range(5))) # Devuelve 5 elementos empezando en 0
# [0, 1, 2, 3, 4]
print("LISTA DE -5 A 4:",list(range(-5, 5))) # Devuelve elementos en el rango -5, 5 pero OJO, NO INCLUYE EL ELEMENTO FINAL

print("lista de -5 a 5, saltando de 3 en tres:",list(range(-5, 5, 3))) # Elementos -5 a 5 en saltos de 3

print("Lista de -5 a 5 saltando de 2 en 2: ",list(range(-5, 5, 2))) # Elementos -5 a 5 en saltos de 2. 