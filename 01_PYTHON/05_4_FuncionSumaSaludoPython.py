#Declaramos las funciones suma y SaludoPython
# Ambas reciben 2 parametros
def suma(a,b):   # funcion con return
    return a+b


def saludoPython(cadena1, cadena2):  # funcion sin return
    print(cadena1+" "+cadena2)
   
x=suma(2,3)

print("La suma de 2 + 3 es:",x) # Igual aqui se pudo escribir suma(2,3) y no la x

# Aqui devuelve None porque la funcion no tiene return.
# Va, ejecuta la funcion , la cual escribe en pantalla, me gusta Python y 
# como tal saludoPython("Me gusta","Python") representa el None por no tener return
print("Quiero declarar que ",saludoPython("Me gusta","Python")) #saludisPython no tiene return
