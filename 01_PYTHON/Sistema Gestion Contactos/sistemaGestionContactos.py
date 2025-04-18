import re                               # Importamos Regular Expresion.

from contactos import Contactos         # Para usar objetos Contactos
from contactos_dao import ContactosDAO  # Para usar los metodos y manejar la base de datos

class SistemaGestionContactos():

    def __init__(self):
        # Creamos instancia de ContactoDAO que trae el archivo a usar y los metodos que gestionan el archivo.
        self.contactos_dao=ContactosDAO()

    def sistema_contactos(self):                        # Activa el ciclo del menu y opciones
        # salir = False
        print("**** Gestion Contactos ****")
        self.contactos_dao.mostrar_contactos()          # Mostramos los contactos existentes en el archivo contactos.txt
        while not salir:
            try:
                opcion = self.mostrar_menu()            # Mostramos el menu
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"Ocurrio un error al salir {e}")

    # Muestra el Menu principal y pide la opcion.
    def mostrar_menu(self):
        print('''\n Menu Sistema Gestion Contactos 
                1. Agregar Contacto.
                2. Mostrar todos.
                3. Buscar un Contacto
                4. Eliminar un Contacto
                5. Salir
                 ''')
        return int(input("Elige una opcion :"))

    # Buscar contactos y simplificar ejecutar_opcion()
    def buscar_contactos(self):
        nombre = input("Nombre o parte de el :")
        lista_encontrados = self.contactos_dao.buscar_contactos_por_cadena(nombre)  # Nombre realmente es una cadena o Nombre
        print(f"{'Nombre':<20}{'Telefono':<15}{'Correo':<25}")
        for contacto in lista_encontrados:
            print(contacto)

    # Segun la opcion elegida activa la logica y metodos a usar
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.agregar_contacto()
        elif opcion == 2:
            self.contactos_dao.mostrar_contactos()
        elif opcion == 3:
           self.buscar_contactos()
        elif opcion == 4:
            nombre=input("Nombre de contacto a eliminar : ")
            print("El nombre introducido fue ", nombre)
            self.contactos_dao.eliminar_contacto_por_nombre(nombre)

            #self.servicio_snacks.eliminar_snacks(id_eliminar)
        elif opcion == 5:
            print('Saliendo...hasta luego')
            return True
        else:
            print(f'Opcion invalida: {opcion}')

    # Incluye los ciclos para validar nombre, telefono y correo
    def agregar_contacto(self):
        while True:
            nombre = input('Nombre del contacto  : ')
            if not self.validar_nombre(nombre):
                print(
                    "Error: El nombre debe comenzar con al menos 3 letras, seguido opcionalmente de más letras, un espacio y dígitos al final.")
                continue  # Volver a pedir el nombre si no es válido

                # Verificar si el nombre ya existe
            contactos_existentes = self.contactos_dao.buscar_contacto_por_nombre(nombre)
            if contactos_existentes:
                print(f"Error: El nombre '{nombre}' ya existe en la lista de contactos. Haz que sea diferente")
            else:
                break  # El nombre es válido y no existe, salir del bucle
        while True:
            telefono = input('Telefono del contacto: ')
            if telefono.isdigit():                  # Aqui se valida que sean solo digitos
                break
            else:
                print("Error: El teléfono debe contener solo dígitos.")

        while True:
            correo = input('Correo del contacto  :')
            if self.validar_correo(correo):
                break
            else:
                print("Error: El correo electrónico tiene un formato inválido.")

        nuevo_contacto = Contactos(nombre, telefono, correo)
        self.contactos_dao.agregar_contacto(nuevo_contacto)
        print('Contacto agregado')

    # Uso de expresion regular para validar el nombre con REGEX
    def validar_nombre(self, nombre):
        # Patrón modificado:
        # - Al menos 3 letras al inicio.
        # - Opcionalmente:
        #   - Más letras.
        #   - Uno o más espacios seguidos de más letras (para nombres compuestos).
        # - Opcionalmente al final:
        #   - Un espacio seguido de uno o más dígitos.
        patron = r"^[a-zA-Z]{3,}([a-zA-Z]+\s*[a-zA-Z]+)*(\s*\d*)?$"
        return re.match(patron, nombre) is not None   # Significa: Si coincide con Patron no es None=True

    # Valida el correo con expresion regular ( REGEX )
    def validar_correo(self, correo):
        # Expresión regular básica para validar el formato del correo
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(patron, correo) is not None


# programa principal
if __name__=='__main__':
    sistema_gestion=SistemaGestionContactos()   # Crea una instancia de la clase SistemaGestionContactos()
    sistema_gestion.sistema_contactos()         # LLama al metodo sistema_contactos que activa el menu dentro de ciclo while