'''MODO EXCLUSIVO SIGNIFICA QUE SI EL ARCHIVO EXISTE NOS MANDA UNA EXCEPCION 
    Esto evitaria sobre-escribir un archivo que tengamos.

'''

archivo="archivo_prueba.txt"

try:
    with open(archivo,'x') as a:
        a.write("Es la version que no puede sobre.escribir\n" )
        a.write("Aqui borre del disco el archivo y aqui lo cree con este texto\n")
except Exception as e:
    print(f"Error: {e}.  El archivo: {archivo} ya existe")    
else:
    print("El archivo {archivo} fue creado satisfactoriamente")    # Muestra el mensaje en caso de no haber ocurrido error.
    
    