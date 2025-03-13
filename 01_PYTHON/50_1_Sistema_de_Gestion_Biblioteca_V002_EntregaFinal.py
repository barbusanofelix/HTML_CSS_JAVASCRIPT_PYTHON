'''
SISTEMA DE GESTION DE BIBLIOTECA.
Tenemos libros ( representados por la clase Libro, donde sus atributos son titulo, autor, ISBN y disponible ) que forman parte de un inventario 
de una Biblioteca, representado por la clase Biblioteca. 
Dentro de Biblioteca inicializamos una lista (inventario_libros) y se hace la carga con 5 libros para tener una data inicial. 
    inventario_libros es una lista oculta para el usuario, pero siempre se actualiza internamente.
    Cada libro es un objeto Libro, y cada acción (prestar, devolver, mostrar) actúa sobre estos objetos.
    
El codigo esta comentado con bastante detalle y al final del codigo hay un comentario macro del menu()
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
        #* libro que este disponible ( disponible=True) cambiará su status a disponible = False ( Prestado)
        if self.disponible:
            #* Aqui ocurre un hecho clave: Python, al guardar la lista inventario_libros, por ser objetos mutables, lo que hace es guardar la referencia a dichos objetos, asi que al cambiar los atributos en la memoria 
            #* la referencia a ese objeto es cambiada y por tanto la referencia del objeto en la lista tambien cambia y NO es necesario hacer un cambio explicito en el objeto de la lista inventario_libros.
            self.disponible = False                                     #* La instancia del libro es un objeto mutable y al cambiar en memoria el atributo disponible tambien lo hace en la lista inventario_libros.
            print(f"\nEl libro '{self.isbn} - {self.titulo} - {self.autor}' ha sido prestado.")  #* Imprime un mensaje al prestar el libro, con los datos del libro.
        else:       #* Si ya está prestado, pues lo notifica al usuario.
            print(f"\nEl libro '{self.isbn} - {self.titulo} - {self.autor}' YA ESTÁ PRESTADO.")  

    def devolver(self):
        #* libro que no este disponible ( disponible=False -> prestado ) cambiará su status a disponible = True
        #* Ver el comentario en prestar(): El atributo se cambia en memoria y al hacerlo tambien se cambia en el elemento en la lista.
        if not self.disponible:                                         #* Si disponible es False
            self.disponible = True                                      #* Aqui hace el cambio del atributo 'disponible' de la instancia del libro
            print(f"\nEl libro '{self.isbn} - {self.titulo} - {self.autor}' ha sido devuelto.")       #* Imprime mensaje de confirmacion.
        else:
            print(f"\nEl libro '{self.isbn} - {self.titulo} - {self.autor}' YA ESTABA DISPONIBLE.")   #* Se intento devolver un libro que ya habia sido devuelto.

    def __str__(self):                  #* Este metodo se ejecuta cada vez que hacemos un print en el cual hay un objeto Libro ( Una instancia de clase Libro)
        #* Muestra la información de un libro: Su titulo, Autor, ISBN y si esta disponible ó NO.
        if self.disponible:             #* Traducimos el disponible=True o False a que muestre "Disponible" o "Prestado"
            estado="Disponible" 
        else:
            estado="Prestado"    
        return f"{self.titulo:<45}  {self.autor:<25}  {self.isbn:<15}  {estado:<15}"  #* Imprime los atributos de un objeto Libro.

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
            ("Guerra y Paz", "Lev Tolstoi", "23456"),
            ("Las Aventuras de Sherlock Holmes", "Arthur Conan Doyle", "34567"),
            ("Don Quijote de la Mancha", "Miguel de Cervantes", "45678"),
            ("La vuelta al mundo en ochenta días", "Julio Verne", "56789"),
        ]

        for titulo, autor, isbn in libros_iniciales:    #* Recorremos la lista inicial para el titulo, autor e ISBN. 
            self.agregar(isbn, titulo, autor)           #* Al llamar el metodo agregar convertiremos la Lista de strings en objetos de la Clase Libro con sus atributos explicitos e implicitos.
        
        
    def agregar(self, isbn, titulo=None, autor=None):   #* En la carga inicial: titulo y autor no son None, asi que llegan valores de tutulo y autor
        #* Agrega un nuevo libro a la lista inventario_libros, si el ISBN no existe.
        libro_buscado=self.buscar(isbn)                 #* Verificamos si el libro existe. Guardamos el libro_buscado
        if libro_buscado:                               #* Si el libro_buscado existe libro_buscado es True (ya existe) y mostrará un mensaje.
            print(f"Ya existe el libro con ISBN {isbn} y es: {libro_buscado.titulo} De:{libro_buscado.autor}")
            return                                      #* Termina la funcion regresando al origen que la llamo
        if titulo is None:                              #* Si no existe un libro con el isbn que llego como parametro significa que hay que añadir el libro. 
            titulo = input("Ingrese el título del libro: ") #* Suministrar tuitulo
        if autor is None:
            autor = input("Ingrese el autor del libro: ")   #* Suminstrar autor

        nuevo_libro = Libro(titulo, autor, isbn)        #* Creamos instancia de Clase Libro en nuevo_libro
        self.inventario_libros.append(nuevo_libro)      #* Agregamos objetos Libro (nuevo_libro) a la lista inventario_libros. Implicitamente cada Libro tendra el atributo disponible=True.  
        #* En el siguiente print, al colocar {nuevo_libro}, que es un objeto Libro , llamará automaticamente la función __str__ de la clase Libro.        
        print(f"\n{'Título':<45}  {'Autor':<25}  {'ISBN':<15}  {'Disponibilidad':<15}\n{"-"*105} \n{nuevo_libro}")    #* Imprime la info de cada Libro. 

    def buscar(self, isbn):
        #* Busca un libro por ISBN y devuelve el objeto libro o None
        for libro in self.inventario_libros:            #* Recorre, libro a libro, la lista inventario_libros (Que tiene objetos Libro)
            if libro.isbn == isbn:                      #* Verifica si el ISBN, del libro en la lista , es igual al isbn recibido. 
                return libro                            #* Al encontrar el libro en la lista inventario_libros retorna el objeto Libro encntrado
        return None                                     #* Si no encuentra el Libro con el isbn proporcionado retorna None.

    def prestar(self, isbn):
        #* Presta un libro si está disponible.
        libro = self.buscar(isbn)   #* Para prestar un libro, este debe existir en el inventario_libros asi que lo buscamos.
        if libro:                   #* Si libro fue encontrado ( libro contiene los datos del libro y "libro:" es True )
            libro.prestar()         #* Para modificar el atributo "disponible" a False, llamamos el metodo prestar() de Clase Libro
        else:
            print(f"No se encontró el libro con ISBN: {isbn}. Verifica el ISBN")    #* libro=None -> No existe un libro con el ISBN suministrado

    def devolver(self, isbn):
        #* Devuelve un libro si estaba prestado ( atributo disponible=False)
        libro = self.buscar(isbn)   #* Para devolver un libro, este debe existir en el inventario_libros, asi que lo buscamos.
        if libro:                   #* Si libro fue encontrado ( libro contiene los datos del libro y "libro:" es True  y sino libro=None)
            libro.devolver()        #* Para modificar el atributo "disponible" a True, llamamos el metodo devolver() de Clase Libro
        else:
            print(f"No se encontró el libro con ISBN: {isbn}. Verifica el ISBN")    #* libro=None -> No existe un libro con el ISBN suministrado

    def mostrar(self):
        #* Muestra todos los libros en la biblioteca, almacenados en la lista inventrio_libros.
        if not self.inventario_libros:
            print(" NO HAY LIBROS EN LA BIBLIOTECA.")   #* Mensaje si inventario_libros esta vacio
            return                                      #* Retorna despues del print
        print("\nListado de libros:")                   #* Imprime el titulo "Listado de Libros".   
        print(f"\n{'Título':<45}  {'Autor':<25}  {'ISBN':<15}  {'Disponibilidad':<15}\n{"-"*105}")  #* Imprime los encabezado y linea de separacion {"-"*100} 
        for libro in self.inventario_libros:        #* Hace un recorrido libro a libro dentro de la lista de inventario_libros
            print(libro)                            #* El print(libro) llama el metodo def __str__(self): de la clase Libro.

#? La función menu() contiene las opcione del programa. 
def menu():
    #* Creamos una instancia de la Clase Biblioteca, fuera del ciclo while para que sea accesible a todas las opciones del menu
    biblioteca = Biblioteca()  #* Instancia única: biblioteca de la clase Biblioteca.

    while True:      #* Ciclo que no dejará de repetirse hasta tomar la opcion 5, es decir Salida
        print("\n Menú Sistema de Gestión de Biblioteca:\n")
        print(" 1.  Agregar un nuevo libro")
        print(" 2.  Prestar un libro")
        print(" 3.  Devolver un libro")
        print(" 4.  Mostrar todos los libros")
        print(" 5.  Salir")
        #* Recibimos una opcion por pantalla
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

        else:                                               #* Al no introducir 1, 2, 3, 4 ó 5, imprime el mensaje y repite el ciclo.
            print("\n  Opción inválida. Elija el número de la opcion, entre a 1 a 5. \n")




#* AQUI EL CORAZON DEL PROGRAMA: PUNTO DE ENTRADA.
if __name__ == "__main__":      #* Controla el punto de entrada del Programa. Como este programa es el scrpt principal el name es main.
    menu()                      #* Ejecuta la funcion menu(), que controla todo el flujo del programa



'''
Flujo del programa en cada opción del menú
Cuando se ejecuta menu(), lo primero que hace el programa es:

