"""
EXPLICACIÓN DE LISTAS POR COMPRESIÓN

Es una forma de crear listas a través de expresiones en una sola linea

LA SINTAXIS ES:
variable_tipo_lista = [expresión for elemento in iterable if condición]

Notar: Que esta envuelta entre [ ]

expresión: Es la operación o transformación que se aplica a cada elemento. El resultado de esta expresión se convierte
en un elemento de la nueva lista.
for elemento in iterable: Es el bucle que itera sobre cada elemento del iterable (por ejemplo, otra lista, una cadena,
un rango, etc.).
if condición (opcional): Es un filtro. Solo los elementos que cumplan esta condición serán procesados por la expresión
e incluidos en la nueva lista.

"""
""" COMPRESIÓN DE LISTA DE RANGE DE 1 A 10"""
lista_numeros_1_a_10= [ x for x in range(1,11)]

print(lista_numeros_1_a_10)         # salida [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

""" COMPRESIÓN DE LISTA DE RANGE DE 1 A 10, SOLO NUMEROS PARES"""
lista_numeros_1_a_10_pares= [ x for x in range(1,11) if x%2==0]
print(lista_numeros_1_a_10_pares)         # salida [2, 4, 6, 8, 10]

""" COMPRESIÓN DE LISTA DE RANGE DE 1 A 10, SOLO NUMEROS IMPARES"""
lista_numeros_1_a_10_impares= [ x for x in range(1,11) if not x%2==0]
print(lista_numeros_1_a_10_impares)         # salida [1, 3, 5, 7, 9]

""" COMPRESIÓN DE LISTA DE RANGE DE 1 A 10, DEL CUADRADO DE CADA NUMERO"""
lista_cuadrados_numeros_1_a_10= [x**2 for x in range(1,11)]
print("Cuadrados de numeros de 1 a 10, de range(1,11): ", lista_cuadrados_numeros_1_a_10)

""" COMPRESIÓN DE LISTA DEL CUADRADO DE NUMEROS DEL 1 AL 10  ORIGINADO DE UNA LISTA"""

numeros=[1,2,3,4,5,6,7,8,9,10]
lista_cuadrados_numeros=[numero**2 for numero in numeros]    # El nombre de la variable puede ser cualquiera , pero si coincidir "numero**2 for numero" ó "x**2 for x"
print("Cuadros de numeros en una lista del 1 al 10    :", lista_cuadrados_numeros)

""" CREAR UNA LISTA CON LAS INICIALES DE NOMBRES QUE ESTÁN UNA LISTA"""
nombres = ["Ana", "Benito", "Carlos", "Diana"]
iniciales = [nombre[0] for nombre in nombres]           # Obtenemos las iniciales referenciando la posición 0 de cada nombre.
print("Teniendo la lista : ", nombres, " sus iniciales son :", iniciales)  # Output: ['A', 'B', 'C', 'D']

""" CREAR UNA LISTA CON LAS LETRA FINAL DE NOMBRES QUE ESTÁN UNA LISTA"""
nombres = ["Ana", "Benito", "Carlos", "Diana"]
iniciales = [nombre[len(nombre)-1] for nombre in nombres]           # Obtenemos la última letra sabiendo que su índice es la longitud-1
print("Teniendo la lista : ", nombres, " sus iniciales son :", iniciales)  # Output: ['A', 'B', 'C', 'D']

""" 

LISTAS POR COMPRESIÓN COMPLEJA ( ESTO PUEDE APLICARSE A UNA BASE DE DATOS)
Imagina que tienes una lista de listas, donde cada sublista representa la información de un 

producto: [nombre, precio, stock, categoría]. 

Queremos crear una nueva lista que contenga solo los nombres de los productos que cumplan ambas de las siguientes condiciones:
    * Su precio es mayor que 10 euros.
    * Su stock es mayor que 5 unidades o pertenecen a la categoría "Electrónica".

La nueva lista seria: 
productos_seleccionados = [producto[0].upper() for producto in productos if producto[1] > 10 and (producto[2] > 5 or producto[3] == "Electrónica")]

Llenaremos la lista con el nombre de los productos en mayúscula:    [producto[0].upper()
                                                                    producto tiene 4 elementos: 0-> nombre, 1 -> precio, 2-> stock y 3-> categoria.
                                                                    
luego nos pasearemos por cada producto en productos (for producto in productos )                                                                     

y aplicamos las condiciones: Si el precio es >10 y ( stock>5 o categoría=="Electrónica"

"""
# Definición de las variables de filtro
precio=80
nivel_stock=5
categoria="Electrónica"


productos = [
    ["Laptop"       , 1200  , 10    , "Electrónica"],
    ["Mouse"        , 25    , 50    , "Informática"],
    ["Teclado"      , 75    , 20    , "Informática"],
    ["Monitor"      , 300   , 8     ,"Electrónica"],
    ["Libro"        , 15    , 100   , "Libros"],
    ["Auriculares"  , 80    , 3     , "Electrónica"],
    ["Cargador"     , 30    , 15    , "Accesorios"]
]

productos_seleccionados = [
    producto[0].upper()  # Convertimos el nombre a mayúsculas
    for producto in productos
    if producto[1] > precio and (producto[2] > nivel_stock or producto[3] == categoria)
]

print("Tenemos los siguientes productos: ")
print(f"{'Nombre':<20}{'Precio':<10}{'Stock':<10}{'Tipo':<20}{'Cumple':<10}")
for producto in productos:
    print(f"{producto[0]:<20}{producto[1]:<10}{producto[2]:<10}{producto[3]:<20} {producto[1] > precio and (producto[2] > nivel_stock or producto[3] == categoria):<10}")

print(f'Selección, precio>{precio} y (stock>{nivel_stock} ó categoria={categoria}: {productos_seleccionados}')

"""  COMBINAR INFORMACIÓN DE 2 LISTAS  """

tallas =['S','M', 'L']
colores=['Rojo', 'Verde', 'Amarillo']

combinacion= [(color,talla) for color in colores for talla in tallas]
print("La combinacion de Color/Tallas es ", combinacion)

"""     APLANAR UNA MATRIZ   """
"""     Esta matriz esta compuesta por 3 listas asi a cada una la podemos referenciar como fila
        aunque le podemos dar el nombre que queramos.
        Aqui tenemos una Matriz que tiene 3 elementos, que los llamaremos fila  y dentro de la fila están los numeros 
        que nos interesa recuperar.
"""
matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

# Toma el número, que coincida con fila en la matriz y tomando el número en cada fila.
matriz_plana= [numero for fila in matriz for numero in fila]

print(matriz_plana)

"""   LISTA POR COMPRESION PARA LOCALIZAR LETRAS DENTRO DE UNA CADENA """

cadena = 'Listas por compresión en Python'

# La lista sera: caracter c en la cadena si caracteres es cualquiera de estos aeiouáéíóú
vocales=[c for c in cadena.lower() if c in 'aeiouáéíóú']
print(f'Las vocales en la cadena: {cadena} son: {vocales}')

"""   CONVERSION MASIVA DE CENIIGRADOS A CELCIUS """

celcius = [0,10, 20, 30, 40, 100]
farenheis = [ ( 9/5*temp+32) for temp in celcius]
print(f'La conversion de los celciuos: {celcius} a farenheis es {farenheis}')

