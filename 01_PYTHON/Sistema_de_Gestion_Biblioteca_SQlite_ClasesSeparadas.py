import sqlite3
from operator import attrgetter

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True): 
        #* Atributos de Libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False           #* Presta un libro colocando disponible=False
            print(f"\nEl libro {self.isbn} - '{self.titulo}' de {self.autor} ha sido prestado.")
            return True
        else:
            print(f"\nEl libro {self.isbn} - '{self.titulo}' de {self.autor} YA ESTÁ PRESTADO.")
            return False

    def devolver(self):                         #* Devuelve libro. disponible=True
        if not self.disponible:
            self.disponible = True
            print(f"\nEl libro {self.isbn} - '{self.titulo}' de {self.autor} ha sido devuelto.")
            return True
        else:
            print(f"\nEl libro {self.isbn} - '{self.titulo}' de {self.autor} YA ESTABA DISPONIBLE.")
            return False

    def __str__(self):                          #* Impresion de objeto libro
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo:<45}  {self.autor:<25}  {self.isbn:<15}  {estado:<15}"

class DBase:
    '''
    db_nombre. Define el nombre del archivo que se utilizará para la base de datos SQLite. Tiene un valor por defecto de "biblioteca.db". 
    Sino se especifica el nombre de la base de datos "biblioteca.db". Puedes pasar un nombre diferente al crear la instancia.
    '''
    def __init__(self, db_nombre="biblioteca.db"):  #* Inicializacion instancia.
        #* biblioteca.db la creo en E:\Python\WorkSpace curso Python_HTML_CSS_JavaScript  ( El directorio donde se ubica la carpeta con programas Python)
        self.db_nombre = db_nombre                  #* Nombre de la base de datos...Por defecto es biblioteca.db
        self.conexion = sqlite3.connect(self.db_nombre)     #* Aquí es donde se establece la conexión con la base de datos SQLite.Si existe biblioteca.db la abre y sino la crea.
        #* El objeto de conexión resultante (que representa la conexión a la base de datos) se asigna al atributo de la instancia self.conexion. 
        #* A través de este objeto self.conexion, podrás interactuar con la base de datos (realizar consultas, guardar, borrar...)
        self.cursor = self.conexion.cursor()
        #* Para ejecutar comandos SQL (como crear tablas, insertar datos, seleccionar datos), necesitas un objeto "cursor".
        #* self.conexion.cursor(): El método cursor() del objeto de conexión (self.conexion) crea y devuelve un objeto cursor.
        #* Este objeto cursor (self.cursor) se asigna al atributo de la instancia self.cursor. Utilizarás este cursor para enviar y recibir datos de la base de datos.
        self._crear_tabla()    #* LLama al metodo, de esta clase, _crear_tabla()
        '''
        El prefijo _ en el nombre del método (_crear_tabla) es una convención en Python para indicar que este es un método "interno" o "protegido" de la clase, 
        lo que sugiere que no debería ser llamado directamente desde fuera de la clase (aunque técnicamente se puede).
        El propósito de este método es asegurar que la tabla libros,  necesaria para almacenar la información de los libros, exista en la base de datos. 
        Si la tabla ya existe, no se hará nada. Si no existe, se creará con las columnas definidas (isbn, titulo, autor, disponible).
        '''

    def _crear_tabla(self):         #* Crea la tabla libros dentro de biblioteca.db ( si existe no pasa nada y sino la crea) 
        #* self.cursor es el self.cursos creado en la inicializacion de la clase . Aplicará el comando execute.
        #* self.cursor.execute usa comentario de varias lineas '''    ***      ''' para la isntruccion SQL
        self.cursor.execute("""     
            CREATE TABLE IF NOT EXISTS libros (
                isbn TEXT PRIMARY KEY,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                disponible INTEGER NOT NULL
            )
        """)
        '''
        CREATE TABLE: Esta es la instrucción SQL para crear una nueva tabla en la base de datos.
        IF NOT EXISTS libros: verifica si ya existe una tabla llamada libros. Si ya existe, la instrucción CREATE TABLE se ignora.
        ( ... ): Dentro de los paréntesis se definen las columnas de la tabla libros y sus propiedades:
        isbn TEXT PRIMARY KEY: Define una columna llamada isbn. TEXT: Especifica que esta columna será texto. PRIMARY KEY: será la clave primaria de la tabla. 
        Una clave primaria debe contener valores únicos y no nulos.
        titulo TEXT NOT NULL: Define una columna titulo. TEXT: será texto. NOT NULL: no puede contener valores nulos.
        autor TEXT NOT NULL: Igual que titulo.
        disponible INTEGER NOT NULL: Define una columna llamada disponible. INTEGER: Especifica que será un número entero. Se utilizará para almacenar el estado de disponibilidad
        del libro (por ejemplo, 1 para True/disponible y 0 para False/prestado). NOT NULL: no puede tener valores nulos
        '''
        self.conexion.commit()
        '''
        self.conexion: Es el objeto de conexión a la base de datos. 
        .commit(): El método commit() guarda todos los cambios realizados en la base de datos desde la última llamada a commit(). 
        En este caso, guarda la creación de la tabla (si se realizó). Es crucial llamar a commit() después de ejecutar instrucciones 
        que modifican la estructura o los datos de la base de datos (como CREATE TABLE, INSERT, UPDATE, DELETE). Si no se llama a commit(), 
        los cambios podrían no guardarse permanentemente en el archivo de la base de datos.
        '''

        #* Este método tiene como objetivo leer todos los registros de la tabla libros en la base de datos SQLite y convertirlos en una lista de objetos de la clase Libro.
        '''
        Define un método llamado cargar_libros dentro de la clase DBase. El parámetro self permite acceder a los atributos de la instancia de DBase (como self.cursor).
        '''
    def cargar_libros(self):
        #* Es el objeto cursor asociado a la conexión de la base de datos. Este método ejecuta una consulta SQL en la base de datos.
        #* Después de ejecutar esta consulta, el cursor contendrá el resultado de la selección (si hubo alguno).
        self.cursor.execute("SELECT titulo, autor, isbn, disponible FROM libros")
        '''
        fetchall(): Este método recupera todas las filas del resultado de la última consulta ejecutada por el cursor. Cada fila se devuelve como una tupla, 
        donde los elementos de la tupla corresponden a las columnas seleccionadas en la consulta SELECT (en el mismo orden). La variable rows se convierte 
        en una lista de estas tuplas. Si la tabla libros está vacía, rows será una lista vacía ([])
        '''
        rows = self.cursor.fetchall()
        '''
        Esta línea utiliza una list comprehension para crear y devolver una nueva lista de objetos Libro. 
        for titulo, autor, isbn, disponible in rows: Itera sobre cada tupla (row) en la lista rows. En cada iteración, desempaqueta los elementos de la tupla 
        en las variables titulo, autor, isbn, y disponible. El orden de estas variables debe coincidir con el orden de las columnas en la consulta SELECT.
        Libro(titulo, autor, isbn, bool(disponible)): Para cada tupla, se crea una nueva instancia de la clase Libro, pasando los valores desempaquetados 
        como argumentos al constructor de la clase Libro.
        Es importante notar el uso de bool(disponible). La columna disponible en la base de datos se almacena como un entero (0 o 1). Aquí, se convierte 
        explícitamente a un valor booleano (True o False) antes de pasarlo al constructor de Libro, que se espera que reciba un booleano para el estado de 
        disponibilidad.
        [...]: Los corchetes indican que se está construyendo una nueva lista. La list comprehension crea un nuevo objeto Libro para cada fila recuperada 
        de la base de datos y los añade a esta nueva lista.
        return: Finalmente, el método devuelve esta lista recién creada de objetos Libro.
        '''
        return [Libro(titulo, autor, isbn, bool(disponible)) for titulo, autor, isbn, disponible in rows]

    def guardar_libro(self, libro):     #* Este método tiene como objetivo guardar la información de un objeto Libro en la tabla libros de la base de datos SQLite
        '''
        self: Permite acceder a los atributos de la instancia de DBase (como self.cursor y self.conexion).
        libro: Este es el parámetro que espera recibir el método. Se supone que será un objeto de la clase Libro cuya información se desea guardar en la base de datos.
        
        self.cursor: El objeto cursor asociado a la conexión de la base de datos.
        Este método ejecuta una consulta SQL parametrizada en la base de datos.
        """ ... """: Define la sentencia SQL:
        INSERT OR REPLACE INTO libros (titulo, autor, isbn, disponible): Esta es la instrucción SQL para insertar un nuevo registro en la tabla libros o reemplazar un 
        registro existente.
        INSERT OR REPLACE INTO libros: Indica que se va a insertar un nuevo registro. Si ya existe un registro con la misma clave primaria (en este caso, isbn), ese 
        registro será eliminado y el nuevo registro será insertado.
        (titulo, autor, isbn, disponible): Especifica las columnas de la tabla en las que se van a insertar los valores. El orden de estas columnas es importante y debe coincidir con el orden de los valores proporcionados.
        VALUES (?, ?, ?, ?): Especifica los valores que se van a insertar en las columnas. Los signos de interrogación (?) son marcadores de posición (placeholders). 
        Estos placeholders se sustituirán por los valores reales que se pasan como segundo argumento al método execute(). Esto es una práctica segura para evitar la 
        inyección de código SQL.
        (libro.titulo, libro.autor, libro.isbn, int(libro.disponible)): Este es el segundo argumento del método execute(), que es una tupla que contiene los valores 
        que se van a sustituir por los placeholders en la sentencia SQL.
        libro.titulo: Se toma el valor del atributo titulo del objeto libro que se pasó al método.
        libro.autor: Se toma el valor del atributo autor del objeto libro.
        libro.isbn: Se toma el valor del atributo isbn del objeto libro. Dado que isbn está definido como PRIMARY KEY, SQLite utilizará este valor para determinar si ya 
        existe un registro con el mismo ISBN.
        int(libro.disponible): Se toma el valor del atributo booleano disponible del objeto libro y se convierte a un entero (1 para True, 0 para False). 
        Esto es necesario porque la columna disponible en la tabla se definió como INTEGER.
        '''
        self.cursor.execute("""
            INSERT OR REPLACE INTO libros (titulo, autor, isbn, disponible)
            VALUES (?, ?, ?, ?)
        """, (libro.titulo, libro.autor, libro.isbn, int(libro.disponible)))
        self.conexion.commit()

    def eliminar_libro(self, isbn):   #* objetivo eliminar un registro de la tabla libros en la base de datos SQLite, utilizando el ISBN del libro como criterio de eliminación.
        '''
        def eliminar_libro(self, isbn):: Define un método llamado eliminar_libro dentro de la clase DBase.
        self: Permite acceder a los atributos de la instancia de DBase (como self.cursor y self.conexion).
        isbn: Este es el parámetro que espera recibir el método. Se supone que será el ISBN (como una cadena) del libro que se desea eliminar de la base de datos.
        self.cursor.execute("DELETE FROM libros WHERE isbn = ?", (isbn,)):

        self.cursor: El objeto cursor asociado a la conexión de la base de datos.
        .execute("DELETE FROM libros WHERE isbn = ?", (isbn,)): Este método ejecuta una consulta SQL parametrizada en la base de datos.
        "DELETE FROM libros WHERE isbn = ?": Define la sentencia SQL:
        DELETE FROM libros: Esta es la instrucción SQL para eliminar registros de la tabla libros.
        WHERE isbn = ?: Esta es la cláusula WHERE que especifica la condición para eliminar registros. Solo se eliminarán los registros donde el valor de la columna 
        isbn coincida con el valor proporcionado como parámetro.
        ?: Este es un marcador de posición (placeholder) que se sustituirá por el valor del ISBN. Esto es una práctica segura para evitar la inyección de código SQL.
        (isbn,): Este es el segundo argumento del método execute(), que es una tupla que contiene el valor que se va a sustituir por el placeholder en la sentencia SQL.
        isbn: Se toma el valor del parámetro isbn que se pasó al método. Es importante notar que se coloca una coma después de isbn ((isbn,)) para indicar que es una 
        tupla de un solo elemento. Esto es necesario porque el método execute() espera recibir los valores como una tupla, incluso si solo hay un valor.
        self.conexion.commit():

        self.conexion: El objeto de conexión a la base de datos.
        .commit(): Guarda los cambios realizados en la base de datos desde la última llamada a commit(). En este caso, guarda la eliminación del registro del libro. Es fundamental llamar a commit() después de ejecutar instrucciones que modifican los datos de la base de datos para que los cambios se guarden permanentemente en el archivo.
        '''
        
        self.cursor.execute("DELETE FROM libros WHERE isbn = ?", (isbn,))
        self.conexion.commit()

    def cerrar_conexion(self):   #* objetivo cerrar la conexión a la base de datos SQLite y proporcionar un mensaje de confirmación al usuario.
        '''
        self.conexion: Es el objeto de conexión a la base de datos que se creó durante la inicialización de la clase DBase.
        .close(): El método close() del objeto de conexión cierra la conexión a la base de datos. Esto es importante para liberar los recursos que la conexión estaba 
        utilizando y para asegurarse de que todos los cambios pendientes se guarden correctamente en el archivo de la base de datos.
        Es una buena práctica cerrar explícitamente las conexiones a la base de datos cuando ya no se necesitan, ya que dejar conexiones abiertas innecesariamente puede 
        consumir recursos y, en algunos casos, causar problemas.
        '''
        self.conexion.close()
        print("\nConexión a la base de datos cerrada.")

