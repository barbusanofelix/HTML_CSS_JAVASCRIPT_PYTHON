
import mysql.connector

#? Todos los parametros siguientes estan dentro del connect
personas_db = mysql.connector.connect( 
host        ='localhost',    #IP 127.0.0.1      #? Esto aparece en WorkBench   
user        ='root',                            
password    ='admin',                           #? Clave que le dimos al crear MySql ( Aunque le dimos admin / admin , toma root en user) 
database    ='personas_db'                      #! Debe ser igual al nombre de la base de datos en MySQL
)

#? Crea un cursor
cursor = personas_db.cursor()

#? Datos a insertar
nombre = "Pedro"
apellido = "Rufian"
edad = 35

# Define la consulta INSERT INTO.
# No necesitas especificar la columna 'id' si es auto-incrementable.
sql = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)"
val = (nombre, apellido, edad)

try:
    # Ejecuta la consulta
    cursor.execute(sql, val)

    # Confirma los cambios en la base de datos
    personas_db.commit()

    print(cursor.rowcount, "registro insertado.")
    print("El ID generado automáticamente es:", cursor.lastrowid)

except mysql.connector.Error as err:
    print(f"Error al insertar: {err}")

finally:
    # Cierra el cursor y la conexión
  # Cierra el cursor y la conexión
    if cursor:  # Asegúrate de que el cursor se haya creado
        cursor.close()
    if personas_db and personas_db.is_connected():
        personas_db.close()