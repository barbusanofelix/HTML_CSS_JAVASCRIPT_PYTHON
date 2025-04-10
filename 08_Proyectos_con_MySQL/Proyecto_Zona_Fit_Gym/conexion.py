'''CONEXION A LA BASE DE DATOS MANEJANDO CONCEPTO DE  POOL CONEXION'''

#! Para lograr el auto-completado en las clases que usen la clase Conexion el chat GPT sugiere :
from mysql.connector import pooling
from mysql.connector.connection import MySQLConnection as MySQLConnectionType


#from mysql.connector import pooling  # Comente esta importacion porque arriba ya esta :  from mysql.connector import pooling, MySQLConnection
from mysql.connector import Error

class Conexion:
    
    DATABASE    ='zona_fit_db'
    USERNAME    ='root'
    PASSWORD    ='admin'
    DB_PORT     ='3306'
    HOST        ='localhost'
    POOL_SIZE   = 5
    POOL_NAME   ='zona_fit_pool'
    pool        = None
    
        
    @classmethod
    def obtener_pool(cls):      #? Con cls se accede a las contantes o variables de clase
        # Para usar el pool necesitaremos importar "from mysql.connector import pooling"  
        if cls.pool is None:    #? Creamos el objeto Pool ( No se ha usado )
            try:
                cls.pool =pooling.MySQLConnectionPool(
                    pool_name   =cls.POOL_NAME,
                    pool_size   =cls.POOL_SIZE,
                    host        =cls.HOST,
                    port        =cls.DB_PORT,
                    database    =cls.DATABASE,
                    user        =cls.USERNAME,
                    password    =cls.PASSWORD
                )
                return cls.pool     #? Despues de crearlo lo retornamos
                
            except Error as e:      #? Error lo importamos "from mysql.connector import Error"
                print(f'Ocurrio un error al obtener pool: {e}')      
        else:
            return cls.pool         #? Ya existe y retornamos el cls.pool que se inicializó
        
        #! Una cosa es el objeto pool y otra el objeto de conexion del pool hacia la base de datos.
        
    @classmethod   #! AQUí LA CLAVE PARA QUE EL AUTOCOMPLETADO DE código funcione con cursor en la class ClienteDAO:  ( Commit, execute, rowcount.....)
    def obtener_conexion(cls)-> MySQLConnectionType:   #! Se agrega -> MySQLConnectionType: para mejorar el autocompletado de codigo. antes solo era def obtener_conexion(cls): 
        return cls.obtener_pool().get_connection()
    
    @classmethod
    def liberar_conexion(cls,conexion):
        conexion.close()
            
if __name__=='__main__':
    pool =Conexion.obtener_pool()
    print(pool)
    conexion1=pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print("Se ha liberado la conexion1")
                