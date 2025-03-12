'''
SISTEMA DE GESTION DE BIBLIOTECA.
Tenemos libros ( representados por la clase Libro, donde sus atributos son titulo, autor, ISBN y disponible ) que forman parte de un inventario 
de una Biblioteca, representado por la clase Biblioteca. 
Dentro de Biblioteca inicializamos una lista (inventario_libros) y la carga con 5 libros para tener una data inicial. 
Atraves del menu y por su puesto de los metodos, de las clases,  podremos agregar, prestar, devolver, buscar y mostrar los libros.
El codigo esta comentado con bastante detalle. 
'''


class Libro:                                                            #* Clase Libro 
    #* Cosntructor.
    def __init__(self, titulo: str, autor: str, isbn: str):
        #* Inicializa un libro con título, autor, ISBN y disponible por defecto.
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True                                          #* Por defecto, cada instancia que se cree, tendrá disponible=True

    def prestar(self):                                                  #* Basicamente cambia el atributo 'disponible' de True -> False.
        # libro que este disponible cambiará su status a disponible = False
        if self.disponible:
            self.disponible = False                                     #* Aqui hace el cambio del atributo 'disponible' de la instancia del libro
            print(f" El libro '{self.isbn} - {self.titulo} - {self.autor}' ha sido prestado.")
        else:       #* Si ya está prestado, pues lo notifica al usuario.
            print(f" El libro '{self.isbn} - {self.titulo} - {self.autor}' YA ESTÁ PRESTADO.")

    def devolver(self):
        #* libro que no este disponible ( prestado ) cambiará su status a disponible = True
        if not self.disponible:
            self.disponible = True                                      #* Aqui hace el cambio del atributo 'disponible' de la instancia del libro
            print(f"El libro '{self.isbn} - {self.titulo} - {self.autor}' ha sido devuelto.")
        else:
            print(f"El libro '{self.isbn} - {self.titulo} - {self.autor}' YA ESTABA DISPONIBLE.")

    def __str__(self):
        """Muestra la información del libro."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo:<35}  {self.autor:<25}  {self.isbn:<6}   {estado:<15}"

# Bibliote es la clase que gestiona la carga de 5 libros al inventario_libros y maneja el inventario de libros
class Biblioteca:
    #* Cosntructor: Inicializa la lista inventario_libros y carga 5 libros en la lista inventario_libros 
    def __init__(self):
        #* Inicializa la biblioteca con una lista inventario_libros vacia ( [] ) que la llenamos con la funcion _cargar_libros_iniciales() 
        self.inventario_libros = []
        self._cargar_libros_iniciales()

    def _cargar_libros_iniciales(self):    
        print("\nCarga automática de 5 libros en el inventario de la Biblioteca\n")     #* Muestra este mensaje en pantalla.
        libros_iniciales = [                                                            #* Es un lista que contiene los strings que llenaran los atributos de los Libros
            ("Cien años de soledad", "Gabriel García Márquez", "12345"),
            ("1984", "George Orwell", "23456"),
            ("El Principito", "Antoine de Saint-Exupéry", "34567"),
            ("Don Quijote de la Mancha", "Miguel de Cervantes", "45678"),
            ("Orgullo y prejuicio", "Jane Austen", "56789"),
        ]

        for titulo, autor, isbn in libros_iniciales:    #* Recorremos la lista inicial para el titulo, autor e ISBN. 
            self.agregar(isbn, titulo, autor)           #* Al llamar el metodo agregar convertiremos la Lista de strings en objetos de la Clase Libro con sus atributos explicitos e implicitos.

    def agregar(self, isbn, titulo=None, autor=None):
        """Agrega un nuevo libro a la biblioteca si el ISBN no existe."""
        if self.buscar(isbn):
            print(f"⚠️ Ya existe un libro con ISBN {isbn} en la biblioteca.")
            return

        if titulo is None:
            titulo = input("Ingrese el título del libro: ")
        if autor is None:
            autor = input("Ingrese el autor del libro: ")

        nuevo_libro = Libro(titulo, autor, isbn)
        self.inventario_libros.append(nuevo_libro)
        #print(f"Libro agregado:\n{nuevo_libro}")
        print(f"{'Título':<35}  {'Autor':<25}  {'ISBN':<7}  {'Disponibilidad':<15}\n{nuevo_libro}")

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
            print(" NO HAY LIBROS EN LA BIBLIOTECA.")
            return
        print("\nListado de libros:")
        for libro in self.inventario_libros:        #* Hace un recorrido libro a libro dentro de la lista de inventario_libros
            print(libro)                            #* El print(libro) llama el metodo def __str__(self): de la clase Libro

#? La función menu() contiene las opcione del programa. 
def menu():
    # Creamos una instancia de la Clase Biblioteca, fuera del ciclo while para que sea accesible a todas las opciones del menu
    biblioteca = Biblioteca()  # Instancia única: biblioteca de la clase Biblioteca.

    while True:      #Ciclo que no dejará de repetirse hasta tomar la opcion 5, es decir Salida
        print("\n Menú Sistema de Gestión de Biblioteca:\n")
        print(" 1.  Agregar un nuevo libro")
        print(" 2.  Prestar un libro")
        print(" 3.  Devolver un libro")
        print(" 4.  Mostrar todos los libros")
        print(" 5.  Salir")
        # Recibimos una opcion por pantalla
        opcion = input("Seleccione una opción: ")

        if opcion == "1":                                   #* Añadir un libro. 
            isbn = input("Ingrese el ISBN del libro: ")     #* Inicalmente pedidmos solo el ISBN para verificar si existe. 
            biblioteca.agregar(isbn)                        #* LLamar metodo agregar() de instancia biblioteca. Si ISBN no existe, pedira Titulo y autor.

        elif opcion == "2":                                 #* Prestar un libro, dando el isbn
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            biblioteca.prestar(isbn)                        #* LLama metodo prestar de instancia biblioteca 

        elif opcion == "3":                                 #* Devolver un libro usando el isbn para localizarlo
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            biblioteca.devolver(isbn)                       #* Llama al metodo devolver de la instancia biblioteca 

        elif opcion == "4":                                 #* Opcion para mostrar todos los libros.
            biblioteca.mostrar()                            #* LLama al metodo Mostrar de la instancia Biblioteca

        elif opcion == "5":                                 #* Salir del Programa
            print("\n Programa terminado !!!\n")
            break                                           #* con break, rompe el ciclo while True y culmina el programa

        else:
            print("\n  Opción inválida. Elija el número de la opcion, entre a 1 a 5. \n")


if __name__ == "__main__":
    menu()
'''
Flujo del programa en cada opción del menú
Cuando se ejecuta menu(), lo primero que hace el programa es:

Crear una única instancia de Biblioteca, la cual:
Inicializa inventario_libros como una lista vacía.
Llama a _cargar_libros_iniciales(), que agrega 5 libros automáticamente.
Después, entra en un bucle donde espera que el usuario seleccione una opción.

Ahora veamos qué sucede en cada opción del menú.

1️⃣ Opción 1: Agregar un nuevo libro
🔹 ¿Qué ve el usuario?
Se le pide que ingrese un ISBN.
Si el ISBN no existe, se le solicita el título y el autor.
Se muestra un mensaje confirmando que el libro ha sido agregado.
🔹 Flujo interno (lo que no es visible)
📌 El usuario elige "1" y el programa llama a biblioteca.agregar(isbn).
🔽
📌 agregar(isbn) busca si el ISBN ya existe llamando a buscar(isbn).
🔽
📌 buscar(isbn) recorre la lista inventario_libros y:

Si encuentra el libro, devuelve el objeto Libro → 🚫 Se muestra un mensaje de que ya existe.
Si no lo encuentra, devuelve None → ✅ Continúa agregando el libro.
🔽
📌 Como el ISBN no existe, agregar() solicita al usuario el título y el autor (si no se proporcionaron).
🔽
📌 Se crea una instancia de Libro:
python
Copiar
Editar
nuevo_libro = Libro(titulo, autor, isbn)
🔽
📌 Se añade a inventario_libros con:

python
Copiar
Editar
self.inventario_libros.append(nuevo_libro)
🔽
📌 Se muestra el mensaje confirmando que el libro ha sido agregado.

2️⃣ Opción 2: Prestar un libro
🔹 ¿Qué ve el usuario?
Se le pide que ingrese un ISBN.
Si el libro está disponible, se le informa que fue prestado.
Si no está disponible, se muestra un mensaje de error.
🔹 Flujo interno (lo que no es visible)
📌 El usuario elige "2" y el programa llama a biblioteca.prestar(isbn).
🔽
📌 prestar(isbn) busca el libro con buscar(isbn).
🔽
📌 buscar(isbn) revisa la lista inventario_libros:

Si encuentra el libro, devuelve su instancia.
Si no lo encuentra, devuelve None.
🔽
📌 Si buscar() encontró el libro, se ejecuta:
python
Copiar
Editar
libro.prestar()
🔽
📌 Dentro de Libro.prestar(), se revisa self.disponible:

Si es True, se cambia a False y se muestra el mensaje ✅.
Si es False, se muestra un mensaje de error ❌.
3️⃣ Opción 3: Devolver un libro
🔹 ¿Qué ve el usuario?
Se le pide que ingrese un ISBN.
Si el libro estaba prestado, se marca como disponible.
Si ya estaba disponible, se muestra un mensaje de advertencia.
🔹 Flujo interno (lo que no es visible)
📌 El usuario elige "3" y el programa llama a biblioteca.devolver(isbn).
🔽
📌 devolver(isbn) busca el libro con buscar(isbn).
🔽
📌 buscar(isbn) recorre inventario_libros:

Si encuentra el libro, devuelve su instancia.
Si no lo encuentra, devuelve None.
🔽
📌 Si el libro existe, se ejecuta:
python
Copiar
Editar
libro.devolver()
🔽
📌 Dentro de Libro.devolver(), se revisa self.disponible:

Si es False, se cambia a True y se muestra el mensaje ✅.
Si ya era True, se muestra el mensaje ⚠️.
4️⃣ Opción 4: Mostrar todos los libros
🔹 ¿Qué ve el usuario?
Se muestra una lista con todos los libros en la biblioteca y su estado (Disponible/Prestado).
Si no hay libros, aparece un mensaje indicando que la biblioteca está vacía.
🔹 Flujo interno (lo que no es visible)
📌 El usuario elige "4" y el programa llama a biblioteca.mostrar().
🔽
📌 mostrar() revisa si inventario_libros está vacío.

Si está vacío, muestra 📭 "No hay libros en la biblioteca".
Si hay libros, recorre inventario_libros y llama a __str__() en cada Libro.
🔽
📌 Libro.__str__() devuelve un string con la información del libro:
python
Copiar
Editar
return f"📖 {self.titulo} - {self.autor} (ISBN: {self.isbn}) - Estado: {estado}"
🔽
📌 Se imprime la lista de libros.

5️⃣ Opción 5: Salir
🔹 ¿Qué ve el usuario?
Se muestra un mensaje "👋 Saliendo del programa. ¡Hasta luego!"
El programa termina.
🔹 Flujo interno (lo que no es visible)
📌 El usuario elige "5", por lo que el while True en menu() se interrumpe con break.
🔽
📌 El programa finaliza.

📌 Punto clave:

inventario_libros es una lista oculta para el usuario, pero siempre se actualiza internamente.
Cada libro es un objeto Libro, y cada acción (prestar, devolver, mostrar) actúa sobre estos objetos.
La herencia ya no es necesaria porque Biblioteca maneja todo el inventario desde su constructor.

'''