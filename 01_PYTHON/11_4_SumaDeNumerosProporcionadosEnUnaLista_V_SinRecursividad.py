# Hace lo mismo que lo "mismo que 11_4_SumaDeNumerosProporcionadosEnUnaLista."
# pero sin aplicar recursividad


def list_sum(num_List):
    suma = 0
    for n in num_List:
        suma+=n
    return suma  # el return no se puede colocar con el identado de suma pues sino se sale en el primer ciclo.

# CORAZON DEL PROGRAMA    
print(list_sum([3, 5, 8, 9, 9]))