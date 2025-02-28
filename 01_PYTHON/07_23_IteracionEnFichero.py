zen = '''\
    Bello es mejor que feo.
    Explícito es mejor que implícito.
    Simple es mejor que complejo.
    Complejo es mejor que complicado.
    '''

f = open('short_zen.txt', 'w')
f.writelines(zen) # Escribe el fichero con el fichero en memoria ( variable zen )
f.close() # Cierra el fichero

f = open('short_zen.txt', 'r')
linea=f.readline()
print(linea)
# salida 'Bello es mejor que feo. \n'

linea=f.readline()
if linea == '':
    print('Fin del fichero')
else:    
    print(linea)
# salida 'Explícito es mejor que implícito.\n'

linea=f.readline()
if linea == '':
    print('Fin del fichero')
else:    
    print(linea)
#salida 'Simple es mejor que complejo. \n'

linea=f.readline()
if linea == None:
    print('Fin del fichero')
else:    
    print(linea)
#salida 'Complejo es mejor que complicado. \n'

# Devuelve una cadena vacía cuando termina el fichero

linea=f.readline()
if linea == "":
    print('Fin del fichero')
else:    
    print(linea)

print('Ahora con for in ')
# lo sigueinte es lo mismo que el codigo anterio pues recorre el archovo short_zen.txt'
for linea in open('short_zen.txt'): # Por defecto el archivo se abre en modo lectura ( 'r' )
    print(linea.upper(), end='')

f.close() # Cierra el fichero