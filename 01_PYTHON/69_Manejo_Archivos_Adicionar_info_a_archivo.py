'''PARA AADICIONAR INFORMACION A UN ARCHIVO SE USA APPEND ( 'a' )'''


archivo='archivo_prueba.txt'

with open(archivo,'a') as a:
    a.write("Adicionando informacion al archivo .....\n" )
    a.write("4ta linea en el archivo\n")
    
print("Se termino e adicionar info al archivo {archivo}\n")    
    
    
with open(archivo,'r') as a:
    print(a.read())         # Lee todas las lineas
    
    
       