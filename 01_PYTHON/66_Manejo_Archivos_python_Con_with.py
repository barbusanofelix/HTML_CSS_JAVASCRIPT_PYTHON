
""" UTILIZAR EL BLOQUE WITH tiene las ventajas:

1. Podemos abrir el archivo y asignar directamente su nombre de uso en nuestro programa con "as"
2. No necesitamos cerrar el archivo porque al finalizar el bloque with se cierra automaticamente. 

En el programa 65_Manejo_Archivos_Python_Crear_y_adicionar.py teniamos el codigo:


   CREACION DE ARCHIVO PARA AGREGAR INFORMACION

# PASO 1: Definimos el nombre del archivo.
nombre_archivo='archivo_prueba.txt'         # definimos un nombre del tipo txt

#PASO 2:Abrimos el archivo en modo escritura 
archivo=open(nombre_archivo, 'w')       #! En este modo , w , reescribe siempre todo


#PASO 3:añadimos info al archivo:
archivo.write("Aqui cree mi primera linea dentro del archivo srchivo<-prueba.txt\n")
archivo.write("agregamos una 2da linea al archivo archivo_prueba.txt\n")

#PASO 4:Cerramos el archivo para liberar espacio
archivo.close()

Ahora lo podemos hacer asi: ( de 5 lineas bajamos a 3) 
"""

with open('archivo_prueba.txt','w') as archivo:
    archivo.write("Aqui cree mi primera linea dentro del archivo srchivo<-prueba.txt\n")
    archivo.write("agregamos una 2da linea al archivo archivo_prueba.txt con with\n")
    




