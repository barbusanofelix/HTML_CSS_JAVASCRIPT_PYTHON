# Generacion de numeros aleatorios o ramdom

import random

 #la llene con diferentes numeros ascendentes
lista = [2,9,13,15,18,25,32,45,46,53] 

# Listas en Python son elementos mutables y si asignamos directamente 
# como listaDesordenada = lista , los cambios en listaDesordenada afectaran a lista
# Para copiar la lista hay que usar .copy() ó [:] 
listaDesordenada=lista.copy()   # Guardo copia de lista 
listaDes=lista[:]               # Guardo otra copia de lista
# Genera un random entre 0 u 1
randon= random.random()

# Elegir un aleaorio de la lista
elegido =random.choice(lista)

#shuffle() ( Barajar ) se aplica sobre la misma variable, es decir, sobre listaDesordenada
#Si se usa una variable intermedia devolvera None
random.shuffle(listaDesordenada) #Desordena y la guarda en la misma listaDesordenada
desOrden=random.shuffle(listaDes)


print("La lista original es:", lista)
print("Numero aleatorio 0 a 1 : ", randon)
print("Eleccion de un numero de la lista:", elegido)
print("Lista desordenada ( al azar ) :", listaDesordenada) # Aplique random.shuffle(listaDesordenada)
# No funciona porque shuffle() hay que usarlo directo sobre si mismo
print("Asigne a variable desOrden=random.shuffle(listaDes)", desOrden)