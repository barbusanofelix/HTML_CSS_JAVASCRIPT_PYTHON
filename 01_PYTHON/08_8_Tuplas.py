# TUPLAS
"""Una tupla es una colección ordenada e inmutable.
En Python, las tuplas se escriben entre paréntesis.
"""
print()
# Declaración de una tupla
miTupla = ("manzana", "banana", "cereza")
print(); print("imptimr posicion 1 que es banana:")
print(miTupla[1]) # banana
# Otra forma de declararla
print()
miTupla = tuple(("manzana", "banana","cereza"))
print("Imprime manzana,banana,cereza")
print(miTupla)
print()
# Indexación Negativa
miTupla = ("manzana", "banana", "cereza")
print( "Imprime la tupla [-1], es decir el ultimo que es Cereza")
print(miTupla[-1]) 
print()

print()
print("Recorrer la tupla en reverse")
for elemento in reversed(miTupla):
    print(elemento)

print()    
# Rango de índices
# Devuelve el tercer, cuarto y quinto elemento:
print("preparando impresion miTupla[2:5]")
miTupla = ("manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango")
print(miTupla)
print("Aqui el 2:5: 'cereza', 'naranja', 'kiwi' ,miTupla[2:5]) # es como si pide >=2 ( no lo incluye) hasta <5 , que es melon")
# Convierta la tupla en una lista para poder cambiarla:
print()
miTupla = ("manzana", "banana", "cereza")
print("Cambio mi Tupla a ", miTupla)
print()
print("Esto iniciando cambio con kiwi")
miLista = list(miTupla)
miLista[1] = "kiwi"  # sobreescrive el valor de de banana por kiwi
miTupla = tuple(miLista)  # Imprime manzana, kiwi y cereza
print("Aqui deberia salir: ",miTupla)
# Recorrer una tupla

print()
print("Recorrer a tupla manzana", "banana", "cereza")
miTupla = ("manzana", "banana", "cereza")
for x in miTupla:
    print(x)
# Comprobar si existe un elemento
# Compruebe si "manzana" está presente en la tupla:
print()
print("Esta manzana en la Tupla")
miTupla = ("manzana", "banana", "cereza")
if "manzana" in miTupla:
    print("Sí, 'manzana' está en la tupla.")
# Otra forma, simplemente con un boolean
print("manzana" in miTupla)
# Longitud de la tupla
print()
print("Asigno  una tupla con Manzana, banana, Cereza")
miTupla = ("manzana", "banana", "cereza")
print("Longitud de la tupla indicado:",len(miTupla))
# Unir dos tuplas
print()
print('Suma de Tuplas; tupla1 = ("a", "b" , "c") + tupla2 = (1, 2, 3)')
tupla1 = ("a", "b" , "c")
tupla2 = (1, 2, 3)
tupla3 = tupla1 + tupla2
print("Suma de Tupla: ", tupla3)
# Cuantas veces se encuentra el elemento 4 en miTupla?
print()

miTupla = ("manzana", "banana", "cereza", "manzana")
print( " Contar cuantas manzanas hay en la tupla en ", miTupla)
print("Manzana aparece :",miTupla.count("manzana"), "veces")
# Desempaquetdo de tupla
print()

miTupla=("Angel", 4, 5.345, True, 4)
print("Tenemos la Tupla", miTupla)
print(" Asignaremos la tupla a: nombre, num1, num2, valor1, num3=miTupla")
nombre, num1, num2, valor1, num3=miTupla
print("Entonces el desempacado quedara asi:")
print("Nombre: ",nombre)
print("num1 ", num1)
print("num2 ", num2)
print("Valor1 ", valor1)
print("num3 ", num3)
