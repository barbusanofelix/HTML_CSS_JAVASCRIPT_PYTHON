class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        if self.buscar_isbn(libro.isbn):
            print(f"Error: El ISBN '{libro.isbn}' ya existe en la biblioteca.")
            return
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def prestar(self, isbn):
        libro = self.buscar_isbn(isbn)
        if libro:
            if libro.disponible:
                libro.disponible = False
                print(f"Libro '{libro.titulo}' prestado.")
            else:
                print(f"El libro '{libro.titulo}' ya está prestado.")
        else:
            print("Libro no encontrado.")

    def devolver(self, isbn):
        libro = self.buscar_isbn(isbn)
        if libro:
            if not libro.disponible:
                libro.disponible = True
                print(f"Libro '{libro.titulo}' devuelto.")
            else:
                print(f"El libro '{libro.titulo}' ya está disponible.")
        else:
            print("Libro no encontrado.")

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
            isbn = input("ISBN: ") #Solicito primero el isbn
            titulo = input("Título: ")
            autor = input("Autor: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregar(libro)
        elif opcion == 'b':
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar(isbn)
        elif opcion == 'c':
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver(isbn)
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