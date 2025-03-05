def es_primo(numero):
    """
    Determina si un número es primo.
    Args: numero (int): El número a verificar.
    Returns: bool: True si el número es primo, False en caso contrario.
    """

    # Los números menores o iguales a 1 no son primos
    if numero <= 1:
        return False
    
    # 2 es el único número primo par
    if numero == 2:
        return True

    # Los números pares mayores que 2 no son primos
    if numero % 2 == 0:
        return False

    # Verificar divisibilidad desde 3 hasta la raíz cuadrada del número
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False

    return True


# programa principal
numero = int(input("Numero a ver si primo : "))

if es_primo(numero):
    print(f"El numero {numero} ES PRIMO !!!")
else:
    print(f"El numero {numero} NO ES PRIMO")

