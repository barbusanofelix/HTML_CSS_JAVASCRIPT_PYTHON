def merge(arr, left_index, mid_index,right_index):
## matrices izquierda y derecha
    left_array =arr[left_index:mid_index+1]
    right_array =arr[mid_index+1:right_index+1]
    ## obtener las longitudes de matriz izquierda y derecha
    left_array_length = mid_index -left_index + 1
    right_array_length = right_index -mid_index
    ## índices para fusionar dos matrices
    i = j = 0
    ## índice para el reemplazo de elementos de matriz
    k = left_index
    ## iterando sobre las dos submatrices
    while i < left_array_length and j <right_array_length:
    ## comparar los elementos de lasmatrices izquierda y derecha
        if left_array[i] <right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1
    ## agregando elementos restantes de las matrices izquierda y derecha
    while i < left_array_length:
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < right_array_length:
        j += 1
        k += 1
def merge_sort(arr, left_index,right_index):
## caso base para función recursiva
    if left_index >= right_index:
        return
    ## encontrar el índice medio
    mid_index = (left_index +right_index) // 2
    ## llamadas recursivas
    merge_sort(arr, left_index,mid_index)
    merge_sort(arr, mid_index + 1,right_index)
    ## fusionando las dos sub-matrices
    merge(arr, left_index, mid_index,right_index)
if __name__ == '__main__':
    ## inicialización de matriz
    arr = [3, 4, 7, 8, 10, 9, 5, 2, 6,1]
    cantElementos=len(arr)
merge_sort(arr, 0, cantElementos-1)
## imprimiendo la matriz
print(str(arr))