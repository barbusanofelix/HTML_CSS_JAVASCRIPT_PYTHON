'''
Cada clave representa un atributo de esa persona (nombre, edad, ciudad) y el valor asociado es el valor 
de ese atributo.
¿Cómo representar múltiples personas?
Si quisieras registrar la información de múltiples personas, podrías usar una lista de diccionarios. 
Cada diccionario en la lista representaría a una persona.

Explicación:

personas = [...]: Se crea una lista llamada personas.
{...}: Cada diccionario dentro de la lista representa a una persona.
personas[1]["nombre"]: Se accede al nombre de la segunda persona en la lista.
for persona in personas:: Se itera sobre cada diccionario en la lista.
Esta estructura te permite almacenar y acceder a la información de múltiples personas de manera organizada.

'''
# Iterar sobre la lista de personas para mostrar todos los diccionarios almacenados en la lista
def imprimirPersonas(personas):
    print( "iMPRIMIENDO PERSONAS :")
    for persona in personas:
        print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Ciudad: {persona['ciudad']}")
    print()    

personas = [
    {
        "nombre": "Juan",
        "edad": 43,
        "ciudad": "Madrid"
    },
    {
        "nombre": "Ana",
        "edad": 30,
        "ciudad": "Barcelona"
    },
    {
        "nombre": "Carlos",
        "edad": 25,
        "ciudad": "Valencia"
    },
    {
        "nombre": "Pepe",
        "edad": 28,
        "ciudad": "Barcelona"
    }
]

# Acceder a la información de una persona
print(personas[1]["nombre"])  # Salida: Ana

imprimirPersonas(personas)

# PARA OBTENER LAS PERSONAS QUE VIVEN EN BARCELONA?
for persona in personas:
    if persona["ciudad"] == "Barcelona":
        print(f"La persona que vive en Barcelona es: {persona['nombre']}")
        #break  # Opcional: Detener el bucle después de encontrar la primera persona

# PARA MODIFICAR LA EDAD DE CARLOS QUE TENIA 35 Y QUEREMOS SUSTITUIRLA POR 35
# 
for persona in personas:
    if persona["nombre"] == "Carlos":
        persona["edad"] = 35
        break  # Opcional: Detener el bucle después de modificar la edad de Carlos

# Verificar la modificación
imprimirPersonas(personas)     

# AÑADIR UNA PERSONA
# Crear un nuevo diccionario para la persona a añadir
'''
Explicación:
nueva_persona = {...}: Se crea un nuevo diccionario llamado nueva_persona que contiene la información de la persona que deseas añadir.
personas.append(nueva_persona): Se utiliza el método append() para agregar el diccionario nueva_persona al final de la lista personas.
print(personas): Se imprime la lista personas para verificar que la nueva persona se ha añadido correctamente.
'''
nueva_persona = {
    "nombre": "Laura",
    "edad": 28,
    "ciudad": "Sevilla"
}

# Añadir el diccionario a la lista
personas.append(nueva_persona)

imprimirPersonas(personas)

# ELIMINAR UNA PERSONA
nombre_a_eliminar = "Ana"

for persona in personas[:]:  # Iterar sobre una copia de la lista
    if persona["nombre"] == nombre_a_eliminar:
        personas.remove(persona)
        break  # Opcional: Detener el bucle después de eliminar la persona

# Verificar la lista actualizada
imprimirPersonas(personas)
