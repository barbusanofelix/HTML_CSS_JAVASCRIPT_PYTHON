'''

Version contruida por Felix, con ayuda de Gemini.
Gemini indica que asi es mala practica 
Estás buscando una implementación en la que la lista de libros sea una variable global y toda la lógica de gestión esté dentro 
de la clase Libro. Sin embargo, hay un problema fundamental con esta aproximación:
La clase Libro representa un libro individual. No es lógico que un libro individual gestione una lista de todos los libros. 
La clase Libro debe centrarse en las propiedades y acciones de un solo libro.

Problemas con esta implementación:
Acoplamiento excesivo: La clase Libro depende de una variable global (biblioteca), lo que dificulta la reutilización y el 
mantenimiento del código.
Violación del principio de responsabilidad única: La clase Libro tiene demasiadas responsabilidades (gestionar un solo libro y gestionar 
la lista de todos los libros).
Dificultad para las pruebas: Las variables globales dificultan la escritura de pruebas unitarias.

En resumen:
Aunque técnicamente es posible hacer lo que pides, no es una buena práctica de POO. Es mejor mantener la responsabilidad de gestionar la lista 
de libros en una clase separada (Biblioteca) para tener un código más organizado, mantenible y reutilizable.

'''

biblioteca = [] #lista global

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}"

    def agregar(self):
        if self.buscar_isbn(self.isbn):
            print(f"Error: El ISBN '{self.isbn}' ya existe en la biblioteca.")
            return
        biblioteca.append(self)
        print(f"Libro '{self.titulo}' agregado a la biblioteca.")

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

    @staticmethod
    def mostrar():
        if not biblioteca:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in biblioteca:
                print(libro)

    @staticmethod
    def buscar_isbn(isbn):
        for libro in biblioteca:
            if libro.isbn == isbn:
                return libro
        return None

def menu():
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
            libro.agregar()
        elif opcion == 'b':
            isbn = input("ISBN del libro a prestar: ")
            libro = Libro.buscar_isbn(isbn)
            if libro:
                libro.prestar()
            else:
                print("Libro no encontrado.")
        elif opcion == 'c':
            isbn = input("ISBN del libro a devolver: ")
            libro = Libro.buscar_isbn(isbn)
            if libro:
                libro.devolver()
            else:
                print("Libro no encontrado.")
        elif opcion == 'd':
            Libro.mostrar()
        elif opcion == 'e':
            isbn = input("ISBN del libro a buscar: ")
            libro = Libro.buscar_isbn(isbn)
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