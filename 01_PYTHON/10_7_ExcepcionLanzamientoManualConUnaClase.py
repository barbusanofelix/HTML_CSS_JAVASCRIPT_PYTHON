'''
Que hace el pass en la clase? ....solo evita que no este vacia y de error, al no ejecutar nada?

Sí, tu comprensión del uso de pass en una clase es correcta. La declaración pass en Python se utiliza como un marcador de 
posición cuando se requiere sintácticamente una declaración, pero no se necesita ejecutar ninguna acción. En el contexto de 
una clase, pass se utiliza para:

Evitar errores de sintaxis:
En Python, un bloque de código (como una clase, función o bucle) no puede estar vacío. Si intentas definir una clase sin ningún contenido, 
obtendrás un error de sintaxis. pass se utiliza para proporcionar un cuerpo vacío válido para la clase, evitando este error.
Crear clases vacías o marcadores de posición:
A veces, puedes querer definir una clase sin implementar su funcionalidad de inmediato. pass te permite crear la clase y posponer la 
implementación para más tarde. Esto es útil durante el desarrollo, cuando estás diseñando la estructura de tu código.

'''


class IndiceFueraDeRangoError(Exception):
    pass

def iterador(objeto, indice):
    return objeto[indice]

def error(ite, longEntrada):
    if ite > (longEntrada - 1):
        raise IndiceFueraDeRangoError("Índice fuera de rango")
    else:
        return False

entrada = input("Suministra un nombre: ")
ite = int(input(f"Suministra un indice para obtener el caracter de {entrada}: "))

longEntrada = len(entrada)

try:
    if not error(ite, longEntrada):
        c = iterador(entrada, ite)
        print(c)
except IndiceFueraDeRangoError as e:
    print(f"Indice muy grande: {e}")
except IndexError:
    print("Error de indice interno")
except ValueError:
        print("Debes introducir un número entero como indice.")
except Exception as e:
    print(f"Ocurrio un error inesperado: {e}")