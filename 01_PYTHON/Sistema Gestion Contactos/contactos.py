
class Contactos():

    def __init__(self, nombre, telefono, correo):  # Constructor
        self.nombre =nombre
        self.telefono=telefono
        self.correo=correo

    def __str__(self):
        return f'{self.nombre:<20}{self.telefono:<15}{self.correo:<25}'

    # Metodo para escribir la informacion del contacto en el archivo en disco: nombre,telefono, correo
    # Basicamente estamos separando por coma elemento.
    # Este metodo es llamado por def guardar_contactos_archivo de contactos_dao.py por la clase ContactoDAO
    def escribir_contactos(self):
        return f'{self.nombre},{self.telefono},{self.correo}'  # Se accesa directo porque estamos dentro de la clase