Crear una única instancia de Biblioteca, la cual:
Inicializa inventario_libros como una lista vacía.
Llama a _cargar_libros_iniciales(), que agrega 5 libros automáticamente.
Después, entra en un bucle donde espera que el usuario seleccione una opción.

Veamos qué sucede en cada opción del menú.

Opción 1: Agregar un nuevo libro
Se pide al usuario que ingrese un ISBN.
El programa llama el metodo biblioteca.agregar(isbn): 
    agregar(isbn) busca si el ISBN ya existe llamando a buscar(isbn).
        buscar(isbn) recorre la lista inventario_libros y:
            Si encuentra el libro, devuelve el objeto Libro → Se muestra un mensaje de que ya existe.
            Si no lo encuentra, devuelve None → Continúa agregando el libro. Se le solicita el título y el autor.
                Se crea una instancia de Libro:nuevo_libro = Libro(titulo, autor, isbn). 
                Se añade el libro a la lista: self.inventario_libros.append(nuevo_libro)            
                Se muestra un mensaje confirmando que el libro ha sido agregado al inventario. 

Opción 2: Prestar un libro
Se pide al usuario que ingrese un ISBN.
El programa llama a biblioteca.prestar(isbn)
    prestar(isbn) busca el libro con buscar(isbn).
        buscar(isbn) revisa la lista inventario_libros: Si no lo encuentra, devuelve None.
            Si encuentra el libro, devuelve su instancia. 
                Se llama a libro.prestar() (De la clase Libro)
                    Dentro de Libro.prestar(), se revisa self.disponible:
                        Si es True, se cambia a False y se muestra el mensaje indicando que el libro ha sido prestado.
                        Si es False, se muestra un mensaje de error, que indica que el libro ya esta prestado.
                 
