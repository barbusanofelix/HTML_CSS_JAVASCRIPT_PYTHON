
'''CLASE SNACKS'''

class Snacks():
    contador_snack=0        #Variable de Clase
    
    def __init__(self,nombre='', precio=0.0 ):
        Snacks.contador_snack+=1                #Incrementamos en 1 el contador.
        # id automatico
        self.id_snack = Snacks.contador_snack   # Cada vez que creemos un Snack se incrementa en 1 el contador y se le asigna al id.
        self.__nombre_snack=nombre              # Aplicamos encapsulamiento colocando los __ antes del nombre de la variable.
        self.__precio_snack=precio
        
    # Getter para el nombre
    def get_nombre(self):
        return self.__nombre_snack

    # Setter para el nombre
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):                       # Verifica que sea un string 
            self.__nombre_snack = nuevo_nombre
        else:
            print("Error: El nombre debe ser una cadena de texto.")

    # Getter para el precio
    def get_precio(self):
        return self.__precio_snack

    # Setter para el precio
    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)):                  # Verifica que sea intero o float 
            if nuevo_precio >= 0:
                self.__precio_snack = float(nuevo_precio)           # Al asignarlo lo hace como float
            else:
                print("Error: El precio no puede ser negativo.")
        else:
            print("Error: El precio debe ser un número.")

    # Getter para el id (normalmente el ID no se modifica)
    def get_id(self):
        return self.id_snack

    # (No se suele proporcionar un setter para el ID si es automático)

    # Getter para el contador de snacks (variable de clase - se accede a través de la clase)
    @classmethod                                            # Esta vinculado solo a la clase Snack ( se llama con la clase) 
    def get_contador_snacks(cls):                           # cls es el equivalente de self pero se refiere a la clase.
        return cls.contador_snack

    # (No se suele proporcionar un setter directo para el contador si se gestiona internamente)
        
        
    
    def __str__(self):                          # Imprimir elementos de la clase Snacks
        return (f'Id_Snack: {self.id_snack:<12} Nombre: {self.__nombre_snack:<15}  Precio: {self.__precio_snack:<8}')
    
    
    def escribir_snacks(self):                         # Metodo para escribir la informacion del Snack en el archivo en disco: id,nombre,precio
        return  f'{self.id_snack },{self.__nombre_snack},{self.__precio_snack}'   #Se accesa directo porque estamos dentro de la clase