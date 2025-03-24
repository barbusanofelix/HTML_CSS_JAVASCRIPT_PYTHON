import sqlite3
from operator import attrgetter

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"\nEl libro {self.isbn} - '{self.titulo}' de {self.autor} ha sido prestado.")
            return True
        else:
            print(f"\nEl libro {self.isbn} - '{self.titulo}' de {self.autor} YA ESTÁ PRESTADO.")
            return False

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"\nEl libro {self.isbn} - '{self.titulo}' de {self.autor} ha sido devuelto.")
            return True
        else:
            print(f"\nEl libro {self.isbn} - '{self.titulo}' de {self.autor} YA ESTABA DISPONIBLE.")
            return False

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo:<45}  {self.autor:<25}  {self.isbn:<15}  {estado:<15}"

class Biblioteca:
    def __init__(self, db_nombre="biblioteca.db"):
        self.db_nombre = db_nombre
        self.conexion = sqlite3.connect(self.db_nombre)
        self.cursor = self.conexion.cursor()
        self._crear_tabla()
        self.inventario = self._cargar_libros_desde_db()
        self.mostrar()

    def _crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                isbn TEXT PRIMARY KEY,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                disponible INTEGER NOT NULL
            )
        """)
        self.conexion.commit()

    def _cargar_libros_desde_db(self):
        self.cursor.execute("SELECT titulo, autor, isbn, disponible FROM libros")
        rows = self.cursor.fetchall()
        libros = [Libro(titulo, autor, isbn, bool(disponible)) for titulo, autor, isbn, disponible in rows]
        print(f"\nSe cargaron {len(libros)} libros desde la base de datos.")
        return sorted(libros, key=attrgetter("titulo"))

    def _guardar_libro_en_db(self, libro):
        self.cursor.execute("""
            INSERT OR REPLACE INTO libros (titulo, autor, isbn, disponible)
            VALUES (?, ?, ?, ?)
        """, (libro.titulo, libro.autor, libro.isbn, int(libro.disponible)))
        self.conexion.commit()

    def _eliminar_libro_de_db(self, isbn):
        self.cursor.execute("DELETE FROM libros WHERE isbn = ?", (isbn,))
        self.conexion.commit()

    def agregar(self, isbn, titulo=None, autor=None):
        if self.buscar(isbn):
            print(f"Ya existe el libro con ISBN {isbn}.")
            return

        if titulo is None:
            titulo = input("Ingrese el título del libro: ")
        if autor is None:
            autor = input("Ingrese el autor del libro: ")

        nuevo_libro = Libro(titulo, autor, isbn)
        self.inventario.append(nuevo_libro)
        self.inventario.sort(key=attrgetter("titulo"))
        self._guardar_libro_en_db(nuevo_libro)
        self.mostrar(isbn=isbn)

    def buscar(self, isbn):
        for libro in self.inventario:
            if libro.isbn == isbn:
                return libro
        return None

    def prestar(self, isbn):
        libro = self.buscar(isbn)
        if libro:
            if libro.prestar():
                self._guardar_libro_en_db(libro)
        else:
            print(f"No se encontró el libro con ISBN: {isbn}. Verifica el ISBN")

    def devolver(self, isbn):
        libro = self.buscar(isbn)
        if libro:
            if libro.devolver():
                self._guardar_libro_en_db(libro)
        else:
            print(f"No se encontró el libro con ISBN: {isbn}. Verifica el ISBN")

    def mostrar(self, isbn=None):
        if not self.inventario:
            print("NO HAY LIBROS EN LA BIBLIOTECA.")
            return

        if isbn:
            print("\nDatos del libro:")
        else:
            print("\nListado de libros:")

        print(f"\n{'Título':<45}  {'Autor':<25}  {'ISBN':<15}  {'Disponibilidad':<15}\n{'-'*105}")

        if isbn:
            libro = self.buscar(isbn)
            if libro:
                print(libro)
        else:
            for libro in self.inventario:
                print(libro)

    def solicitar_isbn(self, mensaje: str):
        while True:
            isbn = input(mensaje).strip()
            if not isbn:
                print("El ISBN no puede estar vacío.")
                continue
            if len(isbn) <= 13 and isbn.isdigit():
                return isbn
            elif not isbn.isdigit():
                print("El ISBN debe contener <= 13 dígitos")
            else:
                print("El ISBN no puede tener más de 13 dígitos.")

    def cerrar_conexion(self):
        self.conexion.close()
        print("\nConexión a la base de datos cerrada.")

def mostrar_menu():
    b = Biblioteca()

    while True:
        print("\n Menú Sistema de Gestión de Biblioteca:\n")
        print(" 1.  Agregar un nuevo libro")
        print(" 2.  Prestar un libro")
        print(" 3.  Devolver un libro")
        print(" 4.  Mostrar todos los libros")
        print(" 5.  Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            isbn = b.solicitar_isbn("Ingrese el ISBN del libro: ")
            b.agregar(isbn)
        elif opcion == "2":
            isbn = b.solicitar_isbn("Ingrese el ISBN del libro a prestar: ")
            b.prestar(isbn)
        elif opcion == "3":
            isbn = b.solicitar_isbn("Ingrese el ISBN del libro a devolver: ")
            b.devolver(isbn)
        elif opcion == "4":
            b.mostrar()
        elif opcion == "5":
            b.cerrar_conexion()
            print("\n Programa terminado !!!\n")
            break
        else:
            print("\n  Opción inválida. Elija el número de la opcion, entre a 1 a 5. \n")

if __name__ == "__main__":
    mostrar_menu()