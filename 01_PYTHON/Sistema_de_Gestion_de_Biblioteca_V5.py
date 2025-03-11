class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        if self.buscar_isbn(libro.isbn):
            print(f"Error: El ISBN '{libro.isbn}' ya existe en la biblioteca.")
            return
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def mostrar(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(libro)

    def buscar_isbn(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n--- Menú de la Biblioteca ---")
        print("a) Agregar un libro")
        print("b) Prestar un libro")
        print("c) Devolver un libro")
        print("d) Mostrar todos los libros")
        print("e) Buscar libro por ISBN")
        print("f) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == 'a':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregar(libro)
        elif opcion == 'b':
            isbn = input("ISBN del libro a prestar: ")
            libro = biblioteca.buscar_isbn(isbn)
            if libro:
                libro.prestar()
            else:
                print("Libro no encontrado.")
        elif opcion == 'c':
            isbn = input("ISBN del libro a devolver: ")
            libro = biblioteca.buscar_isbn(isbn)
            if libro:
                libro.devolver()
            else:
                print("Libro no encontrado.")
        elif opcion == 'd':
            biblioteca.mostrar()
        elif opcion == 'e':
            isbn = input("ISBN del libro a buscar: ")
            libro = biblioteca.buscar_isbn(isbn)
            if libro:
                print(libro)
            else:
                print("Libro no encontrado.")
        elif opcion == 'f':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()