class Biblioteca:
    def __init__(self, db_manager=None):
        if db_manager is None:
            self.db_manager = DBase()
        else:
            self.db_manager = db_manager
        self.inventario = self.db_manager.cargar_libros()
        self.mostrar()

    def agregar(self, isbn, titulo=None, autor=None):
        if self.buscar(isbn):
            print(f"Ya existe el libro con ISBN {isbn}.")
            return

        if titulo is None:
            titulo = input("Ingrese el título del libro: ")
        if autor is None:
            autor = input("Ingrese el autor del libro: ")

        nuevo_libro = Libro(titulo, autor, isbn)
        self.inventario.append(nuevo_libro)
        self.inventario.sort(key=attrgetter("titulo"))
        self.db_manager.guardar_libro(nuevo_libro)
        self.mostrar(isbn=isbn)

    def buscar(self, isbn):
        for libro in self.inventario:
            if libro.isbn == isbn:
                return libro
        return None

    def prestar(self, isbn):
        libro = self.buscar(isbn)
        if libro:
            if libro.prestar():
                self.db_manager.guardar_libro(libro)
        else:
            print(f"No se encontró el libro con ISBN: {isbn}. Verifica el ISBN")

    def devolver(self, isbn):
        libro = self.buscar(isbn)
        if libro:
            if libro.devolver():
                self.db_manager.guardar_libro(libro)
        else:
            print(f"No se encontró el libro con ISBN: {isbn}. Verifica el ISBN")

    def mostrar(self, isbn=None):
        if not self.inventario:
            print("NO HAY LIBROS EN LA BIBLIOTECA.")
            return

        if isbn:
            print("\nDatos del libro:")
        else:
            print("\nListado de libros:")

        print(f"\n{'Título':<45}  {'Autor':<25}  {'ISBN':<15}  {'Disponibilidad':<15}\n{'-'*105}")

        if isbn:
            libro = self.buscar(isbn)
            if libro:
                print(libro)
        else:
            for libro in self.inventario:
                print(libro)

    def solicitar_isbn(self, mensaje: str):
        while True:
            isbn = input(mensaje).strip()
            if not isbn:
                print("El ISBN no puede estar vacío.")
                continue
            if len(isbn) <= 13 and isbn.isdigit():
                return isbn
            elif not isbn.isdigit():
                print("El ISBN debe contener <= 13 dígitos")
            else:
                print("El ISBN no puede tener más de 13 dígitos.")

    def cerrar_conexion(self):
        self.db_manager.cerrar_conexion()

def mostrar_menu():
    db_manager = DBase()
    b = Biblioteca(db_manager)

    while True:
        print("\n Menú Sistema de Gestión de Biblioteca:\n")
        print(" 1.  Agregar un nuevo libro")
        print(" 2.  Prestar un libro")
        print(" 3.  Devolver un libro")
        print(" 4.  Mostrar todos los libros")
        print(" 5.  Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            isbn = b.solicitar_isbn("Ingrese el ISBN del libro: ")
            b.agregar(isbn)
        elif opcion == "2":
            isbn = b.solicitar_isbn("Ingrese el ISBN del libro a prestar: ")
            b.prestar(isbn)
        elif opcion == "3":
            isbn = b.solicitar_isbn("Ingrese el ISBN del libro a devolver: ")
            b.devolver(isbn)
        elif opcion == "4":
            b.mostrar()
        elif opcion == "5":
            b.cerrar_conexion()
            print("\n Programa terminado !!!\n")
            break
        else:
            print("\n  Opción inválida. Elija el número de la opcion, entre a 1 a 5. \n")

if __name__ == "__main__":
    mostrar_menu()