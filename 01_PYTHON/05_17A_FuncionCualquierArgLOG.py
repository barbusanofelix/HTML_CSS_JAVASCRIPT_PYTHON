'''
1.Crea una función log que acepte cualquier número de argumentos y los imprima 
por pantalla en una misma línea. La línea debe empezar con el prefijo ‘LOG: ’.

2.Modifica la función log para que usuario pueda especificar cualquier prefijo 
que desee.

3.Modifica la función log para que el prefijo tenga el valor por defecto ‘LOG: ’.

4.Modifica la función log para que el usuario pueda establecer tanto prefijo 
como separador entre argumentos. Ambos deben pasarse sólo por los nombres 
(no por posición) ‘sep’ y ‘prefix’. No hace falta que estos tengan valor 
por defecto.

5.Modfica la función log para que ahora ‘sep’ y ‘prefix’ tengan un valor por 
defecto.
Modifica la función log para que acepte el siguiente diccionario: España - Madrid, Venezuela - Caracas, Colombia - Bogota. Recuerda que hay que pasarlo
desempaquetándolo con la sintaxis de doble asterisco (**).
'''

#1.
def log1(*arg): #El * significa que puede recibir n argumentos / arg: Puede ser cualquier nombre
    """
    Imprime los argumentos en una misma línea, con el prefijo 'LOG: '.
    *args: Cualquier número de argumentos.
    """
    print("LOG:", *arg)

# -------------------------------------------------------------
def log2(prefijo, *args):
    """
    Imprime los argumentos en una misma linea, con el prefijo especificado.
    prefijo (str): El prefijo que se añadirá a la línea de salida.
    *args: Cualquier número de argumentos.
    """
    print(prefijo, *args)

def log3(prefijo, *args): 
    """
    Imprime los argumentos en una misma linea, con el prefijo especificado o LOG por defecto.
    prefijo (str)="LOG:": El prefijo que se añadirá a la línea de salida, usando el recibido o LOG:.
    *args: Cualquier número de argumentos.
    """
    if prefijo=="":
        prefijo="LOG:"
    print(prefijo, *args)

def log4(prefijo,separador, *args): 
    """
    Imprime los argumentos en una misma linea, con el prefijo especificado o LOG por defecto.
    prefijo (str)="LOG:": El prefijo que se añadirá a la línea de salida, usando el recibido o LOG:.
    *args: Cualquier número de argumentos.
    """
    if prefijo=="":
        prefijo="LOG:"    # por defecto: LOG:
    if separador=="":
        separador=" - "     # Por defecto " - "  guion    
    print(prefijo, *args, sep=separador)    


   
print()
print("Funcion que acepte n argumentos y los imprima en linea. Debe empezar LOG: ")
print()
print("Ejemplo de uso con 5 argumentos")
log1("x", "y", "z", "m", "r")
print()
# Ejemplo de uso con diferentes tipos de argumentos
print("Ejemplo de uso con 4 argumentos")
log1(1, "hola", 3.14, True)
print()
# Ejemplo de uso sin argumentos
print("Ejemplo de uso sin argumentos")
log1()
print()
print("Funcion con prefijo definido por usuario y n Argumentos")
# Ejemplo de uso con prefijo personalizado
log2("AVISO:", "Se ha producido un error critico.")
# Ejemplo de uso con diferentes tipos de argumentos
log2("DEBUG:", 1, "hola", 3.14, True)
# Ejemplo de uso sin argumentos adicionales
log2("INFO:") 
log2("LOG:", 1,2,3)

print()
print("caso 3:")
print("Funcion con prefijo definido por usuario o LOG por defecto y n Argumentos")
# Ejemplo de uso con prefijo personalizado
log3("AVISO:", "Se ha producido un error critico.")
# Ejemplo de uso con diferentes tipos de argumentos
log3(1, "hola", 3.14, True)
# Ejemplo de uso sin argumentos adicionales
log3("INFO:") 
log3("",1,2,3,6,7)

print()
print()
print("caso 4:")
print("Funcion con prefijo por defecto LOG o separador por defecto  -  ")
# Ejemplo de uso con prefijo personalizado
log4("AVISO:", " -- ", "Se ha producido un error critico.")
# Ejemplo de uso con diferentes tipos de argumentos
log4(""," / ", 1, "hola", 3.14, True)
# Ejemplo de uso sin argumentos adicionales
log4("INFO:", " + ") 
log4("","",1,2,3,6,7)
