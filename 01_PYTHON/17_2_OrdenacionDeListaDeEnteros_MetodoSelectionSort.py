'''
Selection Sort
El orden de selección es similar al orden de inserción con una ligera diferencia. Este algoritmo también
divide la matriz en subpartes ordenadas y no ordenadas. Y luego, en cada iteración, tomaremos el
elemento mínimo de la subparte sin clasificar y lo colocaremos en la última posición de la subparte
ordenada.

Veamos los pasos para implementar el tipo de selección.

• Inicialice la matriz con datos ficticios (enteros).
• Itere sobre la matriz dada.
    o Mantener el índice del elemento mínimo.
    o Escribe un bucle que repita desde el elemento actual hasta el último elemento.
▪ Compruebe si el elemento actual es menor que el elemento mínimo o no.
▪ Si el elemento actual es menor que el elemento mínimo, reemplace el índice.
    o Tenemos el índice mínimo de elementos con nosotros. Intercambia el elemento actual con
    el elemento mínimo usando los índices.
La complejidad temporal del tipo de selección is O (n^ 2), y la complejidad del espacio si O (1).

'''



def selection_sort(arr, n):
    for i in range(n): 
    ## para almacenar el índice del elemento mínimo
        min_element_index = i
        for j in range(i + 1, n):
    ## comprobando y reemplazando el índice mínimo del elemento
            if arr[j] < arr[min_element_index]:
                min_element_index = j
            ## intercambiando el elemento actual con el elemento mínimo
        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]

if __name__ == '__main__':
## inicialización del array
    arr = [3, 4, 7, 8, 10, 9, 5, 2, 6,1]
canElementos=len(arr)    
selection_sort(arr, canElementos)
## imprimiendo el array
print(str(arr))
print()