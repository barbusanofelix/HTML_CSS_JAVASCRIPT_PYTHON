'''
Sistema de Gestion de Biblioteca
Elaborado por: Felix Concepcion Lopez Barbusano
email        : barbusanofelix@gmail.com
Ver el enunciado de esta practica al final de este archivo

Clase Libro:
Define los atributos titulo, autor, isbn y disponible.
El método __str__ proporciona una representación legible del libro.
Clase Biblioteca:
Utiliza una lista libros para almacenar objetos Libro.
agregar(): Crea un nuevo libro y lo añade a la lista.
prestar(): Busca un libro por ISBN y cambia su estado a prestado.
devolver(): Busca un libro por ISBN y cambia su estado a disponible.
mostrar(): Muestra todos los libros en la biblioteca.
buscar(): Busca un libro por ISBN y lo muestra.
Función menu():
Crea una instancia de Biblioteca.
Muestra un menú interactivo al usuario.
Procesa la opción del usuario y llama a los métodos correspondientes.
Valida la entrada del usuario y maneja errores.
Cómo ejecutar el código:

Guarda el código en un archivo llamado, por ejemplo, biblioteca.py.
Abre una terminal o línea de comandos.
Navega hasta el directorio donde guardaste el archivo.
Ejecuta el comando python biblioteca.py.


'''
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

    def agregar(self, titulo, autor, isbn):
        libro = Libro(titulo, autor, isbn)
        self.libros.append(libro)
        print(f"Libro '{titulo}' agregado a la biblioteca.")

    def prestar(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                if libro.disponible:
                    libro.disponible = False
                    print(f"Libro '{libro.titulo}' prestado.")
                    return
                else:
                    print(f"El libro '{libro.titulo}' ya está prestado.")
                    return
        print("Libro no encontrado.")

    def devolver(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                if not libro.disponible:
                    libro.disponible = True
                    print(f"Libro '{libro.titulo}' devuelto.")
                    return
                else:
                    print(f"El libro '{libro.titulo}' ya está disponible.")
                    return
        print("Libro no encontrado.")

    def mostrar(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(libro)

    def buscar(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                print(libro)
                return
        print("Libro no encontrado.")

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
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            biblioteca.agregar(titulo, autor, isbn)
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
            biblioteca.buscar(isbn)
        elif opcion == 'f':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()





'''
Enunciado de esta practica:

'''