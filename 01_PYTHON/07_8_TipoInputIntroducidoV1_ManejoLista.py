lista_enteros = []

def imprimir_lista(lista):
    print("\nLa lista de enteros es:", lista, "\n")

def es_salida(entrada):
    if entrada.lower() == 's':
        print("\nLa lista de enteros final es:", lista_enteros, "\nSaliendo...\n")
        return True
    return False

def agregar_entero(entrada):
    try:
        numero = float(entrada)
        if numero.is_integer():
            numero_entero = int(numero)
            if numero_entero not in lista_enteros:
                lista_enteros.append(numero_entero)
                print(f"El número {numero_entero} fue añadido a la lista.")
            else:
                print(f"El número {numero_entero} ya está en la lista.")
        else:
            print(f"El número {numero} no es un entero.")
    except ValueError:
        print(f'"{entrada}" no es un número válido.')

def main():
    while True:
        imprimir_lista(lista_enteros)
        entrada = input("Teclee un número entero (s = Salir): ")
        if es_salida(entrada):
            break
        agregar_entero(entrada)
    print("Fin del programa.")

if __name__ == "__main__":  #para ejecutar la funcion main() solo si se ejecuta el fichero python directamente.
    main()