Opción 3: Devolver un libro
Se pide al usuario que ingrese un ISBN.
El programa llama a biblioteca.devolver(isbn)
    devolver(isbn) busca el libro con buscar(isbn).
        buscar(isbn) recorre inventario_libros: Si no lo encuentra, devuelve None.
            Si encuentra el libro, devuelve su instancia.
                Se llama a libro.devolver()
                    Dentro de Libro.devolver(), se revisa self.disponible:
                        Si es False, se cambia a True y se muestra el mensaje 
                        Si ya era True, se muestra el mensaje
                        Si el libro estaba prestado, se marca como disponible y un mensaje de que el libro ha sido devuelto.
                        Si ya estaba disponible, se muestra un mensaje de advertencia, indicando que ya estaba disponible.

Opción 4: Mostrar todos los libros (Se muestra una lista con todos los libros en la biblioteca y su estado (Disponible/Prestado).
El programa llama a biblioteca.mostrar()
    mostrar() revisa si inventario_libros está vacío
        Si está vacío el inventario, muestra  un mensaje "No hay libros en la biblioteca".
        Si hay libros, recorre inventario_libros y llama a __str__() en cada Libro.
            Libro.__str__() devuelve un string con la información del libro y es imprimida.

Opción 5: Salir
El while True en menu() se interrumpe con break
    El programa finaliza.

'''