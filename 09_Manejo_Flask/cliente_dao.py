"""
    CLASE DE CLIENTE DAO

    Es la clase que maneja el CRUD de la entidad de datos. Es decir maneja las operaciones
    de C = Create, R= Read ( leer) , U=Update y D=Delete ( Borrar ) elementos de la entidad
    en un modelo. Siendo la entidad y/o modelo un cliente representado por la Clase Cliente.

    Al manejar la entidad en una base de datos tenemos que las sentencias en MySQL seran
    equivalentes a:

    Operacion     MySQL
    C= Create   = INSERT
    R= Read     = SELECT
    U= Update   = UPDATE
    D= Delete   = DELETE

    """
 #"E:\Python\WorkSpace curso Python_HTML_CSS_JavaScript\08_Proyectos_con_MySQL\Proyecto_Zona_Fit_Gym\conexion.py"
# Importamos la Clase Conexion del archivo conexion que se ubica en la carpeta Proyecto_Zona_Fit_Gym.    
from conexion import Conexion 
from clientes import Cliente                        # Importamos la clase Cliente dentro del archivo cliente.py     
#from mysql.connector.cursor import MySQLCursor            #! Para ayudar el autocompletado de elementos cursor y sus metodos
#from mysql.connector.connection import MySQLConnection    #! Para autocompletar código en cursor
    
class ClienteDAO():
    # Variable a cambiar: cliente por el nombre de la tabla que tengamos en la base de datos 
    SELECCIONAR ='SELECT * FROM cliente ORDER BY id'

    SELECCIONAR_ID='SELECT * FROM cliente WHERE id=%s'
    # Variables: cliente por nombre de la tabla y nombre, apellido y membresia por los atributos en modelo cliente
    # NO colocamos el id porque es autoincremental.
    INSERTAR ='INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    # Variables: cliente nombre de la tabla. nombre, apellido, membresia e id son los campos en la tabla y clase Cliente
    ACTUALIZAR ='UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    # Variable cliente y el id
    ELIMINAR='DELETE FROM cliente WHERE id=%s'     
    
    @classmethod
    def seleccionar(cls):       
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()         # Obtenemos una conexion a la base de datos
            cursor=conexion.cursor()                     # Creamos el cursor 
            cursor.execute(cls.SELECCIONAR)              # Ejecutamos la sentencia SELECT ( Recupera todos los clientes) 
            registros=cursor.fetchall()
            # Convertiremos la recuperacion en una lista de clientes
            # Mapeo de la clase-tabla cliente
            clientes =[]    # Creamos la lista vacia para recuperar los clientes.
            for registro in registros:
               #? Creamos objetos Cliente por cada registro con sus 4 atributos: id - 0, nombre:1, Apellido: 2 , membresia:3
               #? registro[0] es el id.....registro[3] es la membresia ( sigue el orden de los campos en el modelo cliente)
               #? Aqui Aplicamos el ORM : Object Relational Maping ( Es la equivalencia de los datos o campos en MySQL a la clase Clientes.)
                cliente=Cliente(registro[0], registro[1],
                               registro[2],registro[3])
                clientes.append(cliente)  # Añadimos el cliente a la lista de cliente.
            return clientes   #! Retorna una lista de todos los clientes     
        except Exception as e:
           print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:   # Si se uso hay que liberar la conexion    
                cursor.close()                                  # Este cursor lo creamos en el try
                Conexion.liberar_conexion(conexion)             # liberar_conexion en un ClassMethod

    @classmethod
    def seleccionar_por_id(cls,id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()  # Obtenemos una conexion a la base de datos
            cursor = conexion.cursor()  # Creamos el cursor
            valores=(id, )
            cursor.execute(cls.SELECCIONAR_ID,valores)  # Ejecutamos la sentencia SELECT ( Recupera todos los clientes)
            registro = cursor.fetchone()
            # Al ser un solo registro no es necesario hacer una lista ni iterar en ella.

            cliente = Cliente(registro[0], registro[1],registro[2], registro[3])
            return cliente  # ! Retorna el cliente
        except Exception as e:
            print(f'Ocurrio un error al seleccionar cliente: {e}')
        finally:
            if conexion is not None:  # Si se uso hay que liberar la conexion
                cursor.close()  # Este cursor lo creamos en el try
                Conexion.liberar_conexion(conexion)  # liberar_conexion en un ClassMethod

    @classmethod
    def insertar(cls,cliente):     # Recibe un objeto cliente
        conexion=None
        try:  
            #! Para que muestre las sugerencias de metodos en cursor hay que importar modulos en conexion.py que tiene la clase Conexion
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            # Creamos la Tupla que se ingresara, que viene del parametro cliente que es un objeto cliente
            # No hace falta el id porqe MySql lo añade automatico, al ser autoincremental en MySql
            valores=(cliente.nombre, cliente.apellido,cliente.membresia)  
            cursor.execute(cls.INSERTAR,valores)    # Para insertar pasamos la sentencia SQL y los valores
            conexion.commit()       #! Asegura la aplicacion de la insercion de valores. El commit es un metodo commit()   .NO HACE NADA SI NO PONEMOS LOS ()
            conexion.com 
            return cursor.rowcount  # Opcional: Devuelve los objetos aadidos a la base de datos ( Que sera 1 porque le mandaremos solo 1 a 1) 
        except Exception as e:
            print(f'Ocurrio un error al adicionar un nuevo cliente: {e}')
        finally:
            if conexion is not None:   # Si se uso hay que liberar la conexion    
                cursor.close()                                  # Este cursor lo creamos en el try
                Conexion.liberar_conexion(conexion)             # liberar_conexion en un ClassMethod
               
    @classmethod
    def actualizar(cls,cliente):                # BASICO: DEBE RECIBIR EL id para localizar el registro
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente.nombre, cliente.apellido,cliente.membresia, cliente.id)    #Los valores deben tener el mismo orden que tienen en la sentencia de MYSQL  
            cursor.execute(cls.ACTUALIZAR,valores)
            conexion.commit()                       # Hay que confirmar la actualizacion
            return cursor.rowcount                  # Indica cuantos objetos se modificaron
        except Exception as e:
            print(f'Ocurrio un error en la actualizacion del registro: {e}')    
        finally:
            if conexion is not None:   # Si se uso hay que liberar la conexion    
                cursor.close()                                  # Este cursor lo creamos en el try
                Conexion.liberar_conexion(conexion)             # liberar_conexion en un ClassMethod             


    @classmethod
    def eliminar(cls,cliente):         # Recibir solo el id del cliente.
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente.id,)                   # Una tupla de un solo elemento, entonces tiene que ser id,
            cursor.execute(cls.ELIMINAR,valores)     
            conexion.commit()
            
            return cursor.rowcount                       
        except Exception as e:
            print(f'Ocurrio un error durante la elimiancion de un cliente: {e}') 
        finally:
            if conexion is not None:   # Si se uso hay que liberar la conexion    
                cursor.close()                                  # Este cursor lo creamos en el try
                Conexion.liberar_conexion(conexion)             # liberar_conexion en un ClassMethod             
       


