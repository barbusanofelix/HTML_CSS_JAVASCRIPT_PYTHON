'''ACTUALIZAR UN REGISTRO '''

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

'''
# Datos a modificar
registro_id = 18
nuevo_apellido = "Galfaro"
'''

# Datos para la modificación
apellido_a_reemplazar = "Garcia"
nuevo_apellido = "Rodriguez"

'''
# Define la consulta UPDATE
sql = "UPDATE personas SET apellido = %s WHERE id = %s"
val = (nuevo_apellido, registro_id)
'''

# Define la consulta UPDATE utilizando la columna 'apellido' en la cláusula WHERE
sql = "UPDATE personas SET apellido = %s WHERE apellido = %s"
val = (nuevo_apellido, apellido_a_reemplazar)


try:
    # Ejecuta la consulta
    cursor.execute(sql, val)

    # Confirma los cambios en la base de datos
    personas_db.commit()

    print(cursor.rowcount, "registro(s) actualizado(s).")

except mysql.connector.Error as err:
    print(f"Error al actualizar: {err}")

finally:
    # Cierra el cursor y la conexión
    if cursor:
        cursor.close()
    if personas_db and personas_db.is_connected():
        personas_db.close()