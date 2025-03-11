'''
Desarrollado junto al ChapGPT

Al final el enunciado y eexplicacion del programa.
'''


class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        # Metodo Constructor de la clase Libro:
        # Al crear un libro se inicializa  con título, autor, isbn y disponible Truw,  por defecto.
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  

    def prestar(self):
        # Metodo prestar(). Si el libro está disponible, cambiamos el atributo disponible a False
        # de lo contrario, muestra un mensaje
        if self.disponible:
            self.disponible = False                 # Aqui cambiamos el atributo de la clase a False
            print(f"✅ El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"❌ El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        """Devuelve el libro si estaba prestado, de lo contrario, muestra un mensaje"""
        if not self.disponible:
            self.disponible = True
            print(f"✅ El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"⚠️ El libro '{self.titulo}' ya estaba disponible.")

    def __str__(self):
        """Muestra la información del libro"""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"📖 {self.titulo} - {self.autor} (ISBN: {self.isbn}) - Estado: {estado}"


class Biblioteca:
    def __init__(self):
        """Inicializa la biblioteca con una lista vacía de libros"""
        # Inicializamos la lista que contiene el inventario de libros que se hara al crear una instancia
        # de Biblioteca, y tendremos una unica lista pues crearemos solo una instancia de Biblioteca
        self.inventario_libros = []

    def agregar(self, isbn):
        """Agrega un nuevo libro a la biblioteca"""
        if self.buscar(isbn):  #Antes de agregar verificamos si ya existe el libro
            print("⚠️ Ya existe un libro con este ISBN en la biblioteca.")
            return
        # Si el libro no existe pedimos los datos que faltan (titulo y autor)
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro : ")
        nuevo_libro = Libro(titulo, autor, isbn)
        self.inventario_libros.append(nuevo_libro)
        print(f"📚 Libro '\nISBN    : {isbn}\nTitulo : {titulo}\nAutor   :{autor}'\n FUE AGREGADO!!!\n")

    def buscar(self, isbn):
        """Busca un libro por ISBN y devuelve el objeto libro o None"""
        for libro in self.inventario_libros:     # Libro es Lista de libros
            if libro.isbn == isbn:
                return libro
        return None

    def pestrar(self, isbn):
        """Presta un libro si está disponible"""
        libro = self.buscar(isbn)
        if libro:
            libro.prestar()
        else:
            print("❌ No se encontró un libro con ese ISBN.")

    def devolver(self, isbn):
        """Devuelve un libro si estaba prestado"""
        libro = self.buscar(isbn)
        if libro:
            libro.devolver()
        else:
            print("❌ No se encontró un libro con ese ISBN.")

    def mostrar(self):
        """Muestra todos los libros en la biblioteca"""
        if not self.inventario_libros:
            print("📭 No hay libros en la biblioteca.")
            return
        print("\n📚 Listado de libros:")
        for libro in self.inventario_libros:
            print(libro)

'''    
def cargar_libros_iniciales(biblioteca):
    """Carga 5 libros famosos en la biblioteca al iniciar el programa."""
    
    libros_iniciales = [
        ("Cien años de soledad", "Gabriel García Márquez", "12345"),
        ("1984", "George Orwell", "23456"),
        ("El Principito", "Antoine de Saint-Exupéry", "34567"),
        ("Don Quijote de la Mancha", "Miguel de Cervantes", "45678"),
        ("Orgullo y prejuicio", "Jane Austen", "56789"),
    ]

    for titulo, autor, isbn in libros_iniciales:
        biblioteca.agregar(titulo, autor, isbn)
'''

def menu():
    """Función principal para gestionar la biblioteca desde un menú"""
    # Hacemos una unica instancia de Biblioteca pues en ella llevamos el inventario 
       
    biblioteca =Biblioteca()    # carga 5 libreos para iniciar el inventario de libros. El usuario puede añadir mas libros.
    #cargar_libros_iniciales(biblioteca) 
    
    while True:
        print("\n📌 Menú Sistema de Gestion de Biblioteca:")
        print("1️⃣ Agregar un nuevo libro")
        print("2️⃣ Prestar un libro")
        print("3️⃣ Devolver un libro")
        print("4️⃣ Mostrar todos los libros")
        print("5️⃣ Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
          # titulo = input("Ingrese el título del libro: ")
          # autor = input("Ingrese el autor del libro: ")
            isbn =input("Ingrese el ISBN del libro: ")
            biblioteca.agregar(isbn)        #Original : biblioteca.agregar_libro(titulo, autor, isbn)

        elif opcion == "2":
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            biblioteca.pestrar(isbn)

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
    menu


'''
ENUNCIADO:
Debes crear un programa en Python que permita registrar libros y gestionar préstamos a usuarios. El programa debe cumplir con los siguientes
requisitos:

1. Clase Libro:
• Crea una clase Libro con los atributos titulo (str), autor (str), isbn (str) y disponible (bool, inicialmente True).
• Incluye un método agregar() que permita introducir un nuevo libro con sus características.
• Incluye un método prestar() que cambie el estado de disponible a False si el libro está disponible, y muestre un mensaje si ya está prestado.
• Incluye un método devolver() que cambie el estado de disponible a True si estaba prestado, y muestre un mensaje si ya estaba disponible.
• Incluye un método mostrar() que devuelva una lista con todos los libros de la biblioteca y los muestre en pantalla con todos sus datos
y diga si estás disponible o no.
• Incluye un método buscar() que busque un libro en concreto por su ISBM y lo muestre en pantalla con todos sus datos y diga si está
disponible o no.

2. Gestión del inventario:
• Usa una lista para almacenar objetos de la clase Libro.
• Implementa un bucle que permita al usuario interactuar con el programa mediante un menú con las siguientes opciones:
• a) Agregar un nuevo libro ingresando título, autor e ISBN.
• b) Prestar un libro buscando por ISBN.
• c) Devolver un libro buscando por ISBN.
• d) Mostrar todos los libros y su estado (disponible o no).
• e) Salir del programa.
3. Condiciones:
• Valida que el ISBN ingresado exista en la lista antes de prestar o devolver un libro.
• Si el usuario ingresa una opción inválida en el menú, muestra un mensaje de error y vuelve a pedir una opción.

Entregable:

• Un script en Python que implemente todas las funcionalidades descritas.
• El código debe ser claro, con comentarios explicativos y usando buenas prácticas

Que se podria hacer para cumplir el enunciado? ( interpreto que todos los metodos nombrados deben ir en la clase Libro)

SOLUCION PLANTEADA:
• Arriba el codigo.

1️⃣ Organización del Código
Encapsulación: Todos los métodos relacionados con un libro deben ir dentro de la clase Libro.
Gestión del Inventario: Para manejar la lista de libros y la interacción del usuario, podrías usar una clase separada Biblioteca, 
lo que mejora la separación de responsabilidades.
Uso de Métodos de Clase o Estáticos: Métodos que afectan a la colección de libros pueden estar en Biblioteca, no en Libro.
2️⃣ Buenas Prácticas Específicas
✅ Métodos bien estructurados
Cada método debe hacer solo lo que le corresponde (ejemplo: prestar() solo cambia el estado del libro).
✅ Mensajes de error y validaciones
Siempre verificar si un ISBN existe antes de prestar o devolver un libro.
✅ Evitar código repetitivo
Por ejemplo, un método buscar() en Biblioteca podría evitar búsquedas repetidas en varios métodos.
✅ Separación de interfaz y lógica de negocio
El menú de usuario debe estar separado de la lógica de la biblioteca.

✅ Aplicación de Buenas Prácticas
Encapsulación
La clase Libro maneja solo sus atributos y comportamiento individual.
La clase Biblioteca gestiona el inventario y las operaciones generales.

Separación de responsabilidades
Libro solo define el comportamiento de los libros.
Biblioteca gestiona la colección de libros.
menu() se encarga de la interacción con el usuario.
Validaciones adecuadas

Se verifica si el ISBN ya existe antes de agregar un libro.
Se valida que el ISBN exista antes de prestar o devolver un libro.

Uso de Métodos de Apoyo
buscar() evita repetir el mismo código de búsqueda en diferentes partes del programa.

Interfaz de Usuario Clara
Mensajes informativos para el usuario con emojis para mayor claridad.
🎯 Conclusión
Siguiendo este diseño, el programa cumple con el enunciado y sigue buenas prácticas de programación. Además, es fácil de mantener y 
ampliar en el futuro. 🚀

'''