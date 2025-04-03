'''FUNCION OPEN'''

"""LA FUNCION 
opene( nombreArchivo, modo)
 
en modo tenemos:
r  -> Read ( leer )
a  -> Append ( añadir informacion al archivo) . Se usa para añadir mas informacion al archivo, manteniendo la existente.
w  -> Write ( Escribir) . OJO: Sobre-escribe todo lo que teniamos anteriormente. Cambia todo lo que habia. 
x  -> Crear un archivo.  Crear un archivo nuevo y es modo exclusivo...Si exite podriamos crear en exepcion.
r+ -> Lectura y escritura.
w+ -> Lectura y escritura. Si el archivo exste se sobreescribe la informacion ( como w) y si el archivo NO existe se crea uno nuevo.
a+ -> Lectura y agregar. Si el archivo no existe lo crea para escritura. 
"""


"""CREACION DE ARCHIVO PARA AGREGAR INFORMACION"""

# PASO 1: Definimos el nombre del archivo.
nombre_archivo='archivo_prueba.txt'         # definimos un nombre del tipo txt

#PASO 2:Abrimos el archivo en modo escritura 
archivo=open(nombre_archivo, 'w')       #! En este modo , w , reescribe siempre todo


#PASO 3:añadimos info al archivo:
archivo.write("Aqui cree mi primera linea dentro del archivo srchivo<-prueba.txt\n")
archivo.write("agregamos una 2da linea al archivo archivo_prueba.txt\n")

#PASO 4:Cerramos el archivo para liberar espacio
archivo.close()



