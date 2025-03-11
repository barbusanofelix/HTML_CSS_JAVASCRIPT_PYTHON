'''
SISTEMA DE GESTION DE BIBLIOTECA.
Despues del codigo, una explicacion general del programa y entre las lineas los comentarios correspondientes
'''


class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        """Constructor de la clase Libro: Inicializa título, autor, ISBN y estado disponible (True)."""
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  

    def prestar(self):
        """Presta el libro si está disponible, de lo contrario muestra un mensaje."""
        if self.disponible:
            self.disponible = False  # Cambiamos el estado a 'No disponible'
            print(f"✅ El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"❌ El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        """Devuelve el libro si estaba prestado, de lo contrario muestra un mensaje."""
        if not self.disponible:
            self.disponible = True  # Cambiamos el estado a 'Disponible'
            print(f"✅ El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"⚠️ El libro '{self.titulo}' ya estaba disponible.")

    def __str__(self):
        """Devuelve una cadena con la información del libro y su estado."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"📖 {self.titulo} - {self.autor} (ISBN: {self.isbn}) - Estado: {estado}"


class Biblioteca:
    def __init__(self):
        """Inicializa la biblioteca con una lista vacía de libros."""
        self.inventario_libros = []  # Lista donde se almacenarán los libros

    def agregar(self, isbn, titulo=None, autor=None):
        """Agrega un nuevo libro a la biblioteca si el ISBN no existe."""
        if self.buscar(isbn):
            print(f"⚠️ Ya existe un libro con ISBN {isbn} en la biblioteca.")
            return

        # Si el título y autor no fueron dados (caso de entrada manual), solicitarlos al usuario
        if titulo is None:
            titulo = input("Ingrese el título del libro: ")
        if autor is None:
            autor = input("Ingrese el autor del libro: ")

        nuevo_libro = Libro(titulo, autor, isbn)
        self.inventario_libros.append(nuevo_libro)
        print(f"📚 Libro agregado: {nuevo_libro}")

    def buscar(self, isbn):
        """Busca un libro por ISBN y devuelve el objeto libro si existe, sino None."""
        for libro in self.inventario_libros:
            if libro.isbn == isbn:
                return libro
        return None

    def prestar(self, isbn):
        """Presta un libro si existe y está disponible."""
        libro = self.buscar(isbn)
        if libro:
            libro.prestar()
        else:
            print("❌ No se encontró un libro con ese ISBN.")

    def devolver(self, isbn):
        """Devuelve un libro si existe y estaba prestado."""
        libro = self.buscar(isbn)
        if libro:
            libro.devolver()
        else:
            print("❌ No se encontró un libro con ese ISBN.")

    def mostrar(self):
        """Muestra todos los libros en la biblioteca con su estado."""
        if not self.inventario_libros:
            print("📭 No hay libros en la biblioteca.")
            return
        print("\n📚 Listado de libros:")
        for libro in self.inventario_libros:
            print(libro)


class BibliotecaConLibrosIniciales(Biblioteca):
    def __init__(self):
        """Extiende la clase Biblioteca inicializando con libros famosos."""
        super().__init__()  # Llamamos al constructor de Biblioteca

        # Lista de libros iniciales
        libros_iniciales = [
            ("Cien años de soledad", "Gabriel García Márquez", "12345"),
            ("1984", "George Orwell", "23456"),
            ("El Principito", "Antoine de Saint-Exupéry", "34567"),
            ("Don Quijote de la Mancha", "Miguel de Cervantes", "45678"),
            ("Orgullo y prejuicio", "Jane Austen", "56789"),
        ]

        # Agregamos los libros iniciales
        for titulo, autor, isbn in libros_iniciales:
            self.agregar(isbn, titulo, autor)


def menu():
    """Función principal para gestionar la biblioteca mediante un menú."""
    biblioteca = BibliotecaConLibrosIniciales()  # Se cargan automáticamente los libros iniciales
    
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

'''
DETALLE DEL CODIGO
Clase Libro
Representa un libro con sus atributos (titulo, autor, isbn, disponible).
Métodos para prestar, devolver y mostrar su información.

Clase Biblioteca
Contiene la lista inventario_libros, que almacena los libros.

Métodos:
agregar()   : Permite añadir libros verificando que el ISBN no exista.
buscar()    : Busca un libro por ISBN.
prestar()   : Cambia el estado de un libro si está disponible.
devolver()  : Marca un libro como disponible si estaba prestado.
mostrar()   : Muestra todos los libros y su estado.

Clase BibliotecaConLibrosIniciales ()
Hereda de Biblioteca, por lo que tiene todos sus métodos.
Sobrescribe el constructor (__init__) para que, al crearse una instancia, se agreguen automáticamente 5 libros.
Llama self.agregar(isbn, titulo, autor) dentro del for para añadir los libros directamente.

menu()
Crea una instancia de BibliotecaConLibrosIniciales(), Qque hereda de Biblioteca asi que tiene todos sus medos, lo que hace que los 
libros iniciales se carguen automáticamente.
Presenta un menú interactivo que permite al usuario gestionar la biblioteca.

Los libros iniciales se agregan automáticamente
BibliotecaConLibrosIniciales hereda Biblioteca, pero su __init__ añade libros iniciales al inventario al momento de crear la instancia.

Métodos de Biblioteca siguen funcionando en BibliotecaConLibrosIniciales
BibliotecaConLibrosIniciales hereda todos los métodos de Biblioteca, por lo que biblioteca.mostrar(), biblioteca.prestar(isbn), etc., 
siguen funcionando sin problemas.
La lista inventario_libros se gestiona correctamente
inventario_libros sigue perteneciendo a Biblioteca pero se llena desde BibliotecaConLibrosIniciales.

La clase BibliotecaConLibrosIniciales hereda de Biblioteca.

Aunque no se define explícitamente en BibliotecaConLibrosIniciales, la lista inventario_libros sí existe porque fue declarada en Biblioteca.
La instancia de BibliotecaConLibrosIniciales tendrá automáticamente todos los atributos y métodos de Biblioteca.
Cuando se ejecuta este bloque en el __init__ de BibliotecaConLibrosIniciales:

for titulo, autor, isbn in libros_iniciales:
    self.agregar(isbn, titulo, autor)
    
self.agregar(isbn, titulo, autor) llama al método agregar(), que no está definido explícitamente en BibliotecaConLibrosIniciales, pero se 
hereda de Biblioteca. Entonces, el programa busca el método en BibliotecaConLibrosIniciales, no lo encuentra, y sigue buscando en 
Biblioteca, donde sí está definido.

Ejecutando agregar():
def agregar(self, isbn, titulo=None, autor=None):
Se le pasan los valores isbn, titulo, autor desde la llamada en el for, así que no serán None, por lo que el programa no pedirá entrada 
manual del usuario.
Luego, llama a:
if self.buscar(isbn),   para verificar si el ISBN ya existe. Como estamos cargando libros iniciales con ISBN distintos, no entrará en el 
return y continuará.

Creación del libro y almacenamiento:
nuevo_libro = Libro(titulo, autor, isbn)
self.inventario_libros.append(nuevo_libro)

Aquí inventario_libros no está declarado en BibliotecaConLibrosIniciales, pero existe por herencia de Biblioteca.
El libro se añade correctamente a la lista inventario_libros que pertenece a la instancia de BibliotecaConLibrosIniciales.

'''