

''' CONTENER EL MENU DE LA APICACION'''

from cliente_dao import ClienteDAO   # Importamos Clase ClienteDAO
from clientes import Cliente         # Importamos la Clase Cliente

class App_Zona_Fit():

    def control_clientes(self):
        salir=False
        #print("**** Control de Clientes ****")
        # self.dao_clientes.listar_clientes()
        while not salir:
            try:
                
                opcion= self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"Ocurrio un error al salir {e}")    
        
    
    def mostrar_menu(self):
        print('''\n Menu Clientes
             1. Listar
             2. Modificar
             3. Agregar 
             4. Eliminar
             5. Salir
              ''')
        return int(input("Elige una opcion :"))
    
    def titulo_impresion(self, clientes):
        print()
        print('*'*25 +' '*10+'LISTADO DE CLIENTES'+' '*10+'*'*25)
        print(f'{'id':<6}{'Nombre':<35}{'Apellido':<35}{'Membresia':<10}')  
        print('-'*90)
        for cliente in clientes:
            print(cliente)
           
    def datos_cliente(self):
        id_cliente=input('id :')
        nombre=input('Nombre: ')
        apellido= input('Apellido :')
        membresia=int(input('Membresia:'))     
        return Cliente(nombre=nombre, apellido=apellido, membresia=membresia, id=id_cliente)                
    
    def ejecutar_opcion(self, opcion):
        if opcion==1:
            clientes=ClienteDAO.seleccionar()
            self.titulo_impresion(clientes)  
        elif opcion==2:
            cliente=self.datos_cliente()
            actualizado=ClienteDAO.actualizar(cliente)
            print('Se actualizo cliente', actualizado)
            
        elif opcion==3:
            pass
            #ClienteDAO.insertar()
        elif opcion==4:
            pass
            #ClienteDAO.eliminar()
        elif opcion==5:
            print('Saliendo...hasta luego')
            return True
        else:
            print(f'Opcion invalida: {opcion}')   
            
            
if __name__=='__main__':
    zona_fit=App_Zona_Fit()             # Creo un Objeto de la clase
    zona_fit.control_clientes()         #Es una funcion     