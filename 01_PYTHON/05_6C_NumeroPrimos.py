def obtener_primos(numero):
    """
    Devuelve una lista de números primos menores o iguales a un número dado.
    numero (int): El número máximo hasta el cual buscar primos.
    Returns:
        primos : Una lista de números primos.
    """

    if numero < 2: # No hay primos <2 asi que devuelve vacio
        return []

    # Inicializamos num_candidato con True ( Todos son candidatos a primos, incluyendo al numero)
    num_candidato = [True] * (numero + 1)  # Crea una lista de 0 a n ( por eso el +1)
    num_candidato[0] = num_candidato[1] = False  # 0 y 1 no son primos

    # Metodo Eratostenes ( https://www.youtube.com/watch?v=QsNFfwwpB88&t=292s )
    # Los posibles primos van desde el 2 hasta raiz cuadrada de numero y el numero es si, que ya esta marcado como primo
    for n in range(2, int(numero**0.5) + 1,1): # n=numero en el rango
        if num_candidato[n]: #n inicio en 2 y es primo asi que descartaremos lo noPrimos
            # Metodo: noPrimo el n x n y luego sumarle n y repetir hasta recorrer hasta el numero ( numero+1, porque indice inicia en cero)     
            for noPrimo in range(n * n, numero + 1, n):#Inicia en noPrimoxnoPrimo
                num_candidato[noPrimo] = False

    #Construye una lista de los primos. En los ciclos anterios ya se determino los n=True
    # por cada indice( n ) en rango de 2 al 11 ( Toma hasta 10), si n es True lo añade a primo
    primos = [n for n in range(2, numero + 1,1) if num_candidato[n]]
    return primos

# Ejemplo de uso
numero_maximo = 33
lista_primos = obtener_primos(numero_maximo)
print(f"Numeros primos menores o iguales a {numero_maximo}: {lista_primos}")

