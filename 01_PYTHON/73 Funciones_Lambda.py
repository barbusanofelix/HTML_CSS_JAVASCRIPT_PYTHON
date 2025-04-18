"""  FUNCIONES LAMBDA  """

"""  Son básicamente funciones anónimas, es decir, no tienen nombre y se usan para funciones cortas, de una linea"""

""" Sintaxis 
    variable= lambda argumentos:expresión 
    """
# Aqui definimos una función lambda
cuadrado= lambda x:x**2
numero=4
print(f'El cuadrado de {numero} es {cuadrado(numero)}')    # para llamar la funcion lambda, igual se pasa un parametro

"""  EJEMPLO DE APLICAR CONVERSION DE VALORES EN UNA LISTA ....SIMILAR A COMPRESION DE LISTA """

numeros= [1,2,3,4]
# con lista de compresion es:
numeros_cuadrado = [ x**2 for x in numeros ]
print(f'Usando Compresion de Lista: Elevar al cuadrado la lista {numeros} y obtenemos {numeros_cuadrado}')

# Usando lambda
numeros_cuad_lambda = list(map(lambda x:x**2,numeros))      # La función map funciona indicando que hacer ( lambda y  y a que se aplica ( numeros )
print(f'Con map aplicamos función lambda sobre la lista de numeros y luego casteamos a list para obtener {numeros_cuad_lambda}')

"""   USO DE FILTER JUNTO CON FUNCION LAMBDA  """
"""   Básicamente de la lista elegir los numeros pares, usando la funcion filter que trabaja similar a maps"""

numeros= [1,2,3,4]          # Tenemos una lista de numeros de los cuales queremos elegir los pares.

numeros_pares = list(filter( lambda x: x%2==0, numeros))
print(f'De la lista de numeros {numeros} los pares son: {numeros_pares}')

'''
CON SORTED ORDENAR UNA LISTA [] FORMADA POR DICCIONARIO {}
'''
personas = [
    {"nombre": "Ana"    ,   "edad": 30},
    {"nombre": "Luis"   ,   "edad": 25},
    {"nombre": "Carlos" ,   "edad": 40}
    ]

ordenadas = sorted(personas, key=lambda p: p["edad"])
print(f'Elementos diccionario ordenados en forma Ascendente de edad')
for persona in ordenadas:
    print(persona)

"""   MISMA LISTA PERO ORDENADA DESCENTE """
personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Carlos", "edad": 40}
]

print(f'\nElementos diccionario ordenados en forma Descendente de edad')
ordenadas_descendente = sorted(personas, key=lambda p: p["edad"], reverse=True)
for persona in ordenadas_descendente:
    print(persona)

"""  MULTIPLICACION DE 2 PARAMETROS CON LAMBDA  """

a=4
b=3

multiplicar= lambda a, b: a*b

print(f'La multiplicación de {a} x {b} = {multiplicar(a,b)}')  # Al ser funcion debe enviarse los parámetros aunque no sea claro