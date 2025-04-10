''' CLASE SERVICIO SNACKS'''



import os.path
from snacks import Snacks



class ServicioSnacks():
    #paso 1: Creamos un nombre de archivo para guardar los Snacks
    NOMBRE_ARCHIVO='snacks.txt'                 # Una constante.
        
    
    def __init__(self):
        #paso 2: Creamos una lista para guardar los objetos en memoria
        self.snacks=[]                          # creamos una lista vacia 
        #Verificamos si existe el el archivo Snacks.txt
        #paso 3: Verificamos si existe el archivo 
        #* Si existe el archivo de snacks.txt cargamos los Snacks en la lista 
        if os.path.isfile(self.NOMBRE_ARCHIVO):         # verifica si existe el archivo
            print(f"El archivo {self.NOMBRE_ARCHIVO} ya existe ")
            self.snacks=self.obtener_Snacks()           #* Si existe obtenemos los snacks 
        else:                                           #* Sino existe cargamos algunos Snacks iniciales
            print(f"El archivo {self.NOMBRE_ARCHIVO} no existe y lo crearemos")
            self.cargar_snacks_iniciales()
            
      
    def cargar_snacks_iniciales(self):                  # Sino usas el self estas jodido
        snacks_iniciales=[
            Snacks('Papas',70),
            Snacks('Refresco',50),
            Snacks('Sandwich',120)
        ]
        self.snacks.extend(snacks_iniciales)            # Con esto se carga la lista de snacks con los snacks iniciales. Objetos class Snacks
        self.guardar_snacks_archivo(snacks_iniciales)   # mandamos a guardar los snacks iniciales en el archivo snacks.txt
    def obtener_Snacks(self):
        snacks=[]
        try:
            with open(self.NOMBRE_ARCHIVO,'r') as archivo:
                for linea in archivo:
                    # obtenemos una tupla y la desempaquetamos y asignamos a 3 variables que la conforman
                    id_snack,nombre,precio=linea.strip().split(',')     # Sabemos que cada elemento esta separado con , ( split ) y que hay \n asi que los eleminamos
                    # El precio debe ser tipo flotante y vienen como cadena
                    snack=Snacks(nombre,float(precio))     # No incluimos el id porque lo genera automaticamente la clase Snacks
                    snacks.append(snack)
        except Exception as e:
            print("Error, al leer el archivo : {e}")  
        return snacks      
        
    
    
    def agregar_snack(self,snack):
        self.snacks.append(snack)   # agregamos el snack a nuestra lista de snacks
        self.guardar_snacks_archivo([snack])  #! Guardar archivo trabaja con una lista asi que mandamos el snack envuelto entre []
        pass
    
    def eliminar_snacks(self,id):  # Recibira el id a eliminar
        print("Recibi el id a eliminar : ", id)
        snacks = self.get_snacks()   # Se trae la losta completa de los snacks en inventario y los guarda en una lista
        # definimos un iterador 
        print("Cantidad de snacks en snacks ", len(snacks))
        snack = next((snack for snack in snacks if snack.id_snack == id),None)
        if snack:
            snacks.remove(snack)
            print(f'Snack encontrado {snack}')
            self.reasignar_ids(snacks)  # Reasignar IDs  ....Vuelve a reasignar id o contador a los items
            for snack in snacks:
                print(snack)
            self.guardar_snacks_archivo(snacks,'w')  # Lo mando para reescribir.
            self.obtener_Snacks()  
        else:
            print('\n')
            print("*"*80)
            print(f'Snack no encontrado con id : {id}')   
        return
    
    def reasignar_ids(self, snacks):                                    #Despues de eliminar un id se reasignan los otros.
        Snacks.contador_snack = 0  # Reiniciar el contador de IDs
        for snack in snacks:
            Snacks.contador_snack += 1
            snack.id_snack = Snacks.contador_snack
        self.snacks = snacks  # Actualizar la lista interna
    
    def mostrar_snacks(self):  # Metodo que muestra todos los snacks en el inventario
        # Muestra los snacks que estan en memoria que en son los mismos que estan en el archivo.
        print("*******  inventario de Snacks *********")
        for snack in self.snacks:
            print(snack)             # al ser snack una objeto de la clase Snacks llama el metodo __str__ de Snacks
    
    def guardar_snacks_archivo(self, snacks,modo='a'):   # Trabaja con una lista de snacks
        try:
            with open(self.NOMBRE_ARCHIVO,modo) as archivo:    # Por defecto el modo sera apend ('a')
                for snack in snacks:
                    # Para meter la info en el archivo usamos el metodo de la clase , escribir_snacks y lo hacemos formato de salto de linea
                    archivo.write(f'{snack.escribir_snacks()}\n')   # Ademas de escribir en el archivo al colocar f'' lo imprime
                    
        except Exception as e:
            print(f'Errpor al guardar en archivo: {e}')
        
    def get_snacks(self):           # Realmente esto recupera la lista de memoria.
        return self.snacks
    
    
    
