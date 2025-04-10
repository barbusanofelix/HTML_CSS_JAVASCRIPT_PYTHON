'''SERVICIO PELICULAS'''
from pelicula import Pelicula
import os.path

class Servicio_peliculas():
    NOMBRE_ARCHIVO='pelicula.txt'
    
    
    def __init__(self):
        self.peliculas=[]
        
        #Si exite el archivo cargamos las peliculas y sino exite hacemos una carga inicial
        if os.path.isfile(Servicio_peliculas.NOMBRE_ARCHIVO):
            self.peliculas = self.obtener_peliculas_disco()
        else:
            print("\n** El catalogo de Peliculas esta vacio. Si desea podria añadir una carga inicial **")
            opcion=input("   Crea una carga inicial de 3 peliculas (s=si, cualquiera = No) :")
            
            if opcion.upper()=='S':
                self.carga_inicial_peliculas()    
            
    def agregar_pelicula(self):        # Pelicula es un objeto pelicula
        nombre= input("Nombre de la pelicula :")        # Recibimos por Teclado el nombre de la pelicula
        peli=Pelicula(nombre)                           # Crea el objeto pelicula
        
        self.peliculas.append(peli)                     # Agregamos la pelicula a la Lista en memoria
        
        self.guardar_pelis_archivo([peli])              # Pasamos una lista con un solo elemento
        print(f"\nSe agrego la pelicula {nombre}")
            
    def obtener_peliculas_disco(self):
        pelis=[]
        try:
            with open(self.NOMBRE_ARCHIVO,'r') as archivo:
                for pelicula in archivo:       # En realidad es cada linea ( Cada linea tiene una Pelicula) 
                    # obtenemos una tupla y la desempaquetamos y asignamos a 2 variables que la conforman
                    id_pelicula,nombre=pelicula.strip().split(',')     # Sabemos que cada elemento esta separado con , ( split ) y que hay \n asi que los eleminamos
                    # El precio debe ser tipo flotante y vienen como cadena
                    peli=Pelicula(nombre)     # Creamos un objeto Pelicula con el nombre. No incluimos el id porque lo genera automaticamente la clase Snacks
                    pelis.append(peli)        # Esto añade a la lista pelis
        except Exception as e:
            print("Error, al leer el archivo : {e}")  
        return pelis            
        
    def carga_inicial_peliculas(self):
        pelis_iniciales =['Estrella','Superman', 'Pokemon']     # Lista de peliculas iniciales
        peli_tipo_clase =[]
        for p in pelis_iniciales:
            peli=Pelicula(p)                    #Convierte los nombres en objeto Pelicula , la p=nombre en la lista
            peli_tipo_clase.append(peli)
        
        self.peliculas.extend(peli_tipo_clase)                  # Adiciona en bloque las peliculas iniciales a la lista.
        self.guardar_pelis_archivo(peli_tipo_clase)
        print("\nSe añadio con exito 3 peliculas")
          
    def guardar_pelis_archivo(self, peliculas,modo='a'):   # Trabaja con una lista de snacks
        try:
            with open(self.NOMBRE_ARCHIVO,modo) as archivo:    # Por defecto el modo sera apend ('a')
                for peli in peliculas:
                    # Para meter la info en el archivo usamos el metodo de la clase , escribir_snacks y lo hacemos formato de salto de linea
                    archivo.write(f'{peli.formato_grabar_en_archivo()}\n')   # Ademas de escribir en el archivo al colocar f'' lo imprime
                    
        except Exception as e:
            print(f'Error al guardar en archivo: {e}')
            
    def listar_peliculas(self):
        print("\n***************** Listado de Peliculas *****************")
        if self.peliculas:
            for p in self.peliculas:
                print(p)                            # Deberia llaar al __str__ de la clase Pelicula     
        else:
            print("\n========  Catalgo de Peliculas esta vacio ========")        
            
    import os

    def eliminar_archivo(self):
        """Elimina un archivo si existe, con confirmación."""
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            confirmacion = input(f"¿Estás seguro de que quieres eliminar el archivo '{self.NOMBRE_ARCHIVO}'? (s/n): ")
            if confirmacion.lower() == 's':
                try:
                    os.remove(self.NOMBRE_ARCHIVO)                                      # Eliminamos el archivo del disco
                    self.peliculas.clear()                                              # Borramos el contenido de la Lista en Memoria.
                    print(f"El archivo '{self.NOMBRE_ARCHIVO}' ha sido eliminado.")
                except OSError as e:
                    print(f"Error al eliminar '{self.NOMBRE_ARCHIVO}': {e}")
            else:
                print("Eliminación cancelada.")
        else:
            print(f"El archivo '{self.NOMBRE_ARCHIVO}' no existe.")

                

            