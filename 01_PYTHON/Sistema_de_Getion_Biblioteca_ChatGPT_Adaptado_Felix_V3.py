class Libro: 
    def __init__(self, titulo: str, autor: str, isbn: str):
        """Constructor de la clase Libro."""
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  

    def prestar(self):
        """Presta el libro si está disponible."""
        if self.disponible:
            self.disponible = False
            print(f"✅ El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"❌ El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        """Devuelve el libro si estaba prestado."""
        if not self.disponible:
            self.disponible = True
            print(f"✅ El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"⚠️ El libro '{self.titulo}' ya estaba disponible.")

    def __str__(self):
        """Muestra la información del libro."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"📖 {self.titulo} - {self.autor} (ISBN: {self.isbn}) - Estado: {estado}"


class Biblioteca:
    def __init__(self):
        """Inicializa la biblioteca con una lista vacía de libros."""
        self.inventario_libros = []

    def agregar(self, isbn):
        """Agrega un nuevo libro validando que no exista el ISBN."""
        if self.buscar(isbn):
            print("⚠️ Ya existe un libro con este ISBN en la biblioteca.")
            return
        
        # Si el libro no existe, se piden los datos faltantes
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro : ")
        nuevo_libro = Libro(titulo, autor, isbn)
        self.inventario_libros.append(nuevo_libro)
        print(f"📚 Libro agregado:\nISBN: {isbn}\nTítulo: {titulo}\nAutor: {autor}\n")

    def buscar(self, isbn):
        """Busca un libro por ISBN y devuelve el objeto libro o None."""
        for libro in self.inventario_libros:
            if libro.isbn == isbn:
                return libro
        return None

    def prestar(self, isbn):
        """Presta un libro si está disponible."""
        libro = self.buscar(isbn)
        if libro:
            libro.prestar()
        else:
            print("❌ No se encontró un libro con ese ISBN.")

    def devolver(self, isbn):
        """Devuelve un libro si estaba prestado."""
        libro = self.buscar(isbn)
        if libro:
            libro.devolver()
        else:
            print("❌ No se encontró un libro con ese ISBN.")

    def mostrar(self):
        """Muestra todos los libros en la biblioteca."""
        if not self.inventario_libros:
            print("📭 No hay libros en la biblioteca.")
            return
        print("\n📚 Listado de libros:")
        for libro in self.inventario_libros:
            print(libro)

 
def cargar_libros_iniciales(biblioteca):
    """Carga 5 libros famosos en la biblioteca al iniciar el programa."""
    libros_iniciales = [
        ("Cien años de soledad", "Gabriel García Márquez", "12345"),
        ("1984", "George Orwell", "23456"),
        ("El Principito", "Antoine de Saint-Exupéry", "34567"),
        ("Don Quijote de la Mancha", "Miguel de Cervantes", "45678"),
        ("Orgullo y prejuicio", "Jane Austen", "56789"),
    ]
    print("Pedi mostrar la inventario")
    biblioteca.mostrar()
    
    for titulo, autor, isbn in libros_iniciales:
        if not biblioteca.buscar(isbn):  # Asegura que no haya duplicados
            nuevo_libro = Libro(titulo, autor, isbn)
            biblioteca.inventario_libros.append(nuevo_libro)


def menu():
    """Función principal para gestionar la biblioteca desde un menú."""
    biblioteca = Biblioteca()
    cargar_libros_iniciales(biblioteca)  # Carga los 5 libros iniciales
    

    while True:
        print("\n📌 Menú Sistema de Gestión de Biblioteca:")
        print("1️⃣ Agregar un nuevo libro")
        print("2️⃣ Prestar un libro")
        print("3️⃣ Devolver un libro")
        print("4️⃣ Mostrar todos los libros")
        print("5️⃣ Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            isbn = input("Ingrese el ISBN del libro: ")
            biblioteca.agregar(isbn)

        elif opcion == "2":
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            biblioteca.prestar(isbn)

        elif opcion == "3":
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            biblioteca.devolver(isbn)

        elif opcion == "4":
            biblioteca.mostrar()

        elif opcion == "5":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("⚠️ Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