# Prueba de que esta retornando los clientes

if __name__=='__main__':
    
    
    
    '''  PRUEBAS REALIZADAS
   
    nuevo_Cliente=Cliente(nombre='Federico', apellido='Uribe', membresia=600)
    # no_clientes_insertados= ClienteDAO.insertar(nuevo_Cliente)                  # OJO : Metodo insertar devuelve un valor asi que hay que asignarlo para que corra bien.
    ClienteDAO.insertar(nuevo_Cliente)                  # OJO : Metodo insertar devuelve un valor "return cursor.rowcount" pero NO pasa nada si no recogemos ese valor en una variable pero lo podemos hacer. 
    #print("REGISTROS ADICIONADOS :", no_clientes_insertados)
    
    modificar_cliente=Cliente(nombre='Juan', apellido='Ruiz', membresia=510, id=9)
    # no_clientes_insertados= ClienteDAO.insertar(nuevo_Cliente)                  # OJO : Metodo insertar devuelve un valor asi que hay que asignarlo para que corra bien.
    no_clientes_modificados=ClienteDAO.actualizar(modificar_cliente)                  # OJO : Metodo insertar devuelve un valor "return cursor.rowcount" pero NO pasa nada si no recogemos ese valor en una variable pero lo podemos hacer. 
    print("REGISTROS MODIFICADOS :", no_clientes_modificados)
    
    cliente_eliminar =Cliente(id=2)
    # no_clientes_insertados= ClienteDAO.insertar(nuevo_Cliente)                  # OJO : Metodo insertar devuelve un valor asi que hay que asignarlo para que corra bien.
    no_clientes_eliminados=ClienteDAO.eliminar(cliente_eliminar)                  # OJO : Metodo insertar devuelve un valor "return cursor.rowcount" pero NO pasa nada si no recogemos ese valor en una variable pero lo podemos hacer. 
    print("REGISTROS ELIMINADOS :", no_clientes_eliminados)
    
    
    

    cliente=ClienteDAO.seleccionar_por_id(15)
    print()

    print(cliente)
'''