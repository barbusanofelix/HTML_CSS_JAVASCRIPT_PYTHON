#----------------------------------------------------------------------------
import pickle 
from pathlib import Path

#Create an empty dictionary
d = dict()

def abrirOCrearDicionario(nombreArchivo_pkl):
    #Ask for file name to load dictionary from
    # Podemos usar otro nombre de archivo si queremos. Sino existe lo creara con el nombre que le demos. En este caso es diccionario.pkl
    file_name =nombreArchivo_pkl         #"datos.pkl"   #input("Introduce el nombre del archivo con los datos: ")

    #Comprobamos que existe
    path = Path(file_name)  #Crea un objeto Path que representa la ruta del archivo especificado por el usuario.
    print("El path del diccionario es:", path)
    # Obtener la ruta absoluta
    ruta_absoluta = path.absolute()

    # Imprimir la ruta absoluta
    print("Ruta absoluta:", ruta_absoluta)
    if path.is_file():                  #Verifica si el archivo existe realmente en el sistema de archivos.
        # Open file in reading mode
        input_file = open(file_name, 'rb')
        d = pickle.load(input_file)
        #Close de file
        input_file.close()
    else:    
        print("El file no existe, creamos diccionario vacio")
        # Guarda el diccionario vacío en el archivo
        with open(file_name, 'wb') as output_file: #Esto crea y abre el archivo en modo escritura binaria ('wb') y guarda el diccionario vacío d en él.
            pickle.dump(d, output_file)
    return d, file_name


#----------------------------------------------------------------------------------------------------
# Iniciamos un diccionario con dos elementos, dni y la edad
#d = { "50862634" : 37 , "43394932" : 32} # d= diciionario con dos elementos, dni y la edad
#----------------------------------------------------------------------------------------------------
def imprimirDic(d):
    print()
    print("El diccionario tiene :",d);print()
#----------------------------------------------------------------------------------------------------
def salida(dni):
    if dni.lower() == 's':
        print()
        print("El diccionario quedo asi:",d)
        print()
        print("Saliendo...");print()
        return True
    return False
#----------------------------------------------------------------------------------------------------
def comprobar(dni):
    if dni.isnumeric(): # Verificamos si dni es solo digitos ( un entero)
        if dni in d:
            print("La edad de " + dni + " es " + str(d[dni]) )# str(d[dni]) muestra el valor de la edad para el dni
        else:
            edad = input("Documento no existente. Introduce edad: ")
            print()
            if edad.isnumeric():  # Verificamos si edad es solo digitos ( un entero) 
                num = int(edad)
                d[dni] = num  # Añadimos el dni y la edad al diccionario
                print("Añadido al diccionario")
    else:
        print()
        print(f'Documento, "{dni}" no esválido. Solo se permiten números')
        print()

#-------------------------------------------------------------------------------------------
def guardar_diccionario(diccionario, nombre_archivo):
    """Guarda un diccionario en un archivo usando pickle."""
    try:
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(diccionario, archivo)
        print(f"Diccionario guardado en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar el diccionario: {e}")        
#----------------------------------------------------------------------------------------------------
# BLOQUE PRINCIPLA
#-------------------------------------------------------------------------------------------
# Iniciamos el programa
# Asignamos el diccionario a la variable d y a file_name el nombre del archivo en Disco que realmente es diccionario.pkl
# Si queremos usar o crear otro diccionario cambiamos el nombre de diccionario.pkl por otro nombre
#-------------------------------------------------------------------------------------------
d,file_name=abrirOCrearDicionario("diccionario.pkl")  
while True:
    imprimirDic(d)                                        # Imprime el diccionario
    dni = input("Introduce un documento de indentidad ( s: salir): ")  # Solicita el dni
    if salida(dni):                                       # Verifica si salimos con s o S
        break                                             # Salimos del programa si usuario introdujo s ó S                              
    comprobar(dni)                                        # Verifica si el dni existe en el diccionario
                                                          # Sino existe lo añadimos al diccionario
#----------------------------------------------------------------------------------------------------       
  # Para guardar al final del programa:
    guardar_diccionario(d, file_name) # d es el diccionario en memoria y file_name es el nombre del archivo en disco.