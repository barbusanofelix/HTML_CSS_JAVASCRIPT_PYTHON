from servicio_snacks import ServicioSnacks
from snacks import Snacks

class MaquinaSnacks():
    
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()           # Creamos una instancia de ServicioSnacks para usar los metodos
        self.productos=[]                               # creamos una lista para los productos que se iran comprando.
    
    # Por aqui en la entrada principal del programa
    def maquinasnacks(self):
        #lugar=input("Estoy aqui para depurara")
        print("Entra a Maquina Snacks")
        salir=False
        print("**** Maquina Snacks ****")
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                
                opcion= self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"Ocurrio un error al salir {e}")    
        
    
    def mostrar_menu(self):
        print('''\n Menu
             1. Comprar Snacks
             2. Mostrar Ticket
             3. Agregar nuevo Snack al inventario
             4. Inventario Snacks
             5. Eliminar un Snack del inventario
             6. Salir
              ''')
        return int(input("Elige una opcion :"))
    
    def ejecutar_opcion(self, opcion):
        if opcion==1:
            self.comprar_snack()
        elif opcion==2:
            self.mostrar_ticket()
        elif opcion==3:
            self.agregar_snack()
        elif opcion==4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion==5:
            id_eliminar=int(input("Id_Snack a eliminar : "))
            self.servicio_snacks.eliminar_snacks(id_eliminar)
        elif opcion==6: 
            print('Saliendo...hasta luego')
            return True
        else:
            print(f'Opcion invalida: {opcion}')            
    
    def comprar_snack(self):
        print("Estos son los Snacks disponibles\n")
        self.servicio_snacks.mostrar_snacks()
        id_snack = int(input('Que Snack quieres comprar (id) :'))
        snacks = self.servicio_snacks.get_snacks()   # Se trae la losta completa de los snacks en inventario y los guarda en una lista
        # definimos un iterador 
        snack = next((snack for snack in snacks if snack.id_snack == id_snack),None)
        if snack:
            self.productos.append(snack)
            print(f'Snack encontrado {snack}')
        else:
            print('Snack no encontrado con id {id_snack}')    
            
    def mostrar_ticket(self):
        if not self.productos:
            print('No hay snacks en el ticket')
            return
       
        total=sum(snack.get_precio() for snack in self.productos)
        print('\n **** Ticket de Venta ***')
        for producto in self.productos:
            # Al ser producto un objeto Snacks y como el nombre y precio estan protegidos hay que accesarlos usando el get_nombre y get_precio
            print(f'\t-{producto.get_nombre():<25}   -   ${producto.get_precio():>15.2f}')
            
        print(f'\t Total  -> {total:>38.2f}')
        
    def agregar_snack(self):
        nombre= input('Nombre del snack: ')
        precio=float(input('Precio del Snack : '))
        nuevo_snack=Snacks(nombre, precio)
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print('Snack agregado')
        
        
# programa principal
if __name__=='__main__':
    maquina_snacks=MaquinaSnacks()    
    maquina_snacks.maquinasnacks()    # Crea una instancia de la clase maquina
        