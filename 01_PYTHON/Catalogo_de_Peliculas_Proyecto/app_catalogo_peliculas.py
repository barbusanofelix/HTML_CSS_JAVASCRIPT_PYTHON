
from servicio_peliculas import Servicio_peliculas

class CatalogoPeliculas():
   
   
    def __init__(self):
            self.servicio_peli =Servicio_peliculas()           # Creamos una instancia de ServicioSnacks para usar los metodos
             
    def manejo_catalogo(self):
        #lugar=input("Estoy aqui para depurara")
        
        salir=False
        print("**** Manejo Catalogo de Peliculas ****")
        
        while not salir:
            try:
                opcion= self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"Ocurrio un error al salir {e}") 
    
    def mostrar_menu(self):
        print('''\n Menu
             1. Agregar Peliculas.
             2. Mostrar Peliculas.
             3. Eliminar Catalogo de Peliculas.
             4. Salir
             ''')
        return int(input("Elige una opcion :"))
    
    def ejecutar_opcion(self, opcion):
        if opcion==1:
            self.servicio_peli.agregar_pelicula()
        elif opcion==2:
            self.servicio_peli.listar_peliculas()
        elif opcion==3:
            self.servicio_peli.eliminar_archivo()
        elif opcion==4:
            print('Saliendo...hasta luego')
            return True
        else:
            print(f'Opcion invalida: {opcion}')   
    
    
    
   # Entrada del Programa
   # programa principal
if __name__=='__main__':
    catalogo=CatalogoPeliculas()    # Cramos la instancia de nuestra clase CatalogoPeliculas()
    catalogo.manejo_catalogo()      # Activamos el manejo de catalogo