''' CLASE SERVICIO CONTACTOS'''

import os.path
from contactos import Contactos


class ContactosDAO():
    # paso 1: Creamos un nombre de archivo para guardar los Contactos
    NOMBRE_ARCHIVO = 'contactos.txt'  # Una constante. Archivo para los contactos.

    def __init__(self):
        # paso 2: Creamos una lista para guardar los objetos contactos en memoria
        self.contactos = []  # creamos una lista vacia
        # Verificamos si existe el el archivo contactos.txt
        # paso 3: Verificamos si existe el archivo
        # * Si existe el archivo de contactos.txt cargamos los contactos en la lista
        if os.path.isfile(self.NOMBRE_ARCHIVO):  # verifica si existe el archivo
            print(f"El archivo {self.NOMBRE_ARCHIVO} ya existe ")
            self.contactos = self.obtener_contactos()  # * Si existe obtenemos los contactos
        else:  # * Sino existe creamos el archivo
            print(f"El archivo {self.NOMBRE_ARCHIVO} no existe y lo crearemos vacío")
            # Simplemente abrimos el archivo en modo escritura ('w')
            # Esto creará el archivo si no existe y lo dejará vacío.
            with open(self.NOMBRE_ARCHIVO, 'w'):
                pass  # No necesitamos escribir nada en el archivo en este momento

    # Busca un nombre especifico para eliminar. Es llamado por eliminar_contacto_por_nombre(self, nombre_eliminar):
    def buscar_contacto_por_nombre(self,nombre_buscar):
        resultados = [contacto for contacto in self.contactos if contacto.nombre.lower() == nombre_buscar.lower()]
        return resultados

    # Busca una cadena de texto dentro de los contactos ( puede ser una vocal hasta un nombre completo )
    def buscar_contactos_por_cadena(self, cadena_buscar):
        resultados = [
            contacto for contacto in self.contactos
            if cadena_buscar.lower() in contacto.nombre.lower()
        ]
        return resultados

    # LLena la lista de contactos
    def obtener_contactos(self):
        contactos = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    # obtenemos una tupla y la desempaquetamos y asignamos a 3 variables que la conforman
                    nombre, telefono, correo = linea.strip().split(',')  # Sabemos que cada elemento esta separado con , ( split ) y que hay \n asi que los eleminamos
                    # Asumí todos las variables alfanuméricas
                    contacto = Contactos(nombre,telefono, correo)
                    contactos.append(contacto)                      # Añadimos el contacto a la lista contactos
        except Exception as e:
            print("Error, al leer el archivo : {e}")
        return contactos            # devolvemos la lista de contactos

    # Agregamos un contacto nuevo
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)  # agregamos el contacto a nuestra lista de contactos
        self.guardar_contactos_archivo([contacto])  # ! Guardar archivo trabaja con una lista asi que mandamos el contacto envuelto entre []
        pass

    """
    def eliminar_contactos(self, id):  # Recibira el id a eliminar
        print("Recibi el id a eliminar : ", id)
        contactos = self.get_contactos()  # Se trae la losta completa de los contactos en inventario y los guarda en una lista
        # definimos un iterador
        print("Cantidad de contactos en contactos ", len(contactos))
        contacto = next((contacto for contacto in contactos if contacto.id_contacto == id), None)
        if contacto:
            contactos.remove(contacto)
            print(f'contacto encontrado {contacto}')
            self.reasignar_ids(contactos)  # Reasignar IDs  ....Vuelve a reasignar id o contador a los items
            for contacto in contactos:
                print(contacto)
            self.guardar_contactos_archivo(contactos, 'w')  # Lo mando para reescribir.
            self.obtener_contactos()
        else:
            print('\n')
            print("*" * 80)
            print(f'contacto no encontrado con id : {id}')
        return
    """

    # Muestra los contactos en orden alfabetico por el nombre
    def mostrar_contactos(self):
        print("*******     Lista de Contactos     *********")
        # Ordenar la lista de contactos alfabéticamente por nombre antes de mostrar
        contactos_ordenados = sorted(self.contactos, key=lambda contacto: contacto.nombre.lower())
        for contacto in contactos_ordenados:
            print(contacto)

    # Guarda los contactos en el archivo contactos.txt
    def guardar_contactos_archivo(self, contactos, modo='a'):  # Trabaja con una lista de contactos
        try:
            with open(self.NOMBRE_ARCHIVO, modo) as archivo:  # Por defecto el modo sera apend ('a')
                for contacto in contactos:
                    # Para meter la info en el archivo usamos el metodo de la clase , escribir_contactos y lo hacemos formato de salto de linea
                    # escribir_contactos() colocará nombre,telefono,correo y luego le añadimos salto de linea para que el proximo se escriba en la
                    # siguiente linea.
                    archivo.write(f'{contacto.escribir_contactos()}\n')  # Ademas de escribir en el archivo al colocar f'' lo imprime

        except Exception as e:
            print(f'Errpor al guardar en archivo: {e}')

    # Eliminamos un contacto segun su nombre
    def eliminar_contacto_por_nombre(self, nombre_eliminar):
        print('En eliminar contacto por nombre llegó el nombre:', nombre_eliminar)
        contactos_a_eliminar = self.buscar_contacto_por_nombre(nombre_eliminar)  # La cadena puede ser el nombre o una parte de él.
        if contactos_a_eliminar:
            contacto_a_eliminar = contactos_a_eliminar[0]  # Tomamos el primer (y único) resultado
            self.contactos.remove(contacto_a_eliminar)
            self.guardar_contactos_archivo(self.contactos, 'w')  # Sobreescribir el archivo
            print(f"Contacto '{nombre_eliminar}' eliminado.")
        else:
            print(f"No se encontraron contactos con el nombre '{nombre_eliminar}'.")
