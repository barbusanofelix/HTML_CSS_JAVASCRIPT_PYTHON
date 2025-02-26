def maxmin(lista):
    return max(lista), min(lista) #Devuelve 2 elementos

listaOriginal = [1, 3, 5, 6, 0]
# Asignamos el maximo y minimo simultaneamente porque maxmin() recibe 2 salidas,
maximo, minimo = maxmin(listaOriginal) #Desempaqueta la tupla en 2 variables
print(minimo, maximo, sep= '/')  #sep es el separador entre los valores que se imprimiran