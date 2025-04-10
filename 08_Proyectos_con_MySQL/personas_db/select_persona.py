
'''RECUPERA UNO O VARIOS REGISTROS'''


import mysql.connector

#? Todos los parametros siguientes estan dentro del connect
personas_db = mysql.connector.connect( 
host        ='localhost',    #IP 127.0.0.1      #? Esto aparece en WorkBench   
user        ='root',                            
password    ='admin',                           #? Clave que le dimos al crear MySql ( Aunque le dimos admin / admin , toma root en user) 
database    ='personas_db'                      #! Debe ser igual al nombre de la base de datos en MySQL
)

#? Ejecutar la sentencia SELECT
#? Creamos un objeto cursor 
cursor =personas_db.cursor()     # El objeto persona_db se creo con el conector

#? Ejecutamos la sentencia de consulta mediante el cursor
cursor.execute('SELECT * FROM personas');       #! TERMINA CON ;

#? La consulta la guardamos en la variable resultado
resultado=cursor.fetchall()    # fetchall recupera todo en forma de lista de tuplas

for persona in resultado:
    v1,v2,v3,v4 = persona   # Podemos colocar simplemente print(persona) pero como es una tupla de 4 elementos: id, nombre, apellido y edad la podemos desempaquetar
    print(f'{v1:<10} {v2:<20} {v3:<20} {v4:<10}')
