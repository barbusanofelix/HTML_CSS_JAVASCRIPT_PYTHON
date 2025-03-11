
# ? EJEMPLO DE PROGRAMACION ESTRUCURADA PARA COMPARARLA CON POO


#* Definimos unos cuantos clientes. Clientes es una Lista con diccionarios en su interior
clientes= [{'Nombre': 'Hector','Apellidos':'Costa Guzman','dni':'11111111A'},
           {'Nombre': 'Juan','Apellidos':'González Márquez','dni':'22222222B'}]

#* Creamos una función que muestra un cliente en una lista a partir del DNI
#* Se manda clientes porque clientes esta definido fuera de la funcion y asi usarlo dentro de ella.
def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return                  #* Si encuentra el cliente ya se imprimio y se sale.
    print('Cliente no encontrado')  #* Linea fuera del for, asi que si no encuentra el cliente la muestra
        
# Creamos una función que borra un cliente en una lista a partir del DNI
def borrar_cliente(clientes, dni):
    print(f"Buscando cliente con DNI {dni}", end=" ")
    for i,c in enumerate(clientes):
        if (dni == c['dni']):
            del( clientes[i] )
            print(str(c),"> BORRADO")
            return
    print('Cliente no encontrado')
    
def imprimirClientes(clientes):
    for cliente in clientes:
        print(cliente)
            
def imprimirNombresCliente(clientes):
    print()
    print( "IMPRIME SOLO NOMBRES POR CLIENTE ")
    for cliente in clientes:
        print(cliente["Nombre"])
        
#? USANDO COMPRESION DE LISTA
def soloNombreClientes(clientes):
    #* Usando la compresion de lista
    print()
    print("REUNIR LOS NOMBRES DE LOS CLIENTES")
    nombres=[cliente["Nombre"] for cliente in clientes ]  
    nombres=",".join(nombres)      
    print(nombres)
                    
### Fíjate muy bien cómo se utiliza el código estructurado
print("==LISTADO DE CLIENTES==")
imprimirClientes(clientes)
print("\n==MOSTRAR CLIENTES POR DNI==")
mostrar_cliente(clientes, '11111111A')
mostrar_cliente(clientes, '22222222B')
print("\n==BORRAR CLIENTES POR DNI==")
borrar_cliente(clientes, '22222222V')
borrar_cliente(clientes, '22222222B')
print("\n==LISTADO DE CLIENTES==")
imprimirClientes(clientes)
imprimirNombresCliente(clientes)
soloNombreClientes(clientes)
        
        
        
# mostrar_cliente(clientes,"11111111B")        
