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

def descomponer_en_factores(numero):
    """
    Descompone un número en sus factores primos.
        numero (int): El número a descomponer.
        factores: Una lista de factores primos.
    """

    factores = [] # Inicializamos la lista de factores, vacia
    primos = obtener_primos(numero)  # Obtenemos la lista de primos del numero
    
    for primo in primos: # Iteramos en la lista de primos por cada primo
        
        while numero % primo == 0:  # Si division del numero entre primo es exacta es un factor
            factores.append(primo)  # añado el factor a la lista
            numero //= primo  # Esto es igual a numero = numero // primo. El resultado de la division para a ser el numero
          
    return factores

def verificarFactores(factores):
    # verificamos:
    cantidad= len(factores) # Obtenemos la cantidad de factores primos

    multiplicacion=1  # Inicializo en 1 para luego acumular la multiplicacion de factores
    for f in range(0,cantidad,1):
        multiplicacion*= factores_primos[f]  # Multiplico p
    
    return multiplicacion

# Ejemplo de uso
numero_a_descomponer =100


factores_primos = descomponer_en_factores(numero_a_descomponer)
print(f"Factores primos de {numero_a_descomponer}: {factores_primos}")

# Verificacion  
resultado = " x ".join(str(elemento) for elemento in factores_primos) # Resullado coloca los elementos con signo x entre ellos
print(f"La verificacion de {resultado} nos da {numero_a_descomponer}")




