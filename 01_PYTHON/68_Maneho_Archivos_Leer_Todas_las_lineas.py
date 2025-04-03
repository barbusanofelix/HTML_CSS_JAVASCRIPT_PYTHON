'''LEER LAS LINEAS DE UN ARCHIVO'''


nombre_archivo='archivo_prueba.txt'

#Leer el archivo usando readlines
#! IMPORTANTE: SI SE EFECTUA UNA LECTURA EL ITERADOR SE COLOCA AL FINAL Y SI QUIERES HACER OTRA LECTURA NO RESULTARA.
with open(nombre_archivo,'r') as archivo:
    #print(archivo.readlines())      #! ojo , si ejecutamos esto, el archivo llega al final y no se ejecutara el for ( No mostrara nada) 
    
    print("USO DE METODO READLINES ...UNA LINEA A LA VEZ")
    lineas=archivo.readlines()
    for linea in lineas:
        #print(linea)
        print(linea.strip())  #? Aqui quitamos los saltos de linea pero como es un ciclo cada linea pasa a la siguiente.
        
        
'''METODO READ LEE TODO EL ARCHIVO''' 

print("\n USO DEL METODO READ: LEE TODO EL ARCHIVO COMPLETO")
with open(nombre_archivo,'r') as archivo:
    print(archivo.read().strip())               # SE PUEDE USAR COMBINADO CON STRIP() PARA QUEITAR SALTOS DE LINEAS Y TABULADORES.
    