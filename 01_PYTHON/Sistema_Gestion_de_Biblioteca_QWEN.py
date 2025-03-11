class Libro:
    libros = []  # Lista para almacenar todos los libros

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    @classmethod
    def agregar(cls):
        """Agrega un nuevo libro con los datos ingresados por el usuario."""
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")
        nuevo_libro = cls(titulo, autor, isbn)
        cls.libros.append(nuevo_libro)
        print(f"Libro '{titulo}' agregado exitosamente.")

    def prestar(self):
        """Marca el libro como no disponible si está prestado."""
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        """Marca el libro como disponible si fue devuelto."""
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")

    @classmethod
    def mostrar(cls):
        """Muestra todos los libros con su estado actual."""
        if not cls.libros:
            print("No hay libros registrados.")
        else:
            print("\n--- Lista de Libros ---")
            for libro in cls.libros:
                estado = "Disponible" if libro.disponible else "Prestado"
                print(f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Estado: {estado}")

    @classmethod
    def buscar(cls, isbn):
        """Busca un libro por ISBN y lo muestra. Devuelve el objeto si existe."""
        for libro in cls.libros:
            if libro.isbn == isbn:
                estado = "Disponible" if libro.disponible else "Prestado"
                print("\n--- Libro Encontrado ---")
                print(f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Estado: {estado}")
                return libro
        print(f"\nNo se encontró ningún libro con ISBN '{isbn}'.")
        return None

def main():
    while True:
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar todos los libros")
        print("5. Buscar libro por ISBN")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            Libro.agregar()
        elif opcion == '2':
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            libro = Libro.buscar(isbn)
            if libro:
                libro.prestar()
        elif opcion == '3':
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            libro = Libro.buscar(isbn)
            if libro:
                libro.devolver()
        elif opcion == '4':
            Libro.mostrar()
        elif opcion == '5':
            isbn = input("Ingrese el ISBN del libro a buscar: ")
            Libro.buscar(isbn)
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()