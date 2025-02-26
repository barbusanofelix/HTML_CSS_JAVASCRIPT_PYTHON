'''
Un usuario introduce texto desde teclado y queremos averiguar si 
es un número entero. Si es entero lo añadiremos a una variable tipo lista 
de números enteros. 
'''
listaEnteros=[]  # Creamos una lista vacía
numeroRecibido=None # Inicializamos la variable numeroRecibido
#----------------------------------------------------------------------------------------------------   

def imprimirLista(listaEnteros): # Imprime la lista de enteros
    print()
    print(f"La lista de enteros es {listaEnteros}")
    print()
#----------------------------------------------------------------------------------------------------
def salida(numeroRecibido): # Verifica si el usuario quiere salir
    if numeroRecibido.lower() == 's':
        print()
        print("La lista de enteros quedo asi:",listaEnteros)
        print()
        print("Saliendo...");print()
        return True
    return False
#----------------------------------------------------------------------------------------------------
# Verifica si el numero se puede convertir en flotante
# Si se coloca un numero con decimales distintos de cero, ej: 5.89 ( n.nn) o se introduce un numero, ej: 5.00 (n.00)
def convertirAFloat(numeroRecibido): 
    try:
        numeroRecibido = float(numeroRecibido)          # Si pasa es tipo n.nn ó n.00
        return True
    except ValueError:
        print()
        print(f'"{numeroRecibido}" No es un número!!')  # Si no pasa es texto
        return False
#----------------------------------------------------------------------------------------------------    
def es_entero(numero): # Verifica si el numero es de la instancia Entero
    try:
        if numero%1==0:
            return True  # Si el residuo de la division es 0, es entero
        else:
            print()
            print(f"El número {numero} NO es entero simple ( sin decimales). No se aadira a la lista !!")
            return False # Si el residuo de la division es diferente de 0, no es entero)
    except ValueError:
        print("No es un número válido.")
        return False
#----------------------------------------------------------------------------------------------------
def buscarNumero(listaEnteros,numeroRecibido): # Busca si el numero ya esta en la lista
    if numeroRecibido in listaEnteros:
        print()
        print(f"El numero {numeroRecibido} ya esta en la lista")
        
    else:
        listaEnteros.append(numeroRecibido)
        print(f"El numero {numeroRecibido} fue añadido a la lista")
    
#----------------------------------------------------------------------------------------------------
# Iniciamos      

while True:
    imprimirLista(listaEnteros) # Imprime la lista
    numeroRecibido= input("Teclea un numero - si es entero lo añadire a la lista ( s= Salir ):")
    if salida(numeroRecibido): # Verifica si el usuario quiere salir    
        break
    if convertirAFloat(numeroRecibido): # Verifica si el numero esta en formato flotante
       if es_entero(float(numeroRecibido)):   # verifica si el formato no tiene decimales distintos de cero
            numeroRecibido = float(numeroRecibido) # Convertimos el numero a entero
            numeroRecibido = int(numeroRecibido)
            buscarNumero(listaEnteros,numeroRecibido)
            #listaEnteros.append(numeroRecibido)
    
print("Fin del programa")
