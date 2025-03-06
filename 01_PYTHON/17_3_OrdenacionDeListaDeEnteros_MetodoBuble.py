'''
Bubble Sort
La clasificación de burbujas es un algoritmo simple.
Intercambia los elementos adyacentes en cada iteración repetidamente hasta que se ordena la
matriz dada.
Itera sobre la matriz y mueve el elemento actual a la siguiente posición hasta que es menor que el
siguiente elemento.

Veamos los pasos para implementar el ordenamiento de burbuja.
• Inicialice la matriz con datos ficticios (enteros).
• Itere sobre la matriz dada.
    o Iterar desde 0 a ni-1. El último i los elementos ya están ordenados.
▪ Compruebe si el elemento actual es mayor que el siguiente elemento o no.
▪ Si el elemento actual es mayor que el siguiente, intercambie los dos elementos.

La complejidad temporal del ordenamiento de burbuja is O (n ^ 2), y la complejidad del espacio si O(1).


'''


def bubble_sort(arr, n):
    for i in range(n):
    ## iterando de 0 a n-i-1 ya que los últimos i elementos ya están ordenados
        for j in range(n - i - 1):
        ## comprobando el siguiente elemento
            if arr[j] > arr[j + 1]:
            ## intercambiando los elementos adyacentes
                arr[j], arr[j + 1] =arr[j + 1], arr[j]


if __name__ == '__main__':
    ## inicialización del array
    arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
    bubble_sort(arr, 9)

## imprimiendo el array
print(str(arr))