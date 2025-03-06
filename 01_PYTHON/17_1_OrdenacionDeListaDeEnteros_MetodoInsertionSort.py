'''
Insertion Sort 
( Ver documento 17_Programacion en Python_Algoritmos de clasificacion en Python_Tema6_Parte6_Clasificacion_v1.pdf - pag 4)
La ordenación por inserción es uno de los algoritmos de ordenación más simples. Es fácil de implementar, pero a la hora 
de ordenar matrices necesitará más tiempo. No es recomendable para clasificar matrices grandes.
El algoritmo mantiene subpartes ordenadas y no ordenadas en la matriz dada.
La subparte contiene solo el primer elemento al comienzo del proceso de clasificación. Tomaremos un elemento de la matriz 
no ordenada y los colocaremos en la posición correcta en la sub-matriz ordenada.

'''



def insertion_sort(arr, n):
    for i in range(1, n):
    ## posición actual y elemento
        current_position = i
        current_element = arr[i]
        ## iterar hasta llega al primer elemento o ## el elemento actual es más pequeño que el elemento anterior
        while current_position > 0 and current_element <arr[current_position - 1]:
            ## actualizar el elemento actual con el elemento anterior
            arr[current_position] =arr[current_position - 1]
            ## moviéndose a la posición anterior
            current_position -= 1
            ## actualizar el elemento de  posición actual
            arr[current_position] =current_element

if __name__ == '__main__':
    ## inicialización del array
    arr = [3, 4, 11, 8, 1, 9, 5, 2, 6,10,7]
    arrCopy=arr.copy()
    cantElementos = len(arr) # La cantidad de elementos en el arreglo se envian a la funcion junto con el arreglo.
    insertion_sort(arr, cantElementos)
## imprimiendo el array
print(str(arr))
print();print()
print("Ahora ordeno con sort ()")
arrCopy.sort()
print("Ordenado con sort : ", arrCopy)
