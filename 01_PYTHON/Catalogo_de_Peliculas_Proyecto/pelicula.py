'''CLASE PELICULAS'''


class Pelicula():
    contador_pelicula=0       # atributo de clase. Son atributos que son compartidos y tienen el mismo valor para todas las clases
    
    def __init__(self, nombre):
        Pelicula.contador_pelicula+=1                      #Incrementamos el contador en 1 por cada objeto creado.
        self.id_pelicula=Pelicula.contador_pelicula       # Asignamos el id con el numero de contador.
        self.__nombre_pelicula = nombre 
    
    def get_nombre_peli(self):
        return self.__nombre_pelicula                       # Encapsulada
    
    def set_nombre_peli(self, nombre):
        self.__nombre_pelicula=nombre
    
    
    @classmethod                                          # Esta vinculado solo a la clase Pelicula ( se llama con la clase) 
    def get_contador_peli(cls):                           # cls es el equivalente de self, pero se refiere a la clase.
        return cls.contador_pelicula

    # (No se suele proporcionar un setter directo para el contador si se gestiona internamente)       
    
    def __str__(self):                          # Imprimir elementos de la clase Snacks
        return f'Id_Pelicula: {self.id_pelicula:<12} Nombre: {self.__nombre_pelicula:<30}'
        
    def formato_grabar_en_archivo(self):                         # Metodo para escribir la informacion de l pelicula en el archivo
        return  f'{self.id_pelicula },{self.__nombre_pelicula}'   #Se accesa directo porque estamos dentro de la clase    
    
    
    

        
    
        
        
        
    

