
zen = '''\
    Bello es mejor que feo.
    Explícito es mejor que implícito.
    Simple es mejor que complejo.
    Complejo es mejor que complicado.
    '''

f = open('short_zen.txt', 'w')   # f es un objeto de tipo file con el fichero short_zen.txt abierto en modo escritura
f.writelines(zen) # Escribe el fichero con el fichero en memoria ( variable zen )
f.close() # Cierra el fichero


f = open('short_zen.txt', 'r')

for line in f:
    print(line.upper(), end='')
# salida 'BELLO ES MEJOR QUE FEO. \nEXPLÍCITO ES MEJOR QUE IMPLÍCITO.\nSIMPLE ES MEJOR QUE COMPLEJO. \nCOMPLEJO ES MEJOR QUE COMPLICADO. \n'    

print(); print()
# Esto es identicamente igaual a lo anterior.
for line in open('short_zen.txt'):  
    print(line.upper(), end='')
'''
# Lo anterior es como hacer este print(f.__next__())  en un bucle
print(f.__next__())
# salida 'Bello es mejor que feo. \n'
f. __next__()
# salida 'Explícito es mejor que implícito.\n'      
f. __next__()
# salida 'Simple es mejor que complejo. \n'
f. __next__()
# salida 'Complejo es mejor que complicado. \n'
f. __next__()
'''   
# salida ''
f.close()
