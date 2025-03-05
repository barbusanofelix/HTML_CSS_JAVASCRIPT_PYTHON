
#ORDENA UNA LISTA DE NUMEROS STRING 

# Lista original: Numeros en string
lista =[ "4", "1", "8", "6", "2","1"]
print("La lista original es            :", lista)

# Convierte numero a entero por cada numero en la lista
lista=[int(numero) for numero in lista]  

lista.sort()
print("La lista ahora es               :", lista)
# devolvemos la lista a string
lista =[str(numero) for numero in lista]

print("La lista como string , ahora es :", lista)